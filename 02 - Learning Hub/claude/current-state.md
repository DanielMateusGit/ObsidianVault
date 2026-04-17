# Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorso attivo** | Entrambi in parallelo (focus primario: Architect Quest) |
| **Progetto AQ** | P1 Notification Service |
| **Modulo AQ** | Modulo 5 COMPLETATO ✅ → SEDIMENTAZIONE M5 |
| **Progetto SE** | P1 Task Manager |
| **Modulo SE** | M1 COMPLETATO ✅ → M2 Infrastructure + API |
| **Task corrente** | Sedimentazione AQ M5 (letture) + SE P1 M2 |

---

## Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 6002 |
| **Livello** | 7 - System Designer (1198 XP al prossimo) |
| **Streak** | 1 giorno (reset dopo 6gg pausa) |
| **Data inizio** | 2025-01-29 |
| **Achievement** | 10 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire, First Exam, First Lesson, Course Master, Perfect Score) |
| **Certificazioni** | 1 (Claude Code in Action - 8/8 Perfect Score) |

---

## Architect Quest - Status

| Progetto | Status | Prerequisiti |
|----------|--------|--------------|
| P1 - Notification Service | In corso | M5 ✅ → Sedimentazione |
| P2.5 - AI Gateway | Locked | Completamento P1 |
| P2 - NutriPlan | Locked | Completamento P2.5 |
| P3 - BookingHub | Locked | Completamento P2 |
| P4 - FamilyBudget | Locked | Completamento P3 |
| P5 - FitHub | Locked | Completamento P4 |

### Modulo 5 Completato (450/450 XP) — 2026-03-28
- Message Queue (RabbitMQ), Outbox Pattern, Retry + DLQ applicativa
- OutboxMessage, OutboxStore, OutboxProcessor, DeliveryAttemptRepository
- NotificationWorker con retry logic (CanRetry + DeliveryAttempts + Outbox per re-publish)
- ADR-004: Message Queue Strategy
- 294 test totali (185 Domain + 74 Application + 35 Infrastructure)
- 4 note: message-queues, rabbitmq-fundamentals, outbox-pattern, retry-error-handling

### Modulo 4 Completato (400/400 XP)
- Infrastructure Layer, Repository Pattern, EF Core, Value Object Persistence, Integration Tests
- 268 test totali (185 Domain + 72 Application + 11 Infrastructure)
- Esame tematico "Clean Arch + Domain + Infrastructure": 25/30 (Superato con merito)

---

## Senior Engineer - Status

| Progetto | Status | Prerequisiti |
|----------|--------|--------------|
| P1 - Task Manager | In corso (iniziato 2026-03-02) | — |
| P1.5 - Auth & Security | Locked | Completamento P1 |
| P2 - Chat App | Locked | Completamento P1.5 |
| P3 - E-commerce | Locked | Completamento P2 |
| P4 - Alert Gateway | Locked | Completamento P3 |
| P5 - URL Shortener | Locked | Completamento P4 |
| P6 - Capstone | Locked | Completamento P5 |

### P1 Task Manager - Moduli

| Modulo | Focus | Status |
|--------|-------|--------|
| M1 | Domain + Application Layer | COMPLETATO ✅ (36 Domain + 25 Application test) |
| M2 | Infrastructure + API Layer | In corso |
| M3 | Redis + Patterns + Boss Battle | Da fare |

**Regole Senior Engineer:** 70% coding, 30% teoria. Dan scrive, Claude guida. TDD rigoroso.

### TODO Senior P1
1. ~~IUnitOfWork - Interface in Application~~ ✅
2. ~~Commands (Create, Complete, Update, Delete)~~ ✅
3. ~~Recap #5 - CompleteTaskCommand da solo~~ ✅
4. ~~Queries (GetById, GetAll, GetByStatus)~~ ✅
5. ~~DTOs per response~~ ✅ (TaskItemDto record)
6. ~~FluentValidation sui Commands~~ ✅ (4 validators)
7. ~~ValidationBehavior~~ ✅ (con test)
8. ~~LoggingBehavior~~ ✅ (con test, 2026-03-31) — M1 COMPLETATO

---

## Ultima Sessione

**Data:** 2026-04-10
**Tipo:** Quiz + Codice (SE P1 M2)

- **Spaced repetition**: 5 quiz (2✅ 2🟡 1❌), COUP-01 Box2→3, QRY-01 Box3→4, LSP-01/INFRA-04 tornano Box1, UOW-02 ancora sbagliato
- **TaskEndpoints**: Minimal API con MapGroup, 7 endpoint (CRUD + Complete + ByStatus)
- **Teoria**: Minimal API vs Controllers, MapGroup, ISender vs IMediator, Send vs Publish, parameter binding
- **Program.cs**: aggiunto MapTaskEndpoints()
- 61 test verdi, build OK
- +122 XP

---

## Prossima Sessione

**Opzioni:**
1. **Spaced repetition** (OBBLIGATORIA — molti quiz Box 2+ in coda)
2. **SE P1 M2** — Continuare: Exception Handling Middleware, Serilog + Correlation ID, Swagger, Integration tests, API tests
3. **Sedimentazione AQ M5** — Dan racconta cosa ha letto su messaging/RabbitMQ → Knowledge notes
4. **Esame tematico Messaging & Persistence** — sblocca al completamento M4+M5 AQ P1 (prerequisiti: ✅)

**Piano:** Quiz + SE P1 M2 (Exception Middleware → Serilog → Tests)

---

## Decisioni Attive

- **Percorsi in parallelo:** B - Parallelo Sfalsato (deciso 2026-02-02)
- **Senior Engineer workflow:** Compartimento stagno con recap exercises
- **Percorso self-paced:** Deciso 2026-04-17. Eliminata ogni timeline (18-22 mesi, M1-M22, "fine mese"). Si avanza per completamento, non per calendario. Esami trigger dai moduli completati, non da date.
- **AI Engineer target primario:** Deciso 2026-03-24. Roadmap AI Skills aggiornata con +5 gap (Evals, Guardrails, Multi-Agent, AI Testing, Fine-tuning). Career strategy riallineata.
- **Quiz nomenclatura:** Source mapping per ogni prefisso quiz. Tabella overlap noti per evitare duplicati (2026-03-24)
- **Quiz regola Box 1:** Minimo 10 quiz Box 1 non-risposti + 1 CLCODE per sessione (aggiornato 2026-03-25, era 2)
- **Quiz spaced repetition a rotazione:** Dal 2026-04-17, Box 2=2 sessioni attesa, Box 3=4, Box 4=8, Box 5=16. Nessuna data, solo contatore sessioni.
- **Cross-linking obbligatorio:** Ogni Knowledge note deve avere [[links]] a concetti correlati (2026-03-24)
- **n8n Prototype Practice:** Sandwich PRIMA+DOPO per ogni progetto da P2 in poi. Per P1 AQ/SE solo DOPO. (2026-03-26)
- **Messaging progressivo SE:** Redis Pub/Sub (P1 M3) → RabbitMQ (P2 M5) → Outbox TDD (P3 M10) → Multi-service completo (P4 M11). Deciso 2026-03-28.

---

## Domande Aperte

Nessuna.

---

*Ultimo aggiornamento: 2026-04-17 (refactor self-paced: rimossa timeline, esami completion-based, Week→Modulo)*
