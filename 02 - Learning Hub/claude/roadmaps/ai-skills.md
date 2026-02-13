# 🤖 Roadmap: AI Skills Track

> Percorso parallelo per diventare **Claude-Native & AI-Native Architect**

## 🎯 Obiettivo Finale

Essere capace di:
- **Creare MCP Servers** - Estendere Claude con tool e dati custom
- **Claude API mastery** - Integrazioni avanzate, prompt engineering, agentic workflows
- **Ollama locale** - AI embedded nelle app (privacy, offline, zero cost)
- **Hybrid architectures** - Orchestrare Ollama + Claude + MCP
- **Tool building** - Creare strumenti che Claude può usare
- **Prompt optimization** - Massimizzare reasoning di Claude

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

```
Mesi 5-6:   P2.5 - Claude-Native Calendar System
            ├─ Phase 1: Ollama Foundation (intent parsing)
            ├─ Phase 2: Claude API + MCP Server
            └─ Phase 3: Agentic Workflows (Claude orchestrates)

Mese 10-14: P3 - BookingHub + AI Integration
            ├─ MCP Server for booking data
            ├─ Claude-powered admin assistant
            └─ Hybrid Ollama + Claude architecture

Mese 15-18: P4 - FamilyBudget + AI Integration
            ├─ MCP Server for financial data
            ├─ Claude budget advisor (complex reasoning)
            └─ Ollama for categorization (fast, local)
```

**Approccio:** Impara progressivamente (Ollama → Claude → MCP → Agentic), poi applica in sistemi complessi.

---

## 🤖 PROGETTO 2.5: AI Gateway + Calendar System (Mesi 5-6) 🔧 SHARED SERVICE

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
| **2 (W4-6)** | Claude + Tools | 80% Generico | Concetti tool use universali |
| **3 (W7-8)** | Abstraction + Router | **95% Generico** | Pattern architetturale universale |

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

```csharp
// Interface universale per qualsiasi AI provider
public interface IAIProvider
{
    string Name { get; }
    Task<AIResponse> Chat(ChatRequest request);
    Task<AIResponse> ChatWithTools(ChatRequest request, List<Tool> tools);
    Task<Stream<AIResponse>> ChatStream(ChatRequest request);
    decimal GetCostPer1MTokens(TokenType type);
}

// Implementazioni specifiche
public class OllamaProvider : IAIProvider
{
    public string Name => "Ollama (Local)";
    public async Task<AIResponse> Chat(ChatRequest request) { /* ... */ }
    // Cost = $0 sempre
}

public class ClaudeProvider : IAIProvider
{
    public string Name => "Claude (Anthropic)";
    public async Task<AIResponse> Chat(ChatRequest request)
    {
        // Usa Anthropic SDK
        var response = await _anthropicClient.Messages.CreateAsync(/*...*/);
        return MapToAIResponse(response);
    }
}

public class OpenAIProvider : IAIProvider
{
    public string Name => "OpenAI";
    public async Task<AIResponse> Chat(ChatRequest request)
    {
        // Usa OpenAI SDK
        var response = await _openAIClient.Chat.CreateAsync(/*...*/);
        return MapToAIResponse(response);
    }
}

// AI Router - sceglie provider dinamicamente
public class AIRouter
{
    private readonly Dictionary<string, IAIProvider> _providers;

    public async Task<AIResponse> RouteRequest(ChatRequest request)
    {
        // Logica di routing (configurabile)
        if (request.RequiresComplexReasoning)
            return await _providers["claude"].Chat(request);

        if (request.RequiresFastResponse)
            return await _providers["ollama"].Chat(request);

        if (request.Budget == Budget.Low)
            return await _providers["ollama"].Chat(request);

        // Fallback chain
        try {
            return await _providers["claude"].Chat(request);
        } catch {
            return await _providers["openai"].Chat(request);
        }
    }
}
```

**Risultato:** Il resto del codice usa `IAIProvider`, non dipende da Claude specificamente.

### Tool System (Generic)

```csharp
// Definizione tool generica (funziona con Claude, OpenAI, etc.)
public record Tool
{
    public string Name { get; init; }
    public string Description { get; init; }
    public JsonSchema Parameters { get; init; }
}

// Executor generico
public interface IToolExecutor
{
    Task<string> Execute(string toolName, Dictionary<string, object> parameters);
}

// Registro tool universale
public class ToolRegistry
{
    private readonly Dictionary<string, IToolExecutor> _tools = new();

    public void Register(string name, IToolExecutor executor)
    {
        _tools[name] = executor;
    }

    public async Task<string> Execute(ToolCall toolCall)
    {
        if (_tools.TryGetValue(toolCall.Name, out var executor))
            return await executor.Execute(toolCall.Name, toolCall.Parameters);

        throw new ToolNotFoundException(toolCall.Name);
    }
}
```

**Questo funziona con:**
- ✅ Claude (via tool use API o MCP)
- ✅ OpenAI (via function calling)
- ✅ Gemini (via function calling)
- ✅ Ollama (via custom prompt engineering)

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

## 🔄 **ESEMPIO CONCRETO: Multi-Provider Support**

```csharp
// Configurazione
public class AIConfiguration
{
    public string DefaultProvider { get; set; } = "claude";
    public Dictionary<string, ProviderConfig> Providers { get; set; } = new()
    {
        ["claude"] = new() { ApiKey = "...", Model = "claude-sonnet-4-5" },
        ["openai"] = new() { ApiKey = "...", Model = "gpt-4-turbo" },
        ["ollama"] = new() { BaseUrl = "http://localhost:11434", Model = "llama3.1:8b" }
    };

    public RoutingStrategy Strategy { get; set; } = new()
    {
        FastQueries = "ollama",
        ComplexReasoning = "claude",
        Fallback = new[] { "claude", "openai", "ollama" }
    };
}

// Service layer (provider-agnostic!)
public class CalendarService
{
    private readonly IAIRouter _aiRouter;

    public async Task<string> HandleUserQuery(string query)
    {
        // Non sa quale provider verrà usato!
        var response = await _aiRouter.RouteRequest(new ChatRequest
        {
            Message = query,
            RequiresReasoning = IsComplexQuery(query),
            Tools = GetAvailableTools()
        });

        return response.Content;
    }
}

// Domani vuoi passare a OpenAI? Cambi config.DefaultProvider = "openai". FATTO.
```

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

**Week 3: Context & Polish**
- Conversation history (PostgreSQL)
- Context window management
- Multi-turn conversations
- Redis caching per risposte comuni
- Flutter app MVP (chat interface)

**Deliverable Phase 1:** Calendar assistant che usa solo Ollama ✅

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

**Week 6: Claude Reasoning**
- Complex queries via Claude:
  - "Quando sono libero per un caffè con Marco?"
  - "Suggerisci il miglior orario per un meeting importante"
  - "Analizza la mia settimana e dimmi dove posso ottimizzare"
- Multi-step reasoning
- Claude + MCP tools orchestration
- Comparison Ollama vs Claude (speed, accuracy, cost)

**Deliverable Phase 2:** MCP Server funzionante + Claude integration ✅

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

**Week 8: Autonomous Agent** 🚀
- **Claude come autonomous agent:**
  - User: "Organizza la mia settimana"
  - Claude:
    1. Reads all events via MCP
    2. Analyzes patterns & conflicts
    3. Proposes optimizations
    4. Executes changes (with confirmation)
- Multi-step workflows
- Error recovery & fallbacks
- Production polish:
  - Observability (Logs, metrics, traces)
  - Rate limiting
  - Graceful degradation
  - Voice interface Flutter (speech_to_text, opzionale)

**Deliverable Phase 3:** Autonomous AI agent production-ready ✅

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

### Technical Highlights

#### Ollama Function Calling
```csharp
public class OllamaService
{
    private const string SYSTEM_PROMPT = """
        You are a calendar assistant. Parse requests and return JSON.

        Available functions:
        - create_event: Create new calendar event
        - list_events: Query events by date range
        - update_event: Modify existing event
        - delete_event: Remove event
        - find_free_slots: Find available time slots

        Response format:
        {
          "function": "create_event",
          "params": { ... },
          "confidence": 0.95,
          "clarification_needed": false
        }
        """;

    public async Task<AIResponse> ParseIntent(
        string userMessage,
        List<Message> conversationHistory
    )
    {
        var messages = new List<object> {
            new { role = "system", content = SYSTEM_PROMPT }
        };

        // Add conversation history for context
        messages.AddRange(conversationHistory.Select(m =>
            new { role = m.Role, content = m.Content }
        ));

        messages.Add(new { role = "user", content = userMessage });

        var response = await _httpClient.PostAsJsonAsync("/api/chat", new {
            model = "llama3.1:8b",
            messages = messages,
            format = "json",
            temperature = 0.3, // Low for consistent parsing
            stream = false
        });

        return await response.Content
            .ReadFromJsonAsync<AIResponse>();
    }
}
```

#### RAG Pattern
```csharp
public class CalendarRAGService
{
    // Quando user chiede "quando sono libero questa settimana"
    public async Task<string> GetRelevantContext(string query)
    {
        // 1. Fetch eventi rilevanti dal DB
        var events = await _db.Events
            .Where(e => e.StartTime >= DateTime.Now
                     && e.StartTime <= DateTime.Now.AddDays(7))
            .ToListAsync();

        // 2. Converti in contesto testuale per l'AI
        var context = $"""
            Current events this week:
            {string.Join("\n", events.Select(e =>
                $"- {e.StartTime:ddd MMM dd HH:mm}: {e.Title} ({e.Duration}min)"))}

            User's typical schedule:
            - Prefers meetings after 10 AM
            - Lunch usually 13:00-14:00
            - Avoids Friday afternoons when possible
            """;

        return context;
    }

    public async Task<AIResponse> QueryWithContext(string userQuery)
    {
        var context = await GetRelevantContext(userQuery);

        var prompt = $"""
            Context:
            {context}

            User query: {userQuery}

            Analyze the schedule and respond naturally.
            """;

        return await _ollama.Chat(prompt);
    }
}
```

#### Entity Extraction
```csharp
public record ExtractedEvent
{
    public string? Title { get; init; }
    public DateTime? StartDate { get; init; }
    public TimeSpan? StartTime { get; init; }
    public int? DurationMinutes { get; init; }
    public string? Calendar { get; init; }
    public List<string>? Attendees { get; init; }
    public bool NeedsReminder { get; init; }
}

// AI Output Example:
{
  "function": "create_event",
  "params": {
    "title": "Dentista",
    "start_date": "2026-02-11",
    "start_time": "15:00",
    "duration_minutes": 60,
    "calendar": "personal",
    "needs_reminder": true,
    "reminder_minutes_before": 60
  },
  "confidence": 0.96
}
```

---

### 🔧 MCP Server & Claude Integration (Phase 2-3)

#### MCP Server Implementation (TypeScript)

**File: `mcp-calendar-server/src/index.ts`**

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { GoogleCalendarAPI } from "./calendar-api.js";

const server = new Server(
  {
    name: "calendar-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

const calendarAPI = new GoogleCalendarAPI();

// Register tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "calendar_list_events",
        description: "List calendar events in a date range",
        inputSchema: {
          type: "object",
          properties: {
            start_date: {
              type: "string",
              description: "Start date (YYYY-MM-DD)",
            },
            end_date: {
              type: "string",
              description: "End date (YYYY-MM-DD)",
            },
            calendar_id: {
              type: "string",
              description: "Calendar ID (optional, defaults to primary)",
            },
          },
          required: ["start_date", "end_date"],
        },
      },
      {
        name: "calendar_create_event",
        description: "Create a new calendar event",
        inputSchema: {
          type: "object",
          properties: {
            title: { type: "string" },
            date: { type: "string", description: "Date (YYYY-MM-DD)" },
            time: { type: "string", description: "Time (HH:mm)" },
            duration_minutes: { type: "number" },
            description: { type: "string" },
          },
          required: ["title", "date", "time"],
        },
      },
      {
        name: "calendar_find_free_slots",
        description: "Find available time slots in calendar",
        inputSchema: {
          type: "object",
          properties: {
            date: { type: "string" },
            min_duration_minutes: { type: "number" },
            prefer_morning: { type: "boolean" },
          },
          required: ["date", "min_duration_minutes"],
        },
      },
    ],
  };
});

// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "calendar_list_events": {
      const events = await calendarAPI.listEvents(
        args.start_date,
        args.end_date,
        args.calendar_id
      );
      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(events, null, 2),
          },
        ],
      };
    }

    case "calendar_create_event": {
      const event = await calendarAPI.createEvent({
        title: args.title,
        date: args.date,
        time: args.time,
        duration: args.duration_minutes || 60,
        description: args.description,
      });
      return {
        content: [
          {
            type: "text",
            text: `Event created: ${event.id}`,
          },
        ],
      };
    }

    case "calendar_find_free_slots": {
      const slots = await calendarAPI.findFreeSlots(
        args.date,
        args.min_duration_minutes,
        args.prefer_morning
      );
      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(slots, null, 2),
          },
        ],
      };
    }

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

**Configuration: `claude_desktop_config.json`**

```json
{
  "mcpServers": {
    "calendar": {
      "command": "node",
      "args": ["/path/to/mcp-calendar-server/dist/index.js"]
    }
  }
}
```

---

#### Claude API Integration (.NET)

**File: `CalendarAssistant.Infrastructure/ClaudeService.cs`**

```csharp
using Anthropic.SDK;
using Anthropic.SDK.Messaging;

public class ClaudeService
{
    private readonly AnthropicClient _client;
    private readonly ILogger<ClaudeService> _logger;

    public ClaudeService(IConfiguration config, ILogger<ClaudeService> logger)
    {
        var apiKey = config["Anthropic:ApiKey"];
        _client = new AnthropicClient(apiKey);
        _logger = logger;
    }

    public async Task<string> AnalyzeSchedule(
        string userQuery,
        List<CalendarEvent> events
    )
    {
        var context = BuildScheduleContext(events);

        var messages = new List<Message>
        {
            new Message
            {
                Role = "user",
                Content = $"""
                    Context: {context}

                    User query: {userQuery}

                    Analyze the schedule and provide insights.
                    Consider: workload balance, gaps, optimization opportunities.
                    """
            }
        };

        var response = await _client.Messages.CreateAsync(new MessageRequest
        {
            Model = "claude-sonnet-4-5-20250929",
            MaxTokens = 4096,
            Messages = messages,
            Temperature = 0.3m
        });

        return response.Content[0].Text;
    }

    public async Task<CalendarAction> GetSmartAction(
        string userRequest,
        List<CalendarEvent> context
    )
    {
        // Define tools Claude can use
        var tools = new List<Tool>
        {
            new Tool
            {
                Name = "create_event",
                Description = "Create a new calendar event",
                InputSchema = new
                {
                    type = "object",
                    properties = new
                    {
                        title = new { type = "string" },
                        date = new { type = "string" },
                        time = new { type = "string" },
                        duration_minutes = new { type = "number" }
                    },
                    required = new[] { "title", "date", "time" }
                }
            },
            new Tool
            {
                Name = "find_free_slot",
                Description = "Find best available time slot",
                InputSchema = new
                {
                    type = "object",
                    properties = new
                    {
                        date = new { type = "string" },
                        min_duration = new { type = "number" },
                        prefer_time = new { type = "string", @enum = new[] { "morning", "afternoon", "evening" } }
                    },
                    required = new[] { "date", "min_duration" }
                }
            }
        };

        var messages = new List<Message>
        {
            new Message
            {
                Role = "user",
                Content = $"""
                    Current schedule: {JsonSerializer.Serialize(context)}

                    User request: {userRequest}

                    Use available tools to accomplish this request.
                    Think step by step and use tools as needed.
                    """
            }
        };

        var response = await _client.Messages.CreateAsync(new MessageRequest
        {
            Model = "claude-sonnet-4-5-20250929",
            MaxTokens = 4096,
            Messages = messages,
            Tools = tools,
            Temperature = 0.2m
        });

        // Handle tool use
        if (response.StopReason == "tool_use")
        {
            var toolUse = response.Content
                .OfType<ToolUseContent>()
                .FirstOrDefault();

            if (toolUse != null)
            {
                _logger.LogInformation(
                    "Claude wants to use tool: {Tool} with params: {Params}",
                    toolUse.Name,
                    JsonSerializer.Serialize(toolUse.Input)
                );

                return new CalendarAction
                {
                    Type = toolUse.Name,
                    Parameters = toolUse.Input,
                    Reasoning = response.Content
                        .OfType<TextContent>()
                        .FirstOrDefault()?.Text
                };
            }
        }

        throw new InvalidOperationException("Claude did not return a tool use");
    }
}

public record CalendarAction
{
    public string Type { get; init; }
    public Dictionary<string, object> Parameters { get; init; }
    public string? Reasoning { get; init; }
}
```

---

#### Agentic Workflow Example

**File: `CalendarAssistant.Application/AgenticOrchestrator.cs`**

```csharp
public class AgenticCalendarOrchestrator
{
    private readonly ClaudeService _claude;
    private readonly OllamaService _ollama;
    private readonly GoogleCalendarAPI _calendar;
    private readonly ILogger<AgenticCalendarOrchestrator> _logger;

    public async Task<string> HandleComplexRequest(string userMessage)
    {
        // Step 1: Fast intent recognition con Ollama
        var intent = await _ollama.ParseIntent(userMessage);

        _logger.LogInformation("Intent detected: {Intent}", intent.Function);

        // Step 2: Decide routing
        if (intent.Confidence > 0.9 && intent.Function == "create_event")
        {
            // Simple case: direct execution
            var evt = await _calendar.CreateEvent(intent.Parameters);
            return $"✅ Event created: {evt.Title} on {evt.Date}";
        }

        // Step 3: Complex case: delegate to Claude
        _logger.LogInformation("Complex request, delegating to Claude");

        var events = await _calendar.ListEvents(
            DateTime.Now,
            DateTime.Now.AddDays(14)
        );

        var action = await _claude.GetSmartAction(userMessage, events);

        // Step 4: Execute Claude's decision
        return action.Type switch
        {
            "create_event" => await ExecuteCreate(action.Parameters),
            "find_free_slot" => await ExecuteFindSlot(action.Parameters),
            "optimize_schedule" => await ExecuteOptimize(action.Parameters),
            _ => throw new NotSupportedException($"Action not supported: {action.Type}")
        };
    }

    // Example: Multi-step agentic workflow
    public async Task<string> OptimizeWeek()
    {
        _logger.LogInformation("Starting autonomous week optimization");

        // Claude works as an agent with multiple steps
        var messages = new List<Message>
        {
            new Message
            {
                Role = "user",
                Content = """
                    Analyze my calendar for this week and optimize it.

                    Steps:
                    1. Use calendar_list_events to fetch all events
                    2. Identify issues: back-to-back meetings, no lunch breaks, etc.
                    3. Use find_free_slot to find better times
                    4. Propose specific changes

                    Work autonomously through these steps.
                    """
            }
        };

        // Claude will make multiple tool calls
        var conversationMessages = new List<Message>(messages);
        int maxIterations = 5;
        int iteration = 0;

        while (iteration < maxIterations)
        {
            iteration++;

            var response = await _claude.Messages.CreateAsync(new MessageRequest
            {
                Model = "claude-sonnet-4-5-20250929",
                MaxTokens = 4096,
                Messages = conversationMessages,
                Tools = GetAvailableTools()
            });

            if (response.StopReason == "end_turn")
            {
                // Claude finished reasoning
                var finalText = response.Content
                    .OfType<TextContent>()
                    .FirstOrDefault()?.Text;

                return finalText ?? "Optimization complete";
            }

            if (response.StopReason == "tool_use")
            {
                // Execute tool and continue conversation
                var toolResults = await ExecuteTools(response.Content);

                conversationMessages.Add(new Message
                {
                    Role = "assistant",
                    Content = response.Content
                });

                conversationMessages.Add(new Message
                {
                    Role = "user",
                    Content = toolResults
                });
            }
        }

        return "Optimization reached max iterations";
    }
}
```

---

### 📅 **Learning Path Dettagliato: Generico → Specifico**

Ogni settimana indica esplicitamente cosa è **universale** vs **specifico**.

---

## **MESE 5: FOUNDATIONS (100% → 80% Generic)**

### **W1: Universal Foundations** | 🟢 **100% GENERICO**

**Tutti questi concetti funzionano con QUALSIASI LLM:**

- ✅ Ollama .NET integration → Pattern: HTTP client + JSON (universale)
- ✅ System prompt engineering → Identico per GPT/Claude/Gemini
- ✅ Intent recognition → Concetto universale (parsing user intent)
- ✅ Entity extraction → Pattern universale (NER con LLM)
- ✅ JSON mode forcing → Supportato da tutti i LLM moderni
- ✅ Confidence scoring → Pattern universale

**💡 Perché Ollama?** È il "lab gratuito" per imparare senza spendere. I concetti sono identici con altri LLM.

**Deliverable:** Intent parser che funziona con Ollama → Riutilizzabile al 100% con altri provider

---

### **W2: Integration Patterns** | 🟢 **100% GENERICO**

- ✅ External API integration (Google Calendar OAuth2) → Pattern universale
- ✅ CRUD operations → Logica business, non AI-specific
- ✅ Natural language date parsing → Tecnica universale
- ✅ Conversation history management → Pattern universale
- ✅ Multi-turn conversations → Concetto universale
- ✅ Frontend integration (Flutter mobile) → Non dipende da AI provider

**Deliverable:** Calendar integration → Zero dipendenza da provider AI specifico

---

### **W3: Advanced Patterns** | 🟢 **100% GENERICO**

- ✅ Context window management → Problema universale (tutti i LLM hanno limiti)
- ✅ RAG pattern → Retrieval-Augmented Generation (universale)
- ✅ Smart suggestions → Logica applicabile a qualsiasi LLM
- ✅ Redis caching → Infrastructure pattern (universale)
- ✅ Temperature/token optimization → Concetti universali

**Checkpoint:** ✅ Sistema funzionante con Ollama
**Transferability:** Puoi passare a GPT-4 in 2 ore cambiando solo l'endpoint HTTP

---

### **W4: Cloud AI Provider** | 🟡 **85% GENERICO**

**Concetti universali:**
- ✅ Cloud API integration patterns → Stesso per OpenAI/Claude/Gemini
- ✅ Streaming responses (SSE) → Standard web
- ✅ Cost tracking & optimization → Logica universale
- ✅ Provider abstraction layer → Design pattern universale

**Claude-specific (MA concetti trasferibili):**
- ⚡ Anthropic SDK syntax → 15% specifico (OpenAI SDK è simile)
- ⚡ Claude Messages API → Equivalente a OpenAI Chat Completions
- ⚡ Tool use format → Standard tra provider (leggere differenze sintattiche)

**💡 Cosa impari:** Come integrare un cloud AI provider. Passare da Claude ad OpenAI richiede ~2 giorni (solo SDK diverso).

**Deliverable:** `IAIProvider` abstraction + ClaudeProvider implementation

---

## **MESE 6: SPECIALIZATION + ABSTRACTION (70% → 95% Generic)**

### **W5: Tool Systems** | 🟡 **70% GENERICO**

**Concetti universali (70%):**
- ✅ Tool/Function calling paradigm → Standard OpenAI/Anthropic/Google
- ✅ Tool definition (JSON Schema) → Universale
- ✅ Tool executor pattern → Design pattern universale
- ✅ Tool registry → Pattern architetturale universale

**Claude-specific (30%):**
- ⚡ MCP Protocol → Claude-native, MA...
  - Concetto di "tool server" è universale
  - Puoi creare adapter OpenAI → MCP
  - Altri provider aggiungeranno simili

**💡 Strategy:** Impari MCP (vantaggio Claude), MA progetti tool system generico riutilizzabile

**Deliverable:**
- MCP Server (Claude-native) ✅
- Generic `IToolExecutor` interface (riusabile con OpenAI) ✅

---

### **W6: Tool Orchestration** | 🟢 **90% GENERICO**

**Quasi tutto è universale:**
- ✅ Multi-step reasoning → Concetto universale (tutti i LLM lo supportano)
- ✅ Tool chaining → Pattern universale
- ✅ Error handling & fallbacks → Engineering best practices (universali)
- ✅ Autonomous tool selection → Tutti i LLM moderni lo fanno

**Specifico (10%):**
- ⚡ MCP integration specifics → Ma logica riutilizzabile

**Deliverable:** Orchestrator che funziona con qualsiasi provider che supporta tool calling

---

### **W7: Provider-Agnostic Architecture** | 🟢 **95% GENERICO** ⭐

**CORE ARCHITECTURE WEEK - Tutto riutilizzabile:**

- ✅ **AI Router pattern** → Design pattern universale
  - Input: request characteristics
  - Output: best provider for the job
  - Works with ANY provider
- ✅ **Provider abstraction** → Interface-based design (universale)
- ✅ **Multi-provider fallback** → Resilience pattern (universale)
- ✅ **Cost optimization logic** → Business logic (universale)
- ✅ **Performance benchmarking** → Methodology (universale)

**Specifico (5%):**
- ⚡ Claude/OpenAI/Ollama configurations → Solo config, non logica

**💡 Risultato:** Sistema che supporta 3+ provider simultanei. Aggiungere nuovo provider = 1 giorno di lavoro.

**Deliverable:** Production-ready multi-provider system

---

### **W8: Production Patterns** | 🟢 **100% GENERICO**

**Engineering best practices (universali):**

- ✅ Observability (logs, metrics, traces) → Standard engineering
- ✅ Rate limiting & quotas → Infrastructure pattern
- ✅ Graceful degradation → Resilience pattern
- ✅ Error recovery strategies → Software engineering fundamentals
- ✅ Documentation (C4, ADR) → Universal practices
- ✅ Voice interface → Flutter speech_to_text (cross-platform)

**Zero dipendenze specifiche da provider.**

**Checkpoint:** ✅ Production-ready, provider-agnostic AI system

---

## 📊 **SUMMARY: Genericità per Settimana**

| Week | Focus | Genericità | Provider Lock-in |
|------|-------|------------|------------------|
| W1 | Ollama Basics | 🟢 100% | Zero |
| W2 | Integrations | 🟢 100% | Zero |
| W3 | Advanced Patterns | 🟢 100% | Zero |
| W4 | Cloud Provider | 🟡 85% | Minimo (solo SDK) |
| W5 | Tool Systems | 🟡 70% | Medio (MCP specifico) |
| W6 | Orchestration | 🟢 90% | Basso |
| W7 | Abstraction | 🟢 95% | Quasi zero |
| W8 | Production | 🟢 100% | Zero |

**Media ponderata: ~90% skill generiche**, 10% Claude-specific (che comunque insegna concetti trasferibili)

---

## ✅ **GARANZIA DI TRASFERIBILITÀ**

Dopo questo percorso, in **1 settimana** puoi:

- ✅ Migrare completamente a OpenAI (2-3 giorni)
- ✅ Aggiungere Gemini come 3° provider (2-3 giorni)
- ✅ Supportare Cohere, Mistral, o qualsiasi futuro LLM (3-4 giorni)
- ✅ Creare custom adapter per LLM proprietario aziendale (5-7 giorni)

**Non sei locked-in su Claude. Hai skill architetturali universali + specializzazione Claude come bonus.**

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
**"Autonomous Week Organizer"**: Chiedi a Claude di "ottimizzare la mia settimana". Claude deve autonomamente:
1. Leggere tutti gli eventi via MCP
2. Identificare problemi (conflitti, no breaks, etc.)
3. Proporre e implementare ottimizzazioni
4. Zero errori, 100% autonomous

**Reward: +500 XP**

---

## 🏛️ AI INTEGRATION IN ARCHITECT PROJECTS

### P3 - BookingHub + AI (Mesi 10-14)

**AI Features da Aggiungere:**

#### 1. Patient-Facing AI Assistant
```
Patient: "Vorrei spostare l'appuntamento di giovedì"
AI: "Vedo che hai un appuntamento giovedì 13 alle 15:00.
     Quando preferiresti spostarlo?"
Patient: "Venerdì alla stessa ora"
AI: "Venerdì 14 alle 15:00 è disponibile. Confermo lo spostamento?"
```

#### 2. Smart Scheduling
- AI suggerisce slot ottimali basati su:
  - Pattern storici del professionista
  - Durata media visite per tipo
  - Travel time tra appuntamenti
  - Preferenze paziente

#### 3. Appointment Reminders Intelligenti
- AI personalizza il messaggio:
  - Tono formale vs casual basato su relazione
  - Include info rilevanti (cosa portare, come prepararsi)
  - Suggerisce spostamento se vede conflitti nel calendario paziente

#### 4. Natural Language Search
```
Staff: "Mostrami tutti i pazienti che hanno cancellato negli ultimi 3 mesi"
Staff: "Chi non si è più fatto vivo da settembre?"
Staff: "Slot liberi domani mattina"
```

**Nuove Settimane (in P3):**
- W17: AI Assistant MVP integration
- W18: Smart scheduling algorithm
- W19-20: Production + Boss Battle (come pianificato)

---

### P4 - FamilyBudget + AI (Mesi 15-18)

**AI Features da Aggiungere:**

#### 1. Expense Categorization
```
User: "Ho speso 45€ per pizza e birra ieri sera"
AI: "Registrato:
     💰 45€
     🍕 Categoria: Ristoranti
     📅 Data: 01/02/2026

     Budget 'Ristoranti' mensile: 180€ / 300€ (60%)"
```

#### 2. Smart Queries
```
User: "Quanto stiamo spendendo in cibo?"
AI: "Febbraio 2026 (primi 2 giorni):
     🛒 Supermercato: 45€
     🍕 Ristoranti: 85€
     ☕ Caffè/snack: 12€

     Totale: 142€
     Trend: +15% vs gennaio"

User: "Posso permettermi un MacBook da 2000€?"
AI: "Analizzando il budget:
     💰 Risparmio attuale: 3400€
     📊 Risparmio medio mensile: 450€

     ✅ Sì, ma:
     - Ti resterebbero 1400€ (emergency fund ok)
     - Ricostruiresti il buffer in ~4 mesi
     - Alternative: rateizzazione, aspettare sconti"
```

#### 3. Budget Optimization AI
- Analizza spese e suggerisce ottimizzazioni
- Identifica spese duplicate/inutili
- Trova pattern anomali
- Suggerisce limiti realistici per categoria

#### 4. Family Conflict Resolution
```
// 2 membri famiglia offline modificano stesso budget
AI: "Rilevati conflitti:
     - Marco: aggiunto spesa 30€ 'Farmacia'
     - Sara: aggiunto spesa 25€ 'Farmacia'

     Probabilmente è la stessa spesa?
     Suggerisco: unire in 30€ (valore maggiore)"
```

**Nuove Settimane (in P4):**
- W17: AI expense categorization
- W18: AI budget advisor + conflict resolution
- Poi production come pianificato

---

## 🔬 **AI FRONTIER EXPLORATION LAB**

> **"L'AI evolve rapidamente. Questo lab ti tiene aggiornato senza bloccare i progetti principali."**

### 🎯 Perché Serve

**Reality Check:**
- Nuovi modelli ogni 3-6 mesi (GPT-5, Claude Opus 5, Gemini 3, etc.)
- Nuove tecniche emergono (reasoning models, agentic frameworks, nuovi pattern)
- Costi che cambiano (modelli più economici con stessa qualità)
- Protocolli che evolvono (MCP competitors, nuovi standard)

**Rischio senza exploration:**
- ❌ Rimani indietro con tech obsolete
- ❌ Paghi troppo (esistono alternative più economiche)
- ❌ Perdi opportunità competitive (early adoption)

**Soluzione:** Lab separato dai progetti principali = zero rischi, massimo learning.

---

### 📁 Struttura

```
AI-Frontier/
├── README.md           ← Metodologia completa
├── 2026/
│   ├── Q1/            ← Esperimenti Q1 (o3-mini, Gemini 2.0, etc.)
│   │   ├── exploration-queue.md
│   │   └── [tech-name]/
│   ├── Q2/
│   └── Q3-Q4/
├── Templates/
│   └── experiment-template.md  ← Template standard
└── Archive/            ← Tech deprecate/superate
```

**Location:** `AI-Frontier/` (root del Learning Hub)
**Full Guide:** [[../../AI-Frontier/README.md]]

---

### 🧪 Metodologia: 3 Phases

#### **Phase 1: Quick Assessment** (30-60 min)

Domande chiave:
- [ ] Cos'è? Cosa promette di fare meglio?
- [ ] Maturity? (Experimental vs Production-ready)
- [ ] Costi? (Free vs paid, pricing model)
- [ ] Chi supporta? (Big tech, startup, community size)
- [ ] Integration? (Drop-in replacement o rewrite?)

**Output:** ✅ Deep Dive | 👀 Monitor | ❌ Skip

---

#### **Phase 2: Hands-On** (2-4 ore, solo se Deep Dive)

1. **Setup** (30 min) - Install, hello world, docs quality
2. **Comparison** (1-2 ore) - Test vs tech attuale
   - Metrics: speed, accuracy, cost, developer experience
3. **Integration POC** (1-2 ore) - Quanto è facile integrare nei progetti?

**Output:** Experiment documentato con metriche concrete

---

#### **Phase 3: Decision** (15 min)

| Decision | Action |
|----------|--------|
| **✅ ADOPT** | Schedule integration in progetti |
| **👀 MONITOR** | Revisit in 3-6 mesi |
| **❌ SKIP** | Archive + document perché |

---

### 🎯 Q1 2026 - Cosa Esplorare

**High Priority:**

1. **OpenAI o3-mini** (reasoning economico)
   - Use case: Complex reasoning in P3/P4 → Ridurre costi Claude

2. **Gemini 2.0 Flash (Thinking)** (gratis!)
   - Use case: Multi-step reasoning → Extended thinking gratis

3. **LangGraph vs Custom**
   - Use case: Agentic orchestration P2.5 → Framework o custom?

**Medium Priority:**

4. **Semantic Kernel 2.0** (.NET native orchestration)
5. **Ollama Function Calling** (improvements → più reliable?)
6. **MCP Community Servers** (reusable pre-built servers)

**Experimental:**

7. **Claude Artifacts API** (if released)
8. **Local Reasoning** (DeepSeek-R1, Qwen2.5-Coder)
9. **AutoGen Studio 2.0** (multi-agent systems)

**Full list:** [[../../AI-Frontier/2026/Q1/exploration-queue.md|Q1 Exploration Queue]]

---

### 📅 Cadenza

**Ogni Quarter (3 mesi):**
- [ ] Review AI landscape (cosa è nuovo?)
- [ ] Prioritize 2-3 tech da esplorare
- [ ] Schedule 1 weekend session (4-6 ore)
- [ ] Document findings & decisions

**Ogni 6 mesi:**
- [ ] Review archived tech (qualcosa è maturato?)
- [ ] Review adopted tech (ancora il best choice?)
- [ ] Update progetti se necessario

---

### 🎮 XP System

| Activity | XP |
|----------|-----|
| Quick assessment completato | +25 |
| Hands-on experiment completato | +75 |
| Decision documentata | +25 |
| POC integration funzionante | +100 |
| Tech adopted in progetto principale | +200 |
| **BONUS:** Tech esplorata diventa mainstream in 6 mesi | +300 |

**Achievements Speciali:**
- 🔮 **Early Adopter** - Adopt 3+ mesi prima che diventi mainstream (+500 XP)
- 🧠 **Trend Spotter** - 3+ correct "Monitor → Adopt" predictions (+300 XP)
- ⚡ **Fast Learner** - 5+ tech esplorate in un quarter (+250 XP)

---

### ✅ Benefici

**Perché funziona:**
- ✅ **Stay current** - Skill sempre aggiornate
- ✅ **Reduce risk** - Test before commit nei progetti principali
- ✅ **Optimize costs** - Scopri alternative economiche early
- ✅ **Competitive edge** - Early adoption di tech vincenti
- ✅ **Learn faster** - Structured methodology vs random exploration

**Separato dai progetti = zero rischi per i deliverables critici.**

---

### 📰 Resources per Stare Aggiornato

**Newsletter (15 min/settimana):**
- The Batch (Andrew Ng) - AI news digest
- TLDR AI - Daily condensed
- Anthropic/OpenAI newsletters - Official updates

**Community (30 min/settimana):**
- r/LocalLLaMA - Open-source models
- r/ClaudeAI - Claude community
- HackerNews (AI tag) - Curated discussions
- Twitter/X: @AnthropicAI, @OpenAI, key researchers

**Podcasts (Commute/gym):**
- Latent Space Podcast
- Practical AI
- The Cognitive Revolution

---

### 💡 Example: Valutazione Reale

**Scenario:** Gemini 2.0 Flash esce con "thinking mode" gratis.

**Phase 1 (45 min):**
- ✅ Promette: Extended thinking simile a Claude, ma gratis
- ✅ Maturity: Production (Google backing)
- ✅ Cost: $0 (gratis)
- ✅ Decision: **Deep Dive**

**Phase 2 (3 ore):**
- Test: "Ottimizza la mia settimana" (calendario complesso)
- Claude: ottimo, ma $0.015 per richiesta
- Gemini: buono (85% quality), $0
- **POC:** Integra in IAIProvider → funziona
- **Decision: ✅ ADOPT per query non critiche**

**Phase 3:**
- Action: Update AI Router
  - Critical reasoning → Claude (quality)
  - Standard reasoning → Gemini (cost)
- **Risparmio:** 70% costi reasoning queries

**Questo è il valore dell'exploration lab.** 🚀

---

**Full Documentation:** [[../../AI-Frontier/README.md|AI Frontier Lab Guide]]

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

### **Agentic Workflows**
- [ ] Multi-step autonomous reasoning
- [ ] Tool chaining & orchestration
- [ ] Error recovery & fallbacks
- [ ] Agent planning & execution
- [ ] Human-in-the-loop patterns

### **Hybrid Architectures**
- [ ] AI Router design (when Ollama vs Claude)
- [ ] Cost optimization (95% local, 5% cloud)
- [ ] Performance benchmarking
- [ ] Graceful degradation
- [ ] Privacy-first design

### **Production Skills**
- [ ] RAG (Retrieval-Augmented Generation)
- [ ] Context management & conversation history
- [ ] AI observability (logs, metrics, traces)
- [ ] Rate limiting & quotas
- [ ] AI testing strategies
- [ ] Voice interface integration (optional)

### **Economic Understanding**
- [ ] Token cost analysis (per 1M tokens)
- [ ] ROI calculation (Ollama vs Cloud API)
- [ ] Scaling strategies
- [ ] Privacy compliance (GDPR, HIPAA)

---

## 💰 Economic Value - Perché Queste Skill Pagano

### **Claude-Native Development = RARISSIMO** 🚀

**Market Reality (Feb 2026):**
- 🔴 Migliaia di dev sanno usare OpenAI API
- 🟡 Centinaia sanno usare Claude API base
- 🟢 **Pochissimi (<1%) sanno creare MCP Servers**
- 💎 **Quasi nessuno sa hybrid Ollama + Claude + MCP**

### **Salary Impact**

| Skill Level | Base Salary | Con AI Skills | Premium |
|-------------|-------------|---------------|---------|
| Mid-level | €50-70k | €60-80k | +15-20% |
| Senior | €70-90k | €90-110k | +20-25% |
| **Senior + Claude-Native** | €90-110k | **€110-140k** | **+25-35%** |

### **Cosa Cercano le Aziende**

**🔥 TOP DEMAND (2026):**
1. **MCP Server developers** - Extend AI with custom tools
2. **Agentic workflow architects** - Multi-step AI systems
3. **Hybrid AI engineers** - Local + cloud optimization
4. **Privacy-first AI** - GDPR-compliant AI systems

**Real Job Examples:**
```
"Senior AI Engineer - MCP Development"
€120-140k remote | Series B startup
"Build MCP servers to extend Claude with company data"

"Staff Engineer - Agentic AI Systems"
€130-160k remote | Enterprise
"Design autonomous AI workflows with Claude + custom tools"

"AI Architect - Privacy-First Systems"
€110-135k remote | Healthcare/Finance
"Hybrid local/cloud AI, GDPR-compliant, offline-capable"
```

### **Why This Pays**

✅ **Riduce costi:** Ollama = $0, Claude = $3/1M tokens (vs GPT-4 $10)
✅ **Privacy:** Critical per healthcare, finance, legal
✅ **Offline:** Edge computing, mobile apps
✅ **Customizzazione:** MCP = infinite estensioni
✅ **Future-proof:** Agentic AI è il futuro

**ROI Example:**
- 1M API calls/mese
- OpenAI: $10k/mese
- Claude: $3k/mese
- **Ollama (95%) + Claude (5%): ~$150/mese** 💰

Risparmi: **$9,850/mese = $118k/anno**

**Un developer che sa fare questo vale MOLTO.**

---

### **Portfolio Pieces che Impressionano**

Con questo percorso, avrai:

1. **MCP Server pubblico su GitHub** - "Wow, sa estendere Claude!"
2. **Hybrid architecture demo** - "Capisce cost optimization!"
3. **Agentic workflow example** - "Claude autonomous agent funzionante!"
4. **3 progetti real-world** con AI embedded

**Questo portfolio da solo apre porte a:**
- Startups AI-first (equity + salary alto)
- Big Tech (Google, Microsoft, Anthropic)
- Consulting (@$200-300/ora)
- Prodotti propri (SaaS AI-powered)

---

*Ultimo aggiornamento: 2026-02-11*
