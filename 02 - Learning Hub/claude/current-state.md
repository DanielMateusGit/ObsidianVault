# Stato Attuale

> **AGGIORNA QUESTO FILE DOPO OGNI SESSIONE**

## Focus Corrente

| Campo | Valore |
|-------|--------|
| **Percorsi attivi** | 3 paralleli: Architect Quest (primario) + Senior Engineer + **English UK** (formazione professionale) |
| **Progetto AQ** | P1 Notification Service |
| **Modulo AQ** | Modulo 5 COMPLETATO ✅ → SEDIMENTAZIONE M5 |
| **Progetto SE** | P1 Task Manager |
| **Modulo SE** | M1 COMPLETATO ✅ → M2 Infrastructure + API |
| **English Track** | B2.3 → C1+ · 58 card (49 Thursday Murder Club + 9 grammar-corrections) · 0 journal entries |
| **Task corrente** | SE P1 M2 FASE 2 (Domain extension) — safety net test in place ✅ + Sedimentazione AQ M5 + English |

---

## Progress

| Metrica | Valore |
|---------|--------|
| **XP Totali** | 7452 |
| **Livello** | 8 - **Cloud Engineer** ☁️ (1548 XP al prossimo, target Lv.9 Principal Developer @ 9000) |
| **Streak** | 4 giorni |
| **Data inizio** | 2025-01-29 |
| **Achievement** | 10 (First Commit, Docker Newbie, Architect Apprentice, Spark, Knowledge Seeker, On Fire, First Exam, First Lesson, Course Master, Perfect Score) |
| **Certificazioni completate** | 1 (Claude Code in Action - 8/8 Perfect Score) |
| **Certificazioni in corso** | 1 (Claude Code 101 - iniziata 2026-04-28) |
| **Certificazioni in pipeline** | AZ-204 (Tier 1, Year 1), Terraform Associate (Tier 1, Year 1), AZ-400 o CKAD (Tier 2, Year 2), AWS DVA-C02 + GCP Pro Cloud Dev (Tier 3, Year 3) |

> **Hub certificazioni:** `Certifications/` (struttura creata 2026-04-28). Tracker per cert in `Certifications/[cert-slug]/tracker.md`. Note atomiche restano in `Knowledge/ai/claude/`.

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
| M2 | Infrastructure + API Layer | 🚧 In corso (FASE 1 di 6 ✅ — Testcontainers + first integration test green 2026-05-07) |
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

**Data:** 2026-05-07
**Tipo:** Misto — Spaced Repetition + Coding (SE M2 FASE 1) + Knowledge note + Strategic planning + English cards
**Durata:** Sessione lunga densa (multiple hour blocks)

- **Spaced rep 8 quiz** (3✅ 1🟡 4❌, +43 XP). Errori spiegati a livello "bambino" per consolidamento. CLCODE-01 (LLM vs Coding Assistant), CMD-01 (Create return type), VAL-01 (CQS/TryExecute), CL101-01 (4 fasi agentic loop).
- **SE P1 M2 FASE 1 ✅ COMPLETATA**: Audit codice esistente → identificate incoerenze (DueDate VO orfano, Project/Tag isolate, Description nullable mismatch, dispatch eventi mancante) → decisione strategica refactor consapevole (A3+B1+C1) in 6 fasi → eseguita FASE 1: Testcontainers.PostgreSql NuGet + `PostgresFixture.cs` (IAsyncLifetime + container + DbContext + MigrateAsync) + `TaskItemRepositoryTests.cs` con primo integration test → **VERDE al primo run** 🎉. 5 invarianti verificate.
- **Knowledge note creata**: `Knowledge/databases/ef-core-configurations-and-migrations.md` (4 quiz embedded, status/learning, capture le Q&A su 3-layer rules, migration generation, MigrateAsync vs EnsureCreatedAsync). Knowledge: 24 → 25 note.
- **English UK**: deck `grammar-corrections.md` creato con 9 cards (5 + 4) — pattern catturati da production libera in chat. Memory feedback salvati (card format = question, dictation = ignore punctuation). Total cards: 49 → 58.
- **Strategic decisions**:
  - Switch deployment learning approach: certificazioni invece di hands-on FT items
  - Tier 1 cert pipeline definita: **AZ-204 + Terraform Associate** (Year 1)
  - .NET Aspire bundled in AZ-204 prep (no separate module)
- **Roadmap audit deployment**: ~65-70% coverage. Gap critici: Azure App Service hands-on, Cloud Run, ECS, release engineering, Aspire. Audit completo via Explore agent.
- **+268 XP** → **🎉 LEVEL UP a Lv.8 Cloud Engineer** ☁️ (threshold 7200 superato).
- **Post-end micro-session** (`/quiz` di follow-up dopo level up): 5 quiz misti (2✅ 2🟡 1❌). +32 XP → 7452 totale. Pattern emersi: confondere "componenti del modello" vs "gerarchia di priorità" (EFCM-01); ripetere stesso motivo in parole diverse (REPO-01 5° parziale). Worth deliberate reread: `Knowledge/patterns/repository-pattern.md`.

---

## Sessione Precedente

**Data:** 2026-05-06
**Tipo:** Init only (check-in, nessuna attività produttiva)

- `/init` eseguito + lettura completa contesto
- Status review: 35 quiz Box 2+ in coda + 21 parziali da recuperare + 119 Box 1 non risposti (carico spaced rep alto)
- English B2.3, 49 card Box 1 nuove (Thursday Murder Club ch.6-9), streak journaling 0
- `/end` invocato senza svolgere attività → 0 XP

---

## Sessione Antecedente

**Data:** 2026-04-24
**Tipo:** Strategy (Fast Track roadmap v1.0 cross-roadmap) + Refactor post-creazione

- **Creata `roadmaps/fast-track.md` v1.0** — roadmap conduttore cross-roadmap con 29 topic max CV-ROI estratti da tutte le roadmap (AI / SE / FE / AQ / Career Boost) organizzati in 3 Fasi:
  - Fase 1 — Entry AI-Augmented SWE (8 item): MCP server, Python AI Bridge skeleton, LangChain chain base, prompt library, 3 AI mini-projects, guardrails
  - Fase 2 — AI Engineering Core Cluster #2 (8 item): vector DB, RAG slice, hybrid retrieval, Ragas eval, LangGraph agent, multi-agent ReAct, semantic caching, responsible AI
  - Fase 3 — Production Polish Cross (13 item): observability, Docker/deploy/Terraform/CI-CD, TypeScript Craft, Streaming UI, Modern Testing, FE Security, System Design, OSS contribution
- **Sincronizzazione bidirezionale progettata:** item ✅ in fast-track → sorgente completato; item 🟡 → sorgente "già affrontato". `/end` skill aggiornato con regola sync esplicita
- **/refactor eseguito** post-creazione: 0 CRITICAL, 2 WARN + 1 LOW applicati (link Sequenza consigliata in CLAUDE.md, sezione Sync Fast Track in `/end` SKILL, nota XP-sync in quiz-tracker.md)
- **Falsi positivi dell'agent scartati:** rejected "Fine-tuning Tier 1" (viola filosofia "no Python deep upfront") + "Production LLM Patterns Tier 1" (già coperti FT-A04 + FT-B07)
- **Cascade updates:** current-state.md (Decisioni Attive + Prossima Sessione fast-track friendly), CLAUDE.md (struttura roadmaps + sezione Fast Track con sequenza), memoria persistente project_fast_track_roadmap.md
- **Anchor validity verificata:** tutti i riferimenti `source` degli item fast-track puntano a sezioni esistenti nelle roadmap sorgente
- +450 XP (sessione strategica profonda)

---

## Sessione Pre-Antecedente

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

**Opzioni (post-FASE 1 SE M2 + cert pipeline definita):**

1. **SE P1 M2 FASE 2 ⭐** — Domain extension (Description, DueDate VO, Project/Tag relations) + Domain tests. Safety net (integration tests) ora c'è — refactor confidente.
   → Cluster target: **SE #5 Modern Full-Stack**

2. **Più integration tests + cleanup pattern** — Respawn library o transaction-rollback tra test (oggi 1 solo test, prossimi multi-test richiedono isolation strategy).

3. **Sedimentazione**: completare le 4 Knowledge notes pending da oggi:
   - `dotnet/nullable-reference-types.md` (`?` vs `null!`)
   - `architecture/testing/testcontainers-vs-inmemory.md`
   - `architecture/testing/xunit-fixture-lifecycle.md`
   - `architecture/deployment/container-orchestration-patterns.md`

4. **Spaced repetition** (still alta: 31 Box 2+ in coda + 21 parziali + 117 Box 1)

5. **English** — primo passaggio sulle 58 card Box 1 (vocab + grammar corrections oggi)

6. **AZ-204 prep** — partire la cert pipeline. Capitolo 1 Microsoft Learn syllabus + creare quiz tracker per AZ204-NN

7. **Roadmap edits pendenti** (low priority): aggiungere FT-C-Concepts a fast-track + aggiornare AQ P2 Aspire come AZ-204 prep

**Piano consigliato (sessione media):** Quiz scaricamento coda → SE P1 M2 FASE 2 step 1-2 (Description + DueDate aggiunti a TaskItem). Momentum alto, sfrutta safety net.

**Piano consigliato (sessione corta <2h):** Quiz + 1-2 Knowledge notes pending (capture concetti prima che svaniscano).

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

- **Certification-based deployment learning (Tier 1: AZ-204 + Terraform Associate):** Deciso 2026-05-07. Dopo audit roadmap deployment (~65-70% coverage, gap critici: Azure App Service hands-on, Cloud Run, release engineering, Aspire), Dan ha scelto strategia cert-based invece di hands-on FT items. Razionale: certs danno curriculum strutturato + CV value + forced cadence. Tier 1 (Year 1): AZ-204 (copre App Service, Functions, Container Apps, AKS basics, Cosmos, Service Bus, Aspire) + HashiCorp Terraform Associate. Tier 2 (Year 2): AZ-400 o CKAD. Tier 3 (Year 3): AWS DVA-C02 + GCP Pro Cloud Dev. .NET Aspire bundled in AZ-204 prep (no cert dedicata). Vedi `career-strategy.md` > Certification Roadmap.

- **SE P1 M2 refactor consapevole (path A3 + B1 + C1):** Deciso 2026-05-07. Codice attuale ha incoerenze (DueDate VO orfano, Project/Tag isolate, Description nullable mismatch, dispatch eventi mancante) ma compila e ha test verdi. Decisione: NO rollback, refactor TDD-driven in 6 FASI (FASE 1 ✅ Testcontainers + integration tests safety net → FASE 2 Domain extension → FASE 3 Configuration update → FASE 4 Domain Events dispatch → FASE 5 Application cleanup → FASE 6 API hardening). Razionale: il "before" del refactor è il miglior insegnante.

- **English UK track come percorso paritetico:** Deciso 2026-05-05. Il percorso `English/` (vivere a Londra, B2.3 → C1+) è **alla pari** dei percorsi tech (AI Engineer / Senior Engineer / Architect Quest) come parte della formazione professionale per il mercato UK. Non è un side track. Sistema flashcards Box 1-6 incrementale/decrementale, skill `/english` + `/journal` parametrizzato, EXP separato in `English/stats.md`. Auto-promotion livello DISABLED (Dan promuove). Vedi `English/CLAUDE.md`.
- **Fast Track roadmap cross-roadmap:** Deciso 2026-04-24. Nuovo file `roadmaps/fast-track.md` (v1.0) conduttore parallelo a tutte le roadmap: estrae 29 topic con massimo CV-ROI per minimo effort, organizzati in 3 Fasi (Entry AI #4 → AI Core #2 → Polish Cross). Sincronizzazione: item completato 100% in fast-track → completato anche in roadmap sorgente; parziale → "già affrontato" nella sorgente. Pensata per sessioni corte quando Dan vuole il massimo valore immediato. Consultare prima di proporre topic di sessione.
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

*Ultimo aggiornamento: 2026-05-07 (post-end micro quiz session: +32 XP, REPO-01 5° parziale flagged, pattern "componenti vs gerarchia" e "ripetizione motivo" identificati). XP day total: 7452.*

*Versione precedente: 2026-05-07 (sessione massiva — SE M2 FASE 1 completa con Testcontainers + first integration test verde, 1 Knowledge note creata, 9 English cards, cert pipeline AZ-204+Terraform definita, +268 XP, **LEVEL UP a Lv.8 Cloud Engineer**)*

*Versione precedente: 2026-05-06 (sessione init-only chiusa subito — 0 XP, log creato per coerenza; alert spaced rep tech alto al rientro)*

*Versione precedente: 2026-05-05 (post-English /refactor — 3 CRITICAL + 2 WARN + 1 LOW: skill /refactor /end /context integrate con English; profile.md Italia→Londra + English B2.3→C1+ aggiunto a competenze; career-strategy English C1+ prerequisito UK; rimossa duplicazione Box 1-6 in claude/CLAUDE.md)*

*Versione precedente: 2026-05-05 (English UK track v1.0 paritetico — `English/` setup, skill `/english` + `/journal` parametrizzato, deck Thursday Murder Club migrato 49 card, current-state riposizionato come "3 percorsi paralleli", memoria persistente Dan-a-Londra-B2.3 + English-paritetico)*

*Versione precedente: 2026-05-05 (/refactor — 3 CRITICAL + 5 WARN + 2 LOW applicati: skill /init, /quiz, /refactor, /context allineate a self-paced + canonical sources; profile.md timeline rimossa; QUICK-REFERENCE.md refresh v4.0; quiz-tracker stats ricalcolate; XP allineato a Progress.md (7152, scartato +35 non tracciato); files.md aggiunge fast-track; reading-list.md MESE/Week→Modulo)*

*Versione precedente: 2026-04-24 (Fast Track v1.0 creata + /refactor post-creazione + sync bidirezionale documentata + XP 6702→7152 +450)*

*Versione precedente: 2026-04-23 (refactor sessione job-postings-driven enrichment + pulizia: cascade decisions + Cluster Positioning + Job Market Tracking + cluster-aware Prossima Sessione)*

*Versione precedente: 2026-04-17 (refactor self-paced: rimossa timeline, esami completion-based, Week→Modulo)*
