---
tags: [context, cluster-taxonomy, job-market, canonical-source]
created: 2026-04-23
updated: 2026-04-23
status: canonical
---

# Cluster Taxonomy — Canonical Source

> **Single source of truth** per la tassonomia dei ruoli identificata dall'analisi job-postings (28 annunci IT + UK).
> Tutte le roadmap referenziano questo file. **Non duplicare** le definizioni cluster nelle roadmap — link qui.

---

## Filosofia generale

Il mercato dei ruoli software (specialmente in UK 2026) **non è monolitico**. Per ogni famiglia di ruolo (AI / SE / FE) esistono **cluster distinti** con stack, accessibilità e salary diversi. Targetizzare un cluster specifico (invece di "Senior Engineer generic") rende la candidatura **molto più efficace**.

**Principio Dan:** lo stack secondario (Java/Spring Boot, Python deep) si impara **on the job**, non upfront. Concentrarsi sui concetti universali (DDD, EDA, CQRS, Clean Arch, AI patterns) — la sintassi specifica si assimila in 2-4 settimane sul lavoro reale.

---

## 🤖 AI Skills — 4 Cluster

Riferimento: `roadmaps/ai-skills.md`. Source data: `context/job-postings-analysis.md` (8 annunci).

### Cluster #1 — AI Tech Lead Enterprise
- **Esempio annuncio:** Open Reply (Milano)
- **Stack:** Broad + leadership + on-prem + ML classico (TF/PyTorch)
- **Stack secondario (on-the-job):** Java per integrazione enterprise
- **Accessibilità Dan:** 18-30+ mesi (long-game)
- **Salary range:** IT €70-100k+
- **Mindset:** Architettura + team leadership + multi-domain

### Cluster #2 — AI Engineer GenAI / LLMOps
- **Esempi annunci:** Reply, hlpy, AI Eng London recruiter, Fintech Series A London
- **Stack:** Python + LangChain/LangGraph + RAG + eval (Ragas/DeepEval) + agents + MCP + vector DB
- **Accessibilità Dan:** 12-18 mesi
- **Salary range:** IT €80-120k / UK £100-200k
- **Mindset:** IC specializzato GenAI production-grade

### Cluster #3 — Full-Stack AI-First
- **Esempio annuncio:** Euphoric (London)
- **Stack:** React/TS + Python/FastAPI + AI methods (LLM, RecSys, RL) + cloud
- **Accessibilità Dan:** 6-12 mesi
- **Salary range:** UK £90-110k
- **Mindset:** T-shaped FE/BE/ML, ship AI features end-to-end

### Cluster #4 — AI-Augmented SWE / Growth ⭐ BRIDGE
- **Esempi annunci:** Jet HR (IT), Homey (UK)
- **Stack:** Backend (qualsiasi) + Claude Code/Cursor mastery + business sense
- **Accessibilità Dan:** **3-6 mesi** ⭐ (hai già SE solido + Claude Code cert + mindset strutturato)
- **Salary range:** IT €40-65k / UK £70-100k
- **Mindset:** AI come leva di business (sales, marketing, GTM, growth)

### Path strategico AI

```
[OGGI] SE solido + Claude Code cert + studio AI strutturato
    ↓
[3-6 MESI] Cluster #4 candidabile
    Required: Python AI Bridge + 3-5 mini-projects GitHub AI-built
    ↓
[6-12 MESI] Cluster #3 candidabile
    Required: P2.5 completato + Flutter mobile + AI methods diversificati
    ↓
[12-18 MESI] Cluster #2 candidabile
    Required: LangGraph deep + eval pipeline + multi-agent + MCP server pubblico
    ↓
[18-30 MESI] Cluster #1 candidabile (opzionale)
    Required: anni accumulati + leadership track + ML classico (long-game)
```

---

## 💻 Senior Engineer — 6 Cluster

Riferimento: `roadmaps/senior-engineer.md`. Source data: `context/job-postings-senior.md` (12 annunci).

### Cluster #1 — AI-Native Backend ⭐ SWEET SPOT
- **Esempi annunci:** Nothing (London), Paloma (London £85k)
- **Stack:** Node/Python/.NET + LangGraph + MCP + RAG + Claude Code
- **Accessibilità Dan:** 6-12 mesi
- **Salary range:** £85k+ UK
- **Sinergia:** intersezione perfetta con AI Cluster #2/#3 → **target principale per Dan**

### Cluster #2 — Fintech Low-Latency
- **Esempio annuncio:** TP ICAP (London)
- **Stack:** .NET/C# + low-latency + observability + TDD + DAPR
- **Stack secondario:** Java alternative (on-the-job)
- **Accessibilità Dan:** 9-12 mesi
- **Salary range:** £80-130k UK
- **Coincidenza con Architect Quest stack** ✅

### Cluster #3 — Infrastructure / SRE-leaning
- **Esempio annuncio:** Spotify (London/Stockholm)
- **Stack:** Java + cloud + distributed + on-call + CDN
- **Stack secondario:** open a learning others (on-the-job)
- **Accessibilità Dan:** 12+ mesi (richiede on-call experience track record)
- **Salary range:** £80-120k UK

### Cluster #4 — Fintech Java Backend
- **Esempi annunci:** NatWest Boxed, Deutsche Bank
- **Stack:** Java + Spring Boot + Kafka + K8s + AWS / Big Data
- **Filosofia Dan:** **Java/Spring Boot somiglia a .NET, si impara on the job**. Focus su **concetti universali** (Kafka, K8s, AWS, microservices) che trasferisci facilmente.
- **Accessibilità Dan:** 6-9 mesi (per concept transfer .NET → Java solo on-the-job ramp-up)
- **Salary range:** £70-110k UK
- **Approccio:** non investire upfront in Java mastery, candidati su strength concettuale + dimostra capacità di pickup linguaggio

### Cluster #5 — Modern Full-Stack ⭐ BRIDGE
- **Esempi annunci:** Trainline, Freetrade, Elliptic, recruiter £50-60k
- **Stack:** Node/TS + React + AWS/GCP + microservices + Postgres
- **Accessibilità Dan:** **3-6 mesi** ⭐ (stack moderno, vicino a AQ tech)
- **Salary range:** £52-90k UK
- **Note:** "lingua franca" mid-senior UK 2026 (7/12 annunci usano Node/TS)

### Cluster #6 — Consulting Polyglot
- **Esempio annuncio:** Accenture (London)
- **Stack:** React + Node + Python + Java + cloud + **AI cert OBBLIGATORIA**
- **Filosofia Dan:** non imparare 4 linguaggi upfront. Focus su AI cert + 1 stack moderno solido (.NET o Node/TS).
- **Accessibilità Dan:** 9-12 mesi
- **Salary range:** £60-100k UK

### Path strategico SE

```
[OGGI] .NET solido + Architect Quest in corso + Senior P1 in corso
    ↓
[3-6 MESI] Cluster #5 Modern Full-Stack accessibile
    Required: completamento P1-P2 + esposizione cloud (AWS/GCP) + 2-3 mini-projects GitHub
    ↓
[6-9 MESI] Cluster #4 Fintech Java OR Cluster #1 AI-Native Backend
    Path Java: solo conceptual, Java vero on-the-job
    Path AI-Native: LangGraph + MCP + RAG hands-on
    ↓
[9-12 MESI] Cluster #2 Fintech Low-Latency OR Cluster #6 Consulting Polyglot
    Path Low-Latency: + observability + DAPR
    Path Consulting: + AI cert + multi-stack awareness
    ↓
[12+ MESI] Cluster #3 Infrastructure / SRE
    Required: on-call experience + reliability mindset
```

---

## 🎨 Senior Frontend — 6 Cluster

Riferimento: `roadmaps/senior-frontend.md`. Source data: `context/job-postings-frontend.md` (6 annunci).

### Cluster #1 — Enterprise FE
- **Esempio annuncio:** State Street
- **Stack:** Stack agnostic + design system + a11y + Node BFF
- **Accessibilità Dan:** Subito (con minimal portfolio)
- **Salary range:** ~£55-75k UK

### Cluster #2 — Modern Fintech FE
- **Esempio annuncio:** Moneybox
- **Stack:** Next.js + Tailwind + Zustand + TanStack + Storybook + headless CMS
- **Accessibilità Dan:** 6-9 mesi
- **Salary range:** ~£70-90k UK

### Cluster #3 — Scale-up React FE ⭐ BRIDGE
- **Esempio annuncio:** Xelix
- **Stack:** React + Redux Toolkit + RTK Query + WebSocket + Data viz
- **Accessibilità Dan:** **3-6 mesi** ⭐ (Redux Toolkit già noto)
- **Salary range:** £60-75k UK

### Cluster #4 — Product Engineer / Founding FE ⭐ PREMIUM
- **Esempi annunci:** Edra, Jumpstart
- **Stack:** TS + React + Next.js high-craft + library/SDK building + greenfield
- **Accessibilità Dan:** 9-12 mesi
- **Salary range:** £90-130k+ UK

### Cluster #5 — AI-Native FE ⭐ SWEET SPOT
- **Esempio annuncio:** Euphoric
- **Stack:** React/TS + Vercel AI SDK + streaming UI + AI methods + Cursor/Claude Code
- **Accessibilità Dan:** 9-12 mesi
- **Salary range:** £90-110k UK
- **Sinergia:** intersezione perfetta AI + FE (compatibile con target Dan)

### Cluster #6 — Data-Heavy AI FE
- **Esempio annuncio:** Hook
- **Stack:** TS + React + Data viz CORE (D3/Visx) + dashboard + AI awareness
- **Accessibilità Dan:** 6-9 mesi
- **Salary range:** up to £105k UK

---

## 🔗 Cross-Cluster Intersections

Alcuni cluster si **intersecano** tra famiglie di ruoli — opportunità di doppia targetizzazione.

| Intersezione | Combina | Beneficio |
|--------------|---------|-----------|
| **AI #4 + SE #5 + FE #3** | AI-Augmented SWE + Modern Full-Stack + Scale-up React | **Triple bridge** accessibili in 3-6 mesi — base ampia di candidatura |
| **AI #2 + SE #1** | AI Engineer GenAI + AI-Native Backend | Stack quasi identico (Python/Node + LangGraph + MCP + RAG). 1 portfolio, 2 cluster targetizzabili |
| **AI #3 + FE #5** | Full-Stack AI-First + AI-Native FE | Profilo full-stack AI-first (Euphoric-style). React + Python/FastAPI + AI methods |
| **SE #5 + FE #4** | Modern Full-Stack + Founding FE | "Founding engineer" che fa BE+FE. Edra/Jumpstart pattern |
| **AI #1 + SE #2** | AI Tech Lead Enterprise + Fintech Low-Latency | Long-game architect AI + low-latency. Fascia premium ma 18+ mesi |

---

## 📊 Insight strategici per Dan

### Bridge accessibili in 3-6 mesi (priorità immediata)

1. **AI Cluster #4 — AI-Augmented SWE** (€40-65k IT / £70-100k UK) — leva su Claude Code cert + SE solido
2. **SE Cluster #5 — Modern Full-Stack** (£52-90k UK) — Node/TS è "lingua franca", richiede esposizione cloud
3. **FE Cluster #3 — Scale-up React FE** (£60-75k UK) — Redux Toolkit già noto, manca data viz

**Strategia ottimale:** 1 mini-project ben fatto può toccare **2-3 cluster contemporaneamente**.

### Sweet spot a 6-12 mesi

- **SE Cluster #1 AI-Native Backend** (£85k+ UK) ⭐ — target principale Dan come AI Engineer
- **FE Cluster #5 AI-Native FE** (£90-110k UK) — intersezione AI+FE

### Long-game a 12-30+ mesi

- **AI Cluster #2 AI Engineer GenAI/LLMOps** (£100-200k UK) — richiede LangGraph deep + eval + multi-agent + MCP
- **SE Cluster #2 Fintech Low-Latency** (£80-130k UK) — richiede DAPR + observability + low-latency engineering

### Posizione cluster da NON over-investire upfront

- **SE Cluster #4 Fintech Java**: stack si impara on-the-job, focus universali
- **AI Cluster #1 AI Tech Lead Enterprise**: long-game, richiede anni
- **SE Cluster #3 Infrastructure/SRE**: richiede on-call exp accumulato sul lavoro

---

## 🔄 Update process

**Quando aggiornare questo file:**
- Dopo ogni batch di nuovi annunci analizzati (cadenza 3-5 annunci)
- Quando Dan scopre un cluster nuovo non rappresentato
- Quando il mercato evolve (nuove categorie emergenti, es. "AI-Native SRE")

**Workflow update:**
1. Aggiungere annunci a `context/job-postings-{topic}.md`
2. Se nuovo cluster emerge → aggiungerlo qui (con esempio + stack + accessibility)
3. Aggiornare path strategici se il bridge cambia
4. Cascade update a roadmap (link, non duplicare)

---

## 📚 File correlati

- `context/job-postings-analysis.md` — annunci AI Skills (8 annunci)
- `context/job-postings-senior.md` — annunci SE (12 annunci)
- `context/job-postings-frontend.md` — annunci FE (6 annunci)
- `context/job-postings-architect.md` — annunci Architect (skipped, decision log)
- `roadmaps/ai-skills.md` — roadmap AI con riferimento ai 4 cluster
- `roadmaps/senior-engineer.md` — roadmap SE con riferimento ai 6 cluster
- `roadmaps/senior-frontend.md` — roadmap FE con riferimento ai 6 cluster
- `career-strategy.md` — Cluster Positioning Matrix + salary per cluster
- `context/mini-projects-index.md` — central catalog Mini-Projects + sinergia cross-cluster

---

*Created: 2026-04-23 (refactor sessione job-postings-driven enrichment) — versione 1.0*
