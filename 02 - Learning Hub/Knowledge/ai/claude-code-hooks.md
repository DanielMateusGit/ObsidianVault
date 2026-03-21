---
tags:
  - ai
  - claude
  - anthropic
  - automation
  - from/course-claude-code
  - status/learning
aliases:
  - Claude Code Hooks
  - Hook Automation
  - TDD con Hooks
created: 2026-03-13
updated: 2026-03-18
source: "Claude Code in Action - Lessons 7-8 + Anthropic Docs (code.claude.com/docs/en/hooks)"
---

# Claude Code Hooks - Automazione e Validazione

> **One-liner:** Gli Hooks sono comandi (shell, HTTP, prompt LLM, o agent) che si eseguono automaticamente prima o dopo le azioni di Claude Code, funzionando come un CI/CD integrato nell'editor.

## Cos'e

Un **Hook** e un'azione automatica che si attiva in risposta a eventi nel lifecycle di Claude Code. Pensa a un hook come un trigger: "quando Claude fa X, esegui automaticamente Y".

### Configurazione

```json
// In .claude/settings.json o ~/.claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npm run tsc --noEmit"
          }
        ]
      }
    ]
  }
}
```

### Eventi principali

| Evento | Quando | Puo bloccare? |
|--------|--------|---------------|
| **PreToolUse** | Prima dell'esecuzione di un tool | Si (deny/allow) |
| **PostToolUse** | Dopo l'esecuzione di un tool | No (ma puo dare feedback) |
| **PermissionRequest** | Quando appare il dialogo permessi | Si (auto-allow/deny) |
| **UserPromptSubmit** | Prima che Claude processi il prompt | Si (block) |
| **Stop** | Quando l'agente finisce | Si (forza continuazione) |
| **SessionStart** | All'inizio sessione | No (inject contesto) |

### Matcher (filtro)

I matcher sono regex che filtrano quando l'hook si attiva:

```json
"matcher": "Bash"           // Solo tool Bash
"matcher": "Edit|Write"     // Edit O Write
"matcher": "mcp__memory__.*" // Tool MCP specifici
```

### 4 Tipi di Hook

| Tipo | Come funziona | Caso d'uso |
|------|---------------|------------|
| **command** | Esegue script shell, riceve JSON su stdin | Validazione, linting, test |
| **http** | POST a endpoint HTTP | Policy server, audit esterno |
| **prompt** | Invia a un modello Claude per valutazione | Review semantica del codice |
| **agent** | Spawn agente con accesso a tool (Read, Grep) | Validazione complessa multi-file |

### Exit codes (per command hooks)

- **Exit 0**: Successo, JSON su stdout viene parsato per decisioni
- **Exit 2**: Errore bloccante, stderr viene inviato a Claude come errore
- **Altro**: Errore non bloccante, loggato in verbose mode

### Pattern Killer: Claude SDK in Hooks ("Hook Inception")

Un hook puo chiamare Claude stesso per fare code review automatica:

```javascript
// hook-review.js
import Anthropic from '@anthropic-ai/sdk';

const claude = new Anthropic();
const code = readFile(filePath);

const response = await claude.messages.create({
  model: 'claude-sonnet-4-5-20241022',
  messages: [{ role: 'user', content: `Review this code:\n${code}` }]
});
```

**Risultato:** Claude edita → Hook chiama ALTRO Claude per review → Feedback a Claude principale.

## Quando usarlo

- **TDD automatico**: Hook post-edit che esegue test → Claude vede fallimenti → fixa automaticamente
- **Code quality**: Linting, type checking dopo ogni modifica
- **Sicurezza**: Bloccare comandi pericolosi (`rm -rf`, `git push --force`)
- **Audit**: Logging di tutte le operazioni di Claude
- **Contesto dinamico**: Iniettare info (es. ultimi commit) all'inizio sessione
- **Auto-permessi**: Approvare automaticamente comandi sicuri (es. `npm test`)

## Quando NON usarlo

- **Azioni irreversibili**: Mai hook per `git push`, `deploy`, `delete` — devono essere decisioni esplicite
- **Hook lenti (>30s)**: Rallentano il workflow, Claude aspetta
- **Troppi hook (>5)**: Overhead eccessivo, confondono Claude con troppo output
- **Side effects permanenti**: Hook deve essere di validazione/feedback, non di azione critica
- **Output verboso**: Claude si confonde con troppo feedback; mantieni conciso

## Esempio

### Pattern TDD con Hooks

```json
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "dotnet test --no-restore --verbosity quiet",
            "statusMessage": "Running tests..."
          }
        ]
      }
    ]
  }
}
```

**Workflow risultante:**
```
1. Claude scrive codice
2. Hook esegue test automaticamente
3. Test falliscono → Claude vede errori nell'output
4. Claude fixa automaticamente
5. Hook riesegue test
6. Test passano ✅ → Claude continua
```

### Hook per bloccare comandi pericolosi

```bash
#!/bin/bash
# .claude/hooks/block-dangerous.sh
COMMAND=$(jq -r '.tool_input.command' < /dev/stdin)

if echo "$COMMAND" | grep -qE '(rm -rf|git push --force)'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "Comando pericoloso bloccato"
    }
  }'
  exit 0
fi
exit 0
```

## Collegamenti

- [[coding-assistant-vs-llm]] - Gli hooks sono parte del tool system del Coding Assistant
- [[mcp-servers]] - Hooks possono validare anche tool MCP
- [[context-management]] - SessionStart hooks possono iniettare contesto

## Quiz

### Q1: Configurazione hook TypeScript post-edit (CLCODE-07)
Vuoi che TypeScript venga controllato DOPO che Claude modifica file `.ts`. Come configuri l'hook?

A) `trigger: "pre", tools: ["Edit"], command: "tsc"`
B) `trigger: "post", tools: ["Edit", "Write"], matcher: "**/*.ts", command: "npm run tsc"`
C) `trigger: "post", tools: ["Bash"], command: "tsc"`

**Mia risposta:**

---

### Q2: Claude SDK vs linter in hook (CLCODE-08)
Hai un hook che chiama Claude SDK per fare code review. Qual e il vantaggio rispetto a un normale linter?

A) E piu veloce
B) Capisce il contesto semantico del codice
C) Non richiede configurazione
D) Costa meno

**Mia risposta:**

---

### Q3: Cosa NON dovrebbe essere un hook? (CLCODE-09)
Quale di questi NON dovrebbe essere un hook?

A) `npm run tsc` post-edit TypeScript
B) `git push` post-commit
C) `eslint` post-edit JavaScript
D) `npm test` post-edit src files

**Mia risposta:**

---

### Q4: Hook feedback levels (CLCODE-22)
Qual e la differenza tra exit code 0, exit code 2, e un altro exit code in un command hook? Quando usi ciascuno?

**Mia risposta:**

---

## Risorse

- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) - Documentazione completa hooks
- [Hook Examples](https://code.claude.com/docs/en/hooks#examples) - Esempi ufficiali
- [Anthropic SDK](https://www.npmjs.com/package/@anthropic-ai/sdk) - Per hook con Claude SDK
