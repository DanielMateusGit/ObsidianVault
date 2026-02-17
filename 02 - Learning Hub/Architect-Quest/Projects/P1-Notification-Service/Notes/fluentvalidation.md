---
tags:
  - p1
  - application-layer
  - validation
  - from/week-03
  - status/learning
aliases:
  - FluentValidation
  - Input Validation
  - ValidationBehavior
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# FluentValidation

> **One-liner:** Libreria che separa le regole di validazione input in classi dedicate con API fluent, integrandosi con MediatR tramite Pipeline Behaviors.

## Cos'è

FluentValidation è una libreria .NET che permette di definire regole di validazione per i tuoi oggetti in modo **dichiarativo** e **separato** dalla business logic.

Invece di spargere `if` di validazione negli handler:

```csharp
// ❌ Validazione mischiata con business logic
public async Task<Guid> Handle(ScheduleNotificationCommand request, ...)
{
    if (string.IsNullOrEmpty(request.Recipient))
        throw new ArgumentException("Recipient required");
    if (request.ScheduledFor < DateTime.UtcNow)
        throw new ArgumentException("Cannot schedule in the past");

    // ... business logic
}
```

Definisci una classe Validator dedicata:

```csharp
// ✅ Validazione separata
public class ScheduleNotificationCommandValidator : AbstractValidator<ScheduleNotificationCommand>
{
    public ScheduleNotificationCommandValidator()
    {
        RuleFor(x => x.Recipient)
            .NotEmpty().WithMessage("Recipient is required");

        RuleFor(x => x.ScheduledFor)
            .GreaterThan(DateTime.UtcNow).WithMessage("Cannot schedule in the past");
    }
}
```

### Integrazione con MediatR

FluentValidation si integra con MediatR tramite un **ValidationBehavior**:

```
Request → ValidationBehavior → [Validator] → Handler
              ↓ (se fallisce)
           Return Result.Failure
```

Il ValidationBehavior:
1. Trova tutti i validator registrati per il tipo di request
2. Li esegue **PRIMA** dell'handler
3. Se falliscono → ritorna errore (l'handler non viene mai chiamato)
4. Se passano → prosegue all'handler

## Quando usarlo

- **Commands/Queries con input da validare** - Qualsiasi request che arriva dall'esterno
- **Regole di validazione riusabili** - Es. validazione email usata in più posti
- **Separazione di responsabilità** - Handler puliti che fanno solo business logic
- **Validazioni complesse** - Condizionali, cross-field, con messaggi personalizzati

## Quando NON usarlo

| Situazione | Perché | Alternativa |
|------------|--------|-------------|
| **Business rules** | Non è validazione input | Domain (Entity) |
| **Validazione già nel Domain** | Evita duplicazione | Value Object |
| **Check esistenza entità** | È business logic, non input validation | Handler |
| **CRUD semplicissimi** | Overkill | Data annotations |

### Distinzione Critica: Input Validation vs Business Logic

| Tipo | Dove | HTTP Status | Esempio |
|------|------|-------------|---------|
| **Input validation** | FluentValidation | 400 Bad Request | "Guid vuoto", "Email non valida" |
| **Business logic** | Handler/Domain | 404/409/422 | "Notification non esiste", "Max retry reached" |

**Regola pratica:** Il Validator controlla la **forma** dell'input. L'Handler controlla se l'**operazione** è possibile.

## Esempio

### Validator

```csharp
public class ScheduleNotificationCommandValidator : AbstractValidator<ScheduleNotificationCommand>
{
    public ScheduleNotificationCommandValidator()
    {
        RuleFor(x => x.Recipient)
            .NotEmpty().WithMessage("Recipient is required")
            .MaximumLength(255).WithMessage("Recipient too long");

        RuleFor(x => x.Channel)
            .IsInEnum().WithMessage("Invalid notification channel");

        RuleFor(x => x.ScheduledFor)
            .GreaterThan(DateTime.UtcNow).WithMessage("Cannot schedule in the past");

        RuleFor(x => x.TemplateId)
            .NotEmpty().WithMessage("Template is required");

        // Validazione condizionale
        RuleFor(x => x.Recipient)
            .EmailAddress()
            .When(x => x.Channel == NotificationChannel.Email)
            .WithMessage("Invalid email format for email channel");
    }
}
```

### ValidationBehavior (Pipeline)

```csharp
public class ValidationBehavior<TRequest, TResponse> : IPipelineBehavior<TRequest, TResponse>
    where TRequest : IRequest<TResponse>
{
    private readonly IEnumerable<IValidator<TRequest>> _validators;

    public ValidationBehavior(IEnumerable<IValidator<TRequest>> validators)
    {
        _validators = validators;
    }

    public async Task<TResponse> Handle(
        TRequest request,
        RequestHandlerDelegate<TResponse> next,
        CancellationToken cancellationToken)
    {
        if (!_validators.Any())
            return await next();

        var context = new ValidationContext<TRequest>(request);

        var failures = _validators
            .Select(v => v.Validate(context))
            .SelectMany(result => result.Errors)
            .Where(f => f != null)
            .ToList();

        if (failures.Any())
            throw new ValidationException(failures);

        return await next();
    }
}
```

## Collegamenti

- [[cqrs-and-mediatr]] - MediatR e Pipeline Behaviors
- [[clean-architecture]] - Dove vive la validazione (Application Layer)
- [[domain-model-patterns]] - Value Objects per validazione domain

## Domande dalla Sessione

### D: Che regola FluentValidation metteresti per CancelNotificationCommand con NotificationId (Guid)?
**R:** `RuleFor(x => x.NotificationId).NotEmpty()` per escludere `Guid.Empty`. È input validation pura - verifica la forma, non l'esistenza.

### D: È una buona idea mettere MustAsync con ExistsAsync nel Validator?
**R:** No, è controverso. Il check di esistenza:
- Introduce dipendenze nel Validator (repository)
- Rende la validazione async e lenta
- Restituisce 400 invece di 404 (semanticamente sbagliato)
- È business logic, non input validation

Meglio controllare l'esistenza nell'Handler e ritornare 404.

### D: Se ValidationBehavior trova errori, cosa dovrebbe ritornare?
**R:** Un Result con l'errore, non un'eccezione. La validazione fallita è un flusso normale dell'applicazione, non qualcosa di "eccezionale".

## Quiz

### Q1: Input validation vs Business rule
Un collega mette questa regola nel Validator:
```csharp
RuleFor(x => x.UserId)
    .MustAsync(async (id, ct) => await _userRepo.HasPermissionAsync(id, "send_notification"))
    .WithMessage("User not authorized");
```
Cosa c'è di sbagliato?

<details>
<summary>Risposta</summary>

È una **business rule**, non input validation. Il check dei permessi:
- Dipende dallo stato del sistema (non dalla forma dell'input)
- Dovrebbe restituire 403 Forbidden, non 400 Bad Request
- Appartiene all'Handler o a un authorization middleware

Nel Validator metti solo: `RuleFor(x => x.UserId).NotEmpty()`
</details>

### Q2: Validazione condizionale
Come validi che `PhoneNumber` sia presente SOLO se `Channel == Sms`?

<details>
<summary>Risposta</summary>

```csharp
RuleFor(x => x.PhoneNumber)
    .NotEmpty()
    .When(x => x.Channel == NotificationChannel.Sms)
    .WithMessage("Phone number required for SMS channel");
```

Il metodo `.When()` applica la regola solo se la condizione è vera.
</details>

### Q3: Dove va il Validator?
In quale layer/progetto della Clean Architecture vive `ScheduleNotificationCommandValidator`?

<details>
<summary>Risposta</summary>

**Application Layer** - perché:
- Valida i Commands/Queries (che sono nell'Application)
- Non ha dipendenze dal Domain (non usa Entity o Value Objects)
- È un concern dell'orchestrazione, non della business logic

Path tipico: `Application/Validators/ScheduleNotificationCommandValidator.cs`
</details>

---

## Risorse per Approfondire

- **[FluentValidation Documentation](https://docs.fluentvalidation.net/)** - Docs ufficiale, molto completa
- **[FluentValidation with MediatR](https://code-maze.com/cqrs-mediatr-fluentvalidation/)** - Tutorial integrazione step-by-step
- **[Validation in DDD - Vladimir Khorikov](https://enterprisecraftsmanship.com/posts/validation-and-ddd/)** - Distinzione input vs domain validation
- **[Jimmy Bogard - Validation in CQRS](https://jimmybogard.com/validation-in-cqrs/)** - Best practices dal creatore di MediatR
