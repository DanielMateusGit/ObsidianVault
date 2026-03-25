---
tags:
  - p1
  - architecture
  - messaging
  - rabbitmq
  - from/week-05
  - status/learning
aliases:
  - RabbitMQ
  - Exchange
  - AMQP
created: 2026-03-25
source: "Sessione Week 5 - RabbitMQ Fundamentals"
---

# RabbitMQ — Fondamentali

> **One-liner:** RabbitMQ e un message broker che smista messaggi dai produttori alle queue attraverso Exchange, Binding e Routing Key, permettendo disaccoppiamento totale tra chi pubblica e chi consuma.

---

## Il Flusso in RabbitMQ

A differenza di altri sistemi dove il produttore manda direttamente alla coda, in RabbitMQ il messaggio passa prima da un **Exchange**:

```
Producer → Exchange → Binding → Queue → Consumer
```

Il produttore non sa (e non deve sapere) quante queue esistono o chi le ascolta. Disaccoppiamento totale.

---

## I 4 Componenti

### 1. Exchange (Lo Smistatore)

Riceve tutti i messaggi e decide in quale queue smistarli, in base alla **routing key** (un'etichetta sul messaggio).

```
Producer: "Messaggio con routing key = notification.scheduled"
Exchange: "Queue A e legata con pattern notification.* → lo metto li"
```

**4 tipi di Exchange:**

| Tipo | Comportamento | Analogia | Quando usarlo |
|------|--------------|----------|---------------|
| **Direct** | Routing key esatta | Lettera con indirizzo preciso | 1 queue per tipo di messaggio |
| **Fanout** | Broadcast a tutte le queue | Altoparlante in ufficio | Tutti devono ricevere tutto |
| **Topic** | Pattern matching con wildcard | Canali Reddit per argomento | Queue diverse per sottotipi |
| **Headers** | Basato su attributi header | (raramente usato) | Casi molto specifici |

**Wildcard nel Topic Exchange:**
- `*` = esattamente 1 parola → `notification.*` matcha `notification.scheduled` ma NON `notification.email.scheduled`
- `#` = 0 o piu parole → `notification.#` matcha tutto cio che inizia con `notification.`

**Per il nostro progetto:** Direct Exchange per iniziare (1 queue sola). Topic se in futuro servono queue separate per canale (email.*, sms.*, push.*).

### 2. Queue (La Coda)

Il buffer dove i messaggi aspettano di essere consumati.

```
Queue: "notification-processing"
  ┌──────────────────────────────────────┐
  │ MSG-5 │ MSG-4 │ MSG-3 │ MSG-2 │ MSG-1│
  └──────────────────────────────────────┘
    ← entra                      esce →
```

Proprieta importanti:
- **Nome** — identificativo univoco (es. `notification-processing`)
- **Durable** — se `true`, sopravvive al restart di RabbitMQ
- **Dead Letter Exchange** — dove vanno i messaggi dopo N retry falliti

### 3. Binding (La Regola di Collegamento)

Collega un Exchange a una Queue con una routing key. Senza binding, l'Exchange non sa dove mandare i messaggi.

```
Exchange ──── Binding (routing key: "notification.scheduled") ──── Queue
```

**Un Exchange puo avere piu binding:**

```
                          ┌── binding (notification.scheduled) ── Queue: processing
                          │
Exchange (topic) ─────────┤
                          │
                          └── binding (notification.sent) ─────── Queue: analytics
```

Cosi lo stesso Exchange smista messaggi diversi a queue diverse, in base alla routing key.

### 4. Consumer (Il Worker)

Si "iscrive" a una queue e riceve messaggi. Configurazioni:
- **Prefetch count** — quanti messaggi ricevere prima di fare ACK (controlla il parallelismo)
- **ACK mode** — manuale (noi controlliamo) o automatico (sconsigliato in produzione)

**Piu consumer sulla stessa queue = load balancing automatico (round-robin):**

```
                         ┌─── Consumer 1 (Worker)
                         │
Queue: processing ───────┤─── Consumer 2 (Worker)
                         │
                         └─── Consumer 3 (Worker)

RabbitMQ distribuisce i messaggi tra i 3 worker
```

Per scalare basta avviare piu istanze del worker (Docker Compose `replicas: 3`, Kubernetes). Il codice non cambia.

**NOTA:** RabbitMQ NON crea worker automaticamente. Fa solo load balancing tra i consumer gia connessi. L'orchestrazione (creare/distruggere worker) spetta a Docker/Kubernetes.

---

## Flusso Completo nel Notification Service

```
ScheduleNotificationHandler                    RabbitMQ
         │                                        │
         │── Publish(msg) ───────────────────────→│
         │   routing key: "notification.scheduled" │
         │                                        │
         │                              ┌─────────▼──────────┐
         │                              │  Exchange (direct)  │
         │                              │  "notification"     │
         │                              └─────────┬──────────┘
         │                                        │
         │                              binding: "notification.scheduled"
         │                                        │
         │                              ┌─────────▼──────────┐
         │                              │  Queue              │
         │                              │  "notification-     │
         │                              │   processing"       │
         │                              └─────────┬──────────┘
         │                                        │
         │                              ┌─────────▼──────────┐
         │                              │  Consumer           │
         │                              │  (NotificationWorker│
         │                              │   BackgroundService)│
         │                              └────────────────────┘
```

---

## Quando Entra in Gioco il DB

DB e RabbitMQ sono completamente separati. Il codice li collega:

```
PRIMA della Queue (Handler API):
  1. Salva notifica nel DB (Pending)
  2. Pubblica messaggio in Queue (solo ID)
  3. Risponde al client

DOPO la Queue (Worker):
  1. Riceve messaggio (solo ID)
  2. Carica notifica dal DB (dettagli completi)
  3. Controlla status == Sent (idempotenza)
  4. Invia email/SMS
  5. Aggiorna status nel DB (Sent/Failed)
  6. ACK alla queue
```

**Visualizzazione temporale:**

```
Tempo →

  DB:    ──[Save Pending]──────────────────────[Read]───[Update Sent]──
                │                                  ↑          │
  Queue:        └──[Publish msg]──[msg in coda]────│──────────│────[ACK → rimosso]
                                        │          │          │
  Worker:                               └──[Riceve]┘──[Invia]─┘
```

**Caso problematico:** Se l'Handler salva nel DB ma la pubblicazione in queue fallisce → la notifica e Pending nel DB ma nessun worker la processera. Soluzione: **Outbox Pattern** (topic separato, post flusso base).

---

## Persistenza dei Messaggi

RabbitMQ gira in RAM — se crasha, i messaggi si perdono. Per evitarlo, TUTTE e tre le cose devono essere persistenti:

| Cosa | Come |
|------|------|
| **Queue** | `durable: true` |
| **Messaggio** | `deliveryMode: persistent` |
| **Exchange** | `durable: true` |

Se la queue e durable ma il messaggio no → il messaggio si perde al restart.

---

## RabbitMQ in Docker

```yaml
rabbitmq:
  image: rabbitmq:3-management    # include la UI di gestione
  ports:
    - "5672:5672"                  # AMQP (protocollo messaggi)
    - "15672:15672"                # Management UI (browser)
  environment:
    RABBITMQ_DEFAULT_USER: guest
    RABBITMQ_DEFAULT_PASS: guest
```

**Management UI** (http://localhost:15672): vedi queue, messaggi in attesa, consumer connessi, rate invio/ricezione. Utilissima per debug.

---

## Quiz

### Q1: Perche l'Exchange? (RMQ-01)
Perche il produttore manda il messaggio all'Exchange e non direttamente alla Queue? Che vantaggio da?

**Mia risposta:**

---

### Q2: Topic Exchange (RMQ-02)
Vuoi una queue separata per email e una per SMS. Quale tipo di Exchange usi e come configuri i binding?

**Mia risposta:**

---

### Q3: Scaling Worker (RMQ-03)
1 queue, 1 worker, 1000 msg/s in arrivo ma il worker processa 100/s. Come risolvi? RabbitMQ crea worker automaticamente?

**Mia risposta:**

---

### Q4: Persistenza (RMQ-04)
Queue `durable: true`, messaggio senza `deliveryMode: persistent`. RabbitMQ crasha e riparte. Cosa succede ai messaggi in coda?

**Mia risposta:**

---

### Q5: Binding multipli (RMQ-05)
Un Exchange di tipo Topic ha 3 binding: `email.*`, `sms.*`, `push.*` verso 3 queue diverse. Il produttore pubblica con routing key `email.scheduled`. Quante queue ricevono il messaggio? Quali?

**Mia risposta:**

---

### Q6: Direct vs Fanout (RMQ-06)
Hai un evento `NotificationSent` e vuoi che sia il servizio Analytics SIA il servizio Billing lo ricevano. Direct o Fanout? Perche?

**Mia risposta:**

---

### Q7: Consumer e Prefetch (RMQ-07)
Il prefetch count del consumer e impostato a 10. Cosa significa in pratica? Cosa succede se lo imposti a 1?

**Mia risposta:**

---

## Risorse

- [RabbitMQ Tutorials](https://www.rabbitmq.com/tutorials) - Tutorial ufficiali (1-6)
- [RabbitMQ Concepts](https://www.rabbitmq.com/tutorials/amqp-concepts) - Exchange types, binding, routing
- [CloudAMQP Blog](https://www.cloudamqp.com/blog/part1-rabbitmq-for-beginners-what-is-rabbitmq.html) - Intro visuale eccellente
