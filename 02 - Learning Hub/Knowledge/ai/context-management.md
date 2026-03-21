---
tags:
  - ai
  - claude
  - anthropic
  - from/course-claude-code
  - status/learning
aliases:
  - CLAUDE.md 3 Levels
  - Context Management Claude Code
created: 2026-03-13
updated: 2026-03-18
source: "Claude Code in Action - Lessons 1-2 + Anthropic Docs"
---

# Context Management - I 3 Livelli

> **One-liner:** Il contesto in Claude Code si gestisce su 3 livelli gerarchici (progetto, locale, globale) seguendo la regola d'oro: fornire il minimo necessario per il task specifico.

## Cos'e

Claude Code legge automaticamente file `CLAUDE.md` per ottenere contesto persistente. Esistono 3 livelli con scope diversi:

### Livello 1: `CLAUDE.md` (Project-level)
- **Dove:** Root del progetto (e sotto-cartelle)
- **Condiviso:** Si, committato su Git
- **Contiene:** Architettura, convenzioni team, setup, workflow standard
- **Quando:** Contesto che TUTTI nel team devono conoscere

### Livello 2: `CLAUDE.local.md` (Developer-level)
- **Dove:** Root del progetto
- **Condiviso:** No (in `.gitignore`)
- **Contiene:** Preferenze personali, environment locale, note private
- **Quando:** Contesto specifico per te, non per il team

### Livello 3: `~/.claude/CLAUDE.md` (Cross-project)
- **Dove:** Home directory
- **Condiviso:** No (locale)
- **Contiene:** Stile coding personale, convenzioni trasversali, tool preferences
- **Quando:** Regole che valgono per TUTTI i tuoi progetti

### La Regola d'Oro

```
Contesto Perfetto = Minimo Necessario per il Task Specifico
```

| Troppo Poco | Giusto | Troppo |
|-------------|--------|--------|
| Claude indovina | Claude sa esattamente cosa fare | Claude si confonde |
| Risultati vaghi | Risultati precisi | Perde focus |

### Altri meccanismi di contesto

- **`@file`** — Cita un file specifico nel prompt
- **`@folder`** — Cita un'intera cartella
- **`@url`** — Cita contenuto web
- **Auto-memory** — Claude salva automaticamente apprendimenti tra sessioni (build commands, debugging insights)
- **`# Ricorda X`** — Interrompi Claude e salva una preferenza in memoria persistente

## Quando usarlo

- **CLAUDE.md**: Setup iniziale di ogni progetto (5 min, ROI enorme ~16x)
- **CLAUDE.local.md**: Quando hai preferenze diverse dal team (es. path custom, env vars)
- **~/.claude/CLAUDE.md**: Preferenze personali che valgono ovunque (es. "preferisco async/await")
- **@file/@folder**: Quando un task richiede contesto specifico da file precisi
- **# Ricorda**: Per correzioni al volo che devono persistere

## Quando NON usarlo

- Non mettere informazioni temporanee in CLAUDE.md (usa prompt diretto)
- Non sovraccaricare il contesto con file non necessari (sintomo: risposte generiche)
- Non duplicare info tra i 3 livelli (metti ogni cosa al livello giusto)
- Non usare `@` su intere cartelle grandi — seleziona solo i file rilevanti

## Esempio

```bash
# Progetto team con preferenze personali

# CLAUDE.md (committato, tutti lo vedono):
# - "Usiamo Clean Architecture con 4 layer"
# - "TDD obbligatorio, coverage minima 80%"
# - "PostgreSQL per persistence"

# CLAUDE.local.md (solo tu):
# - "Il mio DB locale e su localhost:5433"
# - "Preferisco NSubstitute per i mock"

# ~/.claude/CLAUDE.md (tutti i tuoi progetti):
# - "Preferisco async/await a .then()"
# - "Commenta in inglese"
# - "Usa early return pattern"
```

```
# Contesto mirato per un task:
❌ "Leggi tutta la repo e fixa il bug"
✅ "@src/auth/login.ts c'e un bug al login con email invalide.
    @src/auth/validation.ts mostra le regole. Fixa il bug."
```

## Collegamenti

- [[coding-assistant-vs-llm]] - Architettura del Coding Assistant
- [[claude-code-hooks]] - Automazione post-contesto
- [[mcp-servers]] - Estendere le capabilities

## Quiz

### Q1: Dove mettere una preferenza personale cross-project? (CLCODE-02)
Stai lavorando su un progetto team. Hai una preferenza personale per usare `async/await` invece di `.then()`. Dove la metti?

A) `CLAUDE.md` (project-level)
B) `CLAUDE.local.md` (developer-level)
C) `~/.claude/CLAUDE.md` (cross-project)

**Mia risposta:**

---

### Q2: Contesto giusto per un bug fix (CLCODE-03)
Devi fixare un bug nel login (file `auth/login.ts`). Quale approccio e migliore?

A) "Leggi tutta la cartella src/ e fixa il bug"
B) "@auth/login.ts c'e un bug quando l'email e invalida. @auth/validation.ts mostra le regole."
C) "Fixa il bug nel login"

**Mia risposta:**

---

### Q3: Sintomi di troppo contesto (CLCODE-12)
Hai dato a Claude Code 15 file di contesto con `@` per un task semplice. Quali sono i sintomi che stai dando troppo contesto?

**Mia risposta:**

---

### Q4: /init su nuovo progetto (CLCODE-10)
Esegui `/init` su un nuovo progetto. Cosa crea automaticamente Claude Code?

**Mia risposta:**

---

## Risorse

- [Claude Code Memory & Instructions](https://code.claude.com/docs/en/memory) - Documentazione ufficiale CLAUDE.md
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) - Pattern di contesto consigliati
