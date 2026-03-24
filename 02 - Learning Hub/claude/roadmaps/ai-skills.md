# 🤖 Roadmap: AI Skills Track → AI Engineer

> Percorso parallelo per diventare **AI Engineer** capace di costruire sistemi AI production-ready.
> Target: ruolo AI Engineer / AI-Native Engineer (€90-130k EU, €110-160k US)

## 🎯 Obiettivo Finale

Essere un **AI Engineer completo** capace di:
- **Creare MCP Servers** - Estendere Claude con tool e dati custom
- **Claude API mastery** - Integrazioni avanzate, prompt engineering, agentic workflows
- **Ollama locale** - AI embedded nelle app (privacy, offline, zero cost)
- **Hybrid architectures** - Orchestrare Ollama + Claude + MCP
- **Tool building** - Creare strumenti che Claude può usare
- **Prompt optimization** - Massimizzare reasoning di Claude
- **AI Evals & Observability** - Misurare e monitorare sistemi AI in produzione
- **Guardrails & Safety** - Proteggere sistemi AI da prompt injection, output pericolosi
- **Multi-Agent Systems** - Orchestrare agenti specializzati che collaborano
- **AI Testing** - Testare output non-deterministici, regression testing su prompt
- **Fine-tuning Decision Framework** - Sapere QUANDO usare RAG vs fine-tuning vs prompt engineering

---

## 🧠 **FILOSOFIA: Quando Usare Cosa**

```
┌─────────────────────────────────────────────────────────────┐
│                    OLLAMA (Local AI)                        │
│  Use Cases: Fast, Private, Offline, Zero Cost              │
├─────────────────────────────────────────────────────────────┤
│  ✅ Intent recognition (user messages)                     │
│  ✅ Entity extraction (dates, numbers, names)              │
│  ✅ Categorization (expenses, emails)                      │
│  ✅ Embedded in apps (offline-first)                       │
│  ✅ Privacy-critical data (healthcare, finance)            │
│  ✅ High-volume, low-complexity tasks                      │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  CLAUDE API (Cloud AI)                      │
│  Use Cases: Complex Reasoning, Planning, Orchestration     │
├─────────────────────────────────────────────────────────────┤
│  ✅ Complex reasoning & planning                           │
│  ✅ Code generation & review                               │
│  ✅ Multi-step workflows (agentic)                         │
│  ✅ Context-heavy analysis                                 │
│  ✅ Orchestration of multiple systems                      │
│  ✅ When accuracy > speed/cost                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│            MCP SERVERS (Extend Claude)                      │
│  Use Cases: Custom Tools, Data Access, Actions             │
├─────────────────────────────────────────────────────────────┤
│  ✅ Give Claude access to your databases                   │
│  ✅ Custom tools (calendar, notifications, analytics)      │
│  ✅ Domain-specific actions                                │
│  ✅ Real-time data integration                             │
│  ✅ Make Claude "aware" of your systems                    │
└─────────────────────────────────────────────────────────────┘

BEST: Combine all three for ultimate flexibility!
```

---

## 📅 Timeline Overview

> **Nota:** I mesi qui corrispondono a quelli in `architect-quest.md` (fonte di verita per le date).

```
Mesi 6-8:   P2.5 - AI Engineer Calendar System
            ├─ Phase 1: Ollama Foundation (intent parsing)
            ├─ Phase 2: Claude API + MCP Server + Guardrails
            └─ Phase 3: Multi-Agent + Evals + Production

Mesi 13-18: P3 - BookingHub + AI Integration
            ├─ MCP Server for booking data
            ├─ Claude-powered admin assistant
            └─ Hybrid Ollama + Claude architecture

Mesi 19-24: P4 - FamilyBudget + AI Integration
            ├─ MCP Server for financial data
            ├─ Claude budget advisor (complex reasoning)
            └─ Ollama for categorization (fast, local)
```

**Approccio:** Impara progressivamente (Ollama → Claude → MCP → Agentic), poi applica in sistemi complessi.

---

## 🤖 PROGETTO 2.5: AI Gateway + Calendar System (Mesi 6-8) 🔧 SHARED SERVICE

> **Tipo:** Shared Service - L'AI Gateway sarà riutilizzato da P3 BookingHub e P4 FamilyBudget
>
> **Filosofia:** Impara principi **universali** applicabili a qualsiasi LLM, poi specializzati su Claude per il vantaggio competitivo.

### Ruolo nell'Ecosystem
```
P2.5 AI Gateway → P3 BookingHub (assistente prenotazioni)
                → P4 FamilyBudget (categorizzazione, consigli)
```

### Obiettivo
Sistema calendario intelligente **provider-agnostic** che combina:
- **Ollama** (AI locale - concetti universali)
- **Claude** (AI cloud - esempio specifico, ma architettura riutilizzabile)
- **Provider abstraction** (facilmente estendibile a OpenAI, Gemini, etc.)

**Skill trasferibili al 95%** - Puoi applicare tutto ad altri LLM con minime modifiche.

### Stack (Provider-Agnostic)
- **AI Layer (Abstracted):**
  - Ollama (llama3.1:8b) - Intent parsing locale
  - Claude API (Sonnet 4.5) - Complex reasoning **[Facilmente sostituibile con OpenAI, Gemini, etc.]**
  - Provider abstraction layer - **IAIProvider interface**
  - Tool system (generic, not MCP-only)
- **Backend:** .NET 8 Minimal API
- **Data:** PostgreSQL, Redis
- **Integrations:** Google Calendar, Microsoft Graph API
- **Frontend:** Flutter (iOS + Android) 📱
- **Optional:** Native voice input (Flutter speech_to_text)

### 📱 Decisione: Flutter Mobile App (2026-02-11)

**Scelta:** Flutter invece di React web

**Perché:**
- App mobile nativa (iOS + Android) da un solo codebase
- Esperienza utente migliore su telefono (notifiche push, voice input nativo)
- Skill Flutter riutilizzabile in altri progetti
- Offline-first possibile (calendar sync)

**Trade-offs:**
- Refresh Flutter necessario (Dan ha esperienza 2021, basi solide ma da rispolverare)
- Backend deve esporre API REST/gRPC pulite (no server-side rendering)

**Nota:** Dan ha già le basi Flutter (2021) → refresh veloce, non da zero

**Architettura:**
```
┌─────────────────────────────┐
│   Flutter App (iOS/Android) │
│   ├─ Chat UI                │
│   ├─ Voice input (optional) │
│   └─ Local cache (Hive/SQLite)
└──────────────┬──────────────┘
               │ REST API / WebSocket
               ▼
┌─────────────────────────────┐
│   .NET 8 Backend            │
│   (AI Router + Orchestrator)│
└─────────────────────────────┘
```

---

### 🎓 **Progressione Didattica: Generico → Specifico**

Il progetto è strutturato per insegnare **prima i fondamentali universali**, poi specializzarti:

| Phase | Focus | Genericità | Trasferibilità |
|-------|-------|------------|----------------|
| **1 (W1-3)** | Ollama + Fundamentals | **100% Generico** | Applicabile a qualsiasi LLM |
| **2 (W4-6)** | Claude + Tools + Guardrails + Fine-tuning Framework | 80% Generico | Concetti tool use + safety + decision framework universali |
| **3 (W7-9)** | Multi-Agent + Evals + Production | **95% Generico** | Pattern AI Engineer universale |

**Risultato:** Sai lavorare con Claude (vantaggio competitivo) MA puoi adattarti a qualsiasi provider in giorni, non mesi.

### Cosa Impari (con livello di genericità)

#### **Phase 1: Ollama Foundation** (W1-3) → **100% UNIVERSALE** ✅

**Skill generiche applicabili a QUALSIASI LLM:**
- ✅ Prompt engineering fundamentals
- ✅ Function calling / Tool use (standard OpenAI/Anthropic)
- ✅ Intent recognition patterns
- ✅ Entity extraction techniques
- ✅ JSON mode forcing
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Context management strategies
- ✅ Local AI deployment

**Nota:** Usi Ollama come "lab gratuito", ma i concetti funzionano identici con GPT-4, Gemini, Mistral, etc.

---

#### **Phase 2: Cloud AI + Tool Systems** (W4-6) → **80% UNIVERSALE** ✅

**Skill generiche:**
- ✅ Cloud API integration patterns (HTTP, streaming, retry)
- ✅ Tool use / Function calling (standard tra provider)
- ✅ Streaming responses (SSE, WebSocket)
- ✅ Cost tracking & optimization
- ✅ Provider abstraction design
- ✅ Tool definition schemas (JSON Schema - universale)

**Skill Claude-specific (MA trasferibili):**
- ⚡ Anthropic Messages API (simile a OpenAI Chat Completions)
- ⚡ MCP Protocol (Claude-specific, MA concetti di "tool server" universali)
- ⚡ Extended thinking mode (unico Claude, ma pattern applicabile)

**Tempo per passare a OpenAI dopo questa fase:** ~2-3 giorni (solo SDK diverso, logica identica)

---

#### **Phase 3: Provider-Agnostic Architecture** (W7-8) → **95% UNIVERSALE** ✅

**Architettura completamente generica:**
- ✅ **AI Router pattern** (funziona con QUALSIASI provider)
- ✅ **Provider abstraction layer** (`IAIProvider` interface)
- ✅ Multi-provider fallback chains
- ✅ Agentic workflows (concetti universali)
- ✅ Tool orchestration (non MCP-specifico)
- ✅ Cost optimization strategies
- ✅ Observability patterns

**Risultato:** Sistema che può usare Claude, OpenAI, Gemini, o Ollama intercambiabilmente.

---

## 🏗️ **PROVIDER-AGNOSTIC ARCHITECTURE**

### Perché è Importante

**Scenario reale:**
- Oggi: Claude è il migliore per reasoning
- Domani: OpenAI GPT-5 supera Claude
- Dopodomani: Nuovo provider emerge

**Con architettura agnostica:** Cambi provider in **1 giorno**, non 1 mese.

### Provider Abstraction Layer

**Concetti chiave (implementazione durante il progetto):**
- `IAIProvider` interface universale (Chat, ChatWithTools, ChatStream, GetCost)
- Implementazioni: `OllamaProvider`, `ClaudeProvider`, `OpenAIProvider`
- `AIRouter` sceglie provider dinamicamente (reasoning → Claude, fast → Ollama, budget → Ollama)
- Fallback chain configurabile

**Risultato:** Il resto del codice usa `IAIProvider`, non dipende da Claude specificamente.

### Tool System (Generic)

**Concetti chiave:**
- `Tool` record con Name, Description, Parameters (JSON Schema)
- `IToolExecutor` interface generica
- `ToolRegistry` per registrare e invocare tool

**Funziona con:** Claude (tool use), OpenAI (function calling), Gemini (function calling), Ollama (custom prompt)

---

### Architecture (Hybrid: Ollama + Claude + Provider Abstraction)

```
┌─────────────────────────────────────────────────────────┐
│                   User Interface                         │
│      (React + Natural Language + Voice Input)           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              .NET 8 Web API (Orchestrator)              │
│                                                          │
│  ┌──────────────────┐          ┌───────────────────┐   │
│  │  Ollama Service  │          │  Claude Service   │   │
│  │  (Fast, Local)   │          │  (Smart, Cloud)   │   │
│  └────────┬─────────┘          └─────────┬─────────┘   │
│           │                              │             │
│           │    ┌─────────────────────────┘             │
│           ▼    ▼                                        │
│  ┌──────────────────────┐                              │
│  │   AI Router          │ ← Decides: Ollama or Claude? │
│  │   (Smart Dispatch)   │                              │
│  └──────────┬───────────┘                              │
│             │                                           │
│             ▼                                           │
│  ┌─────────────────────┐                               │
│  │  Calendar Actions   │ ← Executes via APIs           │
│  └──────────┬──────────┘                               │
│             │                                           │
└─────────────┼───────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│   MCP Server (TypeScript)                               │
│   ├─ calendar.list_events()                             │
│   ├─ calendar.create_event()                            │
│   ├─ calendar.find_free_slots()                         │
│   └─ calendar.get_preferences()                         │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│  Google Calendar  │  Outlook  │  PostgreSQL  │  Redis  │
└─────────────────────────────────────────────────────────┘

FLOW EXAMPLE (Provider-agnostic):
1. User: "Prenota dal dentista martedì"
   → AIRouter → OllamaProvider (fast intent extraction)
   → Ollama extracts: intent=create, date=2026-02-11

2. System: Complex reasoning needed?
   → AIRouter → ClaudeProvider (or OpenAI, configurable)
   → AI uses registered tools to check availability
   → AI reasons: "14:00 is best (after lunch, before busy hours)"

3. System creates event via Google Calendar API
```

---

## 📊 **SKILL TRANSFERABILITY MATRIX**

### Quanto Tempo Serve per Passare ad Altri Provider?

| Skill Imparata | Claude | OpenAI GPT-4 | Google Gemini | Ollama | Transfer Time |
|----------------|--------|--------------|---------------|---------|---------------|
| **Prompt Engineering** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (identico) |
| **Function Calling** | ✅ tool_use | ✅ functions | ✅ function_calling | ✅ custom | **1-2 giorni** (sintassi diversa, concetti identici) |
| **JSON Mode** | ✅ | ✅ response_format | ✅ | ✅ | **0 giorni** (identico) |
| **Streaming** | ✅ SSE | ✅ SSE | ✅ SSE | ✅ SSE | **0 giorni** (standard) |
| **Context Management** | ✅ 200K | ✅ 128K | ✅ 1M | ✅ varies | **0 giorni** (concetto universale) |
| **RAG Pattern** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (universale) |
| **Agentic Workflows** | ✅ | ✅ | ✅ | ⚠️ limited | **1-2 giorni** (API diversa, logica identica) |
| **MCP Protocol** | ✅ native | ❌ custom | ❌ custom | ❌ custom | **3-5 giorni** (devi implementare adapter) |
| **Cost Optimization** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (pattern universale) |
| **Provider Abstraction** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (hai già l'interfaccia!) |
| **AI Evals** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (universale, provider-agnostic) |
| **Guardrails/Safety** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (pattern universale) |
| **Multi-Agent** | ✅ | ✅ | ⚠️ partial | ⚠️ limited | **1-2 giorni** (SDK diversi, pattern identici) |
| **AI Testing** | ✅ | ✅ | ✅ | ✅ | **0 giorni** (universale) |

### **Tempo Totale per Migrare ad Altro Provider**

Dopo questo percorso:
- **Da Claude a OpenAI:** 2-3 giorni (solo SDK diverso)
- **Da Claude a Gemini:** 3-4 giorni (API meno matura)
- **Aggiungere 2° provider (fallback):** 1 giorno (hai già l'interfaccia!)
- **Supportare 3+ provider simultanei:** 2-3 giorni (router già pronto)

### **Cosa È Claude-Specific (e cosa farne)**

| Feature Claude-Specific | Transfer Strategy |
|------------------------|-------------------|
| **MCP Protocol** | Concetti → "tool server pattern" universale. Puoi creare adapter OpenAI-MCP |
| **Extended Thinking** | Concetto → "reasoning mode". Altri provider lo aggiungeranno |
| **Artifacts** | Concetto → "structured outputs". Implementabile con qualsiasi LLM |
| **Sonnet vs Opus models** | Concetto → "model selection strategy". Ogni provider ha tiers |

**Bottom line:** Anche le feature "Claude-only" insegnano pattern architetturali universali.

---

## Multi-Provider Support

**Pattern:** `AIConfiguration` con provider map + `RoutingStrategy` (fast → ollama, complex → claude, fallback chain).
Il service layer usa `IAIRouter` senza sapere quale provider verra usato. Cambio provider = cambio config, zero codice.

---

### Features - Progressive Evolution

#### **PHASE 1: Ollama Foundation** (Settimane 1-3)

**Goal:** Local AI per intent parsing veloce e privacy-first

**Week 1: Ollama Setup & Integration**
- Setup Ollama in .NET (HttpClient + JSON)
- Basic prompt engineering
- Intent recognition (create/read/update/delete)
- Entity extraction (date, time, duration, title)
- JSON mode forcing (no markdown, always valid JSON)

**Week 2: Calendar API Integration**
- Google Calendar API setup + OAuth
- CRUD eventi via API
- Date parsing ("domani", "martedì prossimo")
- Conflict detection
- Basic testing

**Week 3: RAG Reale + Context Management**
- **🔍 Vector Search con pgvector** (PostgreSQL extension — gia nel tuo stack)
  - Il Calendar System deve cercare eventi per significato, non solo per data
  - "Trova quel meeting dove parlavamo di budget" → vector similarity search
  - pgvector setup, indici HNSW vs IVFFlat, distanza coseno vs L2
  - Confronto pratico: pgvector vs Qdrant (quando serve un DB dedicato?)
- **🧠 Embedding model selection**
  - Quale modello per contenuto misto italiano/inglese? Benchmark 2-3 modelli
  - Ollama embeddings (nomic-embed-text) vs API (voyage, OpenAI)
  - Dimensioni embedding: 384 vs 768 vs 1536 — trade-off qualita/costo/velocita
- **📦 Chunking & retrieval strategies**
  - Come spezzi gli eventi in chunk? (per campo? per settimana? overlap?)
  - Hybrid search: keyword (PostgreSQL full-text) + vector → reranking
  - Query decomposition: "Sono libero martedi dopo pranzo?" → 2 sub-query (eventi martedi + orari pranzo)
- Conversation history (PostgreSQL)
- Context window management & multi-turn
- Redis caching per risposte comuni
- Flutter app MVP (chat interface)

**Deliverable Phase 1:** Calendar assistant con Ollama + RAG reale (vector search, non solo text match) ✅

---

#### **PHASE 2: Claude API + MCP Server** (Settimane 4-6)

**Goal:** Introduce Claude per reasoning complesso + crea MCP server

**Week 4: Claude API Integration**
- Setup Claude API (.NET SDK)
- Anthropic Messages API
- Streaming responses
- Tool use (function calling)
- Prompt engineering per Claude
- Cost tracking & optimization

**Week 5: MCP Server Development** 🎯 **CORE LEARNING**
- **Crea primo MCP Server (TypeScript/Python)**
- Tool definitions:
  - `calendar.list_events(start_date, end_date)`
  - `calendar.create_event(title, date, time, duration)`
  - `calendar.find_free_slots(date, min_duration)`
  - `calendar.get_user_preferences()`
- MCP protocol implementation
- Tool registration con Claude
- Testing con Claude Desktop

**Week 6: Claude Reasoning + Guardrails + Decision Framework**
- Complex queries via Claude:
  - "Quando sono libero per un caffè con Marco?"
  - "Suggerisci il miglior orario per un meeting importante"
  - "Analizza la mia settimana e dimmi dove posso ottimizzare"
- Multi-step reasoning
- Claude + MCP tools orchestration
- Comparison Ollama vs Claude (speed, accuracy, cost)
- **🛡️ AI ENGINEER GAP: Guardrails & Safety**
  - Prompt injection defense (user input sanitization)
  - Output validation layer (schema check, content filter)
  - PII detection nelle risposte
  - Test di sicurezza AI (adversarial prompts)
- **🧠 AI ENGINEER GAP: Fine-tuning Decision Framework**
  - Decision tree: RAG vs fine-tuning vs prompt engineering (quando usare cosa)
  - Costo/beneficio fine-tuning (quando vale la pena vs RAG)
  - Awareness: come funziona il fine-tuning (teoria, no hands-on richiesto)
  - Data preparation: formato, qualita, quantita minime

**Deliverable Phase 2:** MCP Server funzionante + Claude integration + Guardrails layer + Fine-tuning decision framework ✅

---

#### **PHASE 3: Agentic Workflows** (Settimane 7-8)

**Goal:** Claude autonomous agent che orchestra tutto il sistema

**Week 7: Hybrid Architecture**
- **AI Router:** Decide quando usare Ollama vs Claude
  - Ollama → Fast intent parsing, simple queries
  - Claude → Complex reasoning, multi-step workflows
- Smart dispatch logic
- Cost optimization (95% Ollama, 5% Claude)
- Performance benchmarking

**Week 8: Autonomous Agent + Multi-Agent** 🚀
- **Claude come autonomous agent:**
  - User: "Organizza la mia settimana"
  - Claude:
    1. Reads all events via MCP
    2. Analyzes patterns & conflicts
    3. Proposes optimizations
    4. Executes changes (with confirmation)
- Multi-step workflows
- Error recovery & fallbacks
- **🤖 AI ENGINEER GAP: Multi-Agent Systems**
  - Planner agent + Executor agent + Reviewer agent pattern
  - Agent SDK exploration (Claude Agent SDK)
  - Agent communication & handoff patterns
  - When single-agent vs multi-agent (decision framework)

**Week 9: AI Evals, Testing & Production** 🎯 (NUOVA)
- **📊 AI ENGINEER GAP: Evaluation & Observability**
  - Eval pipeline: input → LLM → output → score (automated)
  - Metriche: accuracy, hallucination rate, latency, cost per request
  - A/B testing prompt (quale funziona meglio?)
  - Dashboard metriche AI (Langfuse o custom)
  - Token usage tracking & cost alerts
- **🧪 AI ENGINEER GAP: AI Testing**
  - Testing output non-deterministici (range-based assertions)
  - Snapshot testing per prompt (regression)
  - Contract testing per tool use (schema validation)
  - Eval-driven development: scrivi l'eval PRIMA del prompt
- **🚀 AI Deployment & Serving**
  - Ollama in produzione: Docker container con modello pre-loaded, healthcheck, memory limits
  - CPU vs GPU trade-off per inference locale (M4 Pro = ottimo per dev, ma in cloud?)
  - Scaling AI endpoints: quando un singolo container non basta (queue + workers)
  - Model caching: evitare cold start di 10s su primo request
- Production polish:
  - Observability completa (Logs, metrics, traces con AI-specific dimensions)
  - Rate limiting per utente + per provider (budget protection)
  - Graceful degradation (Claude down? Fallback a Ollama con UX ridotta)
  - Voice interface Flutter (speech_to_text, opzionale)

**Deliverable Phase 3:** Multi-agent system + eval pipeline + AI production-ready ✅

### Conversation Examples

```
User: "Prenota dal dentista martedì prossimo alle 15"
AI:   "Ho capito. Vuoi prenotare:
       📅 Martedì 11 febbraio 2026
       🕒 15:00 - 16:00
       📝 Dentista

       Confermi?"

User: "Sì, e manda promemoria 1 ora prima"
AI:   "✅ Evento creato su Google Calendar
       🔔 Promemoria impostato per le 14:00"

---

User: "Quando ho tempo libero questa settimana per un caffè?"
AI:   "Ecco i tuoi slot liberi di almeno 1 ora:
       • Mercoledì 5 feb: 14:00-16:00 ✨
       • Giovedì 6 feb: 10:00-12:00
       • Venerdì 7 feb: 15:00-18:00

       (✨ = consigliato, hai pochi meeting quel giorno)"

---

User: "Ho troppi meeting domani, sposta quelli non urgenti"
AI:   "Ho trovato 5 meeting domani. Questi sembrano spostabili:
       1. ☕ 1-1 con Sara (internal)
       2. 📊 Review metrics (internal)

       Vuoi spostarli a dopodomani?"
```

### Technical Highlights (da implementare durante il progetto)

**Ollama Function Calling:**
- System prompt con funzioni disponibili + JSON response format
- Temperature bassa (0.3) per parsing consistente
- Conversation history per contesto multi-turn

**RAG Pattern (Production-grade):**
- Pipeline: Query → Embedding → Vector search (pgvector) → Reranking → Context injection → LLM
- Hybrid retrieval: vector similarity + keyword full-text → merge & rerank risultati
- Chunking strategy: sliding window con overlap, metadata preservation
- Pattern universale applicabile a qualsiasi dominio

**Entity Extraction:**
- `ExtractedEvent` record con campi tipizzati (Title, StartDate, Duration, etc.)
- AI restituisce JSON strutturato con confidence score

---

### MCP Server & Claude Integration (Phase 2-3)

**MCP Server (TypeScript):**
- Tool definitions: `calendar_list_events`, `calendar_create_event`, `calendar_find_free_slots`
- Usa `@modelcontextprotocol/sdk` con `StdioServerTransport`
- Handler per `ListToolsRequest` e `CallToolRequest`
- Config in `claude_desktop_config.json`

**Claude API Integration (.NET):**
- `ClaudeService` con Anthropic SDK
- `AnalyzeSchedule()` per reasoning complesso (context injection)
- `GetSmartAction()` con tool definitions → Claude sceglie e invoca tool
- Handle `StopReason == "tool_use"` → esegui tool → ritorna risultato

**Agentic Workflow:**
- `AgenticCalendarOrchestrator` combina Ollama (fast intent) + Claude (complex reasoning)
- Routing: confidence alta + intent semplice → esecuzione diretta
- Confidence bassa o query complessa → Claude con tool use
- Multi-step loop: Claude fa multiple tool calls, orchestrator esegue, fino a `end_turn`
- Max iterations per safety

---

### Genericita per Settimana

| Week | Focus | Genericita | Provider Lock-in |
|------|-------|------------|------------------|
| W1 | Ollama Basics (prompt eng, intent, JSON mode) | 100% | Zero |
| W2 | Integrations (Calendar API, multi-turn, Flutter) | 100% | Zero |
| W3 | Advanced Patterns (RAG, context mgmt, Redis cache) | 100% | Zero |
| W4 | Cloud Provider (streaming, cost tracking, abstraction) | 85% | Minimo (solo SDK) |
| W5 | Tool Systems (function calling, MCP, tool registry) | 70% | Medio (MCP specifico) |
| W6 | Orchestration + Guardrails + Fine-tuning Decision Framework | 90% | Basso |
| W7 | Provider-Agnostic Architecture (AI Router, multi-provider) | 95% | Quasi zero |
| W8 | Multi-Agent Systems (planner/executor, Agent SDK) | 90% | Basso |
| W9 | AI Evals + Testing + Production (eval pipeline, observability) | 100% | Zero |

**Media: ~92% skill generiche.** Migrare a OpenAI dopo il percorso: 2-3 giorni. Aggiungere Gemini: 2-3 giorni.

### Deliverables
- [ ] **Ollama Service** - Intent parsing & entity extraction
- [ ] **Claude API Integration** - Complex reasoning & planning
- [ ] **MCP Server** - Custom tools per Claude (TypeScript/Python)
- [ ] **Hybrid Architecture** - AI Router (Ollama + Claude)
- [ ] **Agentic Workflows** - Multi-step autonomous reasoning
- [ ] Google Calendar + Outlook integration
- [ ] RAG per context-aware responses
- [ ] Flutter app (iOS + Android) con chat interface
- [ ] 80%+ test coverage
- [ ] **Documentation:** C4, ADR, MCP Server docs, Prompt engineering guide

### Boss Battle
**"Autonomous Week Organizer"**: Claude ottimizza la settimana autonomamente via MCP tools.
**Reward: +500 XP**

---

## AI INTEGRATION IN ARCHITECT PROJECTS

> Dettagli completi in `roadmaps/architect-quest.md` per ogni progetto.

### P3 - BookingHub + AI (Mesi 13-18, allineato ad architect-quest.md)
- Patient-facing AI assistant (spostamenti, domande)
- Smart scheduling (pattern storici, durata visite, preferenze)
- Appointment reminders intelligenti (tono personalizzato)
- Natural language search per staff
- AI integration nelle ultime settimane del progetto AQ P3

### P4 - FamilyBudget + AI (Mesi 19-24, allineato ad architect-quest.md)
- Expense categorization automatica (Ollama, locale per privacy)
- Smart queries budget ("posso permettermi X?", Claude per reasoning)
- Budget optimization e pattern anomali
- Family conflict resolution (sync offline)
- AI features nelle ultime settimane del progetto AQ P4

---

## AI FRONTIER EXPLORATION LAB

> Lab separato dai progetti per esplorare nuove tech AI. Zero rischi per i deliverables.
> **Full Guide:** [[../../AI-Frontier/README.md]]

### Metodologia: 3 Phases

| Phase | Durata | Output |
|-------|--------|--------|
| **1. Quick Assessment** | 30-60 min | Deep Dive / Monitor / Skip |
| **2. Hands-On** | 2-4 ore | Experiment documentato con metriche |
| **3. Decision** | 15 min | ADOPT / MONITOR / SKIP |

### Cadenza

- **Ogni Quarter:** Review landscape, prioritize 2-3 tech, 1 weekend session, document
- **Ogni 6 mesi:** Review archived + adopted tech, update progetti se necessario

### 🔮 Exploration Backlog (Tier 3 — quando hai tempo/curiosita)

> Cose che vale la pena esplorare ma che NON bloccano il percorso.
> Perfette per sessioni AI Frontier da 2-4 ore.

| Tech | Perche esplorarlo | Quando ha senso |
|------|-------------------|-----------------|
| **Semantic Kernel (.NET)** | Orchestrazione AI nativa per il tuo stack. Confronta con le tue astrazioni: fa di piu? di meno? | Dopo P2.5 Phase 2 |
| **LangChain / LlamaIndex** | I due framework piu citati. Sapere cosa risolvono e dove sono overkill ti da conversazioni informate | Dopo P2.5 completato |
| **Vercel AI SDK** | Se esplori frontend AI-powered (chat UI, streaming). Leggero e pragmatico | Quando tocchi React |
| **Instructor / Pydantic AI** | Structured output enforcement. Potresti volerlo nel tuo AI Gateway | Quando il JSON mode di Ollama ti frustra |
| **Weights & Biases / MLflow** | Experiment tracking per AI. Overkill ora, utile se vai deep in AI/ML | Post-percorso |

### XP System

| Activity | XP |
|----------|-----|
| Quick assessment | +25 |
| Hands-on experiment | +75 |
| POC integration | +100 |
| Tech adopted in progetto | +200 |
| Tech diventa mainstream in 6 mesi | +300 |

### Resources

- **Newsletter:** The Batch (Andrew Ng), TLDR AI, Anthropic/OpenAI newsletters
- **Community:** r/LocalLLaMA, r/ClaudeAI, HackerNews AI
- **Podcasts:** Latent Space, Practical AI, The Cognitive Revolution

---

## 📚 Libri & Resources

### **Claude & MCP (CORE)** 🎯
1. **Anthropic Documentation** (MUST READ)
   - https://docs.anthropic.com/
   - Prompt engineering guide
   - Tool use (function calling)
   - Extended thinking mode
2. **MCP Documentation** (MUST READ)
   - https://modelcontextprotocol.io/
   - Quickstart & tutorials
   - Server implementation guides
   - Example servers (TypeScript, Python)
3. **Claude Cookbook** - Anthropic (free)
   - https://github.com/anthropics/anthropic-cookbook
   - Real-world examples
   - Best practices

### **Ollama & Local AI**
4. **Ollama Documentation** - https://ollama.ai/docs
5. **"Prompt Engineering Guide"** - DAIR.AI (free)
6. **"Building LLM Apps"** - OpenAI Cookbook (concepts trasferibili)

### **AI Engineering (General)**
7. **"Designing Data-Intensive Applications"** - Kleppmann (FONDAMENTALE)
8. **"AI Engineering"** - Chip Huyen (blog + book)
9. **"Generative AI with LangChain"** - Ben Auffarth (patterns riutilizzabili)

### **Papers (Opzionali ma Utili)**
- **"Constitutional AI"** - Anthropic (come Claude ragiona)
- **"ReAct: Synergizing Reasoning and Acting in LLMs"** (agentic workflows)
- **"Retrieval-Augmented Generation"** (RAG fundamentals)
- **"Extended Context Windows"** (managing 200K+ tokens)

### **Video & Talks**
- Anthropic YouTube Channel (Agent patterns, MCP intros)
- "Building with Claude" series
- MCP community examples

---

## 🎯 AI Skills Finali - Checklist

Alla fine del percorso AI (P2.5 + integrazioni in P3/P4):

### **Ollama (Local AI)**
- [ ] Ollama integration in .NET production apps
- [ ] Intent recognition & entity extraction
- [ ] JSON mode forcing & validation
- [ ] Prompt engineering per local models
- [ ] Performance optimization (latency, tokens)

### **Claude API**
- [ ] Anthropic SDK (.NET, TypeScript)
- [ ] Messages API (streaming, non-streaming)
- [ ] Advanced prompt engineering per Claude
- [ ] Tool use (function calling)
- [ ] Context window management (200K tokens)
- [ ] Cost optimization strategies

### **MCP (Model Context Protocol)** 🎯 **CORE**
- [ ] **MCP Server development** (TypeScript/Python)
- [ ] Tool definition & registration
- [ ] Custom tool implementation
- [ ] MCP protocol understanding
- [ ] Debugging & testing MCP servers
- [ ] Multi-tool orchestration

### **Agentic Workflows & Multi-Agent** 🆕
- [ ] Multi-step autonomous reasoning
- [ ] Tool chaining & orchestration
- [ ] Error recovery & fallbacks
- [ ] Agent planning & execution
- [ ] Human-in-the-loop patterns
- [ ] **Multi-agent orchestration** (planner + executor + reviewer)
- [ ] **Agent SDK** (Claude Agent SDK)
- [ ] **Agent communication patterns** (handoff, delegation)
- [ ] **When single vs multi-agent** (decision framework)

### **Guardrails & AI Safety** 🆕
- [ ] Prompt injection defense (input sanitization)
- [ ] Output validation (schema + content filter)
- [ ] PII detection & redaction
- [ ] Adversarial prompt testing
- [ ] Rate limiting per utente AI
- [ ] Graceful fallback su risposte non sicure

### **AI Evaluation & Observability** 🆕
- [ ] Eval pipeline automatizzata (input → output → score)
- [ ] Metriche AI: accuracy, hallucination rate, latency, cost/request
- [ ] A/B testing prompt
- [ ] Dashboard metriche AI (Langfuse o custom)
- [ ] Token usage tracking & cost alerts
- [ ] Quality regression detection

### **AI Testing** 🆕
- [ ] Testing output non-deterministici (range-based assertions)
- [ ] Snapshot testing per prompt (regression)
- [ ] Contract testing per tool use
- [ ] Eval-driven development (eval PRIMA del prompt)
- [ ] Mock vs real LLM testing strategy

### **Fine-tuning Decision Framework** 🆕
- [ ] Quando RAG vs fine-tuning vs prompt engineering (decision tree)
- [ ] Costo/beneficio fine-tuning (quando vale la pena?)
- [ ] Awareness: come funziona il fine-tuning (no hands-on richiesto)
- [ ] Data preparation per fine-tuning (formato, qualita, quantita)

### **Hybrid Architectures**
- [ ] AI Router design (when Ollama vs Claude)
- [ ] Cost optimization (95% local, 5% cloud)
- [ ] Performance benchmarking
- [ ] Graceful degradation
- [ ] Privacy-first design

### **RAG & Vector Search** (Tier 1 — costruisci in P2.5 W3)
- [ ] Vector DB setup (pgvector su PostgreSQL)
- [ ] Embedding model selection e benchmarking (locale vs API)
- [ ] Chunking strategies (sliding window, metadata preservation)
- [ ] Hybrid search (vector + keyword full-text + reranking)
- [ ] Query decomposition per query complesse
- [ ] RAG pipeline completa: query → embed → search → rerank → inject → LLM

### **Production & Deployment** (Tier 2 — costruisci in P2.5 W9)
- [ ] Context management & conversation history
- [ ] AI observability (logs, metrics, traces con dimensioni AI-specific)
- [ ] Rate limiting & quotas (per utente + per provider)
- [ ] AI deployment: Ollama containerizzato, healthcheck, model caching
- [ ] Scaling strategy: quando servono queue + workers
- [ ] Graceful degradation (provider fallback)
- [ ] Voice interface integration (optional)

### **Economic Understanding**
- [ ] Token cost analysis (per 1M tokens)
- [ ] ROI calculation (Ollama vs Cloud API)
- [ ] Scaling strategies
- [ ] Privacy compliance (GDPR, HIPAA)

---

## Economic Value

> Dettagli salary: vedi `career-strategy.md`

**AI Skills premium:** +20-35% su salary Senior. MCP Server development e hybrid Ollama+Claude sono skill rarissime (<1% dev).

**Portfolio pieces:** MCP Server su GitHub, hybrid architecture demo, agentic workflow funzionante, 3+ progetti con AI embedded.

---

*Ultimo aggiornamento: 2026-03-24 (v2.1 - Refactor: timeline allineate, +Vector DB/Embeddings/Advanced RAG in W3, +AI Deployment in W9, +Fine-tuning in W6, +Tier 3 exploration backlog)*
