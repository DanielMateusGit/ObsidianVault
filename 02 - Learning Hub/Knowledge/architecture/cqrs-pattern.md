---
tags:
  - architecture
  - cqrs
  - patterns
  - mediatr
  - from/article
  - status/learned
aliases:
  - CQRS
  - Command Query Responsibility Segregation
  - Separate Read Write Models
created: 2026-02-26
source: "Milan Jovanovic - CQRS Pattern With MediatR"
---

# CQRS (Command Query Responsibility Segregation)

> **One-liner:** Pattern architetturale che separa completamente le operazioni di scrittura (Command) da quelle di lettura (Query), permettendo ottimizzazioni e scalabilità indipendenti.

---

## Cos'è

**CQRS** separa il **modello di scrittura** dal **modello di lettura** a livello architetturale.

```
┌─────────────────────────────────────────────────────────────┐
│  Architettura Tradizionale (CRUD)                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   API Controller                                            │
│         │                                                   │
│         ├──> Create(User) ──┐                               │
│         ├──> Read(User)     ├──> User Entity ──> Database  │
│         ├──> Update(User)   │                               │
│         └──> Delete(User) ──┘                               │
│                                                             │
│   Stesso modello (User) per tutto                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│  CQRS (Modelli Separati)                                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────── WRITE SIDE ───────┐  ┌───── READ SIDE ────────┐│
│   │                           │  │                         ││
│   │  Commands                 │  │  Queries                ││
│   │  ├─ CreateUserCommand     │  │  ├─ GetUserQuery       ││
│   │  ├─ UpdateUserCommand     │  │  └─ SearchUsersQuery   ││
│   │  └─ DeleteUserCommand     │  │                         ││
│   │         │                 │  │         │               ││
│   │         ↓                 │  │         ↓               ││
│   │  User (Entity)            │  │  UserDto (DTO)          ││
│   │  Rich Domain Model        │  │  Flat, Denormalizzato   ││
│   │         │                 │  │         │               ││
│   │         ↓                 │  │         ↓               ││
│   │  Write Database           │  │  Read Database          ││
│   │  (Normalizzato)           │  │  (Denormalizzato)       ││
│   │                           │  │                         ││
│   └───────────────────────────┘  └─────────────────────────┘│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## CQS vs CQRS

### 🔹 CQS (Command Query Separation) - Bertrand Meyer

**Livello:** Method-level (singola classe)

**Principio:** Un metodo deve essere SOLO:
- **Command** = Modifica stato, ritorna void
- **Query** = Ritorna dati, zero side effects

```csharp
public class UserService
{
    // ✅ Command: modifica, ritorna void
    public void UpdateUserEmail(Guid userId, string email)
    {
        var user = _repository.GetById(userId);
        user.Email = email;
        _repository.Save(user);
    }

    // ✅ Query: ritorna dati, nessuna modifica
    public User GetUserById(Guid userId)
    {
        return _repository.GetById(userId);  // ← Solo lettura
    }

    // ❌ Violazione CQS: modifica E ritorna
    public User CreateUser(string name)
    {
        var user = new User(name);
        _repository.Add(user);
        return user;  // ← Command che ritorna dati!
    }
}
```

**Problema CQS:** Stesso modello (User) per write e read → coupling, difficile ottimizzare.

---

### 🔹 CQRS (Command Query Responsibility Segregation) - Greg Young

**Livello:** Architecture-level (intero sistema)

**Principio:** Separa **completamente** write model e read model.

```csharp
// ═══════════════════════════════════════════════════════
//  WRITE SIDE - Commands
// ═══════════════════════════════════════════════════════

// Command
public record CreateUserCommand(string Name, string Email) : IRequest<Result<Guid>>;

// Handler
public class CreateUserHandler : IRequestHandler<CreateUserCommand, Result<Guid>>
{
    private readonly IUserRepository _repository;  // ← Write-only repo

    public async Task<Result<Guid>> Handle(CreateUserCommand request, ...)
    {
        // Rich domain model con business logic
        var user = User.Create(request.Name, request.Email);

        await _repository.AddAsync(user);
        await _unitOfWork.SaveChangesAsync();

        return Result<Guid>.Success(user.Id);
    }
}

// Domain Model (write)
public class User : Entity
{
    public string Name { get; private set; }
    public Email Email { get; private set; }  // ← Value Object

    // Business logic, invariants, domain events...
    public static User Create(string name, string email) { ... }
}


// ═══════════════════════════════════════════════════════
//  READ SIDE - Queries
// ═══════════════════════════════════════════════════════

// Query
public record GetUserByIdQuery(Guid UserId) : IRequest<UserDto>;

// Handler
public class GetUserByIdHandler : IRequestHandler<GetUserByIdQuery, UserDto>
{
    private readonly IReadDbContext _readDb;  // ← Read-only DB

    public async Task<UserDto> Handle(GetUserByIdQuery request, ...)
    {
        // Query diretta, nessuna business logic
        return await _readDb.Users
            .Where(u => u.Id == request.UserId)
            .Select(u => new UserDto
            {
                Id = u.Id,
                Name = u.Name,
                Email = u.Email,
                CreatedAt = u.CreatedAt
            })
            .FirstOrDefaultAsync();
    }
}

// DTO (read)
public record UserDto
{
    public Guid Id { get; init; }
    public string Name { get; init; }
    public string Email { get; init; }
    public DateTime CreatedAt { get; init; }
}
```

**Differenza chiave:**
- **CQS** = Stesso modello, metodi separati
- **CQRS** = Modelli/database/stack separati

---

## I Due Livelli di CQRS

### 🟢 CQRS Logico (Simple CQRS)

**Separazione logica, stesso database.**

```
┌───────────────────────────────────────────────────┐
│                                                   │
│   Commands ──┐                                    │
│              ├──> Domain Model ──> Database       │
│   Queries ───┘                                    │
│                                                   │
│   Stesso DB, modelli logicamente separati        │
│                                                   │
└───────────────────────────────────────────────────┘
```

**Caratteristiche:**
- ✅ Command → Handler → Domain Model → DB (normalizzato)
- ✅ Query → Handler → DTO projection → DB (stesso!)
- ✅ Una sola source of truth (un DB)
- ✅ Consistency forte (transazioni ACID)
- ✅ Più semplice da implementare

**Quando usarlo:**
- Applicazioni medie (< 100k users)
- Read e Write con volumi simili
- Consistency è critica

---

### 🔴 CQRS Fisico (Advanced CQRS) 🤯

**Separazione fisica: due database diversi!**

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│   ┌─────── WRITE SIDE ────────┐       ┌───── READ SIDE ─────┐ │
│   │                            │       │                      │ │
│   │  Commands                  │       │  Queries             │ │
│   │      ↓                     │       │      ↓               │ │
│   │  Domain Model              │       │  DTOs                │ │
│   │      ↓                     │       │      ↓               │ │
│   │  ┌──────────────────┐      │       │  ┌────────────────┐ │ │
│   │  │  WRITE DATABASE  │      │       │  │  READ DATABASE │ │ │
│   │  │                  │      │       │  │                │ │ │
│   │  │  PostgreSQL      │      │       │  │  MongoDB       │ │ │
│   │  │  (Normalizzato)  │      │       │  │ (Denormalizzato│ │ │
│   │  │                  │      │       │  │                │ │ │
│   │  └────────┬─────────┘      │       │  └────────────────┘ │ │
│   │           │                │       │         ↑            │ │
│   │           │                │       │         │            │ │
│   └───────────┼────────────────┘       └─────────┼────────────┘ │
│               │                                  │              │
│               │  Events / Change Data Capture    │              │
│               └──────────────────────────────────┘              │
│                     (Sincronizzazione Asincrona)                │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Caratteristiche:**
- ✅ **Write DB** = PostgreSQL/SQL Server (normalizzato, ACID)
- ✅ **Read DB** = MongoDB/Redis/Elasticsearch (denormalizzato, veloce)
- ✅ Sincronizzazione asincrona (Domain Events, CDC, Event Sourcing)
- ✅ **Eventual Consistency** (read può essere leggermente stale)
- ✅ Scalabilità indipendente (scale read ≠ scale write)
- ✅ Ottimizzazioni specifiche (indices su read, sharding, caching)

**Quando usarlo:**
- Applicazioni massive (milioni di users)
- Read volume >> Write volume (90% read, 10% write)
- Eventual consistency accettabile
- Need for speed (query sub-millisecond)

---

## 🤯 Pattern: SQL Write + NoSQL Read

### Scenario Concreto: E-commerce

```
┌────────────────────────────────────────────────────────────────┐
│  WRITE SIDE - Transactional                                    │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Command: CreateOrder                                          │
│      ↓                                                         │
│  Domain:                                                       │
│  ├─ Order (Entity)                                             │
│  ├─ OrderItem (Entity)                                         │
│  ├─ Customer (Entity)                                          │
│  └─ Product (Entity)                                           │
│      ↓                                                         │
│  PostgreSQL (Normalizzato):                                    │
│  ├─ orders (id, customer_id, status, total)                   │
│  ├─ order_items (id, order_id, product_id, qty, price)        │
│  ├─ customers (id, name, email)                               │
│  └─ products (id, name, price, stock)                         │
│                                                                │
│  ✅ ACID transactions                                          │
│  ✅ Referential integrity                                      │
│  ✅ Complex joins per business logic                           │
│                                                                │
└────────────────────────────────────────────────────────────────┘

                        │ Domain Events
                        ↓

┌────────────────────────────────────────────────────────────────┐
│  READ SIDE - Query Optimized                                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Query: GetOrderDetailsQuery(orderId)                          │
│      ↓                                                         │
│  MongoDB (Denormalizzato):                                     │
│                                                                │
│  Collection: order_details                                     │
│  {                                                             │
│    "_id": "order-123",                                         │
│    "orderNumber": "ORD-2024-001",                              │
│    "status": "Shipped",                                        │
│    "total": 129.99,                                            │
│    "customer": {                    ← Embedded (no join!)      │
│      "name": "John Doe",                                       │
│      "email": "john@example.com"                               │
│    },                                                          │
│    "items": [                       ← Embedded (no join!)      │
│      {                                                         │
│        "productName": "iPhone 15",                             │
│        "quantity": 1,                                          │
│        "price": 999.99                                         │
│      },                                                        │
│      {                                                         │
│        "productName": "Case",                                  │
│        "quantity": 2,                                          │
│        "price": 29.99                                          │
│      }                                                         │
│    ],                                                          │
│    "shippingAddress": { ... },      ← Embedded                │
│    "createdAt": "2024-01-15T10:30:00Z"                         │
│  }                                                             │
│                                                                │
│  ✅ Una query, zero join (< 5ms)                               │
│  ✅ Perfetto per API GET /orders/{id}                          │
│  ✅ Può cachare facilmente (Redis)                             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Sincronizzazione Asincrona

```csharp
// ═══════════════════════════════════════════════════════
//  WRITE SIDE - Command Handler
// ═══════════════════════════════════════════════════════

public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, Result<Guid>>
{
    public async Task<Result<Guid>> Handle(CreateOrderCommand request, ...)
    {
        // 1. Business logic con Domain Model
        var order = Order.Create(customer, items);

        // 2. Salva su Write DB (PostgreSQL)
        await _orderRepository.AddAsync(order);
        await _unitOfWork.SaveChangesAsync();

        // 3. Pubblica Domain Event
        await _eventBus.PublishAsync(new OrderCreatedEvent
        {
            OrderId = order.Id,
            CustomerId = order.CustomerId,
            Items = order.Items.Select(i => new OrderItemDto { ... }),
            Total = order.Total,
            CreatedAt = order.CreatedAt
        });

        return Result<Guid>.Success(order.Id);
    }
}


// ═══════════════════════════════════════════════════════
//  Event Handler - Sincronizza Read DB
// ═══════════════════════════════════════════════════════

public class OrderCreatedEventHandler : INotificationHandler<OrderCreatedEvent>
{
    private readonly IMongoDatabase _readDb;

    public async Task Handle(OrderCreatedEvent @event, ...)
    {
        // Crea documento denormalizzato per MongoDB
        var orderDetails = new OrderDetailsDocument
        {
            Id = @event.OrderId,
            OrderNumber = GenerateOrderNumber(@event.OrderId),
            Status = "Pending",
            Total = @event.Total,
            Customer = await GetCustomerDetails(@event.CustomerId),  // ← Join fatto qui
            Items = @event.Items.Select(i => new OrderItemDocument
            {
                ProductName = i.ProductName,
                Quantity = i.Quantity,
                Price = i.Price
            }).ToList(),
            CreatedAt = @event.CreatedAt
        };

        // Salva su Read DB (MongoDB)
        var collection = _readDb.GetCollection<OrderDetailsDocument>("order_details");
        await collection.InsertOneAsync(orderDetails);
    }
}


// ═══════════════════════════════════════════════════════
//  READ SIDE - Query Handler
// ═══════════════════════════════════════════════════════

public class GetOrderDetailsHandler : IRequestHandler<GetOrderDetailsQuery, OrderDetailsDto>
{
    private readonly IMongoDatabase _readDb;

    public async Task<OrderDetailsDto> Handle(GetOrderDetailsQuery request, ...)
    {
        var collection = _readDb.GetCollection<OrderDetailsDocument>("order_details");

        // Query velocissima: nessun join, tutto embedded
        var document = await collection
            .Find(d => d.Id == request.OrderId)
            .FirstOrDefaultAsync();

        return Map(document);
    }
}
```

### Vantaggi SQL Write + NoSQL Read

| Aspetto | SQL (Write) | NoSQL (Read) | Perché |
|---------|-------------|--------------|---------|
| **Consistency** | ACID | Eventual | Write richiede consistency forte |
| **Normalization** | Normalizzato | Denormalizzato | Write evita duplicati, Read evita join |
| **Queries** | Complex joins | Document fetch | Write fa business logic, Read fa display |
| **Scalability** | Vertical | Horizontal | Write è bounded, Read può crescere infinito |
| **Schema** | Rigido | Flessibile | Write ha invariants, Read può evolvere |
| **Performance** | OK (< 100ms) | Eccellente (< 5ms) | Read può pre-computare tutto |

---

## Eventual Consistency

**Problema:** Read DB può essere **leggermente stale** (ritardato).

```
┌────────────────────────────────────────────────────────────┐
│  Timeline                                                  │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  t=0ms    CreateOrder command                              │
│           ↓                                                │
│  t=50ms   Order salvato su PostgreSQL ✅                   │
│           Event pubblicato                                 │
│           ↓                                                │
│  t=100ms  User fa GET /orders/123                          │
│           ❌ MongoDB non ha ancora l'ordine! (stale)       │
│           ↓                                                │
│  t=150ms  Event handler aggiorna MongoDB ✅                │
│           ↓                                                │
│  t=200ms  User fa GET /orders/123                          │
│           ✅ Ora MongoDB ha l'ordine!                       │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Soluzioni:**

### 1. Return ID + Poll
```csharp
// POST /orders
return CreatedAtAction("GetOrder", new { id = orderId }, null);
// ← Status 201 Created, Location header con URL

// Client fa GET /orders/{id}
// Se non trovato → retry dopo 100ms
```

### 2. Ottimistic Read
```csharp
public async Task<OrderDetailsDto> Handle(GetOrderDetailsQuery request, ...)
{
    // Prima prova Read DB
    var cached = await _readDb.GetOrderAsync(request.OrderId);
    if (cached != null)
        return cached;

    // Fallback a Write DB se non trovato (appena creato)
    var fresh = await _writeDb.Orders
        .Include(o => o.Items)
        .Include(o => o.Customer)
        .FirstOrDefaultAsync(o => o.Id == request.OrderId);

    return Map(fresh);  // Più lento ma sempre consistente
}
```

### 3. Versioning
```csharp
{
  "_id": "order-123",
  "_version": 5,  // ← Incrementa ad ogni update
  "status": "Shipped",
  ...
}

// Client può cachare e controllare version
// If-None-Match: "5" → 304 Not Modified
```

---

## Quando Usare CQRS

### ✅ USA CQRS quando:

#### 🟢 CQRS Logico (Simple)
- Read e Write hanno **logiche diverse** (complesse write, semplici read)
- Vuoi **ottimizzare separatamente** read e write
- Team separati per read e write
- Hai già **MediatR** nel progetto (costa poco aggiungere)
- Preparti per scalare in futuro

**Esempio:** Sistema ticketing
- Write: Business logic complessa (assign, escalate, SLA)
- Read: Lista ticket flat, nessuna logica

#### 🔴 CQRS Fisico (Advanced)
- **Read volume >> Write volume** (90% read, 10% write)
- **Milioni di read/sec** (social media, e-commerce massive)
- Read richiede **< 10ms** (UX critica)
- Write può tollerare **eventual consistency** (100-500ms stale OK)
- Budget e team per gestire complessità

**Esempio:** Amazon product catalog
- Write: Pochi update al giorno per prodotto
- Read: Milioni di ricerche/minuto

---

### ❌ NON usare CQRS quando:

- CRUD semplice (admin panel, backoffice)
- Read e Write hanno **stesso volume**
- Team piccolo (< 5 devs)
- **Strong consistency critica** ovunque (banking transactions)
- Primo progetto (impara prima pattern più semplici)
- Budget/tempo limitato

**Regola d'oro:** Inizia semplice, aggiungi CQRS se serve. Non fare over-engineering!

---

## CQRS ≠ Event Sourcing

**Misconception comune:** CQRS richiede Event Sourcing.

```
❌ SBAGLIATO:
CQRS → Devi fare Event Sourcing

✅ GIUSTO:
CQRS → Separa read/write models
Event Sourcing → Salva eventi invece di stato

Sono INDIPENDENTI (ma si combinano bene!)
```

**CQRS senza Event Sourcing:**
```csharp
// Write: Salva stato corrente (tradizionale)
var order = Order.Create(...);
await _repository.AddAsync(order);  // ← INSERT INTO orders ...

// Read: Query stato corrente
var dto = await _readDb.Orders.FirstAsync(...);
```

**CQRS con Event Sourcing:**
```csharp
// Write: Salva stream di eventi
var order = Order.Create(...);
order.AddDomainEvent(new OrderCreatedEvent { ... });
await _eventStore.SaveAsync(order.DomainEvents);  // ← Eventi, non stato

// Read: Proietta eventi su read model
// Event handler ascolta e costruisce OrderDetailsDocument
```

**Quando combinare:**
- Sistema con **audit trail completo** (finance, healthcare)
- **Temporal queries** ("Come era l'ordine il 15 Gennaio?")
- **Event-driven architecture**

Ma **CQRS funziona benissimo** senza Event Sourcing!

---

## Pro e Contro

### ✅ Vantaggi

**CQRS Logico:**
- ✅ Codice più pulito (separation of concerns)
- ✅ Query ottimizzate (proiezioni DTO, no ORM overhead)
- ✅ Testabilità (test command e query separatamente)
- ✅ Team velocity (read team ≠ write team, no blocchi)

**CQRS Fisico:**
- ✅ **Scalabilità massima** (scale read ≠ write)
- ✅ **Performance eccezionale** su read (< 5ms)
- ✅ **Flessibilità tecnologica** (SQL + NoSQL + Redis + Elastic)
- ✅ **Fault isolation** (write down ≠ read down)

### ❌ Svantaggi

**CQRS Logico:**
- ❌ Complessità architetturale (più classi, più codice)
- ❌ Learning curve (team deve capire pattern)
- ❌ Ancora un solo DB (scalabilità limitata)

**CQRS Fisico:**
- ❌ **Eventual consistency** (read può essere stale)
- ❌ **Complessità operazionale** (due DB, sincronizzazione, monitoring)
- ❌ **Costi infrastruttura** (PostgreSQL + MongoDB + Event Bus)
- ❌ **Debugging difficile** (dati in due posti, sync issues)
- ❌ **Data migration complessa** (due schemi, due migrazioni)

---

## Pattern Correlati

### CQRS + Event Sourcing
```
Commands → Append events → Event Store
                             ↓ (replay)
Queries  ← Read Models ←────┘
```

### CQRS + CQRS (Nested)
```
CQRS Level 1: Commands vs Queries
CQRS Level 2: Multiple Read Models per use case
  ├─ Read Model 1: List view (MongoDB)
  ├─ Read Model 2: Search (Elasticsearch)
  └─ Read Model 3: Analytics (BigQuery)
```

---

## Collegamenti

- [[mediatr-pipeline-behaviors]] - Come implementare CQRS con MediatR
- [[event-sourcing]] - Pattern complementare
- [[eventual-consistency]] - Consistency model in CQRS fisico
- [[domain-events]] - Per sincronizzare read DB
- [[repository-pattern]] - Write side usa repository
- [[dtos-vs-entities]] - Read side ritorna DTO

---

## Quiz

### Q1: CQS vs CQRS

Qual è la differenza principale tra CQS e CQRS?

A) CQS è method-level, CQRS è architecture-level
B) CQS usa MediatR, CQRS no
C) CQS separa database, CQRS no
D) Sono sinonimi

<details>
<summary>Risposta</summary>

**A) CQS è method-level, CQRS è architecture-level**

**CQS (Bertrand Meyer):**
- Principio a livello di **singoli metodi**
- Stessa classe, metodi command vs query
- Stesso modello (User)

**CQRS (Greg Young):**
- Pattern a livello di **architettura**
- Classi/stack/database separati
- Modelli diversi (User entity vs UserDto)

**Analogia:**
- CQS = "Separa read() e write() nella stessa classe File"
- CQRS = "Separa FileWriter e FileReader in classi diverse"

</details>

---

### Q2: Command Return Value

Un Command può ritornare dati in CQRS?

A) No, mai. Solo void
B) Sì, ma solo l'ID dell'entity creata
C) Sì, può ritornare l'intera Entity
D) Dipende: strict CQRS (no), pragmatic CQRS (ID ok)

<details>
<summary>Risposta</summary>

**D) Dipende: strict CQRS (no), pragmatic CQRS (ID ok)**

**Strict CQRS (purista):**
```csharp
public record CreateOrderCommand(...) : IRequest<Result>;  // ← void
// Client: POST → 201 Created con Location → GET
```

**Pragmatic CQRS (realista):**
```csharp
public record CreateOrderCommand(...) : IRequest<Result<Guid>>;  // ← ID
// Client: POST → 201 con ID → può fare subito altre operazioni
```

**Mai:**
```csharp
public record CreateOrderCommand(...) : IRequest<Order>;  // ❌ Intera entity
// Coupling, pesante, viola separazione
```

**Regola pratica:** Ritornare ID è **accettato** in CQRS moderno. Ritornare entity intera no.

</details>

---

### Q3: SQL + NoSQL Pattern

Hai un e-commerce con 10 milioni utenti. 95% traffico è ricerca prodotti, 5% è checkout. Come implementi CQRS?

A) CQRS logico: stesso PostgreSQL per tutto
B) CQRS fisico: PostgreSQL write, MongoDB read
C) CQRS fisico: MongoDB write, PostgreSQL read
D) Non usare CQRS, è overkill

<details>
<summary>Risposta</summary>

**B) CQRS fisico: PostgreSQL write, MongoDB read**

**Analisi scenario:**
- ✅ Read volume >> Write volume (95% vs 5%)
- ✅ Milioni di utenti (scala massive)
- ✅ Ricerca prodotti = query semplici, no business logic
- ✅ Checkout = business logic complessa, transazioni

**Architettura:**

**Write Side (Checkout) - PostgreSQL**
```
Commands: CreateOrder, ProcessPayment, UpdateInventory
Domain: Order, OrderItem, Payment (rich models)
DB: PostgreSQL (ACID, referential integrity)
```

**Read Side (Search) - MongoDB**
```
Queries: SearchProducts, GetProductDetails
DTO: ProductSearchResultDto (denormalizzato)
DB: MongoDB (document fetch, no join, velocissimo)
```

**Sincronizzazione:**
```
Checkout → OrderCreatedEvent → Handler → Aggiorna MongoDB
Inventory → StockChangedEvent → Handler → Aggiorna MongoDB
```

**Perché NON C:**
- MongoDB write = perde ACID transactions (pericoloso per checkout!)
- PostgreSQL read = troppo lento per ricerche massive (join, normalization)

**Perché NON A:**
- Un solo DB non scala a 10M users con 95% read
- PostgreSQL farebbe fatica con milioni di search/min

**Perché NON D:**
- CQRS è PERFETTO qui! Read/Write hanno esigenze completamente diverse

</details>

---

## Risorse per Approfondire

- **📝 [Milan Jovanovic - CQRS Pattern With MediatR](https://www.milanjovanovic.tech/blog/cqrs-pattern-with-mediatr)** - Articolo originale
- **📖 [Greg Young - CQRS Documents](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf)** - Il paper originale del creatore
- **🎥 [Greg Young - CQRS and Event Sourcing](https://www.youtube.com/watch?v=JHGkaShoyNs)** - Talk fondamentale
- **📝 [Martin Fowler - CQRS](https://martinfowler.com/bliki/CQRS.html)** - Overview e quando usarlo
- **📖 [Microsoft Docs - CQRS Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)** - Guida Azure

---

*Nota creata da Dan dopo aver letto l'articolo di Milan Jovanovic il 2026-02-26*
*Sezione "SQL + NoSQL" enfatizzata per la curiosità di Dan! 🤯*
