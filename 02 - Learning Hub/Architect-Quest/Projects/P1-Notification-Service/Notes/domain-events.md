---
tags:
  - p1
  - patterns
  - domain
  - event-driven
  - from/week-02
  - status/learning
aliases:
  - Domain Events
  - Eventi di Dominio
  - Event-driven Domain
created: 2026-02-11
source: "Sessione Week 2 - P1 Notification Service"
---

# Domain Events

> **One-liner:** Un Domain Event rappresenta un fatto significativo già accaduto nel dominio, permettendo di comunicare cambiamenti senza accoppiamento diretto tra componenti.

---

## Cos'è

Un **Domain Event** è un oggetto immutabile che cattura qualcosa di importante che è successo nel dominio. È sempre espresso al **passato** (è un fatto compiuto):

- `NotificationScheduledEvent` - "Una notifica è stata schedulata"
- `NotificationSentEvent` - "Una notifica è stata inviata"
- `NotificationFailedEvent` - "Una notifica è fallita"

### Caratteristiche Fondamentali

| Caratteristica | Spiegazione |
|----------------|-------------|
| **Immutabile** | Una volta creato, non cambia mai |
| **Passato** | Nome al passato: "Sent", "Failed", non "Send" |
| **Contiene dati** | Tutto il necessario per capire cosa è successo |
| **Generato dal Domain** | L'entity decide QUANDO creare l'evento |
| **Dispatched dall'Application** | L'entity NON chiama handlers direttamente |

### Architettura del Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│  DOMAIN LAYER                                                   │
│  ┌──────────────┐      ┌──────────────────┐                    │
│  │  Entity      │ ───► │  Domain Event    │  (raccoglie)       │
│  │  Notification│      │  "È successo X"  │                    │
│  └──────────────┘      └──────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼  (dopo SaveChanges)
┌─────────────────────────────────────────────────────────────────┐
│  APPLICATION LAYER                                              │
│  ┌──────────────────┐     ┌──────────────────┐                 │
│  │  Event Dispatcher│ ──► │  Event Handlers  │                 │
│  └──────────────────┘     │  - UpdateStats   │                 │
│                           │  - SendWebhook   │                 │
│                           │  - WriteAuditLog │                 │
│                           └──────────────────┘                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quando Usarlo

| Scenario | Esempio |
|----------|---------|
| **Side effects dopo un'azione** | Dopo `Send()` → aggiorna statistiche |
| **Notificare altri bounded contexts** | `NotificationSent` → Billing aggiorna consumo |
| **Audit trail** | Ogni cambio di stato → log immutabile |
| **Event sourcing** (futuro) | Ricostruire stato da eventi |
| **Decoupling** | Domain non sa chi ascolta |

---

## Quando NON Usarlo

| Scenario | Perché |
|----------|--------|
| **Query semplici** | Overkill, usa metodo diretto |
| **Validazione** | Lancia eccezione, non evento |
| **Comunicazione sincrona necessaria** | Eventi sono (spesso) asincroni |
| **Tutto** | Non ogni metodo ha bisogno di evento! |

**Regola pratica:** Se nessuno deve reagire a qualcosa che è successo, non serve un evento.

---

## Esempio

### Il Problema (senza eventi)

```csharp
public void Send()
{
    Status = NotificationStatus.Sent;
    SentAt = DateTime.UtcNow;

    // E ora? Come aggiorniamo statistiche, webhook, audit?
    // Non possiamo chiamare servizi esterni dal Domain!
}
```

### La Soluzione (con eventi)

```csharp
// 1. L'EVENTO (Domain Layer)
public record NotificationSentEvent(
    Guid NotificationId,
    NotificationChannel Channel,
    DateTime SentAt
) : IDomainEvent
{
    public DateTime OccurredOn { get; } = DateTime.UtcNow;
}

// 2. ENTITY BASE con supporto eventi (Domain Layer)
public abstract class Entity
{
    private readonly List<IDomainEvent> _domainEvents = new();

    public IReadOnlyList<IDomainEvent> DomainEvents => _domainEvents.AsReadOnly();

    protected void AddDomainEvent(IDomainEvent domainEvent)
    {
        _domainEvents.Add(domainEvent);
    }

    public void ClearDomainEvents() => _domainEvents.Clear();
}

// 3. NOTIFICATION usa gli eventi (Domain Layer)
public class Notification : Entity
{
    public void Send()
    {
        if (Status != NotificationStatus.Pending)
            throw new InvalidOperationException("Can only send pending notifications");

        Status = NotificationStatus.Sent;
        SentAt = DateTime.UtcNow;

        // Registra evento (NON lo dispatcha!)
        AddDomainEvent(new NotificationSentEvent(
            NotificationId: Id,
            Channel: Channel,
            SentAt: SentAt.Value
        ));
    }
}

// 4. HANDLER (Application Layer)
public class StatsHandler : INotificationHandler<NotificationSentEvent>
{
    public async Task Handle(NotificationSentEvent evt, CancellationToken ct)
    {
        await _stats.IncrementSentCountAsync(evt.Channel);
    }
}
```

### Flusso Completo

```
1. UseCase: notification.Send()
              │
              ▼
2. Entity: Status = Sent
           _domainEvents.Add(NotificationSentEvent)
           [evento REGISTRATO, non dispatched]
              │
              ▼
3. UseCase: await _repository.SaveAsync(notification)
              │
              ▼
4. DbContext: await base.SaveChangesAsync()  ◄── DB salvato!
              │
              ▼
5. DbContext: foreach event → dispatcher.Dispatch(event)
              │
              ├──► StatsHandler.Handle()      → incrementa contatore
              ├──► WebhookHandler.Handle()    → chiama webhook
              └──► AuditHandler.Handle()      → scrive log
              │
              ▼
6. DbContext: entity.ClearDomainEvents()  ◄── pulisce la lista
```

### Perché DOPO SaveChanges?

```
❌ SBAGLIATO: Dispatch PRIMA di SaveChanges
─────────────────────────────────────────
1. notification.Send()         → evento registrato
2. dispatcher.Dispatch(event)  → handler scrive su altro sistema
3. SaveChanges() FALLISCE!     → DB rollback
4. PROBLEMA: altro sistema ha dati inconsistenti! 💥

✅ CORRETTO: Dispatch DOPO SaveChanges
─────────────────────────────────────────
1. notification.Send()         → evento registrato
2. SaveChanges() OK            → DB persistito ✅
3. dispatcher.Dispatch(event)  → handler scrive su altro sistema
4. Tutto coerente! ✅
```

---

## Come Funziona il Dispatcher

Il dispatcher mantiene un **Registry** (un `Dictionary<TipoEvento, List<Handler>>`):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ALL'AVVIO DELL'APP (Program.cs)                                            │
│                                                                             │
│                         ┌─────────────────────────────────────┐             │
│                         │          REGISTRY                   │             │
│                         ├─────────────────────────────────────┤             │
│                         │                                     │             │
│                         │  NotificationSentEvent ──────────►  │             │
│                         │      ├─► StatsHandler               │             │
│                         │      ├─► WebhookHandler             │             │
│                         │      └─► AuditHandler               │             │
│                         │                                     │             │
│                         │  NotificationFailedEvent ────────►  │             │
│                         │      ├─► AlertHandler               │             │
│                         │      └─► RetryHandler               │             │
│                         │                                     │             │
│                         └─────────────────────────────────────┘             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**MediatR** è essenzialmente questo Dictionary **con steroidi**:
- Auto-discovery degli handler (scansiona l'assembly)
- Integrazione col DI Container
- Pipeline con Behaviors (logging, validation)
- Gestione async built-in

```
TL;DR:
Dictionary<Type, Func<>>  =  MediatR senza le feature extra
MediatR = Dictionary + DI integration + auto-discovery + pipeline
```

---

## Collegamenti

- [[domain-model-patterns]] - Entity vs Value Object
- [[clean-architecture]] - Perché il Domain non può chiamare servizi esterni
- [[entities-and-clean-architecture]] - Come strutturare le Entity

---

## Domande dalla Sessione

### D: Perché l'evento si chiama `NotificationSentEvent` e non `SendNotificationEvent`?

**R:** Perché è qualcosa di **già successo**. È al passato. Un Domain Event rappresenta un fatto compiuto, non un comando da eseguire. I comandi sono imperativi ("Send!"), gli eventi sono al passato ("Sent").

---

### D: L'entity Notification può chiamare direttamente `_emailService.Send()`?

**R:** **No!** Perché:
- Si perde il decoupling
- Il Domain Layer dipenderebbe dall'Infrastructure
- Viola OCP (ogni nuovo servizio = modifica all'entity)
- Il Domain deve essere puro, senza dipendenze esterne

---

### D: Chi è responsabile di gestire l'evento (chiamare gli handler)?

**R:** L'**Application Layer** (o Infrastructure). L'entity registra solo l'evento in una lista interna. Dopo `SaveChanges()`, il dispatcher legge quella lista e chiama gli handler appropriati.

---

### D: Come fa l'handler giusto ad essere chiamato? Dove è specificata l'associazione?

**R:** Il Dispatcher mantiene un **Registry** (essenzialmente un `Dictionary<TipoEvento, List<Handler>>`). All'avvio dell'app, gli handler vengono registrati. Quando arriva un evento, il dispatcher:
1. Guarda il tipo dell'evento
2. Cerca nel registry tutti gli handler per quel tipo
3. Chiama `Handle()` su ognuno

MediatR fa esattamente questo, ma con auto-discovery via reflection e integrazione col DI Container.

---

### D: Quindi MediatR è un Dictionary con steroidi?

**R:** Esatto! MediatR è un `Dictionary<TipoEvento, List<Handler>>` con feature aggiuntive:
- Registrazione automatica (scansiona assembly)
- Integrazione DI Container
- Pipeline behaviors
- Lifecycle management

Concettualmente fa la stessa cosa che faremmo a mano, ma meglio.

---

## Quiz

### Q1: Perché dispatchiamo eventi DOPO SaveChanges?

<details>
<summary>Risposta</summary>

Perché se dispatchiamo PRIMA e poi `SaveChanges()` fallisce, abbiamo dati inconsistenti: gli handler hanno già eseguito side effects (es: inviato email, aggiornato altri sistemi) ma il DB ha fatto rollback.

Dispatchando DOPO, siamo sicuri che i dati sono persistiti prima di notificare altri sistemi.

</details>

---

### Q2: Questo codice è corretto?

```csharp
public class Notification : Entity
{
    private readonly IStatsService _stats;

    public void Send()
    {
        Status = NotificationStatus.Sent;
        _stats.IncrementSentCount();  // ◄── Qui
    }
}
```

<details>
<summary>Risposta</summary>

**No!** L'Entity nel Domain Layer non deve avere dipendenze da servizi esterni (`IStatsService`).

Il modo corretto è generare un `NotificationSentEvent` e lasciare che un handler nell'Application Layer aggiorni le statistiche.

</details>

---

### Q3: Quanti handler possono ascoltare lo stesso evento?

<details>
<summary>Risposta</summary>

**Quanti ne vuoi!** Il pattern è 1:N (uno a molti). Un `NotificationSentEvent` può avere:
- `StatsHandler` → aggiorna contatori
- `WebhookHandler` → chiama API esterna
- `AuditHandler` → scrive log

Ogni handler è indipendente e non sa degli altri.

</details>

---

### Q4: L'entity può dispatchare direttamente l'evento?

```csharp
public void Send()
{
    Status = NotificationStatus.Sent;
    _dispatcher.Dispatch(new NotificationSentEvent(...));  // ◄── Corretto?
}
```

<details>
<summary>Risposta</summary>

**No!** L'entity:
1. Non deve avere dipendenze (`_dispatcher`)
2. Non sa quando è il momento giusto per dispatchare (prima o dopo SaveChanges?)

L'entity **registra** l'evento in una lista interna. Qualcun altro (Repository, DbContext, Unit of Work) legge quella lista e dispatcha al momento giusto.

</details>

---

### Q5: Quale di questi NON è un buon caso d'uso per Domain Events?

A) Aggiornare statistiche dopo invio notifica
B) Validare che l'email sia nel formato corretto
C) Scrivere audit log di ogni cambio di stato
D) Notificare un sistema esterno di billing

<details>
<summary>Risposta</summary>

**B) Validare che l'email sia nel formato corretto**

La validazione deve lanciare un'eccezione, non un evento. Se l'email non è valida, l'operazione deve fallire immediatamente, non generare un "EmailInvalidEvent".

Gli eventi sono per side effects dopo che qualcosa è successo con successo.

</details>

---

### Q6: Cos'è MediatR in relazione ai Domain Events?

<details>
<summary>Risposta</summary>

MediatR è essenzialmente un `Dictionary<TipoEvento, List<Handler>>` con feature aggiuntive:
- Auto-discovery degli handler (scansiona l'assembly)
- Integrazione col DI Container
- Pipeline con Behaviors (logging, validation)
- Gestione async built-in
- Facile da testare/mockare

Concettualmente fa la stessa cosa che faremmo a mano, ma meglio.

</details>

---

## Risorse per Approfondire

- **[Martin Fowler - Domain Event](https://martinfowler.com/eaaDev/DomainEvent.html)** - L'articolo originale che ha definito il pattern. Breve ma fondamentale.

- **[Microsoft - Domain Events Design and Implementation](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation)** - Guida ufficiale Microsoft con implementazione completa in .NET. Include esempi con MediatR.

- **[Jimmy Bogard - A better domain events pattern](https://lostechies.com/jimmybogard/2014/05/13/a-better-domain-events-pattern/)** - Dal creatore di MediatR. Spiega l'evoluzione del pattern e le best practices.

- **[Udi Dahan - Domain Events Salvation](https://udidahan.com/2009/06/14/domain-events-salvation/)** - Articolo fondamentale che ha influenzato l'approccio moderno ai domain events.

- **Libro: "Implementing Domain-Driven Design" - Vaughn Vernon, Cap. 8** - Trattazione completa con esempi enterprise. Il capitolo sui Domain Events è uno dei migliori.

- **[MediatR Wiki](https://github.com/jbogard/MediatR/wiki)** - Documentazione ufficiale di MediatR con esempi di notifiche (domain events).

---

*Creata: 2026-02-11*
*Argomenti: Domain Events, Event-driven architecture, MediatR, Dispatcher pattern, Pub/Sub*
