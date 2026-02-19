# 📍 Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## 🎯 Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto** | Architect Quest → P1 Notification Service |
| **Settimana** | Week 4 ✅ COMPLETATA |
| **FASE** | 🚨 **BLOCCO PRE-WEEK 5: Letture + Esame Mese 1** |
| **Task corrente** | Completare 9 letture obbligatorie → Esame Mese 1 (30 punti) |

---

## ✅ WEEK 4 COMPLETATA (400/400 XP)

### Teoria + Note
| Argomento | Nota | Quiz | Status |
|-----------|------|------|--------|
| Infrastructure Layer | `infrastructure-layer.md` | 5 quiz | ✅ |
| Repository Pattern | `repository-pattern.md` | 3 quiz | ✅ |
| EF Core Migrations | `ef-core-migrations.md` | 3 quiz | ✅ |
| Value Object Persistence | `value-object-persistence.md` | 3 quiz | ✅ |
| Integration Tests | `integration-tests.md` | 2 quiz | ✅ |

### Implementato
- `AppDbContext` con 3 DbSet
- `NotificationConfiguration`, `TemplateConfiguration`, `DeliveryAttemptConfiguration`
- `PostgresNotificationRepository`, `PostgresTemplateRepository`
- `UnitOfWork`
- `InitialCreate` + `UseRecipientValueObject` migrations
- `Recipient` Value Object con EF Core Owned Types
- Integration tests con Testcontainers (11 test)
- **268 test totali** (185 Domain + 72 Application + 11 Infrastructure)
- ADR-003: Database Strategy
- README aggiornato con database setup

---

## 🚨🚨🚨 BLOCCO PRE-WEEK 5 🚨🚨🚨

> **Week 4 COMPLETATA!** Ma prima di procedere a Week 5:

### Step 1: Letture Obbligatorie (0/9)
| # | Risorsa | Tempo | Status |
|---|---------|-------|--------|
| 1 | Clean Architecture Cap. 7-14 | ~2-3h | ⬜ |
| 2 | A Philosophy of Software Design Cap. 1-5 | ~2h | ⬜ |
| 3 | Domain Model Pattern - Fowler | ~20min | ⬜ |
| 4 | CQRS - Martin Fowler | ~15min | ⬜ |
| 5 | MediatR Wiki | ~30min | ⬜ |
| 6 | MediatR Behaviors - Jimmy Bogard | ~20min | ⬜ |
| 7 | FluentValidation Docs | ~30min | ⬜ |
| 8 | Validation in DDD - Vladimir Khorikov | ~20min | ⬜ |
| 9 | Clean Architecture Cap. 21-22 | ~1h | ⬜ |

**Totale:** ~7-8 ore | **XP disponibili:** +195

### Step 2: Esame Mese 1 (30 punti)
- **Argomenti:** Week 1-4 (Clean Architecture, Domain Model, CQRS, Infrastructure)
- **Formato:** Domande aperte + Multiple choice + Codice + Design
- **XP:** +100-200 (in base al voto)

### Solo dopo → Week 5 (Message Queue)

---

## 📊 Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 2179 |
| **Livello** | 4 - Module Builder (prossimo: 2500 XP → 321 XP mancanti) |
| **Streak** | 3 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement sbloccati** | 6 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire) |

## 🏛️ Architect Quest - Status

| Progetto | Status | Settimana |
|----------|--------|-----------|
| P1 - Notification Service | 🟢 In corso | W4 ✅ → Letture + Esame → W5 |
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

**Data:** 2026-02-19
**Tipo:** Week 4 COMPLETATA - Infrastructure Layer

**Cosa fatto:**

### 🧠 Spaced Repetition
- 4 quiz: OCP-02, OCP-03, DIP-03, EVT-02
- Tutte corrette!

### 📝 Teoria + Note
| Argomento | Nota Creata | Quiz |
|-----------|-------------|------|
| Repository Pattern | `repository-pattern.md` | 3 |
| EF Core Migrations | `ef-core-migrations.md` | 3 |
| Value Object Persistence | `value-object-persistence.md` | 3 |
| Integration Tests | `integration-tests.md` | 2 |

### 🛠️ Implementazione
- EF Core + PostgreSQL setup completo
- Entity Configurations con Owned Types (Recipient VO)
- Repository implementations
- UnitOfWork pattern
- Integration tests con Testcontainers (11 test)
- 268 test totali passati

### 📦 Commit
- `0a8efb2` - feat: Add Infrastructure Layer with EF Core and PostgreSQL
- `887198e` - refactor: Use Recipient Value Object with EF Core Owned Types
- `6feff35` - test: Add integration tests with Testcontainers
- `f4fd2d9` - docs: Add ADR-003 Database Strategy and update README

### 📊 Week 4 Summary
- **XP guadagnati:** 400/400 ✅
- **Test totali:** 268 (185 Domain + 72 Application + 11 Infrastructure)
- **Status:** COMPLETATA

**Prossima sessione:**
1. ⬜ Letture obbligatorie (9 risorse)
2. ⬜ Esame Mese 1 (30 punti)
3. ⬜ Week 5 (Message Queue)

---

## ✅ Sessione Precedente (2026-02-18)

**Data:** 2026-02-18
**Tipo:** Week 4 Start - Infrastructure Layer Theory

**Cosa fatto:**
- Teoria Infrastructure Layer + nota
- 5 quiz Infrastructure (INFRA-01 to INFRA-05)
- Iniziata teoria Repository Pattern (interrotta)

---

## ✅ Sessione Precedente (2026-02-17)

**Data:** 2026-02-17
**Tipo:** Week 3 - Recupero Teoria Completo

**Cosa fatto:**
- Spaced Repetition: 3 domande corrette
- 6 note recuperate con workflow corretto
- Sistema /init creato
- Commit: `83084cd`

**XP guadagnati:** ~200 XP

---

## ✅ Sessione Precedente (2026-02-16)

**Data:** 2026-02-16
**Tipo:** Week 3 Start - CQRS & MediatR

**XP guadagnati:** +202

---

## 🎯 Prossima Sessione

**Fase attuale:** 🚨 **BLOCCO PRE-WEEK 5** - Letture + Esame Mese 1

**TODO (in ordine):**
1. ⬜ **Letture obbligatorie** (9 risorse, ~7-8h totali)
2. ⬜ **Esame Mese 1** (30 punti, Week 1-4)
3. ⬜ **Week 5** - Message Queue (Azure Service Bus / RabbitMQ)

**Timeline:**
- Deadline letture + esame: Fine Febbraio 2026
- Giorni rimasti: ~9-10 giorni

**Prossimi achievement:**
- 📐 **System Architect** (Level 5) → mancano 321 XP
- 🔥 **Inferno** (30 giorni streak) → 20 giorni rimanenti
- 📝 **First Exam** → completare Esame Mese 1

---

## 📋 Decisione Strategica: Percorsi in Parallelo (2026-02-02)

**Opzione scelta:** B - Parallelo Sfalsato

**Piano:**
- **Mese 1 (Feb):** 100% Architect P1 (Week 1-4) - basi Clean Architecture
- **Mese 2 (Mar):** 70% Architect P1 + 30% Senior P1 (Task Manager)
- **Mese 3+ :** Continua parallelo (2 sessioni Architect + 1 Senior)

**Quando iniziare Senior Engineer:** Dopo Week 4 di Architect P1 (fine Febbraio)

---

## 🤖 AI Skills - Overview Completa

### Architect Quest - AI Integration
| Progetto | AI Focus |
|----------|----------|
| P2.5 AI Gateway | Provider abstraction, routing, MCP |
| P2 NutriPlan | Usa Notification Service |
| P3 BookingHub | Usa Notification + AI Gateway |
| P4 FamilyBudget | Usa entrambi + AI categorization |

### Architect Quest - AI-First Track
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

---

## ❓ Domande Aperte

_Nessuna_

## 🚧 Blocchi / Problemi

**BLOCCO ATTIVO:** Completare 9 letture + Esame Mese 1 prima di Week 5

## 📝 Note

- Workflow definito: coach.py per motivazione, Claude per apprendimento
- Sessioni corte frequenti (30-45 min) preferite
- Orari flessibili
- **LEVEL UP → Module Builder (Lv.4)!** 🎉

---

*Ultimo aggiornamento: 2026-02-19 (Week 4 completata, BLOCCO pre-Week 5 attivo)*
