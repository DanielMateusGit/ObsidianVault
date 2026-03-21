---
tags:
  - ai
  - claude
  - anthropic
  - mcp
  - from/course-claude-code
  - status/learning
aliases:
  - Model Context Protocol
  - MCP
  - MCP Server
created: 2026-03-13
updated: 2026-03-18
source: "Claude Code in Action - Lesson 3 + modelcontextprotocol.io + Anthropic Docs"
---

# MCP Servers - Model Context Protocol

> **One-liner:** MCP e uno standard aperto (come USB-C per l'AI) che permette a un Coding Assistant di connettersi a sistemi esterni tramite un protocollo client-server con 3 primitive: Tools, Resources e Prompts.

## Cos'e

**Model Context Protocol (MCP)** e un protocollo open-source creato da Anthropic per connettere applicazioni AI a sistemi esterni in modo standardizzato.

### Architettura Client-Server

```
MCP Host (Claude Code)
├── MCP Client 1 ──── MCP Server A (locale, es. filesystem)
├── MCP Client 2 ──── MCP Server B (locale, es. database)
└── MCP Client 3 ──── MCP Server C (remoto, es. GitHub)
```

- **MCP Host**: L'applicazione AI (Claude Code, VS Code, ChatGPT)
- **MCP Client**: Componente nel host che mantiene la connessione a un server
- **MCP Server**: Programma che espone capabilities al client

### Le 3 Primitive

| Primitiva | Cosa fa | Esempio |
|-----------|---------|---------|
| **Tools** | Azioni eseguibili dall'AI | Creare PR, query DB, inviare email |
| **Resources** | Dati leggibili dall'AI | Contenuto file, record DB, risposte API |
| **Prompts** | Template riutilizzabili | System prompt, few-shot examples |

### Layer di Trasporto

| Trasporto | Dove | Caratteristiche |
|-----------|------|-----------------|
| **stdio** | Locale (stessa macchina) | Veloce, zero network overhead |
| **Streamable HTTP** | Remoto (server esterno) | Supporta auth (OAuth, API keys), serve molti client |

### Protocollo

- Basato su **JSON-RPC 2.0**
- **Lifecycle management**: Handshake iniziale per negoziare capabilities
- **Discovery dinamica**: Il client scopre tool/resources con `*/list`, poi li usa
- **Notifiche real-time**: Il server notifica cambiamenti ai client connessi

## Quando usarlo

- **Integrazione con sistemi esterni**: GitHub (PR, issues), Jira, Slack, database
- **Accesso a dati non nel filesystem**: API interne, Google Drive, Notion, Confluence
- **Automazione workflow**: ADO Work Items → Claude → GitHub PR → Pipeline
- **Tool specializzati**: Playwright (browser testing), Sentry (error tracking), Blender (3D)
- **Quando i tool nativi non bastano**: I tool built-in (Read, Write, Bash) coprono il filesystem locale; MCP estende a tutto il resto

## Quando NON usarlo

- Se i tool nativi bastano (Read/Write/Bash coprono la maggior parte dei task locali)
- Se esiste un modo piu semplice (es. `git` via Bash invece di un MCP Git server)
- Per operazioni una tantum (non vale la pena configurare un server per un singolo task)
- Se il server MCP non e mantenuto/sicuro (valuta sempre la fonte)

## Esempio

```json
// Configurazione MCP in .claude/settings.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxx"
      }
    }
  }
}
```

```
// Workflow semi-automatizzato con MCP:

[Work Item ADO]  →  "Fix bug login email validation"
     ↓
[Programmatore]  →  Arricchisce descrizione, lancia Claude
     ↓
[Claude + MCP]   →  1. Legge Work Item (MCP ADO)
                     2. Analizza codebase (tool nativi)
                     3. Crea branch + implementa fix
                     4. Commit + push (MCP GitHub)
                     5. Apre PR (MCP GitHub)
     ↓
[Pipeline CI]    →  Build + Test automatici
     ↓
[Programmatore]  →  ✅ Review PR  ← CONTROLLO UMANO
     ↓
[Claude]         →  Merge + chiude Work Item

Risultato: 80% lavoro meccanico automatizzato
           20% decisioni critiche dall'umano
```

### Creare un MCP Server custom (TypeScript)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "my-server", version: "1.0.0" });

// Esponi un tool
server.tool("query_db", { sql: z.string() }, async ({ sql }) => ({
  content: [{ type: "text", text: JSON.stringify(await db.query(sql)) }]
}));

// Esponi una resource
server.resource("schema://tables", async () => ({
  contents: [{ uri: "schema://tables", text: await db.getSchema() }]
}));

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Collegamenti

- [[coding-assistant-vs-llm]] - Architettura del Coding Assistant (MCP estende i tool)
- [[claude-code-hooks]] - Hooks possono lavorare con MCP tools
- [[context-management]] - MCP e un meccanismo di contesto aggiuntivo

## Quiz

### Q1: Ruolo dell'umano nel workflow automatizzato (CLCODE-05)
Nel workflow `ADO → Claude → GitHub → Pipeline`, qual e il ruolo critico dell'umano?

A) Scrivere il codice manualmente
B) Validare la PR prima del merge
C) Lanciare la pipeline CI
D) Chiudere il Work Item

**Mia risposta:**

---

### Q2: Setup MCP GitHub (CLCODE-18)
Dove va la configurazione di un MCP server come GitHub in Claude Code?

**Mia risposta:**

---

### Q3: MCP locale vs remoto (CLCODE-19)
Qual e la differenza tra un MCP server locale e uno remoto? Fai un esempio di ciascuno.

**Mia risposta:**

---

### Q4: Le 3 primitive MCP
Un MCP server puo esporre Tools, Resources e Prompts. Spiega la differenza tra le tre con un esempio concreto per ciascuna.

**Mia risposta:**

---

## Risorse

- [MCP Introduction](https://modelcontextprotocol.io/introduction) - Introduzione ufficiale al protocollo
- [MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture) - Architettura dettagliata
- [Build MCP Servers](https://modelcontextprotocol.io/docs/develop/build-server) - Guida per creare server custom
- [Claude Code MCP Docs](https://code.claude.com/docs/en/mcp) - Integrazione MCP in Claude Code
