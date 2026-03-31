---
tags:
  - p1
  - architecture
  - messaging
  - reliability
  - from/week-05
  - status/learning
aliases:
  - Outbox Pattern
  - Transactional Outbox
  - Dual Write Problem
created: 2026-03-27
source: "Sessione Week 5 - Outbox Pattern"
---

# Outbox Pattern — Pubblicazione Affidabile DB + Queue

> **One-liner:** L'Outbox Pattern risolve il Dual Write Problem scrivendo messaggi e dati nella stessa transazione DB, delegando la pubblicazione in coda a un processo separato.

---

## Il Problema: Dual Write

Quando devi scrivere su **due sistemi diversi** (DB + Message Queue), non puoi fare una transazione atomica tra loro. Non esiste un `BEGIN TRANSACTION` che copra sia PostgreSQL che RabbitMQ. Sono due sistemi completamente indipendenti.

Questo crea due scenari di fallimento, entrambi pericolosi:

**Scenario A — Save-then-Publish:** L'Handler salva nel DB, poi prova a pubblicare in RabbitMQ. Se RabbitMQ e giu, il Publish fallisce. Risultato: la notifica esiste nel DB ma nessun messaggio e in coda. Il Worker non la processera mai. Notifica "fantasma" nel DB.

**Scenario B — Publish-then-Save:** L'Handler pubblica in RabbitMQ, poi prova il SaveChanges. Se il DB rifiuta (constraint violation, timeout), il messaggio e gia in coda. Risultato: il Worker riceve il messaggio, cerca la notifica nel DB... non esiste. Messaggio "orfano" nella queue.

```
Scenario A: Handler → SaveChanges ✅ → Publish ❌ (RabbitMQ down)
  → Notifica nel DB, nessun messaggio in coda. Worker non la processa MAI.

Scenario B: Handler → Publish ✅ → SaveChanges ❌ (constraint violation)
  → Worker riceve messaggio, cerca nel DB... non esiste. Errore.
```

**Anche mettendo il Publish "dentro" il blocco della transazione**, RabbitMQ resta un servizio esterno — non partecipa al ROLLBACK del DB. Se fai Publish e poi il DB fallisce, il messaggio e gia in RabbitMQ e non puoi "ritirarlo".

---

## La Soluzione: Scrivi SOLO sul DB

L'intuizione chiave: **elimina uno dei due sistemi dalla scrittura**. L'Handler non tocca mai RabbitMQ. Scrive tutto nel DB, in una sola transazione atomica. Un processo separato (Outbox Processor) si occupa di spostare i messaggi dal DB alla queue.

**Fase 1 — Handler (una sola transazione)**
1. L'Handler riceve la richiesta dal client
2. Crea una `Notification` (status=Pending) nel DB
3. Crea un `OutboxMessage` (con il payload serializzato) nello **stesso** DbContext
4. Chiama `SaveChangesAsync()` — EF Core salva entrambi in un'unica transazione SQL
5. O **entrambi** vengono salvati, o **nessuno**. Atomicita garantita dal DB.

**Fase 2 — Outbox Processor (background, ogni N secondi)**
1. Legge tutti gli `OutboxMessages` con `ProcessedAt IS NULL`
2. Per ogni messaggio: lo pubblica su RabbitMQ
3. Aggiorna `ProcessedAt = NOW()` — quel messaggio non verra ripubblicato
4. Ripete il ciclo ogni 5 secondi

```
HANDLER (transazione atomica):
  INSERT Notification + INSERT OutboxMessage → SaveChanges
  → O entrambi o nessuno. RabbitMQ non e coinvolto.

OUTBOX PROCESSOR (ogni 5s):
  SELECT OutboxMessages WHERE ProcessedAt IS NULL
  → Per ognuno: Publish su RabbitMQ → UPDATE ProcessedAt = NOW()
```

### Perche funziona

Analizziamo tutti i possibili fallimenti:

- **SaveChanges fallisce** → nessun record in nessuna tabella. Niente Notification, niente OutboxMessage. Perfettamente consistente — come se la richiesta non fosse mai arrivata.
- **SaveChanges ha successo** → entrambi i record esistono. L'OutboxProcessor prima o poi trovera l'OutboxMessage e lo pubblichera. Il messaggio non puo andare perso finche il DB e vivo.
- **OutboxProcessor crasha dopo Publish, prima di UPDATE ProcessedAt** → al prossimo giro trova lo stesso messaggio (ProcessedAt ancora NULL) e lo ripubblica. Messaggio duplicato in coda, ma il Worker e idempotente (check `status == Sent` → skip). At-least-once delivery, nessun messaggio perso.

---

## La tabella OutboxMessage

La tabella Outbox e semplice di proposito. Ogni riga e un messaggio da pubblicare:

- **Type** — il tipo di evento (es. `"NotificationScheduled"`). Serve all'Outbox Processor per sapere su quale exchange/routing key pubblicare.
- **Payload** — il contenuto serializzato in JSON (es. l'ID della notifica). Contiene solo l'ID, non tutti i dati — il Worker leggera i dettagli dal DB.
- **OccurredAt** — quando e stato creato. Utile per debug e ordinamento.
- **ProcessedAt** — la chiave del pattern. `NULL` = da processare. Quando l'Outbox Processor pubblica con successo, segna il timestamp. Una query `WHERE ProcessedAt IS NULL` trova tutti i messaggi in attesa.

```csharp
public class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; }        // "NotificationScheduled"
    public string Payload { get; set; }     // JSON serializzato (solo ID)
    public DateTime OccurredAt { get; set; }
    public DateTime? ProcessedAt { get; set; } // NULL = da processare
}
```

---

## Quando usarlo

- Devi scrivere su DB + message broker nella stessa operazione
- La consistenza e critica (notifiche, pagamenti, ordini)
- Hai gia un DB relazionale

## Quando NON usarlo

- Stai solo leggendo (query) — non c'e dual write
- Il sistema tollera messaggi persi (analytics, logging non critico)
- Usi un DB con Change Data Capture nativo (MongoDB Change Streams, Debezium su PostgreSQL)

## Trade-off

| Pro | Contro |
|-----|--------|
| Consistenza garantita | Latenza aggiuntiva (polling) |
| Nessuna transazione distribuita | Tabella Outbox cresce, serve cleanup |
| Semplice da implementare | Complessita nell'OutboxProcessor |
| Funziona con qualsiasi broker | Messaggi duplicati possibili (serve idempotenza) |

---

## Alternativa scartata: Publish-then-Save con compensazione

L'idea: prima pubblichi il messaggio, poi salvi nel DB. Se il DB fallisce, pubblichi un secondo messaggio di "compensazione" che dice al Worker di ignorare il primo.

Perche non funziona:

1. **La compensazione puo fallire** — se anche il secondo Publish fallisce, hai un messaggio orfano in coda e nessun modo di ritirarlo. Due fallimenti in cascata.
2. **Race condition** — il Worker potrebbe processare il primo messaggio prima che arrivi la compensazione. Ha gia tentato l'invio, gia modificato lo stato. Troppo tardi.
3. **Complessita inutile** — stai costruendo un sistema di compensazione distribuita per risolvere un problema che l'Outbox elimina alla radice scrivendo su un solo sistema.

```
Publish ✅ → SaveChanges ❌ → Publish compensazione...
  → Ma se anche questa fallisce? Messaggio orfano.
  → E se il Worker processa prima della compensazione? Race condition.

Outbox: scrivi solo sul DB → problema eliminato alla radice.
```

---

## Collegamenti

- [[message-queues|Message Queue — Architettura Event-Driven]]
- [[rabbitmq-fundamentals|RabbitMQ Fundamentals]]
- [[background-service|BackgroundService in .NET]]
- [[unit-of-work-pattern|Unit of Work Pattern]] — stessa idea di transazione atomica
- [[domain-events-theory|Domain Events]] — dispatching affidabile

---

## Quiz

### Q1: Perche NON possiamo mettere il Publish dentro la transazione DB?

Perche RabbitMQ e un servizio esterno che non partecipa al ROLLBACK del DB. Sono due sistemi indipendenti senza transazione distribuita.

✅ **Corretto** — Non esiste un `BEGIN TRANSACTION` che copra DB + broker.

---

### Q2: OutboxProcessor pubblica e crasha prima di aggiornare ProcessedAt. Problema?

No. Al prossimo giro riprova il Publish (messaggio duplicato), ma il Worker e idempotente — check status == Sent → skip.

✅ **Corretto** — At-least-once delivery + idempotenza = nessun problema.

---

### Q3: Perche l'Outbox e meglio della compensazione (Publish-then-Save)?

La compensazione puo fallire, c'e race condition, e aggiunge complessita. L'Outbox elimina il problema alla radice scrivendo su un solo sistema.

✅ **Corretto** — Una tabella SQL batte un sistema di compensazione distribuita.
