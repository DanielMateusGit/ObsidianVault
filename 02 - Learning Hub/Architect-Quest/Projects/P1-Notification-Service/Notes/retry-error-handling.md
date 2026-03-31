---
tags:
  - p1
  - architecture
  - messaging
  - reliability
  - error-handling
  - from/week-05
  - status/learning
aliases:
  - Retry Pattern
  - Error Handling
  - Dead Letter Queue
  - DLQ
  - Poison Message
created: 2026-03-28
source: "Sessione Week 5 - Retry + Error Handling"
---

# Retry + Error Handling — Gestione Fallimenti nel Messaging

> **One-liner:** Il Retry Pattern gestisce i fallimenti di invio con tentativi limitati, tracciati nel DB, usando l'Outbox per ripubblicare e la DLQ applicativa per i messaggi irrecuperabili.

---

## Architettura dei Componenti

Quattro attori collaborano per gestire i fallimenti:

- **Handler** — riceve la richiesta dal client, crea la Notification e un OutboxMessage nella stessa transazione DB. Non tocca mai RabbitMQ direttamente.
- **Outbox Processor** — ogni 5 secondi legge gli OutboxMessage con `ProcessedAt = NULL` e li pubblica su RabbitMQ. Fa da ponte tra DB e queue.
- **RabbitMQ** — contiene la queue `notification.send`. Il suo unico compito e consegnare i messaggi al Worker.
- **Worker** — consuma dalla queue, legge la notifica dal DB, tenta l'invio, e gestisce successo/fallimento/retry. E lui che decide se riprovare o arrendersi.

Il **DB PostgreSQL** ha 3 tabelle chiave:

| Tabella | Ruolo |
|---------|-------|
| `Notifications` | Stato della notifica (Pending/Sent/Failed), priority, errorMessage |
| `OutboxMessages` | Messaggi da pubblicare su RabbitMQ. `ProcessedAt = NULL` = da processare |
| `DeliveryAttempts` | Storico di ogni tentativo: numero, esito, errore. Audit trail completo |

```
Handler ──────► DB ◄────── Outbox Processor ──────► RabbitMQ ──────► Worker
(scrive)     (fonte        (legge outbox,            (queue)        (consuma,
              di verita)    pubblica)                                legge DB,
                                                                    invia,
                                                                    gestisce retry)

PostgreSQL:
┌──────────────┐  ┌──────────────┐  ┌─────────────────────┐
│ Notifications│  │OutboxMessages│  │  DeliveryAttempts   │
│              │  │              │  │                     │
│ id           │  │ id           │  │ id                  │
│ status       │  │ type         │  │ notificationId      │
│ errorMessage │  │ payload      │  │ attemptNumber       │
│ priority     │  │ processedAt  │  │ status (ok/fail)    │
└──────────────┘  └──────────────┘  │ errorMessage        │
                                    └─────────────────────┘
```

---

## Macchina a Stati della Notifica

Una notifica attraversa questi stati durante il suo ciclo di vita:

1. **PENDING** — stato iniziale. L'Handler ha creato la notifica, il Worker non l'ha ancora presa.
2. **PROCESSING** — il Worker sta tentando l'invio. Ha creato un DeliveryAttempt.
3. **SENT** — invio riuscito. Stato finale positivo. Fine del flusso.
4. **FAILED** — invio fallito. Qui si biforca:
   - **CanRetry = SI** → chiama `Retry()` che resetta lo stato a PENDING + crea un nuovo OutboxMessage. Il ciclo ricomincia.
   - **CanRetry = NO** → resta FAILED definitivamente. E la nostra **DLQ applicativa**: una query `WHERE Status = 'Failed'` mostra tutti i "messaggi morti".

La decisione `CanRetry` dipende dalla Priority (business rule nel Domain): il numero di tentativi gia fatti vs il massimo consentito.

```
PENDING ──► PROCESSING ──┬──► SENT (fine)
  ▲                       │
  │                       └──► FAILED ──► CanRetry?
  │                                         │    │
  │                              SI ◄───────┘    └──────► NO
  │                              │                        │
  └── Retry() + OutboxMessage ◄──┘                  FAILED (finale)
                                                    = DLQ applicativa
```

**Max retry per Priority (business rule nel Domain):**

| Priority | Max tentativi |
|----------|---------------|
| Low      | 2             |
| Normal   | 3             |
| High     | 5             |
| Critical | 10            |

---

## Flusso Dettagliato — SUCCESSO

Il percorso felice di una notifica, dal client alla casella email:

**Fase 1 — Handler (ricezione)**
1. Il client chiama `POST /notify`
2. L'Handler crea una `Notification` (status=Pending) e un `OutboxMessage` nella **stessa transazione** DB
3. `SaveChanges()` salva entrambi atomicamente
4. Il client riceve `201 Created` — la richiesta e accettata, l'invio e asincrono

**Fase 2 — Outbox Processor (ponte DB → Queue)**
5. Ogni 5 secondi, l'Outbox Processor cerca `OutboxMessages WHERE ProcessedAt = NULL`
6. Trova il nostro messaggio, lo pubblica su RabbitMQ
7. Aggiorna `ProcessedAt` con il timestamp — quel messaggio non verra piu ripubblicato

**Fase 3 — Worker (invio)**
8. Il Worker consuma il messaggio dalla queue
9. Legge la notifica dal DB (`GetById`) e conta i tentativi precedenti (`AttemptCount = 0`)
10. Crea un `DeliveryAttempt #1` e tenta l'invio (es. SMTP)
11. Invio riuscito → `attempt.MarkAsSuccess()`, `notification.Send()` (status=Sent)
12. `SaveChanges()` persiste tutto
13. Invia **ACK** a RabbitMQ → il messaggio viene rimosso dalla queue

```
CLIENT → HANDLER → DB (Notification + OutboxMessage, atomico)
                   ↓
         OUTBOX PROCESSOR → legge DB → Publish su RabbitMQ → segna ProcessedAt
                                        ↓
                              WORKER → consuma → legge DB → invia email
                                     → MarkAsSuccess → Send() → SaveChanges
                                     → ACK a RabbitMQ

Stato finale DB:
  Notification    → Status=Sent, SentAt=now
  DeliveryAttempt → #1, Status=Success
  OutboxMessage   → ProcessedAt=timestamp
```

---

## Flusso Dettagliato — FALLIMENTO + RETRY

Cosa succede quando l'invio fallisce ma ci sono ancora tentativi disponibili:

**Fase 1 — Tentativo fallito**
1. Il Worker consuma il messaggio, legge la notifica dal DB (status=Pending, AttemptCount=0)
2. Crea `DeliveryAttempt #1` e tenta l'invio
3. L'SMTP e giu → l'invio fallisce

**Fase 2 — Gestione del fallimento**
4. `attempt.MarkAsFailed("SMTP connection refused")` — segna il tentativo come fallito
5. `notification.Fail("SMTP connection refused")` — la notifica passa a status=Failed
6. Il Worker chiede: `CanRetry(attemptCount=1)?` → **SI** (per Priority Normal il max e 3)

**Fase 3 — Schedulare il retry**
7. `notification.Retry()` — **resetta lo status a Pending** (pronta per un nuovo giro)
8. `outboxStore.Add(nuovoMessaggio)` — crea un **nuovo** OutboxMessage con `ProcessedAt = NULL`
9. `SaveChanges()` — persiste tutto atomicamente
10. Invia **ACK** a RabbitMQ — il messaggio originale viene **rimosso** dalla queue

**Fase 4 — Retry automatico**
11. Dopo ~5 secondi, l'Outbox Processor trova il nuovo OutboxMessage
12. Lo pubblica su RabbitMQ → il Worker consuma un **nuovo** messaggio
13. Questa volta `AttemptCount = 1` → crea `DeliveryAttempt #2` e riprova

Il punto chiave: il retry **non** avviene tramite NACK+requeue di RabbitMQ. Il messaggio originale viene sempre ACKato. Il retry passa attraverso il DB (Retry → Outbox → RabbitMQ → Worker). Questo da il controllo totale: contatore persistente, backoff, regole di dominio.

```
WORKER: consuma → legge DB → Attempt #1 → SMTP DOWN!
  → MarkAsFailed → Fail → CanRetry(1)? SI
  → Retry() [status→Pending] → Add OutboxMessage → SaveChanges → ACK

OUTBOX PROCESSOR: trova nuovo OutboxMessage → Publish su RabbitMQ

WORKER: consuma (nuovo msg) → legge DB → AttemptCount=1 → Attempt #2 → riprova...

Stato DB dopo retry schedulato:
  Notification    → Status=Pending (resettato da Retry)
  DeliveryAttempt → #1, Status=Failed, Error="SMTP..."
  OutboxMessage#1 → ProcessedAt=timestamp (gia fatto)
  OutboxMessage#2 → ProcessedAt=NULL (pronto per Outbox Processor!)
```

---

## Flusso Dettagliato — RETRY ESAURITI (DLQ Applicativa)

Cosa succede quando una notifica Normal fallisce per la terza e ultima volta:

**Fase 1 — Ultimo tentativo**
1. Il Worker consuma il messaggio, legge la notifica dal DB
2. `AttemptCount = 2` (2 tentativi precedenti gia falliti)
3. Crea `DeliveryAttempt #3` e tenta l'invio
4. Fallisce di nuovo (es. "SMTP timeout")

**Fase 2 — Niente retry**
5. `attempt.MarkAsFailed("SMTP timeout")` — segna il tentativo come fallito
6. `notification.Fail("SMTP timeout")` — status=Failed
7. Il Worker chiede: `CanRetry(attemptCount=3)?` → **NO** (Normal ha max=3)
8. **NON** chiama `Retry()` — lo status resta Failed
9. **NON** crea un OutboxMessage — nessun nuovo messaggio per la queue
10. `SaveChanges()` → ACK a RabbitMQ

**Fase 3 — DLQ Applicativa**
La notifica resta nel DB con `Status = Failed` per sempre. Questa e la nostra **Dead Letter Queue applicativa**: non e una coda separata, ma una semplice query SQL.

Per monitoraggio e alerting:
```sql
SELECT * FROM notifications WHERE status = 'Failed'
```

Un operatore o un sistema di alerting puo monitorare questa query per intervenire manualmente (re-inviare, contattare il team infra, escalare).

```
WORKER: consuma → legge DB → AttemptCount=2 → Attempt #3 → FALLISCE
  → MarkAsFailed → Fail → CanRetry(3)? NO (Normal max=3)
  → NON chiama Retry(), NON crea OutboxMessage
  → SaveChanges → ACK → messaggio rimosso dalla queue per sempre

Stato DB finale:
  Notification    → Status=Failed, Error="SMTP timeout"
  DeliveryAttempt → #1 Failed, #2 Failed, #3 Failed
  OutboxMessages  → tutti con ProcessedAt (nessuno nuovo)
```

---

## Flusso Dettagliato — CRASH DEL WORKER

Il caso peggiore: il Worker muore nel mezzo del processing. Perche non perdiamo il messaggio?

**Fase 1 — Il crash**
1. Il Worker consuma il messaggio dalla queue
2. Legge la notifica dal DB, crea un DeliveryAttempt nel **Change Tracker** (in memoria)
3. Il Worker crasha (eccezione non gestita, OOM, kill del processo)

**Fase 2 — Conseguenze**
4. `SaveChanges()` **non** e mai stato chiamato → il DeliveryAttempt non e mai stato salvato nel DB. Nessuna traccia del crash.
5. `ACK` **non** e mai stato inviato a RabbitMQ

**Fase 3 — Recovery automatico**
6. RabbitMQ non riceve ACK entro il **visibility timeout** → considera il messaggio non processato
7. Il messaggio torna **available** nella queue (redelivery automatico)
8. Il Worker riparte e consuma lo **stesso** messaggio
9. Legge dal DB: `AttemptCount = 0` (il crash non ha lasciato traccia)
10. Riprocessa da zero, come se niente fosse successo

Questa e la garanzia **at-least-once delivery**: un messaggio viene processato almeno una volta. Il prezzo e che potrebbe essere processato due volte (se il crash avviene dopo l'invio email ma prima del SaveChanges), per questo serve il **check di idempotenza** (controlla `Status == Sent` prima di inviare).

```
WORKER: consuma → legge DB → crea Attempt (in memoria) → CRASH!
  → SaveChanges MAI chiamato → DB pulito, nessuna traccia
  → ACK MAI inviato → RabbitMQ aspetta timeout

RABBITMQ: timeout senza ACK → messaggio torna in coda

WORKER (ripartito): consuma STESSO messaggio → AttemptCount=0 → riprocessa da zero

= AT-LEAST-ONCE DELIVERY GARANTITO
```

---

## Pattern Alternativo: DLQ a livello RabbitMQ (NON implementato)

L'alternativa al nostro approccio e delegare tutto a RabbitMQ. Come funziona:

1. La queue `notification.send` e configurata con `x-dead-letter-exchange` e `x-dead-letter-routing-key`
2. Il Worker tiene un **contatore in memoria** dei tentativi
3. Tentativo 1 fallito → `NACK requeue=true` (RabbitMQ rimette in coda)
4. Tentativo 2 fallito → `NACK requeue=true`
5. Tentativo 3 fallito → `NACK requeue=false` → RabbitMQ sposta il messaggio nella **DLQ** (`notification.dlq`)
6. Un operatore monitora la DLQ via Management UI

**Il problema critico:** se il Worker crasha, il contatore in-memory si perde. Al restart, riparte da tentativo 1. Potenzialmente un loop infinito di retry.

```
Producer → notification.send (con x-dead-letter-exchange configurato)
              ↓
         Worker (contatore in memoria)
         tentativo 1: NACK requeue=true → torna in coda
         tentativo 2: NACK requeue=true → torna in coda
         tentativo 3: NACK requeue=false → va in notification.dlq

PROBLEMA: Worker crash → contatore perso → riparte da 1 → loop infinito
```

### Confronto: DLQ RabbitMQ vs DLQ Applicativa

| Aspetto | DLQ RabbitMQ | DLQ Applicativa (nostra scelta) |
|---------|-------------|-------------------------------|
| **Contatore retry** | In-memory nel Worker. Si perde al crash | `COUNT(DeliveryAttempts)` nel DB. Persistente, sopravvive ai crash |
| **Backoff** | Nessuno nativo (torna subito in coda) | Controllabile (delay nell'Outbox Processor o TTL sul messaggio) |
| **Dove sono i "morti"** | Queue `notification.dlq` (serve RabbitMQ UI) | `SELECT * FROM notifications WHERE status = 'Failed'` (stesso DB, stessi tool) |
| **Debug** | Payload JSON nella queue (poco contesto) | DeliveryAttempts con timestamp, error message, durata per ogni tentativo |
| **Quando usarla** | Sistemi senza Outbox, microservizi stateless con logica semplice | Sistemi con Outbox Pattern, quando serve audit trail, retry controllato, visibilita DB |

---

## Cos'e

Il Retry Pattern con DLQ applicativa e una strategia di error handling che:
1. **Traccia ogni tentativo** nel DB (DeliveryAttempt)
2. **Limita i retry** in base alla priority (business rule nel Domain)
3. **Ripubblica tramite Outbox** per riprovare (non NACK+requeue)
4. **Marca come Failed** quando i retry sono esauriti (DLQ applicativa)
5. **Fa sempre ACK** su RabbitMQ (il messaggio e "gestito", anche se con errore)

## Quando usarlo

- Invio a sistemi esterni inaffidabili (SMTP, SMS provider, webhook)
- Quando serve tracciabilita di ogni tentativo (audit, SLA)
- Quando hai gia un Outbox Pattern
- Quando le regole di retry dipendono dal dominio (priority, tipo notifica)

## Quando NON usarlo

- Processing idempotente che puo semplicemente riprovare (NACK+requeue basta)
- Sistemi con pochissimi fallimenti (overengineering)
- Quando non hai un DB (worker stateless puri → usa DLQ RabbitMQ)

---

## Collegamenti

- [[outbox-pattern|Outbox Pattern — Pubblicazione Affidabile DB + Queue]]
- [[message-queues|Message Queue — Architettura Event-Driven]]
- [[rabbitmq-fundamentals|RabbitMQ Fundamentals]]
- [[background-service|BackgroundService in .NET]]

---

## Quiz

### Q1: Perche il Worker fa sempre ACK anche quando l'invio fallisce?

Perche il fallimento e gestito a livello applicativo (DB). Il messaggio e stato "processato" — il retry avviene tramite un nuovo OutboxMessage, non tramite NACK+requeue. Se facessimo NACK+requeue senza contatore persistente, rischieremmo un loop infinito.

### Q2: Una notifica Normal fallisce al tentativo 3. Cosa succede?

`CanRetry(3)` ritorna false (max 3 per Normal). La notifica resta in stato Failed nel DB. Nessun OutboxMessage creato, nessun retry. Il messaggio RabbitMQ viene ACKato. La notifica e nella "DLQ applicativa" (query: `WHERE status = 'Failed'`).

### Q3: Il Worker crasha dopo Fail() ma prima di SaveChanges(). Cosa succede?

Niente e stato salvato nel DB (nessun DeliveryAttempt, nessun Fail). L'ACK non e stato inviato. RabbitMQ rimette il messaggio in coda dopo il timeout. Il Worker lo riprocessa da zero. At-least-once delivery garantito.

### Q4: Perche la DLQ applicativa e meglio della DLQ RabbitMQ per il nostro caso?

Perche il contatore retry nel DB sopravvive ai crash, abbiamo audit trail completo (DeliveryAttempts), possiamo fare query SQL per monitoring, e le regole di retry sono nel Domain (dipendono da Priority). La DLQ RabbitMQ perde il contatore al crash del Worker.
