# Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto AQ** | P1 Notification Service |
| **Settimana AQ** | Week 4 COMPLETATA → Pronto per Week 5 |
| **Progetto SE** | P1 Task Manager |
| **Settimana SE** | W1 95% (Domain ✅, Commands ✅, Queries ✅, DTOs ✅, Validators ✅, ValidationBehavior ✅ — manca solo LoggingBehavior) |
| **Task corrente** | Senior P1 W1 (LoggingBehavior) → poi W2 |

---

## Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 4169 |
| **Livello** | 5 - Service Architect |
| **Streak** | 6 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement** | 10 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire, First Exam, First Lesson, Course Master, Perfect Score) |
| **Certificazioni** | 1 (Claude Code in Action - 8/8 Perfect Score) |

---

## Architect Quest - Status

| Progetto | Status | Periodo |
|----------|--------|---------|
| P1 - Notification Service | In corso | W5 prossima |
| P2 - NutriPlan | Locked | M5-9 |
| P2.5 - AI Gateway | Locked | M5-6 |
| P3 - BookingHub | Locked | M10-14 |
| P4 - FamilyBudget | Locked | M15-18 |
| P5 - FitHub | Locked | M19-22 |

### Week 4 Completata (400/400 XP)
- Infrastructure Layer, Repository Pattern, EF Core, Value Object Persistence, Integration Tests
- 268 test totali (185 Domain + 72 Application + 11 Infrastructure)
- Esame Mese 1: 25/30 (Superato con merito)

---

## Senior Engineer - Status

| Progetto | Status | Periodo |
|----------|--------|---------|
| P1 - Task Manager | In corso | W1-3 (iniziato 2026-03-02) |
| P1.5 - Auth & Security | Locked | W4 |
| P2 - Chat App | Locked | W5-7 |
| P3 - E-commerce | Locked | W8-11 |
| P4 - Alert Gateway | Locked | W12-14 |
| P5 - URL Shortener | Locked | W15-17 |
| P6 - Capstone | Locked | M6-16 |

### P1 Task Manager - Roadmap

| Week | Focus | Status |
|------|-------|--------|
| W1 | Domain + Application Layer | 95% (manca solo LoggingBehavior) |
| W2 | Infrastructure + API Layer | Da fare |
| W3 | Redis + Patterns + Boss Battle | Da fare |

**Regole Senior Engineer:** 70% coding, 30% teoria. Dan scrive, Claude guida. TDD rigoroso.

### TODO Senior P1
1. ~~IUnitOfWork - Interface in Application~~ ✅
2. ~~Commands (Create, Complete, Update, Delete)~~ ✅
3. ~~Recap #5 - CompleteTaskCommand da solo~~ ✅
4. ~~Queries (GetById, GetAll, GetByStatus)~~ ✅
5. ~~DTOs per response~~ ✅ (TaskItemDto record)
6. ~~FluentValidation sui Commands~~ ✅ (4 validators)
7. ~~ValidationBehavior~~ ✅ (con test)
8. LoggingBehavior ← UNICO MANCANTE W1

---

## Ultima Sessione

**Data:** 2026-03-24 (sessione 3)
**Tipo:** Refactor progetto (skill /refactor + coerenza contesto)

- Creata skill `/refactor` con 5 dimensioni analisi + Step 2b (framework 3-tier gap analysis cross-path)
- Fix strutturali: duplicazioni (files.md), stale (QUICK-REFERENCE), legacy (PROMPT.md)
- AI Engineer primario allineato su TUTTI i file (CLAUDE.md, profile, career-strategy, ecc.)
- Timeline ricalibrata da 18 a ~20-22 mesi con dati pace reale
- Gap Tier 1: Resilience patterns (Circuit Breaker, Retry) → SE P2 Chat App W5
- Gap Tier 2: Observability base (OpenTelemetry, correlation ID) → AQ P1 W15-16 + SE P1 W2
- Gap Tier 3: Exploration backlog → AI Frontier Lab
- Career-boost aggiornato (budget ore, system design reordered, LinkedIn headline AI Engineer)
- Verificato codice SE P1: W1 è al 95% (non 80%) — aggiornato TODO
- Verificato codice AQ P1: W1-W4 coerenti col codice, 220+ test
- **NOTA:** Progress.md disallineato (XP 3864 vs 4169, level 6 vs 5). Da sistemare.

---

## Prossima Sessione

**Opzioni:**
1. **Spaced repetition** (OBBLIGATORIA — quiz scaduti!)
2. Finisci SE P1 W1: solo LoggingBehavior → poi W1 completata
3. Inizia AQ W5 (Message Queue — Azure Service Bus o RabbitMQ)
4. Sistemare Progress.md (riallineare XP history)

**Piano parallelo:** 70% Architect Quest + 30% Senior Engineer (2 sessioni AQ + 1 SE)
**Focus:** Ogni decisione architetturale va vista anche in ottica AI Engineer

---

## Decisioni Attive

- **Percorsi in parallelo:** B - Parallelo Sfalsato (deciso 2026-02-02)
- **Senior Engineer workflow:** Compartimento stagno con recap exercises
- **Percorso Minimo ~20-22 mesi:** Approvato (2026-03-13, ricalibrato 2026-03-24 con pace reale). Focus su AQ P1+P2.5+P2 e SE P1+P1.5+P2+P3. Il resto e Percorso Completo post-lavoro.
- **AI Engineer target primario:** Deciso 2026-03-24. Roadmap AI Skills aggiornata con +5 gap (Evals, Guardrails, Multi-Agent, AI Testing, Fine-tuning). Career strategy riallineata.
- **Quiz nomenclatura:** Source mapping per ogni prefisso quiz. Tabella overlap noti per evitare duplicati (2026-03-24)
- **Quiz regola Box 1:** Minimo 2 quiz Box 1 non-risposti + 1 CLCODE per sessione (2026-03-24)
- **Cross-linking obbligatorio:** Ogni Knowledge note deve avere [[links]] a concetti correlati (2026-03-24)

---

## Domande Aperte

Nessuna.

---

*Ultimo aggiornamento: 2026-03-24 (sessione 3 - refactor progetto + coerenza contesto)*
