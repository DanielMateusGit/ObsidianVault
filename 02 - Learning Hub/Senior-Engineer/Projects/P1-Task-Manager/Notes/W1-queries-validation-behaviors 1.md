# W1 - Queries, FluentValidation & Pipeline Behaviors

> **Data:** 2026-03-21
> **Fase:** Week 1 - Application Layer (parte 2)

---

## 1. CQRS Queries

### Concetto

Nel CQRS, le Queries sono il mirror dei Commands:

| | Command | Query |
|---|---------|-------|
| **Scopo** | Modifica stato | Legge stato |
| **Return** | ID o void/Unit | DTO con dati |
| **Side effects** | Si (DB, eventi) | **MAI** (solo lettura) |
| **Validazione** | Spesso necessaria | Raramente |
| **Dipendenze** | Repository + UnitOfWork | Solo Repository |

**Regole chiave:**
1. Una Query **non deve MAI** modificare lo stato (no SaveChanges, no Add, no Delete)
2. Una Query ritorna **DTO**, non Entity — l'Entity ha comportamento che il chiamante non deve vedere
3. Il mapping Entity -> DTO avviene **nell'handler**, non nel repository
4. Il filtro che riduce dati dal DB va nel **repository** (WHERE a livello SQL), non nell'handler (filtro in memoria)

### Struttura

```csharp
// La Query — record immutabile
public record GetTaskByIdQuery(Guid TaskId) : IRequest<TaskItemDto?>;

// L'Handler — solo lettura + mapping
public class GetTaskByIdHandler : IRequestHandler<GetTaskByIdQuery, TaskItemDto?>
{
    private readonly ITaskRepository _repository;
    // NO IUnitOfWork — non modifichiamo nulla

    public async Task<TaskItemDto?> Handle(GetTaskByIdQuery request, CancellationToken ct)
    {
        TaskItem? task = await _repository.GetById(request.TaskId, ct);
        if (task == null) return null;

        return new TaskItemDto(
            task.Id, task.Title, task.Priority.Name,
            task.IsCompleted, task.CreatedAt, task.CompletedAt
        );
    }
}
```

### Query implementate

| Query | Input | Output | Caso null/vuoto |
|-------|-------|--------|-----------------|
| `GetTaskByIdQuery` | `Guid TaskId` | `TaskItemDto?` | Ritorna null |
| `GetAllTasksQuery` | nessuno | `IEnumerable<TaskItemDto>` | Lista vuota |
| `GetTaskByStatusQuery` | `bool IsCompleted` | `IEnumerable<TaskItemDto>` | Lista vuota |

`GetByStatus` ha richiesto di aggiungere il metodo all'interfaccia `ITaskRepository`:
```csharp
Task<IEnumerable<TaskItem>> GetByStatus(bool isCompleted, CancellationToken ct = default);
```

---

## 2. FluentValidation

### Due livelli di validazione (confini diversi!)

| Livello | Dove | Cosa valida | Esempio |
|---------|------|-------------|---------|
| **Application** | FluentValidation | Formato input (sintassi) | Titolo non vuoto, Guid non empty |
| **Domain** | Entity | Regole di business (semantica) | Task gia completato |

**Non sono duplicati** — proteggono confini diversi:
- FluentValidation protegge l'**input della request** (bouncer alla porta)
- Il Domain protegge l'**invariante dell'Entity** (logica di business)

### Cosa NON fare in un Validator

- **NO** query al database (`MustAsync` con `_repo.ExistsAsync()`)
- **NO** logica di business
- **NO** dipendenze da servizi esterni

Un Validator valida solo il **formato** dell'input.

### Struttura

```csharp
// Application/Validators/CreateTaskItemCommandValidator.cs
public class CreateTaskItemCommandValidator : AbstractValidator<CreateTaskItemCommand>
{
    public CreateTaskItemCommandValidator()
    {
        RuleFor(x => x.Title)
            .NotEmpty().WithMessage("Il titolo e obbligatorio")
            .MaximumLength(200).WithMessage("Il titolo non puo superare 200 caratteri");
    }
}
```

`AbstractValidator<T>` viene dal pacchetto **FluentValidation** (non MediatR). Ogni Validator sa le regole per UN comando specifico.

### Regole per i 4 Commands

| Command | Regole |
|---------|--------|
| `CreateTaskItemCommand` | Title: NotEmpty, MaxLength(200) |
| `UpdateTaskItemCommand` | TaskItemId: NotEqual(Guid.Empty). Title: NotEmpty, MaxLength(200) |
| `CompleteTaskItemCommand` | TaskId: NotEqual(Guid.Empty) |
| `DeleteTaskItemCommand` | TaskItemId: NotEqual(Guid.Empty) |

### Come testare un Validator

```csharp
[Fact]
public void ShouldHaveError_WhenTitleIsEmpty()
{
    var validator = new CreateTaskItemCommandValidator();
    var command = new CreateTaskItemCommand("", Priority.High);

    var result = validator.TestValidate(command);

    result.ShouldHaveValidationErrorFor(x => x.Title);
}

[Fact]
public void ShouldNotHaveError_WhenCommandIsValid()
{
    var validator = new CreateTaskItemCommandValidator();
    var command = new CreateTaskItemCommand("Titolo valido", Priority.High);

    var result = validator.TestValidate(command);

    result.ShouldNotHaveAnyValidationErrors();
}
```

---

## 3. Pipeline Behaviors (MediatR Middleware)

### I tre pezzi e come si collegano

Pensa a un ristorante:

| Cosa | Pacchetto | Ruolo | Analogia |
|------|-----------|-------|----------|
| `AbstractValidator<T>` | FluentValidation | Definisce le regole per UN comando | Il cameriere che controlla la prenotazione |
| `IPipelineBehavior<T,R>` | MediatR | Interfaccia generica per uno step nella pipeline | Il corridoio tra la porta e la cucina |
| `ValidationBehavior` | **Lo scrivi tu** | Un behavior specifico che esegue i validator | Un controllo che metti nel corridoio |

```
                     IPipelineBehavior (il concetto generico - interfaccia MediatR)
                    /                    \
       ValidationBehavior            LoggingBehavior
       (usa i Validator)             (logga le request)
            |
  ┌─────────┼──────────┐
  │         │          │
Create    Update    Delete
Validator Validator Validator
       (FluentValidation)
```

**IPipelineBehavior** e' lo stesso concetto dei **middleware di ASP.NET** — ma invece di intercettare richieste HTTP, intercetta Commands e Queries di MediatR. Qualsiasi classe che lo implementa diventa uno step nella catena.

**ValidationBehavior** e' la **colla** tra MediatR e FluentValidation. Per ogni request in arrivo, va a cercare TUTTI i Validator registrati per quel comando e li esegue. Se anche uno solo fallisce, blocca tutto. Se passano tutti, chiama `next()` e la request prosegue verso l'Handler. Senza di esso, i Validator esistono ma nessuno li chiama.

### Il flusso completo

```
Request entra
    → PipelineBehavior 1 (es. ValidationBehavior)
        → PipelineBehavior 2 (es. LoggingBehavior)
            → Handler (esegue la logica)
        ← ritorna
    ← ritorna
← Response esce
```

### ValidationBehavior — codice

```csharp
// Application/Behaviors/ValidationBehavior.cs
public class ValidationBehavior<TRequest, TResponse>
    : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    // MediatR inietta TUTTI i Validator registrati per questo TRequest
    public ValidationBehavior(IEnumerable<IValidator<TRequest>> validators)
    {
        _validators = validators;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,  // il prossimo step
        CancellationToken ct)
    {
        // 1. Esegui tutti i validator
        var context = new ValidationContext<TRequest>(request);
        var failures = _validators
            .Select(v => v.Validate(context))
            .SelectMany(result => result.Errors)
            .Where(f => f != null)
            .ToList();

        // 2. Se errori → lancia eccezione, NON chiama next()
        if (failures.Any())
            throw new ValidationException(failures);

        // 3. Se OK → passa al prossimo step
        return await next();
    }
}
```

**Punto chiave:** `next()` e' la chiamata all'Handler (o al behavior successivo). Se la validazione fallisce, `next()` non viene MAI chiamato.

### Come testare un Behavior

```csharp
[Fact]
public async Task ShouldThrow_WhenValidationFails()
{
    var command = new CreateTaskItemCommand("", Priority.High);
    var validator = new CreateTaskItemCommandValidator();
    var behavior = new ValidationBehavior<CreateTaskItemCommand, Guid>(
        new[] { validator }
    );

    // next() non dovrebbe mai essere chiamato
    RequestHandlerDelegate<Guid> next = () => Task.FromResult(Guid.NewGuid());

    await Assert.ThrowsAsync<ValidationException>(
        () => behavior.Handle(command, next, CancellationToken.None)
    );
}

[Fact]
public async Task ShouldCallNext_WhenValidationPasses()
{
    var command = new CreateTaskItemCommand("Titolo valido", Priority.High);
    var validator = new CreateTaskItemCommandValidator();
    var behavior = new ValidationBehavior<CreateTaskItemCommand, Guid>(
        new[] { validator }
    );

    var expectedId = Guid.NewGuid();
    RequestHandlerDelegate<Guid> next = () => Task.FromResult(expectedId);

    var result = await behavior.Handle(command, next, CancellationToken.None);

    result.Should().Be(expectedId);
}
```

### Registrazione (nel layer API, quando ci arriveremo)

```csharp
services.AddValidatorsFromAssembly(typeof(ApplicationAssembly).Assembly);
services.AddTransient(typeof(IPipelineBehavior<,>), typeof(ValidationBehavior<,>));
```

---

## Struttura file

```
Application/
├── Commands/          ← gia fatto
├── Queries/           ← fatto oggi
├── DTOs/              ← gia fatto
├── Interfaces/        ← gia fatto
├── Validators/        ← da fare
│   ├── CreateTaskItemCommandValidator.cs
│   ├── UpdateTaskItemCommandValidator.cs
│   ├── CompleteTaskItemCommandValidator.cs
│   └── DeleteTaskItemCommandValidator.cs
└── Behaviors/         ← da fare
    └── ValidationBehavior.cs
```

---

*Ultimo aggiornamento: 2026-03-21*
