# 🎨 Senior Frontend - Roadmap

> **Focus:** Frontend React avanzato, best practices 2026, tecnologie di punta
> **Prerequisiti:** React solido (Dan ce l'ha)
> **Priority:** 🟢 Side track - quando c'è tempo/voglia

> [!important] 🔹 PERCORSO COMPLETO
> Tutto il Senior Frontend rientra nel **Percorso Completo**, non nel Percorso Minimo.
> Se il tempo è limitato, i progetti consigliati sono:
> - **P1 Focus Tube** — core React moderno + monetizzazione
> - **P5 FitHub Mobile** — Flutter + prodotto reale
>
> P2 Dashboard, P3 Component Lib, P4 Next.js E-commerce sono tagliabili senza impatto sul target €85k+.

---

## 📊 Overview

| Campo | Valore |
|-------|--------|
| **Ritmo** | Rilassato, self-paced (side track) |
| **Progetti** | 5 |
| **Focus** | React avanzato, performance, architettura FE, **Flutter** |
| **Output** | Portfolio FE + 2 SaaS monetizzabili (Focus Tube + FitHub) |

---

## 🎯 Obiettivi

1. Padroneggiare stack React 2026 (TanStack, Server Components, etc.)
2. Architettura frontend scalabile
3. Performance & Core Web Vitals
4. Almeno 1 progetto monetizzabile

---

## 🧭 6 Cluster di Ruolo FE Targetizzabili (data-driven da analisi mercato)

> Derivato da analisi 6 annunci UK + 1 batch AI (vedi `context/job-postings-frontend.md`). Il mercato FE ha **6 cluster distinti** con stack, accessibilità e salary diversi.

| Cluster | Esempio | Stack chiave | Salary UK | Accessibilità Dan |
|---------|---------|--------------|-----------|--------------------|
| **#1 Enterprise FE** | State Street | Stack agnostic + design system + a11y + Node BFF | ~£55-75k | Subito |
| **#2 Modern Fintech FE** | Moneybox | Next.js + Tailwind + Zustand + TanStack + Storybook | ~£70-90k | 6-9 mesi |
| **#3 Scale-up React FE** | Xelix | React + Redux Toolkit + RTK + WebSocket + Data viz | £60-75k | **3-6 mesi** ⭐ |
| **#4 Product Engineer / Founding FE** ⭐ | Edra, Jumpstart | TS + React + Next.js high-craft + library/SDK + greenfield | £90-130k+ | 9-12 mesi |
| **#5 AI-Native FE** | Euphoric | React/TS + Vercel AI SDK + streaming UI + AI methods | £90-110k | 9-12 mesi |
| **#6 Data-Heavy AI FE (sweet spot)** ⭐ | Hook | TS + React + Data viz CORE + dashboard + AI awareness | up to £105k | 6-9 mesi |

### Path strategico FE per Dan

```
[OGGI] React + Redux + TS + .NET (vantaggio competitivo backend)
    ↓
[3-6 MESI] Cluster #3 Scale-up React FE accessibile
    Required: P2 Dashboard + data viz + Playwright + 2-3 mini-projects GitHub
    ↓
[6-9 MESI] Cluster #2 Modern Fintech FE OR #6 Data-Heavy AI FE accessibili
    Required: + Next.js App Router + Tailwind + Storybook + TanStack Query + D3/Visx
    ↓
[9-12 MESI] Cluster #4 Founding FE OR #5 AI-Native FE accessibili (PREMIUM)
    Required: + library/SDK building + craft TS + Vercel AI SDK + streaming UI
```

### Portfolio richiesto per cluster

| Cluster | Cosa devi avere su GitHub |
|---------|---------------------------|
| #1 Enterprise | Portfolio React + tests + docs (Anche solo 1-2 progetti curati) |
| #2 Modern Fintech | 1 progetto Next.js + Storybook + headless CMS demo |
| #3 Scale-up React | Portfolio React + dashboard data viz + Playwright tests |
| #4 Founding | Component library/SDK pubblicata su npm + craft TS in evidenza |
| #5 AI-Native | Streaming UI demo + chat UI patterns + tool rendering live |
| #6 Data-Heavy AI | Dashboard analitico complesso + D3/Visx + drill-down + perf |

### Sinergia con altre roadmap

- **Cluster #5 AI-Native FE = sweet spot** intersezione AI + FE (compatibile target Dan AI Engineer)
- **Cluster #4 Founding FE** + Cluster #4 AI-Augmented SWE (`ai-skills.md`) = profili **complementari**
- **AI Mini-Projects Portfolio** (deciso 2026-04-23 in `ai-skills.md`) serve a **entrambi i path AI + FE**
- **P5 FitHub Mobile** (Flutter) connesso ad Architect Quest P5

---

## 📚 Progetti

### P1: Focus Tube 🎬
**Il tuo progetto! Client YouTube per focused learning.**

| Campo | Valore |
|-------|--------|
| **Tipo** | Full-stack (FE focus) |
| **Monetizzazione** | ⭐⭐⭐⭐⭐ Freemium SaaS |

**Stack:**
- TanStack Router + Query
- Zustand/Jotai (state)
- shadcn/ui + Tailwind
- React Hook Form + Zod
- Clerk (auth)
- Stripe (payments)
- .NET 8 backend (Clean Architecture)

**Impari:**
- TanStack ecosystem completo
- Community features (ratings, shared playlists)
- Subscription/payments
- YouTube Data API integration

---

### P2: Real-time Dashboard 📊 ⭐ MARKET-CRITICAL (cluster #6)
**Dashboard analytics con dati live + data viz mastery.**

> **Razionale (data-driven):** Data viz è in 3/6 annunci FE (cluster #6 Hook lo vuole CORE, £105k). Non basta Recharts/Tremor — serve mastery D3/Visx + dashboard pattern enterprise per accedere al cluster premium.

| Campo | Valore |
|-------|--------|
| **Tipo** | Frontend heavy |
| **Monetizzazione** | ⭐⭐⭐ Template/Boilerplate |
| **Cluster target** | #3 Scale-up React FE + #6 Data-Heavy AI FE |

**Stack:**
- **WebSockets + Server-Sent Events** (real-time)
- **Recharts / Tremor** (entry-level, decloration-based)
- **D3.js fundamentals** (low-level mastery)
- **Visx** (Airbnb, D3 + React pattern)
- **TanStack Virtual** (virtualization per liste/tabelle grandi)
- **Optimistic updates** + cache invalidation pattern

**Impari (entry-level → mastery):**
- Real-time data handling (WebSocket + SSE patterns, reconnection, backpressure)
- Data viz **decloration-based** (Recharts/Tremor) → **low-level** (D3) → **React-native** (Visx)
- Performance con dati massivi (virtualization, windowing, canvas vs SVG trade-off)
- **Dashboard enterprise patterns:**
  - Drill-down (aggregato → dettaglio)
  - Time-series large-scale (zoom, brush, pan)
  - Filter composition (multi-dim, stato URL-driven)
  - KPI composition (sparkline, deltas, trends)
  - Export (CSV, PDF, screenshot)
- **Decisione tecnologica:** Recharts (rapid prototyping) vs Visx (medium control) vs D3 puro (full control + perf) — quando usare cosa

**Deliverable:**
- Dashboard live con data viz multi-livello (KPI + time-series + drill-down)
- Esempio standalone D3 chart pubblicato su GitHub (per portfolio)
- Documentazione comparativa: Recharts vs Visx vs D3 (decision framework)

---

### P3: Component Library 🧩
**Design system completo, pubblicabile su npm.**

| Campo | Valore |
|-------|--------|
| **Tipo** | Library |
| **Monetizzazione** | ⭐⭐ Open source + consulting |

**Stack:**
- Storybook 8
- Radix UI primitives
- CVA (class-variance-authority)
- Changesets (versioning)
- Testing Library + Chromatic

**Impari:**
- Design system architecture
- Accessibility (a11y) profonda
- Component API design
- Publishing npm packages
- Visual regression testing

---

### P4: Next.js E-commerce ⚡
**Storefront performante con SSR/SSG/ISR.**

| Campo | Valore |
|-------|--------|
| **Tipo** | Full-stack Next.js |
| **Monetizzazione** | ⭐⭐⭐⭐ Template premium |

**Stack:**
- Next.js 15 (App Router)
- Server Components
- Server Actions
- Edge Runtime
- Vercel AI SDK (search)

**Impari:**
- SSR vs SSG vs ISR (quando usare cosa)
- Server Components patterns
- SEO avanzato
- Core Web Vitals optimization
- Edge computing

---

### P5: FitHub Mobile (Flutter) 📱🏋️
**App mobile per FitHub - collegata al backend Architect Quest P5.**

| Campo | Valore |
|-------|--------|
| **Tipo** | Mobile (Flutter) |
| **Monetizzazione** | ⭐⭐⭐⭐⭐ Parte del prodotto FitHub! |
| **Prerequisito** | Architect Quest P5 (FitHub Backend) |

**Stack:**
- Flutter 3.x
- Riverpod (state management)
- Drift (local DB)
- go_router (navigation)
- Consuma API FitHub backend (.NET)

**Impari:**
- Flutter da zero (rispolverare dal 2021!)
- State management moderno (Riverpod)
- Offline-first mobile
- Push notifications
- App Store / Play Store deployment
- White-label mobile (3 skin: Yoga, CrossFit, Gym)

**Collegamento Architect Quest:**
```
Architect Quest P5 (Backend)     Senior Frontend P5 (Mobile)
┌─────────────────────────┐     ┌─────────────────────────┐
│ .NET 8 API              │◄───►│ Flutter App             │
│ Multi-tenant            │     │ 3 skin white-label      │
│ AI Gateway integration  │     │ Offline-first           │
│ Notification Service    │     │ Push notifications      │
└─────────────────────────┘     └─────────────────────────┘
```

**Screens principali:**
- 🏠 Home (workout del giorno, AI suggestions)
- 📅 Calendar (schedule, prenotazioni)
- 💪 Workout (esercizi, timer, tracking)
- 📊 Progress (grafici, PR, statistiche)
- 👤 Profile (settings, subscription)
- 👨‍🏫 Coach Dashboard (solo per coach)
- 📈 Owner Analytics (solo per owner)

---

### P6: AI-Native FE Showcase 🤖 ⭐ MARKET-CRITICAL (cluster #5)
**App showcase con UX AI-first (streaming, copilot, tool rendering).**

> **Razionale (data-driven):** Cluster #5 AI-Native FE è premium UK (£90-110k Euphoric). Roadmap attuale lo cita solo come "Vercel AI SDK per search" in P4 — insufficiente. Serve un progetto dedicato che dimostri craft AI-FE.

| Campo | Valore |
|-------|--------|
| **Tipo** | Frontend AI-first showcase |
| **Monetizzazione** | ⭐⭐⭐⭐ Template AI-app + portfolio premium |
| **Cluster target** | #5 AI-Native FE + cross-roadmap con AI Skills |
| **Sinergia** | Riusa AI Mini-Projects (`ai-skills.md`) + Python AI Bridge |

**Stack:**
- **Next.js 15 App Router** + Server Components
- **Vercel AI SDK** (deep, non solo cenno): `useChat`, `useCompletion`, `streamUI`
- **AI SDK RSC** per React Server Components con streaming
- **shadcn/ui** + Tailwind (AI-friendly UI primitives)
- Backend: opzionale Python AI Bridge (sinergia con `ai-skills.md`)

**Impari (AI-FE mastery):**
- **Streaming UI** patterns: token-by-token, structured streaming, suspense boundaries
- **Chat UI craft**: message bubbles, typing indicators, code blocks, markdown rendering, copy-paste UX
- **Copilot UX**: ghost text, autocomplete, suggestions inline (à la Cursor / GitHub Copilot)
- **Tool-use rendering**: visualizzare quando l'agente chiama tool, mostrare progress, render risultati strutturati
- **Structured output UI**: rendering schemi Zod-validated come UI components dinamici
- **AI input patterns**: prompt input rich (mention, slash commands, file attach)
- **Error states AI-specific**: rate limit, timeout, hallucination detection feedback
- **Optimistic UI per AI**: mostrare risposta parziale + correggere
- **Latency masking**: skeleton loaders intelligenti, predictive prefetch

**Riferimenti reali da studiare:**
- **Cursor** (copilot UX, ghost text, agent mode)
- **v0.dev** (generative UI, streaming components)
- **Linear AI** (agentic actions UX)
- **ChatGPT / Claude.ai** (chat UI craft)
- **Vercel AI SDK examples** ([sdk.vercel.ai/docs/ai-sdk-rsc](https://sdk.vercel.ai/))

**Deliverable:**
- App Next.js 15 con chat AI streaming (riusabile come template)
- Demo deployata Vercel
- 1-2 pattern documentati come blog/README pubblico (es. "Building tool-use UI with AI SDK RSC")
- Repo GitHub portfolio-ready

**Boss Battle:**
**"Mini Cursor"**: editor di testo con copilot UX (ghost text + AI completions inline). +500 XP

---

## 🧪 MODULI TRASVERSALI (applicare a tutti i progetti)

### TypeScript Craft Module ⭐ (cluster #4 prerequisito)

> **Razionale:** Cluster #4 Founding FE (Edra, £90-130k+) richiede esplicitamente "TypeScript as superpower". Non basta "uso TS" — serve mastery deep.

**Topics dettagliati (10):**

1. **Generics avanzati**: bounded `<T extends ...>`, conditional types `T extends U ? X : Y`, mapped types `{ [K in keyof T]: ... }`, `infer` keyword per type extraction
2. **Branded types** (nominal typing) per type-safety dominio: `type UserId = string & { __brand: 'UserId' }` — `UserId` ≠ `OrderId` a compile-time
3. **Discriminated unions** + exhaustive `switch` con `never` enforcement: garanzia che tutti i case siano gestiti
4. **Zod inferenza**: schema → type (`z.infer<typeof schema>`), `parse()` vs `safeParse()`, transform pipeline, refinements
5. **Type-driven design**: "parse-don't-validate", types come spec del dominio, no `any`, no `as` casting senza motivazione
6. **Utility types custom**: `DeepPartial<T>`, `RequireAtLeastOne<T, K>`, `Prettify<T>`, `XOR<T, U>`
7. **TS strict mode + tsconfig production-grade**: `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`
8. **Template literal types**: type-safe routing, type-safe event names, builder patterns type-checked
9. **API contract types**: shared types FE/BE via tRPC, OpenAPI codegen (orval, openapi-ts), GraphQL codegen
10. **Type-level testing**: `expectType<>`, `assertType<>`, type-only test files

**Esercizio obbligatorio (cluster #4):**
- Refactor 1 modulo P1 Focus Tube (es. video state management) usando branded types per ID e Zod per validation
- Pubblica esempio TS Craft come **mini-project standalone** (vedi `context/mini-projects-index.md`)

**Da applicare in:** TUTTI i progetti P1-P6. Mindset, non modulo isolato.

**Risorse:**
- "Effective TypeScript" - Dan Vanderkam
- "TypeScript Deep Dive" - Basarat Ali
- Type Challenges (github.com/type-challenges/type-challenges)

---

### Modern Testing Stack ⭐

> **Razionale:** Mercato chiede Vitest + Playwright + MSW come standard 2026 (2/6 annunci espliciti, standard de facto).

**Stack standard:**
- **Vitest** — unit + integration testing (vs Jest: faster, ESM-native, Vite-based)
- **React Testing Library** — component testing user-centric (NO testing implementation details)
- **Playwright** — E2E + visual regression + cross-browser
- **MSW (Mock Service Worker)** — mock API network-level (no fetch mocks fragili)
- **Chromatic** — visual regression hosted per Storybook

**Topics dettagliati (10):**

1. **Test pyramid 2026**: 70% unit (Vitest), 20% integration (RTL + MSW), 10% E2E (Playwright)
2. **User-centric component testing**: `getByRole`, `getByLabelText`, no `getByTestId` se evitabile
3. **MSW setup pattern**: handlers per env (dev + test), runtime override per scenario
4. **Playwright POM (Page Object Model)** vs `test.use()` patterns
5. **Visual regression strategy**: cosa testare visivamente vs cosa skippare (animations, dynamic content)
6. **Cross-browser/device coverage**: matrix Playwright (Chromium + WebKit + Firefox + mobile viewports)
7. **Snapshot testing**: solo per output stabili (componenti UI presentazionali, no business logic)
8. **Test coverage target**: ≥80% logica business, lower per UI puro, **never coverage per coverage's sake**
9. **CI integration**: Vitest in unit jobs (parallelo), Playwright in E2E job (sharded)
10. **Test data management**: factories (`test-data-bot`, `Faker`), fixtures, NO duplication

**Esercizio obbligatorio:**
- 1 progetto SE/FE con stack completo: Vitest + Playwright + MSW + Chromatic + CI verde
- Documenta strategia test pyramid scelta nel README

**Da applicare in:** TUTTI i progetti P1-P6 da subito. No "lo aggiungo dopo".

---

### Frontend Security Module ⭐

> **Razionale:** Annuncio #1 State Street richiede esplicitamente "frontend security considerations". Cluster Enterprise + Fintech non transige. Necessario per qualsiasi cluster fintech (#2, #6).

**Topics dettagliati (10):**

1. **XSS (Cross-Site Scripting)**: React default escaping, `dangerouslySetInnerHTML` controlled, DOMPurify per user-generated HTML, `innerHTML` proibito
2. **CSRF (Cross-Site Request Forgery)**: SameSite cookies (Strict/Lax), CSRF token + double-submit cookie pattern, no GET per state-changing
3. **CSP (Content Security Policy)**: header config, nonce strategy per inline scripts, `report-only` mode for debugging, `Trusted Types` API moderna
4. **Auth flows secure**: OAuth 2.0 + PKCE per public clients, JWT refresh rotation, **httpOnly + Secure + SameSite cookies** > localStorage per token
5. **Safe data handling**: PII mask in logs/console, no secrets in repo (gitleaks pre-commit), HTTPS-only enforcement, sensitive data redaction Sentry-side
6. **OWASP Top 10 frontend**: A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection, A05 Security Misconfiguration
7. **Dependency security**: `npm audit` + Dependabot/Renovate, lockfile hygiene (`package-lock.json` committed), `npm ci` in CI (vs `npm install`)
8. **Subresource Integrity (SRI)** per CDN scripts: `<script integrity="sha384-...">` per third-party JS
9. **Iframe + clickjacking**: `X-Frame-Options: DENY` o CSP `frame-ancestors`, sandbox attribute per iframe untrusted
10. **Permissions API + sensitive APIs**: geolocation, notifications, camera/mic — request flow con UX rispettosa

**Esercizio obbligatorio:**
- Audit 1 progetto FE con OWASP ZAP (free tool) o Burp Suite Community → fix vulnerabilità trovate
- Pubblica `SECURITY.md` nel repo + audit report

**Da applicare in:** TUTTI i progetti che hanno auth (P1, P4, P5, P6) — security review esplicita prima del deploy.

**Risorse:**
- OWASP Cheat Sheet Series (Frontend Security)
- "Web Application Security" - Andrew Hoffman
- web.dev/secure

---

## 📦 FE MINI-PROJECTS PORTFOLIO (GitHub) ⭐ MARKET-CRITICAL

> **Razionale (data-driven):** 3/6 annunci FE chiedono esplicitamente "GitHub portfolio in application" (Edra, Jumpstart espliciti, conferma trend AI batch — Homey UK). **Prerequisito candidatura cluster #4 e #5.**

### Obiettivo

Costruire **5-10 micro-progetti FE standalone** (1-2 settimane ciascuno) **built with AI tools** (Cursor, v0.dev, Claude Code), pubblicati su GitHub con README pro + demo live.

### Filosofia (allineata ad AI Mini-Projects)

- **Small but shipped > big but unfinished**: ogni mini-project deployato + funzionante
- **Built with AI**, not just **about AI**: dimostri AI-augmented workflow (Cursor/v0/Claude Code)
- **README professionali**: problem, demo GIF, stack, AI tools usati, learnings
- **Craft visible**: TypeScript well-modeled, tests, a11y, performance

### Backlog idee (FE-specific)

| # | Idea | Cluster target | Stack | Effort |
|---|------|----------------|-------|--------|
| 1 | **D3 chart library** standalone (es. interactive heatmap) | #3, #6 | TS + D3 + Storybook | 1 settimana |
| 2 | **Tailwind landing page generator** AI-built | #4, #5 | Next.js + v0.dev + Vercel | 3-5 giorni |
| 3 | **Storybook design system** seed (10-15 componenti accessibili) | #2, #4 | Storybook + Radix + CVA | 1-2 settimane |
| 4 | **Streaming chatbot UI** (Vercel AI SDK demo) | #5 | Next.js + AI SDK + shadcn | 1 settimana |
| 5 | **Real-time dashboard** mini (con SSE + sparkline) | #3, #6 | React + Recharts + SSE | 1 settimana |
| 6 | **Component library** pubblicata su npm (es. accessibles primitives) | #4 | Vite + Radix + Changesets + npm | 2 settimane |
| 7 | **Playwright test suite** showcase (e2e demo + visual regression) | #2, #3 | Playwright + GitHub Actions | 3-5 giorni |
| 8 | **Tool-use UI** demo (mostra agente che chiama tool con feedback live) | #5 | Next.js + AI SDK + Zod | 1 settimana |
| 9 | **AI prompt input** rich (slash commands + mention + file attach) | #5 | React + custom rich input | 1 settimana |
| 10 | **Stripe subscription** flow demo (pricing → checkout → portal) | #2, #4 | Next.js + Stripe + webhooks | 1-2 settimane |

### Regole esecuzione

1. **Build with AI tools obbligatorio** (Cursor primario, secondario v0.dev/Claude Code) — documenta nel README
2. **Time-box stretto:** ≤2 settimane → tagli scope, non procrastini
3. **Public GitHub** + README + demo live (Vercel free tier)
4. **No perfezionismo:** "ship at 80%, iterate from feedback"
5. **TypeScript craft visible**: branded types, Zod, well-modeled

### XP

- Mini-project completato + GitHub README pro: +150
- Demo live deployata Vercel: +50
- README con AI tools usage doc: +30
- Mini-project con engagement (stars/issues/fork): +100
- 5 mini-projects raggiunti (cluster #4 ready): **Boss Battle "FE Portfolio Built" +500**

### Sinergia con AI Mini-Projects (`ai-skills.md`)

Alcuni mini-projects sono **dual-use** (AI + FE):
- #4 Streaming chatbot UI = AI Mini #2 Document Q&A chatbot lato FE
- #8 Tool-use UI = AI Mini #5 Multi-agent research assistant lato FE
- #9 AI prompt input = AI Mini #3 Email triage agent lato FE

→ ottimizza tempo: 1 progetto, 2 portfolio (AI + FE).

---

## 🛠️ Tecnologie Chiave

### Must Learn (Nuove per Dan)
| Tecnologia | Progetto | Perché |
|------------|----------|--------|
| TanStack Router | P1 | Type-safe routing, meglio di React Router |
| TanStack Query | P1, P2 | Data fetching moderno (1/6 annunci esplicito) |
| Zustand/Jotai | P1 | State leggero - diverso da RTK, impararlo per versatilita (*) |
| Server Components | P4, P6 | Il futuro di React |
| Storybook 8 | P3 | Component development (1/6 annunci esplicito) |
| **Vitest** | TUTTI | Unit/integration testing moderno (vs Jest legacy) |
| **Playwright** | TUTTI | E2E + visual regression (2/6 annunci esplicito) |
| **D3.js + Visx** | P2 | Data viz mastery (3/6 annunci) — cluster #6 CORE |
| **Vercel AI SDK** | P6, P4 | AI-Native FE streaming UI (cluster #5) |
| **Next.js 15 App Router + RSC** | P4, P6 | Standard moderno (3/6 annunci) |
| **MSW** | TUTTI | Mock API network-level per dev + test |
| **Edge Functions** | P4 | Vercel Edge / Cloudflare Workers (perf, locality) |
| **Stripe billing lifecycle** | P1 | Subscription, webhooks, customer portal |
| **Headless CMS (awareness)** | — | Contentful/Sanity (1/6 annunci esplicito) |
| **GraphQL (awareness)** | — | 1/6 annunci esplicito (Moneybox) |
| **BFF (Backend-for-Frontend)** | — | Pattern Node.js (1/6 annunci State Street) |

### Consolidare (Dan le conosce)
| Tecnologia | Focus |
|------------|-------|
| React 19 | Nuove features (use, Server Components, Suspense, Transitions) |
| **TypeScript Craft** ⭐ | Generics avanzati + branded types + Zod inferenza + discriminated unions + well-modeled domain (cluster #4 prerequisito) |
| Tailwind | Design tokens, theming, dark mode |
| Redux Toolkit + RTK Query | Già nei percorsi core, leverage per cluster #3 (Xelix) |

---

## 📋 Sequenza Progetti

```
TRASVERSALI (applicare a tutti i progetti, da subito):
  • TypeScript Craft Module (mindset)
  • Modern Testing Stack (Vitest + Playwright + MSW)
  • Frontend Security Module (auth, XSS, CSRF, CSP)
  • FE Mini-Projects Portfolio (5-10 micro-progetti GitHub, in parallelo)

PROGETTI CORE:
  Step 1: P1 Focus Tube        (core React moderno, monetizzabile, cluster #2/#3)
  Step 2: P2 Dashboard         (real-time + data viz mastery, cluster #3/#6) ⭐
  Step 3: P3 Component Lib     (design system + npm publish, cluster #4) ⭐
  Step 4: P4 Next.js Store     (SSR/SSG, cluster #2/#4)
  Step 5: P5 FitHub Mobile 📱  (Flutter, prodotto reale — richiede AQ P5 completato)
  Step 6: P6 AI-Native FE 🤖   (Vercel AI SDK + streaming UI, cluster #5) ⭐
```

**Note:**
- Ritmo rilassato, side project senza pressione. Nessuna scadenza.
- **Mini-Projects Portfolio in parallelo** ai progetti core (1-2 settimane ciascuno)
- **Moduli trasversali (TS Craft + Testing + Security)** non sono "progetti separati", sono mindset applicato sempre
- P5 FitHub Mobile richiede Architect Quest P5 (FitHub Backend) completato
- P5 è il progetto più importante per **monetizzazione**: prodotto reale + Flutter skill
- **P6 AI-Native FE è il più importante per cluster premium** (#5 AI-Native, sweet spot Dan)
- P3 Component Lib **promosso in priorità** per cluster #4 Founding FE (£90-130k+)

---

## 🎮 Gamification

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 🎨 **Frontend Initiate** | Primo progetto FE completato | +200 |
| ⚡ **Performance Guru** | Core Web Vitals tutti verdi | +150 |
| 📦 **Package Publisher** | Prima libreria su npm | +200 |
| 💰 **FE Monetizer** | Primo pagamento da Focus Tube | +500 |
| 📱 **Flutter Reborn** | FitHub Mobile MVP completato | +300 |
| 🏪 **App Store Ready** | Prima app pubblicata su store | +400 |
| 🏋️ **FitHub Launcher** | FitHub proposto alla palestra | +500 |
| 🤖 **AI-Native Frontend** | P6 completato + demo deployata | +400 |
| 📦 **Mini Builder** | 5 mini-projects pubblicati GitHub | +500 |
| 🚀 **Portfolio Pro** | 10 mini-projects + repo pinned curato | +750 |
| 🛡️ **Security Aware** | Frontend security audit + 0 vuln su dependency | +200 |
| 🎯 **TypeScript Craftsman** | Branded types + Zod inferenza in 3+ progetti | +300 |
| 🧪 **Testing Champion** | Vitest + Playwright + MSW in 3+ progetti | +200 |
| 🏆 **Senior Frontend** | Tutti i progetti completati | +1500 |

---

## 📝 Note

- **Nessuna deadline rigida** - e un side track
- **Inizia quando vuoi** - dopo aver consolidato BE basics
- **Flessibile** - progetti possono cambiare in base a nuove idee
- **P1 Focus Tube e il core React** - gli altri React sono "nice to have"
- **P5 FitHub Mobile e il core Flutter** - progetto reale monetizzabile!
- **Flutter skill nuova** - rispolverare dal 2021, ottimo per portfolio
- **(*)Zustand in P1:** Dan conosce gia Redux Toolkit e lo usa nei percorsi principali. In questo side track, Zustand/Jotai e intenzionale come opportunita di apprendimento per ampliare la versatilita frontend. NON sostituisce RTK nei progetti core.

---

*Creato: 2026-02-24*
*Aggiornato: 2026-04-23 (v2.1 — Refactor pulizia: moduli trasversali (TypeScript Craft + Modern Testing + Frontend Security) ora con 10 topic dettagliati + esercizi obbligatori specifici. Cluster taxonomy referenzia `context/cluster-taxonomy.md`. Mini-Projects link `context/mini-projects-index.md`)*
*Versione precedente: 2026-04-23 (v2.0 — Job-postings-driven enrichment iniziale)*
*Status: 🟢 Pianificato - Da iniziare*
