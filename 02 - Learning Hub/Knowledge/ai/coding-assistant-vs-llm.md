---
tags:
  - ai
  - claude
  - anthropic
  - from/course-claude-code
  - status/learning
aliases:
  - Coding Assistant Architecture
  - Claude Code vs LLM
created: 2026-03-13
updated: 2026-03-18
source: "Claude Code in Action - Lesson 1 + Anthropic Docs"
---

# Coding Assistant vs Language Model

> **One-liner:** Un Coding Assistant e un intermediario che potenzia un LLM con tool (I/O, esecuzione, API) e context management strutturato, trasformandolo da "cervello che parla" a "agente che agisce".

## Cos'e

Un Language Model (LLM) da solo **sa programmare**: conosce i linguaggi, i pattern, le best practice, genera codice corretto. Ma **non puo agire**: non puo leggere file, eseguire comandi, modificare codice o interagire con sistemi esterni.

E come un chirurgo brillantissimo che sa esattamente dove tagliare... ma non ha le mani. Sa **cosa** fare, non puo **farlo**.

Un **Coding Assistant** (come Claude Code) aggiunge tre capacita fondamentali:

1. **Tool System** — Strumenti che l'LLM puo invocare per agire nel mondo reale:
   - **Tool nativi** (built-in): `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`
   - **Tool estesi** (MCP): GitHub, Playwright, database, custom tools
   - **Sub-agents**: altri agenti Claude che lavorano in parallelo su sotto-task

2. **Context Management** — Struttura che fornisce all'LLM le informazioni giuste:
   - File `CLAUDE.md` a 3 livelli (progetto, locale, globale)
   - `@file` e `@folder` per citare contesto specifico
   - Auto-memory per apprendimento persistente tra sessioni

3. **Workflow Specializzati** — Pattern ottimizzati per coding:
   - Hooks (validazione automatica pre/post azione)
   - Custom commands (skill riutilizzabili)
   - Planning mode per problemi complessi

**Architettura:** L'utente parla al Coding Assistant, che costruisce un prompt arricchito (contesto + tool disponibili + istruzioni) e lo invia all'LLM. L'LLM risponde con testo o tool calls, il Coding Assistant esegue i tool e ritorna i risultati all'LLM in un loop agentico.

### Agentic Loop

L'**agentic loop** e il meccanismo che trasforma un LLM da "generatore di testo" a "agente che agisce". Funziona cosi:

```
1. L'utente chiede qualcosa ("fixa il bug nel login")
2. L'LLM analizza e decide: "devo leggere il file"
   → Tool call: Read src/auth/login.ts
3. Il Coding Assistant esegue il tool e ritorna il risultato
4. L'LLM analizza il risultato e decide il prossimo step:
   → Tool call: Edit src/auth/login.ts (applica fix)
5. Il Coding Assistant esegue e ritorna il risultato
6. L'LLM decide: "devo verificare"
   → Tool call: Bash "npm test"
7. Se i test falliscono → torna al punto 4 (corregge e riprova)
8. Se i test passano → risponde all'utente con il riepilogo
```

**Punto chiave:** Il loop e **autonomo** — l'LLM decide da solo quale tool usare, osserva il risultato, e decide il prossimo step. Non e l'utente a guidare ogni singola azione. Questo e cio che rende il Coding Assistant "agentico": agisce, osserva, reagisce, fino a completare il task.

## Quando usarlo

- **Sempre** quando fai coding con un LLM — il Coding Assistant e il modo corretto di lavorare
- Quando hai bisogno che l'AI legga, scriva, esegua codice
- Quando vuoi contesto persistente tra sessioni (CLAUDE.md, auto-memory)
- Quando vuoi automazione (hooks, custom commands)

## Quando NON usarlo

- Per domande puramente teoriche senza bisogno di I/O (un LLM diretto basta)
- Se stai solo chattando/brainstorming senza toccare codice
- Se hai vincoli di privacy e non vuoi dare accesso al filesystem

## Esempio

```
Senza Coding Assistant (LLM diretto):
  User: "Fixa il bug nel login"
  LLM: "Ecco come potresti fixare il bug..." (testo generico)
  → Devi copiare/incollare, applicare, testare manualmente

Con Coding Assistant (Claude Code):
  User: "Fixa il bug nel login"
  Claude Code:
    1. Read src/auth/login.ts        → capisce il codice
    2. Grep "login.*error"           → trova il bug
    3. Edit src/auth/login.ts        → applica il fix
    4. Bash "npm test"               → verifica che funzioni
  → Fix applicato e testato automaticamente
```

## Collegamenti

- [[context-management]] - Come gestire il contesto nei 3 livelli
- [[mcp-servers]] - Come estendere le capabilities con MCP
- [[claude-code-hooks]] - Automazione con hooks
- [[model-selection-strategy]] - Scegliere il modello giusto per il task

## Quiz

### Q1: Perche serve un Coding Assistant invece di usare direttamente il LLM? (CLCODE-01)
Hai un Language Model che sa rispondere a prompt. Perche serve un Coding Assistant invece di usare direttamente il LLM per coding?

**Mia risposta:**

---

### Q2: Tool nativi vs MCP: quando preferire MCP? (CLCODE-13)
Claude Code ha tool nativi (Read, Write, Edit, Bash). Quando ha senso aggiungere un MCP Server invece di usare i tool nativi?

**Mia risposta:**

---

### Q3: Loop agentico
Cosa succede quando Claude Code chiama un tool? Descrivi il ciclo completo dal prompt dell'utente al risultato finale.

**Mia risposta:**

---

## Risorse

- [Claude Code Overview](https://code.claude.com/docs/en/overview) - Documentazione ufficiale
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) - Pattern consigliati
