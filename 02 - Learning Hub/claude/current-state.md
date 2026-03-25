# Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto AQ** | P1 Notification Service |
| **Settimana AQ** | Week 5 IN CORSO (teoria completata, codice prossima sessione) |
| **Progetto SE** | P1 Task Manager |
| **Settimana SE** | W1 95% (Domain ✅, Commands ✅, Queries ✅, DTOs ✅, Validators ✅, ValidationBehavior ✅ — manca solo LoggingBehavior) |
| **Task corrente** | AQ P1 W5 codice (IMessagePublisher, Worker) + SE P1 W1 (LoggingBehavior) |

---

## Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 4399 |
| **Livello** | 6 - Domain Master |
| **Streak** | 7 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement** | 10 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire, First Exam, First Lesson, Course Master, Perfect Score) |
| **Certificazioni** | 1 (Claude Code in Action - 8/8 Perfect Score) |

---

## Architect Quest - Status

| Progetto | Status | Periodo |
|----------|--------|---------|
| P1 - Notification Service | In corso | W5 in corso |
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

**Data:** 2026-03-25
**Tipo:** Misto (Spaced Repetition + AQ P1 W5 Teoria)

- Spaced repetition: 7 quiz (5✅, 2🟡), 2 padroneggiati (DIP-03, FAC-01 → Box 5)
- Iniziata AQ P1 Week 5: Message Queue — teoria completata (3 note progetto)
- Create 2 Knowledge notes .NET Fundamentals (CancellationToken, Task)
- Fix frontmatter note SE P1 W1 + rimosso duplicato
- Aggiornata nota coding-assistant-vs-llm (chiarita ambiguita + sezione Agentic Loop)
- 35 nuovi quiz aggiunti al tracker
- Quiz regola Box 1: da 2 a 10 per sessione
- **LEVEL UP: 6 - Domain Master!** (4399 XP)
- **NOTA:** Progress.md ancora disallineato. Da sistemare.

---

## Prossima Sessione

**Opzioni:**
1. **Spaced repetition** (OBBLIGATORIA — 10 Box 1 + scaduti + 1 CLCODE)
2. **AQ P1 W5 — CODICE:** docker-compose RabbitMQ, IMessagePublisher, RabbitMqPublisher, integrazione handler, worker
3. Finisci SE P1 W1: solo LoggingBehavior → poi W1 completata
4. Outbox Pattern (teoria, dopo flusso base funzionante)
5. Sistemare Progress.md (riallineare XP history)

**Piano parallelo:** 70% Architect Quest + 30% Senior Engineer (2 sessioni AQ + 1 SE)
**Focus:** Ogni decisione architetturale va vista anche in ottica AI Engineer

---

## Decisioni Attive

- **Percorsi in parallelo:** B - Parallelo Sfalsato (deciso 2026-02-02)
- **Senior Engineer workflow:** Compartimento stagno con recap exercises
- **Percorso Minimo ~20-22 mesi:** Approvato (2026-03-13, ricalibrato 2026-03-24 con pace reale). Focus su AQ P1+P2.5+P2 e SE P1+P1.5+P2+P3. Il resto e Percorso Completo post-lavoro.
- **AI Engineer target primario:** Deciso 2026-03-24. Roadmap AI Skills aggiornata con +5 gap (Evals, Guardrails, Multi-Agent, AI Testing, Fine-tuning). Career strategy riallineata.
- **Quiz nomenclatura:** Source mapping per ogni prefisso quiz. Tabella overlap noti per evitare duplicati (2026-03-24)
- **Quiz regola Box 1:** Minimo 10 quiz Box 1 non-risposti + 1 CLCODE per sessione (aggiornato 2026-03-25, era 2)
- **Cross-linking obbligatorio:** Ogni Knowledge note deve avere [[links]] a concetti correlati (2026-03-24)

---

## Domande Aperte

Nessuna.

---

*Ultimo aggiornamento: 2026-03-25 (sessione — spaced repetition + AQ P1 W5 teoria)*
