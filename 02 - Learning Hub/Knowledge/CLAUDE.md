# CLAUDE.md - Knowledge Base Index

> Questo file è l'indice della Knowledge Base di Dan. Claude lo consulta per:
> - Sapere cosa Dan ha già imparato
> - Collegare nuovi concetti a quelli esistenti
> - Evitare ripetizioni nelle spiegazioni
> - Creare note con tag consistenti

---

## 📁 Struttura Cartella

```
Knowledge/
├── CLAUDE.md                 ← SEI QUI - Indice e tag system
├── architecture/             ← Pattern architetturali
│   ├── clean-architecture.md
│   ├── dependency-rule.md
│   └── ...
├── solid/                    ← Principi SOLID
│   ├── srp.md
│   ├── ocp.md
│   └── ...
├── design/                   ← Design principles (non SOLID)
│   ├── deep-modules.md
│   ├── information-hiding.md
│   └── ...
├── patterns/                 ← Design Patterns (GoF)
│   ├── facade-pattern.md
│   └── ...
├── documentation/            ← Come documentare
│   ├── c4-model.md
│   ├── adr.md
│   └── ...
├── devops/                   ← DevOps, CI/CD, Docker
│   └── ...
├── databases/                ← Database, Redis, etc.
│   └── ...
└── ai/                       ← AI, LLM, agents
    └── ...
```

---

## 🏷️ Sistema Tag

### Tag di Categoria (OBBLIGATORI)
Ogni nota DEVE avere almeno un tag di categoria:

| Tag | Descrizione |
|-----|-------------|
| `#architecture` | Pattern e principi architetturali |
| `#solid` | I 5 principi SOLID |
| `#design` | Design principles generici |
| `#patterns` | Design Patterns (GoF, strutturali, etc.) |
| `#documentation` | Documentazione tecnica |
| `#devops` | CI/CD, Docker, Kubernetes |
| `#databases` | Database, caching, storage |
| `#testing` | Unit test, integration, TDD |
| `#ai` | AI, LLM, agents |
| `#dotnet` | Specifico .NET/C# |
| `#cloud` | Azure, AWS, cloud patterns |

### Tag di Origine (OBBLIGATORI)
Da dove viene la conoscenza:

| Tag | Descrizione |
|-----|-------------|
| `#from/week-01` | Imparato durante Week 1 |
| `#from/week-02` | Imparato durante Week 2 |
| `#from/book` | Da un libro |
| `#from/article` | Da un articolo |
| `#from/video` | Da un video |
| `#from/practice` | Dall'esperienza pratica |

### Tag di Stato (OBBLIGATORI)
Livello di comprensione:

| Tag | Descrizione |
|-----|-------------|
| `#status/learning` | In fase di apprendimento |
| `#status/learned` | Capito, da consolidare |
| `#status/mastered` | Padroneggiato |
| `#status/to-review` | Da rivedere |

### Tag di Progetto (OPZIONALI)
Se collegato a un progetto specifico:

| Tag | Descrizione |
|-----|-------------|
| `#project/p1-notification` | Progetto P1 |
| `#project/p2-nutriplan` | Progetto P2 |
| ... | ... |

---

## 📝 Template Nota

```markdown
---
tags:
  - [categoria]
  - from/[origine]
  - status/[stato]
aliases:
  - [nome alternativo]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: "[Libro/Articolo/Video/Sessione]"
---

# [Titolo Concetto]

> **One-liner:** [Spiegazione in una frase]

## Cos'è

[Spiegazione dettagliata]

## Quando usarlo

[Situazioni in cui applicare]

## Quando NON usarlo

[Anti-pattern, situazioni da evitare]

## Esempio

[Codice o diagramma]

## Collegamenti

- [[Nota correlata 1]]
- [[Nota correlata 2]]

## Quiz

### Q1: [Titolo domanda]

[Domanda - può essere aperta O multiple choice, un mix!]

- A) Opzione 1
- B) Opzione 2
- C) Opzione 3

**Mia risposta:** [Risposta di Dan]

✅ **Corretto** - [Feedback e spiegazione]

---

### Q2: [Domanda aperta]

[Qui invece una domanda aperta senza opzioni]

**Mia risposta:** [Risposta di Dan]

❌ **Parzialmente** - [Correzione costruttiva]

---

## Ti è piaciuto parlare di [Topic]? Allora impazzirai per:

> ⚠️ **SEZIONE OPZIONALE** - Claude la aggiunge SOLO se trova risorse
> veramente interessanti che approfondiscono o espandono il tema.
> NON aggiungere link generici. Solo cose che "fanno impazzire".

- [Risorsa 1](link) - Perché è interessante
- [Risorsa 2](link) - Cosa aggiunge di nuovo
```

### ⚠️ Regole Quiz
1. **Formato:** `### QX: [Titolo]` + domanda + `**Mia risposta:**` + feedback
2. **Mix** di domande aperte E multiple choice (varia!)
3. Dan risponde, Claude dà feedback
4. Usa ✅ Corretto / ❌ Sbagliato / ⚠️ Parziale
5. Il feedback spiega il PERCHÉ

### ⚠️ Regole "Impazzirai per"
1. **OPZIONALE** - Non forzare link inutili
2. Solo risorse che aggiungono valore REALE
3. Spiega brevemente PERCHÉ vale la pena
4. Può essere: articolo, video, libro, paper, talk

---

## 📊 Indice Note per Categoria

> Aggiornato automaticamente da Claude dopo ogni nota creata

### Architecture
| Nota | Status | Created |
|------|--------|---------|
| [[architecture/programming-paradigms\|Programming Paradigms]] | learned | 2026-02-05 |
| [[architecture/domain-events-theory\|Domain Events - Teoria e Pattern]] | learned | 2026-02-13 |

### SOLID
| Nota | Status | Created |
|------|--------|---------|
| [[solid/open-closed-principle\|Open/Closed Principle]] | learned | 2026-02-06 |
| [[solid/single-responsibility-principle\|Single Responsibility Principle]] | learned | 2026-02-06 |
| [[solid/dependency-inversion-principle\|Dependency Inversion Principle]] | learned | 2026-02-05 |

### Design
| Nota | Status | Created |
|------|--------|---------|
| *Nessuna nota ancora* | | |

### Documentation
| Nota | Status | Created |
|------|--------|---------|
| *Nessuna nota ancora* | | |

### Patterns
| Nota | Status | Created |
|------|--------|---------|
| [[patterns/facade-pattern\|Facade Pattern]] | learned | 2026-02-06 |

---

## 📈 Statistiche

| Metrica | Valore |
|---------|--------|
| **Note totali** | 6 |
| **Note mastered** | 0 |
| **Note to-review** | 0 |
| **Ultima nota** | 2026-02-13 |

---

## 🔗 Come Collegare dalle Note di Progetto

Nelle note di Week/Progetto, usa:

```markdown
## Concetti Appresi

Questa settimana abbiamo esplorato:
- [[Knowledge/solid/srp|Single Responsibility Principle]]
- [[Knowledge/architecture/clean-architecture|Clean Architecture]]
```

---

*Ultimo aggiornamento: 2026-02-06*
