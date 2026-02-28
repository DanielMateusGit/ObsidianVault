---
tags:
  - patterns
  - ddd
  - data-access
  - ef-core
  - from/explanation
  - status/learned
aliases:
  - Repository Pattern
  - Data Access Pattern
  - Aggregate Root Repository
created: 2026-02-26
source: "Spiegazione Claude + Milan Jovanovic concepts"
---

# Repository Pattern

> **One-liner:** Astrazione che separa il Domain/Application Layer dai dettagli di persistenza, esponendo una collezione in-memory-like per gli Aggregate Root.

---

## Cos'è

**Repository Pattern** = Mediatore tra Domain Layer e Data Access Layer.

Il Domain vede il repository come una **collezione in-memory**:
```csharp
// Il Domain pensa:
var users = new List<User>();  // Collezione in-memory
users.Add(newUser);
var user = users.FirstOrDefault(u => u.Id == id);

// Ma dietro le quinte:
// - PostgreSQL
// - MongoDB
// - File system
// - API esterna
// - etc.
```

### Problema che Risolve

#### ❌ Senza Repository

```csharp
// Application Layer dipende direttamente da DbContext
public class CreateOrderHandler
{
    private readonly AppDbContext _context;  // ← Infra detail!

    public async Task<Result<Guid>> Handle(CreateOrderCommand request, ...)
    {
        // Query EF Core direttamente nell'Application Layer
        var customer = await _context.Customers
            .Include(c => c.Orders)
            .FirstOrDefaultAsync(c => c.Id == request.CustomerId);

        var order = Order.Create(customer, request.Items);

        _context.Orders.Add(order);  // ← EF Core specifico
        await _context.SaveChangesAsync();

        return Result<Guid>.Success(order.Id);
    }
}
```

**Problemi:**
- ❌ Application dipende da `DbContext` (Infrastructure detail)
- ❌ Violazione **Dependency Inversion Principle**
- ❌ Difficile testare (mock DbContext è complesso)
- ❌ Query EF Core sparse in tutti gli handler (duplicazione)
- ❌ Application sa di EF Core, Include, IQueryable, etc.

#### ✅ Con Repository

```csharp
// ═══════════════════════════════════════════════════════
//  APPLICATION LAYER
// ═══════════════════════════════════════════════════════

// Interfaccia (astrazione)
public interface IOrderRepository
{
    Task<Customer?> GetCustomerByIdAsync(Guid id);
    Task AddAsync(Order order);
}

// Handler
public class CreateOrderHandler
{
    private readonly IOrderRepository _repository;  // ← Abstraction!

    public async Task<Result<Guid>> Handle(CreateOrderCommand request, ...)
    {
        // Non sa di DbContext, EF Core, PostgreSQL, etc.
        var customer = await _repository.GetCustomerByIdAsync(request.CustomerId);

        var order = Order.Create(customer, request.Items);

        await _repository.AddAsync(order);
        await _unitOfWork.SaveChangesAsync();

        return Result<Guid>.Success(order.Id);
    }
}


// ═══════════════════════════════════════════════════════
//  INFRASTRUCTURE LAYER
// ═══════════════════════════════════════════════════════

// Implementazione (dettaglio)
public class PostgresOrderRepository : IOrderRepository
{
    private readonly AppDbContext _context;

    public async Task<Customer?> GetCustomerByIdAsync(Guid id)
    {
        return await _context.Customers
            .Include(c => c.Orders)  // ← Include nascosto all'Application
            .FirstOrDefaultAsync(c => c.Id == id);
    }

    public async Task AddAsync(Order order)
    {
        await _context.Orders.AddAsync(order);
    }
}
```

**Vantaggi:**
- ✅ Application dipende da `IOrderRepository` (abstraction)
- ✅ **DIP rispettato** (Application → abstraction ← Infrastructure)
- ✅ Facile testare (mock `IOrderRepository`)
- ✅ Query centralizzate (nessuna duplicazione)
- ✅ Application non sa di EF Core

---

## Generic Repository vs Specific Repository

### 🔴 Generic Repository (Anti-Pattern)

```csharp
// ❌ UN repository per TUTTE le entity
public interface IRepository<T> where T : Entity
{
    Task<T?> GetByIdAsync(Guid id);
    Task<List<T>> GetAllAsync();
    Task AddAsync(T entity);
    Task UpdateAsync(T entity);
    Task DeleteAsync(T entity);
}

// Implementazione
public class Repository<T> : IRepository<T> where T : Entity
{
    private readonly AppDbContext _context;

    public async Task<T?> GetByIdAsync(Guid id)
    {
        return await _context.Set<T>().FindAsync(id);
    }

    public async Task<List<T>> GetAllAsync()
    {
        return await _context.Set<T>().ToListAsync();
    }

    // ...
}

// Uso
public class SomeHandler
{
    private readonly IRepository<User> _userRepository;
    private readonly IRepository<Order> _orderRepository;
    private readonly IRepository<Product> _productRepository;

    // Tutti usano stessi metodi generici
}
```

**Problemi:**

1. **Troppo generico** - Ogni entity ha query diverse!
```csharp
// User ha bisogno di:
GetByEmailAsync(string email)
GetActiveUsersAsync()
GetUsersByRoleAsync(string role)

// Order ha bisogno di:
GetPendingOrdersAsync()
GetOrdersByCustomerAsync(Guid customerId)
GetOrdersWithItemsAsync()

// Come li metti in IRepository<T>? 🤔
```

2. **Forza a esporre IQueryable** (leaky abstraction)
```csharp
// Per permettere query custom, devi fare:
public interface IRepository<T>
{
    IQueryable<T> Query();  // ❌ Espone EF Core!
}

// Handler
var users = await _repository.Query()
    .Where(u => u.IsActive)       // ← Application sa di LINQ
    .Include(u => u.Orders)       // ← Application sa di Include
    .ToListAsync();               // ← Application sa di EF Core
```

3. **Accoppiamento nascosto**
```csharp
// Tutti dipendono da IRepository<T> generico
// Se vuoi aggiungere un metodo specifico... non puoi!
```

**✅ Pro:**
- Meno codice (un repository per tutto)
- DRY (GetById identico per tutte)

**❌ Contro (prevalenti):**
- Troppo generico, non riflette use case reali
- Forza leaky abstraction (IQueryable)
- Difficile evolvere (query specifiche?)
- Non segue DDD (un repository per aggregate root, non per ogni entity!)

---

### 🟢 Specific Repository (Best Practice)

```csharp
// ✅ UN repository per AGGREGATE ROOT
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id);
    Task<List<Notification>> GetPendingAsync();                     // ← Specifico!
    Task<List<Notification>> GetScheduledForAsync(DateTime when);   // ← Specifico!
    Task<Notification?> GetByIdWithAttemptsAsync(Guid id);          // ← Include esplicito!
    Task AddAsync(Notification notification);
}

public interface ITemplateRepository
{
    Task<Template?> GetByIdAsync(Guid id);
    Task<Template?> GetByNameAsync(string name);        // ← Specifico per Template!
    Task<List<Template>> GetActiveAsync();              // ← Specifico!
    Task AddAsync(Template template);
}

public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(Guid id);
    Task<List<Order>> GetByCustomerIdAsync(Guid customerId);  // ← Specifico per Order!
    Task<List<Order>> GetPendingAsync();                       // ← Specifico!
    Task AddAsync(Order order);
}

// Implementazione
public class PostgresNotificationRepository : INotificationRepository
{
    private readonly AppDbContext _context;

    public async Task<Notification?> GetByIdAsync(Guid id)
    {
        return await _context.Notifications
            .FirstOrDefaultAsync(n => n.Id == id);
    }

    public async Task<List<Notification>> GetPendingAsync()
    {
        return await _context.Notifications
            .Where(n => n.Status == NotificationStatus.Pending)
            .OrderBy(n => n.ScheduledAt)
            .ToListAsync();
    }

    public async Task<Notification?> GetByIdWithAttemptsAsync(Guid id)
    {
        return await _context.Notifications
            .Include(n => n.DeliveryAttempts)  // ← Include esplicito
            .FirstOrDefaultAsync(n => n.Id == id);
    }

    // ...
}
```

**Vantaggi:**

1. **Query specifiche per use case**
```csharp
GetPendingAsync()           // Chiaro: solo pending
GetByIdWithAttemptsAsync()  // Chiaro: include DeliveryAttempts
GetScheduledForAsync(when)  // Chiaro: scheduled per data specifica
```

2. **Include espliciti nel repository**
```csharp
// Application non sa di Include, ordina, filtra
var notification = await _repository.GetByIdWithAttemptsAsync(id);

// Repository decide come caricare i dati
public async Task<Notification?> GetByIdWithAttemptsAsync(Guid id)
{
    return await _context.Notifications
        .Include(n => n.DeliveryAttempts)  // ← Dettaglio implementativo
        .FirstOrDefaultAsync(n => n.Id == id);
}
```

3. **Interfaccia espressiva**
```csharp
// Guardando l'interfaccia capisci i use case:
public interface INotificationRepository
{
    Task<List<Notification>> GetPendingAsync();        // ← Use case: "get pending"
    Task<List<Notification>> GetScheduledForAsync(...); // ← Use case: "get scheduled"
}
```

4. **Type-safe** (no IQueryable)
```csharp
// ✅ Ritorna collection concreta
Task<List<Notification>> GetPendingAsync();

// ❌ NON ritorna IQueryable
IQueryable<Notification> GetAll();  // ← Leaky abstraction!
```

**✅ Pro (prevalenti):**
- Query tailored per use case
- Include espliciti (no N+1)
- Interfaccia espressiva
- Segue DDD (aggregate root boundary)
- Facile testare (mock semplice)

**❌ Contro:**
- Più codice (un repository per aggregate)
- Possibile duplicazione (GetById in tutti)

---

### 🎯 Quale Usare?

**Specific Repository** è la scelta standard in:
- Clean Architecture
- Domain-Driven Design
- Hexagonal Architecture

**Regola d'oro:**
```
✅ UN repository PER aggregate root
✅ Metodi specifici PER use case
❌ NO Generic Repository<T>
❌ NO IQueryable esposto
```

**Esempio P1 - GIUSTO! ✅**
```csharp
INotificationRepository  // ← Per Notification (aggregate root)
ITemplateRepository      // ← Per Template (aggregate root)
```

---

## ❌ Anti-Pattern: IQueryable Esposto

### Il Problema

```csharp
// ❌ SBAGLIATO
public interface IUserRepository
{
    IQueryable<User> GetAll();  // ← Espone IQueryable!
}

// Implementazione
public class PostgresUserRepository : IUserRepository
{
    private readonly AppDbContext _context;

    public IQueryable<User> GetAll()
    {
        return _context.Users;  // ← Ritorna IQueryable di EF Core
    }
}

// Handler (Application Layer)
public class GetUsersHandler
{
    private readonly IUserRepository _repository;

    public async Task<List<UserDto>> Handle(...)
    {
        // ❌ Application Layer sa di:
        // - IQueryable (EF Core)
        // - Where (LINQ)
        // - Include (EF Core)
        // - ToListAsync (EF Core async)

        var users = await _repository.GetAll()
            .Where(u => u.IsActive)        // ← LINQ in Application
            .Include(u => u.Orders)        // ← Include in Application
            .OrderBy(u => u.Name)          // ← OrderBy in Application
            .ToListAsync();                // ← EF Core in Application

        return Map(users);
    }
}
```

**Problemi:**

1. **Leaky Abstraction** - Application sa di EF Core
```csharp
// Se cambi da EF Core a Dapper:
// ❌ IQueryable non esiste in Dapper
// ❌ Devi cambiare TUTTI gli handler
```

2. **Accoppiamento**
```csharp
// Application dipende da:
using Microsoft.EntityFrameworkCore;  // ← EF Core!
using System.Linq;                     // ← LINQ provider specific!
```

3. **Testabilità ridotta**
```csharp
// Mock IQueryable è un incubo
var mockRepo = new Mock<IUserRepository>();
mockRepo.Setup(r => r.GetAll())
    .Returns(???);  // ← Come mocki IQueryable? 😱
```

4. **Query sparse**
```csharp
// Where/Include duplicati in TUTTI gli handler
// Handler 1: .Where(u => u.IsActive).Include(u => u.Orders)
// Handler 2: .Where(u => u.IsActive).Include(u => u.Orders)
// Handler 3: .Where(u => u.IsActive).Include(u => u.Orders)
```

---

### ✅ Soluzione: Metodi Specifici

```csharp
// ✅ GIUSTO
public interface IUserRepository
{
    Task<List<User>> GetActiveUsersAsync();              // ← Metodo specifico
    Task<User?> GetByIdWithOrdersAsync(Guid id);         // ← Include nel nome
    Task<List<User>> GetByRoleAsync(string role);        // ← Query specifica
}

// Implementazione
public class PostgresUserRepository : IUserRepository
{
    private readonly AppDbContext _context;

    public async Task<List<User>> GetActiveUsersAsync()
    {
        return await _context.Users
            .Where(u => u.IsActive)
            .Include(u => u.Orders)  // ← Include nascosto all'Application
            .OrderBy(u => u.Name)
            .ToListAsync();
    }

    public async Task<User?> GetByIdWithOrdersAsync(Guid id)
    {
        return await _context.Users
            .Include(u => u.Orders)  // ← Include esplicito nel nome!
            .FirstOrDefaultAsync(u => u.Id == id);
    }

    public async Task<List<User>> GetByRoleAsync(string role)
    {
        return await _context.Users
            .Where(u => u.Role == role)
            .ToListAsync();
    }
}

// Handler (Application Layer)
public class GetUsersHandler
{
    private readonly IUserRepository _repository;

    public async Task<List<UserDto>> Handle(...)
    {
        // ✅ Semplice, pulito, no EF Core knowledge
        var users = await _repository.GetActiveUsersAsync();
        return Map(users);
    }
}
```

**Vantaggi:**
- ✅ **Encapsulation** - Application non sa di EF Core
- ✅ **Testabilità** - Mock ritorna `List<User>` (semplice!)
- ✅ **Riusabilità** - `GetActiveUsersAsync()` usato da più handler
- ✅ **Espressività** - Nome metodo rivela intent
- ✅ **No duplicazione** - Query centralizzata nel repository

---

## 🐌 Problema N+1 (e Come Evitarlo)

### Cos'è il Problema N+1

**Scenario:** Vuoi caricare Orders con i rispettivi Customer.

```csharp
// ❌ PROBLEMA N+1
public async Task<List<OrderDto>> GetOrdersWithCustomers()
{
    // 1 query: carica orders
    var orders = await _context.Orders.ToListAsync();  // Query 1

    var dtos = new List<OrderDto>();
    foreach (var order in orders)  // Loop su 100 ordini
    {
        // N queries: carica customer per ogni order
        var customer = await _context.Customers
            .FirstAsync(c => c.Id == order.CustomerId);  // Query 2, 3, 4... 101!

        dtos.Add(new OrderDto
        {
            OrderId = order.Id,
            CustomerName = customer.Name
        });
    }

    return dtos;  // Totale: 1 + N queries!
}
```

**Timeline con 100 ordini:**
```
Query 1:   SELECT * FROM Orders                    → 100 ordini
Query 2:   SELECT * FROM Customers WHERE Id = 1    → Customer 1
Query 3:   SELECT * FROM Customers WHERE Id = 2    → Customer 2
Query 4:   SELECT * FROM Customers WHERE Id = 3    → Customer 3
...
Query 101: SELECT * FROM Customers WHERE Id = 100  → Customer 100

Totale: 101 queries! 🐌🐌🐌
Tempo: ~1-2 secondi
```

**Perché è un problema:**
- Database round-trip per ogni customer
- Lento (100 ordini = 101 queries)
- Spreca risorse DB

---

### ✅ Soluzione 1: Eager Loading (Include)

```csharp
// ✅ GIUSTO - Eager Loading
public async Task<List<OrderDto>> GetOrdersWithCustomers()
{
    var orders = await _context.Orders
        .Include(o => o.Customer)  // ← Eager loading: carica Customer subito!
        .ToListAsync();

    var dtos = orders.Select(o => new OrderDto
    {
        OrderId = o.Id,
        CustomerName = o.Customer.Name  // ← Già in memoria, no query!
    }).ToList();

    return dtos;
}
```

**SQL generato:**
```sql
SELECT o.*, c.*
FROM Orders o
LEFT JOIN Customers c ON o.CustomerId = c.Id

-- UNA SOLA query con JOIN! ✅
-- Tempo: ~50-100ms
```

**Timeline:**
```
Query 1: SELECT * FROM Orders LEFT JOIN Customers ...  → 100 ordini + customers

Totale: 1 query! ✅
Tempo: ~50-100ms (20x più veloce!)
```

---

### ✅ Soluzione 2: Projection (Select Diretto)

```csharp
// ✅ ANCORA MEGLIO - Projection
public async Task<List<OrderDto>> GetOrdersWithCustomers()
{
    return await _context.Orders
        .Select(o => new OrderDto
        {
            OrderId = o.Id,
            CustomerName = o.Customer.Name  // ← EF genera JOIN automaticamente!
        })
        .ToListAsync();
}
```

**SQL generato:**
```sql
SELECT o.Id AS OrderId, c.Name AS CustomerName
FROM Orders o
LEFT JOIN Customers c ON o.CustomerId = c.Id

-- Query ottimizzata: solo i campi necessari! ✅
-- Tempo: ~30-50ms (ancora più veloce!)
```

**Vantaggi projection vs Include:**
- ✅ **Più veloce** - carica solo campi necessari (non tutto Order + Customer)
- ✅ **Meno memoria** - DTO è più piccolo di Entity
- ✅ **Query ottimizzata** - DB trasferisce meno dati

---

### 🎯 Nel Repository: Dove Mettere Include?

#### Opzione 1: Include Sempre (se quasi sempre necessario)

```csharp
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id);  // ← Include sempre DeliveryAttempts
}

public class PostgresNotificationRepository : INotificationRepository
{
    public async Task<Notification?> GetByIdAsync(Guid id)
    {
        return await _context.Notifications
            .Include(n => n.DeliveryAttempts)  // ← Sempre caricato
            .FirstOrDefaultAsync(n => n.Id == id);
    }
}
```

**Quando:**
- Navigation property è **quasi sempre** usata
- Performance impact minimo

---

#### Opzione 2: Metodi Separati (se opzionale)

```csharp
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id);              // ← Senza DeliveryAttempts
    Task<Notification?> GetByIdWithAttemptsAsync(Guid id);  // ← Con DeliveryAttempts
}

public class PostgresNotificationRepository : INotificationRepository
{
    public async Task<Notification?> GetByIdAsync(Guid id)
    {
        return await _context.Notifications
            .FirstOrDefaultAsync(n => n.Id == id);
    }

    public async Task<Notification?> GetByIdWithAttemptsAsync(Guid id)
    {
        return await _context.Notifications
            .Include(n => n.DeliveryAttempts)  // ← Include esplicito nel nome!
            .FirstOrDefaultAsync(n => n.Id == id);
    }
}
```

**Quando:**
- Navigation property è **opzionale**
- Performance impact significativo (collection grande)

**Regola pratica:**
```
Navigation property quasi sempre necessaria? → Include sempre
Navigation property opzionale? → Metodo separato con nome esplicito
```

---

### 🔍 Come Identificare N+1

**Sintomo:** Loop su collection con query dentro.

```csharp
// ❌ PATTERN N+1
var items = await _repository.GetAllAsync();  // Query 1

foreach (var item in items)  // ← Loop
{
    var related = await _repository.GetRelatedAsync(item.Id);  // ← Query N
    // Usa related...
}
```

**Soluzione:** Include/Projection nel repository.

```csharp
// ✅ NO N+1
var items = await _repository.GetAllWithRelatedAsync();  // 1 query con JOIN

foreach (var item in items)
{
    var related = item.Related;  // ← Già in memoria!
    // Usa related...
}
```

---

## 🤔 Repository + EF Core: Ha Ancora Senso?

**Dibattito nella community:**

### 🔴 "Repository è Obsoleto" (Minority)

**Argomento:** DbContext È GIÀ un Repository Pattern!

```csharp
// DbContext ha già tutto:
_context.Users.Add(user);              // ← Add
_context.Users.Remove(user);           // ← Delete
_context.Users.FindAsync(id);          // ← GetById
_context.Users.Where(...).ToList();    // ← Query

// Perché wrappare con IRepository se DbContext fa tutto?
```

**Pro:**
- ✅ Meno codice (no boilerplate)
- ✅ DbContext è già testabile (InMemory o Testcontainers)
- ✅ Accesso diretto a feature EF Core

**Contro:**
- ❌ Application dipende da DbContext (Infrastructure detail)
- ❌ Viola **Dependency Inversion Principle**
- ❌ Difficile switchare da EF a Dapper/NoSQL
- ❌ Application conosce EF Core (Include, IQueryable, etc.)

---

### 🟢 "Repository è Utile" (Majority - DDD Community)

**Argomento:** Repository protegge Domain da dettagli implementativi.

```csharp
// Application vede solo:
public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id);
}

// Non sa:
// ✓ Che usi EF Core
// ✓ Che usi PostgreSQL
// ✓ Come fai Include
// ✓ DbContext, DbSet, IQueryable, SaveChanges, etc.
```

**Pro:**
- ✅ **Encapsulation** - Application non sa di EF Core
- ✅ **DIP rispettato** - Application → IRepository ← Infrastructure
- ✅ **Aggregate Root boundary** - Repository solo per root
- ✅ **Query centralizzate** - Facile ottimizzare/cachare
- ✅ **Testabilità** - Mock IRepository è triviale

**Contro:**
- ❌ Più codice (interfaccia + implementazione)
- ❌ Possibile duplicazione (GetById simile)

---

### 🎯 Consensus: Dipende dal Contesto

| Scenario | Approccio | Perché |
|----------|-----------|--------|
| **DDD / Clean Architecture** | ✅ Repository | Separation of concerns critica |
| **CRUD semplice** | ❌ No Repository | DbContext sufficiente |
| **Team grande (5+ devs)** | ✅ Repository | Boundaries chiari |
| **Prototipo / MVP** | ❌ No Repository | Velocità > architettura |
| **Domain complesso** | ✅ Repository | Encapsulation fondamentale |
| **Progetto formativo** | ✅ Repository | Imparare pattern |

**Nel P1 Notification Service:**
- ✅ Repository è **giusto**!
- Clean Architecture
- Domain con business logic
- Progetto formativo

---

## Quando Usare Repository

### ✅ USA Repository quando:

- Progetti con **Clean Architecture / DDD**
- **Domain complesso** con business logic
- **Team grande** (boundaries chiari tra layer)
- Vuoi **testabilità** facile (mock repository)
- Possibilità di **cambiare DB** in futuro
- **Aggregate Root** ben definiti

### ❌ NON usare Repository quando:

- **CRUD semplice** (admin panel, backoffice)
- **Prototipo / MVP** (velocità > architettura)
- **Team piccolo** (< 3 devs, overhead non giustificato)
- **Nessuna business logic** (solo lettura/scrittura DB)
- **DbContext è sufficiente** per il tuo caso

---

## Best Practices

### ✅ Fai

1. **Un repository per Aggregate Root**
```csharp
INotificationRepository  // Notification è aggregate root
ITemplateRepository      // Template è aggregate root
```

2. **Metodi specifici per use case**
```csharp
Task<List<Notification>> GetPendingAsync();        // Use case specifico
Task<List<Notification>> GetScheduledForAsync(...); // Use case specifico
```

3. **Include espliciti nel repository**
```csharp
public async Task<Notification?> GetByIdWithAttemptsAsync(Guid id)
{
    return await _context.Notifications
        .Include(n => n.DeliveryAttempts)  // Include qui, non in Application
        .FirstOrDefaultAsync(n => n.Id == id);
}
```

4. **Nome esplicito se Include opzionale**
```csharp
GetByIdAsync(id)              // Senza navigation property
GetByIdWithOrdersAsync(id)    // Con Orders (esplicito nel nome!)
```

5. **Ritorna Entity o DTO**
```csharp
Task<Notification?> GetByIdAsync(Guid id);  // ✅ Entity
Task<List<NotificationDto>> GetPendingAsync();  // ✅ DTO per query
```

6. **Interfaccia in Application, implementazione in Infrastructure**
```
Application/
  ├── Interfaces/
  │   └── INotificationRepository.cs  ← Interfaccia

Infrastructure/
  ├── Repositories/
  │   └── PostgresNotificationRepository.cs  ← Implementazione
```

---

### ❌ Non Fare

1. **Generic Repository<T>**
```csharp
IRepository<T>  // ❌ Troppo generico
```

2. **Esporre IQueryable<T>**
```csharp
IQueryable<Notification> GetAll();  // ❌ Leaky abstraction
```

3. **Query EF in Application Layer**
```csharp
// ❌ Handler
var users = await _context.Users
    .Where(u => u.IsActive)
    .ToListAsync();
```

4. **Repository per ogni Entity**
```csharp
IDeliveryAttemptRepository  // ❌ DeliveryAttempt non è aggregate root!
```

5. **SaveChanges nel repository**
```csharp
public async Task AddAsync(Notification notification)
{
    await _context.Notifications.AddAsync(notification);
    await _context.SaveChangesAsync();  // ❌ Usa UnitOfWork!
}
```

---

## Collegamenti

- [[unit-of-work-pattern]] - Gestisce SaveChanges per tutti i repository
- [[aggregate-root]] - Solo aggregate root hanno repository
- [[dependency-inversion-principle]] - Repository rispetta DIP
- [[clean-architecture-principles]] - Repository in Infrastructure
- [[domain-driven-design]] - Repository è pattern DDD core

---

## Quiz

### Q1: Generic vs Specific

Quale approccio è preferito in Clean Architecture + DDD?

A) Generic Repository (`IRepository<T>`)
B) Specific Repository (`INotificationRepository`)
C) No Repository (DbContext diretto)
D) Dipende dal progetto

<details>
<summary>Risposta</summary>

**B) Specific Repository (`INotificationRepository`)**

**Perché:**
- ✅ Query tailored per aggregate root
- ✅ Metodi specifici per use case (GetPendingAsync)
- ✅ Include espliciti (no N+1)
- ✅ Interfaccia espressiva
- ✅ Segue DDD (un repository per aggregate root)

**Generic Repository (`IRepository<T>`) ha problemi:**
- ❌ Troppo generico (ogni entity ha query diverse)
- ❌ Forza a esporre IQueryable (leaky abstraction)
- ❌ Difficile aggiungere metodi specifici

**Esempio P1 - GIUSTO:**
```csharp
public interface INotificationRepository
{
    Task<List<Notification>> GetPendingAsync();  // ← Specifico!
}
```

</details>

---

### Q2: IQueryable Esposto

Un collega propone:
```csharp
public interface IOrderRepository
{
    IQueryable<Order> GetAll();  // Così posso fare Where nell'handler!
}
```

Cosa c'è di sbagliato?

<details>
<summary>Risposta</summary>

**Leaky Abstraction - Application sa di EF Core!**

**Problemi:**

1. **Accoppiamento:**
```csharp
// Handler sa di:
using Microsoft.EntityFrameworkCore;  // ← EF Core!
using System.Linq;                     // ← LINQ!

var orders = await _repository.GetAll()
    .Where(...)      // ← LINQ
    .Include(...)    // ← EF Core
    .ToListAsync();  // ← EF Core
```

2. **Difficile cambiare DB:**
```csharp
// Se passi a Dapper:
// ❌ IQueryable non esiste in Dapper
// ❌ Devi cambiare TUTTI gli handler
```

3. **Testabilità ridotta:**
```csharp
// Mock IQueryable è complesso
```

**Soluzione:**
```csharp
// ✅ Metodi specifici
public interface IOrderRepository
{
    Task<List<Order>> GetPendingAsync();
    Task<List<Order>> GetByCustomerIdAsync(Guid customerId);
}

// Application non sa di EF Core!
```

</details>

---

### Q3: Problema N+1

Identifica il problema N+1:
```csharp
var notifications = await _repository.GetPendingAsync();

foreach (var notif in notifications)
{
    var template = await _templateRepository.GetByIdAsync(notif.TemplateId);
    Console.WriteLine($"{notif.Id}: {template.Name}");
}
```

Come lo risolvi?

<details>
<summary>Risposta</summary>

**Sì, è N+1!**

**Problema:**
```
Query 1: SELECT * FROM Notifications WHERE Status = 'Pending'  → 100 notifiche
Query 2: SELECT * FROM Templates WHERE Id = 1                 → Template 1
Query 3: SELECT * FROM Templates WHERE Id = 2                 → Template 2
...
Query 101: SELECT * FROM Templates WHERE Id = 100             → Template 100

Totale: 101 queries! 🐌
```

**Soluzione 1: Include nel repository**
```csharp
// Repository
public async Task<List<Notification>> GetPendingWithTemplatesAsync()
{
    return await _context.Notifications
        .Where(n => n.Status == NotificationStatus.Pending)
        .Include(n => n.Template)  // ← Eager loading!
        .ToListAsync();
}

// Handler
var notifications = await _repository.GetPendingWithTemplatesAsync();

foreach (var notif in notifications)
{
    Console.WriteLine($"{notif.Id}: {notif.Template.Name}");  // ← Già in memoria!
}

// 1 query con JOIN ✅
```

**Soluzione 2: Projection**
```csharp
// DTO
public record NotificationWithTemplateDto(Guid Id, string TemplateName);

// Repository
public async Task<List<NotificationWithTemplateDto>> GetPendingWithTemplateNamesAsync()
{
    return await _context.Notifications
        .Where(n => n.Status == NotificationStatus.Pending)
        .Select(n => new NotificationWithTemplateDto(
            n.Id,
            n.Template.Name  // ← EF genera JOIN automaticamente!
        ))
        .ToListAsync();
}

// Ancora più veloce: solo campi necessari! ✅
```

</details>

---

## Risorse per Approfondire

- **📝 [Milan Jovanovic - Repository Pattern](https://www.milanjovanovic.tech/)** - Best practices moderne
- **📖 [Martin Fowler - Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)** - Definizione originale
- **📖 [Domain-Driven Design - Eric Evans](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)** - Repository in DDD
- **📝 [Microsoft Docs - Repository Pattern](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design)** - Implementazione .NET

---

*Nota creata da Dan dopo spiegazione di Claude il 2026-02-26*
*Basata su concetti di Milan Jovanovic + best practices DDD community*
