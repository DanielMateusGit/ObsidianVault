# Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto AQ** | P1 Notification Service |
| **Settimana AQ** | Week 5 COMPLETATA ✅ → SEDIMENTAZIONE W5 |
| **Progetto SE** | P1 Task Manager |
| **Settimana SE** | W1 COMPLETATA ✅ → W2 Infrastructure + API |
| **Task corrente** | Sedimentazione AQ W5 (letture) + SE P1 W2 |

---

## Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 5600 |
| **Livello** | 7 - System Designer (LEVEL UP! 🎉) |
| **Streak** | 12 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement** | 10 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire, First Exam, First Lesson, Course Master, Perfect Score) |
| **Certificazioni** | 1 (Claude Code in Action - 8/8 Perfect Score) |

---

## Architect Quest - Status

| Progetto | Status | Periodo |
|----------|--------|---------|
| P1 - Notification Service | In corso | W5 ✅ → Sedimentazione |
| P2 - NutriPlan | Locked | M5-9 |
| P2.5 - AI Gateway | Locked | M5-6 |
| P3 - BookingHub | Locked | M10-14 |
| P4 - FamilyBudget | Locked | M15-18 |
| P5 - FitHub | Locked | M19-22 |

### Week 5 Completata (450/450 XP) — 2026-03-28
- Message Queue (RabbitMQ), Outbox Pattern, Retry + DLQ applicativa
- OutboxMessage, OutboxStore, OutboxProcessor, DeliveryAttemptRepository
- NotificationWorker con retry logic (CanRetry + DeliveryAttempts + Outbox per re-publish)
- ADR-004: Message Queue Strategy
- 294 test totali (185 Domain + 74 Application + 35 Infrastructure)
- 4 note: message-queues, rabbitmq-fundamentals, outbox-pattern, retry-error-handling

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
| W1 | Domain + Application Layer | COMPLETATA ✅ (36 Domain + 25 Application test) |
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
8. ~~LoggingBehavior~~ ✅ (con test, 2026-03-31) — W1 COMPLETATA

---

## Ultima Sessione

**Data:** 2026-03-31
**Tipo:** Quiz + Codice + Note (Misto)

- **Spaced repetition**: 18 quiz (7✅ 8🟡 3❌), challenge #15
- **Note arricchite**: retry-error-handling.md e outbox-pattern.md — aggiunte spiegazioni discorsive, diagrammi semplificati, testo esplicativo per ogni flusso
- **SE P1 W1 completata**: LoggingBehavior implementato con TDD (2 test)
  - ILogger<T>, Stopwatch, try/catch con rethrow
  - Pipeline behavior pattern: logging osserva, non decide
- **00-Overview.md aggiornato** per allineare al codice reale
- **Esame Mese 2 posticipato** al 2026-04-07
- **Reading list aggiornata** con risorse Sedimentazione W5
- **LEVEL UP** → Livello 7 System Designer!
- +261 XP

---

## Prossima Sessione

**Opzioni:**
1. **Spaced repetition** (OBBLIGATORIA — molti quiz tornati in Box 1 da questa sessione)
2. **Sedimentazione AQ W5** — Dan racconta cosa ha letto su messaging/RabbitMQ → Knowledge notes
3. **SE P1 W2** — Infrastructure + API Layer (DbContext, Repos, Migrations, Controllers, DI, Serilog)
4. **Esame Mese 2** (posticipato al 2026-04-07)

**Piano:** Letture Sedimentazione W5 (RabbitMQ tutorials, Reliability Guide, Outbox articoli) → Sedimentazione → SE P1 W2

---

## Decisioni Attive

- **Percorsi in parallelo:** B - Parallelo Sfalsato (deciso 2026-02-02)
- **Senior Engineer workflow:** Compartimento stagno con recap exercises
- **Percorso Minimo ~20-22 mesi:** Approvato (2026-03-13, ricalibrato 2026-03-24 con pace reale). Focus su AQ P1+P2.5+P2 e SE P1+P1.5+P2+P3. Il resto e Percorso Completo post-lavoro.
- **AI Engineer target primario:** Deciso 2026-03-24. Roadmap AI Skills aggiornata con +5 gap (Evals, Guardrails, Multi-Agent, AI Testing, Fine-tuning). Career strategy riallineata.
- **Quiz nomenclatura:** Source mapping per ogni prefisso quiz. Tabella overlap noti per evitare duplicati (2026-03-24)
- **Quiz regola Box 1:** Minimo 10 quiz Box 1 non-risposti + 1 CLCODE per sessione (aggiornato 2026-03-25, era 2)
- **Cross-linking obbligatorio:** Ogni Knowledge note deve avere [[links]] a concetti correlati (2026-03-24)
- **n8n Prototype Practice:** Sandwich PRIMA+DOPO per ogni progetto da P2 in poi. Per P1 AQ/SE solo DOPO. (2026-03-26)
- **Messaging progressivo SE:** Redis Pub/Sub (P1 W3) → RabbitMQ (P2 W5) → Outbox TDD (P3 W10) → Multi-service completo (P4 W11). Deciso 2026-03-28.

---

## Domande Aperte

Nessuna.

---

*Ultimo aggiornamento: 2026-03-31 (SE W1 completata + LoggingBehavior + LEVEL UP 7 + note arricchite)*
