---
tags:
  - p1
  - application-layer
  - cqrs
  - from/week-03
  - status/learning
aliases:
  - Commands
  - Command Handler
  - Write Operations
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# CQRS: Commands (Write Operations)

> **One-liner:** I Commands sono operazioni che modificano lo stato del sistema, ritornando solo dati primitivi (Guid, bool) e mai DTOs complessi.

## Cos'è

In CQRS (Command Query Responsibility Segregation), un **Command** è un'operazione che:
- **Modifica** lo stato del sistema
- **Ritorna dati semplici** - Guid, bool, Result - mai DTOs
- **Ha nome imperativo** - Schedule, Cancel, Retry (non GetXxx)

### Principio CQS (Bertrand Meyer)

> "Ogni metodo dovrebbe essere o un Command che esegue un'azione, o una Query che ritorna dati, ma mai entrambi."

**IMPORTANTE:** CQS si applica all'**interfaccia pubblica**, non alle operazioni interne. Un Command può (e spesso deve) leggere dati internamente per completare la sua operazione.

## Confronto Command vs Query

| Aspetto | Command | Query |
|---------|---------|-------|
| **Scopo** | Modifica stato | Legge stato |
| **Nome** | Imperativo (Create, Cancel) | Interrogativo (Get, Find) |
| **Return type** | `Guid`, `bool`, `Result<T>` | `Dto`, `List<Dto>` |
| **UnitOfWork** | ✅ Sì (SaveChanges) | ❌ No |
| **Validazione** | Completa (FluentValidation) | Minima (solo parametri) |
| **Idempotente** | Spesso no | Sempre sì |
| **Può leggere internamente** | ✅ Sì (per modificare) | N/A |

## Cosa Ritorna un Command

| Tipo ritorno | Quando | Esempio |
|--------------|--------|---------|
| `Guid` | Creazione - serve l'ID | `ScheduleNotificationCommand → Guid` |
| `bool` | Operazione sì/no | `CancelNotificationCommand → bool` |
| `Result<T>` | Gestione errori esplicita | `RetryCommand → Result<bool>` |
| `Unit` | Fire-and-forget | `LogEventCommand → Unit` |

### Cosa NON Ritorna

```csharp
// ❌ SBAGLIATO: Command che ritorna DTO
public record CreateOrderCommand(...) : IRequest<OrderDto>;

// ✅ CORRETTO: Command ritorna solo l'ID
public record CreateOrderCommand(...) : IRequest<Guid>;

// Se serve il DTO dopo la creazione, il chiamante fa due operazioni:
var orderId = await _mediator.Send(new CreateOrderCommand(...));
var orderDto = await _mediator.Send(new GetOrderByIdQuery(orderId));
```

## Quando usarlo

**USA Commands quando:**
- Crei, modifichi o elimini dati
- L'operazione ha side effects
- Serve validazione completa dell'input
- Devi gestire transazioni (UnitOfWork)

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| Solo lettura dati | Usa Query |
| Ritornare oggetti complessi | Usa Query dopo il Command |
| Operazioni idempotenti pure | Probabilmente è una Query |

## Esempio

### Command (Request)

```csharp
// Application/Commands/Notifications/ScheduleNotificationCommand.cs
public record ScheduleNotificationCommand(
    string Recipient,
    NotificationChannel Channel,
    string Content,
    string? Subject,
    NotificationPriority Priority,
    DateTime? ScheduledAt
) : IRequest<Guid>;
```

### Command Handler

```csharp
// Application/Commands/Notifications/ScheduleNotificationHandler.cs
public class ScheduleNotificationHandler : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    private readonly INotificationRepository _repository;
    private readonly IUnitOfWork _unitOfWork;
    private readonly IDateTimeProvider _dateTimeProvider;

    public ScheduleNotificationHandler(
        INotificationRepository repository,
        IUnitOfWork unitOfWork,
        IDateTimeProvider dateTimeProvider)
    {
        _repository = repository;
        _unitOfWork = unitOfWork;
        _dateTimeProvider = dateTimeProvider;
    }

    public async Task<Guid> Handle(
        ScheduleNotificationCommand command,
        CancellationToken cancellationToken)
    {
        // 1. Crea Entity (Domain decide le regole)
        var notification = new Notification(
            command.Recipient,
            command.Channel,
            command.Content,
            command.Subject,
            command.Priority,
            command.ScheduledAt ?? _dateTimeProvider.UtcNow
        );

        // 2. Persisti via Repository
        await _repository.AddAsync(notification, cancellationToken);

        // 3. Salva transazione
        await _unitOfWork.SaveChangesAsync(cancellationToken);

        // 4. Ritorna ID (non DTO!)
        return notification.Id;
    }
}
```

### Command che Legge e Modifica

```csharp
// Application/Commands/Notifications/CancelNotificationHandler.cs
public class CancelNotificationHandler : IRequestHandler<CancelNotificationCommand, bool>
{
    private readonly INotificationRepository _repository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<bool> Handle(
        CancelNotificationCommand command,
        CancellationToken cancellationToken)
    {
        // ✅ CORRETTO: Legge internamente per modificare
        var notification = await _repository.GetByIdAsync(
            command.NotificationId,
            cancellationToken);

        if (notification is null)
            return false;

        // Chiama metodo Domain (business rule nel Domain)
        notification.Cancel();

        // Aggiorna e salva
        await _repository.UpdateAsync(notification, cancellationToken);
        await _unitOfWork.SaveChangesAsync(cancellationToken);

        return true;
    }
}
```

## Flusso Command

```
API Controller
      │
      ▼
┌─────────────────┐
│ Command         │  ← Record con dati di input
│ (ScheduleNot..) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ValidationBeh.  │  ← FluentValidation (input completo)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LoggingBehavior │  ← Logga request/response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Command Handler │  ← Può leggere internamente!
│  1. GetById     │
│  2. Modify      │
│  3. SaveChanges │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Guid / bool     │  ← Ritorno primitivo
└─────────────────┘
```

## Perché il Command Può Leggere Internamente?

### Malinteso Comune

> "CQS dice che i Command non possono leggere, quindi devo fare prima una Query e poi il Command"

### Realtà

CQS si applica all'**interfaccia pubblica**. Internamente, un Command fa tutto il necessario:

```csharp
// ❌ SBAGLIATO: Logica nel chiamante
var notification = await _mediator.Send(new GetByIdQuery(id));  // Query
if (notification.Status == "Pending")
{
    await _mediator.Send(new CancelCommand(id));  // Command
}

// Problemi:
// 1. Race condition tra le due chiamate
// 2. Business logic nel Controller
// 3. Due round-trip al database
```

```csharp
// ✅ CORRETTO: Tutto nel Command
await _mediator.Send(new CancelCommand(id));

// Il Command Handler gestisce tutto:
// - Legge la notifica
// - Verifica se cancellabile (business rule)
// - Cancella
// - Salva
```

## Collegamenti

- [[cqrs-queries]] - Le operazioni di lettura (complemento)
- [[cqrs-and-mediatr]] - Panoramica CQRS con MediatR
- [[fluentvalidation]] - Validazione input nei Commands
- [[application-layer]] - Dove vivono i Commands

## Domande dalla Sessione

### D: CreateUserCommand ritorna UserDto - cosa c'è di sbagliato?
**R:** Un Command non deve ritornare dati complessi. Ritorna solo:
- `Guid` (ID creato)
- `bool` (successo/fallimento)
- `Result<T>` (con errori espliciti)

Se serve il DTO, il chiamante fa: `Create → GetById`.

### D: Un Command può chiamare GetByIdAsync internamente?
**R:** **Sì!** CQS si applica all'interfaccia pubblica, non alle operazioni interne. Un Command spesso DEVE leggere per modificare:
1. Recupera l'Entity
2. Chiama metodo di modifica
3. Salva

Il chiamante non deve fare Query + Command separati (race condition, logica duplicata).

### D: Cosa ritorna CancelNotificationCommand?
**R:** `bool` - true se cancellato, false se non trovato o non cancellabile. È un dato primitivo, appropriato per un Command.

## Quiz

### Q1: Return type corretto
Quale return type è appropriato per `CreateProductCommand`?

A) `ProductDto`
B) `Product` (Entity)
C) `Guid`
D) `List<ProductDto>`

<details>
<summary>Risposta</summary>

**C) Guid**

I Commands ritornano dati primitivi. Per un'operazione di creazione, l'ID del nuovo oggetto è sufficiente. Se serve il DTO completo, il chiamante fa una Query separata.
</details>

### Q2: Lettura nel Command
```csharp
public async Task<bool> Handle(DeleteOrderCommand cmd, CancellationToken ct)
{
    var order = await _repository.GetByIdAsync(cmd.OrderId, ct);
    if (order is null) return false;

    await _repository.DeleteAsync(order, ct);
    await _unitOfWork.SaveChangesAsync(ct);
    return true;
}
```

Questo handler viola CQS perché legge prima di cancellare?

<details>
<summary>Risposta</summary>

**No, è corretto.**

CQS si applica all'interfaccia pubblica del metodo, non alle operazioni interne. Il Command:
- Ha un **unico scopo pubblico**: cancellare
- **Non ritorna dati complessi**: solo bool
- Legge internamente solo per completare la sua operazione

Un Command può (e deve) leggere internamente quando necessario.
</details>

### Q3: Due chiamate vs Una
Un collega scrive:
```csharp
// Nel Controller
var notification = await _mediator.Send(new GetNotificationQuery(id));
if (notification.Status == "Pending")
{
    await _mediator.Send(new CancelNotificationCommand(id));
}
```

Cosa c'è di sbagliato?

<details>
<summary>Risposta</summary>

Tre problemi:

1. **Race condition**: Tra la Query e il Command, qualcun altro potrebbe modificare la notifica
2. **Business logic nel Controller**: La regola "solo Pending si può cancellare" dovrebbe essere nel Domain
3. **Due round-trip**: Inefficiente

**Soluzione:**
```csharp
// Controller chiama solo il Command
var cancelled = await _mediator.Send(new CancelNotificationCommand(id));

// Il Command Handler gestisce tutto internamente
```
</details>

---

## Risorse per Approfondire

- **[CQRS - Martin Fowler](https://martinfowler.com/bliki/CQRS.html)** - Introduzione al pattern
- **[CQS vs CQRS - Udi Dahan](https://udidahan.com/2009/12/09/clarified-cqrs/)** - Differenza tra i due concetti
- **[MediatR Wiki](https://github.com/jbogard/MediatR/wiki)** - Implementazione pratica
- **[Commands in Clean Architecture](https://jasontaylor.dev/clean-architecture-getting-started/)** - Jason Taylor
