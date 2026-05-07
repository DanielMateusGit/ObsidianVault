---
tags: [roadmap, fast-track, cv-optimization]
created: 2026-04-24
updated: 2026-04-24
version: 1.0
---

# Fast Track Roadmap

> **Percorso conduttore cross-roadmap.**
> Estrae da AI / Senior Engineer / Senior Frontend / Architect Quest / Career Boost solo i topic con **massimo CV-ROI per minimo effort**.
> Pensata per sessioni brevi: "ho poco tempo, cosa faccio che mi dà più valore subito?"

---

## 🎯 Obiettivo

Rendere Dan candidabile nel minor tempo possibile su:

1. **Cluster AI #4 — AI-Augmented SWE** (bridge 3-6 mesi ⭐ accessibile)
2. **Cluster AI #2/#3 — AI Engineer GenAI / Full-Stack AI-First** (long-game ma slice veloci per interview-ready)
3. **Cluster SE #5 — Modern Full-Stack** (bridge 3-6 mesi ⭐ accessibile)
4. **Polish production + interview-ready** (trasversale a tutti i cluster)

**Cosa NON è:** un sostituto delle roadmap sorgenti. I moduli pieni (P1, P2.5, Python AI Bridge completo, ecc.) restano lì. Questa è la **versione "lean"** per sessioni corte.

---

## 🔁 Regole di sincronizzazione

| Stato in Fast Track | Effetto sulla roadmap sorgente |
|---------------------|-------------------------------|
| ✅ Completato 100% | Modulo/sezione sorgente → **completato** (checkbox aggiornato lì) |
| 🟡 Parziale | Modulo/sezione sorgente → **già affrontato** (non da rifare da zero; da completare solo se/quando Dan ci torna) |
| ⬜ Non iniziato | Nessun effetto |

**Sincronizzazione bidirezionale pratica:**
- Se un modulo viene completato per via normale nella roadmap sorgente (es. Dan fa l'intero P2.5 M5), lo slice Fast Track corrispondente si considera **automaticamente completato**.
- Se uno slice Fast Track viene completato, Dan (o Claude in `/end` / `/context`) aggiorna lo status in ENTRAMBI i file.

**Convenzione status `source`:**
- Campo `source` punta a `roadmap-file#anchor` con riferimento esatto al modulo sorgente.
- Quando si marca ✅/🟡 qui, aggiornare anche la sorgente con nota: "Affrontato via Fast Track [ID]".

---

## 📐 Convenzioni

**Effort bands:**
- ⚡ **XS** — 1 sessione (<2h)
- ⚡ **S** — 2-3 sessioni (3-6h)
- 🔨 **M** — 1 settimana part-time (6-12h)
- (L/XL esclusi: questa è fast-track; topic L sono rappresentati come singoli slice S/M)

**CV-ROI (1-10):**
- 10 = appare in 70%+ annunci target E sblocca candidature
- 8-9 = citato 50%+ annunci, altamente differenziante
- 7 = standard moderno 2026, atteso ma non scarso

**Tipo output:** tutti gli item producono un **artefatto tangibile pubblicabile** (repo GitHub, ADR, nota tecnica, demo live, merged PR). Niente solo "ho letto".

---

## 🚀 FASE 1 — Entry AI-Augmented SWE (Cluster #4 Bridge)

> **Goal fase:** rendere Dan candidabile su AI #4 (3-6 mesi bridge) entro 30-45 giorni di sessioni fast-track.
> **Deliverable cumulativo:** 4 repo GitHub pinnati + prompt library + Claude Code mastery visible.

| ID | Topic | Effort | ROI | Source | Output | Cluster | Status | Sync |
|----|-------|--------|-----|--------|--------|---------|--------|------|
| **FT-A01** | MCP Server hello-world pubblico | ⚡ S | 10 | `ai-skills.md` P2.5 M5 | Repo GitHub con 1 MCP server funzionante (calcolatrice/notes) + README + docs install | AI #4, AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M5 |
| **FT-A02** | Python AI Bridge — FastAPI + LiteLLM skeleton | ⚡ S | 10 | `ai-skills.md` Python AI Bridge M1 | Repo GitHub FastAPI server con endpoint /chat via LiteLLM (multi-provider) | AI #4, AI #2, SE #1 | ⬜ | `ai-skills.md` Python AI Bridge M1 |
| **FT-A03** | Python AI Bridge — LangChain chain base | ⚡ S | 10 | `ai-skills.md` Python AI Bridge M2 | 1 chain funzionante (prompt→LLM→parser) + test + README | AI #4, AI #2 | ⬜ | `ai-skills.md` Python AI Bridge M2 |
| **FT-A04** | Prompt engineering strutturato — library | ⚡ XS | 8 | `ai-skills.md` P2.5 M4 | Repo GitHub `prompt-templates` con 5-10 template versionati + ADR su strategy | AI #4, AI #3, AI #2 | ⬜ | `ai-skills.md` P2.5 M4 |
| **FT-A05** | AI Mini-Project #1 — AI Changelog Generator | ⚡ S | 9 | `context/mini-projects-index.md` | Repo GitHub + demo live su GitHub Actions che commenta PR | AI #4 | ⬜ | `mini-projects-index.md` AI#1 |
| **FT-A06** | AI Mini-Project #2 — Lead Scoring Agent | 🔨 M | 9 | `context/mini-projects-index.md` | Repo GitHub + demo (CSV in → scored leads out) + README business angle | AI #4 | ⬜ | `mini-projects-index.md` AI#2 |
| **FT-A07** | AI Mini-Project #3 — Email Triage | 🔨 M | 9 | `context/mini-projects-index.md` | Repo GitHub + demo + eval metrics (precision/recall) | AI #4, AI #3 | ⬜ | `mini-projects-index.md` AI#3 |
| **FT-A08** | Prompt Injection Defense + Guardrails layer | ⚡ XS | 7 | `ai-skills.md` P2.5 M6 | Nota tecnica + 1 codice esempio con input sanitization + adversarial tests | AI #2, AI #4, SE #1 | ⬜ | `ai-skills.md` P2.5 M6 |

**Sinergie Fase 1:**
- FT-A02 + FT-A03 sbloccano stack riusabile per FT-A05/A06/A07 (stesso scheletro FastAPI)
- FT-A01 MCP server dual-portfolio (vale anche per cluster SE #1)
- FT-A04 prompt library riusata in tutti i mini-project

---

## 🧠 FASE 2 — AI Engineering Core (Cluster #2/#3 Slice)

> **Goal fase:** rendere Dan **interview-ready** su cluster AI #2 (GenAI/LLMOps) senza costruire un prodotto intero. Fondamenta RAG + Eval + agentic patterns.
> **Deliverable cumulativo:** RAG endpoint + eval dashboard + LangGraph agent + 3 ADR pubblicati.

| ID | Topic | Effort | ROI | Source | Output | Cluster | Status | Sync |
|----|-------|--------|-----|--------|--------|---------|--------|------|
| **FT-B01** | Vector DB decision framework + benchmark | ⚡ XS | 8 | `ai-skills.md` P2.5 M3 | ADR comparativa pgvector vs Qdrant vs Pinecone con benchmark hands-on su 10k vettori | AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M3 |
| **FT-B02** | RAG slice — chunking + pgvector retrieval | 🔨 M | 9 | `ai-skills.md` P2.5 M3 | Endpoint `/rag/query` funzionante + index pipeline + 10 query di test | AI #2, SE #1, FE #6 | ⬜ | `ai-skills.md` P2.5 M3 |
| **FT-B03** | Semantic search + hybrid retrieval (keyword + vector) | ⚡ S | 7 | `ai-skills.md` P2.5 M3 | Retrieval benchmark con reranking + nota tecnica | AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M3 |
| **FT-B04** | AI Eval Pipeline — Ragas basics | ⚡ S | 9 | `ai-skills.md` P2.5 M9 | Mini eval dashboard (Ragas/DeepEval) con 10 test case su RAG di FT-B02 | AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M9 |
| **FT-B05** | LangGraph — 1 agent state machine | 🔨 M | 9 | `ai-skills.md` P2.5 M5.5 | 1 agente funzionante con state graph + tool use + README + ADR | AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M5.5 |
| **FT-B06** | Multi-agent orchestration — demo ReAct | 🔨 M | 8 | `ai-skills.md` P2.5 M8 | 2 agent che cooperano (Plan + Execute) + trace pubblicato | AI #2, SE #1 | ⬜ | `ai-skills.md` P2.5 M8 |
| **FT-B07** | Semantic caching + prompt dedup | ⚡ S | 8 | `ai-skills.md` P2.5 M9 | Implementazione Redis-backed + benchmark costo (before/after) + nota tecnica | AI #4, AI #2 | ⬜ | `ai-skills.md` P2.5 M9 |
| **FT-B08** | Responsible AI — bias test suite slice | ⚡ XS | 7 | `ai-skills.md` P2.5 M9 | 1 test suite bias detection + audit report + ADR compliance EU | AI #2, AI #3 | ⬜ | `ai-skills.md` P2.5 M9 |

**Sinergie Fase 2:**
- FT-B02 + FT-B04 **non separabili** (RAG senza eval = "funziona ma non lo so"). Farli insieme.
- FT-B01 prerequisito implicito per FT-B02 (scegli pgvector con data-driven reasoning)
- FT-B05 riusa agentic pattern di FT-A06 (Lead Scoring già agente, LangGraph lo formalizza)
- FT-B07 tocca anche cluster SE #2 (cost optimization mindset)

---

## 🏭 FASE 3 — Production Polish & Interview Ready (Cross-Cluster)

> **Goal fase:** trasformare progetti esistenti (AQ P1, SE P1) in **enterprise-ready** + skill FE modern + interview prep. Ogni item è uno slice su 1 progetto esistente.
> **Deliverable cumulativo:** 1 progetto "production-grade completo" visibile + TypeScript craft visible + 2-3 System Design rehearsed.

| ID | Topic | Effort | ROI | Source | Output | Cluster | Status | Sync |
|----|-------|--------|-----|--------|--------|---------|--------|------|
| **FT-C01** | Observability slice — OTel + Prometheus + Grafana | 🔨 M | 8 | `senior-engineer.md` M-T2 | 1 progetto SE con tracing E2E + metrics + dashboard Grafana funzionante | SE #2, SE #3, SE #5, AI #2 | ⬜ | `senior-engineer.md` M-T2 |
| **FT-C02** | Docker multi-container — docker-compose completo | ⚡ S | 7 | `senior-engineer.md` P4 | 1 progetto con `docker-compose.yml` + health checks + networking + volumes | SE #5, SE #2, AI #4 | ⬜ | `senior-engineer.md` P4 |
| **FT-C03** | Cloud deployment slice — 1 progetto su AWS/GCP | ⚡ S | 8 | `senior-engineer.md` M-T3 | 1 progetto deployato (managed service) con URL pubblico + costo monitorato | SE #5, SE #2, AI #4 | ⬜ | `senior-engineer.md` M-T3 |
| **FT-C04** | Terraform slice — VPC + compute + DB IaC | ⚡ S | 8 | `senior-engineer.md` M-T4 | Repo Terraform con modulo VPC + DB + secrets + applicato a FT-C03 | SE #5, SE #2 | ⬜ | `senior-engineer.md` M-T4 |
| **FT-C05** | CI/CD slice — GitHub Actions lint→test→build→deploy | ⚡ S | 7 | `senior-engineer.md` M-T5 | Workflow YAML su 1+ progetto + badge README + deploy auto su push main | SE #5, SE #2, FE #3 | ⬜ | `senior-engineer.md` M-T5 |
| **FT-C06** | Healthcheck patterns — readiness + liveness | ⚡ S | 7 | `senior-engineer.md` P4 | Endpoint `/health` + `/ready` + Prometheus metrics su 1 progetto | SE #2, SE #3, SE #5 | ⬜ | `senior-engineer.md` P4 |
| **FT-C07** | TypeScript Craft slice — branded types + Zod refactor | ⚡ S | 8 | `senior-frontend.md` TS Craft Module | 1 refactor su progetto FE (Focus Tube o nuovo) con branded types, generics, Zod | FE #4, FE #5, SE #1 | ⬜ | `senior-frontend.md` TS Craft |
| **FT-C08** | Streaming UI — Next.js 15 + Vercel AI SDK | 🔨 M | 9 | `senior-frontend.md` P6 | Demo live Next.js + AI SDK streaming + tool-use rendering + deploy Vercel | FE #5, AI #3, SE #1 | ⬜ | `senior-frontend.md` P6 |
| **FT-C09** | Modern Testing slice — Vitest + Playwright + MSW | ⚡ S | 8 | `senior-frontend.md` Modern Testing Module | Test suite (unit + integration + E2E) su 1 progetto con pyramid 70/20/10 visible | FE #3, FE #2, SE #5 | ⬜ | `senior-frontend.md` Testing |
| **FT-C10** | Frontend Security slice — OWASP + CSP | ⚡ S | 7 | `senior-frontend.md` FE Security Module | OWASP ZAP audit su 1 progetto + fix XSS/CSRF/CSP + `SECURITY.md` | FE #2, FE #4, FE #5, SE #5 | ⬜ | `senior-frontend.md` FE Security |
| **FT-C11** | System Design — Rate Limiter + Chat + Notification | ⚡ S | 8 | `career-boost.md` System Design Practice | 3 design doc strutturati + 1 mock interview registrato | SE #5, SE #2, AI #4 | ⬜ | `career-boost.md` System Design |
| **FT-C12** | System Design cluster-specific — AI #2 + SE #1 | ⚡ S | 8 | `career-boost.md` System Design Practice | 2 design doc (Multi-agent RAG, RAG at scale) + trade-off ADR | AI #2, SE #1 | ⬜ | `career-boost.md` System Design |
| **FT-C13** | Open source contribution — 1-2 PR merged | ⚡ S | 7 | `career-boost.md` OSS | 1-2 PR merged su progetto rilevante + link su CV/LinkedIn | AI #4, SE #5, FE #4, AI #1 | ⬜ | `career-boost.md` OSS |

**Sinergie Fase 3:**
- FT-C02 + FT-C03 + FT-C04 + FT-C05 **catena naturale** sullo stesso progetto SE: Docker → Deploy → Terraform → CI/CD. Farli in sequenza sullo stesso target = 1 progetto "enterprise-ready completo" visibile.
- FT-C01 observability applicabile a FT-B02/B04 (RAG traced + osservato) → dual-value AI+SE
- FT-C07 + FT-C08 + FT-C09 catena FE modern: refactor TS → streaming UI → test
- FT-C11 + FT-C12 System Design insieme = 5 design pronti per colloqui

---

## 📊 Dashboard Progress

| Fase | Item totali | Completati | Parziali | Non iniziati |
|------|-------------|------------|----------|--------------|
| Fase 1 — Entry AI #4 | 8 | 0 | 0 | 8 |
| Fase 2 — AI Core | 8 | 0 | 0 | 8 |
| Fase 3 — Polish Cross | 13 | 0 | 0 | 13 |
| **Totale** | **29** | **0** | **0** | **29** |

---

## 🧭 Sequenza consigliata "primi 30-45 giorni"

**Week-batch 1-2 (~10-15h):** FT-A02 → FT-A03 → FT-A01 → FT-A04
→ Risultato: 2 repo GitHub (Python Bridge + MCP) + prompt library

**Week-batch 3 (~6h):** FT-A05 (AI Changelog Generator)
→ Risultato: 1 mini-project GitHub pinnato

**Week-batch 4-5 (~10h):** FT-A06 (Lead Scoring Agent)
→ Risultato: 2° mini-project GitHub, cluster #4 **candidabile**

**Week-batch 6 (~4h):** FT-B01 + FT-B04 setup
→ Risultato: ADR vector DB + eval scaffolding

**Week-batch 7-8 (~10h):** FT-B02 + FT-B04 (RAG + Ragas insieme)
→ Risultato: RAG endpoint + eval dashboard — fondamenta cluster #2

**Interleave sempre:** FT-C11/C12 (System Design) da fare come "warmup" di 1h quando poca energia.

---

## ⚖️ Regole d'uso

1. **Sessioni corte (30-90min):** pesca da XS items. Priorità a items non iniziati di Fase 1.
2. **Sessioni medie (2-4h):** pesca da S items. Priorità Fase 1 finché non completata, poi Fase 2.
3. **Sessioni lunghe (mezza giornata+):** pesca da M items.
4. **Mai saltare Fase 1 per andare a Fase 2** se Dan non è candidabile cluster #4 (portfolio < 3 repo pubblici).
5. **Quando completi uno slice qui:** `/end` aggiorna checkbox qui **E** in roadmap sorgente.
6. **Quando fai un intero modulo sorgente:** segnalo qui ✅ nello slice corrispondente (evita doppio lavoro).

---

*Ultimo aggiornamento: 2026-04-24 (v1.0 — creazione fast-track roadmap cross-roadmap)*
