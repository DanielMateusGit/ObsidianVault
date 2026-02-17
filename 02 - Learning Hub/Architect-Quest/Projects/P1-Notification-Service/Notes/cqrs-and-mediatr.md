---
tags:
  - p1
  - architecture
  - cqrs
  - mediatr
  - from/week-03
  - status/learning
aliases:
  - CQRS
  - Command Query Separation
  - MediatR
created: 2026-02-16
source: "Sessione Week 3"
---

# CQRS e MediatR

> **One-liner:** CQRS separa le operazioni di scrittura (Commands) dalle letture (Queries), MediatR le orchestra tramite handlers disaccoppiati.

## Cos'è CQRS

**Command Query Responsibility Segregation** - un pattern che divide l'Application Layer in due parti:

| Lato | Scopo | Esempio |
|------|-------|---------|
| **Commands** | Modificare stato | `ScheduleNotificationCommand` |
| **Queries** | Leggere stato | `GetNotificationByIdQuery` |

```
┌─────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                       │
│                                                             │
│   ┌─────────────────────┐    ┌─────────────────────┐       │
│   │      COMMANDS       │    │       QUERIES       │       │
│   │    (Write Side)     │    │    (Read Side)      │       │
│   ├─────────────────────┤    ├─────────────────────┤       │
│   │ ScheduleNotification│    │ GetNotificationById │       │
│   │ CancelNotification  │    │ GetPendingList      │       │
│   │ RetryNotification   │    │ GetByStatus         │       │
│   └──────────┬──────────┘    └──────────┬──────────┘       │
│              │                          │                   │
│              ▼                          ▼                   │
│   ┌─────────────────────┐    ┌─────────────────────┐       │
│   │  Command Handlers   │    │   Query Handlers    │       │
│   │  (Business Logic)   │    │  (Just read data)   │       │
│   └─────────────────────┘    └─────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

## Commands vs Queries

| Aspetto | Command | Query |
|---------|---------|-------|
| **Scopo** | Modifica stato | Legge stato |
| **Ritorno** | Void, ID, o Result | Dati (DTO) |
| **Validazione** | Complessa | Minima |
| **Transazione** | Sempre | Raramente |
| **Side effects** | Sì (eventi, email...) | Mai |
| **Naming** | Verbo imperativo | Get/Find/List |

### Esempio Command
```csharp
// Il Command (cosa voglio fare)
public record ScheduleNotificationCommand(
    string Recipient,
    NotificationChannel Channel,
    DateTime ScheduledAt,
    Guid? TemplateId
) : IRequest<Guid>;

// Il Handler (come lo faccio)
public class ScheduleNotificationHandler
    : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    private readonly INotificationRepository _repository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Guid> Handle(
        ScheduleNotificationCommand command,
        CancellationToken ct)
    {
        var notification = Notification.Create(
            command.Recipient,
            command.Channel,
            command.TemplateId
        );

        notification.Schedule(command.ScheduledAt);

        await _repository.AddAsync(notification, ct);
        await _unitOfWork.SaveChangesAsync(ct);

        return notification.Id;
    }
}
```

### Esempio Query
```csharp
// La Query (cosa voglio leggere)
public record GetNotificationByIdQuery(Guid Id)
    : IRequest<NotificationDto?>;

// Il Handler (come lo leggo)
public class GetNotificationByIdHandler
    : IRequestHandler<GetNotificationByIdQuery, NotificationDto?>
{
    private readonly INotificationRepository _repository;

    public async Task<NotificationDto?> Handle(
        GetNotificationByIdQuery query,
        CancellationToken ct)
    {
        var notification = await _repository.GetByIdAsync(query.Id, ct);

        if (notification is null)
            return null;

        return new NotificationDto(
            notification.Id,
            notification.Recipient.Value,
            notification.Status.ToString(),
            notification.ScheduledAt
        );
    }
}
```

## Cos'è MediatR

Libreria che implementa il **Mediator Pattern**: un "postino" che riceve messaggi (Commands/Queries) e li consegna all'handler giusto.

```
Controller
    │
    ▼
IMediator  ──────► trova handler giusto ──────► Handler
    │                                              │
    ◄──────────────── response ◄───────────────────┘
```

### Vantaggi
- Controller non conosce gli Handler (loose coupling)
- Facile aggiungere cross-cutting concerns
- Ogni handler è una classe singola, testabile

## Pipeline Behaviors

Il vero potere di MediatR: comportamenti che si eseguono prima/dopo OGNI handler.

```
Request → [Validation] → [Logging] → [Transaction] → Handler → Response
```

### Esempio: Logging Behavior
```csharp
public class LoggingBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
{
    private readonly ILogger<LoggingBehavior<TRequest, TResponse>> _logger;

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken ct)
    {
        var requestName = typeof(TRequest).Name;

        _logger.LogInformation("Handling {RequestName}", requestName);

        var response = await next();  // Chiama handler o prossimo behavior

        _logger.LogInformation("Handled {RequestName}", requestName);

        return response;
    }
}
```

### Esempio: Validation Behavior
```csharp
public class ValidationBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken ct)
    {
        var failures = _validators
            .Select(v => v.Validate(request))
            .SelectMany(r => r.Errors)
            .Where(f => f != null)
            .ToList();

        if (failures.Any())
            throw new ValidationException(failures);

        return await next();
    }
}
```

## Pipeline Behaviors - Prima vs Dopo

### ❌ PRIMA (senza Behavior) - Codice duplicato in ogni handler
```csharp
public class ScheduleNotificationHandler : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    public async Task<Guid> Handle(ScheduleNotificationCommand command, CancellationToken ct)
    {
        // 🔴 Logging duplicato in OGNI handler
        _logger.LogInformation("Starting ScheduleNotificationCommand");

        // 🔴 Validazione duplicata in OGNI handler
        if (string.IsNullOrEmpty(command.Recipient))
            throw new ValidationException("Recipient required");

        // Logica vera
        var notification = Notification.Create(...);
        await _repository.AddAsync(notification, ct);

        // 🔴 Logging duplicato
        _logger.LogInformation("Completed ScheduleNotificationCommand");

        return notification.Id;
    }
}
// Handler 2, 3, 4... stessa roba duplicata! 😩
```

### ✅ DOPO (con Pipeline Behaviors) - Codice centralizzato
```csharp
// 1️⃣ BEHAVIOR scritto UNA volta, vale per TUTTI gli handler
public class LoggingBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
{
    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, CancellationToken ct)
    {
        _logger.LogInformation("▶ Starting {Request}", typeof(TRequest).Name);
        var response = await next();  // Chiama handler
        _logger.LogInformation("✓ Completed {Request}", typeof(TRequest).Name);
        return response;
    }
}

// 2️⃣ HANDLER ora è PULITO - solo logica di business!
public class ScheduleNotificationHandler : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    public async Task<Guid> Handle(ScheduleNotificationCommand command, CancellationToken ct)
    {
        // ✅ Solo logica! Logging e validazione sono automatici
        var notification = Notification.Create(...);
        await _repository.AddAsync(notification, ct);
        return notification.Id;
    }
}
```

### Flusso di esecuzione
```
Request → [LoggingBehavior] → [ValidationBehavior] → Handler → Response
              ▲                      ▲                  ▲
         Log start              Valida             Logica business
         Log end                Throw se errore
```

---

## Quando usarlo

### Usa CQRS quando:
- Read e Write hanno requisiti diversi
- Vuoi scalare letture e scritture separatamente
- Hai logica di business complessa sulle scritture
- Vuoi handler piccoli e testabili

### NON usare CQRS quando:
- CRUD semplice senza logica
- Applicazioni piccole (over-engineering)
- Team non familiare con il pattern

## Quando NON usarlo

- **CRUD puro:** Se non hai logica di business, CQRS è over-engineering
- **Progetti piccoli:** Il boilerplate non giustifica i benefici
- **Team junior:** La curva di apprendimento può rallentare

## Collegamenti

- [[clean-architecture]] - CQRS vive nell'Application Layer
- [[domain-events]] - Commands possono sollevare eventi
- [[domain-model-patterns]] - Handlers chiamano il Domain

## Domande dalla Sessione

### D: I Command sono solo per modificare stato esistente?
**R:** No, i Command fanno di più:
| Operazione | Command? | Esempio |
|------------|----------|---------|
| **Creare** nuovo stato | ✅ Sì | `ScheduleNotificationCommand` |
| **Modificare** stato esistente | ✅ Sì | `CancelNotificationCommand` |
| **Eliminare** stato | ✅ Sì | `DeleteNotificationCommand` |
| **Leggere** stato | ❌ No | → Query |

**Definizione corretta:** Command = cambia il sistema. Query = legge senza cambiare.

### D: Un Command può ritornare una lista di oggetti?
**R:** No. Il Command cambia stato, non lo legge. Se dopo un Command servono dati, fai una Query separata:
```csharp
// Corretto
var batchId = await _mediator.Send(new CreateBatchCommand(...));
var items = await _mediator.Send(new GetBatchItemsQuery(batchId));
```

### D: Il Query Handler può chiamare Delete?
**R:** Mai. Le Query sono SOLO lettura. Operazioni che modificano stato (anche Delete) vanno in Command.

### D: Devo modificare tutti gli handler per aggiungere logging?
**R:** No! Crei UN `LoggingBehavior` e MediatR lo esegue per tutti automaticamente. Questo è il potere dei Pipeline Behaviors.

### D: I Pipeline Behaviors funzionano con la DI? Come dico "per questo comando fai X"?
**R:** Sì, è tutto DI. Ma attenzione: i behaviors si applicano a **TUTTI** i commands/queries, non a uno specifico.

```csharp
// Registri UNA volta, vale per TUTTI
services.AddTransient(typeof(IPipelineBehavior<,>), typeof(LoggingBehavior<,>));
```

Se vuoi un behavior solo per certi command, hai due opzioni:

**Opzione A - Filtro interno:**
```csharp
public async Task<TResponse> Handle(TRequest request, ...)
{
    if (request is IAuditable auditable)  // Solo se implementa IAuditable
        await _auditService.LogAsync(auditable);
    return await next();
}
```

**Opzione B - Constraint generico:**
```csharp
public class TransactionBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
    where TRequest : ICommand  // ← Si applica SOLO ai ICommand
```

### D: Retry() è uno Use Case? Come decido se la logica va in Domain o Application?
**R:** Entrambi servono! La distinzione:

| Domanda | Se SÌ → | Se NO → |
|---------|---------|---------|
| È una **REGOLA** che il business impone sempre? | Domain | - |
| È **COORDINAZIONE** di più operazioni? | Application | - |
| Se cambio database, questa logica cambia? | Infrastructure | Domain |

**Per Retry:**
- **Domain (`Notification.Retry()`)**: "Cosa SIGNIFICA ritentare" → verifica stato Failed, resetta a Pending, pulisce errore. Queste sono REGOLE di business.
- **Application (`RetryNotificationHandler`)**: "COME orchestro il retry" → trova notifica, chiama Retry(), salva. Questa è COORDINAZIONE.

**Test mentale:** Se un junior mette la logica nell'Handler, altri dev potrebbero dimenticare parti della logica (es. non pulire ErrorMessage). Il Domain protegge le invarianti - non importa chi chiama, le regole sono sempre rispettate.

```
Handler (Application)          Domain
─────────────────────          ──────
1. Trova notifica      ───►
2. notification.Retry() ───►   • Verifica Failed
                               • Resetta Pending
                               • Pulisce errore
                               • Solleva evento
3. Salva               ◄───
```

## Quiz

### Q1: Command Return Type
Un `CreateOrderCommand` cosa dovrebbe ritornare?
- A) `List<Order>`
- B) `Order`
- C) `Guid` o `Result<Guid>`
- D) `void` sempre

<details>
<summary>Risposta</summary>
**C) `Guid` o `Result<Guid>`**

Un Command ritorna al massimo l'ID dell'entità creata o un Result con success/failure. MAI una lista o l'entità intera - per quello usi una Query.
</details>

### Q2: Query Side Effects
È corretto questo codice in un Query Handler?
```csharp
public async Task<OrderDto> Handle(GetOrderQuery query, CancellationToken ct)
{
    var order = await _repository.GetByIdAsync(query.Id);
    order.MarkAsViewed();  // <-- Questo
    await _repository.SaveAsync();
    return _mapper.Map<OrderDto>(order);
}
```

<details>
<summary>Risposta</summary>
**NO!** Una Query non deve MAI modificare stato. `MarkAsViewed()` è un side effect che va in un Command separato:
```csharp
await _mediator.Send(new MarkOrderAsViewedCommand(id));
var order = await _mediator.Send(new GetOrderQuery(id));
```
</details>

### Q3: Pipeline Behavior Order
Se hai `ValidationBehavior`, `LoggingBehavior`, `TransactionBehavior`, in che ordine li registri se vuoi validare PRIMA di loggare?

<details>
<summary>Risposta</summary>
L'ordine di registrazione nel DI container determina l'ordine di esecuzione:
```csharp
services.AddTransient(typeof(IPipelineBehavior<,>), typeof(ValidationBehavior<,>));
services.AddTransient(typeof(IPipelineBehavior<,>), typeof(LoggingBehavior<,>));
services.AddTransient(typeof(IPipelineBehavior<,>), typeof(TransactionBehavior<,>));
```
Request → Validation → Logging → Transaction → Handler
</details>

---

## Risorse per Approfondire

- **[CQRS - Martin Fowler](https://martinfowler.com/bliki/CQRS.html)** - Definizione originale del pattern
- **[MediatR Wiki](https://github.com/jbogard/MediatR/wiki)** - Documentazione ufficiale
- **[Jimmy Bogard - MediatR Behaviors](https://jimmybogard.com/behaviors-in-mediatr/)** - Creatore di MediatR spiega i behaviors
- **Clean Architecture** Cap. 21-22 - Use Cases e Application Layer

---

*Creato: 2026-02-16 | Week 3 - Application Layer*
