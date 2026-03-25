---
tags: [architect-quest, p1, week-05]
status: in-progress
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
| 4 | Outbox Pattern (pubblicazione affidabile DB + Queue) | | Da fare |

---

## Tasks

### Preparazione Teorica (Day 1-2)
- [x] Teoria: Message Queue fundamentals (sincrono vs asincrono, 3 attori) ✅ 2026-03-25
- [x] Teoria: ACK/NACK, at-least-once delivery, idempotenza ✅ 2026-03-25
- [x] Teoria: Dead Letter Queue ✅ 2026-03-25
- [x] Quiz: Message Queue (13 quiz aggiunti al tracker) ✅ 2026-03-25
- [x] Teoria: RabbitMQ (Exchange types, Binding, Consumer) ✅ 2026-03-25
- [x] Teoria: BackgroundService .NET ✅ 2026-03-25
- [ ] Teoria: Outbox Pattern

### RabbitMQ Setup (Day 2-3)
- [ ] Aggiungi RabbitMQ al `docker-compose.yml`
- [ ] Verifica connessione a RabbitMQ Management UI (localhost:15672)
- [ ] Crea progetto o cartella per il Worker

### Astrazione Message Publisher (Day 3-4)
- [ ] Crea interfaccia `IMessagePublisher` in Application Layer
- [ ] Crea `NotificationScheduledMessage` (messaggio leggero con solo ID)
- [ ] Implementa `RabbitMqMessagePublisher` in Infrastructure
- [ ] Registra nel DI Container
- [ ] Scrivi unit test per il publisher

### Integrazione nell'Handler (Day 4-5)
- [ ] Modifica `ScheduleNotificationHandler`: dopo Save → Publish
- [ ] Aggiorna test esistenti dell'handler (mock di IMessagePublisher)
- [ ] Scrivi integration test (handler + queue)

### Notification Worker (Day 5-6)
- [ ] Crea `NotificationWorker` (BackgroundService)
- [ ] Implementa consumer RabbitMQ nel worker
- [ ] Logica: leggi messaggio → carica da DB → invia → aggiorna status → ACK
- [ ] Implementa check idempotenza (status == Sent → skip)
- [ ] Scrivi unit test per il worker
- [ ] Scrivi integration test (worker + DB + queue)

### Retry e Error Handling (Day 6-7)
- [ ] Configura retry policy (3 tentativi con backoff)
- [ ] Implementa NACK su fallimento
- [ ] Aggiorna RetryCount e status Failed nel DB
- [ ] Configura Dead Letter Queue base
- [ ] Test: simula fallimento e verifica retry

### Documentation (Day 7)
- [ ] Crea nota: RabbitMQ fundamentals
- [ ] Crea nota: BackgroundService .NET
- [ ] Aggiorna README con setup RabbitMQ
- [ ] ADR-004: Message Queue Strategy (RabbitMQ dev, Azure Service Bus prod)

---

## XP Disponibili

| Deliverable | XP | Status |
|-------------|-----|--------|
| Teoria + Note | +50 | In corso (+20 per message-queues.md) |
| RabbitMQ Setup | +30 | Da fare |
| IMessagePublisher + Implementazione | +80 | Da fare |
| Integrazione Handler | +60 | Da fare |
| Notification Worker | +100 | Da fare |
| Retry + Error Handling | +80 | Da fare |
| Documentation | +50 | Da fare |

**XP Guadagnati:** 0 / 450
**Meta Week 5:** 300 XP

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
