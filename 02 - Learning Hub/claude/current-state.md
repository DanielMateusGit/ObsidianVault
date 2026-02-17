# 📍 Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## 🎯 Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto** | Architect Quest → P1 Notification Service |
| **Settimana** | Week 3 (in corso) |
| **FASE** | 🎯 **FASE 1 - WEEK 3 (Application Layer)** |
| **Task corrente** | ✅ Teoria completata - pronto per commit o prossimo step |

---

## ✅ TEORIA RECUPERATA (2026-02-17)

> **CONTEXT PER CLAUDE:** Durante la sessione precedente avevo scritto codice SENZA insegnare la teoria. Dan mi ha corretto e abbiamo recuperato TUTTO seguendo il workflow corretto.

### ✅ Argomenti con TEORIA COMPLETA (workflow corretto)
| Argomento | Nota | Quiz |
|-----------|------|------|
| FluentValidation | `Notes/fluentvalidation.md` | ✅ 3 quiz |
| Ports & Adapters | `Notes/ports-and-adapters.md` | ✅ 3 quiz |
| CQRS Queries | `Notes/cqrs-queries.md` | ✅ 3 quiz |

### ✅ Argomenti RECUPERATI (prima avevano solo codice)
| Argomento | Nota Creata |
|-----------|-------------|
| Application Layer | `Notes/application-layer.md` |
| CQRS Commands | `Notes/cqrs-commands.md` |
| Unit of Work | `Notes/unit-of-work.md` |
| Testing Seams (IDateTimeProvider) | `Notes/testing-seams.md` |
| Composition Root / DI | `Notes/composition-root.md` |
| Testing con Mocks | `Notes/testing-with-mocks.md` |

### ✅ Piano di Recupero COMPLETATO

**6 note create con workflow corretto (TEORIA → DOMANDE → NOTA):**
1. ✅ `Notes/application-layer.md`
2. ✅ `Notes/cqrs-commands.md`
3. ✅ `Notes/unit-of-work.md`
4. ✅ `Notes/testing-seams.md`
5. ✅ `Notes/composition-root.md`
6. ✅ `Notes/testing-with-mocks.md`

**Prossimi step possibili:**
- Commit del codice esistente
- Continuare con Week 3 (letture obbligatorie)
- Quiz: Application Layer Fundamentals

## 📋 Decisione Strategica: Percorsi in Parallelo (2026-02-02)

**Opzione scelta:** B - Parallelo Sfalsato

**Piano:**
- **Mese 1 (Feb):** 100% Architect P1 (Week 1-4) - basi Clean Architecture
- **Mese 2 (Mar):** 70% Architect P1 + 30% Senior P1 (Task Manager)
- **Mese 3+ :** Continua parallelo (2 sessioni Architect + 1 Senior)

**Quando iniziare Senior Engineer:** Dopo Week 4 di Architect P1 (fine Febbraio)

**Perché:**
- Applichi subito in Senior ciò che impari in Architect
- P1 Senior rinforza Clean Architecture + aggiunge TDD + Redis
- Varietà = motivazione alta

## 📊 Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 1934 |
| **Livello** | 3 - Pattern Seeker (prossimo: 2000 XP → 66 XP mancanti) |
| **Streak** | 2 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement sbloccati** | 6 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire) |

## 🏛️ Architect Quest - Status

| Progetto | Status | Settimana |
|----------|--------|-----------|
| P1 - Notification Service | 🟢 In corso | W2 |
| P2 - NutriPlan | 🔒 Locked | - |
| P3 - BookingHub | 🔒 Locked | - |
| P4 - FamilyBudget | 🔒 Locked | - |

## 💻 Senior Engineer - Status

| Progetto | Status | Settimana |
|----------|--------|-----------|
| P1 - Task Manager | 🟡 Non iniziato | W1-2 |
| P1.5 - Auth & Security 🔐 | 🔒 Locked | W3 |
| P2 - Chat App | 🔒 Locked | W4-6 |
| P3 - E-commerce | 🔒 Locked | W7-10 |
| P4 - Alert Gateway | 🔒 Locked | W11-13 |
| P5 - URL Shortener | 🔒 Locked | W14-16 |
| P6 - Capstone | 🔒 Locked | M6-16 |

## ✅ Ultima Sessione

**Data:** 2026-02-17
**Tipo:** Week 3 - Correzione Workflow + Teoria

**Cosa fatto:**

### 🧠 Spaced Repetition
- 3 domande: OCP-01 (in scadenza), CQRS-01, EVT-04
- Tutte corrette! OCP-01 passa a Box 4

### 📝 Teoria Insegnata Correttamente
| Argomento | Nota Creata | Quiz |
|-----------|-------------|------|
| FluentValidation | `Notes/fluentvalidation.md` | ✅ 3 |
| Ports & Adapters | `Notes/ports-and-adapters.md` | ✅ 3 |
| CQRS Queries | `Notes/cqrs-queries.md` | ✅ 3 |

### 🔴 ERRORE RICONOSCIUTO
Claude ha scritto molto codice SENZA spiegare la teoria prima:
- ITemplateRepository, IUnitOfWork, IDateTimeProvider
- DI configuration (DependencyInjection.cs, Program.cs)
- 72 unit test per handlers
- Commands (ScheduleNotification, Cancel, Retry)

**Dan ha corretto:** "Non ho imparato niente"

**Decisione:** Tornare indietro e insegnare TUTTA la teoria che manca.

### 🛠️ Codice Scritto (da collegare alla teoria)
- FluentValidation: 3 Validators + ValidationBehavior
- 72 test totali nel progetto Application.Tests
- ITemplateRepository, IUnitOfWork, IDateTimeProvider
- DependencyInjection.cs + Program.cs aggiornato

**XP guadagnati:** Da calcolare dopo recupero teoria
- Spaced Repetition: +35
- (Teoria non completata - XP in sospeso)

**Nessun commit oggi** - prima completiamo la teoria

---

## ✅ Sessione Precedente (2026-02-16)

**Data:** 2026-02-16
**Tipo:** Week 3 Start - CQRS & MediatR

**XP guadagnati:** +202

---

## ✅ Sessione Precedente (2026-02-13)

**Data:** 2026-02-13
**Tipo:** Week 2 Completion + Letture Domain Events

**XP guadagnati:** +262

---

## ✅ Sessione Precedente (2026-02-12)

**Data:** 2026-02-12
**Tipo:** MAJOR Roadmap Update - AI-First Track + AI Features

**Cosa fatto:**
- AI-First Track (3 nuovi progetti: P5, P6, P7)
- AI Features per Senior Engineer
- Boss Battle System
- ADR-002 + C4 Container Diagram

---

## ✅ Sessione Pre-Precedente (2026-02-11)

**Data:** 2026-02-11
**Durata:** ~2h
**Tipo:** Week 2 - Domain Events Implementation

**Cosa fatto:**
- **Domain Events** implementati completamente! (+40 XP)
  - `IDomainEvent` interface
  - `Entity` base class con domain events collection
  - `NotificationScheduledEvent`, `NotificationSentEvent`, `NotificationFailedEvent`
  - Notification entity aggiornata per generare eventi
- **13 nuovi unit test** per Domain Events (tutti verdi ✅)
- **178 test totali** nel progetto
- Nota `domain-events.md` completamente riscritta con teoria Registry/MediatR
- 6 note corrette per seguire template uniforme
- **🔥 Achievement: On Fire (7 giorni streak)** (+100 XP)
- **🎉 LEVEL UP → Pattern Seeker (Lv.3)!**

**XP guadagnati:** +140
- Domain Events implementation: +40
- On Fire achievement (7-day streak): +100

**Commit:**
- `d7eb134` - feat: Add domain events for Notification entity

**File creati/modificati:**
- `src/Domain/Events/IDomainEvent.cs` (NEW)
- `src/Domain/Events/NotificationScheduledEvent.cs` (NEW)
- `src/Domain/Events/NotificationSentEvent.cs` (NEW)
- `src/Domain/Events/NotificationFailedEvent.cs` (NEW)
- `src/Domain/Entities/Entity.cs` (NEW - base class)
- `src/Domain/Entities/Notification.cs` (MODIFIED - inherits Entity, raises events)
- `tests/Events/DomainEventsTests.cs` (NEW - 13 tests)
- `Notes/domain-events.md` (REWRITTEN)

---

## ✅ Sessione Precedente (2026-02-10)

**Data:** 2026-02-10
**Durata:** ~2.5h
**Tipo:** Week 2 - Domain Model Implementation (massiva!)

**Cosa fatto:**
- Challenge del giorno: OCP-01 ✅ (Box 2→3)
- **Template entity** + TemplateData value object (+70 XP)
- **DeliveryAttempt entity** + DeliveryStatus enum (+60 XP)
- **Value Objects:** EmailAddress, PhoneNumber, Recipient (+50 XP)
- **Nota consolidata:** `domain-model-patterns.md` con 6 quiz (+20 XP)
- **165 unit test totali** (tutti verdi ✅)
- 3 commit pushati su GitHub

**XP guadagnati:** +215

**Commit:**
- `6c955a0` - Template entity
- `38da468` - DeliveryAttempt entity
- `b4b6eda` - Value Objects

---

## ✅ Sessione Pre-Precedente (2026-02-09)

**Data:** 2026-02-09
**Durata:** ~2h 30min (2 sessioni)
**Tipo:** Week 1 Completion + Sistema Sedimentazione

**Cosa fatto:**
- C4 Context Diagram (teoria + implementazione + push)
- README.md + .env.example (push)
- Letture overview (SOLID, Clean Architecture, Philosophy of Software Design)
- Quiz superati: 12/12
- Creato sistema Sedimentazione completo
- **LEVEL UP → Code Crafter (Lv.2)**

**XP guadagnati:** +245

**Achievement sbloccati:**
- 📐 Architect Apprentice
- 🔥 Spark (3 giorni streak)

---

## ✅ Sessione Pre-Precedente

**Data:** 2026-02-02
**Durata:** ~2.5h
**Cosa fatto:**

### Setup Tecnico
- Creata solution .NET 8 con 4 progetti Clean Architecture
- Configurate dipendenze corrette tra progetti
- Docker Compose con PostgreSQL 16 + Redis 7 (testati)
- Repo GitHub creato: https://github.com/DanielMateusGit/notification-service
- Installato GitHub CLI (`gh`)
- ADR-001 creato e pushato

### Apprendimento
- **Clean Architecture:** 4 layer, Dependency Rule, violazioni comuni
- **ADR:** Cos'è, quando usarlo, quando NO, granularità, frequenza
- **Quiz completati:** 4 domande Clean Architecture + 6 domande ADR

### Metodologia
- Definita sequenza di insegnamento completa (9 step)
- Aggiunti: domande di verifica, risorse, conferma prima di implementare
- Aggiunta: creazione note con quiz post-implementazione

**XP guadagnati:** +275 totali
- Repo + struttura: +50
- Docker Compose: +50
- ADR-001: +75
- Achievement First Commit: +50
- Achievement Docker Newbie: +50

**Achievement sbloccati:** 🌱 First Commit, 🐳 Docker Newbie

**Appunti creati/aggiornati:**
- `Notes/clean-architecture.md` (con quiz)
- `Notes/project-overview.md`
- `Notes/adr-architecture-decision-records.md` (con quiz)

## 🎯 Prossima Sessione

**Fase attuale:** 🎯 FASE 1 - WEEK 3 (Application Layer)
**Task corrente:** Iniziare Week 3

**Week 3 - Application Layer (W3-W4):**
- Use Cases / Commands & Queries
- Ports & Adapters (interfaces)
- CQRS pattern introduction
- Unit of Work
- Validation (FluentValidation)
- MediatR setup

**Prossimi achievement:**
- 📐 **Module Builder** (Level 4) → mancano 423 XP
- 🔥 **Inferno** (30 giorni streak) → 21 giorni rimanenti

## 🤖 AI Skills - Overview Completa

### Architect Quest - AI Integration
| Progetto | AI Focus |
|----------|----------|
| P2.5 AI Gateway | Provider abstraction, routing, MCP |
| P2 NutriPlan | Usa Notification Service |
| P3 BookingHub | Usa Notification + AI Gateway |
| P4 FamilyBudget | Usa entrambi + AI categorization |

### Architect Quest - AI-First Track (NEW!)
| Progetto | AI Skills |
|----------|-----------|
| P5 Second Brain | RAG, Vector DB, Embeddings, Semantic Search |
| P6 Interview Coach | AI Evaluation, Structured Output, Voice AI |
| P7 Personal Copilot | MCP avanzato, Code Analysis, GitHub integration |

### Senior Engineer - AI Features
| Progetto | AI Feature |
|----------|------------|
| P1 | Smart Prioritization (Ollama base) |
| P2 | Message Summarization (Streaming) |
| P3 | Product Recommendations (Embeddings) |
| P4 | Alert Triage (Classification) |
| P5 | Link Preview (Structured Output) |
| P6 | Full AI Assistant (tutto insieme!) |

### AI Frontier Lab 🔬
- **Cadenza:** Quarterly (1 weekend)
- **Scopo:** Stay current senza bloccare progetti

**Documentazione:** [[roadmaps/ai-skills.md]] | [[roadmaps/architect-quest]]

## ❓ Domande Aperte

_Nessuna - pronti a partire!_

## 🚧 Blocchi / Problemi

_Nessun blocco attuale_

## 📝 Note

- Workflow definito: coach.py per motivazione, Claude per apprendimento
- Sessioni corte frequenti (30-45 min) preferite
- Orari flessibili

## 💪 NOVITÀ: Sistema Motivazionale Aggiunto! (2026-02-02)

**Files creati/aggiornati:**
1. **`claude/WHY.md`** ← Il VERO perché di tutto questo
   - Casa per Dan e Federica (€40-60k anticipo, fattibile in 2-3 anni)
   - Supportare mamma, papà, sorelle senza stress economico
   - Futuro sicuro per eventuali figli
   - Numeri concreti: €100-120k target vs €50-60k ora = +€2k/mese netto
   - 18 mesi di impegno = 40 anni di tranquillità

2. **`claude/career-strategy.md`** ← Certificazioni, ruoli, salary
   - Certificazioni consigliate (AZ-305, CKA, Terraform)
   - Ruoli target (Senior, Staff, AI Engineer)
   - Salary expectations per mercato (Italia: €70-90k, EU: €95-115k, US: €115-135k)

3. **`profile.md`** aggiornato
   - Aggiunto Federica come motivazione principale
   - Obiettivi personali con numeri concreti

4. **`CLAUDE.md`** aggiornato
   - Leggi WHY.md all'inizio di ogni sessione
   - Ricorda il perché durante la motivazione

5. **`coach.py`** aggiornato
   - Nuovo comando: `./coach.py motivation`
   - Genera frasi motivazionali giornaliere basate su WHY.md
   - Temi: casa_federica, famiglia_supporto, figli_futuro, liberta_finanziaria, numeri_concreti, roi_impegno

**Come usare:**
```bash
# Ogni mattina, prima di iniziare
./coach.py motivation

# Output esempio:
"Ogni ora di studio oggi = €100 in più al mese tra 18 mesi.
Quella casa per te e Federica è più vicina di quanto pensi. 🏡"
```

**Reminder per Claude:**
- Quando Dan è stanco/demotivato → ricorda WHY.md
- Connetti sempre lo studio tecnico agli obiettivi personali
- Usa numeri concreti (casa €40-60k, +€2k/mese, 18 mesi → 40 anni)

## 🧠 NOVITÀ: AI-First Track + AI Features (2026-02-12)

### Architect Quest - AI-First Track (3 nuovi progetti!)
| Progetto | Mesi | Cosa Fa | Uso Personale |
|----------|------|---------|---------------|
| **P5 AI Second Brain** | 7-8 | RAG sul tuo vault | Query tue note con AI |
| **P6 AI Interview Coach** | 15-16 | Simula interview | Prep colloqui €90k+ |
| **P7 Personal Copilot** | 19-20 | Code assistant | Il TUO Copilot |

### Senior Engineer - AI Features
Ogni progetto ora ha una **AI Feature bonus**:
- P1 → Smart Prioritization
- P2 → Message Summarization
- P3 → Product Recommendations
- P4 → Alert Triage
- P5 → Link Preview Generator
- P6 → Full AI Study Assistant

### 📊 Risultato Finale
- **15 progetti totali** (8 Architect + 7 Senior)
- **9 progetti con AI** (4 AI-first + 5 con AI feature)
- **Timeline:** 20 mesi Architect, parallelo Senior

---

## 🏆 Boss Battle System

**Cos'è:** Verifica autonoma alla fine di ogni progetto.

**XP:**
- ≥24/30: +300 XP | ≥28/30: +500 XP

**Achievement:**
- 🏆 Architect Champion (7/7) → +1000 XP
- 🏆 Senior Champion (6/6) → +1500 XP

---

*Ultimo aggiornamento: 2026-02-13*