---
tags:
  - p1
  - clean-architecture
  - entities
  - domain
  - from/week-02
  - status/learned
aliases:
  - Entities Clean Architecture
  - Business Rules
  - Screaming Architecture
created: 2026-02-09
source: "Clean Architecture - Uncle Bob, Cap. 20-22"
---

# Entities e Clean Architecture

> **One-liner:** Le Entities sono oggetti software che incapsulano business rules pure, indipendenti da framework, database e UI, formando il cuore immutabile del sistema.

---

## 📚 CAP. 20: ENTITIES

### Cosa Sono le Business Rules

**Business Rules** = Regole che fanno guadagnare o risparmiare denaro.
- Sono **agnostiche dal software** (esistevano prima del software, esisteranno dopo)
- Esempio: "Tasso di interesse del 5% sul prestito"

### Entities: La Trasposizione Software

**Entity** = Oggetto software che contiene dati e metodi per applicare una Business Rule.

**Esempio concreto:**
```csharp
// Business Rule: "Calcola interesse su prestito"
class Loan {
    // Dati
    decimal Amount { get; set; }
    decimal InterestRate { get; set; }

    // Metodo che applica la business rule
    decimal CalculateTotalAmount() {
        return Amount * (1 + InterestRate);
    }
}
```

### Caratteristiche delle Entities

1. **Indipendenti** - Non dipendono da database, UI, framework
2. **Riutilizzabili** - Possono essere usate in contesti diversi
3. **Testabili** - Senza dipendenze esterne
4. **Core del sistema** - Il codice più importante

---

## 📢 CAP. 21: SCREAMING ARCHITECTURE

### Un'Architettura Deve "Urlare" il Suo Scopo

**Analogia della casa:**
- Vedendo i piani di una casa → capisci subito "È una casa!" (cucina, camere, bagno)
- Vedendo i piani di un ospedale → capisci subito "È un ospedale!" (sale operatorie, degenze)

**Stesso per il software:**
- Vedendo la struttura → devi capire "È un sistema di notifiche!"
- Non → "È un progetto ASP.NET MVC!"

**Anti-pattern:**
```
❌ Controllers/
❌ Models/
❌ Views/
❌ Services/
```
→ Questo urla "Sono MVC!" non "Sono un e-commerce!"

**Pattern corretto:**
```
✅ Notifications/
✅ Templates/
✅ Delivery/
✅ Channels/
```
→ Questo urla "Sono un sistema di notifiche!"

### Architettura ≠ Framework

**Architettura** = Organizzazione del sistema (business logic, use cases, entities)
**Framework** = Dettaglio implementativo (ASP.NET, Express, Django)

**Concetto chiave:**
> La stessa architettura può essere implementata con .NET, Java, Node.js, Python...

Le **business rules** (tasso interesse, retry delle notifiche) **non cambiano** se:
- Passi da PostgreSQL a MongoDB
- Passi da .NET a Java
- Passi da REST a gRPC

---

## 🎯 CAP. 22: CLEAN ARCHITECTURE

### I 4 Layer (Cerchi Concentrici)

```
┌─────────────────────────────────────────────┐
│  FRAMEWORKS & DRIVERS (External)            │  ← UI, DB, Devices
│  ┌───────────────────────────────────────┐  │
│  │  INTERFACE ADAPTERS (Controllers)     │  │  ← Trasformatori
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  USE CASES (Application)        │  │  │  ← Regole app
│  │  │  ┌───────────────────────────┐  │  │  │
│  │  │  │  ENTITIES (Domain)        │  │  │  │  ← Business Rules
│  │  │  └───────────────────────────┘  │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

#### 1. **Entities (Domain)** - Cerchio più interno
- Business Rules pure
- Zero dipendenze esterne
- Esempio: `Notification`, `Template`, `DeliveryAttempt`

#### 2. **Use Cases (Application)**
- Regole di business specifiche dell'applicazione
- Orchestrano le entities
- Esempio: `SendNotificationUseCase`, `ScheduleNotificationUseCase`

#### 3. **Interface Adapters (Controllers)**
- Trasformano dati tra formati
- Esempio: HTTP request → Domain object, Domain object → JSON response

#### 4. **Frameworks & Drivers (External)**
- UI, Database, External services
- Dettagli implementativi
- Esempio: ASP.NET, PostgreSQL, Redis

---

### The Dependency Rule (La Regola d'Oro)

> **Le dipendenze puntano SOLO verso l'interno**

```
External  →  Controllers  →  Use Cases  →  Entities
  ✅           ✅             ✅             ✅

Entities  →  Use Cases  →  Controllers  →  External
  ❌           ❌             ❌             ❌
```

**Significa:**
- ✅ Use Cases **possono** usare Entities
- ✅ Controllers **possono** usare Use Cases
- ❌ Entities **non possono** usare Use Cases
- ❌ Use Cases **non possono** usare Controllers
- ❌ Domain **non può** usare Entity Framework, ASP.NET, PostgreSQL

---

### Programmazione vs Astrazione

| Layer | Livello Programmazione | Livello Astrazione | Esempio |
|-------|------------------------|-------------------|---------|
| **External** | Alto (codice concreto) | Basso | `PostgresRepository`, `ASP.NET Controller` |
| **Controllers** | Medio | Medio | `NotificationMapper` |
| **Use Cases** | Medio | Medio-Alto | `INotificationRepository` (interfaccia) |
| **Entities** | Basso (codice astratto) | Alto | `Notification` (business logic pura) |

**External**: Codice molto concreto e specifico (PostgreSQL, ASP.NET)
**Entities**: Codice astratto e generale (business rules universali)

---

### Adapters: I Trasformatori

**Adapter Pattern** permette la comunicazione tra layer:

**Input Adapter** (esterno → interno):
```csharp
// HTTP DTO → Domain Object
var notification = new Notification {
    Recipient = dto.Email,
    Content = dto.Message,
    Channel = NotificationChannel.Email
};
```

**Output Adapter** (interno → esterno):
```csharp
// Domain Object → HTTP Response
var response = new NotificationResponseDto {
    Id = notification.Id,
    Status = notification.Status.ToString(),
    SentAt = notification.SentAt
};
```

---

## 🎯 VANTAGGI DELLA CLEAN ARCHITECTURE

### 1. **Testabilità** 🧪
Posso testare business logic **senza**:
- ❌ Database reale
- ❌ API HTTP
- ❌ Redis
- ❌ External services

**Esempio:**
```csharp
[Test]
public void Notification_CanRetry_WhenHighPriority() {
    // Arrange
    var notification = new Notification(Priority.High);

    // Act
    var canRetry = notification.CanRetry(attemptNumber: 3);

    // Assert
    Assert.IsTrue(canRetry);  // High priority → 5 retry
}
```
✅ Zero dipendenze
✅ Test velocissimo
✅ Reliable

### 2. **Estensibilità** 🔧
Posso **cambiare** senza toccare business logic:
- Database: PostgreSQL → MongoDB
- Framework: ASP.NET → gRPC
- Cache: Redis → Memcached

### 3. **Compartimentazione** 📦
Ogni layer ha responsabilità chiare:
- Domain: Business rules
- Application: Use cases
- Infrastructure: Implementazioni tecniche
- Api: Esposizione HTTP

### 4. **Framework Independence** 🆓
Non sei legato a un framework specifico:
- Puoi passare da .NET a Java
- Puoi passare da Express a NestJS
- La business logic rimane identica

---

## 🔗 NEL NOSTRO PROGETTO

### Struttura
```
NotificationService.Domain         ← Entities (Notification, Template)
NotificationService.Application    ← Use Cases (SendNotification)
NotificationService.Infrastructure ← Adapters (PostgresRepository)
NotificationService.Api            ← Controllers (NotificationController)
```

### Esempio Concreto: Send Notification

#### **1. Domain (Entity)**
```csharp
// Business Rule pura
class Notification {
    NotificationStatus Status { get; private set; }

    void Send() {
        if (Status != NotificationStatus.Pending)
            throw new InvalidOperationException();

        Status = NotificationStatus.Sent;
        SentAt = DateTime.UtcNow;
    }
}
```
✅ Zero dipendenze
✅ Testabile senza infrastruttura

#### **2. Application (Use Case)**
```csharp
// Regola applicativa: "Invia notifica e salva"
class SendNotificationUseCase {
    INotificationRepository _repo;  // ← Interfaccia (astrazione!)
    INotificationSender _sender;

    async Task Execute(Guid id) {
        var notification = await _repo.GetById(id);

        notification.Send();  // ← Business logic nel Domain

        await _sender.SendAsync(notification);
        await _repo.Update(notification);
    }
}
```
✅ Dipende da **interfacce** (nel Domain)
✅ Non sa se è PostgreSQL o MongoDB

#### **3. Infrastructure (Adapter)**
```csharp
// Implementazione concreta
class PostgresNotificationRepository : INotificationRepository {
    DbContext _context;

    async Task<Notification> GetById(Guid id) {
        var entity = await _context.Notifications.FindAsync(id);
        return MapToDomain(entity);  // ← Adapter: DB → Domain
    }

    async Task Update(Notification notification) {
        var entity = MapToDb(notification);  // ← Adapter: Domain → DB
        _context.Notifications.Update(entity);
        await _context.SaveChangesAsync();
    }
}
```
✅ Dipende verso l'interno (implementa interfaccia Domain)
✅ Domain non sa nulla di EF Core

#### **4. Api (Controller)**
```csharp
// Esposizione HTTP
[ApiController]
[Route("api/notifications")]
class NotificationController {
    SendNotificationUseCase _useCase;

    [HttpPost("{id}/send")]
    async Task<IActionResult> Send(Guid id) {
        await _useCase.Execute(id);
        return Ok();
    }
}
```
✅ Dipende verso l'interno (usa Use Case)
✅ Use Case non sa nulla di HTTP

---

## 💻 ESEMPIO COMPLETO: CLEAN ARCHITECTURE IN PRATICA

> Esempio end-to-end: Sistema bancario con operazione "Deposita denaro"

### Scenario
**Business Rule:** "Un deposito deve essere positivo e incrementa il saldo del conto"

Vediamo come implementarlo seguendo Clean Architecture.

---

### 1️⃣ **DOMAIN LAYER** (Cerchio interno)

#### `BankAccount.cs` (Entity)
```csharp
namespace BankingSystem.Domain.Entities;

// 🎯 Entity: Business logic PURA, ZERO dipendenze esterne
public class BankAccount
{
    public Guid Id { get; private set; }
    public string AccountNumber { get; private set; }
    public decimal Balance { get; private set; }
    public DateTime CreatedAt { get; private set; }
    public DateTime? LastTransactionAt { get; private set; }

    // Constructor
    private BankAccount() { } // *Per EF Core (vedi nota sotto)

    public BankAccount(string accountNumber)
    {
        Id = Guid.NewGuid();
        AccountNumber = accountNumber;
        Balance = 0;
        CreatedAt = DateTime.UtcNow;
    }

    // 🔥 BUSINESS RULE: Deposito deve essere positivo
    public void Deposit(decimal amount)
    {
        if (amount <= 0)
            throw new InvalidOperationException("Deposit amount must be positive");

        Balance += amount;
        LastTransactionAt = DateTime.UtcNow;
    }

    // 🔥 BUSINESS RULE: Prelievo non può eccedere saldo
    public void Withdraw(decimal amount)
    {
        if (amount <= 0)
            throw new InvalidOperationException("Withdrawal amount must be positive");

        if (amount > Balance)
            throw new InvalidOperationException("Insufficient balance");

        Balance -= amount;
        LastTransactionAt = DateTime.UtcNow;
    }
}
```

**✅ Caratteristiche:**
- Zero dipendenze esterne (no database, no framework)
- Business logic tutta qui
- Testabile senza infrastruttura

#### `IBankAccountRepository.cs` (Interfaccia nel Domain!)
```csharp
namespace BankingSystem.Domain.Repositories;

// 🎯 Interfaccia nel DOMAIN (non in Infrastructure!)
// Questo è il DIP (Dependency Inversion Principle)
public interface IBankAccountRepository
{
    Task<BankAccount?> GetByIdAsync(Guid id);
    Task<BankAccount?> GetByAccountNumberAsync(string accountNumber);
    Task SaveAsync(BankAccount account);
}
```

**✅ Perché nel Domain?**
- Il Domain **possiede** l'astrazione
- Infrastructure **implementa** l'astrazione
- Dependency Inversion: Infrastructure dipende da Domain!

---

### 2️⃣ **APPLICATION LAYER** (Use Cases)

#### `DepositMoneyRequest.cs` (DTO)
```csharp
namespace BankingSystem.Application.UseCases.DepositMoney;

// DTO per il Use Case
public record DepositMoneyRequest(
    string AccountNumber,
    decimal Amount
);
```

#### `DepositMoneyUseCase.cs` (Orchestrazione)
```csharp
namespace BankingSystem.Application.UseCases.DepositMoney;

// 🎯 Use Case: Regola applicativa (non business rule!)
// Regola: "Per depositare, trova il conto e salva"
public class DepositMoneyUseCase
{
    private readonly IBankAccountRepository _repository;

    // ✅ Dipende da INTERFACCIA (nel Domain)
    public DepositMoneyUseCase(IBankAccountRepository repository)
    {
        _repository = repository;
    }

    public async Task ExecuteAsync(DepositMoneyRequest request)
    {
        // 1. Trova il conto
        var account = await _repository.GetByAccountNumberAsync(request.AccountNumber);

        if (account == null)
            throw new InvalidOperationException($"Account {request.AccountNumber} not found");

        // 2. Esegui business logic (nel Domain!)
        account.Deposit(request.Amount);

        // 3. Salva
        await _repository.SaveAsync(account);
    }
}
```

**✅ Caratteristiche:**
- Dipende da **IBankAccountRepository** (interfaccia nel Domain)
- Non sa se è PostgreSQL, MongoDB, o memoria
- Orchestrazione: trova → esegui → salva

---

### 3️⃣ **INFRASTRUCTURE LAYER** (Dettagli implementativi)

#### `BankAccountDbEntity.cs` (Modello EF Core)
```csharp
namespace BankingSystem.Infrastructure.Persistence.Models;

// 🎯 Modello database (dettaglio implementativo)
// Separato dall'Entity del Domain!
public class BankAccountDbEntity
{
    public Guid Id { get; set; }
    public string AccountNumber { get; set; } = string.Empty;
    public decimal Balance { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime? LastTransactionAt { get; set; }
}
```

#### `PostgresBankAccountRepository.cs` (Implementazione)
```csharp
namespace BankingSystem.Infrastructure.Persistence.Repositories;

// 🎯 Implementazione CONCRETA (PostgreSQL con EF Core)
// ✅ Implementa interfaccia del DOMAIN
public class PostgresBankAccountRepository : IBankAccountRepository
{
    private readonly ApplicationDbContext _context;

    public PostgresBankAccountRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<BankAccount?> GetByIdAsync(Guid id)
    {
        var dbEntity = await _context.BankAccounts.FindAsync(id);

        if (dbEntity == null)
            return null;

        // 🔄 ADAPTER: DB Entity → Domain Entity
        return MapToDomain(dbEntity);
    }

    public async Task<BankAccount?> GetByAccountNumberAsync(string accountNumber)
    {
        var dbEntity = await _context.BankAccounts
            .FirstOrDefaultAsync(x => x.AccountNumber == accountNumber);

        if (dbEntity == null)
            return null;

        return MapToDomain(dbEntity);
    }

    public async Task SaveAsync(BankAccount account)
    {
        var existing = await _context.BankAccounts.FindAsync(account.Id);

        if (existing == null)
        {
            // Nuovo conto
            var dbEntity = MapToDb(account);
            _context.BankAccounts.Add(dbEntity);
        }
        else
        {
            // Aggiorna esistente
            existing.Balance = account.Balance;
            existing.LastTransactionAt = account.LastTransactionAt;
        }

        await _context.SaveChangesAsync();
    }

    // 🔄 ADAPTER: Domain → DB
    private BankAccountDbEntity MapToDb(BankAccount domain)
    {
        return new BankAccountDbEntity
        {
            Id = domain.Id,
            AccountNumber = domain.AccountNumber,
            Balance = domain.Balance,
            CreatedAt = domain.CreatedAt,
            LastTransactionAt = domain.LastTransactionAt
        };
    }

    // 🔄 ADAPTER: DB → Domain
    private BankAccount MapToDomain(BankAccountDbEntity db)
    {
        // Usa reflection o factory per creare l'entity
        var account = (BankAccount)Activator.CreateInstance(
            typeof(BankAccount),
            nonPublic: true
        )!;

        // Setta le proprietà private via reflection
        typeof(BankAccount).GetProperty("Id")!.SetValue(account, db.Id);
        typeof(BankAccount).GetProperty("AccountNumber")!.SetValue(account, db.AccountNumber);
        typeof(BankAccount).GetProperty("Balance")!.SetValue(account, db.Balance);
        // ... etc

        return account;
    }
}
```

**✅ Caratteristiche:**
- Implementa **IBankAccountRepository** (dal Domain)
- Usa EF Core (dettaglio implementativo)
- **Adapter**: trasforma tra DB model e Domain Entity
- Domain non sa NULLA di EF Core o PostgreSQL

---

### 4️⃣ **API LAYER** (Controllers - Esposizione HTTP)

#### `DepositMoneyDto.cs` (DTO HTTP)
```csharp
namespace BankingSystem.Api.Dtos;

// DTO per HTTP request
public record DepositMoneyDto(
    string AccountNumber,
    decimal Amount
);
```

#### `BankAccountController.cs` (Controller)
```csharp
namespace BankingSystem.Api.Controllers;

[ApiController]
[Route("api/accounts")]
public class BankAccountController : ControllerBase
{
    private readonly DepositMoneyUseCase _depositUseCase;

    // ✅ Dipende dal Use Case
    public BankAccountController(DepositMoneyUseCase depositUseCase)
    {
        _depositUseCase = depositUseCase;
    }

    [HttpPost("{accountNumber}/deposit")]
    public async Task<IActionResult> Deposit(
        string accountNumber,
        [FromBody] DepositMoneyDto dto)
    {
        try
        {
            // 🔄 ADAPTER: HTTP DTO → Use Case Request
            var request = new DepositMoneyRequest(
                AccountNumber: accountNumber,
                Amount: dto.Amount
            );

            await _depositUseCase.ExecuteAsync(request);

            return Ok(new { message = "Deposit successful" });
        }
        catch (InvalidOperationException ex)
        {
            return BadRequest(new { error = ex.Message });
        }
    }
}
```

**✅ Caratteristiche:**
- Dipende da **DepositMoneyUseCase** (Application)
- Trasforma: HTTP DTO → Use Case Request (Adapter)
- Use Case non sa NULLA di HTTP, ASP.NET, JSON

---

### 5️⃣ **DEPENDENCY INJECTION** (Startup/Program.cs)

```csharp
// Program.cs (ASP.NET 8)
var builder = WebApplication.CreateBuilder(args);

// Infrastructure
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("Default")));

// ✅ Registra implementazione Infrastructure per interfaccia Domain
builder.Services.AddScoped<IBankAccountRepository, PostgresBankAccountRepository>();

// Application (Use Cases)
builder.Services.AddScoped<DepositMoneyUseCase>();

var app = builder.Build();
app.MapControllers();
app.Run();
```

---

### 📊 FLUSSO COMPLETO

```
1. HTTP POST /api/accounts/IT123/deposit { "amount": 100 }
                     ↓
2. BankAccountController (Api Layer)
   - Riceve DepositMoneyDto
   - Trasforma in DepositMoneyRequest
                     ↓
3. DepositMoneyUseCase (Application Layer)
   - Chiama repository.GetByAccountNumber("IT123")
                     ↓
4. PostgresBankAccountRepository (Infrastructure)
   - Query a PostgreSQL via EF Core
   - Trasforma BankAccountDbEntity → BankAccount (Domain)
                     ↓
5. BankAccount (Domain) ritorna al Use Case
                     ↓
6. DepositMoneyUseCase
   - Chiama account.Deposit(100)  ← BUSINESS LOGIC!
                     ↓
7. BankAccount.Deposit(100)
   - Valida: amount > 0
   - Balance += 100
   - LastTransactionAt = now
                     ↓
8. DepositMoneyUseCase
   - Chiama repository.SaveAsync(account)
                     ↓
9. PostgresBankAccountRepository
   - Trasforma BankAccount → BankAccountDbEntity
   - Salva in PostgreSQL via EF Core
                     ↓
10. Risposta OK al client
```

---

### 🎯 DEPENDENCY RULE IN AZIONE

```
Api Layer (Controller)
    ↓ dipende da
Application Layer (Use Case)
    ↓ dipende da
Domain Layer (IBankAccountRepository interfaccia)
    ↑ implementata da
Infrastructure Layer (PostgresBankAccountRepository)
```

**Nota:** Infrastructure dipende da Domain (inverted!), non viceversa.

---

### ✅ VANTAGGI DIMOSTRATI

#### **1. Testabilità**
```csharp
[Test]
public void Deposit_IncreasesBalance()
{
    // Arrange
    var account = new BankAccount("IT123");

    // Act
    account.Deposit(100);

    // Assert
    Assert.AreEqual(100, account.Balance);
}
```
✅ Zero dipendenze, test istantaneo

#### **2. Cambiare Database**
```csharp
// Voglio passare a MongoDB?
public class MongoBankAccountRepository : IBankAccountRepository
{
    // Implementazione MongoDB
}

// In Startup:
services.AddScoped<IBankAccountRepository, MongoBankAccountRepository>();
```
✅ Domain, Application, Api → **zero modifiche**

#### **3. Cambiare Framework**
```csharp
// Voglio passare da ASP.NET a gRPC?
// - Creo nuovo GrpcBankAccountService
// - Uso stesso DepositMoneyUseCase
```
✅ Domain, Application → **zero modifiche**

---

### 🧪 TEST CON MOCK

```csharp
[Test]
public async Task DepositMoneyUseCase_CallsRepository()
{
    // Arrange
    var mockRepo = new Mock<IBankAccountRepository>();
    var account = new BankAccount("IT123");

    mockRepo.Setup(x => x.GetByAccountNumberAsync("IT123"))
            .ReturnsAsync(account);

    var useCase = new DepositMoneyUseCase(mockRepo.Object);
    var request = new DepositMoneyRequest("IT123", 100);

    // Act
    await useCase.ExecuteAsync(request);

    // Assert
    Assert.AreEqual(100, account.Balance);
    mockRepo.Verify(x => x.SaveAsync(account), Times.Once);
}
```
✅ Testo Use Case senza database reale!

---

## ⚠️ NOTA IMPORTANTE: PURISTA VS PRAGMATICO

### 🚨 Il Problema del Costruttore Privato

Nell'esempio sopra hai visto:
```csharp
private BankAccount() { } // *Per EF Core
```

**Domanda critica:** Perché il Domain menziona EF Core?

**Risposta:** Questo è un **compromesso** tra teoria e pratica. Esistono **2 approcci** per gestire la persistenza in Clean Architecture.

---

### 🎯 APPROCCIO 1: PURISTA (Domain 100% Pulito)

**Filosofia:** Domain e Infrastructure completamente separati, **zero compromessi**.

#### Implementazione

**Domain Entity (pura):**
```csharp
// Domain/Entities/BankAccount.cs
// ✅ NESSUNA concessione all'ORM
public class BankAccount
{
    public Guid Id { get; private set; }
    public decimal Balance { get; private set; }

    // Solo costruttore business
    public BankAccount(string accountNumber) {
        Id = Guid.NewGuid();
        Balance = 0;
        // ...
    }

    public void Deposit(decimal amount) {
        if (amount <= 0) throw new InvalidOperationException();
        Balance += amount;
    }
}
```

**Infrastructure DB Model (separato):**
```csharp
// Infrastructure/Persistence/Models/BankAccountDbEntity.cs
// ✅ Modello SEPARATO per il database
public class BankAccountDbEntity
{
    public Guid Id { get; set; }              // ← Setter pubblico per EF Core
    public string AccountNumber { get; set; } // ← Setter pubblico
    public decimal Balance { get; set; }      // ← Setter pubblico
    public DateTime CreatedAt { get; set; }
}
```

**Repository con Mapping:**
```csharp
// Infrastructure/Persistence/Repositories/PostgresBankAccountRepository.cs
public class PostgresBankAccountRepository : IBankAccountRepository
{
    private readonly DbContext _context;

    public async Task<BankAccount?> GetByIdAsync(Guid id)
    {
        var dbEntity = await _context.BankAccounts.FindAsync(id);
        if (dbEntity == null) return null;

        // 🔄 ADAPTER: DB → Domain
        return MapToDomain(dbEntity);
    }

    public async Task SaveAsync(BankAccount account)
    {
        var existing = await _context.BankAccounts.FindAsync(account.Id);

        if (existing == null) {
            // 🔄 ADAPTER: Domain → DB
            var dbEntity = MapToDb(account);
            _context.BankAccounts.Add(dbEntity);
        } else {
            // Aggiorna solo i campi modificabili
            existing.Balance = account.Balance;
            existing.LastTransactionAt = account.LastTransactionAt;
        }

        await _context.SaveChangesAsync();
    }

    private BankAccount MapToDomain(BankAccountDbEntity db)
    {
        // Ricrea l'entity usando factory o reflection
        var account = BankAccountFactory.Reconstitute(
            id: db.Id,
            accountNumber: db.AccountNumber,
            balance: db.Balance,
            createdAt: db.CreatedAt
        );
        return account;
    }

    private BankAccountDbEntity MapToDb(BankAccount domain)
    {
        return new BankAccountDbEntity {
            Id = domain.Id,
            AccountNumber = domain.AccountNumber,
            Balance = domain.Balance,
            CreatedAt = domain.CreatedAt
        };
    }
}
```

#### ✅ Vantaggi
- **Domain 100% pulito** - Zero dipendenze da ORM
- **Testabilità massima** - Nessun compromesso
- **Indipendenza totale** - Posso cambiare ORM senza toccare Domain
- **Best practice** - Raccomandato da Uncle Bob

#### ❌ Svantaggi
- **Duplicazione** - 2 classi per ogni entity (Domain + DB)
- **Mapping costante** - Devo trasformare sempre Domain ↔ DB
- **Più codice** - Più verbose, più manutenzione
- **Performance** - Overhead del mapping (minimo, ma c'è)

---

### ⚖️ APPROCCIO 2: PRAGMATICO (Compromesso)

**Filosofia:** Usare la stessa classe per Domain e ORM, con piccole concessioni.

#### Implementazione

**Domain Entity (con concessione):**
```csharp
// Domain/Entities/BankAccount.cs
// ⚠️ Concessione: costruttore privato per EF Core
public class BankAccount
{
    public Guid Id { get; private set; }
    public decimal Balance { get; private set; }

    // ⚠️ Costruttore per EF Core (concessione all'ORM)
    private BankAccount() { }

    // Costruttore business
    public BankAccount(string accountNumber) {
        Id = Guid.NewGuid();
        Balance = 0;
    }

    public void Deposit(decimal amount) {
        if (amount <= 0) throw new InvalidOperationException();
        Balance += amount;
    }
}
```

**Repository (senza mapping):**
```csharp
// Infrastructure/Persistence/Repositories/PostgresBankAccountRepository.cs
public class PostgresBankAccountRepository : IBankAccountRepository
{
    private readonly DbContext _context;

    public async Task<BankAccount?> GetByIdAsync(Guid id)
    {
        // ✅ EF Core usa direttamente BankAccount (Domain)
        return await _context.BankAccounts.FindAsync(id);
    }

    public async Task SaveAsync(BankAccount account)
    {
        _context.BankAccounts.Update(account);
        await _context.SaveChangesAsync();
    }
}
```

**DbContext Configuration:**
```csharp
// Infrastructure/Persistence/ApplicationDbContext.cs
public class ApplicationDbContext : DbContext
{
    public DbSet<BankAccount> BankAccounts { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Configura EF Core per usare BankAccount (Domain)
        modelBuilder.Entity<BankAccount>(entity => {
            entity.HasKey(x => x.Id);
            entity.Property(x => x.Balance).IsRequired();
            // ...
        });
    }
}
```

#### ✅ Vantaggi
- **Meno codice** - Nessuna duplicazione
- **Più veloce** - Nessun mapping, implementazione rapida
- **Meno manutenzione** - Una sola classe da gestire
- **Pragmatico** - Usato in molti progetti reali

#### ❌ Svantaggi
- **Domain "inquinato"** - Costruttore privato è una concessione all'ORM
- **Accoppiamento nascosto** - Domain conosce (implicitamente) l'ORM
- **Meno flessibile** - Cambiare ORM richiede modifiche al Domain
- **Viola Clean Architecture ortodossa** - Non è "purista"

---

### 🎯 QUALE USARE NEL NOSTRO PROGETTO?

**Per P1 - Notification Service, useremo l'APPROCCIO PURISTA.**

#### 📋 Motivi:

1. **🎓 Progetto didattico**
   - Vogliamo imparare Clean Architecture nel modo **corretto**
   - Meglio imparare l'approccio ortodosso prima

2. **📚 Best practice**
   - Uncle Bob raccomanda separazione totale
   - È il modo "giusto" di fare Clean Architecture

3. **🔧 Flessibilità**
   - Se domani cambiamo da PostgreSQL a MongoDB
   - Se domani cambiamo da EF Core a Dapper
   - → Domain rimane **identico**

4. **✅ Testabilità**
   - Domain completamente indipendente
   - Zero dipendenze nascoste

#### 📂 Struttura nel nostro progetto:

```
NotificationService.Domain/
  Entities/
    Notification.cs          ← Entity pura
    Template.cs
    DeliveryAttempt.cs
  Repositories/
    INotificationRepository.cs  ← Interfaccia

NotificationService.Infrastructure/
  Persistence/
    Models/
      NotificationDbEntity.cs   ← Modello EF Core
      TemplateDbEntity.cs
      DeliveryAttemptDbEntity.cs
    Repositories/
      PostgresNotificationRepository.cs  ← Mapping Domain ↔ DB
```

---

### 🎓 QUANDO USARE IL PRAGMATICO?

L'approccio pragmatico è accettabile quando:
- ✅ Progetto piccolo/prototipo
- ✅ Deadline strette
- ✅ Team che non conosce Clean Architecture
- ✅ Non prevedi di cambiare ORM

**Ma per imparare, usa sempre il Purista!** 💪

---

### 🚩 REGOLA D'ORO

> **Se il Domain menziona (anche solo in un commento) Infrastructure, Framework, Database, ORM → RED FLAG!**

Il Domain deve essere **beatamente ignorante** di tutto ciò che sta nel cerchio esterno.

**Test rapido:**
- Posso compilare `Domain.csproj` senza dipendenze esterne? → ✅ Purista
- `Domain.csproj` dipende da EF Core? → ❌ Compromesso

---

## 🧠 CONCETTI CHIAVE DA RICORDARE

1. **Entities** = Trasposizione software di Business Rules
2. **Business Rules** = Regole che fanno guadagnare/risparmiare denaro
3. **Dependency Rule** = Dipendenze puntano SOLO verso l'interno
4. **Architettura ≠ Framework** = L'architettura è indipendente dalla tecnologia
5. **Screaming Architecture** = La struttura deve urlare il suo scopo
6. **Testabilità** = Business logic testabile senza infrastruttura
7. **Adapters** = Trasformano dati tra layer (esterno ↔ interno)

---

## 📝 QUIZ

### Domanda 1: Business Rules
**Scenario:** Stai costruendo un sistema bancario. Quale di queste è una **Business Rule**?

a) "I dati sono salvati in PostgreSQL"
b) "Il tasso di interesse su un prestito è del 5% annuo"
c) "L'API è esposta tramite REST"
d) "Il frontend usa React"

<details>
<summary>Risposta</summary>

**b) "Il tasso di interesse su un prestito è del 5% annuo"**

**Perché:**
- È una regola che fa guadagnare denaro
- È agnostica dalla tecnologia
- Esisteva prima del software
- Le altre sono dettagli implementativi (database, API, UI)
</details>

---

### Domanda 2: Dependency Rule
**Scenario:** Hai questi layer:
- Domain (Entities)
- Application (Use Cases)
- Infrastructure (Database)

Quale dipendenza è **CORRETTA**?

a) `Notification` (Domain) dipende da `DbContext` (Infrastructure)
b) `SendNotificationUseCase` (Application) dipende da `Notification` (Domain)
c) `INotificationRepository` (interfaccia) sta in Infrastructure
d) Domain dipende da Application

<details>
<summary>Risposta</summary>

**b) `SendNotificationUseCase` (Application) dipende da `Notification` (Domain)**

**Perché:**
- ✅ Application può dipendere da Domain (verso l'interno)
- ❌ Domain NON può dipendere da Infrastructure (verso l'esterno)
- ❌ `INotificationRepository` deve stare nel Domain (non Infrastructure)
- ❌ Domain NON può dipendere da Application (verso l'esterno)
</details>

---

### Domanda 3: Testabilità
**Perché la Clean Architecture migliora la testabilità?**

a) Perché usa design pattern avanzati
b) Perché le business rules non dipendono da database/API/framework
c) Perché ha più layer
d) Perché usa interfacce

<details>
<summary>Risposta</summary>

**b) Perché le business rules non dipendono da database/API/framework**

**Perché:**
- Posso testare `Notification.Send()` senza database reale
- Posso testare `CanRetry()` senza API HTTP
- Test velocissimi (millisecondi)
- Test affidabili (non falliscono per problemi di rete)
- Le interfacce aiutano, ma la chiave è l'**indipendenza dalle dipendenze esterne**
</details>

---

### Domanda 4: Screaming Architecture
**Quale struttura "urla" meglio il suo scopo?**

**Opzione A:**
```
Controllers/
Models/
Views/
Services/
```

**Opzione B:**
```
Orders/
Products/
Payments/
Shipping/
```

<details>
<summary>Risposta</summary>

**Opzione B**

**Perché:**
- Opzione A urla "Sono MVC!" (framework)
- Opzione B urla "Sono un e-commerce!" (business domain)
- La struttura deve rivelare il **cosa fa** il sistema, non il **come è fatto**
</details>

---

### Domanda 5: Adapters
**A cosa servono gli Adapter nella Clean Architecture?**

a) A far comunicare il frontend con il backend
b) A trasformare dati tra formati diversi (es: HTTP DTO → Domain Object)
c) A migliorare le performance
d) A gestire gli errori

<details>
<summary>Risposta</summary>

**b) A trasformare dati tra formati diversi (es: HTTP DTO → Domain Object)**

**Perché:**
- Adapter trasforma: HTTP request → Domain object (input)
- Adapter trasforma: Domain object → JSON response (output)
- Esempio: `NotificationController` riceve `NotificationDto` (HTTP) e lo converte in `Notification` (Domain)
- Permettono ai layer di parlare linguaggi diversi mantenendo la separazione
</details>

---

### Domanda 6: Framework Independence
**Cosa significa "Framework Independence"?**

a) Non posso usare framework
b) L'architettura può essere implementata con framework diversi senza cambiare business logic
c) Devo scrivere tutto da zero
d) I framework sono nel Domain layer

<details>
<summary>Risposta</summary>

**b) L'architettura può essere implementata con framework diversi senza cambiare business logic**

**Perché:**
- Posso passare da .NET a Java → business logic rimane identica
- Posso passare da PostgreSQL a MongoDB → entities non cambiano
- Posso passare da REST a gRPC → use cases non cambiano
- I framework sono **dettagli** (layer esterno), non il core
</details>

---

## Collegamenti

- [[clean-architecture]] - Overview completa dei 4 layer
- [[domain-model-patterns]] - Entity vs Value Object in dettaglio
- [[domain-events]] - Come le Entities comunicano cambiamenti

---

## Risorse per Approfondire

- **Libro: "Clean Architecture" - Robert C. Martin, Cap. 20-22** - La fonte primaria. Spiega Entities, Screaming Architecture, e i 4 layer in dettaglio.

- **[The Clean Architecture - Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** - L'articolo originale che ha definito il pattern.

- **[Entities in DDD - Martin Fowler](https://martinfowler.com/bliki/EvansClassification.html)** - Come le Entities si collegano al Domain-Driven Design.

- **[Clean Architecture Solution Template](https://github.com/jasontaylordev/CleanArchitecture)** - Esempio pratico .NET di come strutturare le Entities.

- **Libro: "Domain-Driven Design" - Eric Evans, Cap. 5** - Trattazione originale delle Entities nel contesto DDD.

---

*Creato: 2026-02-09 | P1 - Week 2*
