---
tags:
  - ai
  - claude
  - anthropic
  - from/course-claude-code
  - status/learning
  - cheatsheet
aliases:
  - Claude Code Basics
  - Coding Assistant 101
created: 2026-03-13
source: "Claude Code in Action - Lessons 1-3"
---

# Coding Assistant Fundamentals

> **One-liner:** Un Coding Assistant è un intermediario che traduce input utente in istruzioni dettagliate comprensibili da un Language Model, potenziandolo con tool e contesto strutturato.

---

## 🧠 Coding Assistant vs Language Model

| Language Model (LLM)          | Coding Assistant                            |
| ----------------------------- | ------------------------------------------- |
| Comprende linguaggio naturale | Input utente → istruzioni dettagliate → LLM |
| Risponde a prompt             | Aggiunge tool (write, edit, bash, etc.)     |
| Memoria limitata              | Gestisce contesto strutturato               |
| Generico                      | Specializzato per coding tasks              |

**Key insight:** Il LLM è il "cervello", il Coding Assistant è il "corpo" con "mani" (tool) e "memoria" (context management).

---

## 🛠️ Tool System

### Tool Nativi (Built-in)
```
Read    → Legge file
Write   → Crea/sovrascrive file
Edit    → Modifica esistenti
Bash    → Esegue comandi
Grep    → Ricerca nel codice
Glob    → Pattern matching file
```

### Estensibilità via MCP (Model Context Protocol)
- **GitHub MCP Server** → Issues, PR, repo info
- **Playwright MCP Server** → Browser automation, testing
- **Database MCP** → Query dirette su DB
- **Custom MCP** → Crea i tuoi tool!

**Pattern:** Tool = capabilities che LLM non ha nativamente (I/O, execution, API calls)

---

## 📂 Gestione Contesto - I 3 Livelli

### 1. `CLAUDE.md` (Project-level)
**📍 Location:** Root del progetto
**👥 Condiviso:** Sì (committa su Git)
**📝 Contiene:**
- Architettura progetto
- Convenzioni team
- Setup instructions
- Workflow standard

**Quando usarlo:** Contesto che TUTTI nel team devono conoscere

---

### 2. `CLAUDE.local.md` (Developer-level)
**📍 Location:** Root del progetto
**👥 Condiviso:** No (gitignore!)
**📝 Contiene:**
- Preferenze personali
- Environment locale
- Shortcut personali
- Note private

**Quando usarlo:** Contesto specifico per TE, non per il team

---

### 3. `~/.claude/CLAUDE.md` (Cross-project)
**📍 Location:** Home directory
**👥 Condiviso:** No (locale)
**📝 Contiene:**
- Stile coding personale
- Convenzioni trasversali
- Tool preferences
- Pattern riutilizzabili

**Quando usarlo:** Regole che valgono per TUTTI i tuoi progetti

---

## 🚀 Comandi Essenziali

### `/init` - Inizializzazione Progetto
```bash
# Claude analizza la codebase e crea:
- CLAUDE.md          → Contesto progetto
- CLAUDE.local.md    → Template locale
- ~/.claude/CLAUDE.md → Aggiorna cross-project (se serve)
```

**Best practice:** Esegui `/init` all'inizio di ogni nuovo progetto o quando onboardi un nuovo dev.

---

### `@` - Citare Fonti nel Contesto
```
@file.ts           → Cita un file specifico
@docs/architecture → Cita una cartella
@https://...       → Cita un URL
```

**Quando usare:**
✅ Task che richiede info specifiche da un file
❌ Non overload il contesto con file non necessari

---

### `Ricorda X` - Memoria Persistente
```
"Ricorda che usiamo sempre TDD in questo progetto"
"Ricorda di chiedere conferma prima di push"
```

**Salva in:** `~/.claude/CLAUDE.md` (cross-project memory)

**Best practice:** Usa per preferenze che valgono sempre, non per info temporanee.

---

## 🎯 Context Management - La Regola d'Oro

```
Contesto Perfetto = Minimo Necessario per Task Specifico
```

| Troppo Poco | Giusto | Troppo |
|-------------|--------|--------|
| Claude indovina | Claude sa esattamente | Claude si confonde |
| Risultati vaghi | Risultati precisi | Risultati generici |
| "Serve più info" | ✅ | "Non so cosa è importante" |

### 📐 Come Trovare il Giusto Contesto

**Domande da farti:**
1. Quali file/directory servono per questo task?
2. Quali convenzioni deve seguire?
3. Quali vincoli ha il progetto?
4. Cosa NON serve? (escludilo!)

**Esempio Pratico:**
```
❌ "Leggi tutta la repo e fixxa il bug"
   → Troppo generico, contesto enorme

✅ "@src/auth/login.ts c'è un bug al login con email invalide.
    Ricorda che usiamo Zod per validation."
   → Contesto mirato, task chiaro
```

---

## 💡 Pattern Comuni

### Pattern 1: Feature Development
```
1. /init (se nuovo progetto)
2. @CLAUDE.md per capire architettura
3. @relevant-files per contesto specifico
4. Sviluppa feature
5. Aggiorna CLAUDE.md se serve
```

### Pattern 2: Bug Fix
```
1. @file-con-bug
2. @test-file (per capire expected behavior)
3. Descrivi bug + expected vs actual
4. Fix + test
```

### Pattern 3: Refactoring
```
1. @files-da-refactorare
2. @CLAUDE.md (per convenzioni)
3. "Ricorda di mantenere test coverage"
4. Refactor graduale
```

---

## ⚙️ Modalità & Configurazione

### Shift + Tab - Cambio Modalità
**Quick switch** tra configurazioni:

| Opzione | Scelta |
|---------|--------|
| **Modello** | Sonnet, Opus, Haiku |
| **Thinking Mode** | On/Off + intensità |
| **Complessità** | Low, Medium, High reasoning |

**Quando usare:**
- Task complesso → Opus + Thinking High
- Task semplice/veloce → Haiku + Thinking Off
- Balance → Sonnet (default)

---

### 📸 Screenshot con Ctrl+V
```
Ctrl+V → Paste screenshot direttamente in chat
```

**Use cases:**
- UI bug → Screenshot + "Fix this layout"
- Design mockup → "Implementa questo design"
- Error console → "Debug questo errore"

**Tip:** Claude vede l'immagine, capisce contesto visivo → boost enorme!

---

### 🧠 Planning Mode + Thinking Mode

**Combo potente per problemi complessi:**

```
1. Attiva Planning Mode
2. Chiedi a Claude di abilitare Thinking
3. Specifica intensità (low/medium/high)
4. Indica i punti critici dove fermarsi per review
```

**Esempio:**
```
"Usa planning mode con thinking intensity high.
Fermati dopo:
1. Analisi architettura
2. Design componenti
3. Prima di implementare"
```

**Risultato:** Claude ragiona step-by-step, ti mostra il processo, ti fa validare prima di procedere.

---

## 🎛️ Controllo Flusso & Contesto

### Comandi di Controllo Rapidi

| Comando | Azione | Quando usare |
|---------|--------|--------------|
| **ESC** | Interrompe Claude | Output sbagliato, vuoi fermarlo |
| **# + Ricorda** | Interrompe + memorizza | "Fermati! Ricorda di usare async/await" |
| **ESC + ESC** | Rewind conversazione | Torna indietro a un punto precedente |
| **/compact** | Riassume conversazione | Contesto pieno, vuoi continuare |
| **/clear** | Pulisce contesto | Ricomincia da zero |

**Pro tip:** `# Ricorda` è potentissimo per correzioni al volo senza perdere flusso.

---

## 🔧 Custom Commands

### Creare Comandi Personalizzati

**Location:** `~/.claude/commands/`

**Formato:** File `.md` con nome comando

```markdown
# nome-comando.md

Descrizione del comando.

Può accettare argomenti: {arg1}, {arg2}

Esempio comportamento...
```

**Uso:**
```
/nome-comando arg1 arg2
```

**Esempi pratici:**
- `/review-pr` → Analizza PR corrente
- `/test-coverage` → Verifica coverage
- `/deploy-checklist` → Checklist pre-deploy
- `/refactor {file}` → Refactoring guidato

**Best practice:** Comandi per workflow ripetitivi!

---

## 🔌 MCP Servers - Superpoteri Estensibili

### Cos'è un MCP Server
**Model Context Protocol Server** = estensione che aggiunge capabilities a Claude.

**Tipi:**
- **Locali:** Girano sulla tua macchina (es. Playwright)
- **Remoti:** API esterne (es. GitHub, ADO, Jira)

### Setup (Semplice!)
```bash
# Esempio: GitHub MCP
npm install -g @anthropic/mcp-server-github

# Configurazione in ~/.claude/config.json
{
  "mcpServers": {
    "github": {
      "command": "mcp-server-github",
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

**Riavvia Claude → MCP attivo!**

### MCP Servers Popolari

| Server | Capability | Use Case |
|--------|-----------|----------|
| **GitHub** | Issues, PR, Actions | Workflow dev completo |
| **Azure DevOps** | Work Items, Pipelines | Microsoft stack |
| **Playwright** | Browser automation | Testing E2E |
| **Database** | Query dirette | Debug DB |
| **Filesystem** | File operations avanzate | Bulk operations |

**Richiesta esempio:**
```
"Usa il browser per testare il login su localhost:3000"
→ Claude usa Playwright MCP
```

---

## 🤖 Workflow Automatizzato - Il Caso d'Uso Killer

### Scenario: Da Work Item a Produzione (Semi-Automatico)

```
[Funzionale]  →  Apre Work Item ADO
                 "Fix bug login email validation"

[Programmatore]  →  Arricchisce descrizione
                    Lancia Claude con MCP ADO + GitHub

[Claude]  →  1. Legge Work Item
             2. Analizza codebase (context)
             3. Crea branch da develop
             4. Implementa fix + test
             5. Commit + push
             6. Apre PR
             7. Lancia pipeline CI

[Pipeline]  →  Build + Test automatici

[Funzionale]  →  Test E2E manuale (o Playwright MCP)

[Programmatore]  →  ✅ Approva PR  ← CONTROLLO UMANO

[Claude]  →  8. Merge PR
             9. Chiude Work Item
             10. Aggiorna documentazione
```

**Risultato:** 80% del lavoro meccanico automatizzato, umano controlla solo i punti critici.

---

### Perché Funziona

| Componente | Ruolo |
|------------|-------|
| **ADO MCP** | Legge/scrive Work Items |
| **GitHub MCP** | Gestisce repo, PR, Actions |
| **Playwright MCP** | Testa UI automaticamente |
| **Claude Code** | Scrive codice + test |
| **Umano** | Valida punti critici (PR, deploy) |

**Key insight:** Automazione con controllo umano nei punti che contano.

---

### Applicazioni Pratiche (Per I Tuoi Progetti)

#### Senior Engineer P1-P6
```
WI: "Add task priority feature"
→ Claude: implements + tests + PR
→ Tu: review + approve
→ Deploy automatico
```

#### Architect Quest
```
ADR: "Serve scegliere database per P2"
→ Claude: research + draft ADR
→ Tu: valuti opzioni + approvi
→ Claude: implementa setup
```

#### Maintenance
```
Dependabot: "Aggiorna package X"
→ Claude: update + test + PR
→ Pipeline: test passano
→ Auto-merge (se configurato)
```

---

## 🪝 Hooks - Automazione Avanzata

### Cos'è un Hook
**Hook** = Comando eseguito automaticamente **prima** o **dopo** certe operazioni di Claude.

**Location:** `~/.claude/hooks/`

### Configurazione Hook

Quando crei un hook, devi decidere:

| Aspetto | Scelta | Esempio |
|---------|--------|---------|
| **Timing** | Pre o Post operazione | Post-Edit, Pre-Bash |
| **Tool Target** | Quali tool triggerano | Edit, Write, Bash |
| **Command** | Cosa eseguire | `npm run tsc`, `eslint` |
| **Feedback** | Che tipo di risposta | Error, Warning, Info |

### Implementazione Hook

**Componenti:**
1. **Matcher** - Definisce quando il hook si attiva
2. **Command** - Cosa viene eseguito

**Esempio: TypeScript Validation Post-Edit**
```json
{
  "name": "typescript-check",
  "trigger": "post",
  "tools": ["Edit", "Write"],
  "matcher": "**/*.ts",
  "command": "npm run tsc --noEmit",
  "feedback": "error"
}
```

**Cosa fa:**
- Claude modifica file `.ts` → Hook si attiva
- Esegue `tsc` per check errori
- Se errori → Claude li vede e può fixare

---

### Pattern Hooks Comuni

#### 1. Code Quality
```json
// Post-Edit: Linting
{
  "trigger": "post",
  "tools": ["Edit", "Write"],
  "matcher": "**/*.{ts,js}",
  "command": "npm run lint",
  "feedback": "warning"
}
```

#### 2. Duplicate Detection
```json
// Post-Edit: Controllo duplicazione
{
  "trigger": "post",
  "tools": ["Edit"],
  "command": "jscpd --threshold 5",
  "feedback": "warning"
}
```

#### 3. Test Automation
```json
// Post-Edit: Run tests
{
  "trigger": "post",
  "tools": ["Edit", "Write"],
  "matcher": "**/src/**",
  "command": "npm test",
  "feedback": "error"
}
```

#### 4. Build Validation
```json
// Post-Edit: TypeScript compilation
{
  "trigger": "post",
  "tools": ["Edit", "Write"],
  "matcher": "**/*.ts",
  "command": "npm run build",
  "feedback": "error"
}
```

---

### 🤖 Claude SDK - Hooks Avanzati

**Pattern Killer:** Hook che interpella Claude stesso!

```javascript
// hook-script.js
import Anthropic from '@anthropic-ai/sdk';

const claude = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

// Esempio: Code review automatico
async function reviewCode(filePath) {
  const code = readFile(filePath);

  const response = await claude.messages.create({
    model: 'claude-sonnet-4-5',
    messages: [{
      role: 'user',
      content: `Review this code for issues:\n\n${code}`
    }]
  });

  return response.content;
}
```

**Hook configuration:**
```json
{
  "trigger": "post",
  "tools": ["Edit"],
  "command": "node hook-script.js {filePath}",
  "feedback": "info"
}
```

**Risultato:** Claude edita file → Hook chiama ALTRO Claude per review → Feedback immediato!

---

### Use Cases Avanzati

#### 1. Multi-Stage Validation
```
Claude edita → Hook 1: tsc
              → Hook 2: eslint
              → Hook 3: test
              → Hook 4: Claude review (SDK)
→ Feedback aggregato a Claude principale
```

#### 2. AI-Powered Code Review
```
Claude scrive feature → Hook: altra sessione Claude
                      → Analizza per security, performance, best practices
                      → Suggerimenti back al Claude principale
```

#### 3. Documentation Auto-Generation
```
Claude edita API → Hook: Claude SDK
                 → Genera/aggiorna docs automaticamente
                 → Commit docs insieme al codice
```

#### 4. Compliance Checks
```
Claude modifica → Hook: Claude SDK
                → Verifica compliance (GDPR, security standards)
                → Blocca se non conforme
```

---

### Best Practices Hooks

#### ✅ Do
- **Feedback rapido** - Hook veloci (<5s quando possibile)
- **Errori chiari** - Feedback comprensibile per Claude
- **Selective matching** - Solo file/tool rilevanti
- **Idempotent** - Hook eseguibile multiple volte safely

#### ❌ Don't
- **Hook lenti** - Evita operazioni che bloccano (>30s)
- **Troppi hook** - Max 3-5 per non rallentare
- **Feedback verboso** - Claude si confonde con troppo output
- **Side effects pericolosi** - No deploy, no delete in hook

---

### Pattern: Test-Driven Development con Hooks

**Setup:**
```json
{
  "name": "tdd-workflow",
  "trigger": "post",
  "tools": ["Edit", "Write"],
  "matcher": "**/src/**",
  "command": "npm test -- --watch=false",
  "feedback": "error"
}
```

**Workflow:**
1. Claude scrive codice
2. Hook esegue test
3. Test falliscono → Claude vede errori
4. Claude fixa automaticamente
5. Repeat fino a green ✅

**Risultato:** TDD loop automatico!

---

### 🔗 Hooks + MCP = Superpotere

**Combo killer:**
- **MCP GitHub** - Gestisce repo
- **Hook post-commit** - Review automatico via Claude SDK
- **MCP ADO** - Update work item con risultati

**Workflow completo:**
```
Claude code → Commit (MCP GitHub)
           → Hook: Claude SDK review
           → If OK: Push + Update WI (MCP ADO)
           → If issues: Claude fixa → Repeat
```

---

## 💡 Insights di Dan (Parte 3)

> "Hooks = CI/CD integrato direttamente in Claude! No more context switching per vedere se il build passa"

> "Hook che chiama Claude SDK = inception level! Claude che review sé stesso 🤯"

> "Pattern TDD con hook è geniale - test automatici ad ogni modifica, Claude fixa da solo se falliscono"

---

## 💡 Insights di Dan (Parte 2)

> "Shift+Tab per cambiare modello al volo è geniale - task semplici con Haiku risparmio tempo e costi"

> "Il workflow ADO → Claude → GitHub è impressionante. Potrei automatizzare 70% del lavoro ripetitivo"

> "ESC+ESC per rewind è come Ctrl+Z per conversazioni - game changer!"

---

## 🔗 Collegamenti

### Concetti Correlati
- [[mcp-introduction]] - Model Context Protocol deep dive
- [[prompt-engineering]] - Come strutturare request efficaci
- [[ai-workflow]] - Workflow AI-assisted completo

### Applicabile a Progetti
- **Senior Engineer P1-P6** - Setup CLAUDE.md per ogni progetto
- **Architect Quest** - Context management per sistemi complessi
- **AI Track** - MCP custom per progetti AI

---

## 💭 Insights di Dan

> "Il Coding Assistant è come un intermediario intelligente tra me e il cervello dell'AI"

> "Gestire bene il contesto = risultati precisi. Troppo o troppo poco = confusione."

---

## 🧠 Quiz

### Q1: Architettura - Coding Assistant vs LLM
Hai un Language Model che sa rispondere a prompt. Perché serve un Coding Assistant invece di usare direttamente il LLM per coding?

<details>
<summary>Risposta</summary>

**Risposta:** Il LLM da solo può solo leggere/scrivere testo. Il Coding Assistant aggiunge:
1. **Tool** (read/write file, bash, etc.) - capacità che l'LLM non ha
2. **Context management** strutturato (CLAUDE.md, @file, etc.)
3. **Workflow specializzati** per coding tasks
4. **Estensibilità** (MCP per custom tool)

**Analogia:** LLM = cervello intelligente, Coding Assistant = corpo con mani e strumenti.

</details>

---

### Q2: Context Management - I 3 Livelli
Stai lavorando su un progetto team. Hai una preferenza personale per usare `async/await` invece di `.then()`. Dove la metti?

A) `CLAUDE.md` (project-level)
B) `CLAUDE.local.md` (developer-level)
C) `~/.claude/CLAUDE.md` (cross-project)

<details>
<summary>Risposta</summary>

**Risposta:** **C) `~/.claude/CLAUDE.md`**

**Perché:**
- È una preferenza **personale** (non del team) → Non va in `CLAUDE.md`
- Vale per **tutti i tuoi progetti** (non solo questo) → Va in cross-project
- `CLAUDE.local.md` sarebbe OK, ma dovresti riscriverla per ogni progetto

**Regola:** Preferenze personali trasversali = `~/.claude/CLAUDE.md`

</details>

---

### Q3: Context Management - Troppo vs Giusto
Devi fixare un bug nel login (file `auth/login.ts`). Quale approccio è migliore?

A) `"Leggi tutta la cartella src/ e fixa il bug"`
B) `"@auth/login.ts c'è un bug quando l'email è invalida. @auth/validation.ts mostra le regole. Fixa il bug."`
C) `"Fixa il bug nel login"`

<details>
<summary>Risposta</summary>

**Risposta:** **B**

**Perché:**
- **A** = Troppo contesto → Claude si confonde, non sa cosa è rilevante
- **C** = Troppo poco → Claude non sa dove guardare, deve indovinare
- **B** = Giusto contesto → File specifici + descrizione chiara del problema

**Regola d'Oro:** Contesto = minimo necessario per il task specifico.

</details>

---

### Q4: Modalità & Modelli - Task Matching
Devi fare un quick refactoring di 3 linee (rinominare variabile). Quale configurazione è più appropriata?

A) Opus + Thinking Mode High
B) Sonnet + Thinking Mode Medium
C) Haiku + Thinking Mode Off

<details>
<summary>Risposta</summary>

**Risposta:** **C) Haiku + Thinking Mode Off**

**Perché:**
- Task **semplice** (rename variabile) → Non serve ragionamento complesso
- **Haiku** = Più veloce + economico, perfetto per task straightforward
- **Thinking Off** = Zero overhead, risposta immediata
- Opus/Sonnet sarebbero overkill per questo task

**Regola:** Match complessità task con potenza modello.
- Simple/Quick → Haiku
- Medium complexity → Sonnet
- Complex reasoning → Opus + Thinking

</details>

---

### Q5: MCP Servers - Workflow Automation
Nel workflow automatizzato `ADO → Claude → GitHub → Pipeline`, qual è il ruolo critico dell'umano?

A) Scrivere il codice manualmente
B) Validare la PR prima del merge
C) Lanciare la pipeline CI
D) Chiudere il Work Item

<details>
<summary>Risposta</summary>

**Risposta:** **B) Validare la PR prima del merge**

**Perché:**
- **A** = Sbagliato, Claude scrive il codice
- **B** = ✅ Corretto! L'umano deve **controllare** prima che vada in prod
- **C** = Sbagliato, pipeline si lancia automaticamente al push
- **D** = Sbagliato, Claude può chiuderlo automaticamente

**Key insight:** Automazione ≠ zero controllo. L'umano valida i **punti critici** (codice che va in prod), non le parti meccaniche (commit, push, WI admin).

**Pattern:**
```
Claude = lavoro meccanico (80%)
Umano = decisioni critiche (20%)
```

</details>

---

### Q6: Controllo Flusso - Correzione al Volo
Claude sta generando codice ma sta usando `.then()` invece di `async/await` che preferisci. Cosa fai?

A) ESC → Ricomincia da zero
B) # Ricorda che preferisco async/await
C) Aspetti che finisca, poi chiedi di rifare
D) /clear e riparti

<details>
<summary>Risposta</summary>

**Risposta:** **B) # Ricorda che preferisco async/await**

**Perché:**
- **A** = Troppo drastico, perdi tutto il progresso
- **B** = ✅ Perfetto! Interrompi al volo + correggi + Claude memorizza
- **C** = Spreco di tempo, aspetti inutilmente
- **D** = Overkill, pulisci tutto il contesto

**Pro tip:** `# Ricorda` è il comando più potente per correzioni real-time senza perdere flusso.

**Pattern:**
```
Claude genera... → Vedi errore → # Ricorda X → Claude corregge + memorizza
```

Questo viene salvato in `~/.claude/CLAUDE.md` per sessioni future!

</details>

---

### Q7: Hooks - Timing & Configuration
Vuoi che TypeScript venga controllato DOPO che Claude modifica file .ts. Come configuri l'hook?

A) `trigger: "pre", tools: ["Edit"], command: "tsc"`
B) `trigger: "post", tools: ["Edit", "Write"], matcher: "**/*.ts", command: "npm run tsc"`
C) `trigger: "post", tools: ["Bash"], command: "tsc"`

<details>
<summary>Risposta</summary>

**Risposta:** **B**

**Perché:**
- **Trigger "post"** → Dopo la modifica (non prima)
- **Tools ["Edit", "Write"]** → Su entrambi edit E nuovi file
- **Matcher "**/*.ts"** → Solo file TypeScript
- **Command corretto** → `npm run tsc` (con npm script)

**A è sbagliato:** trigger "pre" controlla PRIMA della modifica
**C è sbagliato:** "Bash" non è il tool giusto (Edit/Write modificano file)

**Pattern:** Post-hook su file-modifying tools con matcher specifico.

</details>

---

### Q8: Claude SDK - Hook Inception
Hai un hook che chiama Claude SDK per fare code review. Qual è il vantaggio rispetto a un normale linter?

A) È più veloce
B) Capisce il contesto semantico del codice
C) Non richiede configurazione
D) Costa meno

<details>
<summary>Risposta</summary>

**Risposta:** **B) Capisce il contesto semantico del codice**

**Perché:**
- **Linter** = regole sintattiche fisse (stile, pattern noti)
- **Claude SDK review** = comprende logica, business rules, architettura

**Esempio:**
```typescript
// Linter: ✅ Sintassi OK
function processPayment(amount) {
  // Ma logicamente: manca validazione, error handling, logging
}

// Claude review: ⚠️ "Manca validazione amount, error handling,
// considera idempotency per payments"
```

**A, C, D sono sbagliati:**
- Claude SDK è **più lento** (API call)
- Richiede **più configurazione** (API key, prompt)
- **Costa di più** (token usage)

**Ma:** Feedback qualitativamente superiore per logic/architecture issues.

</details>

---

### Q9: Hooks Best Practices - Quando NON Usarli
Quale di questi NON dovrebbe essere un hook?

A) `npm run tsc` post-edit TypeScript
B) `git push` post-commit
C) `eslint` post-edit JavaScript
D) `npm test` post-edit src files

<details>
<summary>Risposta</summary>

**Risposta:** **B) `git push` post-commit**

**Perché:**
- **Hook = validazione/feedback**, non side effects critici
- `git push` è **irreversibile** e **bloccante**
- Se hook fallisce dopo push → problema
- Push dovrebbe essere **decisione esplicita** dell'utano/Claude

**A, C, D sono OK:**
- tsc, eslint, test = **validazione** → feedback a Claude
- Claude può **fixare** se falliscono
- Non side effects permanenti

**Best Practice:**
```
✅ Hooks per: validation, linting, testing, analysis
❌ Hooks per: deploy, push, delete, production changes

Controllo umano su azioni irreversibili!
```

</details>

---

## 📚 Risorse per Approfondire

### Ufficiali
- **[Claude Code Docs](https://docs.anthropic.com/claude/docs/claude-code)** - Documentazione completa
- **[MCP Specification](https://github.com/anthropics/mcp)** - Model Context Protocol spec
- **[Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use)** - Come funzionano i tool

### Community
- **[MCP Servers Collection](https://github.com/topics/mcp-server)** - MCP servers open source
- **[Claude Code Examples](https://github.com/anthropics/anthropic-cookbook)** - Cookbook ufficiale
- **[Azure DevOps MCP Server](https://github.com/microsoft/ado-mcp-server)** - Microsoft ADO integration
- **[Hook Examples Repo](https://github.com/anthropics/claude-hooks)** - Hook configurations examples

### Video & Talks
- **[Building with MCP](https://www.youtube.com/anthropic)** - Tutorial ufficiali MCP

### SDK & API
- **[@anthropic-ai/sdk](https://www.npmjs.com/package/@anthropic-ai/sdk)** - NPM package ufficiale
- **[API Reference](https://docs.anthropic.com/claude/reference)** - API documentation completa

---

## 🎯 Prossimi Passi

### Basics (Già coperto ✅)
- [ ] Prova `/init` su un tuo progetto esistente
- [ ] Crea `~/.claude/CLAUDE.md` con le tue preferenze
- [ ] Sperimenta con `@file` per capire impatto sul contesto

### Advanced (Nuovi obiettivi 🚀)
- [ ] Setup MCP GitHub per Senior Engineer P1
- [ ] Crea 2-3 custom commands per workflow ripetitivi
- [ ] Sperimenta Shift+Tab per task diversi (Haiku vs Sonnet)
- [ ] Prova Planning Mode + Thinking per problema complesso
- [ ] Testa workflow semi-automatizzato: WI → Claude → PR

### Hooks & Automation (NUOVO! 🪝)
- [ ] Setup hook `tsc` post-edit TypeScript
- [ ] Hook `eslint` per code quality
- [ ] Hook `npm test` per TDD workflow
- [ ] Esperimento: Claude SDK hook per code review
- [ ] Pattern: Hook chain (tsc → lint → test)

### Ambitious (Quando pronto 💎)
- [ ] Workflow completo ADO/GitHub con MCP
- [ ] Custom MCP server per need specifico
- [ ] Hook avanzato: Claude review via SDK
- [ ] Full automation: WI → Code → Hook validation → PR → Deploy

---

*Created: 2026-03-13*
*Updated: 2026-03-13 (Parte 3 - CORSO COMPLETATO! 🎉)*
*Lessons: 1-8 (COMPLETE)*
*Quiz IDs: CLCODE-01 through CLCODE-09*
*Test Finale: 8/8 ✅ PERFECT SCORE*
