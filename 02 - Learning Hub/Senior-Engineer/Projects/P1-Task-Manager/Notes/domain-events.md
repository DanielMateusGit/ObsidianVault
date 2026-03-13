---
tags:
  - ddd
  - domain
  - events
  - from/senior-p1-week-01
  - status/learning
aliases:
  - Domain Event
  - Event Sourcing Light
created: 2026-03-03
source: "Sessione Senior P1 Week 1"
---

# Domain Events

> **One-liner:** L'entity registra che qualcosa è successo, qualcun altro reagisce. Zero dipendenze nell'entity.

## Il Problema

Dopo la creazione di un `TaskItem` vuoi:
- Inviare una notifica
- Aggiornare statistiche
- Loggare l'azione

**Soluzione sbagliata:**
```csharp
public TaskItem Create(...)
{
    var task = new TaskItem(...);
    _notificationService.Send(...);  // ❌ Entity dipende da servizi
    _statsService.Update(...);       // ❌ Entity conosce troppo
    _logger.Log(...);                // ❌ Accoppiamento forte
    return task;
}
```

**Problemi:**
- Viola **SRP** - l'entity ha troppe responsabilità
- Viola **DIP** - l'entity dipende da implementazioni concrete

## La Soluzione

L'entity **registra** che qualcosa è successo. Non sa chi ascolterà.

```csharp
public class TaskItem
{
    private List<IDomainEvent> _domainEvents = new();

    public IReadOnlyList<IDomainEvent> DomainEvents => _domainEvents;

    private TaskItem(...)
    {
        // Costruzione...
        _domainEvents.Add(new TaskCreatedEvent(this.Id, this.Title));
    }

    public void ClearDomainEvents() => _domainEvents.Clear();
}
```

## Flusso Completo

```
1. Handler chiama factory/costruttore TaskItem
2. TaskItem registra TaskCreatedEvent (nella sua lista interna)
3. Handler salva TaskItem nel repository
4. Handler (o UnitOfWork) legge DomainEvents
5. Dispatcher invia eventi a tutti gli handler registrati
6. Handler pulisce gli eventi (ClearDomainEvents)
```

**Importante:** Gli eventi vengono dispatchati **DOPO** il salvataggio, per garantire consistenza.

## Struttura Base

### Interface marker

```csharp
public interface IDomainEvent
{
    DateTime OccurredOn { get; }
}
```

### Evento concreto

```csharp
public class TaskCreatedEvent : IDomainEvent
{
    public Guid TaskId { get; }
    public string Title { get; }
    public DateTime OccurredOn { get; }

    public TaskCreatedEvent(Guid taskId, string title)
    {
        TaskId = taskId;
        Title = title;
        OccurredOn = DateTime.UtcNow;
    }
}
```

### Entity con supporto eventi

```csharp
public abstract class Entity
{
    private List<IDomainEvent> _domainEvents = new();

    public IReadOnlyList<IDomainEvent> DomainEvents => _domainEvents;

    protected void AddDomainEvent(IDomainEvent domainEvent)
    {
        _domainEvents.Add(domainEvent);
    }

    public void ClearDomainEvents() => _domainEvents.Clear();
}
```

## Quando usarlo

| Situazione | Usa Domain Events |
|------------|-------------------|
| Azioni post-creazione/modifica | ✅ |
| Notificare altri bounded context | ✅ |
| Decoupling tra entity e servizi | ✅ |
| Audit trail / logging | ✅ |

## Quando NON usarlo

| Situazione | Alternativa |
|------------|-------------|
| Validazione input | Eccezioni |
| Logica sincrona semplice | Metodo diretto |
| Over-engineering per CRUD banale | Keep it simple |

## Domande dalla Sessione

### D: Perché l'entity NON può chiamare _notificationService.Send()?
**R:** Perché viola SRP (troppe responsabilità) e DIP (dipendenza da implementazioni concrete). L'entity deve solo occuparsi del suo stato.

### D: L'entity dispatcha o registra l'evento?
**R:** Solo registra (aggiunge alla lista). L'Application Layer/Handler dispatcha dopo il salvataggio.

### D: Quanti handler per evento?
**R:** Qualsiasi numero: 0, 1, o N. È publish-subscribe.

## Collegamenti

- [[entity]] - Le entity registrano eventi
- [[application-layer]] - Dove vengono dispatchati
- [[mediator-pattern]] - MediatR per gestire dispatch

## Quiz

### Q1: Dipendenze nell'Entity
Perché l'entity non può avere dipendenze come `INotificationService`?

<details>
<summary>Risposta</summary>

Viola SRP (l'entity avrebbe responsabilità di notifica) e DIP (dipenderebbe da implementazioni concrete). L'entity deve essere pura, senza dipendenze esterne.

</details>

### Q2: Quando dispatchare?
Perché gli eventi vengono dispatchati DOPO SaveChanges e non prima?

<details>
<summary>Risposta</summary>

Per garantire consistenza. Se dispatchi prima e il salvataggio fallisce, hai già notificato qualcosa che non è successo. Dispatch dopo = l'evento è realmente avvenuto.

</details>

### Q3: Handler multipli
Se `TaskCreatedEvent` ha 3 handler registrati, quanti vengono eseguiti?

<details>
<summary>Risposta</summary>

Tutti e 3. È un pattern publish-subscribe: tutti gli handler registrati per quell'evento ricevono la notifica.

</details>

---

## Risorse per Approfondire

- **[Martin Fowler - Domain Events](https://martinfowler.com/eaaDev/DomainEvent.html)** - Definizione originale
- **[Microsoft - Domain Events](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation)** - Implementazione .NET
- **[Jimmy Bogard - A Better Domain Events Pattern](https://lostechies.com/jimmybogard/2014/05/13/a-better-domain-events-pattern/)** - Pattern migliorato

---

*Creato durante: Senior P1 Week 1 - Task Manager*
