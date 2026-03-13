---
tags: [senior-engineer, project, p1]
status: in-progress
started: 2026-03-02
---

# ✅ Progetto 1: Task Manager API

## 📋 Overview
REST API per task con TDD, caching Redis, design patterns.

**Durata:** 3 settimane | **Focus:** Clean Arch, TDD, CQRS, Patterns

---

## 📅 ROADMAP DETTAGLIATA

### Week 1: Domain + Application Layer
| Item | Status | Note |
|------|--------|------|
| **DOMAIN** | | |
| TaskItem Entity | ✅ | 11 test, TDD guidato |
| Priority Value Object | ✅ | Smart Enum pattern |
| Project Entity | ✅ | Recap #1 (+75 XP) |
| Tag Entity | ✅ | Ripasso autonomo |
| DueDate Value Object | ✅ | Factory method |
| Domain Events | ✅ | TaskCreated, TaskCompleted |
| Repository Interfaces | ✅ | ITask, IProject, ITag |
| IUnitOfWork | ⬜ | Interface nel Domain |
| **APPLICATION** | | |
| MediatR setup | ⬜ | |
| CreateTaskCommand + Handler | ⬜ | |
| UpdateTaskCommand + Handler | ⬜ | |
| CompleteTaskCommand + Handler | ⬜ | |
| DeleteTaskCommand + Handler | ⬜ | |
| GetTaskByIdQuery + Handler | ⬜ | |
| GetAllTasksQuery + Handler | ⬜ | |
| GetTasksByStatusQuery + Handler | ⬜ | |
| DTOs (TaskDto, CreateTaskDto) | ⬜ | |
| FluentValidation | ⬜ | |
| ValidationBehavior | ⬜ | |
| LoggingBehavior | ⬜ | |
| **TESTS** | | |
| Handler unit tests (20+) | ⬜ | |

### Week 2: Infrastructure + API Layer
| Item | Status | Note |
|------|--------|------|
| **INFRASTRUCTURE** | | |
| AppDbContext | ⬜ | |
| TaskItemConfiguration | ⬜ | Fluent API |
| ProjectConfiguration | ⬜ | |
| TagConfiguration | ⬜ | |
| TaskRepository | ⬜ | Implementa ITaskRepository |
| ProjectRepository | ⬜ | |
| TagRepository | ⬜ | |
| UnitOfWork | ⬜ | Implementa IUnitOfWork |
| Initial Migration | ⬜ | |
| DateTimeProvider | ⬜ | Seam per testing |
| **API** | | |
| TasksController | ⬜ | CRUD endpoints |
| ProjectsController | ⬜ | |
| TagsController | ⬜ | |
| ExceptionHandlingMiddleware | ⬜ | |
| Serilog setup | ⬜ | Structured logging |
| Swagger/OpenAPI | ⬜ | |
| **TESTS** | | |
| Integration tests (TestContainers) | ⬜ | 10+ tests |
| API tests (WebApplicationFactory) | ⬜ | 10+ tests |

### Week 3: Redis + Patterns + Boss Battle
| Item | Status | Note |
|------|--------|------|
| **REDIS** | | |
| Redis connection setup | ⬜ | |
| ICacheService interface | ⬜ | |
| RedisCacheService | ⬜ | |
| Cache-aside in queries | ⬜ | |
| **PATTERNS** | | |
| TaskFactory | ⬜ | Factory Pattern |
| IPrioritizationStrategy | ⬜ | Strategy Pattern |
| DefaultPrioritizationStrategy | ⬜ | |
| DeadlineFirstStrategy | ⬜ | |
| **POLISH** | | |
| 80%+ test coverage | ⬜ | |
| Performance tests | ⬜ | |
| Documentation | ⬜ | |
| **BOSS BATTLE** | | |
| Note-Taking API | ⬜ | Compartimento stagno (+300 XP) |

---

## 📊 Progresso Attuale

| Week | Status | Completamento |
|------|--------|---------------|
| Week 1 | 🟡 In corso | ~60% (Domain ✅, Application ⬜) |
| Week 2 | ⬜ | 0% |
| Week 3 | ⬜ | 0% |

**XP Totale Progetto:** 430 / ~1500

---

## 🔴🟢🔵 APPROCCIO: TDD RIGOROSO

> **IMPORTANTE:** Questo progetto segue TDD rigoroso.
>
> 1. **🔴 RED** - Dan scrive il TEST prima
> 2. **🔴 RED** - Verifica che fallisce
> 3. **🟢 GREEN** - Dan scrive il CODICE minimo
> 4. **🟢 GREEN** - Verifica che passa
> 5. **🔵 REFACTOR** - Migliora insieme
>
> **MAI scrivere codice senza test che fallisce prima!**

---

## 🎯 Cosa Imparerai

- Clean Architecture (tutti i layer)
- TDD (Red → Green → Refactor)
- CQRS con MediatR
- Repository + UnitOfWork patterns
- Factory Pattern
- Strategy Pattern
- Redis caching
- EF Core + Migrations
- Integration testing (TestContainers)
- API testing (WebApplicationFactory)

---

## 🎨 Patterns

| Pattern | Problema | Week |
|---------|----------|------|
| Repository | Astrae accesso dati | W1 |
| UnitOfWork | Transazioni atomiche | W1-W2 |
| CQRS | Separa read/write | W1 |
| Factory | Crea task diversi | W3 |
| Strategy | Prioritizzazione | W3 |

---

## 🎯 ESERCIZI RECAP

> Dopo ogni argomento TDD, Dan fa un esercizio simile **da solo**.

| # | Argomento | Esercizio | Status | XP |
|---|-----------|-----------|--------|-----|
| 1 | Entity (TaskItem) | Creare `Project` entity | ✅ | +75 |
| 2 | Value Object (Priority) | Creare `Money` VO | ✅ | +75 |
| 3 | Domain Events | Creare `TaskCompletedEvent` | ✅ | +75 |
| 4 | Repository Pattern | Creare `ITagRepository` | ✅ | +75 |
| 5 | Application Layer | Creare `CompleteTaskCommand` da solo | ⬜ | +75 |
| 6 | Infrastructure | Creare `TagRepository` da solo | ⬜ | +75 |
| 7 | API | Creare `TagsController` da solo | ⬜ | +75 |
| **🏆** | **BOSS BATTLE** | **Note-Taking API completa** | ⬜ | +300 |

---

## 📦 Deliverables Finali

- [ ] REST API CRUD completa
- [ ] 80%+ test coverage
- [ ] Redis caching funzionante
- [ ] 4 design patterns applicati (Repository, UnitOfWork, Factory, Strategy)
- [ ] Serilog structured logging
- [ ] EF Core migrations
- [ ] 50+ unit tests
- [ ] 10+ integration tests
- [ ] 10+ API tests
- [ ] Swagger documentation

---

## 📦 GIT

**Repository:** [TaskManager](https://github.com/DanielMateusGit/TaskManager)

### Commit effettuati
| Data | Commit | Descrizione |
|------|--------|-------------|
| 2026-03-03 | `85ca0fb` | feat: initial commit - TaskItem, Project entities |
| 2026-03-03 | `572e2c9` | feat: add Tag entity and DueDate value object |
| 2026-03-04 | `fc58f61` | feat: add Domain Events and fix DueDate UTC |
| 2026-03-04 | `ff7a8f8` | feat: add TaskCompletedEvent and Complete() method |
| 2026-03-04 | `3147db0` | feat: add repository interfaces |

---

*Ultimo aggiornamento: 2026-03-04*
