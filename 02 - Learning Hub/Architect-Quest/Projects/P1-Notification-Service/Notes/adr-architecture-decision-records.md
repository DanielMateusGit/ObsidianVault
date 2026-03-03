---
tags:
  - p1
  - documentation
  - adr
  - architecture
  - from/week-01
  - status/learned
aliases:
  - ADR
  - Architecture Decision Records
  - Decisioni Architetturali
created: 2026-02-02
source: "Sessione Week 1 - P1 Notification Service"
---
Ï
# ADR - Architecture Decision Records

> **One-liner:** Documento breve e strutturato che cattura una decisione architetturale importante con il suo contesto, alternative considerate, e conseguenze.

---

## Cos'è

Un **Architecture Decision Record (ADR)** è un documento breve che cattura una decisione architetturale importante. Risponde alla domanda che ogni team si fa 6 mesi dopo: *"Perché abbiamo scelto X invece di Y?"*

### Il Problema che Risolve

> **6 mesi dopo:**
>
> Nuovo dev: "Perché usiamo PostgreSQL invece di MongoDB?"
> Team: "...boh, era già così"

Le decisioni architetturali si perdono. Nessuno ricorda il *perché*.

### Struttura Standard

```markdown
# ADR-XXX: Titolo della Decisione

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
Qual è il problema? Perché dobbiamo decidere?

## Decision
Cosa abbiamo deciso di fare?

## Alternatives Considered
Quali opzioni abbiamo valutato? Perché scartate?

## Consequences
- Positive: ...
- Negative: ...
- Neutral: ...
```

---

## Quando Usarlo

| Situazione | ADR? |
|------------|------|
| Scelta framework (.NET vs Node) | ✅ Sì |
| Scelta architetturale (Clean vs MVC) | ✅ Sì |
| Scelta database | ✅ Sì |
| Pattern importante (CQRS, Event Sourcing) | ✅ Sì |
| Introduzione di una dipendenza pervasiva (MediatR) | ✅ Sì |
| Cambio significativo di direzione tecnica | ✅ Sì |

**Regola:** Se tra 6 mesi qualcuno potrebbe chiedere "perché?", scrivi un ADR.

---

## Quando NON Usarlo

| NON è un ADR | Dove va invece |
|--------------|----------------|
| Naming conventions (camelCase, PascalCase) | `CODING_STANDARDS.md` o `.editorconfig` |
| Formattazione codice (tabs, spaces) | `.editorconfig`, `.prettierrc` |
| Git workflow (branch naming) | `CONTRIBUTING.md` |
| Scelta di una libreria utility minore | Code review |
| Struttura delle cartelle | `README.md` o `ARCHITECTURE.md` |
| Aggiungere un campo senza impatto architetturale | Nessun documento |
| Nome variabile | ❌ No |

**ADR ≠ Documentazione di ogni decisione. Solo quelle architetturali.**

---

## Esempio

### ADR-001: Clean Architecture

```markdown
# ADR-001: Adozione Clean Architecture

## Status
Accepted

## Context
Stiamo costruendo un Notification Service che dovrà:
- Durare anni
- Supportare cambi di provider (SendGrid → Mailgun)
- Essere testabile senza infrastruttura

## Decision
Adottiamo Clean Architecture con 4 layer:
- Domain, Application, Infrastructure, Api

## Alternatives Considered
- **MVC tradizionale**: Più semplice ma meno testabile
- **Vertical Slices**: Interessante ma team non ha esperienza

## Consequences
- Positive: Testabilità, sostituibilità provider
- Negative: Più setup iniziale, learning curve
- Neutral: Più file da creare
```

### Granularità

| Decisione | Dove va? |
|-----------|----------|
| "Usiamo PostgreSQL" | ✅ **ADR** |
| "Usiamo Clean Architecture" | ✅ **ADR** |
| "Le variabili usano camelCase" | ❌ `CODING_STANDARDS.md` |
| "I commit seguono Conventional Commits" | ❌ `CONTRIBUTING.md` |

---

## Frequenza degli ADR

**Ogni evolutiva = nuovo ADR? NO!**

| Tipo di Cambiamento | ADR? |
|---------------------|------|
| Aggiungo un nuovo endpoint CRUD | ❌ No |
| Aggiungo un nuovo canale seguendo pattern esistente | ❌ No |
| **Cambio** da REST a GraphQL | ✅ Sì |
| Refactoring interno senza cambiare architettura | ❌ No |
| **Introduco** Event Sourcing | ✅ Sì |

**In un progetto tipico:**
- 10 evolutive → probabilmente 1-2 ADR
- 100 evolutive → probabilmente 5-10 ADR

---

## Perché Sono Importanti per un Architect

Come **System Architect**, documenti le decisioni per:

- **Evitare discussioni ripetute** - "Abbiamo già valutato X"
- **Onboarding veloce** - Nuovi dev capiscono il ragionamento
- **Portfolio** - Mostra il tuo processo decisionale
- **Rivalutazione** - Quando il contesto cambia, puoi rivedere

---

## Collegamenti

- [[clean-architecture]] - Esempio di decisione architetturale da documentare
- [[c4-model]] - C4 + ADR = documentazione completa

---

## Domande dalla Sessione

### D: Hai un progetto dove devi scegliere tra PostgreSQL o MongoDB. Scriveresti un ADR?

**R:** Sì! Scelta del database = decisione architetturale importante. Tra 6 mesi qualcuno chiederà "perché PostgreSQL e non MongoDB?" - l'ADR risponde.

---

### D: Un collega propone di modificare un ADR esistente (ADR-003) perché la situazione è cambiata. È corretto modificarlo?

**R:** No! Gli ADR sono **immutabili**. Se la situazione cambia:
- Crei ADR-004 con `Status: Accepted`
- ADR-003 diventa `Status: Superseded by ADR-004`
- Così hai lo **storico** delle decisioni

---

### D: Il team decide di passare da xUnit a NUnit per i test. È un ADR?

**R:** Dipende dal contesto:
- Progetto piccolo, pochi test → Probabilmente no
- Progetto enterprise, 5000 test, team di 15 → Sì

**Regola:** Più grande l'impatto, più serve l'ADR.

---

### D: Decidi di usare MediatR per implementare CQRS. È un ADR?

**R:** Sì! MediatR diventa dipendenza **pervasiva** (ogni command/query lo usa). Cambiare da MediatR ad altro = refactoring massiccio. Influenza come tutto il team scrive codice.

---

## Quiz

### Q1: Un campo "priority" all'entità Notification. È un ADR?

<details>
<summary>Risposta</summary>

**Dipende!**
- `Priority` come campo informativo (solo display) → ❌ No
- `Priority` + priority queue con algoritmi di scheduling → ✅ Sì

La chiave: Non è il campo in sé, è l'**impatto architetturale** che ne deriva.

</details>

---

### Q2: Gli ADR sono modificabili?

<details>
<summary>Risposta</summary>

**No!** Gli ADR sono **immutabili**. Se la situazione cambia, crei un nuovo ADR che **supersedes** il precedente. Così mantieni lo storico completo delle decisioni.

</details>

---

### Q3: Qual è la differenza principale tra un ADR e un documento di design tradizionale?

<details>
<summary>Risposta</summary>

- **Formato standard** → tutti sanno dove trovare le info
- **Brevità** → si legge in 5 minuti, non in 2 ore
- **Focalizzato** → una decisione = un ADR
- **Immutabile** → storico preservato

</details>

---

### Q4: Naming conventions vanno in un ADR?

<details>
<summary>Risposta</summary>

**No!** Le naming conventions vanno in `CODING_STANDARDS.md` o `.editorconfig`. Gli ADR sono per decisioni **architetturali**, non per convenzioni di codice.

</details>

---

## Risorse per Approfondire

- **[Documenting Architecture Decisions - Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)** - L'articolo originale che ha definito il formato ADR. Fondamentale.

- **[ADR GitHub Organization](https://adr.github.io/)** - Template, esempi, e tool per gestire ADR.

- **[Architecture Decision Records in Action - InfoQ](https://www.infoq.com/articles/architecture-decision-records/)** - Casi d'uso reali e best practices.

- **[adr-tools](https://github.com/npryce/adr-tools)** - CLI per creare e gestire ADR da terminale.

- **Libro: "Documenting Software Architectures" - Clements et al.** - Trattazione completa della documentazione architetturale.

---

*Creata: 2026-02-02*
*Argomenti: ADR, Architecture Decision Records, Documentazione, Decisioni Architetturali*
