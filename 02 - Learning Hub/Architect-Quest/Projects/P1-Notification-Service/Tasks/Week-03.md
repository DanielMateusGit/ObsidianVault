---
tags: [architect-quest, p1, week-03]
status: in_progress
xp_available: 400
xp_earned: 80
---

# 📅 Week 3: Application Layer

## 🎯 Obiettivo
Costruire l'Application Layer con Use Cases, CQRS pattern, e l'infrastruttura MediatR + FluentValidation.

## ✅ TEORIA RECUPERATA (2026-02-17)

> Tutti gli argomenti che erano stati saltati sono stati recuperati con il workflow corretto.

**Argomenti COMPLETATI correttamente:**
- ✅ FluentValidation (teoria + nota + quiz + codice)
- ✅ Ports & Adapters (teoria + nota + quiz)
- ✅ CQRS Queries (teoria + nota + quiz)
- ✅ Application Layer (teoria + nota + quiz) - 2026-02-17
- ✅ CQRS Commands (teoria + nota + quiz) - 2026-02-17
- ✅ Unit of Work (teoria + nota + quiz) - 2026-02-17
- ✅ Testing Seams / IDateTimeProvider (teoria + nota + quiz) - 2026-02-17
- ✅ Composition Root / DI (teoria + nota + quiz) - 2026-02-17
- ✅ Testing con Mocks (teoria + nota + quiz) - 2026-02-17

**TEORIA COMPLETATA!** Tutti gli argomenti sono stati trattati con il workflow corretto.

---

## 📋 Tasks

### Preparazione Teorica (Day 1-2)
- [x] Teoria: Application Layer in Clean Architecture ✅ 2026-02-17 (nota creata)
- [x] Teoria: CQRS Commands ✅ 2026-02-17 (nota creata)
- [x] Teoria: CQRS Queries ✅ 2026-02-17 (nota creata)
- [x] Teoria: Ports & Adapters (Interfaces) ✅ 2026-02-17 (nota creata)
- [ ] Quiz: Application Layer Fundamentals

### CQRS + MediatR Setup (Day 2-3)
- [x] Installa MediatR nel progetto Application ✅ 2026-02-16
- [x] Crea struttura cartelle (Commands, Queries, Handlers) ✅ 2026-02-16
- [x] Implementa `IRequest<T>` pattern ✅ 2026-02-16
- [x] Configura DI in Api project ✅ 2026-02-17

### Commands - Notification (Day 3-4)
- [x] Crea `ScheduleNotificationCommand` + Handler ✅ 2026-02-16
- [x] Crea `CancelNotificationCommand` + Handler ✅ 2026-02-16
- [x] Crea `RetryNotificationCommand` + Handler ✅ 2026-02-16
- [x] Scrivi unit test per Command Handlers (27 tests) ✅ 2026-02-17

### Queries - Notification (Day 4-5)
- [x] Crea `GetNotificationByIdQuery` + Handler ✅ 2026-02-16
- [x] Crea `GetNotificationsByStatusQuery` + Handler ✅ 2026-02-16
- [x] Crea `GetPendingNotificationsQuery` + Handler ✅ 2026-02-16
- [x] Scrivi unit test per Query Handlers (17 tests) ✅ 2026-02-17

### Ports/Interfaces (Day 5-6)
- [x] Crea `INotificationRepository` interface ✅ 2026-02-16
- [x] Crea `ITemplateRepository` interface ✅ 2026-02-17
- [x] Crea `IUnitOfWork` interface ✅ 2026-02-16
- [x] Crea `IDateTimeProvider` interface (per testabilità) ✅ 2026-02-16

### Validation (Day 6-7)
- [x] Installa FluentValidation ✅ 2026-02-17
- [x] Crea `ScheduleNotificationCommandValidator` ✅ 2026-02-17
- [x] Implementa Validation Pipeline Behavior ✅ 2026-02-17
- [x] Scrivi unit test per validators (28 tests) ✅ 2026-02-17

### Documentation (Day 7)
- [x] Crea nota: `cqrs-and-mediatr.md` ✅ 2026-02-16
- [x] Aggiorna README con Application Layer overview ✅ 2026-02-17

## 📖 Letture Obbligatorie

**Durante la settimana:**
- [ ] "Clean Architecture" Cap. 21-22 (Use Cases)
- [ ] Martin Fowler: CQRS Pattern
- [ ] MediatR Documentation
- [ ] FluentValidation Documentation

**Opzionali:**
- Microsoft Docs: CQRS Pattern in .NET
- Jimmy Bogard: Vertical Slice Architecture

## ✅ XP

| Deliverable | XP | Status |
|-------------|-----|--------|
| Teoria + Note | +50 | ✅ |
| MediatR Setup | +40 | ✅ |
| Commands + tests | +80 | ✅ |
| Queries + tests | +60 | ✅ |
| Ports/Interfaces | +50 | ✅ |
| Validation + tests | +70 | ✅ |
| Documentation | +50 | ✅ |

**Totale disponibile:** 400 XP

**Meta Week 3:** 200 XP per sbloccare Week 4

[[Week-02|← Week 2]] | [[Week-04|Week 4 →]]
