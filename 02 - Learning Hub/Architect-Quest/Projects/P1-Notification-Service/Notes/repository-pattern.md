---
tags:
  - p1
  - architecture
  - patterns
  - from/week-04
  - status/learning
aliases:
  - Repository Pattern
  - Repository Implementation
created: 2026-02-19
source: "Sessione Week 4 - Infrastructure Layer"
---

# Repository Pattern

> **One-liner:** Un'astrazione che nasconde i dettagli di persistenza (database, ORM) dietro un'interfaccia domain-centric, permettendo testabilità e sostituibilità.

## Cos'è

Il Repository Pattern è un'astrazione tra la business logic e il data access layer. L'handler non sa se stai usando PostgreSQL, MongoDB, o un file JSON - vede solo un'interfaccia.

```
┌─────────────────────────────────────────────────────────────────┐
│  APPLICATION LAYER                                              │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  INotificationRepository (PORT)                          │   │
│  │  ───────────────────────────────────────                 │   │
│  │  + GetByIdAsync(Guid id)                                 │   │
│  │  + AddAsync(Notification notification)                   │   │
│  │  + GetPendingAsync(DateTime threshold, int limit)        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ implements
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  INFRASTRUCTURE LAYER                                           │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  PostgresNotificationRepository (ADAPTER)                │   │
│  │  ───────────────────────────────────────                 │   │
│  │  - _dbContext: AppDbContext                              │   │
│  │                                                          │   │
│  │  + GetByIdAsync(Guid id) → _context.FindAsync(id)        │   │
│  │  + AddAsync(...) → _context.AddAsync(...)                │   │
│  │  + GetPendingAsync(...) → _context.Where(...).ToList()   │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Principi Chiave

| Principio | Significato |
|-----------|-------------|
| **Domain-centric** | L'interfaccia parla il linguaggio del Domain (Notification, Template), non del database (table, row) |
| **Collection-like** | Il repository sembra una collection in-memory: `Add()`, `Get()`, `Remove()` |
| **No leaking** | Non espone dettagli di EF Core (DbContext, IQueryable, DbSet) |
| **Testabile** | Puoi mockare l'interfaccia nei test |

## Quando usarlo

| Situazione | Esempio |
|------------|---------|
| **Aggregate Root persistence** | `INotificationRepository` per salvare/recuperare Notification |
| **Query specifiche per Use Case** | `GetPendingNotificationsAsync()`, `GetByRecipientAsync()` |
| **Isolare da ORM** | Vuoi poter cambiare da EF Core a Dapper senza toccare Application |
| **Testabilità** | Vuoi mockare la persistence nei test |

## Quando NON usarlo

| Situazione | Perché | Alternativa |
|------------|--------|-------------|
| **Query reporting complesse** | Repository non è per analytics | Dapper diretto, Read Model |
| **CRUD semplice senza logica** | Over-engineering | MediatR + DbContext diretto |
| **Esporre IQueryable<T>** | Lega Application a EF Core | Metodi specifici |

## Esempio

### Interfaccia (PORT) - in Application

```csharp
// Application/Interfaces/INotificationRepository.cs
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id, CancellationToken ct = default);
    Task<Notification?> GetByIdWithAttemptsAsync(Guid id, CancellationToken ct = default);
    Task<IReadOnlyList<Notification>> GetPendingAsync(DateTime threshold, int limit, CancellationToken ct = default);
    Task AddAsync(Notification notification, CancellationToken ct = default);
    void Remove(Notification notification);
}
```

### Implementazione (ADAPTER) - in Infrastructure

```csharp
// Infrastructure/Persistence/Repositories/PostgresNotificationRepository.cs
public class PostgresNotificationRepository : INotificationRepository
{
    private readonly AppDbContext _context;

    public PostgresNotificationRepository(AppDbContext context)
    {
        _context = context;
    }

    public async Task<Notification?> GetByIdAsync(Guid id, CancellationToken ct = default)
    {
        return await _context.Notifications.FindAsync(new object[] { id }, ct);
    }

    public async Task<Notification?> GetByIdWithAttemptsAsync(Guid id, CancellationToken ct = default)
    {
        return await _context.Notifications
            .Include(n => n.DeliveryAttempts)  // Eager loading
            .FirstOrDefaultAsync(n => n.Id == id, ct);
    }

    public async Task<IReadOnlyList<Notification>> GetPendingAsync(
        DateTime threshold,
        int limit,
        CancellationToken ct = default)
    {
        return await _context.Notifications
            .Where(n => n.Status == NotificationStatus.Pending)
            .Where(n => n.ScheduledFor <= threshold)
            .OrderBy(n => n.ScheduledFor)
            .Take(limit)
            .ToListAsync(ct);
    }

    public async Task AddAsync(Notification notification, CancellationToken ct = default)
    {
        await _context.Notifications.AddAsync(notification, ct);
    }

    public void Remove(Notification notification)
    {
        _context.Notifications.Remove(notification);
    }
}
```

## Collegamenti

- [[infrastructure-layer]] - Il layer dove vivono i repository
- [[ports-and-adapters]] - PORT (interfaccia) vs ADAPTER (implementazione)
- [[unit-of-work]] - Perché il repository NON chiama SaveChanges
- [[clean-architecture]] - Dependency Rule e direzione dipendenze

## Domande dalla Sessione

### D: Perché esporre IQueryable<T> è un anti-pattern?
**R:** Tre motivi:
1. **Difficile da mockare** - IQueryable richiede un provider EF Core
2. **Nessuna centralizzazione** - Ogni handler scrive query diverse
3. **Leaky abstraction** - Chi usa il repository deve conoscere EF Core (Include, ToListAsync)

L'interfaccia dovrebbe esporre metodi specifici come `GetPendingAsync()`, non `IQueryable<T>`.

### D: Cos'è il problema N+1?
**R:** Quando fai una query per N entity e poi accedi a una navigation property, EF Core fa N query extra (una per entity).

```csharp
// ❌ N+1: 1 query + 100 query extra
var notifications = await _context.Notifications.ToListAsync();  // Query 1
foreach (var n in notifications)
{
    var attempts = n.DeliveryAttempts;  // Query 2, 3, 4... 101!
}

// ✅ Eager Loading: 1 query con JOIN
var notifications = await _context.Notifications
    .Include(n => n.DeliveryAttempts)  // JOIN
    .ToListAsync();  // Query 1 (con JOIN)
```

**Analogia SQL:** È come fare 100 SELECT invece di una JOIN.

### D: Quando usare RepositoryBase<T>?
**R:**
| Quando SÌ | Quando NO |
|-----------|-----------|
| Molte entity con CRUD identico | Poche entity (2-3) |
| Team grande, vuoi consistenza | Ogni entity ha query diverse |
| Ridurre boilerplate | La genericità nasconde inefficienze |

## Quiz

### Q1: IQueryable Anti-pattern
Un collega propone di esporre `IQueryable<Notification> GetAll()` dal repository. Quali problemi causa?

<details>
<summary>Risposta</summary>

1. **Difficile da mockare** nei test
2. **Nessuna centralizzazione** delle query
3. **Leaky abstraction** - l'handler deve conoscere EF Core (Include, ToListAsync)
4. **Accoppiamento nascosto** - sembra disaccoppiato ma non lo è

Meglio: metodi specifici come `GetPendingAsync()`.
</details>

### Q2: N+1 Problem
Questo codice ha un problema di performance. Qual è e come lo risolvi?

```csharp
var notifications = await _context.Notifications.ToListAsync();
foreach (var n in notifications)
{
    Console.WriteLine($"Attempts: {n.DeliveryAttempts.Count}");
}
```

<details>
<summary>Risposta</summary>

**Problema:** N+1 queries. Per 100 notifiche → 101 query al database.

**Soluzione:** Eager loading con Include:
```csharp
var notifications = await _context.Notifications
    .Include(n => n.DeliveryAttempts)
    .ToListAsync();
```

Ora è 1 query con JOIN invece di 101 query separate.
</details>

### Q3: Repository Base
Hai 2 entity: `Notification` e `Template`. Vale la pena creare un `RepositoryBase<T>`?

<details>
<summary>Risposta</summary>

**Probabilmente no.** Con solo 2 entity:
- Il boilerplate risparmiato è minimo
- Le query specifiche saranno comunque diverse
- La complessità aggiunta non vale il beneficio

`RepositoryBase<T>` ha senso con molte entity (5+) e operazioni CRUD molto simili.
</details>

---

## Risorse per Approfondire

- **[Repository Pattern - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)** - Pattern originale
- **[Clean Architecture Cap. 23-24](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)** - Frameworks & Databases are details
- **[EF Core Loading Related Data](https://learn.microsoft.com/en-us/ef/core/querying/related-data/)** - Include, ThenInclude, Eager vs Lazy loading
- **[Jimmy Bogard: Avoid Repository Pattern](https://www.jimmybogard.com/repositories-on-top-unitofwork-are-not-a-good-idea/)** - Punto di vista critico (quando NON usarlo)

---

*Ultimo aggiornamento: 2026-02-19*
