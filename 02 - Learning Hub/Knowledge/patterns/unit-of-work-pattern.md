---
tags:
  - patterns
  - ddd
  - transactions
  - ef-core
  - from/explanation
  - status/learned
aliases:
  - Unit of Work
  - UnitOfWork
  - Transaction Management
created: 2026-02-26
source: "Spiegazione Claude + Milan Jovanovic concepts"
---

# Unit of Work Pattern

> **One-liner:** Pattern che coordina il salvataggio di multiple modifiche come una singola transazione atomica (tutto o niente).

---

## Cos'è

**Unit of Work** = Traccia tutti i cambiamenti durante una business transaction e li salva TUTTI insieme in una transazione atomica.

### 🛒 Analogia: Carrello della Spesa

```
Repository.Add(order)      → Metti nel carrello 🛒
Repository.Add(invoice)    → Metti nel carrello 🛒
Repository.Update(customer) → Metti nel carrello 🛒

UnitOfWork.SaveChanges()   → VAI ALLA CASSA! 💳
                             (paga tutto insieme o niente)
```

**Concetto chiave:** Repository **dice COSA fare**, UnitOfWork **decide QUANDO eseguire**.

---

## Problema che Risolve

### ❌ Senza Unit of Work

```csharp
// ❌ PROBLEMA: SaveChanges in ogni repository
public class OrderRepository
{
    public async Task AddAsync(Order order)
    {
        await _context.Orders.AddAsync(order);
        await _context.SaveChangesAsync();  // ← Repository salva!
    }
}

public class InvoiceRepository
{
    public async Task AddAsync(Invoice invoice)
    {
        await _context.Invoices.AddAsync(invoice);
        await _context.SaveChangesAsync();  // ← Repository salva!
    }
}

// Handler
public class CreateOrderHandler
{
    public async Task<Result<Guid>> Handle(...)
    {
        var order = Order.Create(...);
        await _orderRepository.AddAsync(order);  // ← COMMIT DB qui!

        var invoice = Invoice.Create(order);
        await _invoiceRepository.AddAsync(invoice);  // ← COMMIT DB qui!

        return Result<Guid>.Success(order.Id);
    }
}
```

**Problemi:**

1. **No atomicità** (tutto o niente)
```
Timeline:
t=0:   Order.Add() + SaveChanges()  ✅ Order SALVATO AL DB
t=10:  Invoice.Create()              💥 BOOM! Eccezione

Result: Order salvato, Invoice NO
        → INCONSISTENZA! 💀
```

2. **Violazione SRP**
```
Repository fa troppo:
- Gestisce query (GetById, GetAll)
- Gestisce modifiche (Add, Update)
- Decide QUANDO salvare ← NON è sua responsabilità!
```

3. **Difficile gestire transazioni multi-repository**
```csharp
// Come faccio transazione atomica su 3 repository?
await _repo1.AddAsync(entity1);  // ← Commit 1
await _repo2.AddAsync(entity2);  // ← Commit 2
await _repo3.Update(entity3);    // ← Commit 3

// Se #3 fallisce... #1 e #2 sono GIÀ salvati!
```

---

### ✅ Con Unit of Work

```csharp
// ✅ GIUSTO: Repository NON salva
public class OrderRepository
{
    public async Task AddAsync(Order order)
    {
        await _context.Orders.AddAsync(order);
        // ✅ NO SaveChanges - solo TRACCIA il cambiamento
    }
}

public class InvoiceRepository
{
    public async Task AddAsync(Invoice invoice)
    {
        await _context.Invoices.AddAsync(invoice);
        // ✅ NO SaveChanges - solo TRACCIA il cambiamento
    }
}

// UnitOfWork centralizza SaveChanges
public interface IUnitOfWork
{
    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
}

public class UnitOfWork : IUnitOfWork
{
    private readonly AppDbContext _context;

    public async Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        return await _context.SaveChangesAsync(cancellationToken);
        // ✅ Salva TUTTI i cambiamenti tracciati atomicamente!
    }
}

// Handler
public class CreateOrderHandler
{
    private readonly IOrderRepository _orderRepository;
    private readonly IInvoiceRepository _invoiceRepository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Result<Guid>> Handle(...)
    {
        var order = Order.Create(...);
        await _orderRepository.AddAsync(order);  // ← TRACCIA (ChangeTracker)

        var invoice = Invoice.Create(order);
        await _invoiceRepository.AddAsync(invoice);  // ← TRACCIA (ChangeTracker)

        await _unitOfWork.SaveChangesAsync();  // ← COMMIT atomico!

        return Result<Guid>.Success(order.Id);
    }
}
```

**Vantaggi:**

1. **Atomicità garantita**
```
Timeline:
t=0:   Order.Add()         → Tracciato in memoria (ChangeTracker)
t=10:  Invoice.Add()       → Tracciato in memoria (ChangeTracker)
t=20:  SaveChangesAsync()  → COMMIT atomico al DB

Se Invoice fallisce:
t=0:   Order.Add()    → Tracciato
t=10:  Invoice.Add()  💥 BOOM!
t=20:  SaveChanges()  → ❌ Mai raggiunto

Result: DB pulito! ✅ Order NON salvato (era solo in memoria)
```

2. **SRP rispettato**
```
Repository:   Gestisce query e modifiche (COSA fare)
UnitOfWork:   Gestisce transazioni (QUANDO salvare)
Handler:      Coordina business logic
```

3. **Transazioni multi-repository facili**
```csharp
// Transazione atomica su 3 repository
await _repo1.AddAsync(entity1);   // Traccia
await _repo2.AddAsync(entity2);   // Traccia
await _repo3.Update(entity3);     // Traccia

await _unitOfWork.SaveChangesAsync();  // ← TUTTO insieme o niente!
```

---

## Come Funziona (EF Core ChangeTracker)

### 📦 Change Tracker

EF Core traccia automaticamente i cambiamenti con il **ChangeTracker**:

```csharp
// ═══════════════════════════════════════════════════════
//  STEP 1: Traccia cambiamenti (in memoria)
// ═══════════════════════════════════════════════════════

var order = new Order { ... };
await _context.Orders.AddAsync(order);
// ChangeTracker: "order" → EntityState.Added
// DB: niente ancora! Solo in memoria

var customer = await _context.Customers.FindAsync(id);
customer.UpdateEmail("new@email.com");
// ChangeTracker: "customer" → EntityState.Modified
// DB: niente ancora! Solo in memoria

_context.Orders.Remove(oldOrder);
// ChangeTracker: "oldOrder" → EntityState.Deleted
// DB: niente ancora! Solo in memoria


// ═══════════════════════════════════════════════════════
//  STEP 2: SaveChanges = Commit al DB
// ═══════════════════════════════════════════════════════

await _context.SaveChangesAsync();

// EF Core genera SQL:
// INSERT INTO Orders (...) VALUES (...)         ← Added
// UPDATE Customers SET Email = ... WHERE Id =...  ← Modified
// DELETE FROM Orders WHERE Id = ...             ← Deleted

// DB: TUTTO salvato atomicamente! ✅
```

**Timeline:**
```
AddAsync()     → Solo memoria (ChangeTracker.Added)
Update()       → Solo memoria (ChangeTracker.Modified)
Remove()       → Solo memoria (ChangeTracker.Deleted)
                 ↓
                 ↓ (niente al DB ancora!)
                 ↓
SaveChangesAsync() → DB! (SQL: INSERT/UPDATE/DELETE)
```

---

## Relazione con Repository Pattern

**Repository** e **Unit of Work** sono complementari:

```
┌─────────────────────────────────────────────────────┐
│  Repository Pattern                                 │
│  - COSA modificare (Add, Update, Delete, Query)     │
│  - NO SaveChanges!                                  │
└────────────────────┬────────────────────────────────┘
                     │
                     │ Traccia in ChangeTracker
                     ↓
┌─────────────────────────────────────────────────────┐
│  Unit of Work Pattern                               │
│  - QUANDO salvare (transazione)                     │
│  - Coordina multiple repository                     │
│  - SaveChanges centralizzato                        │
└─────────────────────────────────────────────────────┘
```

### Implementazione Completa

```csharp
// ═══════════════════════════════════════════════════════
//  APPLICATION LAYER - Interfaces
// ═══════════════════════════════════════════════════════

// Repository (COSA)
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id);
    Task AddAsync(Notification notification);
    void Update(Notification notification);    // ← Sincrono (solo traccia)
    void Delete(Notification notification);    // ← Sincrono (solo traccia)
}

// UnitOfWork (QUANDO)
public interface IUnitOfWork
{
    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
    Task<IDbContextTransaction> BeginTransactionAsync();
}


// ═══════════════════════════════════════════════════════
//  INFRASTRUCTURE LAYER - Implementation
// ═══════════════════════════════════════════════════════

// Repository
public class PostgresNotificationRepository : INotificationRepository
{
    private readonly AppDbContext _context;

    public async Task<Notification?> GetByIdAsync(Guid id)
    {
        return await _context.Notifications
            .Include(n => n.DeliveryAttempts)
            .FirstOrDefaultAsync(n => n.Id == id);
    }

    public async Task AddAsync(Notification notification)
    {
        await _context.Notifications.AddAsync(notification);
        // ❌ NO SaveChanges - solo traccia!
    }

    public void Update(Notification notification)
    {
        _context.Notifications.Update(notification);
        // ❌ NO SaveChanges - solo traccia!
    }

    public void Delete(Notification notification)
    {
        _context.Notifications.Remove(notification);
        // ❌ NO SaveChanges - solo traccia!
    }
}

// UnitOfWork
public class UnitOfWork : IUnitOfWork
{
    private readonly AppDbContext _context;

    public UnitOfWork(AppDbContext context)
    {
        _context = context;
    }

    public async Task<int> SaveChangesAsync(CancellationToken cancellationToken = default)
    {
        // Salva TUTTI i cambiamenti tracciati
        return await _context.SaveChangesAsync(cancellationToken);
    }

    public async Task<IDbContextTransaction> BeginTransactionAsync()
    {
        return await _context.Database.BeginTransactionAsync();
    }
}


// ═══════════════════════════════════════════════════════
//  APPLICATION LAYER - Handler
// ═══════════════════════════════════════════════════════

public class ScheduleNotificationHandler
    : IRequestHandler<ScheduleNotificationCommand, Result<Guid>>
{
    private readonly INotificationRepository _notificationRepository;
    private readonly ITemplateRepository _templateRepository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Result<Guid>> Handle(
        ScheduleNotificationCommand request,
        CancellationToken cancellationToken)
    {
        // 1. Recupera template
        var template = await _templateRepository.GetByIdAsync(request.TemplateId);
        if (template == null)
            return Result<Guid>.Failure("Template not found");

        // 2. Crea notification
        var notification = Notification.Create(
            template,
            Recipient.Create(request.RecipientEmail, request.RecipientPhone),
            request.ScheduledAt
        );

        // 3. Traccia nel repository (solo memoria)
        await _notificationRepository.AddAsync(notification);

        // 4. Salva atomicamente (commit al DB)
        await _unitOfWork.SaveChangesAsync(cancellationToken);

        return Result<Guid>.Success(notification.Id);
    }
}
```

---

## 🚫 Perché SaveChanges NON Va nel Repository

### ❌ Anti-Pattern

```csharp
// ❌ SBAGLIATO
public class NotificationRepository : INotificationRepository
{
    public async Task AddAsync(Notification notification)
    {
        await _context.Notifications.AddAsync(notification);
        await _context.SaveChangesAsync();  // ← SBAGLIATO!
    }
}

// Handler
public class CreateOrderHandler
{
    public async Task<Result<Guid>> Handle(...)
    {
        var order = Order.Create(...);
        await _orderRepository.AddAsync(order);  // ← COMMIT DB qui!

        var invoice = Invoice.Create(order);
        await _invoiceRepository.AddAsync(invoice);  // ← BOOM! 💥

        // ❌ Order salvato, Invoice NO → INCONSISTENZA!
    }
}
```

**Timeline del disastro:**
```
t=0:   AddAsync(order)
       ├─ Orders.AddAsync(order)
       └─ SaveChangesAsync()      ✅ Order COMMITTATO AL DB

t=10:  Invoice.Create()           💥 BOOM! ArgumentException

Result: Order salvato al DB, Invoice mai creato
        → DATABASE INCONSISTENTE! 💀
```

---

### ✅ Giusto: SaveChanges in UnitOfWork

```csharp
// ✅ GIUSTO
public class NotificationRepository : INotificationRepository
{
    public async Task AddAsync(Notification notification)
    {
        await _context.Notifications.AddAsync(notification);
        // ✅ NO SaveChanges - solo traccia
    }
}

// Handler
public class CreateOrderHandler
{
    public async Task<Result<Guid>> Handle(...)
    {
        var order = Order.Create(...);
        await _orderRepository.AddAsync(order);  // ← Traccia (memoria)

        var invoice = Invoice.Create(order);     // ← Se BOOM qui...
        await _invoiceRepository.AddAsync(invoice);

        await _unitOfWork.SaveChangesAsync();  // ← ...mai raggiunto!

        // ✅ Order MAI salvato (era solo in memoria)
        // ✅ DB rimane consistente!
    }
}
```

**Timeline sicuro:**
```
t=0:   AddAsync(order)
       └─ ChangeTracker.Add(order)   → Solo memoria ✅

t=10:  Invoice.Create()              💥 BOOM!

t=20:  SaveChanges()                 → ❌ Mai raggiunto

Result: ChangeTracker cleared, niente al DB
        → DATABASE CONSISTENTE! ✅
```

---

## 🤔 DbContext È GIÀ un UnitOfWork!

**Fatto:** EF Core `DbContext` implementa già Unit of Work Pattern.

```csharp
// DbContext è già UnitOfWork:
_context.Orders.Add(order);         // ← Traccia
_context.Invoices.Add(invoice);     // ← Traccia
await _context.SaveChangesAsync();  // ← Commit atomico

// Perché wrappare con IUnitOfWork?
```

### 🔴 "IUnitOfWork è Boilerplate" (Pragmatic Approach)

**Argomento:** DbContext FA GIÀ tutto!

```csharp
// ❌ Wrapper inutile?
public class UnitOfWork : IUnitOfWork
{
    private readonly AppDbContext _context;

    public async Task<int> SaveChangesAsync()
    {
        return await _context.SaveChangesAsync();  // ← Solo delegato!
    }
}

// Perché non usare DbContext direttamente?
public class Handler
{
    private readonly AppDbContext _context;

    public async Task Handle(...)
    {
        _context.Orders.Add(order);
        await _context.SaveChangesAsync();  // ← Diretto!
    }
}
```

**Pro:**
- ✅ Meno codice (no boilerplate)
- ✅ DbContext è già UnitOfWork
- ✅ Veloce da implementare

**Contro:**
- ❌ Handler dipende da DbContext (Infrastructure detail)
- ❌ Viola **Dependency Inversion Principle**
- ❌ Difficile testare (mock DbContext complesso)
- ❌ Difficile cambiare persistence (Dapper, NoSQL)

---

### 🟢 "IUnitOfWork è Utile" (Clean Architecture)

**Argomento:** Separa concern e rispetta DIP.

```csharp
// ✅ Application dipende da abstraction
public interface IUnitOfWork
{
    Task<int> SaveChangesAsync();
    Task<IDbContextTransaction> BeginTransactionAsync();
}

// Handler
public class Handler
{
    private readonly IUnitOfWork _unitOfWork;  // ← Abstraction!

    // Non sa:
    // - Che usi EF Core
    // - Che usi DbContext
    // - Come funziona ChangeTracker
    // - PostgreSQL vs SQL Server vs MongoDB
}
```

**Pro:**
- ✅ **DIP rispettato** - Application → IUnitOfWork ← Infrastructure
- ✅ **Encapsulation** - Application non sa di DbContext
- ✅ **Testabilità** - Mock IUnitOfWork è facile
- ✅ **Transaction management** esplicito
- ✅ **Future-proof** - Cambiare persistence è facile

**Contro:**
- ❌ Più codice (interfaccia + implementazione)

---

### 🎯 Consensus: Dipende dal Progetto

| Scenario | Approccio | Perché |
|----------|-----------|--------|
| **Clean Architecture / DDD** | ✅ IUnitOfWork | DIP critico |
| **CRUD semplice** | ❌ No IUnitOfWork | DbContext sufficiente |
| **Progetto formativo** | ✅ IUnitOfWork | Imparare pattern |
| **Team grande (5+ devs)** | ✅ IUnitOfWork | Boundaries chiari |
| **Prototipo / MVP** | ❌ No IUnitOfWork | Velocità > architettura |
| **Domain complesso** | ✅ IUnitOfWork | Encapsulation fondamentale |

**Nel P1 Notification Service:**
- ✅ IUnitOfWork è **giusto**!
- Clean Architecture
- Rispetta DIP
- Progetto formativo

**In un progetto pragmatico?**
- DbContext diretto andrebbe benissimo!

---

## 💡 Pattern Avanzato: Transaction Scope

Per transazioni che coinvolgono **DB + operazioni esterne** (message queue, API):

```csharp
public class CreateOrderHandler
{
    private readonly IOrderRepository _orderRepository;
    private readonly IUnitOfWork _unitOfWork;
    private readonly IEventBus _eventBus;

    public async Task<Result<Guid>> Handle(...)
    {
        // ═══════════════════════════════════════════════════════
        //  Transaction Scope: DB + Event Bus atomico
        // ═══════════════════════════════════════════════════════

        using var transaction = await _unitOfWork.BeginTransactionAsync();

        try
        {
            // 1. Business logic
            var order = Order.Create(...);
            await _orderRepository.AddAsync(order);

            // 2. Salva DB
            await _unitOfWork.SaveChangesAsync();

            // 3. Pubblica evento (solo se DB commit OK)
            await _eventBus.PublishAsync(new OrderCreatedEvent(order.Id));

            // 4. Commit tutto (DB + Message Queue)
            await transaction.CommitAsync();  // ✅ Atomico!

            return Result<Guid>.Success(order.Id);
        }
        catch
        {
            await transaction.RollbackAsync();  // ❌ Rollback tutto
            throw;
        }
    }
}
```

**Quando usarlo:**
- DB + Message Queue
- DB + API esterna
- Multiple database
- Operazioni che devono essere atomiche

---

## 🔥 Pattern Avanzato: MediatR Pipeline Behavior

Automatizza transazioni per TUTTI i Command!

```csharp
// ═══════════════════════════════════════════════════════
//  Transaction Behavior - Automatico per ogni Command
// ═══════════════════════════════════════════════════════

public class TransactionBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IUnitOfWork _unitOfWork;

    public TransactionBehavior(IUnitOfWork unitOfWork)
    {
        _unitOfWork = unitOfWork;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        // Solo per Command (non Query)
        if (!typeof(TRequest).Name.EndsWith("Command"))
            return await next();

        // ═══════════════════════════════════════════════════════
        //  BEFORE: Apri transazione
        // ═══════════════════════════════════════════════════════

        using var transaction = await _unitOfWork.BeginTransactionAsync();

        try
        {
            // Esegui handler
            var response = await next();

            // ═══════════════════════════════════════════════════════
            //  AFTER: Commit automatico!
            // ═══════════════════════════════════════════════════════

            await transaction.CommitAsync();

            return response;
        }
        catch
        {
            // Rollback automatico se errore
            await transaction.RollbackAsync();
            throw;
        }
    }
}

// Registrazione
services.AddMediatR(cfg =>
{
    cfg.RegisterServicesFromAssembly(assembly);
    cfg.AddBehavior<TransactionBehavior<,>>();  // ← Automatico!
});


// ═══════════════════════════════════════════════════════
//  Handler: NO più gestione transazioni manuale!
// ═══════════════════════════════════════════════════════

public class CreateOrderHandler
{
    public async Task<Result<Guid>> Handle(...)
    {
        var order = Order.Create(...);
        await _orderRepository.AddAsync(order);

        var invoice = Invoice.Create(order);
        await _invoiceRepository.AddAsync(invoice);

        // ✅ TransactionBehavior gestisce tutto automaticamente!
        // NO bisogno di BeginTransaction/Commit/Rollback

        return Result<Guid>.Success(order.Id);
    }
}
```

**Vantaggi:**
- ✅ **Automatico** per tutti i Command
- ✅ **DRY** - no duplicazione try/catch
- ✅ **Consistent** - nessun handler dimentica transazioni
- ✅ **Pulito** - handler focalizzati su business logic

---

## Best Practices

### ✅ Fai

1. **SaveChanges in UnitOfWork, MAI nel Repository**
```csharp
// Repository
public async Task AddAsync(Order order)
{
    await _context.Orders.AddAsync(order);
    // ❌ NO SaveChanges
}

// Handler
await _orderRepository.AddAsync(order);
await _unitOfWork.SaveChangesAsync();  // ✅ Qui!
```

2. **Un SaveChanges per business transaction**
```csharp
public async Task Handle(...)
{
    await _repo1.AddAsync(entity1);
    await _repo2.AddAsync(entity2);
    await _repo3.Update(entity3);

    await _unitOfWork.SaveChangesAsync();  // ← Una volta per tutto!
}
```

3. **Transaction esplicita per operazioni complesse**
```csharp
using var transaction = await _unitOfWork.BeginTransactionAsync();
try
{
    // Multiple operations
    await _unitOfWork.SaveChangesAsync();
    await _eventBus.PublishAsync(...);
    await transaction.CommitAsync();
}
catch { await transaction.RollbackAsync(); throw; }
```

4. **Usa MediatR Behavior per transazioni automatiche**
```csharp
// TransactionBehavior gestisce tutto!
// Handler pulito, niente boilerplate
```

---

### ❌ Non Fare

1. **SaveChanges nel Repository**
```csharp
public async Task AddAsync(Order order)
{
    await _context.Orders.AddAsync(order);
    await _context.SaveChangesAsync();  // ❌ NO!
}
```

2. **Multiple SaveChanges nella stessa operation**
```csharp
await _orderRepository.AddAsync(order);
await _context.SaveChangesAsync();  // ❌ Prima

await _invoiceRepository.AddAsync(invoice);
await _context.SaveChangesAsync();  // ❌ Seconda (no atomicità!)
```

3. **UnitOfWork in Domain Layer**
```csharp
// Domain/Entities/Order.cs
public class Order
{
    private readonly IUnitOfWork _unitOfWork;  // ❌ Domain dipende da infra!
}
```

4. **Dimenticare transazioni per operazioni critiche**
```csharp
// ❌ DB + Event Bus senza transazione
await _unitOfWork.SaveChangesAsync();
await _eventBus.PublishAsync(...);  // ← Se fallisce, DB già committato!
```

---

## Collegamenti

- [[repository-pattern]] - Repository coordina COSA, UnitOfWork QUANDO
- [[mediatr-pipeline-behaviors]] - TransactionBehavior automatico
- [[aggregate-root]] - UnitOfWork salva aggregate root
- [[domain-events]] - Eventi + UnitOfWork per consistency
- [[clean-architecture-principles]] - UnitOfWork rispetta DIP
- [[cqrs-pattern]] — Command handlers chiamano UoW.SaveChanges
- [[dependency-inversion-principle]] — IUnitOfWork in Application, implementazione in Infrastructure

---

## Quiz

### Q1: Perché NON nel Repository?

Perché `SaveChangesAsync()` NON va nel repository ma in UnitOfWork?

<details>
<summary>Risposta</summary>

**Tre motivi principali:**

1. **Atomicità (tutto o niente)**
```csharp
// ❌ Se SaveChanges nel repository:
await _orderRepository.AddAsync(order);  // ← COMMIT DB
await _invoiceRepository.AddAsync(...);  // ← BOOM!
// Order salvato, Invoice NO → INCONSISTENZA!

// ✅ Se SaveChanges in UnitOfWork:
await _orderRepository.AddAsync(order);  // ← Solo memoria
await _invoiceRepository.AddAsync(...);  // ← BOOM!
await _unitOfWork.SaveChangesAsync();    // ← Mai raggiunto
// Order MAI salvato (solo memoria) → CONSISTENZA!
```

2. **SRP (Single Responsibility Principle)**
```
Repository:  Gestisce query e modifiche (COSA)
UnitOfWork:  Gestisce transazioni (QUANDO)
```

3. **Transazioni multi-repository**
```csharp
// Con UnitOfWork = facile!
await _repo1.AddAsync(entity1);
await _repo2.AddAsync(entity2);
await _unitOfWork.SaveChangesAsync();  // ← Atomico!
```

**Analogia:** Repository = metti nel carrello 🛒, UnitOfWork = vai alla cassa 💳

</details>

---

### Q2: Cosa Succede Qui?

```csharp
await _orderRepository.AddAsync(order);         // Riga 1
await _invoiceRepository.AddAsync(invoice);     // Riga 2 - BOOM! 💥
await _unitOfWork.SaveChangesAsync();           // Riga 3
```

Se Riga 2 lancia eccezione, Order viene salvato al DB?

<details>
<summary>Risposta</summary>

**NO! Order NON viene salvato.** ✅

**Perché:**

```csharp
// Riga 1: AddAsync(order)
public async Task AddAsync(Order order)
{
    await _context.Orders.AddAsync(order);
    // ← Solo ChangeTracker (memoria)
    // ← DB ancora pulito!
}

// Riga 2: BOOM! 💥
// ← Eccezione interrompe il flusso

// Riga 3: SaveChanges()
// ← Mai raggiunto!
```

**Timeline:**
```
t=0:   AddAsync(order)
       └─ ChangeTracker.Add(order)  → Solo memoria

t=10:  AddAsync(invoice)            💥 BOOM!

t=20:  SaveChanges()                → ❌ Mai raggiunto

Result: ChangeTracker cleared
        DB rimane pulito! ✅
```

**Concetto chiave:** Con EF Core, **nulla va al DB** finché non chiami `SaveChangesAsync()`!

Se invece SaveChanges fosse nel repository:
```csharp
public async Task AddAsync(Order order)
{
    await _context.Orders.AddAsync(order);
    await _context.SaveChangesAsync();  // ← COMMIT DB!
}

// Riga 1: Order SALVATO AL DB ✅
// Riga 2: BOOM! 💥
// Result: Order salvato, Invoice NO → INCONSISTENZA! 💀
```

</details>

---

### Q3: IUnitOfWork Necessario?

Nel P1 hai `IUnitOfWork`. Era necessario o potevi usare `DbContext.SaveChangesAsync()` direttamente?

<details>
<summary>Risposta</summary>

**Dipende dal contesto!**

#### Opzione A: IUnitOfWork (P1 - Clean Architecture)

```csharp
// ✅ GIUSTO per P1
public interface IUnitOfWork
{
    Task<int> SaveChangesAsync();
}

public class Handler
{
    private readonly IUnitOfWork _unitOfWork;  // ← Abstraction

    // Application non sa di DbContext!
}
```

**Pro:**
- ✅ Rispetta DIP (Application → abstraction)
- ✅ Testabile (mock IUnitOfWork facile)
- ✅ Encapsulation (Application non sa di EF Core)
- ✅ Formativo (impari il pattern)

#### Opzione B: DbContext diretto (Pragmatico)

```csharp
// ✅ OK per progetti pragmatici
public class Handler
{
    private readonly AppDbContext _context;

    public async Task Handle(...)
    {
        _context.Orders.Add(order);
        await _context.SaveChangesAsync();  // ← Diretto
    }
}
```

**Pro:**
- ✅ Meno codice (no boilerplate)
- ✅ DbContext è già UnitOfWork

**Contro:**
- ❌ Viola DIP (Application dipende da Infrastructure)

#### Verdict

**Nel P1:** IUnitOfWork è **giusto** perché:
- Clean Architecture
- Progetto formativo
- Rispetta principi SOLID

**In un CRUD veloce:** DbContext diretto andrebbe benissimo!

**Regola pratica:**
```
Clean Architecture / DDD / Team grande  → IUnitOfWork
CRUD semplice / Prototipo / MVP        → DbContext diretto
```

</details>

---

## Risorse per Approfondire

- **📝 [Milan Jovanovic - Unit of Work Pattern](https://www.milanjovanovic.tech/)** - Best practices moderne
- **📖 [Martin Fowler - Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html)** - Definizione originale
- **📝 [Microsoft Docs - EF Core Change Tracking](https://learn.microsoft.com/en-us/ef/core/change-tracking/)** - Come funziona ChangeTracker
- **📝 [Microsoft Docs - Transactions](https://learn.microsoft.com/en-us/ef/core/saving/transactions)** - Transaction management EF Core

---

*Nota creata da Dan dopo spiegazione di Claude il 2026-02-26*
*Basata su concetti di Milan Jovanovic + best practices DDD community*
*Analogia carrello 🛒 + cassiere 💳 di Dan!*
