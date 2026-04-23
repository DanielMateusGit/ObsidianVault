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
| **XP Totali** | 6702 |
| **Livello** | 7 - System Designer (498 XP al prossimo) |
| **Streak** | 2 giorni |
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

**Data:** 2026-04-23
**Tipo:** Strategy + Refactor (Job-Postings-Driven Enrichment + Sistema Pulizia)

- **Job-postings analysis batch 1 completato:** 28 annunci totali (8 AI + 12 SE + 6 FE + 2 Architect skipped)
- **3 roadmap arricchite job-driven:**
  - `ai-skills.md` v3.1: 4 cluster + Modulo 5.5 LangChain/LangGraph + ReAct/CoT/Memory + Python AI Bridge + AI Mini-Projects
  - `senior-frontend.md` v2.1: 6 cluster + P6 AI-Native FE + 3 moduli trasversali (TS Craft + Modern Testing + FE Security) con 10 topic ciascuno + FE Mini-Projects
  - `senior-engineer.md` v6.1: 6 cluster + 6 moduli trasversali (Polyglot + Observability + Cloud-Native + IaC + CI/CD + AI Engineering CORE) + Enterprise Identity Standards + SE Mini-Projects + 10 achievement
- **Architect Quest:** analizzata e skipped (roadmap già allineata su fundamentals)
- **Refactor sistema completo:** 12 issues identificati (3 CRITICAL + 4 HIGH + 4 MEDIUM + 1 LOW) → tutti risolti
- **2 nuovi canonical sources creati:**
  - `context/cluster-taxonomy.md` (centralizza 16 cluster mappati)
  - `context/mini-projects-index.md` (30 mini-projects + sinergia cross-roadmap)
- **Cascade aggiornamenti:** career-strategy v2.0, gamification v2.0, tech-stack v2.0, files.md, CLAUDE.md, career-boost v2.0
- **Filosofia stack secondario applicata:** Java/Spring Boot e Python deep "on the job" (no over-investment upfront)
- **Memoria persistente** aggiornata con tassonomia 4+6+6 cluster
- +700 XP (sessione strategy/refactor profonda)

---

## Prossima Sessione

**Opzioni (cluster-aware):**

1. **Spaced repetition** (OBBLIGATORIA — molti quiz Box 2+ in coda)

2. **SE P1 M2** — Exception Handling Middleware, Serilog + Correlation ID, Swagger, Integration tests, API tests
   → Cluster target: **SE #5 Modern Full-Stack** (bridge 3-6 mesi)

3. **Sedimentazione AQ M5** — Knowledge notes su messaging/RabbitMQ
   → Cluster target: **SE #2 Fintech Low-Latency** (consolidamento concettuale)

4. **Esame tematico Messaging & Persistence** — prerequisiti ✅ (M4+M5 AQ P1)

5. **AI Mini-Project #1** — primo micro-progetto AI-built da pubblicare GitHub
   → Cluster target: **AI #4 AI-Augmented SWE** (bridge 3-6 mesi ⭐)
   → Idee priority dal backlog (`context/mini-projects-index.md`):
      - **AI changelog generator** (3-5 giorni, low effort, dimostra Claude Code mastery)
      - **Lead scoring agent** (1 settimana, business angle forte)
      - **MCP server pubblico** (1 settimana, dual-use AI #2 + SE #1)

6. **FE Mini-Project #1** — D3 chart library standalone (1 settimana)
   → Cluster target: **FE #3 Scale-up React FE** + **FE #6 Data-Heavy AI FE** (dual-use)

7. **Job-postings batch 2** — Dan incolla altri 3-5 annunci → ulteriore enrichment

**Piano consigliato:** Quiz + SE P1 M2 + parallelo "AI Mini-Project #1" (AI changelog generator come quick win, 3-5 giorni, sblocca cluster #4 candidatura).

---

## Job Market Analysis Tracking

**Last reviewed:** 2026-04-23 (batch 1 completo per 4 roadmap)

| Roadmap | Annunci analizzati | Cluster identificati | Status |
|---------|---------------------|----------------------|--------|
| AI Skills | 8 (IT+UK) | 4 cluster | ✅ Roadmap v3.1 enriched |
| Senior Engineer | 12 (UK+remote) | 6 cluster | ✅ Roadmap v6.0 enriched |
| Senior Frontend | 6 (UK) | 6 cluster | ✅ Roadmap v2.0 enriched |
| Architect Quest | 2 (Tesla, Deel) | — | ⏭️ Skipped (already aligned) |
| **Total** | **28 annunci** | **16 cluster mappati** | |

**Files:** `context/job-postings-*.md` + canonical `context/cluster-taxonomy.md`

---

## Decisioni Attive

- **AI Skills roadmap job-driven:** Deciso 2026-04-23. Roadmap `ai-skills.md` arricchita con gap analysis su 8 annunci (IT + UK). Identificati 4 cluster di ruolo: #4 AI-Augmented SWE (bridge accessibile 3-6 mesi), #3 Full-Stack AI-First, #2 AI Engineer GenAI/LLMOps (target principale), #1 AI Tech Lead Enterprise (long-game). Path strategico: cluster #4 → #3 → #2.
- **Senior Frontend roadmap job-driven:** Deciso 2026-04-23. Roadmap `senior-frontend.md` arricchita con gap analysis su 6 annunci UK. Identificati 6 cluster di ruolo FE: #1 Enterprise FE, #2 Modern Fintech FE, #3 Scale-up React FE (3-6 mesi accessibile ⭐), #4 Founding FE (£90-130k+ premium), #5 AI-Native FE (sweet spot AI+FE), #6 Data-Heavy AI FE. Aggiunto P6 AI-Native FE Showcase, espanso P2 con D3/Visx mastery, moduli trasversali TypeScript Craft + Modern Testing + Frontend Security, FE Mini-Projects Portfolio (5-10 micro-progetti GitHub).
- **Senior Engineer roadmap job-driven:** Deciso 2026-04-23. Roadmap `senior-engineer.md` arricchita v6.0 con gap analysis su 12 annunci UK/remote. Identificati 6 cluster di ruolo Senior IC: #1 AI-Native Backend, #2 Fintech Low-Latency, #3 Infrastructure/SRE, #4 Fintech Java, #5 Modern Full-Stack (3-6 mesi accessibile ⭐), #6 Consulting Polyglot. Aggiunti 6 moduli trasversali: Stack Polyglot Awareness + Modern Observability + Cloud-Native Deployment + IaC (Terraform) + CI/CD Pipelines + AI Engineering Integration (promosso da bonus a CORE). Espanso P1.5 con Enterprise Identity Standards (OAuth2/OIDC/SAML/SCIM/Auth0). Aggiunta SE Mini-Projects Portfolio (5-10 mini-projects backend GitHub).
- **Architect Quest roadmap:** Analizzata 2026-04-23 con 2 annunci (Tesla, Deel). Decisione: NON arricchire — roadmap già allineata sui fundamentals (build solid + leadership + production ownership > buzzword architetturali). File `context/job-postings-architect.md` archiviato come "skipped-roadmap-already-aligned".
- **Python AI Bridge Project:** Deciso 2026-04-23. Progetto parallelo a P2.5 — replica subset funzionale in Python (FastAPI + LangGraph + pgvector + Ragas + Langfuse). Razionale: 8/8 annunci AI richiedono Python, .NET non basta per candidature AI. Trigger: completamento P2.5 Phase 2.
- **AI Mini-Projects Portfolio:** Deciso 2026-04-23. Track parallela di 5-10 micro-progetti GitHub AI-built (Claude Code/Cursor) con README pro + demo live. Razionale: portfolio pubblico è prerequisito di candidatura cluster #4 (es. Homey UK richiede in fase application).
- **Job-postings tracking:** Nuovo file `claude/context/job-postings-analysis.md` per accumulare annunci + gap analysis. Cadenza: aggiornare ai-skills.md ogni 3-5 nuovi annunci.
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

*Ultimo aggiornamento: 2026-04-23 (refactor sessione job-postings-driven enrichment + pulizia: cascade decisions + Cluster Positioning + Job Market Tracking + cluster-aware Prossima Sessione)*

*Versione precedente: 2026-04-17 (refactor self-paced: rimossa timeline, esami completion-based, Week→Modulo)*
