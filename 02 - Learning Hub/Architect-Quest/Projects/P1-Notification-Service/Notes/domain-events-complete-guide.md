---
tags:
  - p1
  - architecture
  - domain-events
  - from/week-02
  - status/learned
aliases:
  - Domain Events Guide
  - Guida Domain Events
created: 2026-02-13
source: "Sessione Week 2 + Articoli (Fowler, Microsoft, Bogard, Jovanović)"
---

# Domain Events in .NET — Riassunto Completo

> **One-liner:** Guida completa ai Domain Events con esempio pratico Dapper + SQL Server + MediatR.

## Indice

1. [Cos'è un Domain Event](#1-cosè-un-domain-event)
2. [Domain Event vs Integration Event](#2-domain-event-vs-integration-event)
3. [Approccio Statico vs Deferred](#3-approccio-statico-vs-deferred)
4. [Componenti in gioco](#4-componenti-in-gioco)
5. [Il Change Tracker di EF Core](#5-il-change-tracker-di-ef-core)
6. [Il Command Pattern](#6-il-command-pattern)
7. [MediatR — Panoramica](#7-mediatr--panoramica)
8. [Esempio completo: Dapper + SQL Server + MediatR](#8-esempio-completo)
9. [Fonti](#9-fonti)

---

## 1. Cos'è un Domain Event

Un oggetto immutabile che cattura il fatto che **qualcosa di interessante è accaduto** nel dominio. Serve a disaccoppiare i side effect dalla logica principale.

Senza domain event, se alla creazione di un ordine devi anche creare un buyer, mandare un'email e riservare lo stock, tutta quella logica finisce nel command handler che diventa un mostro con decine di dipendenze.

Con i domain event, l'entità dice "è successo X" e gli handler reagiscono separatamente:

```
CreateOrder command
   └─► Order aggregate → Raise(OrderStartedEvent)
                              │
                              ├── Handler 1: Crea buyer
                              ├── Handler 2: Manda email
                              ├── Handler 3: Riserva stock
                              └── Handler N: ...qualsiasi cosa futura
```

Ogni handler è una classe isolata. Aggiungerne uno nuovo = creare un file nuovo, senza toccare niente di esistente → **Open/Closed Principle**.

### Convenzioni

- **Immutabili**: un evento è un fatto passato, non cambia mai
- **Naming al passato**: `OrderPlacedEvent`, `CourseCompletedEvent`
- **Fat vs Thin**: un evento "fat" contiene tutti i dati necessari, uno "thin" contiene solo l'Id e l'handler si carica il resto

### Tipi di evento: sottotipi vs event type object

Se eventi diversi hanno **dati strutturalmente diversi** → usa sottotipi (classi separate):

```csharp
public record OrderPlaced(Guid OrderId, List<Item> Items, decimal Total) : IDomainEvent;
public record OrderShipped(Guid OrderId, string TrackingNumber) : IDomainEvent;
```

Se eventi diversi hanno gli **stessi campi** ma comportamenti diversi → usa un'unica classe + un enum:

```csharp
public enum DocumentActionType { Viewed, Downloaded, Printed, Shared, Archived }

public record DocumentAction(Guid DocId, Guid UserId, DocumentActionType ActionType)
    : IDomainEvent;
```

Una classe, cinque comportamenti. L'event processor fa dispatch su `ActionType`.

---

## 2. Domain Event vs Integration Event

| | Domain Event | Integration Event |
|---|---|---|
| **Scope** | Stesso processo, stesso dominio | Tra microservizi / Bounded Context |
| **Trasporto** | In-memory (MediatR) | Bus asincrono (RabbitMQ, Azure Service Bus) |
| **Transazione** | Può stare nella stessa transazione DB | Avviene solo dopo il commit |
| **Scopo** | Coordinare aggregati nello stesso dominio | Propagare stato verso l'esterno |

Un domain event handler può **generare** un integration event — è il ponte tra i due mondi. L'integration event viene salvato in una tabella **outbox** durante la transazione, e un processo separato lo dispatcha dopo il commit (**Transactional Outbox pattern**).

---

## 3. Approccio Statico vs Deferred

### Statico (Udi Dahan)

`DomainEvents.Raise(event)` → dispatch immediato. Gli handler partono nel mezzo del metodo di dominio.

```csharp
public void Complete()
{
    Status = "Completed";
    DomainEvents.Raise(new CourseCompletedEvent(Id));  // handler partono ORA
    CompletedAtUtc = DateTime.UtcNow;  // gli handler non vedono questo
}
```

**Problemi:**

- Gli handler vedono uno **stato incompleto** (il metodo non ha finito)
- Se un handler fallisce, gli handler precedenti hanno già fatto le loro modifiche
- Se il `SaveChanges` finale fallisce, gli handler hanno già lavorato su dati non committati
- **Difficile da testare**: appena chiami il metodo partono tutti gli handler reali

### Deferred (Jimmy Bogard / eShop)

L'evento viene solo **accodato in una lista**. Il dispatch avviene dopo, appena prima (o dopo) il commit.

```csharp
public void Complete()
{
    Status = "Completed";
    CompletedAtUtc = DateTime.UtcNow;
    Raise(new CourseCompletedEvent(Id));  // solo Add su una List<>
}
```

Gli handler partono quando tutti i metodi di dominio hanno finito, lo stato è completo e coerente, e tutto vive nella stessa transazione con rollback.

**Facile da testare:**

```csharp
course.Complete();
Assert.Contains(course.GetDomainEvents(), e => e is CourseCompletedEvent);
// Nessun handler è partito, nessun side effect
```

### Dispatch PRIMA vs DOPO il commit

**Prima del commit (eShop):**

```csharp
await _mediator.DispatchDomainEventsAsync(this);  // dispatch
await base.SaveChangesAsync();                     // commit
```

- Transazione unica, consistenza immediata
- Se un handler è lento, blocchi il commit

**Dopo il commit (Milan Jovanović):**

```csharp
var result = await base.SaveChangesAsync();  // commit
await PublishDomainEventsAsync();             // dispatch
```

- Il commit originale è al sicuro
- Eventual consistency → serve Outbox per non perdere eventi

### Il principio

> Dispatch appena prima del commit = stato in memoria completo e coerente, non ancora scritto a DB. Gli handler aggiungono i loro pezzi, il commit porta tutto al DB in un colpo solo. Nessuna finestra in cui RAM e DB raccontano storie diverse.

---

## 4. Componenti in gioco

| Componente | Ruolo |
|---|---|
| **Entity** | Oggetto di dominio. Contiene la logica di business e accumula domain event in una lista tramite `Raise()` |
| **Aggregate Root** | L'entità radice di un gruppo di entità correlate. Punto di accesso per le modifiche |
| **Domain Event** | Classe immutabile (DTO) che descrive qualcosa che è successo. Implementa `INotification` |
| **Command** | Oggetto che rappresenta un'intenzione dell'utente ("fai questo"). Implementa `IRequest` |
| **Command Handler** | Classe che riceve il command, orchestra l'operazione, chiama `SaveChanges()`. Il regista |
| **Domain Event Handler** | Classe che reagisce a un domain event. Gestisce un side effect specifico. Implementa `INotificationHandler<T>` |
| **MediatR** | Libreria dispatcher. Instrada command → handler e event → handlers |
| **DbContext** | Il "foglio di brutta" di EF Core. Contiene il Change Tracker. Genera l'SQL al `SaveChanges()` |
| **Change Tracker** | Componente interno del DbContext. Traccia lo stato di ogni entità (Unchanged, Modified, Added, Deleted) |
| **Repository** | Incapsula l'accesso al DbContext / DB |
| **Unit of Work** | Pattern che garantisce il commit in una singola transazione. In EF Core è il DbContext stesso |
| **Integration Event** | Evento destinato all'esterno (altri microservizi). Salvato nella tabella outbox |
| **Outbox** | Tabella DB dove si parcheggiano gli integration event. Un processo separato li dispatcha dopo il commit |
| **Event Bus** | Infrastruttura di messaggistica asincrona (RabbitMQ, Azure Service Bus) per gli integration event |

### Flusso completo

```
HTTP Request
  └─► MediatR riceve il Command
      └─► CommandHandler
          ├── carica entità via Repository
          ├── chiama metodi di dominio sull'Entity
          │   └── Raise(event) → evento in lista
          └── Apre transazione
              ├── Persisti modifiche entità (SQL)
              ├── Dispatch domain events via MediatR
              │   ├── DomainEventHandler1 → la sua query SQL
              │   ├── DomainEventHandler2 → la sua query SQL
              │   └── DomainEventHandler3 → scrive IntegrationEvent in Outbox
              └── COMMIT (tutto o niente)

  ...dopo il commit...
  OutboxProcessor → legge Outbox → pubblica su EventBus
```

---

## 5. Il Change Tracker di EF Core

Il Change Tracker è una tabella in memoria. Ogni entità caricata o creata ha una **entry**:

```
Entry:
  Entity:          Order { Id=1, Status=Placed }
  State:           Modified
  Original Values: { Status: "Draft" }
  Current Values:  { Status: "Placed" }
```

Al `SaveChanges()`, EF confronta Original vs Current per ogni entry con State ≠ Unchanged e genera l'SQL minimo:

- `State = Modified` → `UPDATE`
- `State = Added` → `INSERT`
- `State = Deleted` → `DELETE`

### Raccolta domain events dal Change Tracker

```csharp
var domainEvents = ChangeTracker
    .Entries<Entity>()              // tutte le entry che ereditano da Entity
    .Select(e => e.Entity)          // estrai l'oggetto C# reale
    .SelectMany(entity =>           // per ognuno, prendi e pulisci gli eventi
    {
        var events = entity.GetDomainEvents();
        entity.ClearDomainEvents();
        return events;
    })
    .ToList();                      // materializza: lista piatta di tutti gli eventi
```

### In caso di fallimento

Se `SaveChanges()` fallisce → rollback sul DB → niente è persistito. Il Change Tracker "sporco" vive solo in RAM. Il DbContext è Scoped (vive per la request HTTP), quindi alla fine della request viene disposto e il garbage collector lo elimina.

**Non si riutilizza mai un DbContext dopo un SaveChanges fallito** — il change tracker è in stato inconsistente.

### Senza EF Core (SQL puro)

Stessa logica, livello di astrazione più basso. Ogni handler contribuisce la sua query SQL alla transazione:

```csharp
using var tx = connection.BeginTransaction();
// command handler: UPDATE ...
// handler 1: INSERT ...
// handler 2: INSERT ...
tx.Commit();  // tutto o niente
```

---

## 6. Il Command Pattern

Separa **chi chiede** da **chi esegue**. Invece di chiamare direttamente un servizio, impacchetti la richiesta in un oggetto (il command) e lo dai a un mediator che lo instrada all'handler.

### Senza Command pattern

```csharp
[HttpPost("{id:guid}/complete")]
public async Task<IActionResult> Complete(Guid id)
{
    // Il controller conosce tutti i servizi e orchestra tutto
    var course = await _courseService.GetById(id);
    course.Complete();
    await _courseService.Update(course);
    await _certificateService.Issue(course);
    return Ok();
}
```

### Con Command pattern

```csharp
// 1. Command (il foglietto dell'ordine) — solo dati
public record CompleteCourseCommand(Guid CourseId) : IRequest;

// 2. Handler (lo chef) — tutta la logica
public class CompleteCourseHandler : IRequestHandler<CompleteCourseCommand>
{
    public async Task Handle(CompleteCourseCommand cmd, CancellationToken ct)
    {
        // carica, esegui, persisti
    }
}

// 3. Controller (il cliente) — solo passacarte
[HttpPost("{id:guid}/complete")]
public async Task<IActionResult> Complete(Guid id)
{
    await _mediator.Send(new CompleteCourseCommand(id));
    return Ok();
}
```

**Vantaggi:**

- **Testabilità**: testi l'handler senza HTTP, senza controller
- **Single Responsibility**: ogni handler fa una cosa
- **Disaccoppiamento**: lo stesso command può essere invocato da API, job, o altro handler
- **Pipeline behaviors**: logging, validazione, transazioni si applicano a tutto automaticamente

---

## 7. MediatR — Panoramica

Libreria .NET di Jimmy Bogard. Implementa il pattern Mediator: riceve un messaggio e lo consegna a chi lo gestisce.

### Due modalità

**`Send` → uno a uno** (command/query):

```csharp
public record CompleteCourseCommand(Guid CourseId) : IRequest<string>;

public class CompleteCourseHandler : IRequestHandler<CompleteCourseCommand, string>
{
    public async Task<string> Handle(CompleteCourseCommand cmd, CancellationToken ct)
    {
        // ... logica
        return "Fatto";
    }
}

var result = await _mediator.Send(new CompleteCourseCommand(id));
```

**`Publish` → uno a molti** (domain events):

```csharp
public record CourseCompletedEvent(Guid CourseId) : INotification;

// Handler 1
public class IssueCertificateHandler : INotificationHandler<CourseCompletedEvent>
{
    public async Task Handle(CourseCompletedEvent e, CancellationToken ct)
        => // ... crea certificato
}

// Handler 2
public class SendEmailHandler : INotificationHandler<CourseCompletedEvent>
{
    public async Task Handle(CourseCompletedEvent e, CancellationToken ct)
        => // ... manda email
}

await _mediator.Publish(new CourseCompletedEvent(id));  // entrambi invocati
```

### Pipeline Behaviors

Middleware che si inseriscono nella pipeline di ogni `Send`:

```csharp
public class LoggingBehavior<TReq, TRes> : IPipelineBehavior<TReq, TRes>
{
    public async Task<TRes> Handle(TReq request,
        RequestHandlerDelegate<TRes> next, CancellationToken ct)
    {
        _logger.LogInformation("Handling {Request}", typeof(TReq).Name);
        var result = await next();  // passa al prossimo o all'handler
        _logger.LogInformation("Handled {Request}", typeof(TReq).Name);
        return result;
    }
}
```

Si impilano automaticamente:

```
Send(command)
  └─► LoggingBehavior
      └─► ValidationBehavior
          └─► TransactionBehavior
              └─► Handler
```

### Setup

```csharp
builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(Program).Assembly));
```

MediatR scansiona l'assembly, trova tutti gli handler, li registra nella DI.

---

## 8. Esempio completo

Scenario: uno studente completa un corso → domain event → un handler gli assegna un certificato. Dapper + SQL Server + MediatR, senza EF Core.

### Schema SQL Server

```sql
CREATE TABLE Courses (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    StudentName NVARCHAR(200) NOT NULL,
    Title NVARCHAR(200) NOT NULL,
    Status NVARCHAR(50) NOT NULL,        -- 'InProgress' | 'Completed'
    CompletedAtUtc DATETIME2 NULL
);

CREATE TABLE Certificates (
    Id UNIQUEIDENTIFIER PRIMARY KEY,
    CourseId UNIQUEIDENTIFIER NOT NULL,
    StudentName NVARCHAR(200) NOT NULL,
    CourseTitle NVARCHAR(200) NOT NULL,
    IssuedAtUtc DATETIME2 NOT NULL
);
```

### Domain Layer

```csharp
// Interfaccia base
public interface IDomainEvent : INotification { }

// Entity base
public abstract class Entity
{
    private readonly List<IDomainEvent> _domainEvents = new();

    public IReadOnlyList<IDomainEvent> GetDomainEvents() => _domainEvents.ToList();
    public void ClearDomainEvents() => _domainEvents.Clear();
    protected void Raise(IDomainEvent e) => _domainEvents.Add(e);
}

// Domain Event
public record CourseCompletedEvent(
    Guid CourseId, string StudentName, string CourseTitle) : IDomainEvent;

// Entità
public class Course : Entity
{
    public Guid Id { get; private set; }
    public string StudentName { get; private set; }
    public string Title { get; private set; }
    public string Status { get; private set; }
    public DateTime? CompletedAtUtc { get; private set; }

    public Course(Guid id, string studentName, string title,
                  string status, DateTime? completedAtUtc)
    {
        Id = id; StudentName = studentName; Title = title;
        Status = status; CompletedAtUtc = completedAtUtc;
    }

    public void Complete()
    {
        if (Status == "Completed")
            throw new InvalidOperationException("Corso già completato");

        Status = "Completed";
        CompletedAtUtc = DateTime.UtcNow;
        Raise(new CourseCompletedEvent(Id, StudentName, Title));
    }
}
```

### Application Layer

```csharp
// Command
public record CompleteCourseCommand(Guid CourseId) : IRequest;

// Command Handler
public class CompleteCourseHandler : IRequestHandler<CompleteCourseCommand>
{
    private readonly IDbConnection _db;
    private readonly IMediator _mediator;

    public CompleteCourseHandler(IDbConnection db, IMediator mediator)
    {
        _db = db;
        _mediator = mediator;
    }

    public async Task Handle(CompleteCourseCommand cmd, CancellationToken ct)
    {
        // 1. Carica dal DB
        var row = await _db.QuerySingleOrDefaultAsync<dynamic>(
            "SELECT * FROM Courses WHERE Id = @Id",
            new { Id = cmd.CourseId })
            ?? throw new Exception("Corso non trovato");

        var course = new Course(row.Id, row.StudentName, row.Title,
                                row.Status, row.CompletedAtUtc);

        // 2. Logica di dominio (l'evento viene registrato qui dentro)
        course.Complete();

        // 3. Transazione — tutto o niente
        _db.Open();
        using var tx = _db.BeginTransaction();
        try
        {
            // 4. Persisti le modifiche dell'entità
            await _db.ExecuteAsync(
                @"UPDATE Courses SET Status = @Status,
                  CompletedAtUtc = @CompletedAtUtc WHERE Id = @Id",
                new { course.Status, course.CompletedAtUtc, course.Id },
                transaction: tx);

            // 5. Dispatcha gli eventi — gli handler girano nella stessa tx
            foreach (var domainEvent in course.GetDomainEvents())
                await _mediator.Publish(domainEvent, ct);
            course.ClearDomainEvents();

            // 6. Commit
            tx.Commit();
        }
        catch
        {
            tx.Rollback();
            throw;
        }
    }
}

// Domain Event Handler — crea il certificato
public class IssueCertificateHandler : INotificationHandler<CourseCompletedEvent>
{
    private readonly IDbConnection _db;

    public IssueCertificateHandler(IDbConnection db) { _db = db; }

    public async Task Handle(CourseCompletedEvent e, CancellationToken ct)
    {
        await _db.ExecuteAsync(
            @"INSERT INTO Certificates (Id, CourseId, StudentName, CourseTitle, IssuedAtUtc)
              VALUES (@Id, @CourseId, @StudentName, @CourseTitle, @IssuedAtUtc)",
            new {
                Id = Guid.NewGuid(), e.CourseId, e.StudentName,
                e.CourseTitle, IssuedAtUtc = DateTime.UtcNow
            });
    }
}
```

### API Layer

```csharp
[ApiController]
[Route("api/courses")]
public class CoursesController : ControllerBase
{
    private readonly IMediator _mediator;
    public CoursesController(IMediator mediator) { _mediator = mediator; }

    [HttpPost("{id:guid}/complete")]
    public async Task<IActionResult> Complete(Guid id)
    {
        await _mediator.Send(new CompleteCourseCommand(id));
        return Ok("Corso completato e certificato emesso");
    }
}
```

### DI Registration

```csharp
builder.Services.AddScoped<IDbConnection>(sp =>
    new SqlConnection(builder.Configuration.GetConnectionString("Default")));

builder.Services.AddMediatR(cfg =>
    cfg.RegisterServicesFromAssembly(typeof(Program).Assembly));
```

### Flusso della chiamata

```
POST /api/courses/{id}/complete
  │
  ▼
CoursesController → _mediator.Send(CompleteCourseCommand)
  │
  ▼
CompleteCourseHandler
  ├── SELECT dal DB → ricostruisce Course
  ├── course.Complete() → Status="Completed" + Raise(event)
  ├── BEGIN TRANSACTION
  ├── UPDATE Courses SET Status, CompletedAtUtc
  ├── Dispatch: IssueCertificateHandler
  │   └── INSERT INTO Certificates
  ├── COMMIT ✅ (o ROLLBACK ❌ se qualcosa fallisce)
  ▼
Response: 200 OK
```

---

## 9. Fonti

- Martin Fowler — [Domain Event](https://martinfowler.com/eaaDev/DomainEvent.html)
- Microsoft — [Domain events: Design and implementation](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation)
- Jimmy Bogard — [A better domain events pattern](https://lostechies.com/jimmybogard/2014/05/13/a-better-domain-events-pattern/)
- Milan Jovanović — [How to use domain events to build loosely coupled systems](https://www.milanjovanovic.tech/blog/how-to-use-domain-events-to-build-loosely-coupled-systems)

---

## Collegamenti

- [[domain-events|Domain Events (nota implementazione)]]
- [[clean-architecture|Clean Architecture]]
- [[../../../Knowledge/solid/open-closed-principle|Open/Closed Principle]]

---

*Creato durante Week 2 - 2026-02-13*
