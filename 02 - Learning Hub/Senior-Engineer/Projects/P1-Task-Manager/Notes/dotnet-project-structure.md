---
tags:
  - dotnet
  - project-structure
  - cli
  - from/senior-p1-week-01
  - status/learning
aliases:
  - Solution Structure
  - .NET Project Management
created: 2026-03-03
source: "Sessione Senior P1 Week 1"
---

# Struttura Progetto .NET - La Vista del Programmatore

> **One-liner:** Come creare, navigare e gestire una solution .NET multi-progetto dal terminale.

## Struttura Fisica

```
TaskManager/
├── TaskManager.sln              ← IL FILE CHE APRI
├── src/
│   ├── TaskManager.Domain/      ← Entities, Value Objects, Events
│   ├── TaskManager.Application/ ← Commands, Queries, Handlers
│   ├── TaskManager.Infrastructure/ ← EF Core, Redis, External
│   └── TaskManager.Api/         ← Controllers, Program.cs
└── tests/
    ├── TaskManager.Domain.Tests/
    ├── TaskManager.Application.Tests/
    └── TaskManager.Infrastructure.Tests/
```

## Comandi Essenziali

### Build & Run

```bash
# Compila TUTTO (solution intera)
dotnet build

# Compila solo un progetto
dotnet build src/TaskManager.Domain

# Avvia l'API
dotnet run --project src/TaskManager.Api
```

### Test (TDD)

```bash
# Tutti i test
dotnet test

# Solo test di un progetto
dotnet test tests/TaskManager.Domain.Tests

# Watch mode (ri-esegue automaticamente) ← USA QUESTO PER TDD!
dotnet watch test --project tests/TaskManager.Domain.Tests

# Con output dettagliato
dotnet test --logger "console;verbosity=detailed"
```

### Pacchetti NuGet

```bash
# Aggiungi pacchetto a un progetto specifico
dotnet add src/TaskManager.Domain package MediatR.Contracts

# ⚠️ ATTENZIONE: Pacchetti di test vanno nei progetti .Tests!
dotnet add tests/TaskManager.Domain.Tests package FluentAssertions
dotnet add tests/TaskManager.Domain.Tests package xunit
dotnet add tests/TaskManager.Domain.Tests package NSubstitute

# Rimuovi pacchetto
dotnet remove src/TaskManager.Domain package SomePackage

# Vedi pacchetti installati
dotnet list package
```

## Struttura Cartelle Consigliata

```
TaskManager.Domain/
├── Entities/           ← Classi con ID (TaskItem, Project)
├── ValueObjects/       ← Classi senza ID (Priority, DueDate)
├── Events/             ← Domain Events
├── Exceptions/         ← Eccezioni di dominio
└── Interfaces/         ← Porte (ITaskRepository)

TaskManager.Application/
├── Commands/           ← Modificano stato
│   └── CreateTask/
│       ├── CreateTaskCommand.cs
│       └── CreateTaskCommandHandler.cs
├── Queries/            ← Leggono stato
└── Common/             ← Behaviors, interfaces

TaskManager.Infrastructure/
├── Persistence/        ← EF Core, DbContext
├── Repositories/       ← Implementazioni
└── Services/           ← Redis, Email, etc.

TaskManager.Api/
├── Controllers/        ← Endpoint REST
└── Program.cs          ← Composition Root
```

## Riferimenti tra Progetti

```
Domain ← Application ← Infrastructure
                    ← Api
```

### Aggiungere un riferimento

```bash
# Application deve vedere Domain
dotnet add src/TaskManager.Application reference src/TaskManager.Domain

# Infrastructure deve vedere Application (e transitivamente Domain)
dotnet add src/TaskManager.Infrastructure reference src/TaskManager.Application

# Api deve vedere tutto
dotnet add src/TaskManager.Api reference src/TaskManager.Infrastructure
```

### Regola d'Oro

| Progetto | Può referenziare |
|----------|------------------|
| **Domain** | Niente (puro) |
| **Application** | Solo Domain |
| **Infrastructure** | Application (include Domain) |
| **Api** | Infrastructure (include tutto) |

## Creare una Solution da Zero

```bash
# 1. Crea solution
dotnet new sln -n TaskManager

# 2. Crea progetti
dotnet new classlib -n TaskManager.Domain -o src/TaskManager.Domain
dotnet new classlib -n TaskManager.Application -o src/TaskManager.Application
dotnet new classlib -n TaskManager.Infrastructure -o src/TaskManager.Infrastructure
dotnet new webapi -n TaskManager.Api -o src/TaskManager.Api

# 3. Crea progetti test
dotnet new xunit -n TaskManager.Domain.Tests -o tests/TaskManager.Domain.Tests
dotnet new xunit -n TaskManager.Application.Tests -o tests/TaskManager.Application.Tests
dotnet new xunit -n TaskManager.Infrastructure.Tests -o tests/TaskManager.Infrastructure.Tests

# 4. Aggiungi alla solution
dotnet sln add src/TaskManager.Domain
dotnet sln add src/TaskManager.Application
dotnet sln add src/TaskManager.Infrastructure
dotnet sln add src/TaskManager.Api
dotnet sln add tests/TaskManager.Domain.Tests
dotnet sln add tests/TaskManager.Application.Tests
dotnet sln add tests/TaskManager.Infrastructure.Tests

# 5. Aggiungi riferimenti
dotnet add src/TaskManager.Application reference src/TaskManager.Domain
dotnet add src/TaskManager.Infrastructure reference src/TaskManager.Application
dotnet add src/TaskManager.Api reference src/TaskManager.Infrastructure
dotnet add tests/TaskManager.Domain.Tests reference src/TaskManager.Domain
dotnet add tests/TaskManager.Application.Tests reference src/TaskManager.Application
dotnet add tests/TaskManager.Infrastructure.Tests reference src/TaskManager.Infrastructure
```

## Workflow Quotidiano TDD

```bash
# 1. Vai nella cartella progetto
cd /path/to/TaskManager

# 2. Apri watch mode (lascialo aperto in un terminale)
dotnet watch test --project tests/TaskManager.Domain.Tests

# 3. Ciclo TDD:
#    🔴 Scrivi test → fallisce
#    🟢 Scrivi codice minimo → passa
#    🔵 Refactor → ancora passa

# 4. Verifica tutto compila
dotnet build

# 5. Run per test manuale
dotnet run --project src/TaskManager.Api
```

## Quando usarlo

- **Sempre** quando lavori su progetti .NET multi-layer
- **TDD:** `dotnet watch test` è il tuo migliore amico
- **Nuovi pacchetti:** Ricorda la distinzione src vs tests

## Quando NON usarlo

- Progetti single-file o script (usa `dotnet script`)
- Prototype veloce (usa un solo progetto console)

## Collegamenti

- [[smart-enum]] - Value Objects che creerai nel Domain
- [[tdd-basics]] - Come usare watch mode efficacemente

## Quiz

### Q1: Dove va FluentAssertions?

Devi aggiungere FluentAssertions per testare il Domain. Quale comando usi?

- A) `dotnet add src/TaskManager.Domain package FluentAssertions`
- B) `dotnet add tests/TaskManager.Domain.Tests package FluentAssertions`
- C) `dotnet add package FluentAssertions`

**Mia risposta:** B

✅ **Corretto** - I pacchetti di testing vanno sempre nei progetti `.Tests`, mai nel codice di produzione.

---

### Q2: Watch mode per TDD

Quale comando lasci aperto mentre fai TDD sul Domain?

**Mia risposta:** `dotnet watch test --project tests/TaskManager.Domain.Tests`

✅ **Corretto** - Watch mode ri-esegue i test automaticamente quando modifichi i file.

---

### Q3: Riferimenti corretti

L'Infrastructure può referenziare direttamente il Domain?

**Mia risposta:** Sì, transitivamente attraverso Application

✅ **Corretto** - Infrastructure referenzia Application, che referenzia Domain. Quindi Infrastructure "vede" Domain.

---

*Creato durante: Senior P1 Week 1 - Task Manager*
