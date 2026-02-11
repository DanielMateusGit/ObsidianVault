# ADR - Architecture Decision Records

> **Data:** 2026-02-02
> **Sessione:** Week 1

---

## Cos'è un ADR?

Un **Architecture Decision Record** è un documento breve che cattura una decisione architetturale importante.

### Il Problema che Risolve

> **6 mesi dopo:**
>
> Nuovo dev: "Perché usiamo X invece di Y?"
> Team: "...boh, era già così"

Le decisioni architetturali si perdono. Nessuno ricorda il *perché*.

---

## Struttura Standard

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

## QUANDO Scrivere un ADR?

| Situazione | ADR? |
|------------|------|
| Scelta framework (.NET vs Node) | ✅ Sì |
| Scelta architetturale (Clean vs MVC) | ✅ Sì |
| Scelta database | ✅ Sì |
| Nome variabile | ❌ No |
| Pattern importante (CQRS, Event Sourcing) | ✅ Sì |

**Regola:** Se tra 6 mesi qualcuno potrebbe chiedere "perché?", scrivi un ADR.

---

## QUANDO NON Scrivere un ADR?

| NON è un ADR | Dove va invece |
|--------------|----------------|
| Naming conventions (camelCase, PascalCase) | `CODING_STANDARDS.md` o `.editorconfig` |
| Formattazione codice (tabs, spaces, line length) | `.editorconfig`, `.prettierrc` |
| Git workflow (branch naming, commit format) | `CONTRIBUTING.md` |
| Scelta di una libreria utility minore | Code review, nessun documento |
| Struttura delle cartelle nel progetto | `README.md` o `ARCHITECTURE.md` |
| Come scrivere i test | `TESTING.md` o `CONTRIBUTING.md` |
| Configurazione CI/CD | Documentazione inline nel file YAML |
| Aggiungere un campo a un'entità (senza impatto architetturale) | Nessun documento |
| Nuova feature che segue pattern esistenti | Nessun documento |

**Struttura consigliata per documentazione:**
```
docs/
├── adr/                    ← Decisioni ARCHITETTURALI
├── CODING_STANDARDS.md     ← Convenzioni di codice
├── CONTRIBUTING.md         ← Come contribuire
└── ARCHITECTURE.md         ← Overview architettura

Root:
├── .editorconfig           ← Formattazione
└── .prettierrc             ← Formattazione JS/TS
```

---

## Pattern di Codice: Vanno in ADR?

**Dipende dal contesto:**

| Situazione | ADR? | Perché |
|------------|------|--------|
| "Uso Strategy per i canali di notifica (email, SMS, push)" | ✅ Sì | Decisione che impatta la struttura del sistema |
| "Uso Strategy in questo singolo metodo per calcolare lo sconto" | ❌ No | Scelta locale di implementazione |

**Regola pratica:**
- Pattern che influenza **come è strutturato il sistema** → ADR
- Pattern come **scelta locale di implementazione** → Code review / commenti

---

## Frequenza degli ADR

**Ogni evolutiva = nuovo ADR? NO!**

| Tipo di Cambiamento | ADR? |
|---------------------|------|
| Aggiungo un nuovo endpoint CRUD | ❌ No |
| Aggiungo un nuovo canale seguendo il pattern esistente | ❌ No |
| **Cambio** da REST a GraphQL | ✅ Sì |
| Refactoring interno senza cambiare architettura | ❌ No |
| **Introduco** Event Sourcing | ✅ Sì |

**In un progetto tipico:**
- 10 evolutive → probabilmente 1-2 ADR
- 100 evolutive → probabilmente 5-10 ADR

---

## Granularità: Globale vs Particolare

Gli ADR sono per decisioni **ARCHITETTURALI**, non per ogni dettaglio.

| Decisione | Dove va? |
|-----------|----------|
| "Usiamo PostgreSQL" | ✅ **ADR** |
| "Usiamo Clean Architecture" | ✅ **ADR** |
| "Usiamo Unit of Work pattern per le transazioni" | ✅ **ADR** (se decisione di progetto) |
| "Le variabili usano camelCase" | ❌ `CODING_STANDARDS.md` |
| "I commit seguono Conventional Commits" | ❌ `CONTRIBUTING.md` |

---

## Perché Sono Importanti per un Architect?

Come **System Architect**, documenti le decisioni per:

- **Evitare discussioni ripetute** - "Abbiamo già valutato X"
- **Onboarding veloce** - Nuovi dev capiscono il ragionamento
- **Portfolio** - Mostra il tuo processo decisionale
- **Rivalutazione** - Quando il contesto cambia, puoi rivedere

---

## ADR nel Nostro Progetto

**Location:** `docs/adr/`

| ADR | Titolo | Status |
|-----|--------|--------|
| [[ADR-001-clean-architecture\|ADR-001]] | Clean Architecture | Accepted |

**Template:** `docs/adr/TEMPLATE.md`

---

## Risorse

**Must Read:**
- [Documenting Architecture Decisions - Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - L'articolo originale

**Approfondimenti:**
- [ADR GitHub Organization](https://adr.github.io/) - Template e tool
- [Architecture Decision Records in Action - InfoQ](https://www.infoq.com/articles/architecture-decision-records/) - Casi d'uso reali

**Tool:**
- [adr-tools](https://github.com/npryce/adr-tools) - CLI per gestire ADR

---

## Quiz di Verifica (2026-02-02)

### Q1: Hai un progetto dove devi scegliere tra PostgreSQL o MongoDB. Scriveresti un ADR?

**Mia risposta:** Sì devo scrivere un ADR: sto facendo una scelta architetturale e vanno documentate le ragioni per le quali sono state prese le scelte.

✅ **Corretto** - Scelta del database = decisione architetturale importante. Tra 6 mesi qualcuno chiederà "perché PostgreSQL e non MongoDB?" - l'ADR risponde.

---

### Q2: Un collega propone di modificare un ADR esistente (ADR-003) perché la situazione è cambiata. È corretto modificarlo?

**Mia risposta:** No, bisogna creare un nuovo ADR-004 che documenta il "cambiamento di rotta" e la decisione presa.

✅ **Corretto** - Gli ADR sono **immutabili**. Se la situazione cambia:
- Crei ADR-004 con `Status: Accepted`
- ADR-003 diventa `Status: Superseded by ADR-004`
- Così hai lo **storico** delle decisioni

---

### Q3: Qual è la differenza principale tra un ADR e un documento di design tradizionale?

**Mia risposta:** Il formato: la lunghezza in primis, il contenuto sintetico (status, context, decision, alternatives, consequences). Un documento word generico non segue una "prassi" o uno "standard". Un ADR invece sì.

✅ **Corretto** - Le differenze chiave:
- **Formato standard** → tutti sanno dove trovare le info
- **Brevità** → si legge in 5 minuti, non in 2 ore
- **Focalizzato** → una decisione = un ADR

---

### Q4: Il team decide di passare da xUnit a NUnit per i test. È un ADR?

**Mia risposta:** Io direi che è un ADR. Architetturale, perché stiamo decidendo quale tecnologia usare per i test.

✅ **Ragionamento corretto, con sfumatura:**

| Contesto | ADR? |
|----------|------|
| Progetto piccolo, pochi test, team di 2 | ❌ Probabilmente no |
| Progetto enterprise, 5000 test, team di 15 | ✅ Sì |

**Regola:** Più grande l'impatto, più serve l'ADR.

---

### Q5: Decidi di usare MediatR per implementare CQRS. È un ADR?

**Mia risposta:** Dipende: una decisione architetturale sarebbe eliminare CQRS o sostituirlo. Dire che lo implementiamo con MediatR è più "lieve" perché stiamo pensando a come implementare un aspetto dell'architettura. Ma la decisione di usare proprio MediatR invece di altro effettivamente influenza tutta l'architettura → Io direi che è ADR.

✅ **Ragionamento eccellente!**

| Decisione | ADR? |
|-----------|------|
| "Usiamo CQRS" | ✅ Sicuramente |
| "Implementiamo CQRS con MediatR" | ✅ Probabilmente sì |

**Perché MediatR merita ADR:**
- Diventa dipendenza **pervasiva** (ogni command/query lo usa)
- Cambiare da MediatR ad altro = refactoring massiccio
- Influenza come tutto il team scrive codice

**Bonus:** Puoi fare un singolo ADR: "ADR-005: Adozione di CQRS con MediatR"

---

### Q6: Aggiungi un nuovo campo "priority" all'entità Notification. È un ADR?

**Mia risposta:** Dipende → l'entità Notification di per sé fa parte del Domain, indipendente. Però se questo campo implicasse un cambio nella gestione delle notifiche (quindi introduzione di algoritmi specifici per gestire code di priorità) allora sarebbe utile scrivere un ADR.

✅ **Perfetto!**

| Scenario | ADR? |
|----------|------|
| `Priority` come campo informativo (solo display) | ❌ No |
| `Priority` + priority queue con algoritmi di scheduling | ✅ Sì |

**La chiave:** Non è il campo in sé, è l'**impatto architetturale** che ne deriva.

---

## Principio Fondamentale

> **"L'ADR non è una checklist burocratica. È uno strumento per documentare decisioni che hanno IMPATTO SIGNIFICATIVO sull'architettura."**

La domanda da farsi sempre: **"Tra 6 mesi, qualcuno avrà bisogno di sapere PERCHÉ abbiamo fatto questa scelta?"**

---

*Prossimi ADR previsti: Database choice, Message Queue choice, Template Engine choice*
*Ultimo aggiornamento: 2026-02-02*
