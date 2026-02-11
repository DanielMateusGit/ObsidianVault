---
tags: [architect-quest, p1, week-02]
status: in-progress
xp_available: 350
xp_earned: 365
---

# 📅 Week 2: Domain Model

## 🎯 Obiettivo
Creare le core entities del Domain layer (Notification, Template, DeliveryAttempt).

## 📋 Tasks

### Preparazione Teorica (Day 1)
- [x] Teoria: Entities vs Value Objects ✅ 2026-02-09
- [ ] Teoria: Domain Events
- [x] Teoria: Rich Domain Model vs Anemic Domain Model ✅ 2026-02-09
- [x] Quiz: Domain Model Fundamentals (nella nota) ✅ 2026-02-09

### Entity: Notification (Day 2-3)
- [x] Crea `Notification` entity ✅ 2026-02-09
  - Properties: Id, Recipient, Channel, Content, Status, Priority, Timestamps
  - Methods: Schedule(), Send(), Fail(), Cancel()
- [x] Crea enum `NotificationStatus` (Pending, Sent, Failed, Cancelled) ✅ 2026-02-09
- [x] Crea enum `NotificationChannel` (Email, SMS, Push, Webhook) ✅ 2026-02-09
- [x] Crea enum `Priority` (Low, Normal, High, Critical) ✅ 2026-02-09
- [x] Scrivi unit test per `Notification` behaviors ✅ 2026-02-09 (31 tests)

### Entity: Template (Day 3-4)
- [x] Crea `Template` entity ✅ 2026-02-10
  - Properties: Id, Name, Channel, Subject, Body, IsActive
  - Methods: Render(data), Activate(), Deactivate(), UpdateContent(), GetPlaceholders()
- [x] Crea `TemplateData` value object (per i placeholder) ✅ 2026-02-10
- [x] Scrivi unit test per `Template.Render()` ✅ 2026-02-10 (39 tests: 20 Template + 19 TemplateData)

### Entity: DeliveryAttempt (Day 4-5)
- [x] Crea `DeliveryAttempt` entity ✅ 2026-02-10
  - Properties: Id, NotificationId, AttemptNumber, Status, ErrorMessage, AttemptedAt, CompletedAt
  - Methods: MarkAsSuccess(), MarkAsFailed(errorMessage), GetDuration()
- [x] Crea enum `DeliveryStatus` (InProgress, Success, Failed) ✅ 2026-02-10
- [x] Scrivi unit test per retry logic ✅ 2026-02-10 (24 tests)

### Value Objects (Day 5-6)
- [x] Crea `Recipient` value object (con validazione) ✅ 2026-02-10
- [x] Crea `EmailAddress` value object ✅ 2026-02-10
- [x] Crea `PhoneNumber` value object ✅ 2026-02-10
- [x] Scrivi unit test per Value Objects ✅ 2026-02-10 (71 tests)

### Domain Events (Day 6-7)
- [ ] Crea `NotificationScheduledEvent`
- [ ] Crea `NotificationSentEvent`
- [ ] Crea `NotificationFailedEvent`
- [ ] Aggiungi meccanismo domain events alle entities

### Documentation (Day 7)
- [ ] Scrivi ADR-002: "Rich Domain Model vs Anemic"
- [ ] Aggiungi C4 Container Diagram
- [ ] Aggiorna README con Domain Model overview

## 📖 Letture Obbligatorie

**Durante la settimana:**
- [ ] "Clean Architecture" Cap. 20-22 (Entities)
- [ ] Martin Fowler: Domain Model Pattern

**Opzionali:**
- "Domain-Driven Design Distilled" Cap. 5 (Entities)

## 📝 Note di Sessione

### 2026-02-09 - Kickoff Week 2 + Notification Entity
**Durata:** ~3h
**XP guadagnati:** +185 totali

**Completato:**
- Challenge del giorno (DIP-03) ✅ (+15 XP)
- Lettura Clean Architecture Cap. 20-22 ✅ (+30 XP)
- Nota completa: Entities + Clean Architecture ✅ (+60 XP)
  - Esempio end-to-end BankAccount
  - Sezione Purista vs Pragmatico
  - 6 quiz con risposte
- **Notification entity implementata** ✅ (+80 XP)
  - 3 enum (Status, Channel, Priority)
  - Entity completa con business rules
  - 31 unit test (tutti verdi!)
  - Commit e push su GitHub

**Prossimi passi:**
- Template entity
- DeliveryAttempt entity
- Value Objects (Recipient, EmailAddress, PhoneNumber)

## ✅ XP

| Deliverable | XP | Status |
|-------------|-----|--------|
| Notification entity + tests | +80 | ✅ 2026-02-09 |
| Template entity + tests | +70 | ✅ 2026-02-10 |
| DeliveryAttempt entity + tests | +60 | ✅ 2026-02-10 |
| Value Objects + tests | +50 | ✅ 2026-02-10 |
| Domain Events | +40 | ⬜ |
| ADR-002 | +30 | ⬜ |
| C4 Container Diagram | +20 | ⬜ |

**Totale disponibile:** 350 XP

**Meta Week 2:** 175 XP per sbloccare Week 3

[[Week-01|← Week 1]] | [[Week-03|Week 3 →]]
