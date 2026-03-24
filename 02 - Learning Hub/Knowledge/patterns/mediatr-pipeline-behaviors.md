---
tags:
  - patterns
  - mediatr
  - validation
  - cross-cutting-concerns
  - from/video
  - status/learned
aliases:
  - Pipeline Behaviors
  - MediatR Middleware
  - Validation Pipeline
created: 2026-02-25
updated: 2026-02-26
source: "Nick Chapsas - Validation using MediatR's Pipeline Behaviors and FluentValidation (YouTube)"
---

# MediatR Pipeline Behaviors + FluentValidation

> **One-liner:** Middleware pattern per MediatR che intercetta richieste/risposte, permettendo di aggiungere cross-cutting concerns (validazione, logging, etc.) senza modificare gli handler.

---

## Cos'è

Un **Pipeline Behavior** in MediatR è un meccanismo di middleware che permette di:
- Intercettare richieste PRIMA che raggiungano l'handler
- Intercettare risposte DOPO che l'handler ha finito
- Aggiungere logica trasversale (validazione, logging, caching, etc.) senza toccare gli handler

È l'implementazione del **Decorator Pattern** applicato ai request handler di MediatR.

### Problema che Risolve

**Senza Pipeline Behaviors:**
```csharp
public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, int>
{
    public async Task<int> Handle(CreateOrderCommand request, ...)
    {
        // ❌ Validazione nel handler
        if (string.IsNullOrEmpty(request.ProductName))
            throw new ValidationException("ProductName is required");

        // ❌ Logging nel handler
        _logger.LogInformation("Creating order...");

        // ✅ Business logic
        var order = new Order(request.ProductName, request.Quantity);
        await _repository.AddAsync(order);

        // ❌ Performance tracking nel handler
        _metrics.RecordDuration("CreateOrder", duration);

        return order.Id;
    }
}
```

**Problemi:**
- Codice duplicato in tutti gli handler (validazione, logging, etc.)
- Violazione SRP: l'handler fa troppo
- Difficile testare solo la business logic

**Con Pipeline Behaviors:**
```csharp
// ✅ Handler pulito - solo business logic
public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, int>
{
    public async Task<int> Handle(CreateOrderCommand request, ...)
    {
        var order = new Order(request.ProductName, request.Quantity);
        await _repository.AddAsync(order);
        return order.Id;
    }
}

// ✅ Validazione separata in un behavior
public class ValidationBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
{
    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, ...)
    {
        // Valida prima
        await ValidateAsync(request);

        // Passa al prossimo step
        return await next();
    }
}
```

---

## Come Funziona la Pipeline

### 🪆 Il Concetto delle Matrioske

La pipeline è come **matrioske russe**:
- Apri, apri, apri → arrivi al centro (handler)
- Chiudi, chiudi, chiudi → torni fuori (response)

### Diagramma del Flusso Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                       MediatR Pipeline                           │
└─────────────────────────────────────────────────────────────────┘

   Request (Command/Query)
        │
        ↓
   ┌──────────────────────┐
   │  Behavior 1          │  ← Logging
   │  ┌────────────────┐  │
   │  │ BEFORE         │  │  _logger.LogInformation("Starting...");
   │  └────────────────┘  │
   │         │            │
   │         ↓            │
   │    await next()      │  ← Chiama il prossimo nella catena
   │         │            │
   └─────────┼────────────┘
             ↓
   ┌──────────────────────┐
   │  Behavior 2          │  ← Validation
   │  ┌────────────────┐  │
   │  │ BEFORE         │  │  await ValidateAsync(request);
   │  └────────────────┘  │
   │         │            │
   │         ↓            │
   │    await next()      │  ← Chiama il prossimo
   │         │            │
   └─────────┼────────────┘
             ↓
   ┌──────────────────────┐
   │  Behavior 3          │  ← Transaction
   │  ┌────────────────┐  │
   │  │ BEFORE         │  │  using var transaction = ...
   │  └────────────────┘  │
   │         │            │
   │         ↓            │
   │    await next()      │  ← Chiama l'handler
   │         │            │
   └─────────┼────────────┘
             ↓
   ┌──────────────────────┐
   │  ACTUAL HANDLER      │  ← Business Logic PURA
   │                      │
   │  var order = new ... │
   │  return order.Id;    │
   │                      │
   └──────────┬───────────┘
             │
             ↓ Response (order.Id)
   ┌──────────────────────┐
   │  Behavior 3          │
   │  ┌────────────────┐  │
   │  │ AFTER          │  │  await transaction.CommitAsync();
   │  └────────────────┘  │
   └─────────┬────────────┘
             ↓
   ┌──────────────────────┐
   │  Behavior 2          │
   │  ┌────────────────┐  │
   │  │ AFTER          │  │  (niente da fare qui)
   │  └────────────────┘  │
   └─────────┬────────────┘
             ↓
   ┌──────────────────────┐
   │  Behavior 1          │
   │  ┌────────────────┐  │
   │  │ AFTER          │  │  _logger.LogInformation("Completed!");
   │  └────────────────┘  │
   └─────────┬────────────┘
             ↓
        Response
```

### Anatomia di un Behavior

Un behavior ha **UN SOLO metodo** `Handle()` con tre fasi:

```csharp
public async Task<TResponse> Handle(
    TRequest request,
    RequestHandlerDelegate<TResponse> next,  // ← Delegate al prossimo
    CancellationToken cancellationToken)
{
    // ═══════════════════════════════════════════════════════
    //  BEFORE: Codice PRIMA di next()
    // ═══════════════════════════════════════════════════════
    // Eseguito mentre "scendi" nella pipeline

    _logger.LogInformation("Starting...");

    // ═══════════════════════════════════════════════════════
    //  NEXT: Passa al prossimo behavior o handler
    // ═══════════════════════════════════════════════════════

    var response = await next();  // ← Chiamata NON bloccante!

    // ═══════════════════════════════════════════════════════
    //  AFTER: Codice DOPO next()
    // ═══════════════════════════════════════════════════════
    // Eseguito mentre "risali" dalla pipeline

    _logger.LogInformation("Completed!");

    return response;
}
```

**Nota:** Non sono tre metodi separati (`pre()`, `next()`, `post()`), ma **un solo metodo** con codice before/after della chiamata a `next()`.

---

## Implementazione Step-by-Step

### Step 1: Definire i Validatori (FluentValidation)

```csharp
// Domain o Application layer
public record CreateOrderCommand(string ProductName, int Quantity) : IRequest<int>;

// Application.Validators
public class CreateOrderCommandValidator : AbstractValidator<CreateOrderCommand>
{
    public CreateOrderCommandValidator()
    {
        RuleFor(x => x.ProductName)
            .NotEmpty()
            .WithMessage("Product name is required")
            .MaximumLength(100);

        RuleFor(x => x.Quantity)
            .GreaterThan(0)
            .WithMessage("Quantity must be greater than 0");
    }
}
```

### Step 2: Creare il Pipeline Behavior per la Validazione

```csharp
// Application.Behaviors
public class ValidationBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    public ValidationBehavior(IEnumerable<IValidator<TRequest>> validators)
    {
        _validators = validators;  // ← MediatR inietta TUTTI i validatori per TRequest
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        // ═══════════════════════════════════════════════════════
        //  BEFORE: Esegui validazione PRIMA di chiamare next()
        // ═══════════════════════════════════════════════════════

        if (!_validators.Any())
        {
            // Nessun validatore registrato per questo comando → skip
            return await next();
        }

        var context = new ValidationContext<TRequest>(request);

        // Esegui TUTTI i validatori in parallelo
        var validationResults = await Task.WhenAll(
            _validators.Select(v => v.ValidateAsync(context, cancellationToken))
        );

        // Raccogli tutti gli errori
        var failures = validationResults
            .SelectMany(r => r.Errors)
            .Where(f => f != null)
            .ToList();

        if (failures.Any())
        {
            // ❌ Lancia eccezione → interrompe la pipeline
            // next() NON viene mai chiamato!
            throw new ValidationException(failures);
        }

        // ═══════════════════════════════════════════════════════
        //  NEXT: Validazione OK → passa al prossimo
        // ═══════════════════════════════════════════════════════

        var response = await next();

        // ═══════════════════════════════════════════════════════
        //  AFTER: Niente da fare dopo (opzionale)
        // ═══════════════════════════════════════════════════════

        return response;
    }
}
```

### Step 3: Registrare tutto nel DI Container

```csharp
// Program.cs o ServiceCollectionExtensions.cs
public static IServiceCollection AddApplication(this IServiceCollection services)
{
    var assembly = typeof(CreateOrderCommand).Assembly;

    // 1. Registra MediatR
    services.AddMediatR(cfg => {
        cfg.RegisterServicesFromAssembly(assembly);

        // 2. Registra i Pipeline Behaviors
        // ⚠️ ORDINE IMPORTANTE! Primo registrato = primo eseguito
        cfg.AddBehavior<IPipelineBehavior<,>, LoggingBehavior<,>>();
        cfg.AddBehavior<IPipelineBehavior<,>, ValidationBehavior<,>>();
        cfg.AddBehavior<IPipelineBehavior<,>, TransactionBehavior<,>>();
    });

    // 3. Registra tutti i validatori di FluentValidation dall'assembly
    // ← MediatR li trova automaticamente per tipo: IValidator<CreateOrderCommand>
    services.AddValidatorsFromAssembly(assembly);

    return services;
}
```

**Come funziona `AddValidatorsFromAssembly`?**
- Scansiona l'assembly alla ricerca di classi che ereditano da `AbstractValidator<T>`
- Le registra nel DI come `IValidator<T>`
- MediatR poi le inietta nel `ValidationBehavior<TRequest, TResponse>` in base al tipo della request

### Step 4: Usare il Command

```csharp
// API Controller
[HttpPost]
public async Task<IActionResult> CreateOrder([FromBody] CreateOrderRequest request)
{
    var command = new CreateOrderCommand(request.ProductName, request.Quantity);

    // MediatR automaticamente:
    // 1. Passa per LoggingBehavior (log inizio)
    // 2. Passa per ValidationBehavior (valida input)
    // 3. Passa per TransactionBehavior (apre transazione)
    // 4. Esegue CreateOrderHandler (business logic)
    // 5. Torna indietro chiudendo tutto (commit, log, etc.)

    var orderId = await _mediator.Send(command);

    return Ok(new { OrderId = orderId });
}
```

---

## Ordine dei Behaviors

⚠️ **L'ordine di registrazione = ordine di esecuzione!**

```csharp
cfg.AddBehavior<IPipelineBehavior<,>, LoggingBehavior<,>>();      // 1° (outer)
cfg.AddBehavior<IPipelineBehavior<,>, ValidationBehavior<,>>();   // 2°
cfg.AddBehavior<IPipelineBehavior<,>, TransactionBehavior<,>>();  // 3° (inner)
```

**Esecuzione:**
```
Request
  → Logging (before)      ← Inizia per primo
    → Validation (before)
      → Transaction (before)
        → HANDLER
      ← Transaction (after)
    ← Validation (after)
  ← Logging (after)       ← Finisce per ultimo
Response
```

**Timeline Esempio:**
```
[12:30:45.100] LoggingBehavior   → Starting CreateOrderCommand
[12:30:45.120] ValidationBehavior → Validating CreateOrderCommand
[12:30:45.150] TransactionBehavior → Opening transaction
[12:30:46.200] CreateOrderHandler  → Order created with ID 42
[12:30:46.250] TransactionBehavior ← Committing transaction
[12:30:46.260] ValidationBehavior  ← (niente da fare)
[12:30:46.270] LoggingBehavior    ← Completed in 1.17s
```

---

## Altri Esempi di Behaviors

### Logging Behavior

```csharp
public class LoggingBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly ILogger<LoggingBehavior<TRequest, TResponse>> _logger;

    public LoggingBehavior(ILogger<LoggingBehavior<TRequest, TResponse>> logger)
    {
        _logger = logger;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        var requestName = typeof(TRequest).Name;

        _logger.LogInformation("Handling {RequestName}", requestName);
        var stopwatch = Stopwatch.StartNew();

        try
        {
            var response = await next();

            stopwatch.Stop();
            _logger.LogInformation(
                "Handled {RequestName} in {ElapsedMs}ms",
                requestName,
                stopwatch.ElapsedMilliseconds
            );

            return response;
        }
        catch (Exception ex)
        {
            stopwatch.Stop();
            _logger.LogError(
                ex,
                "Error handling {RequestName} after {ElapsedMs}ms",
                requestName,
                stopwatch.ElapsedMilliseconds
            );
            throw;
        }
    }
}
```

### Transaction Behavior

```csharp
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
        {
            return await next();
        }

        // BEFORE: Apri transazione
        await using var transaction = await _unitOfWork.BeginTransactionAsync();

        try
        {
            var response = await next();

            // AFTER: Commit se tutto ok
            await transaction.CommitAsync(cancellationToken);

            return response;
        }
        catch
        {
            // AFTER: Rollback se errore
            await transaction.RollbackAsync(cancellationToken);
            throw;
        }
    }
}
```

### Caching Behavior (solo Query)

```csharp
public class CachingBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IDistributedCache _cache;

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        // Solo per Query
        if (!typeof(TRequest).Name.EndsWith("Query"))
        {
            return await next();
        }

        var cacheKey = $"{typeof(TRequest).Name}-{JsonSerializer.Serialize(request)}";

        // BEFORE: Prova a leggere dalla cache
        var cached = await _cache.GetStringAsync(cacheKey, cancellationToken);
        if (cached != null)
        {
            // Cache hit → non chiama next()!
            return JsonSerializer.Deserialize<TResponse>(cached);
        }

        var response = await next();

        // AFTER: Salva in cache
        await _cache.SetStringAsync(
            cacheKey,
            JsonSerializer.Serialize(response),
            new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) },
            cancellationToken
        );

        return response;
    }
}
```

---

## Behaviors Selettivi (Marker Interface)

Se vuoi applicare un behavior solo ad alcuni command (non tutti), usa una **marker interface**:

```csharp
// Marker interface
public interface ITransactionalCommand { }

// Command che VUOLE la transazione
public record CreateOrderCommand(...) : IRequest<int>, ITransactionalCommand;

// Command che NON vuole la transazione
public record GetOrderQuery(...) : IRequest<OrderDto>;  // ← Nessuna marker interface

// Behavior selettivo
public class TransactionBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    public async Task<TResponse> Handle(...)
    {
        // Applica solo se implementa ITransactionalCommand
        if (request is not ITransactionalCommand)
        {
            return await next();  // ← Skip
        }

        // ... logica transazione
    }
}
```

---

## Quando Usarlo

✅ **USA Pipeline Behaviors quando:**
- Hai logica **cross-cutting** che si ripete in molti handler (validazione, logging, caching)
- Vuoi **separare responsabilità** (SRP): handler = business logic, behavior = infra logic
- Vuoi logica **before/after** senza modificare gli handler
- Vuoi **testare** handler isolati dalla logica infrastrutturale
- Hai bisogno di **transaction management** centralizzato

### 🎯 Esempi Concreti - QUANDO USARLI

#### ✅ Validazione Input
```
Scenario: Hai 20 command handler, tutti devono validare l'input.
❌ SENZA Behavior: 20 handler con if (string.IsNullOrEmpty...) duplicati
✅ CON Behavior: UN ValidationBehavior che valida tutti automaticamente
```

#### ✅ Logging Richieste
```
Scenario: Il PM vuole tracciare tutte le operazioni per audit.
❌ SENZA Behavior: Aggiungi _logger.Log...() all'inizio di ogni handler
✅ CON Behavior: UN LoggingBehavior che logga automaticamente
```

#### ✅ Transaction Management
```
Scenario: Ogni Command deve salvare in una transazione.
❌ SENZA Behavior: using var transaction = ... in ogni handler
✅ CON Behavior: UN TransactionBehavior che wrappa tutto
```

#### ✅ Authorization
```
Scenario: Alcuni command richiedono permessi specifici.
❌ SENZA Behavior: if (!_authService.HasPermission...) in ogni handler
✅ CON Behavior: UN AuthorizationBehavior che controlla automaticamente
```

#### ✅ Caching Read-Through
```
Scenario: Vuoi cachare tutte le Query, ma NON i Command.
❌ SENZA Behavior: _cache.GetOrSet() duplicato in ogni Query handler
✅ CON Behavior: UN CachingBehavior che fa get/set automaticamente
```

#### ✅ Performance Monitoring
```
Scenario: Vuoi misurare il tempo di ogni operazione per APM.
❌ SENZA Behavior: Stopwatch.StartNew() / .Stop() in ogni handler
✅ CON Behavior: UN PerformanceBehavior con Stopwatch centralizzato
```

#### ✅ Retry con Polly
```
Scenario: Alcuni command possono fallire temporaneamente (rete, DB lock).
❌ SENZA Behavior: try/retry logic duplicata in ogni handler
✅ CON Behavior: UN RetryBehavior che usa Polly automaticamente
```

#### ✅ Enrichment con Contesto Utente
```
Scenario: Ogni Command deve avere UserId e TenantId dall'HttpContext.
❌ SENZA Behavior: _httpContext.User.Id ripetuto in 50 handler
✅ CON Behavior: UN UserContextBehavior che enrichisce automaticamente
```

---

## Quando NON Usarlo

❌ **NON usare Pipeline Behaviors quando:**
- La logica è **specifica** di un singolo handler (mettila nel handler!)
- Hai **pochi** handler e non serve astrazione (YAGNI)
- Il behavior diventa **troppo complesso** (> 50 righe)
- Stai cercando di mettere **business logic** nel behavior (NO! Va nel Domain/Handler)

### 🚫 Esempi Concreti - QUANDO NON USARLI

#### ❌ Business Logic Specifica
```
Scenario: Solo CreateOrderCommand deve applicare sconti bulk.
❌ SBAGLIATO: DiscountBehavior che controlla if (request is CreateOrderCommand)
✅ GIUSTO: Metti la logica sconto nel CreateOrderHandler o nel Domain
Perché: Non è cross-cutting, è business rule specifica
```

#### ❌ Progetto Piccolo
```
Scenario: Hai 3 command handler in un progetto interno.
❌ SBAGLIATO: Creare ValidationBehavior, LoggingBehavior, etc.
✅ GIUSTO: Valida e logga direttamente negli handler
Perché: YAGNI - stai over-engineering
```

#### ❌ Logica Complessa Condizionale
```
Scenario: ValidationBehavior diventa 200 righe con if/switch per casi speciali.
❌ SBAGLIATO: Continuare ad aggiungere if nel behavior
✅ GIUSTO: Spostare validazioni specifiche negli handler o usare FluentValidation
Perché: Il behavior diventa unmaintainable
```

#### ❌ Modificare la Request
```
Scenario: Vuoi normalizzare l'email nel behavior prima del handler.
❌ SBAGLIATO:
public async Task<TResponse> Handle(...)
{
    if (request is IHasEmail emailReq)
        emailReq.Email = emailReq.Email.ToLower().Trim();
    return await next();
}
✅ GIUSTO: Normalizza nell'handler o nel Value Object Email
Perché: I behavior devono essere read-only sulla request
```

#### ❌ Calcoli di Business
```
Scenario: Calcolare il prezzo finale con tasse e sconti.
❌ SBAGLIATO: PricingBehavior che calcola prezzi
✅ GIUSTO: PricingService nel Domain chiamato dall'handler
Perché: Calcoli = business logic, NON infrastruttura
```

#### ❌ Orchestrazione Multi-Step
```
Scenario: CreateOrder deve anche SendEmail e UpdateInventory.
❌ SBAGLIATO: OrchestrationBehavior che coordina operazioni
✅ GIUSTO: Usa Domain Events o Saga pattern
Perché: Orchestrazione complessa non è cross-cutting concern
```

#### ❌ Dipendenze dal Domain
```
Scenario: Behavior che chiama Order.ApplyDiscount() direttamente.
❌ SBAGLIATO: Behavior che conosce le Entity del Domain
✅ GIUSTO: Solo gli Handler chiamano le Entity
Perché: Viola dependency rule (Application → Domain OK, Infrastructure → Domain NO)
```

#### ❌ Un Solo Command
```
Scenario: Solo SendEmailCommand ha bisogno di rate limiting.
❌ SBAGLIATO: RateLimitBehavior globale con if (request is SendEmailCommand)
✅ GIUSTO: Metti il rate limiting nel SendEmailHandler
Perché: Se serve solo a uno, non è cross-cutting
```

#### ❌ Side Effects Nascosti
```
Scenario: Behavior che invia analytics a servizio esterno.
❌ SBAGLIATO: AnalyticsBehavior che fa HTTP call nascosto
✅ GIUSTO: Domain Event + handler dedicato per analytics
Perché: Side effect nascosto = debugging nightmare
```

### 🎯 Regola d'Oro

**Pipeline Behavior** = Cross-cutting concern (validazione, logging, transazioni)
**Handler** = Business logic
**Domain** = Regole di business e invarianti

Se non riesci a dire "questo si applica a TUTTI (o quasi) i command/query", probabilmente NON serve un behavior.

**Anti-pattern:**
```csharp
// ❌ SBAGLIATO: Business logic nel behavior
public class DiscountBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
{
    public async Task<TResponse> Handle(...)
    {
        // ❌ Questo è business logic, NON cross-cutting concern!
        if (request is CreateOrderCommand cmd && cmd.Quantity > 10)
        {
            cmd.ApplyBulkDiscount(0.1m);
        }

        return await next();
    }
}

// ✅ GIUSTO: Business logic nel Domain/Handler
public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, int>
{
    public async Task<int> Handle(CreateOrderCommand request, ...)
    {
        var discount = request.Quantity > 10 ? 0.1m : 0m;
        var order = Order.Create(request.ProductName, request.Quantity, discount);
        // ...
    }
}
```

---

## Pro e Contro

### ✅ Vantaggi
- **DRY**: Elimina codice duplicato (validazione, logging, etc.)
- **SRP**: Handler fanno SOLO business logic
- **Testabilità**: Puoi testare handler e behavior separatamente
- **Flessibilità**: Aggiungi/rimuovi behavior senza toccare handler
- **Composizione**: Componi behavior in ordini diversi per scenari diversi
- **Manutenibilità**: Cambio validazione → tocco solo ValidationBehavior

### ❌ Svantaggi
- **Complessità nascosta**: Non è ovvio a prima vista cosa succede quando chiami `Send()`
- **Debugging più difficile**: Devi seguire la catena di behavior
- **Ordine critico**: L'ordine di registrazione conta, errori sottili
- **Over-engineering**: Se hai 3 handler, forse non serve
- **Performance overhead**: Ogni behavior aggiunge un piccolo overhead

---

## Collegamenti

- [[cqrs-pattern]] - CQRS usa spesso MediatR + Behaviors
- [[decorator-pattern]] - Pipeline Behavior È un Decorator
- [[cross-cutting-concerns]] - Behaviors risolvono cross-cutting concerns
- [[fluent-validation]] - Validazione usata nei Behaviors
- [[single-responsibility-principle]] - SRP applicato ai handler
- [[validation-vs-invariants]] — ValidationBehavior implementa validazione Application-level
- [[open-closed-principle]] — Behaviors aggiungono funzionalità senza modificare handlers
- [[domain-events-theory]] — Behavior chain può dispatchare eventi pre/post handler

---

## Quiz

### Q1: Ordine di esecuzione dei Behaviors

Hai registrato i behavior in questo ordine:
```csharp
cfg.AddBehavior<LoggingBehavior>();
cfg.AddBehavior<ValidationBehavior>();
cfg.AddBehavior<TransactionBehavior>();
```

In che ordine vengono eseguiti i metodi "AFTER" (dopo il handler)?

A) Logging → Validation → Transaction
B) Transaction → Validation → Logging
C) Validation → Transaction → Logging
D) L'ordine è casuale

<details>
<summary>Risposta</summary>

**B) Transaction → Validation → Logging**

I behavior sono come matrioske: l'ordine AFTER è **inverso** rispetto al BEFORE.

```
BEFORE:  Logging → Validation → Transaction → Handler
AFTER:   Handler → Transaction → Validation → Logging
```

Pensa allo stack di chiamate:
1. Logging.Handle() chiama next() → entra in Validation
2. Validation.Handle() chiama next() → entra in Transaction
3. Transaction.Handle() chiama next() → entra in Handler
4. Handler finisce → torna a Transaction (after)
5. Transaction finisce → torna a Validation (after)
6. Validation finisce → torna a Logging (after)

</details>

---

### Q2: Validazione fallita - Cosa succede?

Un ValidationBehavior lancia `ValidationException` se la validazione fallisce. Cosa succede ai behavior "after" degli altri behavior?

A) Vengono eseguiti normalmente
B) Non vengono eseguiti perché l'eccezione li salta
C) Dipende dall'ordine dei behavior
D) Solo i behavior prima di ValidationBehavior eseguono gli "after"

<details>
<summary>Risposta</summary>

**D) Solo i behavior prima di ValidationBehavior eseguono gli "after"**

Se ValidationBehavior lancia eccezione **prima** di chiamare `next()`, la catena si interrompe:

```csharp
// LoggingBehavior (outer)
public async Task<TResponse> Handle(...)
{
    _logger.LogInformation("Starting");  // ✅ ESEGUITO

    try
    {
        var response = await next();     // ← ValidationBehavior lancia eccezione qui

        _logger.LogInformation("Success"); // ❌ MAI ESEGUITO
    }
    catch (ValidationException ex)
    {
        _logger.LogError("Failed");       // ✅ ESEGUITO (catch)
        throw;
    }
}
```

I behavior **dopo** ValidationBehavior (es. TransactionBehavior) non vengono MAI chiamati se la validazione fallisce.

</details>

---

### Q3: Business Logic nel Behavior?

Un collega ha scritto questo behavior:

```csharp
public class OrderDiscountBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
{
    public async Task<TResponse> Handle(TRequest request, RequestHandlerDelegate<TResponse> next, ...)
    {
        if (request is CreateOrderCommand cmd)
        {
            // Applica sconto 10% se quantity > 100
            if (cmd.Quantity > 100)
            {
                cmd.ApplyDiscount(0.10m);
            }
        }

        return await next();
    }
}
```

Cosa c'è di sbagliato?

<details>
<summary>Risposta</summary>

**Violazione SRP + Mixing of Concerns**

❌ **Problemi:**
1. **Business logic nel behavior**: Lo sconto è business logic, NON cross-cutting concern
2. **Behavior command-specific**: Pipeline Behavior deve essere generico
3. **Difficile testare**: La logica di sconto è nascosta nel behavior
4. **Difficile trovare**: Nessuno cercherebbe la logica sconto in un behavior

✅ **Soluzione corretta:**

```csharp
// Business logic nel Domain/Handler
public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, int>
{
    public async Task<int> Handle(CreateOrderCommand request, ...)
    {
        var discount = _discountService.CalculateDiscount(request.Quantity);
        var order = Order.Create(request.ProductName, request.Quantity, discount);
        // ...
    }
}
```

**Regola d'oro:** Pipeline Behavior = Solo cross-cutting concerns (validazione, logging, transazioni). Business logic = Domain/Handler.

</details>

---

## Risorse per Approfondire

- **🎬 [Nick Chapsas - Validation using MediatR's Pipeline Behaviors and FluentValidation](https://www.youtube.com/watch?v=2JzQuIvxIqk)** - Video originale che Dan ha visto
- **📖 [MediatR Official Docs - Behaviors](https://github.com/jbogard/MediatR/wiki/Behaviors)** - Documentazione ufficiale
- **📝 [Milan Jovanovic - CQRS Validation Pipeline](https://www.milanjovanovic.tech/blog/cqrs-validation-with-mediatr-pipeline-and-fluentvalidation)** - Articolo completo su validazione
- **📝 [Jimmy Bogard - MediatR Pipeline Examples](https://lostechies.com/jimmybogard/2014/09/09/tackling-cross-cutting-concerns-with-a-mediator-pipeline/)** - Creatore di MediatR spiega i pattern
- **📖 [FluentValidation Docs](https://docs.fluentvalidation.net/)** - Documentazione validazione

---

*Nota aggiornata da Dan dopo aver completato il video di Nick Chapsas il 2026-02-26*
