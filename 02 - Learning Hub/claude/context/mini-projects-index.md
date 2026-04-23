---
tags: [context, mini-projects, portfolio, gamification, canonical-source]
created: 2026-04-23
updated: 2026-04-23
status: canonical
---

# Mini-Projects Portfolio — Central Index

> **Single source of truth** per i 30 mini-projects (10 AI + 10 SE + 10 FE) della roadmap.
> Roadmap referenziano questo file. **Sinergia cross-roadmap** documentata: 1 mini-project ben fatto può servire 2-3 cluster.

---

## Filosofia

- **Small but shipped > big but unfinished**: ogni mini-project deployato + funzionante
- **Built with AI tools** obbligatorio (Claude Code primario, Cursor/Copilot/Windsurf secondari) — documenta workflow nel README
- **README professionali**: problem, demo GIF/link, stack, AI tools usati, learnings
- **Time-box stretto**: ≤2 settimane → tagli scope, non procrastini
- **Public GitHub** + demo live (Vercel/Railway/Fly.io free tier o cloud managed)
- **Business angle** chiaro nel README

> **Nota stack:** progetti che richiederebbero "imparare Java/Spring Boot upfront" sono **esclusi** (Java si impara on-the-job se cluster #4 SE Fintech Java è target).

---

## 🤖 AI Mini-Projects (10 idee — `roadmaps/ai-skills.md`)

| # | Idea | Cluster target | Stack | Effort |
|---|------|----------------|-------|--------|
| 1 | **Lead scoring agent** — valuta qualità lead da CSV/CRM | AI #4 | Python + LangGraph + LLM | 1 settimana |
| 2 | **Document Q&A chatbot** — RAG su PDF caricati | AI #2 | Python + FastAPI + pgvector | 1-2 settimane |
| 3 | **Email triage agent** — classifica + suggerisce risposta | AI #4 | Python + LangChain + IMAP API | 1 settimana |
| 4 | **Code review bot** — analizza diff GitHub e commenta | AI #4 | Python + GitHub API + Claude | 1-2 settimane |
| 5 | **Multi-agent research assistant** — planner + searcher + writer | AI #2 | LangGraph + web search API | 2 settimane |
| 6 | **MCP server pubblico** — es. notes/tasks Obsidian server | AI #2 | TypeScript + MCP SDK | 1 settimana |
| 7 | **Ad copy A/B optimizer** — genera + valuta varianti | AI #4 | Python + LLM + eval framework | 1-2 settimane |
| 8 | **Receipt categorizer** — OCR + classifica spese | AI #4 | Python + Tesseract/Vision API + LLM | 1 settimana |
| 9 | **Meeting summarizer agent** — transcript → action items | AI #4 | Python + Whisper + Claude | 1-2 settimane |
| 10 | **AI changelog generator** — git log → release notes user-friendly | AI #4 | Python + GitHub API + LLM | 3-5 giorni |

---

## 💻 SE Mini-Projects (10 idee — `roadmaps/senior-engineer.md`)

| # | Idea | Cluster target | Stack | Effort |
|---|------|----------------|-------|--------|
| 1 | **Distributed rate limiter** (token bucket + Redis) — npm/NuGet package | SE #5, SE #2 | .NET o Node + Redis | 1 settimana |
| 2 | **Event store mini** (write-only log + projections) | SE #2 | .NET + Postgres | 2 settimane |
| 3 | **MCP server pubblico** (es. notes / git tools / database query) | SE #1, AI #2 | TypeScript + MCP SDK | 1 settimana |
| 4 | **RAG agent backend** (FastAPI + LangGraph + pgvector) | SE #1, AI #2 | Python + FastAPI + LangGraph | 2 settimane |
| 5 | **Distributed lock service** (Redlock implementation) | SE #5 | .NET o Go + Redis | 1 settimana |
| 6 | **Outbox library standalone** (riusabile in qualsiasi progetto) | SE #2, SE #4 | .NET + EF Core + RabbitMQ | 1-2 settimane |
| 7 | **Webhook gateway** (verifying + retry + DLQ) | SE #5, SE #6 | Node + AWS Lambda + SQS | 1 settimana |
| ~~8~~ | ~~Java/Spring Boot port~~ | — | — | **RIMOSSO** (Java on-the-job) |
| 8 | **DAPR sidecar demo** (state + pub/sub + bindings) | SE #2 | .NET + DAPR + K8s locale | 1-2 settimane |
| 9 | **Observability sample** (Prometheus + Grafana + Jaeger demo) | SE #2, SE #3 | qualsiasi BE + OpenTelemetry | 1 settimana |
| 10 | **OAuth2/OIDC playground** (Auth0 integration + SCIM endpoint) | SE #5 | .NET o Node + Auth0 SDK | 1 settimana |

> **Modifica 2026-04-23:** rimosso "Java/Spring Boot port" da SE Mini #8. Java si impara on-the-job se cluster #4 Fintech Java è target. Sostituito con DAPR sidecar demo (.NET-friendly, distintivo per cluster #2 Fintech Low-Latency).

---

## 🎨 FE Mini-Projects (10 idee — `roadmaps/senior-frontend.md`)

| # | Idea | Cluster target | Stack | Effort |
|---|------|----------------|-------|--------|
| 1 | **D3 chart library** standalone (es. interactive heatmap) | FE #3, FE #6 | TS + D3 + Storybook | 1 settimana |
| 2 | **Tailwind landing page generator** AI-built | FE #4, FE #5 | Next.js + v0.dev + Vercel | 3-5 giorni |
| 3 | **Storybook design system** seed (10-15 componenti accessibili) | FE #2, FE #4 | Storybook + Radix + CVA | 1-2 settimane |
| 4 | **Streaming chatbot UI** (Vercel AI SDK demo) | FE #5 | Next.js + AI SDK + shadcn | 1 settimana |
| 5 | **Real-time dashboard mini** (con SSE + sparkline) | FE #3, FE #6 | React + Recharts + SSE | 1 settimana |
| 6 | **Component library** pubblicata su npm (accessibile primitives) | FE #4 | Vite + Radix + Changesets + npm | 2 settimane |
| 7 | **Playwright test suite** showcase (e2e + visual regression) | FE #2, FE #3 | Playwright + GitHub Actions | 3-5 giorni |
| 8 | **Tool-use UI** demo (mostra agente che chiama tool con feedback live) | FE #5 | Next.js + AI SDK + Zod | 1 settimana |
| 9 | **AI prompt input** rich (slash commands + mention + file attach) | FE #5 | React + custom rich input | 1 settimana |
| 10 | **Stripe subscription** flow demo (pricing → checkout → portal) | FE #2, FE #4 | Next.js + Stripe + webhooks | 1-2 settimane |

---

## 🔗 Cross-Roadmap Synergy Table ⭐

> **1 mini-project = 2-3 portfolio.** Ottimizza il tempo riusando il lavoro tra cluster.

| Mini-Project | AI Slot | SE Slot | FE Slot | Cluster serviti | Effort totale |
|--------------|---------|---------|---------|-----------------|---------------|
| **MCP Server Pubblico** (notes/git/DB query) | AI #6 | SE #3 | — | AI #2 + SE #1 | 1 settimana → 2 portfolio |
| **RAG Agent Backend** (FastAPI + LangGraph) | AI #2 (Document Q&A) | SE #4 | — | AI #2 + SE #1 + AI Bridge | 2 settimane → 2 portfolio |
| **Streaming Chatbot UI** | — | — | FE #4 | FE #5 (deploy come UI di MCP/RAG sopra) | 1 settimana → completa stack AI #2/SE #1 |
| **Tool-use UI** | — | — | FE #8 | FE #5 (visualizza tool calling di AI #5 multi-agent) | 1 settimana → 2 portfolio |
| **AI Prompt Input** (rich slash/mention/attach) | — | — | FE #9 | FE #5 (riusabile in tutti progetti AI con chat UI) | 1 settimana → componente trasversale |
| **Lead Scoring Agent** | AI #1 | — | (opt. dashboard) | AI #4 + opt. SE #1 (porta in prod) | 1 settimana → 1-2 portfolio |
| **Webhook Gateway** | — | SE #7 | (opt. monitoring dashboard) | SE #5 + SE #6 + opt. FE #5 dashboard | 1-2 settimane → triple-use |
| **Observability Sample** | — | SE #9 | — | SE #2 + SE #3 (foundational per tutto il portfolio) | 1 settimana → use as backbone |

### Strategia ottimale combinata

**Portfolio compatto (5 mini-projects → copre 4 cluster):**
1. **MCP Server Pubblico** → AI #2 + SE #1
2. **RAG Agent Backend** + **Streaming Chatbot UI** → AI #2 + SE #1 + FE #5 (full-stack AI demo!)
3. **Tool-use UI** → FE #5
4. **Lead Scoring Agent** → AI #4 (cluster #4 bridge)
5. **D3 Chart Library** → FE #3 + FE #6

**Risultato:** ~5-6 settimane di lavoro = portfolio competitivo per cluster #4 (immediato), #5 (sweet spot), #1 (sweet spot), #3/#6 (bridge), AI #2 (long-game preview).

---

## 📊 Achievement Mini-Projects (cross-roadmap)

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 📦 **Mini Builder** | 5 mini-projects pubblicati GitHub (qualsiasi categoria) | +500 |
| 🚀 **Portfolio Pro** | 10 mini-projects + repo pinned curato | +750 |
| 🌍 **Cluster Ready** | Tutti i mini-projects per 1 cluster completati (vedi cluster-taxonomy) | +1000 |
| 🔥 **Triple Threat** | 1 mini-project che serve 3+ cluster con 3+ portfolio | +500 |

### XP per mini-project

- Mini-project completato + GitHub README pro: +150
- Demo live deployata: +50-75 (Vercel locale, +75 cloud managed AWS/GCP)
- README con AI tools workflow doc: +30
- Mini-project pubblicato come **library/package** (npm/NuGet): +200
- Engagement (stars/issues/fork): +100

---

## 🔄 Update process

**Quando aggiornare:**
- Quando Dan completa un mini-project → aggiorna status (✅ Done, 🚧 In progress, ⏳ Todo)
- Quando emerge nuova idea (da job-postings o da pratica)
- Quando un mini-project rivela sinergia non documentata

**Workflow update:**
1. Aggiungi/modifica entry nella tabella della categoria
2. Se nuova sinergia → aggiorna Cross-Roadmap Synergy Table
3. Cascade su roadmap (link, non duplicare)
4. Update gamification.md se sblocca achievement

---

## 📚 File correlati

- `context/cluster-taxonomy.md` — definizioni cluster di ruolo
- `roadmaps/ai-skills.md` — sezione "AI Mini-Projects Portfolio" linka qui
- `roadmaps/senior-engineer.md` — sezione "SE Mini-Projects Portfolio" linka qui
- `roadmaps/senior-frontend.md` — sezione "FE Mini-Projects Portfolio" linka qui
- `context/gamification.md` — achievement Mini-Projects

---

*Created: 2026-04-23 (refactor sessione job-postings-driven enrichment) — versione 1.0*
