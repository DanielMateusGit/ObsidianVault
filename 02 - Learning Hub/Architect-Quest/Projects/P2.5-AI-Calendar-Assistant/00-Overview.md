---
tags: [architect-quest, project, p2.5, ai]
status: not-started
---

# 🤖 Progetto 2.5: AI-Native Calendar System

## 📋 Overview
Sistema calendario intelligente **provider-agnostic** che combina AI locale (Ollama) + AI cloud (Claude) + custom tools (MCP) per creare un assistente production-ready.

**Durata:** 2 mesi | **Focus:** Claude-Native + Provider-Agnostic Architecture

> **Filosofia:** Impara principi **universali** applicabili a qualsiasi LLM (90%), poi specializzati su Claude per vantaggio competitivo (10%).

## 🛠️ Stack (Provider-Agnostic)
- **AI Layer:**
  - Ollama (llama3.1:8b) - Intent parsing locale
  - Claude API (Sonnet 4.5) - Complex reasoning **[Facilmente sostituibile]**
  - MCP Server (TypeScript) - Custom tools
  - Provider abstraction (`IAIProvider` interface)
- .NET 8 Minimal API
- PostgreSQL, Redis
- Google Calendar + Microsoft Graph API
- React + TypeScript
- Web Speech API (voice, opzionale)

## 🎯 Cosa Impari (90% Generico!)

### **Phase 1: Ollama Foundation** (W1-3) → 🟢 **100% UNIVERSALE**
- Ollama integration, prompt engineering, function calling
- Intent recognition & entity extraction
- RAG (Retrieval-Augmented Generation)
- Context management
- **Trasferibile:** 100% riutilizzabile con GPT/Gemini

### **Phase 2: Cloud AI + Tools** (W4-6) → 🟡 **80% UNIVERSALE**
- Claude API integration (concetti applicabili a OpenAI/Gemini)
- MCP Server development (tool server pattern universale)
- Tool use / Function calling (standard tra provider)
- **Trasferibile:** Puoi migrare a OpenAI in 2-3 giorni

### **Phase 3: Provider-Agnostic** (W7-8) → 🟢 **95% UNIVERSALE**
- AI Router pattern (funziona con QUALSIASI LLM)
- Provider abstraction layer
- Multi-provider fallback
- Agentic workflows
- **Trasferibile:** Sistema supporta Claude/OpenAI/Gemini/Ollama

## 💬 Example Conversations

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
```

```
User: "Quando ho tempo libero questa settimana per un caffè?"
AI:   "Ecco i tuoi slot liberi di almeno 1 ora:
       • Mercoledì 5 feb: 14:00-16:00 ✨
       • Giovedì 6 feb: 10:00-12:00
       • Venerdì 7 feb: 15:00-18:00

       (✨ = consigliato, hai pochi meeting quel giorno)"
```

## 📅 Timeline
| Mese | Focus |
|------|-------|
| 5 | Ollama + Calendar APIs + Context |
| 6 | RAG + Multi-Calendar + Voice + Polish |

## 🏆 Boss Battle
**"Autonomous Week Organizer"**: Chiedi a Claude di "ottimizzare la mia settimana". L'AI deve autonomamente:
1. Leggere tutti gli eventi via MCP
2. Identificare problemi (conflitti, no breaks, etc.)
3. Proporre e implementare ottimizzazioni
4. Zero errori, 100% autonomous

**Reward:** +500 XP

## 🔗 Links
- [[Tasks/Week-01|▶️ Week 1: Ollama Setup (100% Universale)]]
- [[../../../claude/roadmaps/ai-skills|📚 AI Skills Roadmap Completa]]
- [[../../../AI-Frontier/README|🔬 AI Frontier Lab]]

## 🎨 Architecture (Hybrid: Ollama + Claude + MCP)

```
┌─────────────────────────────────────────────────────┐
│              User Interface (React)                  │
│        Natural Language + Voice Input               │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│         .NET 8 Web API (Orchestrator)               │
│                                                      │
│  ┌──────────────┐          ┌──────────────┐        │
│  │   Ollama     │          │   Claude     │        │
│  │  (Local AI)  │          │ (Cloud AI)   │        │
│  └──────┬───────┘          └──────┬───────┘        │
│         │                         │                 │
│         │    ┌────────────────────┘                 │
│         ▼    ▼                                      │
│  ┌─────────────────┐                               │
│  │   AI Router     │ ← Decides: Ollama or Claude?  │
│  │ (Smart Dispatch)│                               │
│  └────────┬────────┘                               │
│           │                                         │
│           ▼                                         │
│  ┌─────────────────┐                               │
│  │ Calendar Actions│ ← Executes via APIs           │
│  └────────┬────────┘                               │
└───────────┼─────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────┐
│   MCP Server (TypeScript)                           │
│   ├─ calendar.list_events()                         │
│   ├─ calendar.create_event()                        │
│   ├─ calendar.find_free_slots()                     │
│   └─ calendar.get_preferences()                     │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│  Google Calendar │ Outlook │ PostgreSQL │ Redis    │
└─────────────────────────────────────────────────────┘

FLOW:
1. User: "Prenota dal dentista"
   → Ollama (fast intent extraction)
2. Complex reasoning needed?
   → Claude via MCP (or OpenAI, configurable!)
3. System creates event
```

## 📝 Key Technical Highlights

### Function Calling
L'AI decide quale funzione chiamare e con quali parametri:
```json
{
  "function": "create_event",
  "params": {
    "title": "Dentista",
    "start_date": "2026-02-11",
    "start_time": "15:00",
    "duration_minutes": 60
  },
  "confidence": 0.96
}
```

### RAG Pattern
L'AI legge eventi passati per rispondere con contesto:
```
Query: "Quando sono libero per un caffè?"
→ Fetch eventi della settimana
→ Analizza slot liberi
→ Considera preferenze utente
→ Risposta personalizzata
```

### Provider Abstraction
Sistema che può usare Claude, OpenAI, Gemini, o Ollama intercambiabilmente:
```csharp
public interface IAIProvider
{
    Task<AIResponse> Chat(ChatRequest request);
    Task<AIResponse> ChatWithTools(ChatRequest request, List<Tool> tools);
}

// Implementazioni: ClaudeProvider, OpenAIProvider, GeminiProvider, OllamaProvider
// AI Router decide quale usare dinamicamente
```

### Hybrid Strategy
- **95% queries** → Ollama (fast, free, local)
- **5% queries** → Claude (complex reasoning)
- **Fallback** → OpenAI se Claude down
- **Cost:** ~$5/mese invece di $150/mese

---

## 📊 Skill Transferability

| Skill | Genericità | Tempo per Migrare ad Altro Provider |
|-------|------------|-------------------------------------|
| Prompt Engineering | 🟢 100% | 0 giorni (identico) |
| Function Calling | 🟢 95% | 1-2 giorni (sintassi diversa) |
| RAG Pattern | 🟢 100% | 0 giorni (universale) |
| Claude API | 🟡 85% | 2-3 giorni (OpenAI simile) |
| MCP Protocol | 🟡 70% | 3-5 giorni (adapter necessario) |
| AI Router | 🟢 100% | 0 giorni (design pattern) |
| Provider Abstraction | 🟢 100% | 0 giorni (architettura) |

**Bottom line:** Dopo questo progetto, puoi passare da Claude ad OpenAI in 2-3 giorni. Non sei locked-in!

---

*Questo progetto ti prepara per:*
- Integrare AI in BookingHub (P3) e FamilyBudget (P4)
- Lavorare con QUALSIASI AI provider
- Essere AI-Native Architect
