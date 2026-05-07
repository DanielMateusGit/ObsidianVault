---
tags:
  - ai
  - claude
  - anthropic
  - agentic-systems
  - from/cl101
  - status/learning
aliases:
  - Agentic Loop
  - Claude Code Loop
  - How Claude Works
created: 2026-04-28
updated: 2026-04-28
source: "Claude Code 101 - Lesson 1.1: How Claude works"
---

# Agentic Loop - Come Funziona Claude Code

> **One-liner:** Claude Code esegue un loop "Receive → Gather Context → Act → Verify → Repeat", controllato da un sistema di permessi e da una toolbelt che il modello invoca per interagire col mondo.

## Cos'è

L'**agentic loop** è il motore di esecuzione di Claude Code: invece di rispondere "una volta sola" come una chat normale, Claude **itera** finché un task non è completato (o l'utente lo interrompe).

### Le 4 fasi del loop

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   ┌──────────┐                                          │
│   │ RECEIVE  │  Input dell'utente (prompt o follow-up)  │
│   └────┬─────┘                                          │
│        ▼                                                │
│   ┌──────────────────┐                                  │
│   │ GATHER CONTEXT   │  Read file, Grep, WebFetch...    │
│   └────┬─────────────┘                                  │
│        ▼                                                │
│   ┌──────────┐                                          │
│   │ ACT      │  Edit/Write/Bash/MCP                     │
│   └────┬─────┘                                          │
│        ▼                                                │
│   ┌──────────┐     not done     ┌─────────┐             │
│   │ VERIFY   │ ───────────────► │ REPEAT  │ ──┐         │
│   └────┬─────┘                  └─────────┘   │         │
│        │ done                                 │         │
│        ▼                                      │         │
│   ┌──────────┐                                │         │
│   │ STOP     │ ◄──────────────────────────────┘         │
│   └──────────┘                                          │
│                                                         │
│   ⚠️ L'utente può INTERROMPERE in qualsiasi momento      │
│      (Esc, nuovo prompt, feedback)                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Verify è il pezzo critico**: senza, Claude potrebbe restituire output che *sembra* fatto ma è rotto (test rotti, build broken, file non salvato). Con Verify, Claude **auto-corregge** prima del ritorno all'utente: scrive codice → esegue test → se fallisce → fix → re-run → ✅ → stop.

### Chi ferma il loop?

**Entrambi**:
- **Claude** (verifica interna): test passano, output coerente, requisiti soddisfatti.
- **Utente** (giudice finale): può interrompere, dare feedback ("non è quello che volevo"), o approvare. L'utente fa parte del loop — il suo feedback è un nuovo input che alimenta il prossimo ciclo.

### Le 2 cose che servono al loop per funzionare

#### 1. Permessi (Permission Modes)

Definiscono cosa Claude può fare senza chiedere conferma:

| Modalità | File edits | Bash | Read/Glob/Grep | Quando usarla |
|----------|------------|------|----------------|---------------|
| **Default** | Chiede | Chiede | Auto | Sessione normale: massima sicurezza |
| **Auto-accept (`acceptEdits`)** | Auto | Chiede | Auto | Task ripetitivi su file noti |
| **Plan mode** | Bloccato | Bloccato | Auto | Esplorazione/design — solo lettura |
| **Bypass permissions** | Auto | Auto | Auto | ⚠️ Solo in sandbox: pericoloso |

Le modalità si cambiano via UI (Shift+Tab) o `--permission-mode` CLI.

#### 2. Tools (la "toolbelt" del modello)

Il **modello** (LLM) invoca tool per interagire col mondo. Il loop sa quali tool sono disponibili e li offre al modello a ogni turno:

| Categoria | Tool | Cosa fa |
|-----------|------|---------|
| **File system** | `Read`, `Write`, `Edit`, `Glob`, `Grep` | Lettura/scrittura/ricerca file |
| **Shell** | `Bash` | Esegue comandi (build, test, git, ecc.) |
| **Web** | `WebFetch`, `WebSearch` | Recupera info dal web |
| **Estensibilità** | **MCP servers** | Tool custom (DB, API, browser, ecc.) |

Senza tool, il loop è solo testo. È la combinazione **modello + tool + verify** che lo rende "agentic".

### Context auto-compaction

Quando il context window si avvicina al limite, Claude Code **comprime automaticamente** i messaggi precedenti: mantiene l'essenziale (file letti, decisioni, task corrente) e scarta dettagli ridondanti. Questo permette al loop di durare a lungo senza "esplodere" per saturazione.

> **Nota:** la compaction non è infinita — task molto lunghi possono comunque perdere contesto. Pratica: se il task lo permette, chiudere e riaprire la sessione con un prompt mirato.

## Quando usarlo

- **Task multi-step** che richiedono lettura → modifica → verifica (refactor, bug fix con test, feature implementation)
- **Workflow autonomi** dove vuoi che Claude itererà finché qualcosa funziona (TDD, build green, lint pass)
- **Esplorazione di codebase** in plan mode (read-only, zero rischio)
- **Lavori ripetitivi** su file simili in auto-accept mode

## Quando NON usarlo

- **Domande puramente teoriche** che non richiedono accesso al filesystem → meglio una chat
- **Task irreversibili** senza review umana (deploy in prod, drop database) — usa sempre default mode con conferma
- **Sandbox non isolato + bypass permissions** → rischio di azioni distruttive
- **Task talmente vaghi che servono 5 round di chiarimenti** → meglio definire i requisiti prima

## Esempio

### Task: "Aggiungi validazione email al register endpoint"

```
[Receive]    User: "Aggiungi validazione email al register endpoint"

[Gather]     Read register.ts
             Grep "email" src/
             Read tests/register.spec.ts

[Act]        Edit register.ts → aggiunge regex validator + 400 response
             Edit register.spec.ts → aggiunge 2 test cases

[Verify]     Bash: npm test
             ❌ Test fallisce: regex non gestisce "+" in email

[Repeat → Act]    Edit register.ts → fix regex
[Verify]          Bash: npm test  ✅
[Stop]            "Done. 2 test aggiunti, tutti passano."
```

Senza il passo **Verify**, il primo `Edit` sarebbe stato consegnato come "fatto", e l'utente avrebbe scoperto il bug solo dopo. Con Verify, il loop si auto-corregge **prima** del ritorno.

## Collegamenti

- [[coding-assistant-vs-llm]] - Differenza tra LLM "puro" e Coding Assistant agentico
- [[context-management]] - Come Claude gestisce il context window (gather + compaction)
- [[mcp-servers]] - Estendere la toolbelt con tool custom
- [[claude-code-hooks]] - Intercettare il loop (PreToolUse, PostToolUse, ecc.)

## Quiz

### Q1: Le 4 fasi del loop (CL101-01)

Nomina le 4 fasi dell'agentic loop in ordine corretto e spiega in 1 frase il ruolo di ciascuna.

**Mia risposta:**

---

### Q2: Auto-accept mode (CL101-02)

Sei in **auto-accept mode (`acceptEdits`)**. Claude vuole fare queste 3 azioni in sequenza:
1. `Edit src/user.ts` (modifica un file)
2. `Bash rm -rf dist/` (esegue comando shell)
3. `Read package.json` (legge un file)

Per quali di queste Claude **chiederà conferma** all'utente?

- A) Solo (1)
- B) Solo (2)
- C) (1) e (2)
- D) Tutte e tre
- E) Nessuna

**Mia risposta:**

---

### Q3: Perché Verify? (CL101-03)

Un collega ti dice: *"Il passo Verify è uno spreco di tempo. Se Claude scrive il codice, è ovvio che funzioni — basta restituirlo all'utente subito dopo Act."*

Spiega perché ha torto, con un esempio concreto di cosa potrebbe andare male senza Verify.

**Mia risposta:**

---

## Risorse

- [Claude Code Docs - Overview](https://docs.claude.com/en/docs/claude-code/overview) - Documentazione ufficiale
- [Anthropic Blog - Building Agents](https://www.anthropic.com/engineering/building-effective-agents) - Pattern per costruire agenti agentic (loop, verify, planner)
