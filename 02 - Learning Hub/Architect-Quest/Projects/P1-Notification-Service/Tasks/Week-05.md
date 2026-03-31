---
tags: [architect-quest, p1, week-05]
status: complete
started: 2026-03-25
xp_available: 450
xp_earned: 0
---

# Week 5: Message Queue — Event-Driven Architecture

## Obiettivo
Introdurre una message queue per processare le notifiche in modo asincrono e affidabile, con RabbitMQ in dev e astrazione per Azure Service Bus in produzione.

---

## Teoria da Completare (PRIMA del codice!)

| # | Argomento | Nota | Status |
|---|-----------|------|--------|
| 1 | Message Queue: cos'e, perche, DB vs Queue vs Worker | `Notes/message-queues.md` | ✅ 2026-03-25 |
| 2 | RabbitMQ: concetti (Exchange, Queue, Binding, Consumer) | `Notes/rabbitmq-fundamentals.md` | ✅ 2026-03-25 |
| 3 | BackgroundService in .NET (IHostedService, Worker pattern) | `Notes/background-service.md` | ✅ 2026-03-25 |
| 4 | Outbox Pattern (pubblicazione affidabile DB + Queue) | `Notes/outbox-pattern.md` | ✅ 2026-03-27 |

---

## Tasks

### Preparazione Teorica (Day 1-2)
- [x] Teoria: Message Queue fundamentals (sincrono vs asincrono, 3 attori) ✅ 2026-03-25
- [x] Teoria: ACK/NACK, at-least-once delivery, idempotenza ✅ 2026-03-25
- [x] Teoria: Dead Letter Queue ✅ 2026-03-25
- [x] Quiz: Message Queue (13 quiz aggiunti al tracker) ✅ 2026-03-25
- [x] Teoria: RabbitMQ (Exchange types, Binding, Consumer) ✅ 2026-03-25
- [x] Teoria: BackgroundService .NET ✅ 2026-03-25
- [x] Teoria: Outbox Pattern ✅ 2026-03-27

### RabbitMQ Setup (Day 2-3)
- [x] Aggiungi RabbitMQ al `docker-compose.yml` ✅ (gia presente)
- [x] Verifica connessione a RabbitMQ Management UI (localhost:15672) ✅ 2026-03-28
- [x] Crea progetto o cartella per il Worker ✅ (gia presente)

### Astrazione Message Publisher (Day 3-4)
- [x] Crea interfaccia `IMessagePublisher` in Application Layer ✅ (gia presente)
- [x] Crea `NotificationScheduledMessage` (messaggio leggero con solo ID) ✅ (SendNotificationMessage)
- [x] Implementa `RabbitMqMessagePublisher` in Infrastructure ✅ (+ overload routing key)
- [x] Registra nel DI Container ✅
- [x] Scrivi unit test per il publisher ✅ (testato via OutboxProcessor)

### Integrazione nell'Handler (Day 4-5)
- [x] Modifica `ScheduleNotificationHandler`: Outbox Pattern ✅ 2026-03-27
- [x] Aggiorna test esistenti dell'handler (mock di IOutboxStore) ✅ 2026-03-27
- [x] Scrivi integration test (outbox + DB PostgreSQL) ✅ 2026-03-28

### Outbox Pattern
- [x] OutboxMessage + EF Core config + migration ✅ 2026-03-27
- [x] IOutboxStore (Application) + OutboxStore (Infrastructure) ✅ 2026-03-27
- [x] OutboxProcessor BackgroundService ✅ 2026-03-27
- [x] Unit test OutboxStore (6 test) ✅ 2026-03-28
- [x] Unit test OutboxProcessor (7 test) ✅ 2026-03-28
- [x] Integration test Outbox + PostgreSQL (3 test) ✅ 2026-03-28

### Notification Worker (Day 5-6)
- [x] Crea `NotificationWorker` (BackgroundService) ✅ (gia presente)
- [x] Implementa consumer RabbitMQ nel worker ✅ (gia presente)
- [x] Logica: leggi messaggio → carica da DB → invia → aggiorna status → ACK ✅
- [x] Implementa check idempotenza (status == Sent → skip) ✅
- [x] Scrivi unit test per il worker (5 test) ✅ 2026-03-28

### Retry e Error Handling (Day 6-7)
- [x] IDeliveryAttemptRepository + PostgresDeliveryAttemptRepository ✅ 2026-03-28
- [x] Retry logic nel Worker (DeliveryAttempt + CanRetry + Outbox) ✅ 2026-03-28
- [x] ACK sempre (retry via Outbox, non NACK+requeue) ✅ 2026-03-28
- [x] DLQ applicativa (Failed nel DB, query per monitoring) ✅ 2026-03-28
- [x] Test retry/failure (worker tests) ✅ 2026-03-28

### Documentation (Day 7)
- [x] Crea nota: RabbitMQ fundamentals ✅ 2026-03-25
- [x] Crea nota: BackgroundService .NET ✅ 2026-03-25
- [x] Crea nota: Outbox Pattern ✅ 2026-03-27
- [x] Crea nota: Retry + Error Handling ✅ 2026-03-28
- [x] Aggiorna README con setup RabbitMQ ✅ 2026-03-28
- [x] ADR-004: Message Queue Strategy ✅ 2026-03-28

---

## XP Disponibili

| Deliverable | XP | Status |
|-------------|-----|--------|
| Teoria + Note (4 note) | +50 | ✅ |
| RabbitMQ Setup | +30 | ✅ |
| IMessagePublisher + Implementazione | +80 | ✅ |
| Integrazione Handler (Outbox) | +60 | ✅ |
| Notification Worker | +100 | ✅ |
| Retry + Error Handling | +80 | ✅ |
| Documentation (ADR-004 + README) | +50 | ✅ |

**XP Guadagnati:** 450 / 450 ✅ WEEK COMPLETATA
**Meta Week 5:** 300 XP → superata!

---

## Letture Obbligatorie

**Durante la settimana:**
- [ ] RabbitMQ Tutorials (1-3) — Getting started, Work Queues, Pub/Sub
- [ ] Microsoft Docs — BackgroundService in .NET
- [ ] Enterprise Integration Patterns — Message Channel, Dead Letter Channel
- [ ] Azure Service Bus Overview (per capire il target produzione)

**Opzionali:**
- MassTransit Documentation (libreria .NET per message bus)
- Outbox Pattern — Reliable messaging

---

## Collegamenti

[[Week-04|← Week 4]] | [[Week-06|Week 6 →]]
