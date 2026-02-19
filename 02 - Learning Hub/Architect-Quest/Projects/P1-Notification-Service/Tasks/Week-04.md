---
tags: [architect-quest, p1, week-04]
status: complete
started: 2026-02-18
xp_available: 400
xp_earned: 400
---

# Week 4: Infrastructure Layer - Database con EF Core

## Obiettivo
Implementare l'Infrastructure Layer con Entity Framework Core, Repository pattern concreti, e database persistence.

---

## Teoria da Completare (PRIMA del codice!)

| # | Argomento | Nota | Status |
|---|-----------|------|--------|
| 1 | Infrastructure Layer in Clean Architecture | `Notes/infrastructure-layer.md` | ✅ 2026-02-18 |
| 2 | Repository Pattern (implementazione) | `Notes/repository-pattern.md` | ✅ 2026-02-19 |
| 3 | Entity Framework Core Basics | (incluso in infrastructure-layer.md) | ✅ 2026-02-18 |
| 4 | DbContext e Configuration | (incluso in infrastructure-layer.md) | ✅ 2026-02-18 |
| 5 | Migrations Strategy | `Notes/ef-core-migrations.md` | ✅ 2026-02-19 |
| 6 | Value Object Persistence (Owned Types) | `Notes/value-object-persistence.md` | ✅ 2026-02-19 |

---

## Tasks

### Preparazione Teorica (Day 1-2)
- [x] Teoria: Infrastructure Layer in Clean Architecture ✅ 2026-02-18
- [x] Teoria: EF Core + Npgsql (cos'è, perché, trade-offs) ✅ 2026-02-18
- [x] Teoria: Repository Pattern Implementation ✅ 2026-02-19
- [x] Teoria: EF Core Migrations ✅ 2026-02-19
- [x] Quiz: Infrastructure Fundamentals (5 quiz) ✅ 2026-02-18
- [x] Quiz: Repository Pattern (3 quiz) ✅ 2026-02-19
- [x] Quiz: Migrations (3 quiz) ✅ 2026-02-19

### EF Core Setup (Day 2-3)
- [x] Installa EF Core + Npgsql nel progetto Infrastructure ✅ 2026-02-19
- [x] Crea `AppDbContext` con DbSet per tutte le entities ✅ 2026-02-19
- [x] Configura connection string (appsettings.Development.json) ✅ 2026-02-19
- [x] Crea prima migration (InitialCreate) ✅ 2026-02-19
- [x] Applica migration a PostgreSQL ✅ 2026-02-19

### Entity Configuration (Day 3-4)
- [x] Crea `NotificationConfiguration` (IEntityTypeConfiguration) ✅ 2026-02-19
- [x] Crea `TemplateConfiguration` ✅ 2026-02-19
- [x] Crea `DeliveryAttemptConfiguration` ✅ 2026-02-19
- [x] Configura Value Objects come Owned Types (Recipient) ✅ 2026-02-19

### Repository Implementation (Day 4-5)
- [x] Implementa `PostgresNotificationRepository : INotificationRepository` ✅ 2026-02-19
- [x] Implementa `PostgresTemplateRepository : ITemplateRepository` ✅ 2026-02-19
- [x] Implementa `UnitOfWork : IUnitOfWork` ✅ 2026-02-19
- [x] Scrivi integration test per repositories ✅ 2026-02-19

### DI Registration (Day 5-6)
- [x] Crea `DependencyInjection.cs` in Infrastructure ✅ 2026-02-19
- [x] Registra DbContext, Repositories, UnitOfWork ✅ 2026-02-19
- [x] Configura lifetime corretto (Scoped) ✅ 2026-02-19

### Integration Tests (Day 6-7)
- [x] Setup test container (Testcontainers + PostgreSQL) ✅ 2026-02-19
- [x] Scrivi integration test per repository operations ✅ 2026-02-19
- [x] Verifica migrations funzionano ✅ 2026-02-19

### Documentation (Day 7)
- [x] Crea nota: `infrastructure-layer.md` ✅ 2026-02-18
- [x] Crea nota: `repository-pattern.md` ✅ 2026-02-19
- [x] Crea nota: `ef-core-migrations.md` ✅ 2026-02-19
- [x] Aggiorna README con database setup instructions ✅ 2026-02-19
- [x] ADR-003: Database Strategy (PostgreSQL, EF Core) ✅ 2026-02-19

---

## Commit

| Data | Commit | Descrizione |
|------|--------|-------------|
| 2026-02-19 | `0a8efb2` | feat: Add Infrastructure Layer with EF Core and PostgreSQL |
| 2026-02-19 | `887198e` | refactor: Use Recipient Value Object with EF Core Owned Types |
| 2026-02-19 | `6feff35` | test: Add integration tests with Testcontainers |
| 2026-02-19 | `f4fd2d9` | docs: Add ADR-003 Database Strategy and update README |

---

## Letture Obbligatorie

**Durante la settimana:**
- [ ] EF Core Documentation - Getting Started
- [ ] EF Core - Configuring Entities
- [ ] Repository Pattern - Martin Fowler
- [ ] Clean Architecture Cap. 23-24 (Frameworks & Databases)

**Opzionali:**
- EF Core Performance Tips
- Testcontainers Documentation

---

## XP Disponibili

| Deliverable | XP | Status |
|-------------|-----|--------|
| Teoria + Note | +50 | ✅ +50 |
| EF Core Setup | +40 | ✅ +40 |
| Entity Configuration | +60 | ✅ +60 |
| Repository Implementation | +80 | ✅ +80 |
| DI Registration | +30 | ✅ +30 |
| Integration Tests | +80 | ✅ +80 |
| Documentation | +60 | ✅ +60 |

**XP Guadagnati:** 400 / 400 ✅ COMPLETATA!
**Meta Week 4:** 250 XP ✅ RAGGIUNTA

---

## ✅ Week 4 COMPLETATA!

**Data completamento:** 2026-02-19
**XP Totali:** 400/400

---

## 🚨 PROSSIMI STEP (BLOCCANTI per Week 5)

### 1. Letture Obbligatorie (0/9) → +195 XP
Vedi `context/reading-list.md`

### 2. Esame Mese 1 (30 punti) → +100-200 XP
- Argomenti: Week 1-4 (Clean Architecture, Domain, CQRS, Infrastructure)
- Formato: Domande aperte + Multiple choice + Codice + Design

### Solo dopo → Week 5 (Message Queue)

---

## Collegamenti

[[Week-03|← Week 3]] | [[Week-05|Week 5 →]]
