---
tags:
  - ai
  - claude
  - anthropic
  - from/course-claude-code
  - status/learning
aliases:
  - Model Selection
  - Haiku vs Sonnet vs Opus
  - Task-Model Matching
created: 2026-03-13
updated: 2026-03-18
source: "Claude Code in Action - Lesson 4 + Anthropic Docs"
---

# Model Selection Strategy

> **One-liner:** Ogni task ha una complessita diversa — abbina il modello giusto (Haiku/Sonnet/Opus) alla complessita del task per ottimizzare velocita, costo e qualita.

## Cos'e

Claude Code permette di cambiare modello al volo con **Shift+Tab** (o `/model`). La famiglia Claude ha 3 tier di modelli, ciascuno ottimizzato per un diverso livello di complessita:

| Modello | Forza | Velocita | Costo | Quando |
|---------|-------|----------|-------|--------|
| **Haiku** | Task semplici, routine | Molto veloce | Basso | Rename, formatting, task meccanici |
| **Sonnet** | Balance qualita/velocita | Veloce | Medio | Feature medie, bug fix, refactoring |
| **Opus** | Ragionamento complesso | Piu lento | Alto | Architettura, debugging complesso, design |

### Thinking Mode

Combinabile con il modello per controllare la profondita di ragionamento:

| Thinking | Effetto | Quando |
|----------|---------|--------|
| **Off** | Risposta diretta, zero overhead | Task banali |
| **Medium** | Ragionamento moderato | Task standard |
| **High** | Ragionamento approfondito, step-by-step | Problemi complessi, architettura |

### Planning Mode

Modalita speciale dove Claude pianifica prima di agire:

```
1. Attiva Planning Mode
2. Claude analizza il problema
3. Mostra il piano step-by-step
4. Tu validi/correggi
5. Solo dopo OK → Claude implementa
```

**Combo potente:** Opus + Thinking High + Planning Mode = massima qualita per problemi architetturali.

### Regola pratica

```
Complessita Task   →   Modello + Thinking
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rename variabile   →   Haiku + Off
Fix bug semplice   →   Sonnet + Medium
Feature complessa  →   Sonnet + High
System design      →   Opus + High + Planning
```

**Key insight:** Usare Opus per rinominare una variabile e come usare un TIR per andare a comprare il pane — funziona, ma e uno spreco enorme.

## Quando usarlo

- **Haiku**: Rename, formatting, generazione boilerplate, task ripetitivi, quick questions
- **Sonnet**: Feature development, bug fix, refactoring, code review, la maggior parte del lavoro quotidiano
- **Opus**: Design architetturale, debugging di problemi cross-system, analisi di sicurezza, decisioni strategiche
- **Planning Mode**: Quando il task ha molte parti, rischi di fare errori, o vuoi validare l'approccio prima

## Quando NON usarlo

- Non usare Opus + Thinking High per task banali (spreco di tempo e token)
- Non usare Haiku per ragionamento complesso (qualita insufficiente, rischia errori)
- Non usare Planning Mode per task da 2 minuti (overhead non giustificato)
- Non cambiare modello continuamente durante un singolo task (mantieni consistenza)

## Esempio

```
Scenario: Giornata tipo di sviluppo

09:00 - Rinominare costanti in 3 file
        → Haiku + Thinking Off (30 secondi)

09:30 - Fixare bug nel validation middleware
        → Sonnet + Thinking Medium (5 minuti)

10:30 - Implementare nuovo endpoint CRUD
        → Sonnet + Thinking High (20 minuti)

14:00 - Decidere architettura caching layer
        → Opus + Thinking High + Planning Mode (40 minuti)

16:00 - Scrivere test per i nuovi endpoint
        → Sonnet + Thinking Medium (15 minuti)

16:30 - Fix typo nella docs
        → Haiku + Thinking Off (10 secondi)
```

## Collegamenti

- [[coding-assistant-vs-llm]] - Il modello e il "cervello" del Coding Assistant
- [[context-management]] - Il contesto influenza quanto il modello deve ragionare
- [[claude-code-hooks]] - Gli hooks funzionano con qualsiasi modello

## Quiz

### Q1: Task matching (CLCODE-04)
Devi fare un quick refactoring di 3 linee (rinominare variabile). Quale configurazione e piu appropriata?

A) Opus + Thinking Mode High
B) Sonnet + Thinking Mode Medium
C) Haiku + Thinking Mode Off

**Mia risposta:**

---

### Q2: Planning + Thinking combo (CLCODE-14)
Quando ha senso usare la combinazione Planning Mode + Thinking High? Descrivi un caso d'uso concreto.

**Mia risposta:**

---

### Q3: Costo-beneficio
Perche NON dovresti usare sempre Opus + Thinking High per tutto?

**Mia risposta:**

---

## Risorse

- [Claude Code Settings](https://code.claude.com/docs/en/settings) - Configurazione modelli
- [Claude Models](https://docs.anthropic.com/en/docs/about-claude/models) - Specifiche dei modelli
