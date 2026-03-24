---
tags:
  - architecture
  - clean-architecture
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - Screaming Architecture
  - Clean Architecture
  - Architettura Pulita
created: 2026-02-20
source: "Clean Architecture - Cap. 21-22"
---

# Clean Architecture Principles

> **One-liner:** Un'architettura deve "urlare" l'intento dell'applicazione, non la tecnologia usata - ed essere indipendente da framework, UI, database e agenti esterni.

## Screaming Architecture (Cap. 21)

### Il Test del "Colpo d'Occhio"

Guardando la struttura del progetto, cosa capisci?

```
❌ URLA LA TECNOLOGIA
src/
├── controllers/
├── services/
├── repositories/
├── entities/
├── dto/
└── config/

"È un'app Spring Boot/ASP.NET!"
Ma... cosa FA?
```

```
✅ URLA L'INTENTO
src/
├── Notifications/
│   ├── Schedule/
│   ├── Send/
│   └── Templates/
├── Users/
│   ├── Register/
│   └── Preferences/
└── Billing/
    ├── Invoices/
    └── Payments/

"È un sistema di notifiche con gestione utenti e fatturazione!"
```

### Principi

| Principio | Significato |
|-----------|-------------|
| **Use Case Driven** | Organizza per casi d'uso, non per tecnologia |
| **Framework Agnostic** | L'architettura esiste PRIMA del framework |
| **Testabile** | Architetture a use case sono facilmente testabili |
| **Intento Chiaro** | Un nuovo dev capisce subito cosa fa l'app |

### Framework = Dettaglio

> "Una buona architettura può essere implementata in qualsiasi framework. Il framework è un dettaglio, non l'architettura."

L'architettura definisce:
- Cosa fa l'applicazione (use cases)
- Come sono organizzate le responsabilità (layers)
- Chi dipende da chi (dependency rule)

Il framework implementa:
- Come si fa HTTP (ASP.NET, Spring)
- Come si accede al DB (EF Core, Hibernate)
- Come si fa DI (Microsoft DI, Autofac)

## The Clean Architecture (Cap. 22)

### Tante Architetture, Stessi Principi

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARCHITETTURE "PULITE"                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  • Hexagonal Architecture (Ports & Adapters) - Alistair Cockburn│
│  • Onion Architecture - Jeffrey Palermo                        │
│  • Clean Architecture - Robert C. Martin                       │
│  • BCE (Boundary-Control-Entity) - Ivar Jacobson               │
│                                                                 │
│  TUTTE condividono gli stessi principi fondamentali!           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Le 5 Caratteristiche Comuni

| # | Indipendenza da... | Significa che... |
|---|---------------------|------------------|
| 1 | **Framework** | Puoi cambiare framework senza riscrivere business logic |
| 2 | **UI** | Puoi avere Web, CLI, API con lo stesso core |
| 3 | **Database** | Puoi passare da SQL a Mongo senza toccare use cases |
| 4 | **Agenti esterni** | Email, payment, cloud - sono tutti sostituibili |
| 5 | **Testabilità** | Puoi testare business logic senza UI, DB, web server |

### I Concetti Universali

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                    ┌─────────────┐                              │
│                    │   ENTITIES  │  Business objects + rules    │
│                    │   (Domain)  │  Indipendenti da tutto       │
│                    └──────▲──────┘                              │
│                           │                                      │
│              ┌────────────┴────────────┐                        │
│              │        USE CASES        │  Application logic     │
│              │      (Application)      │  Orchestrano entities  │
│              └────────────▲────────────┘                        │
│                           │                                      │
│         ┌─────────────────┴─────────────────┐                   │
│         │      INTERFACE ADAPTERS           │  Controllers,     │
│         │   (Ports in, Adapters out)        │  Presenters,      │
│         └─────────────────▲─────────────────┘  Repositories     │
│                           │                                      │
│    ┌──────────────────────┴──────────────────────┐              │
│    │         FRAMEWORKS & DRIVERS                 │              │
│    │    (Infrastructure, Web, DB, External)       │              │
│    └──────────────────────────────────────────────┘              │
│                                                                 │
│    ══════════════════════════════════════════════════════════   │
│                     DEPENDENCY RULE                             │
│         Le dipendenze puntano SEMPRE verso l'interno           │
│    ══════════════════════════════════════════════════════════   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Dependency Rule (Riassunto)

> **"Il codice sorgente può solo puntare verso l'interno."**

- Domain non conosce nessuno
- Application conosce solo Domain
- Infrastructure conosce Application e Domain
- Niente nell'interno può sapere qualcosa dell'esterno

## Collegamento con P1 Notification Service

Il nostro progetto segue questi principi:

```
NotificationService/
├── Domain/           ← Entities, Value Objects (ZERO dipendenze)
├── Application/      ← Use Cases, Commands, Queries, Interfaces
├── Infrastructure/   ← EF Core, Repositories, External services
└── Api/              ← Controllers (entry point)

✅ Screaming: "È un servizio di notifiche!"
✅ Framework agnostic: possiamo cambiare da EF Core a Dapper
✅ Testabile: 268 test senza DB reale
✅ Dependency Rule: Infrastructure → Application → Domain
```

## Collegamenti

- [[dependency-inversion-principle]] - Abilita la Dependency Rule
- [[components]] - L'architettura si manifesta nei componenti
- [[component-coupling]] - SDP e SAP applicati ai layer
- [[cqrs-pattern]] — CQRS è un pattern applicato dentro Clean Architecture
- [[repository-pattern]] — Repository pattern è il ponte Domain→Infrastructure
- [[unit-of-work-pattern]] — UoW gestisce le transazioni rispettando i layer

## Quiz

### Q1: Screaming Architecture
Guardi una codebase e vedi: `controllers/`, `services/`, `repositories/`, `models/`. Cosa "urla"?

<details>
<summary>Risposta</summary>

Urla la **tecnologia/pattern** (MVC, repository pattern), non l'intento dell'applicazione. Non sai se è un e-commerce, un sistema bancario, o un social network. Un'architettura screaming mostrerebbe `Orders/`, `Payments/`, `Users/` - i casi d'uso.
</details>

### Q2: Caratteristiche comuni
Qual è la caratteristica che TUTTE le clean architectures condividono?

<details>
<summary>Risposta</summary>

La **Dependency Rule**: le dipendenze puntano sempre verso l'interno (verso le business rules). Questo garantisce indipendenza da framework, UI, database e agenti esterni.
</details>
