---
tags:
  - p1
  - patterns
  - repository
  - from/week-01
  - status/learning
aliases:
  - Repository Pattern
  - IRepository
created: 2026-03-04
source: "Sessione Week 1 - Senior Engineer P1"
---

# Repository Interfaces

> **One-liner:** Un'interfaccia nel Domain che rappresenta una collezione di Entity, implementata nell'Infrastructure.

## Cos'è

Il Repository Pattern definisce un contratto (interfaccia) che astrae l'accesso ai dati. L'interfaccia vive nel **Domain Layer**, mentre l'implementazione concreta (con EF Core, Dapper, etc.) vive nell'**Infrastructure Layer**.

```
┌─────────────────────────────────────────────────────┐
│  DOMAIN LAYER                                       │
│  ┌─────────────────────────────────────────────┐   │
│  │  ITaskRepository                             │   │
│  │  - GetByIdAsync(Guid id)                     │   │
│  │  - AddAsync(TaskItem task)                   │   │
│  │  - GetAllAsync()                             │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                        ▲
                        │ implementa (DIP)
                        │
┌─────────────────────────────────────────────────────┐
│  INFRASTRUCTURE LAYER                               │
│  ┌─────────────────────────────────────────────┐   │
│  │  PostgresTaskRepository : ITaskRepository    │   │
│  │  - usa DbContext, EF Core, SQL...            │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Principio chiave:** Dependency Inversion - il Domain definisce cosa gli serve, l'Infrastructure implementa.

## Quando usarlo

| Situazione | Repository? |
|------------|-------------|
| Accesso a Entity (aggregate root) | ✅ Sì |
| CRUD operations | ✅ Sì |
| Persistenza di Value Objects | ❌ No (non hanno identità) |
| Query complesse di reporting | ⚠️ Meglio CQRS Query dedicata |

## Quando NON usarlo

- **Value Objects**: non hanno identità, non hanno repository
- **Query di sola lettura complesse**: meglio una Query separata (CQRS)
- **Cross-aggregate queries**: potrebbero indicare bounded context sbagliato

## Esempio

```csharp
// Domain/Repositories/ITaskRepository.cs
namespace TaskManager.Domain.Repositories;

public interface ITaskRepository
{
    Task<TaskItem?> GetByIdAsync(Guid id, CancellationToken ct = default);
    Task<IEnumerable<TaskItem>> GetAllAsync(CancellationToken ct = default);
    Task AddAsync(TaskItem task, CancellationToken ct = default);
    void Remove(TaskItem task);
}
```

**Note importanti:**
- Niente `SaveChangesAsync()` - quello è responsabilità di UnitOfWork
- `CancellationToken` per operazioni cancellabili
- Return `Task<T>` per async
- `GetByIdAsync` ritorna `T?` (nullable) perché potrebbe non esistere

## Collegamenti

- [[domain-events]] - Events registrati nelle Entity
- [[value-objects]] - VO non hanno repository
- [[00-Overview]] - Progetto P1 Task Manager

## Domande dalla Sessione

### D: Perché l'interfaccia sta nel Domain?
**R:** Dependency Inversion Principle. Il Domain definisce il contratto (cosa gli serve), l'Infrastructure implementa. Così il Domain non dipende dall'Infrastructure - è il contrario!

### D: Perché niente SaveChangesAsync nel repository?
**R:** Il repository gestisce la "bozza" delle modifiche. Il salvataggio effettivo (transazione) è responsabilità di UnitOfWork, che può salvare modifiche da più repository in una singola transazione.

### D: I Value Objects hanno repository?
**R:** No. I VO non hanno identità propria, vengono persistiti insieme all'Entity che li contiene (es. `Recipient` dentro `Notification`).

## Quiz

### Q1: Dove vive l'interfaccia ITaskRepository?
Nel Domain o nell'Infrastructure?

<details>
<summary>Risposta</summary>

**Nel Domain.** L'interfaccia (contratto) vive nel Domain perché definisce cosa il Domain ha bisogno. L'implementazione concreta vive nell'Infrastructure.

Questo segue il Dependency Inversion Principle: i moduli di alto livello (Domain) non dipendono da quelli di basso livello (Infrastructure). Entrambi dipendono da astrazioni.
</details>

### Q2: Chi chiama SaveChangesAsync?
Il Repository o qualcos'altro?

<details>
<summary>Risposta</summary>

**UnitOfWork** (o il Command Handler tramite UnitOfWork).

Il Repository prepara le modifiche (Add, Remove, Update tracking), ma il salvataggio effettivo avviene tramite UnitOfWork. Questo permette di:
- Salvare modifiche da più repository in una transazione
- Fare rollback se qualcosa fallisce
- Mantenere consistenza (tutto o niente)
</details>

### Q3: Creeresti un IPriorityRepository?
Priority è un Value Object (Smart Enum).

<details>
<summary>Risposta</summary>

**No.** I Value Objects non hanno repository perché:
- Non hanno identità propria
- Vengono persistiti come parte dell'Entity che li contiene
- Priority è un Smart Enum, non ha nemmeno bisogno di persistenza separata

Solo le Entity (specialmente gli Aggregate Root) hanno repository.
</details>

---

## Risorse per Approfondire

- **[Repository Pattern - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)** - Definizione originale del pattern
- **[Implementing the Repository Pattern - Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)** - Guida pratica con EF Core
- **Clean Architecture (Robert C. Martin)** - Cap. 22: The Clean Architecture
