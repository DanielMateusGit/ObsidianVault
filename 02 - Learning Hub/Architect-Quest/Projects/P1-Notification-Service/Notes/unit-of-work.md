---
tags:
  - p1
  - application-layer
  - patterns
  - from/week-03
  - status/learning
aliases:
  - Unit of Work
  - UoW
  - Transaction Pattern
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---
ƒ
# Unit of Work Pattern

> **One-liner:** Pattern che raggruppa tutte le modifiche in una singola transazione - o tutto viene salvato, o niente.

## Cos'è

Il pattern **Unit of Work** (Martin Fowler, PoEAA) coordina la scrittura delle modifiche al database:

> "Mantiene una lista di oggetti modificati durante una transazione e coordina la scrittura delle modifiche."

### Il Problema Senza Unit of Work

```csharp
public async Task Handle(PlaceOrderCommand cmd, CancellationToken ct)
{
    // Ogni operazione committa separatamente!
    await _orderRepository.AddAsync(order, ct);
    await _orderRepository.SaveChangesAsync();  // COMMIT 1

    await _productRepository.UpdateAsync(product, ct);
    await _productRepository.SaveChangesAsync();  // COMMIT 2

    await _paymentRepository.AddAsync(payment, ct);
    await _paymentRepository.SaveChangesAsync();  // COMMIT 3 - Se fallisce qui?
}
// Problema: ordine e prodotto salvati, ma pagamento no → stato inconsistente!
```

### La Soluzione

```csharp
public async Task Handle(PlaceOrderCommand cmd, CancellationToken ct)
{
    await _orderRepository.AddAsync(order, ct);
    await _productRepository.UpdateAsync(product, ct);
    await _paymentRepository.AddAsync(payment, ct);

    // UN SOLO commit alla fine
    await _unitOfWork.SaveChangesAsync(ct);  // Tutto o niente!
}
```

## Repository vs Unit of Work

| Repository | Unit of Work |
|------------|--------------|
| Gestisce UNA collezione di Entity | Gestisce LA TRANSAZIONE |
| `Add`, `Update`, `Delete`, `GetById` | Solo `SaveChanges` |
| Non sa degli altri repository | Coordina tutti i repository |
| Molti nel progetto | Uno solo |
| "Cosa fare" | "Quando persistere" |

## Come Funziona con EF Core

### Il Change Tracker

EF Core ha un **Change Tracker** interno che traccia lo stato di ogni oggetto:

```
┌─────────────────────────────────────────────────┐
│           EF Core Change Tracker                │
│                                                 │
│  notification ──────────────► ADDED             │
│  product ───────────────────► MODIFIED          │
│  order ─────────────────────► ADDED             │
│                                                 │
│  Database: nessuna modifica ancora!             │
└─────────────────────────────────────────────────┘
```

### Flusso Passo per Passo

```csharp
// 1. Repository aggiunge - NON va al DB!
await _notificationRepository.AddAsync(notification, ct);
// EF Core segna: "notification" → stato ADDED
// Database: NESSUNA QUERY

// 2. Modifica oggetto - NON va al DB!
var product = await _productRepository.GetByIdAsync(id, ct);
// EF Core segna: "product" → stato UNCHANGED (appena letto)

product.ReduceStock(5);
// EF Core rileva la modifica automaticamente!
// EF Core segna: "product" → stato MODIFIED
// Database: NESSUNA QUERY

// 3. SOLO QUI va al database!
await _unitOfWork.SaveChangesAsync(ct);
// EF Core genera:
//   BEGIN TRANSACTION;
//   INSERT INTO Notifications (...);
//   UPDATE Products SET Stock = ...;
//   COMMIT;
```

### Stesso DbContext Ovunque

```
┌──────────────────────────────────────────────────────────────┐
│                    SCOPED (per request HTTP)                 │
│                                                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                   AppDbContext                       │   │
│   │              (Change Tracker interno)                │   │
│   └────────▲──────────────▲──────────────▲──────────────┘   │
│            │              │              │                   │
│   ┌────────┴───┐  ┌───────┴────┐  ┌──────┴──────┐          │
│   │ OrderRepo  │  │ProductRepo │  │ IUnitOfWork │          │
│   └────────────┘  └────────────┘  └─────────────┘          │
│                                                              │
│   Tutti puntano allo STESSO AppDbContext (Scoped)!          │
└──────────────────────────────────────────────────────────────┘
```

## Implementazione

### 1. Interfaccia (Application Layer)

```csharp
// Application/Interfaces/IUnitOfWork.cs
namespace NotificationService.Application.Interfaces;

public interface IUnitOfWork
{
    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
}
```

### 2. DbContext implementa IUnitOfWork (Infrastructure)

```csharp
// Infrastructure/Persistence/AppDbContext.cs
namespace NotificationService.Infrastructure.Persistence;

public class AppDbContext : DbContext, IUnitOfWork
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
    {
    }

    public DbSet<Notification> Notifications { get; set; }
    public DbSet<Template> Templates { get; set; }

    // IUnitOfWork.SaveChangesAsync è già implementato da DbContext!
    // Non serve scrivere nulla - il metodo esiste già
}
```

### 3. Repository SENZA SaveChanges

```csharp
// Infrastructure/Persistence/NotificationRepository.cs
public class NotificationRepository : INotificationRepository
{
    private readonly AppDbContext _context;

    public NotificationRepository(AppDbContext context)
    {
        _context = context;
    }

    public async Task AddAsync(Notification notification, CancellationToken ct)
    {
        // Aggiunge al Change Tracker, NON al database
        await _context.Notifications.AddAsync(notification, ct);
    }

    public async Task UpdateAsync(Notification notification, CancellationToken ct)
    {
        // Segna come Modified nel Change Tracker
        _context.Notifications.Update(notification);
    }

    // NOTA: Nessun SaveChanges qui!
}
```

### 4. Registrazione DI

```csharp
// Infrastructure/DependencyInjection.cs
services.AddDbContext<AppDbContext>(options =>
    options.UseNpgsql(connectionString));

// IUnitOfWork → stesso AppDbContext
services.AddScoped<IUnitOfWork>(sp => sp.GetRequiredService<AppDbContext>());

// Repository → usano stesso AppDbContext
services.AddScoped<INotificationRepository, NotificationRepository>();
```

### 5. Uso nell'Handler

```csharp
public class PlaceOrderHandler : IRequestHandler<PlaceOrderCommand, Guid>
{
    private readonly IOrderRepository _orderRepository;
    private readonly IProductRepository _productRepository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Guid> Handle(PlaceOrderCommand cmd, CancellationToken ct)
    {
        var order = new Order(cmd.CustomerId);
        await _orderRepository.AddAsync(order, ct);

        foreach (var item in cmd.Items)
        {
            var product = await _productRepository.GetByIdAsync(item.ProductId, ct);
            product.ReduceStock(item.Quantity);
            // Non serve UpdateAsync - EF Core rileva la modifica!
        }

        // UN SOLO commit
        await _unitOfWork.SaveChangesAsync(ct);
        return order.Id;
    }
}
```

## Senza EF Core (Dapper)

Senza Change Tracker automatico, usi una **transazione SQL esplicita**:

```csharp
// Interfaccia diversa
public interface IUnitOfWork : IDisposable
{
    IDbTransaction Transaction { get; }
    void Begin();
    void Commit();
    void Rollback();
}

// Implementazione
public class DapperUnitOfWork : IUnitOfWork
{
    private readonly IDbConnection _connection;
    private IDbTransaction? _transaction;

    public void Begin()
    {
        _connection.Open();
        _transaction = _connection.BeginTransaction();
    }

    public void Commit() => _transaction?.Commit();
    public void Rollback() => _transaction?.Rollback();
}

// Repository esegue subito, ma nella transazione
public async Task AddAsync(Notification notification, CancellationToken ct)
{
    await _connection.ExecuteAsync(
        "INSERT INTO Notifications (...) VALUES (...)",
        notification,
        transaction: _unitOfWork.Transaction  // Nella transazione!
    );
}

// Handler
public async Task<Guid> Handle(PlaceOrderCommand cmd, CancellationToken ct)
{
    _unitOfWork.Begin();
    try
    {
        await _orderRepository.AddAsync(order, ct);  // INSERT eseguito
        await _productRepository.UpdateAsync(product, ct);  // UPDATE eseguito
        _unitOfWork.Commit();  // Rende visibili le modifiche
        return order.Id;
    }
    catch
    {
        _unitOfWork.Rollback();  // Annulla tutto
        throw;
    }
}
```

### Confronto EF Core vs Dapper

| EF Core | Dapper |
|---------|--------|
| Modifiche in memoria fino a SaveChanges | Modifiche eseguite subito in transazione |
| Change Tracker automatico | Transazione SQL esplicita |
| `SaveChangesAsync()` = commit | `Commit()` = commit |
| Rollback automatico se non chiami Save | Devi chiamare `Rollback()` |

## Quando usarlo

**USA Unit of Work quando:**
- Più operazioni devono essere atomiche
- Usi più repository nello stesso handler
- Vuoi "tutto o niente"

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| Singola operazione semplice | Overkill |
| Solo letture (Query) | Non ci sono modifiche |
| Microservizi con eventual consistency | Pattern diverso |

## Collegamenti

- [[cqrs-commands]] - I Commands usano UnitOfWork
- [[ports-and-adapters]] - UoW è un Port
- [[application-layer]] - Dove vive l'interfaccia IUnitOfWork

## Domande dalla Sessione

### D: Perché INotificationRepository non ha SaveChangesAsync()?
**R:** Per rispettare il pattern Unit of Work:
- Solo `IUnitOfWork` ha `SaveChangesAsync()`
- Tutte le modifiche dei repository vengono committate insieme
- "O tutto o niente" - se c'è un errore, rollback automatico
- Se ogni repository avesse SaveChanges → stato inconsistente possibile

### D: Cosa succede se SaveChangesAsync() fallisce (es. violazione constraint)?
**R:** EF Core fa **rollback automatico**. Nessuna modifica viene applicata al database. Il DB rimane nello stato precedente alla chiamata.

### D: Quante implementazioni di IUnitOfWork servono con EF Core?
**R:** **Una sola** - il DbContext stesso. Non devi scrivere codice extra perché `DbContext` ha già `SaveChangesAsync()`. Devi solo:
1. Definire `IUnitOfWork` in Application (con il metodo)
2. Far implementare l'interfaccia a `AppDbContext`
3. Registrare nel DI: `IUnitOfWork → AppDbContext`

### D: Come funziona senza EF Core?
**R:** Usi transazioni SQL esplicite:
- `Begin()` → apre transazione
- Le operazioni vengono eseguite subito, ma dentro la transazione
- `Commit()` → rende visibili le modifiche
- `Rollback()` → annulla tutto

## Quiz

### Q1: Perché separare Repository da UnitOfWork?
Un collega mette `SaveChangesAsync()` in ogni repository. Cosa c'è di sbagliato?

<details>
<summary>Risposta</summary>

**Stato inconsistente possibile.** Se hai 3 operazioni e la terza fallisce:
- Con SaveChanges in ogni repo: prime 2 committate, terza no → inconsistente
- Con UnitOfWork separato: tutto in una transazione → rollback completo

Il Repository gestisce "cosa fare", UnitOfWork gestisce "quando persistere".
</details>

### Q2: Change Tracker
```csharp
var product = await _productRepository.GetByIdAsync(id, ct);
product.Price = 99.99m;
await _unitOfWork.SaveChangesAsync(ct);
```

Serve chiamare `_productRepository.UpdateAsync(product)` prima di SaveChanges?

<details>
<summary>Risposta</summary>

**No, con EF Core.** Il Change Tracker rileva automaticamente le modifiche agli oggetti "tracked". Quando chiami `GetByIdAsync`, l'oggetto viene tracciato. Qualsiasi modifica alle sue proprietà viene rilevata automaticamente.

`UpdateAsync` serve solo se l'oggetto è "detached" (non tracciato).
</details>

### Q3: Scoped Lifetime
Perché è importante che DbContext sia registrato come `Scoped` nel DI?

<details>
<summary>Risposta</summary>

Perché **tutti i repository devono condividere lo stesso DbContext** per request:
- `Scoped` = una istanza per richiesta HTTP
- OrderRepository, ProductRepository, IUnitOfWork → stesso DbContext
- Il Change Tracker accumula tutte le modifiche
- `SaveChangesAsync()` committa tutto insieme

Se fosse `Transient` (nuova istanza ogni volta), ogni repository avrebbe un DbContext diverso e il pattern non funzionerebbe.
</details>

---

## Risorse per Approfondire

- **[Unit of Work - Martin Fowler](https://martinfowler.com/eaaCatalog/unitOfWork.html)** - Definizione originale (PoEAA)
- **[EF Core Change Tracking](https://learn.microsoft.com/en-us/ef/core/change-tracking/)** - Come funziona il tracker
- **[Repository + UoW in .NET](https://learn.microsoft.com/en-us/aspnet/mvc/overview/older-versions/getting-started-with-ef-5-using-mvc-4/implementing-the-repository-and-unit-of-work-patterns-in-an-asp-net-mvc-application)** - Microsoft Docs
- **[Unit of Work with Dapper](https://www.learndapper.com/transactions)** - Transazioni esplicite
