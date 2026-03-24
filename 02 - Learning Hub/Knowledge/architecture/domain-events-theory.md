---
tags:
  - architecture
  - from/article
  - status/learned
  - project/p1-notification
aliases:
  - Domain Events
  - Eventi di Dominio
created: 2026-02-13
updated: 2026-02-13
source: "Martin Fowler, Microsoft Docs, Jimmy Bogard, Milan Jovanović"
---

# Domain Events - Teoria e Pattern

> **One-liner:** Un Domain Event è un record immutabile di qualcosa di significativo accaduto nel dominio.

## Cos'è

Un Domain Event cattura il fatto che **qualcosa è successo** nel dominio. È un pattern che permette di:

1. **Registrare** cosa è accaduto (audit, history)
2. **Reagire** a cambiamenti di stato (side effects)
3. **Disaccoppiare** componenti (loose coupling)

### Struttura di un Domain Event

```
Input Stream → Domain Event → Persistent Log → Event Processor
```

### Tipi di Dati negli Eventi

| Tipo | Descrizione | Caratteristiche |
|------|-------------|-----------------|
| **Source Data** | Cosa è successo | Immutabile, il "fatto" |
| **Processing Data** | Cosa è stato fatto in risposta | Generato dagli handler |
| **Cache Data** | Dati derivati per performance | Opzionale, con complessità |

### Timestamp Importanti

Ogni evento dovrebbe avere:
- **OccurredAt**: Quando l'evento è realmente accaduto
- **NoticedAt**: Quando il sistema ha rilevato l'evento

Utile per sistemi distribuiti dove c'è latenza tra occorrenza e rilevamento.

## Domain Events vs Integration Events

| Aspetto | Domain Event | Integration Event |
|---------|--------------|-------------------|
| **Scope** | Singolo bounded context | Cross microservizi |
| **Trasporto** | In-memory (MediatR) | Message broker (RabbitMQ) |
| **Consistenza** | Stesso transaction | Eventually consistent |
| **Esempio** | `NotificationSentEvent` | `NotificationSentIntegrationEvent` |

```csharp
// Domain Event - interno, stesso processo
public record NotificationSentEvent(Guid NotificationId, DateTime SentAt)
    : IDomainEvent;

// Integration Event - esterno, via message broker
public record NotificationSentIntegrationEvent(
    Guid NotificationId,
    string Channel,
    DateTime SentAt);
```

## Dispatch: Static vs Deferred

### Static Dispatch
```csharp
// ❌ Dispatch immediato - problematico
notification.MarkAsSent();  // Genera e dispatcha SUBITO
// Rischio: stato inconsistente se qualcosa fallisce dopo
```

### Deferred Dispatch
```csharp
// ✅ Accumula, poi dispatcha in momento controllato
notification.MarkAsSent();           // Solo registra l'evento
// ... altre operazioni ...
await SaveChangesAsync();            // Persisti
await DispatchEventsAsync();         // Ora dispatcha
```

## Quando Dispatchare (Il Grande Dibattito)

### Approccio 1: Prima del Commit (Jimmy Bogard)
```csharp
// Handler possono modificare lo stato
await DispatchEventsAsync();  // Handler lavorano su stato RAM
await SaveChangesAsync();     // Tutto in un transaction
// Se fallisce → rollback completo
```

**Pro:** Handler possono partecipare alla stessa transaction
**Contro:** Se handler fallisce, rollback di tutto

### Approccio 2: Dopo il Commit (Comune)
```csharp
await SaveChangesAsync();     // Prima persisti
await DispatchEventsAsync();  // Poi notifica
// Certezza che l'evento corrisponde a dato persistito
```

**Pro:** Notifichi solo eventi "reali" (persistiti)
**Contro:** Handler non possono modificare stessa transaction

> **Nostra scelta in P1:** Dopo SaveChanges - per garantire consistenza.

## Event Chaining

Gli eventi possono scatenare altri eventi:

```
EventX → HandlerX → modifica stato → EventY → HandlerY → ...
```

Questo è il pattern di **eventual consistency**: le reazioni si propagano a cascata.

## Correzione Eventi (Retroactive Events)

Gli eventi sono **immutabili**. Per correggere:

```csharp
// ❌ Non puoi modificare l'evento originale
originalEvent.Amount = 100;  // VIETATO

// ✅ Crea un evento correttivo
new AmountCorrectedEvent(originalEventId, oldAmount: 50, newAmount: 100);
```

## Subtypes vs Enum

Per eventi simili, preferire enum:

```csharp
// ❌ Troppi tipi
class ExcelDocumentEditedEvent { }
class WordDocumentEditedEvent { }
class MarkdownDocumentEditedEvent { }

// ✅ Un tipo + enum
class DocumentEditedEvent
{
    public DocumentType Type { get; }  // Excel, Word, Markdown
}
```

## Quando usarlo

- Hai side effects da eseguire dopo un'azione (email, notifiche, audit)
- Vuoi disaccoppiare chi genera l'evento da chi reagisce
- Hai bisogno di un audit log di cosa è successo
- Più componenti devono reagire allo stesso cambiamento

## Quando NON usarlo

- Operazioni semplici senza side effects
- Quando la complessità non giustifica il beneficio
- Per comunicazione sincrona stretta (meglio chiamata diretta)

## Implementazione con MediatR

```csharp
// 1. Evento implementa INotification
public record NotificationSentEvent(Guid Id, DateTime SentAt)
    : INotification;

// 2. Entity accumula eventi
public abstract class Entity
{
    private readonly List<IDomainEvent> _domainEvents = new();

    public IReadOnlyCollection<IDomainEvent> DomainEvents
        => _domainEvents.AsReadOnly();  // Protetto!

    protected void Raise(IDomainEvent @event)
        => _domainEvents.Add(@event);

    public void ClearDomainEvents()
        => _domainEvents.Clear();
}

// 3. Handler reagisce
public class NotificationSentHandler
    : INotificationHandler<NotificationSentEvent>
{
    public Task Handle(NotificationSentEvent evt, CancellationToken ct)
    {
        // Aggiorna stats, invia conferma, etc.
    }
}
```

## Collegamenti

- [[../solid/single-responsibility-principle|SRP]] - Eventi separano responsabilità
- [[../solid/open-closed-principle|OCP]] - Nuovi handler senza modificare entity
- [[../solid/dependency-inversion-principle|DIP]] - Entity non dipende da handler
- [[cqrs-pattern]] — Events collegano Commands a side effects
- [[mediatr-pipeline-behaviors]] — MediatR dispatcha gli eventi
- [[unit-of-work-pattern]] — Dispatch DOPO SaveChanges (UoW)
- [[repository-pattern]] — Repository non dispatcha eventi, lo fa l'infrastruttura

## Quiz

### Q1: Perché gli eventi sono immutabili?

Come correggi un evento sbagliato se non puoi modificarlo?

**Mia risposta:** Con retroactive events - crei un nuovo evento che corregge quello precedente

✅ **Corretto** - Gli eventi rappresentano fatti storici. Non puoi cambiare il passato, ma puoi registrare una correzione.

---

### Q2: Dispatch prima o dopo SaveChanges?

Qual è la differenza pratica tra le due strategie?

- A) Prima: handler in stesso transaction, rollback totale se fallisce
- B) Dopo: certezza che evento corrisponde a dato persistito
- C) Non c'è differenza
- D) Entrambe A e B sono corrette

**Mia risposta:** D

✅ **Corretto** - Sono due approcci validi con trade-off diversi. Noi usiamo "dopo" per garantire consistenza.

---

### Q3: Quando preferire enum a sottotipi?

Hai `OrderCreatedEvent`, `OrderUpdatedEvent`, `OrderCancelledEvent`. Li unifichi con enum?

**Mia risposta:** No, sono eventi semanticamente diversi con dati diversi. L'enum è per eventi simili con stessa struttura (es. DocumentEdited per Excel/Word/MD).

✅ **Corretto** - L'enum è per varianti dello stesso evento. Qui sono eventi distinti con significati e payload diversi.

---

## Ti è piaciuto parlare di Domain Events? Allora impazzirai per:

- **[Domain Events vs Integration Events vs Application Events](https://www.youtube.com/watch?v=dmYP-9jhfGY)** - Derek Comartin spiega le 3 categorie con esempi pratici
- **[Outbox Pattern](https://microservices.io/patterns/data/transactional-outbox.html)** - Come garantire che eventi e dati siano consistenti (lo useremo con RabbitMQ!)

---

*Fonti: Martin Fowler, Microsoft Docs, Jimmy Bogard, Milan Jovanović*
