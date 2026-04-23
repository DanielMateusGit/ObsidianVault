---
tags: [context, senior-frontend, job-market, gap-analysis]
created: 2026-04-23
status: batch-1-complete
---

# Job Postings Analysis — Senior Frontend Roadmap Enrichment

> Accumulo annunci rilevanti per il ruolo Senior Frontend (React + Flutter side-track). Ogni 3-5 annunci → gap analysis contro `roadmaps/senior-frontend.md` → update roadmap.

---

## Batch 1 (COMPLETO — 6/6) — UK focus, esteso a 6

### #1 — State Street — Front End Developer (Digital Asset / Financial Services) — Enterprise

**Meta:**
- Azienda: State Street (US, big custodian bank — enterprise financial services)
- Sede: non specificato (globally distributed team)
- Seniority: mid-level (non "senior" esplicito, "support from senior team members")
- Tipo: Enterprise frontend per fintech/digital asset platform
- Domain: **digital asset** (custody dashboards, tokenized assets, blockchain-adjacent UX)

**Stack tecnico (CORE):**
- **Modern JS framework:** React **OR** Angular **OR** Vue.js (agnostic — segnale enterprise)
- **HTML / CSS / JavaScript / TypeScript** (TS esplicito)
- **Responsive design**
- **REST API integration** + async data flows
- **Unit + component testing**
- **Version control + code reviews**

**Stack tecnico (NICE-TO-HAVE):**
- **Frontend testing frameworks** (component + end-to-end)
- **CI/CD integration**
- **Performance optimization** per data-heavy / operational UI ← importante enterprise
- **Node.js BFF** (Backend-for-Frontend lightweight) ← nuovo pattern
- Integrazione con Java backend enterprise

**Design / UX:**
- **Enterprise design systems** (State Street-approved, look&feel consistente)
- **Accessibility** (esplicito)
- Collaborazione UX/UI designer (translate wireframes → code)

**Security:**
- Frontend security basics (safe data handling, auth flows, common client-side issues — XSS, CSRF, etc.)

**Domain knowledge (differenziatore):**
- **Digital asset awareness**: custody dashboards, tokenized assets, transaction history, blockchain-adjacent flows
- Financial services / regulated environment experience

**Soft skills:**
- Agile ceremonies (sprint planning, stand-ups, reviews)
- Documentation (esplicito)
- Globally distributed teams + time zone management
- Quality + consistency + documentation mindset (regulated environment)

**Insight:**
Profilo **Enterprise Frontend Mid-Level**. Stack agnostic-by-design (React/Angular/Vue) → segnala che il valore è in:
1. **Modern FE fundamentals solidi** (HTML/CSS/JS/TS + responsive)
2. **Domain knowledge** (digital asset / finance)
3. **Enterprise discipline** (design system + a11y + docs + tests)
4. **Node.js BFF pattern** (lightweight backend-for-frontend)

**Differenze vs profilo "AI-Native FE" (#6 Euphoric):**
- Zero AI tools / AI methods / streaming UI
- Stack agnostic vs stack specifico
- "Support from senior" vs "ownership"
- Big enterprise vs scale-up startup

**Implicazione per Dan:**
Questo annuncio rappresenta il **cluster Enterprise FE** — accessibile con SE solido + portfolio React + tests. Tuttavia, è meno premium del cluster "AI-Native FE": tipicamente paga meno e carriera più lenta. Utile come **fallback option** o come trampolino per entrare in fintech.

---

### #2 — Moneybox (London, UK) — Web Developer (Modern Fintech FE)

**Meta:**
- Azienda: Moneybox (UK fintech wealth management, 1.5M utenti, established + scale-up)
- Sede: London hybrid (Oxo Tower)
- Seniority: mid-senior ("build and lead a team")
- Tipo: **Modern Fintech FE** (Next.js + Tailwind + headless CMS)
- Methodology: **Shape Up** (Basecamp's)

**Stack tecnico (SPECIFICO, non agnostic):**
- **Next.js / React (latest) con SSR / App Router** ← stack moderno esplicito
- **Tailwind CSS** ← utility-first standard
- **Zustand** (state management) ← Dan lo conosce ✅
- **TanStack Query** (server state / data fetching) ← nuovo pattern moderno
- **Storybook** (design system docs)
- **Contentful** (headless CMS)
- **Playwright** (E2E QA automation)
- **Vitest** o **Jest** (unit testing)
- **GraphQL** (knowledge)
- **Feature flagging + A/B testing** esplicito ← growth-engineering signal

**Infrastructure:**
- **Azure** (App Services, Docker, Azure Pipelines)
- **Azure DevOps + GitHub Actions** (CI/CD)
- Backend integration: **C# / .NET Core** ← interessante per Dan (stack già noto)

**Soft skills:**
- End-to-end ownership ("ship features from concept to launch")
- Code reviews + knowledge sharing
- Engineering excellence + clean/testable code
- Accessibility + security + performance **integrate nel lifecycle** (non add-on)

**Insight:**
- Stack tecnico **opposto a #1 State Street**: ultra-specifico, opinionated, moderno
- **Headless CMS pattern** (Contentful) → frontend disaccoppiato dal CMS
- **Feature flagging + A/B testing** esplicito → growth-mindset (overlap con #4 Jet HR / cluster #4 AI)
- Backend **C#/.NET Core** → coincidenza vantaggiosa per Dan (stack già noto)
- Methodology **Shape Up** → richiede mindset di scoping cycles e ownership totale

**Differenze vs #1 State Street:**
- Stack specifico vs agnostic
- Modern (Next.js + Tailwind + Zustand) vs traditional
- Storybook + Playwright + Vitest (modern testing) vs generic "testing frameworks"
- A/B testing + feature flagging esplicito (growth) vs zero
- Headless CMS (Contentful) vs design system enterprise

**Implicazione per Dan:**
Profilo **molto allineato** con il side track Senior Frontend. Stack quasi 1:1 con quello che dovresti studiare in roadmap (React + Tailwind + Zustand è già decisione attiva). Backend .NET Core = vantaggio competitivo per Dan. Differenziatore mancante: **Next.js SSR / App Router**, **TanStack Query**, **Storybook**, **Contentful**, **Playwright** — da verificare se in roadmap attuale.

---

## Pattern emergenti (2/5 annunci)

**Stack ricorrente in 2/2:**
- **TypeScript** (100%)
- **React** (100% — #1 lo nomina come opzione, #2 esplicito)
- **Testing frameworks** (100%)
- **CI/CD** (100%)
- **Accessibility** (100% esplicito)
- **Performance** (100% esplicito)
- **Code reviews + version control** (100%)

**Citato in 1/2:**
- **Next.js + SSR / App Router** (#2)
- **Tailwind CSS** (#2)
- **Zustand + TanStack Query** (#2)
- **Storybook** (#2)
- **Headless CMS (Contentful)** (#2)
- **Playwright E2E** (#2)
- **GraphQL** (#2)
- **A/B testing + feature flagging** (#2)
- **Azure infrastructure** (#2)
- **Node.js BFF** (#1)
- **Frontend security** (#1 esplicito, #2 implicito in "security")
- **Domain knowledge** financial / digital asset (#1)
- **Enterprise design system + Storybook** (#1 generico, #2 specifico)
- **Globally distributed teams** (#1)

### #3 — Xelix (London, UK) — React Developer (AI-AP Scale-up)

**Meta:**
- Azienda: Xelix (UK fintech AI per Accounts Payable automation, Series B Insight Partners Giu 2025)
- Sede: London hybrid (Hoxton, dog-friendly)
- RAL: **£60-75k** ← fascia mid (più bassa di Moneybox/Euphoric)
- Seniority: mid-senior (mentoring esplicito, "take responsibility")
- Tipo: **React Developer "puro"** in azienda AI (paradosso interessante: azienda AI ma ruolo non è AI-Native FE)

**Stack tecnico:**
- **React** (modern syntax, expert) ← richiesto deep
- **Redux + RTK Query** ← Dan lo conosce ✅ (decisione attiva: NON suggerire Zustand)
- **JavaScript + TypeScript** (esplicito)
- **CSS3** (no menzione Tailwind — segnale di stack legacy o custom CSS)
- **REST API + WebSocket** ← WebSocket nuovo nel batch
- **Playwright + Jest** (e2e + unit + integration)
- **Figma** (design handoff)

**Nice-to-have (differenzianti):**
- **Data visualization** ← overlap con #1 State Street (data-heavy UI)
- **UX/UI design skills** ← T-shaped FE+UX

**Soft skills:**
- **Mentoring** esplicito (segnale mid-senior)
- Code reviews + comprehensive tests
- Cross-browser / device QA
- Performance optimization
- Ownership ("take responsibility for solving the problem")
- Communication tech/non-tech

**Insight:**
- Paradosso interessante: **azienda AI** (AP automation con LLM) ma **ruolo FE puro** — l'AI è solo nel backend, FE è dashboard/workflow
- **Redux + RTK Query** vs Zustand + TanStack Query (#2): segnala 2 mondi paralleli del mercato React state management
  - Enterprise / scale-up consolidato → Redux Toolkit (consolidato, type-safe, DevTools)
  - Modern startup → Zustand + TanStack (leggero, opinionato, server-state separato)
- **CSS3 puro** (no Tailwind) → potrebbe essere stack legacy o scelta deliberata
- **Data visualization** come Big Plus → dashboard finanziari (analogia con custody dashboards #1)

**Differenze vs #1 e #2:**
- Stack React-specifico (vs #1 agnostic)
- Redux Toolkit (vs Zustand #2)
- WebSocket esplicito (vs solo REST in #1, #2)
- A11y NON esplicita (vs entrambi #1 e #2 espliciti) — possibile gap o omissione
- £60-75k → fascia mid London (vs £90-110k Euphoric, £90-200k fintech Series A)

**Implicazione per Dan:**
Profilo accessibile **immediatamente** con conoscenze attuali:
- ✅ React + Redux Toolkit (decisione attiva: Dan lo conosce)
- ✅ TypeScript
- ❓ WebSocket (non sicuro se in roadmap)
- ❓ Playwright (probabilmente in roadmap testing)
- ❓ Data viz (D3 / Recharts / Visx — non sicuro se in roadmap)

Salary più bassa indica: ruolo **bridge ideale** per entrare nel mercato UK frontend. Non target finale, ma trampolino.

---

### #4 — Edra (London + NY, Series A) — Product Engineer FE ⭐ HIGH-CRAFT

**Meta:**
- Azienda: Edra (Series A AI agents enterprise — Sequoia + lead VCs, NY + London)
- Sede: London + NY (in office presunto)
- RAL: non specificato (Series A premium, probabilmente top tier)
- Seniority: **3+ anni**
- Tipo: **Product Engineer / Founding FE** ← nuova categoria nel batch
- Domain: AI agents per process automation enterprise

**Filosofia esplicita:**
- "Care deeply about the craft of building software"
- Strong typing "**feels like a superpower, not a chore**"
- "Velocity and quality are **complementary, not competing**"
- "**No separation between building it and shipping it**"
- Greenfield work where decisions compound over time

**Stack tecnico (essenziale ma deep):**
- **TypeScript** (high standard: well-modeled, well-typed, well-documented)
- **React** (fundamentals strong)
- **Next.js** (in production, bonus point esplicito)
- Frontend architecture decisions ownership
- Component libraries / design systems
- API design awareness
- Backend debug capability ("debug backend in day-to-day")

**Soft skills (PESO ALTO — definiscono il ruolo):**
- **Visual + interaction judgment** (anche se non designer di titolo)
- **End-to-end ownership** ("no PM handing tickets")
- **Multiple hats** (morning component lib, afternoon designer pairing, evening backend debug)
- **Library/SDK building** track record (made other devs' lives easier)
- **Comfortable with ambiguity** (vague → well-scoped solution)
- **Greenfield mindset** (decisioni che compongono nel tempo)
- "Wear multiple hats when work demands it"

**Insight:**
- Categoria emergente: **Product Engineer / Founding Frontend** — analoga al cluster #4 AI-Augmented SWE ma full-craft FE
- Stack **stringato ma deep**: solo TS + React + Next.js, ma a livello craftsman
- Mindset di **founding engineer**: non solo "developer", è co-architetto del prodotto e cultura tech
- Esplicita differenziazione da AI Engineer ("If your primary interest is RAG/LLM/applied ML, check out our AI Engineering role")
- "Strong typing as superpower" → segnale di codebases altamente type-safe (Zod, branded types, discriminated unions)

**Differenze vs #1, #2, #3:**
- vs #1 State Street: opposite (greenfield craft vs enterprise discipline)
- vs #2 Moneybox: simile per Next.js, più craft-focused, meno feature-flagging/growth
- vs #3 Xelix: simile per ownership, ma stack moderno (Next.js vs Redux+CSS3)
- **Nuovo nel batch:** mindset "founding engineer" + library/SDK building + craft-bar esplicita

**Implicazione per Dan:**
Questo cluster è **accessibile** ma richiede:
- ✅ TypeScript a livello craft (non solo "uso", ma deep types, generics, well-modeled)
- ✅ React fundamentals deep (non solo "ho fatto componenti", ma architettura, performance, SSR)
- ❓ Next.js production experience
- ❓ Design system/component library building track record
- ❓ Tooling/SDK building visible (open-source o portfolio)

Per Dan: cluster molto interessante perché premia **mentalità engineer/architect** > "stack chasing". Compatibile con il suo background SE solido + Architect Quest. Differenziatore mancante: **portfolio di library/SDK pubbliche** (overlap con AI Mini-Projects Portfolio).

---

### #5 — Jumpstart (London, UK) — Founding Frontend Engineer (Platform/Aggregator)

**Meta:**
- Azienda: Jumpstart (NON un'azienda, è una **platform di matching** ingegneri ↔ startup VC-backed UK)
- Sede: London or remote-friendly UK
- RAL: **£50k - £120k** (range enorme, dipende da seniority + startup)
- Seniority: range ampio (Seed/Series A founding engineer)
- Tipo: **Founding Frontend Engineer** (conferma cluster #4 Edra come trend di mercato, non eccezione)

**Filosofia esplicita (forte signal di mercato):**
- "Most frontend roles today aren't really frontend roles. They're **ticket queues**. This one is different."
- → Si oppone esplicitamente al cluster Enterprise FE (#1 State Street)
- → Conferma che il cluster Product Engineer/Founding FE è un **pattern di mercato** in crescita

**Stack tecnico:**
- **Stack-agnostic dichiarato**: "We care far more about your ability to **reason, ship, and own** problems than about any specific tech stack"
- Modern frontend + backend tooling: **React, TypeScript, Node**
- "**Strong across the stack**" → full-stack mindset richiesto
- Product-minded > implementation-focused

**Soft skills (PESO ALTO — è il vero discriminante):**
- **High-agency** (autonomy, ownership, no PM tickets)
- **Pragmatic + autonomous**
- Comfortable con early-stage / fast-moving environments
- Clear communicators
- Collaborazione cross-engineering (design + product + founders)

**Recruitment process (signal mercato):**
- "**No live coding. No take-homes**" → conta reasoning + portfolio, non leetcode
- Portfolio richiesto in application: "**CV + anything you've built (GitHub, side projects, startups)**"
- → Conferma trend del batch AI: **GitHub portfolio è prerequisito di candidatura**

**Insight cross-cluster (importante):**
Questo annuncio è una **meta-conferma** del cluster #4 Edra. Jumpstart si è **specializzato** nell'aggregare questo tipo di ruolo (founding FE / product engineer). Significa che il pattern non è eccezione ma **tendenza di mercato UK** in forte crescita (Seed/Series A boom 2024-2026).

**Differenze vs precedenti:**
- vs #1 State Street: opposto polare (anti-ticket-queue)
- vs #2 Moneybox: simile per ownership ma più early-stage
- vs #3 Xelix: simile per ownership ma full-stack obbligatorio (non solo FE)
- vs #4 Edra: **conferma il cluster** (non è eccezione, è pattern)

**Implicazione per Dan:**
- Cluster Product Engineer/Founding FE = **trend di mercato UK** documentato da 2/5 annunci espliciti (Edra + Jumpstart) → vale investire in questa direzione
- **Portfolio GitHub è prerequisito assoluto** (Jumpstart application + Homey applicazione + Jet HR portfolio): ogni annuncio cluster #4/#5 lo richiede
- **Salary range £50-120k** conferma flessibilità: parte da junior £50k, arriva a senior founding £120k+
- Dan può candidarsi a Jumpstart **direttamente** quando vuole esplorare il mercato UK (no recruiter, no spam, CTOs pitch to you)

---

### #6 — Hook (London, UK) — Front End Engineer (AI/ML Customer Growth, Series A)

**Meta:**
- Azienda: Hook (UK fintech-adjacent, AI/ML per customer growth prediction, Series A — Balderton + Lightspeed top-tier VC)
- Sede: London hybrid (Liverpool Street, 3 giorni in office)
- RAL: **Up to £105k** (London) ← conferma fascia premium cluster #4
- Seniority: senior (deep TypeScript + React, ownership architecture)
- Tipo: **Hybrid Scale-up FE + Founding-flavored** (data viz + AI-curious + architecture influence)

**Stack tecnico:**
- **TypeScript + React** (deep, esplicito)
- Modern web technologies / modern frameworks
- **Data visualization + dashboards** ← CORE della role (overlap #3 Xelix, #1 State Street)
- API design collaboration con backend
- Performance + scalability + accessibility (esplicita)
- Cross-browser / device

**Caratteristiche speciali:**
- "Translate complex data and insights into clean, intuitive **visualisations and dashboards**" → data viz è **CORE** non nice-to-have
- Architecture influence ("Help define and evolve our front-end architecture")
- Backend API collaboration (not full-stack ma backend-aware)
- AI-curious ma non AI-Native FE puro (lavora in AI company ma costruisce dashboard, non streaming UI)

**Soft skills:**
- Ownership concept-to-deployment
- Collaborative cross-team (design + product + data + backend)
- "Eye for detail BUT know when to ship and iterate" → pragmatismo
- AI/data-driven products curiosity
- Initiative + autonomy

**Insight:**
Profilo **ibrido cluster #3 + #4**:
- #3 Scale-up React FE: data viz + ownership + senior
- #4 Founding FE: architecture decisions + craft + premium salary (£105k)
- AI awareness ma non AI-Native FE (no Vercel AI SDK, no streaming UI esplicito)

**Conferma trend dal batch:**
- **Data visualization** è ora citato in **3/6 annunci** (#1 State Street nice-to-have, #3 Xelix Big Plus, #6 Hook CORE) → trend forte per AI/fintech con dashboard analitici
- **Architecture ownership** in 4/6 annunci (cluster #2-#6 esclusi #1 enterprise) → mercato premia mid-senior con voice nelle decisioni
- **A11y** torna esplicita (#6 conferma), gap solo in #3, #4, #5 — adesso 3/6 espliciti

**Differenze vs precedenti:**
- vs #3 Xelix: stessa fascia mid-senior + data viz, ma stack moderno (no Redux esplicito) + salary premium (£105k vs £75k)
- vs #4 Edra: simile per architecture + craft, ma meno "founding" e più "scale-up consolidato"
- vs #5 Euphoric AI-Native: simile per AI-context, ma costruisce dashboard, non AI-UX (streaming, copilot)

**Implicazione per Dan:**
Profilo **sweet spot** per chi:
- Ama data viz + dashboard analitici
- Vuole salary premium senza esposizione totale founding-engineer-risk
- Curioso di AI ma non specializzato AI-FE

**Per Dan:** se il side-track FE include focus su **data visualization** (D3, Recharts, Visx, Tremor), questo cluster è ad alto ROI. Combinabile con Architect Quest dashboard + AI Mini-Projects con data viz.

---

## Pattern emergenti aggiornati (6/6 — finale)

**Stack ricorrente in 4/4 (CORE inevitabile):**
- **TypeScript** (100%)
- **React** (100%)
- **Code reviews / craft / quality** (100%)

**Citato in 3/4:**
- **Testing frameworks** (#1, #2, #3 — #4 non lo nomina ma "quality" implica)
- **Performance optimization** (#1, #2, #3)
- **End-to-end ownership** (#2, #3, #4 — #1 NO "support from senior")
- **Next.js / SSR** (#2, #4 espliciti, #1 opzionale)

**Citato in 2/4:**
- **Accessibility** (#1, #2 — gap in #3 e #4)
- **CI/CD** (#1, #2)
- **REST API + async data flows** (#1, #3)
- **Data visualization / data-heavy UI** (#1, #3)
- **Mentoring / sharing knowledge** (#1, #3)
- **State management opinionated** (#2 Zustand+TanStack, #3 Redux+RTK Query)
- **Component library / design system** (#2 Storybook, #4 building from scratch)
- **Backend awareness** (#1 BFF Node.js, #4 debug backend)

**Citato in 1/4:**
- **Tailwind CSS** (#2 — assente in #3 CSS3 puro, non specificato altri)
- **Headless CMS (Contentful)** (#2)
- **GraphQL** (#2)
- **A/B testing + feature flagging** (#2)
- **Azure** (#2)
- **WebSocket** (#3)
- **Figma handoff** (#3)
- **UX/UI design skills** (#3, #4 visual judgment)
- **Frontend security** (#1)
- **Domain knowledge fintech / digital asset** (#1, #4 enterprise process)
- **Globally distributed teams** (#1)
- **Library / SDK building track record** (#4)
- **Greenfield mindset** (#4)
- **Strong typing as superpower** (#4 esplicito)

**Tassonomia FE in 5 cluster (validata con 4 annunci batch FE + 1 batch AI):**

| Cluster | Esempio | Stack | Salary range UK |
|---------|---------|-------|-----------------|
| **Enterprise FE** | #1 State Street | Stack agnostic + design system + a11y + docs + Node.js BFF | non specificato (presunto £55-75k) |
| **Modern Fintech FE** | #2 Moneybox | Next.js + Tailwind + Zustand + TanStack + Storybook + Contentful | non specificato (~£70-90k) |
| **Scale-up React FE** | #3 Xelix | React + Redux Toolkit + RTK Query + WebSocket + Data viz | £60-75k |
| **Product Engineer / Founding FE** | #4 Edra | TS + React + Next.js (high-craft) + library building + greenfield | non specificato (Series A premium, presunto £90-130k+) |
| **AI-Native FE** | (#6 Euphoric — batch AI) | React/TS + Vercel AI SDK + streaming UI + AI methods | £90-110k |

**Stack ricorrente in 5/5 (CORE inevitabile):**
- **TypeScript** (100%)
- **React** (100% — esplicito o opzionale-tra-frameworks)
- **Code reviews / craft / quality** (100%)
- **End-to-end ownership / autonomy** (100% — anche #1 State Street richiede "deliver incremental features")

**Citato in 4/5:**
- **Testing frameworks** (#1, #2, #3, #5 — implicito #4)
- **Performance optimization** (#1, #2, #3, #4 implicito)
- **Product mindset** (#2, #3, #4, #5)
- **Backend awareness / full-stack** (#1 BFF, #4 backend debug, #5 Node esplicito) → 3/5 espliciti

**Citato in 3/5:**
- **Next.js / SSR** (#2, #4 espliciti, #1 opzionale)
- **Library/SDK/component building** (#2 Storybook, #4 esplicito, #5 Node)
- **GitHub portfolio in application** (#4 implicito, #5 esplicito, batch AI #5 Homey esplicito)

**Citato in 2/5:**
- **Accessibility esplicita** (#1, #2 — gap in #3, #4, #5)
- **CI/CD esplicita** (#1, #2)
- **REST API** (#1, #3)
- **Data visualization** (#1, #3)
- **Mentoring** (#1, #3)
- **State management opinionated** (#2 Zustand+TanStack, #3 Redux+RTK)
- **Greenfield / founding mindset** (#4, #5)
- **Stack-agnostic** (#1, #5)

**Citato in 1/5:**
- **Tailwind CSS** (#2)
- **Headless CMS** (#2 Contentful)
- **GraphQL** (#2)
- **A/B testing + feature flagging** (#2)
- **Azure** (#2)
- **WebSocket** (#3)
- **Figma handoff** (#3)
- **UX/UI design skills** (#3)
- **Frontend security** (#1)
- **Domain knowledge fintech / digital asset** (#1)
- **Strong typing as superpower** (#4)

---

## SINTESI FINALE BATCH 1 (5/5)

### Tassonomia FE consolidata (6 cluster) ⭐

| # | Cluster | Esempio | Stack chiave | Salary UK | Mindset | Accessibilità Dan |
|---|---------|---------|--------------|-----------|---------|--------------------|
| 1 | **Enterprise FE** | State Street | Stack agnostic + design system + a11y + Node BFF | ~£55-75k | Discipline + regulated | **Subito** (con cur portfolio) |
| 2 | **Modern Fintech FE** | Moneybox | Next.js + Tailwind + Zustand + TanStack + Storybook | ~£70-90k | Ownership + Shape Up + growth | **6-9 mesi** (manca Next.js + Storybook) |
| 3 | **Scale-up React FE** | Xelix | React + Redux Toolkit + RTK Query + WebSocket + Data viz | £60-75k | Ownership + mid-senior | **3-6 mesi** (Redux già noto, manca data viz) |
| 4 | **Product Engineer / Founding FE** ⭐ | Edra, Jumpstart | TS + React + Next.js high-craft + library/SDK + greenfield | £90-130k+ | Founding engineer + craft | **9-12 mesi** (richiede portfolio library/SDK) |
| 5 | **AI-Native FE** | Euphoric (batch AI) | React/TS + Vercel AI SDK + streaming UI + AI methods | £90-110k | AI-first + ship fast | **9-12 mesi** (richiede AI Mini-Projects) |
| 6 | **Data-Heavy AI FE (sweet spot)** ⭐ | Hook | TS + React + Data viz core + dashboard + AI awareness | up to £105k | Architecture influence + AI-curious + ship-pragma | **6-9 mesi** (manca data viz mastery) |

### Trend di mercato emergenti (validati 5/5)

1. **TypeScript + React = standard de facto** (5/5 annunci)
2. **Next.js sale come standard moderno** (3/5)
3. **GitHub portfolio = prerequisito di candidatura** (3/5 espliciti, conferma batch AI)
4. **State management bipolare**: Redux Toolkit (consolidato) vs Zustand+TanStack (modern)
5. **Founding/Product Engineer pattern in crescita** (2/5 espliciti — Edra + Jumpstart) → conferma trend
6. **"Anti-ticket-queue" mindset** esplicito (#5 Jumpstart) → mercato UK premia ownership
7. **Differenziatori che alzano salary/seniority**:
   - Next.js SSR / App Router
   - AI-Native skills (Vercel AI SDK, streaming UI)
   - Data viz (D3/Recharts/Visx)
   - Library/SDK building portfolio
   - "Founding engineer" craft mindset
8. **Testing moderni**: Playwright (E2E) + Vitest (unit) emergono come standard (2/5 espliciti)
9. **A11y** "must" per enterprise/fintech, "implicito" per scale-up/founding (gap interessante per portfolio)

### Insight strategici per Dan

**Vantaggio competitivo Dan ha già:**
- ✅ React + Redux Toolkit + TypeScript (decisioni attive)
- ✅ Backend .NET solido (vantaggio per #2 Moneybox + #4 Edra full-stack)
- ✅ Mindset Architect Quest = craft + ownership (allineato cluster #4)
- ✅ Claude Code cert (allineato cluster #5 AI-Native)

**Gap principali da colmare per cluster prioritario (#4 Founding FE):**
1. **Next.js production experience** (App Router, Server Components, RSC, streaming)
2. **TypeScript "as superpower"**: deep types, generics, branded types, Zod, well-modeled
3. **Component library / SDK** building track record (overlap AI Mini-Projects)
4. **Tailwind CSS** mastery (de facto standard moderno)
5. **Storybook** per design system docs
6. **Playwright + Vitest** testing stack moderno
7. **Portfolio GitHub pubblico** con almeno 2-3 progetti FE-craft

**Path strategico FE per Dan (ordine accessibilità):**

```
[OGGI] React + Redux + TS + .NET
    ↓
[3-6 MESI] Cluster #3 Scale-up React FE accessibile
    Required: Data viz library + Playwright + 1-2 progetti GitHub
    ↓
[6-9 MESI] Cluster #2 Modern Fintech FE accessibile
    Required: + Next.js App Router + Tailwind + Storybook + TanStack Query
    ↓
[9-12 MESI] Cluster #4 Founding FE accessibile (PREMIUM)
    Required: + library/SDK building portfolio + craft TS
    ↓
[9-12 MESI] Cluster #5 AI-Native FE accessibile (PREMIUM)
    Required: + Vercel AI SDK + streaming UI + AI Mini-Projects
```

**Sinergia con AI Skills roadmap:**
- Cluster #4 Founding FE + Cluster #4 AI-Augmented SWE = profili **complementari**
- Cluster #5 AI-Native FE = **intersezione perfetta** AI + FE (target sweet spot)
- AI Mini-Projects Portfolio (deciso 2026-04-23) serve a entrambi i path

---

## Gap identificati vs `roadmaps/senior-frontend.md`

*Da compilare in fase di gap analysis (prossimo step).*

---

## Gap identificati vs `roadmaps/senior-frontend.md`

*Da compilare a fine batch.*
