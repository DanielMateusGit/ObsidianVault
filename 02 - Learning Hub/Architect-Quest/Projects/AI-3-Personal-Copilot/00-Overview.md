---
tags: [architect-quest, project, ai-track, ai-3, mcp, code-analysis, vscode]
status: locked
duration: 2 months
start: M23
end: M24
type: ai-first
---

# 🤖 AI-3: Personal Copilot

## 📋 Overview
Un Copilot personalizzato che conosce il TUO stile di codice e i TUOI progetti.

**Durata:** 2 mesi (Mesi 23-24) | **Focus:** MCP Avanzato, Code Analysis, VS Code Extension

**Tipo:** AI-First Project - Il TUO assistente coding!

**Dopo:** Tutto il resto completato

---

## 🎯 Obiettivo
Costruire un assistente AI che conosce:
- Il tuo stile di codice
- I tuoi pattern preferiti
- I tuoi progetti passati
- Le tue decisioni architetturali

---

## 🛠️ Stack
- MCP Server (TypeScript) - già conosci da P2.5
- GitHub API
- AST parsing (Roslyn per C#)
- Claude API con tool use
- VS Code extension

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| MCP Avanzato | Complex tools, multi-step workflows |
| Code Analysis | AST parsing, static analysis |
| GitHub Integrations | PR review, commit analysis |
| Personalization | Learning user patterns |
| VS Code Extension | Development e pubblicazione |
| Pattern Mining | Analisi del tuo codice passato |

---

## 🖥️ Features

```
┌─────────────────────────────────────────────────────────────┐
│                   PERSONAL COPILOT                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔍 CODE REVIEW                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ PR #42: "Add notification retry logic"              │   │
│  │                                                      │   │
│  │ 🤖 Review:                                           │   │
│  │ • ✅ Good: Follows your retry pattern from P1       │   │
│  │ • ⚠️ Suggestion: Consider exponential backoff       │   │
│  │ • ❌ Issue: Missing null check line 45              │   │
│  │ • 💡 Style: You usually use guard clauses here      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  🧪 TEST GENERATION                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Selected: NotificationService.SendAsync()           │   │
│  │                                                      │   │
│  │ 🤖 Generated tests:                                  │   │
│  │ • SendAsync_ValidNotification_ReturnsSuccess        │   │
│  │ • SendAsync_NullRecipient_ThrowsArgumentException   │   │
│  │ • SendAsync_ChannelUnavailable_RetriesThreeTimes    │   │
│  │                                                      │   │
│  │ [Apply to project] [Edit] [Regenerate]              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📝 REFACTORING SUGGESTIONS                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ File: NotificationHandler.cs                        │   │
│  │                                                      │   │
│  │ 🤖 Suggestions based on YOUR patterns:              │   │
│  │ • Extract method: lines 45-67 → ValidateRequest()   │   │
│  │ • This class has 8 methods, you usually keep < 6    │   │
│  │ • Consider splitting into Handler + Validator       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  💬 CHAT (Context-aware)                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ You: "How did I implement retry in P1?"             │   │
│  │                                                      │   │
│  │ 🤖: "In P1 Notification Service, you used Polly    │   │
│  │     with exponential backoff. Here's the code:      │   │
│  │     [code from your actual project]                 │   │
│  │     Want me to apply the same pattern here?"        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📅 Piano Settimane

### Mese 23: Core Features
- [ ] W1: MCP server con GitHub integration
- [ ] W2: Code review automation
- [ ] W3: Test generation con AST parsing
- [ ] W4: Refactoring suggestions

### Mese 24: Personalization + VS Code
- [ ] W5: Learn user patterns (analyze past commits)
- [ ] W6: VS Code extension
- [ ] W7: Chat mode con project context
- [ ] W8: Boss Battle

---

## 📦 Deliverables

- [ ] MCP server con tool use avanzato
- [ ] GitHub PR review automation
- [ ] Test generation
- [ ] Refactoring suggestions
- [ ] VS Code extension
- [ ] Chat con context dei tuoi progetti
- [ ] Pattern learning dal tuo codice

---

## 🔧 MCP Tools

```typescript
// Tools che il Copilot espone
const tools = [
  {
    name: "analyze_pr",
    description: "Analyzes a GitHub PR against user's patterns",
    parameters: { pr_number: "number" }
  },
  {
    name: "generate_tests",
    description: "Generates tests for a method in user's style",
    parameters: { file_path: "string", method_name: "string" }
  },
  {
    name: "suggest_refactoring",
    description: "Suggests refactoring based on user's preferences",
    parameters: { file_path: "string" }
  },
  {
    name: "find_similar_code",
    description: "Finds similar patterns in user's past projects",
    parameters: { code_snippet: "string" }
  }
];
```

---

## 🏆 Boss Battle: "Team Copilot"

**Scenario:** Estendi per supportare team (shared patterns, team style guide enforcement).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (team patterns storage), C4 Container |
| **B. Domain Model** | Team, StyleGuide, Pattern, Violation |
| **C. API Spec** | OpenAPI per team management, pattern CRUD |
| **D. Implementazione** | Style guide enforcement in PR review |

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 💡 Cosa Lo Rende "Personal"

Il Copilot impara da:

| Fonte | Cosa Impara |
|-------|-------------|
| Tuoi progetti GitHub | Pattern, naming, struttura |
| Tue note Obsidian | Preferenze architetturali, ADR |
| Tuoi commit | Stile messaggi, frequenza refactoring |
| Tue PR reviews | Cosa consideri importante |

---

## 🔗 Integrazione con Ecosystem

```
┌─────────────────────────────────────────────────┐
│              PERSONAL COPILOT                    │
│                                                  │
│  LEGGE:                                          │
│  ├── GitHub repos (P1, P2, P3, P4, P5)          │
│  ├── Obsidian notes (AI-1 Second Brain)         │
│  └── Past reviews & decisions                    │
│                                                  │
│  USA:                                            │
│  ├── AI Gateway (P2.5) per LLM calls            │
│  └── Pattern database costruito nel tempo       │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## ❤️ Connessione al WHY

Questo progetto ti rende **più produttivo**:
- ⚡ Review più veloci
- 🧪 Test automatici
- 📝 Refactoring guidato
- 💼 Più tempo per quello che conta

---

*Ultimo aggiornamento: 2026-03-04*
