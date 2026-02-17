---
tags:
  - p1
  - application-layer
  - cqrs
  - from/week-03
  - status/learning
aliases:
  - Queries
  - Query Handler
  - Read Operations
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# CQRS: Queries (Read Operations)

> **One-liner:** Le Queries sono operazioni di sola lettura che ritornano DTOs senza mai modificare lo stato del sistema.

## Cos'è

In CQRS (Command Query Responsibility Segregation), una **Query** è un'operazione che:
- **Legge** dati dal sistema
- **Non modifica** mai lo stato
- **Ritorna un DTO**, non l'Entity del Domain

### Principio CQS (Bertrand Meyer)

> "Ogni metodo dovrebbe essere o un Command che esegue un'azione, o una Query che ritorna dati, ma mai entrambi."

## Confronto Command vs Query

| Aspetto | Command | Query |
|---------|---------|-------|
| **Scopo** | Modifica stato | Legge stato |
| **Return type** | `Guid`, `bool`, `Result` | `Dto`, `List<Dto>` |
| **UnitOfWork** | ✅ Sì (SaveChanges) | ❌ No |
| **Validazione** | FluentValidation completa | Minima (solo parametri) |
| **Idempotente** | Spesso no | Sempre sì |
| **Può essere cached** | No | Sì |

## Quando usarlo

**USA Queries separate quando:**
- Vuoi proteggere il Domain (non esporre Entity)
- Hai bisogno di DTOs specifici per ogni use case
- Vuoi poter cacheare le letture
- Vuoi scalare letture e scritture separatamente

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| CRUD semplice | Overhead inutile |
| Entity = DTO | Se non hai logica nel Domain |
| Progetto piccolissimo | Overkill |

## Esempio

### Query (Request)

```csharp
// Application/Queries/Notifications/GetNotificationByIdQuery.cs
public record GetNotificationByIdQuery(Guid Id) : IRequest<NotificationDto?>;
```

### Query Handler

```csharp
// Application/Queries/Notifications/GetNotificationByIdHandler.cs
public class GetNotificationByIdHandler : IRequestHandler<GetNotificationByIdQuery, NotificationDto?>
{
    private readonly INotificationRepository _repository;
    // ⚠️ NOTA: Niente IUnitOfWork! Le Query non salvano.

    public GetNotificationByIdHandler(INotificationRepository repository)
    {
        _repository = repository;
    }

    public async Task<NotificationDto?> Handle(
        GetNotificationByIdQuery query,
        CancellationToken cancellationToken)
    {
        // 1. Leggi dal repository
        var notification = await _repository.GetByIdAsync(query.Id, cancellationToken);

        if (notification is null)
            return null;

        // 2. Mappa Entity → DTO (OBBLIGATORIO!)
        return new NotificationDto(
            Id: notification.Id,
            Recipient: notification.Recipient,
            Channel: notification.Channel.ToString(),  // Enum → string
            Content: notification.Content,
            Subject: notification.Subject,
            Status: notification.Status.ToString(),
            Priority: notification.Priority.ToString(),
            CreatedAt: notification.CreatedAt,
            ScheduledAt: notification.ScheduledAt,
            SentAt: notification.SentAt
        );
    }
}
```

### DTO (Response)

```csharp
// Application/DTOs/NotificationDto.cs
public record NotificationDto(
    Guid Id,
    string Recipient,
    string Channel,      // Stringa, non enum (disaccoppiamento)
    string Content,
    string? Subject,
    string Status,
    string Priority,
    DateTime CreatedAt,
    DateTime? ScheduledAt,
    DateTime? SentAt
);
```

### Query senza parametri

```csharp
// Nessun parametro = niente da validare
public record GetPendingNotificationsQuery() : IRequest<IReadOnlyList<NotificationDto>>;
```

## Perché ritornare DTO invece di Entity?

| Entity | DTO |
|--------|-----|
| Ha metodi di business (`Cancel()`, `Retry()`) | Solo dati, nessun metodo |
| Può essere modificata | Immutabile (record) |
| Espone il Domain all'esterno | Disaccoppiata dal Domain |
| Potrebbe avere troppi dati | Solo ciò che serve al chiamante |

**Esempio di problema se ritorni Entity:**

```csharp
// ❌ PERICOLOSO
var notification = await _mediator.Send(new GetByIdQuery(id));
notification.Cancel();  // L'Entity è uscita dal Domain, chi la salva?
// Stato inconsistente!
```

```csharp
// ✅ SICURO
var dto = await _mediator.Send(new GetByIdQuery(id));
dto.Cancel();  // ❌ ERRORE DI COMPILAZIONE! Il DTO non ha metodi.
```

## Flusso Query

```
API Controller
      │
      ▼
┌─────────────────┐
│ GetByIdQuery    │  ← Request (record con parametri)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ValidationBeh.  │  ← Valida parametri (se presenti)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LoggingBehavior │  ← Logga request/response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Query Handler   │  ← Legge da Repository, mappa a DTO
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ NotificationDto │  ← Response (record immutabile)
└─────────────────┘
```

## Collegamenti

- [[cqrs-and-mediatr]] - Panoramica completa CQRS con MediatR
- [[ports-and-adapters]] - Come le Query usano i Repository (Ports)
- [[fluentvalidation]] - Validazione (minima) nelle Query

## Domande dalla Sessione

### D: Un Query Handler usa UnitOfWork e chiama SaveChanges. Cosa c'è di sbagliato?
**R:** Tre errori:
1. Una Query non deve mai modificare lo stato
2. Non deve mai chiamare SaveChanges
3. Se modifica qualcosa (es. `MarkAsViewed()`), deve essere un Command, non una Query

### D: Perché le Query ritornano DTO invece di Entity?
**R:** Per proteggere il Domain:
- Il DTO è immutabile (record) - non può essere modificato
- Non ha metodi di business - nessuno può chiamare `Cancel()` su un DTO
- Contiene solo ciò che serve al chiamante
- Disaccoppia API dal Domain (cambio interno ≠ cambio API)

### D: Una Query senza parametri ha bisogno di validazione?
**R:** No. Se non ci sono parametri di input, non c'è nulla da validare. Il validator sarebbe vuoto. Esempio: `GetPendingNotificationsQuery()` non ha parametri.

## Quiz

### Q1: Cosa ritorna una Query?
Una Query deve ritornare:
A) L'Entity del Domain
B) Un DTO immutabile
C) Un bool per indicare successo
D) Void

<details>
<summary>Risposta</summary>

**B) Un DTO immutabile**

Le Query ritornano sempre dati sotto forma di DTO (Data Transfer Object). Mai Entity (espone il Domain), mai void (quello è per i Command che non ritornano dati), mai bool (quello è per Command come Cancel/Delete).
</details>

### Q2: Trova l'errore
```csharp
public async Task<NotificationDto> Handle(GetByIdQuery query, CancellationToken ct)
{
    var notification = await _repository.GetByIdAsync(query.Id, ct);
    notification.IncrementViewCount();
    await _unitOfWork.SaveChangesAsync(ct);
    return MapToDto(notification);
}
```

<details>
<summary>Risposta</summary>

L'handler sta **modificando lo stato** (`IncrementViewCount()`) e **salvando** (`SaveChangesAsync`). Questo viola il principio delle Query: solo lettura, mai scrittura.

Se serve tracciare le visualizzazioni, deve essere un **Command separato** (`IncrementViewCountCommand`), oppure un evento asincrono.
</details>

### Q3: Query con filtri
Hai bisogno di una query che ritorni le notifiche filtrate per status E per data. Come la modelli?

<details>
<summary>Risposta</summary>

```csharp
public record GetNotificationsByFilterQuery(
    NotificationStatus? Status,
    DateTime? FromDate,
    DateTime? ToDate
) : IRequest<IReadOnlyList<NotificationDto>>;
```

I parametri sono opzionali (`?`) così puoi usare la stessa Query per diversi filtri. Il validator può verificare che `FromDate <= ToDate` se entrambi sono specificati.
</details>

---

## Risorse per Approfondire

- **[CQRS - Martin Fowler](https://martinfowler.com/bliki/CQRS.html)** - Introduzione al pattern
- **[CQS vs CQRS - Udi Dahan](https://udidahan.com/2009/12/09/clarified-cqrs/)** - Differenza tra i due concetti
- **[MediatR Wiki](https://github.com/jbogard/MediatR/wiki)** - Implementazione pratica
