---
tags: [architect-quest, p2.5, week-01, ai]
status: not-started
xp_available: 350
genericita: 100%
---

# 📅 Week 1: Universal AI Foundations → 🟢 **100% GENERICO**

## 🎯 Obiettivo
Imparare fondamenti AI **universali** applicabili a QUALSIASI LLM (GPT, Claude, Gemini, Ollama).

**Perché Ollama?** È il "lab gratuito" per imparare senza spendere. I concetti sono identici con altri provider.

**Transferability:** Tutto ciò che impari questa settimana funziona con OpenAI, Claude, Gemini, Mistral, etc.

## 📋 Tasks

### Setup Environment (Day 1)
- [ ] Verifica Ollama funzionante: `ollama list`
- [ ] Pull modelli necessari:
  - `ollama pull llama3.1:8b` (veloce, accurato)
  - `ollama pull qwen2.5:32b` (più potente, opzionale)
- [ ] Crea repo GitHub `ai-calendar-assistant`
- [ ] Solution .NET 8:
  - CalendarAssistant.Domain
  - CalendarAssistant.Application
  - CalendarAssistant.Infrastructure
  - CalendarAssistant.Api

### Ollama Integration (Day 2-3)
- [ ] Crea `OllamaService.cs` per comunicare con Ollama
- [ ] Implementa basic chat endpoint
- [ ] Test: "Ciao" → risposta dall'AI
- [ ] Implementa JSON mode forcing
- [ ] Test: risposta strutturata JSON

### Intent Recognition (Day 4)
- [ ] Design system prompt per calendar assistant
- [ ] Implementa riconoscimento intents:
  - `create_event`
  - `list_events`
  - `update_event`
  - `delete_event`
- [ ] Test con frasi esempio:
  - "Prenota meeting domani alle 10"
  - "Mostrami i miei appuntamenti"
  - "Cancella il dentista"

### Entity Extraction (Day 5)
- [ ] Estrai date da linguaggio naturale
- [ ] Estrai orari (formato 12h/24h)
- [ ] Estrai durata (esplicita o inferita)
- [ ] Gestisci date relative ("domani", "lunedì prossimo")
- [ ] Test cases completi

## 📖 Letture (Universali!)
- [ ] **"Prompt Engineering Guide"** - DAIR.AI (universale, non Ollama-specific)
- [ ] **Ollama docs** - https://ollama.ai/docs (per setup, ma concetti universali)
- [ ] **"Function Calling Overview"** - Anthropic/OpenAI docs (pattern standard)

**Nota:** Stai imparando concetti che funzionano con TUTTI i LLM moderni, non solo Ollama.

## 💻 Code Examples da Implementare

### 1. OllamaService Basic
```csharp
public class OllamaService
{
    private readonly HttpClient _httpClient;

    public OllamaService(HttpClient httpClient)
    {
        _httpClient = httpClient;
        _httpClient.BaseAddress = new Uri("http://localhost:11434");
    }

    public async Task<string> Chat(string message)
    {
        var response = await _httpClient.PostAsJsonAsync("/api/chat", new
        {
            model = "llama3.1:8b",
            messages = new[]
            {
                new { role = "user", content = message }
            },
            stream = false
        });

        var result = await response.Content
            .ReadFromJsonAsync<OllamaResponse>();
        return result.Message.Content;
    }
}
```

### 2. System Prompt
```csharp
private const string SYSTEM_PROMPT = """
    You are a calendar assistant. Parse user requests about calendar events.

    Respond ONLY with valid JSON in this format:
    {
      "intent": "create_event" | "list_events" | "update_event" | "delete_event",
      "entities": {
        "title": string | null,
        "date": "YYYY-MM-DD" | null,
        "time": "HH:mm" | null,
        "duration_minutes": number | null
      },
      "confidence": number (0-1),
      "clarification_needed": boolean,
      "clarification_question": string | null
    }

    Examples:
    Input: "Prenota meeting domani alle 10"
    Output: {
      "intent": "create_event",
      "entities": {
        "title": "meeting",
        "date": "2026-02-03",
        "time": "10:00",
        "duration_minutes": 60
      },
      "confidence": 0.9,
      "clarification_needed": false
    }

    Input: "Mostrami gli appuntamenti"
    Output: {
      "intent": "list_events",
      "entities": {},
      "confidence": 0.95,
      "clarification_needed": false
    }

    Current date: {DateTime.Now:yyyy-MM-dd}
    Current time: {DateTime.Now:HH:mm}
    """;
```

### 3. Intent Recognition Endpoint
```csharp
[HttpPost("parse")]
public async Task<ActionResult<CalendarIntent>> ParseIntent(
    [FromBody] ParseRequest request)
{
    var prompt = $"{SYSTEM_PROMPT}\n\nUser: {request.Message}";

    var response = await _ollama.ChatWithJson<CalendarIntent>(prompt);

    if (response.ConfidenceScore < 0.7)
    {
        return Ok(new {
            success = false,
            clarification_needed = true,
            question = response.ClarificationQuestion
        });
    }

    return Ok(response);
}
```

## 🧪 Test Cases

```csharp
[Fact]
public async Task ParseIntent_CreateEvent_ExtractsCorrectly()
{
    // Arrange
    var message = "Prenota dal dentista martedì prossimo alle 15";

    // Act
    var result = await _service.ParseIntent(message);

    // Assert
    Assert.Equal("create_event", result.Intent);
    Assert.Equal("Dentista", result.Entities.Title);
    Assert.Equal("2026-02-11", result.Entities.Date);
    Assert.Equal("15:00", result.Entities.Time);
}

[Theory]
[InlineData("domani alle 10", "2026-02-03", "10:00")]
[InlineData("dopodomani mattina", "2026-02-04", "09:00")]
[InlineData("lunedì prossimo", "2026-02-10", null)]
public async Task ParseIntent_RelativeDates_WorkCorrectly(
    string input, string expectedDate, string? expectedTime)
{
    var result = await _service.ParseIntent($"Meeting {input}");

    Assert.Equal(expectedDate, result.Entities.Date);
    Assert.Equal(expectedTime, result.Entities.Time);
}
```

## ✅ Acceptance Criteria

- [ ] LLM risponde correttamente (Ollama per ora, ma pattern universale)
- [ ] JSON mode funziona sempre (no markdown, no testo)
- [ ] Riconosce i 4 intent base (create/list/update/delete)
- [ ] Estrae date relative ("domani", "prossimo lunedì")
- [ ] Estrae orari in formato 24h
- [ ] Confidence score > 0.7 per frasi chiare
- [ ] Test coverage > 80%
- [ ] **BONUS:** Code è provider-agnostic (può swap Ollama → GPT in futuro)

## ✅ XP
| Deliverable | XP |
|-------------|-----|
| LLM integration funzionante | +75 |
| Intent recognition implementato | +100 |
| Entity extraction (date/time) | +100 |
| Test suite completa | +75 |

**Totale Week 1:** +350 XP

---

## 🎯 Skill Universali Imparate

Questa settimana hai imparato:
- ✅ **Prompt engineering** → Funziona con GPT/Claude/Gemini/Mistral
- ✅ **Function calling** → Standard OpenAI/Anthropic
- ✅ **JSON mode** → Supportato da tutti i LLM moderni
- ✅ **Intent recognition** → Pattern universale
- ✅ **Entity extraction** → Tecnica universale

**Tempo per migrare ad altro provider:** 2-3 ore (solo endpoint HTTP diverso, logica identica)

---

[[Week-02|Week 2 → (Integration Patterns, ancora 100% universale)]]
