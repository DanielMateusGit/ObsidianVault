---
tags:
  - p1
  - architecture
  - ddd
  - domain-model
  - from/week-02
  - status/learned
aliases:
  - Rich Domain Model
  - Anemic Domain Model
  - Domain Model
created: 2026-02-11
source: "Sessione Week 2 - P1 Notification Service"
---

# Rich vs Anemic Domain Model

> **One-liner:** Nel Rich Domain Model le entità contengono dati + comportamento; nell'Anemic sono solo contenitori di dati con logica sparsa nei Service.

---

## Cos'è

Due approcci opposti per organizzare la logica di business:

### Anemic Domain Model (Anti-pattern)

```csharp
// Entity = solo dati, nessun comportamento
public class Notification
{
    public Guid Id { get; set; }
    public string Recipient { get; set; }
    public string Status { get; set; }
}

// Logica FUORI dall'entity, nei Service
public class NotificationService
{
    public void Send(Notification n)
    {
        if (n.Status != "Pending") throw ...;
        n.Status = "Sent";  // Chiunque può farlo!
        n.SentAt = DateTime.UtcNow;
    }
}
```

**Problemi:**
- Entity è un "sacco di dati"
- Logica sparsa in molti Service
- Validazione duplicata ovunque
- Stati invalidi possibili (`n.Status = "BananaState"`)

### Rich Domain Model (Best Practice)

```csharp
// Entity = dati + comportamento + regole
public class Notification : Entity
{
    public NotificationStatus Status { get; private set; }  // private set!

    public void MarkAsSent()
    {
        if (Status != NotificationStatus.Pending)
            throw new InvalidOperationException("...");

        Status = NotificationStatus.Sent;
        AddDomainEvent(new NotificationSentEvent(...));
    }
}
```

**Vantaggi:**
- Entity protegge i suoi invarianti
- Logica centralizzata ("dove sta la regola?" → nell'entity)
- Impossibile creare stati invalidi
- Self-documenting: `MarkAsSent()` > `Status = "Sent"`

---

## Quando Usarlo

| Situazione | Approccio |
|------------|-----------|
| Dominio con regole di business complesse | ✅ Rich Domain Model |
| Cicli di vita delle entità (stati, transizioni) | ✅ Rich Domain Model |
| Sistema che deve durare anni | ✅ Rich Domain Model |
| CRUD semplice senza logica | ⚠️ Anemic può bastare |
| Prototipo veloce usa-e-getta | ⚠️ Anemic può bastare |

**Nel Notification Service:** Rich Domain Model perché abbiamo:
- Ciclo di vita: Pending → Sent/Failed/RetryScheduled
- Regole: "solo Pending può diventare Sent"
- Retry logic, template validation, multi-channel

---

## Quando NON Usarlo

**Non usare Rich Domain Model se:**
- È un CRUD banale senza logica (es. tabella di lookup)
- Prototipo che butterai via
- Performance critica e l'overhead è misurabile

**Ma attenzione:** La maggior parte dei "CRUD semplici" diventano complessi. Meglio partire Rich.

---

## Esempio

### Il Nostro Notification (Rich)

```csharp
public class Notification : Entity
{
    public Recipient Recipient { get; private set; }      // Value Object
    public NotificationStatus Status { get; private set; } // Enum
    public DateTime? SentAt { get; private set; }

    private Notification() { }  // Solo EF Core

    // Factory method - unico modo per creare
    public static Notification Schedule(
        Recipient recipient,
        NotificationChannel channel,
        string content)
    {
        var notification = new Notification
        {
            Id = Guid.NewGuid(),
            Recipient = recipient,
            Status = NotificationStatus.Pending,
            // ...
        };

        notification.AddDomainEvent(new NotificationScheduledEvent(...));
        return notification;
    }

    // Metodo con nome significativo
    public void MarkAsSent()
    {
        // Regola di business DENTRO l'entity
        if (Status != NotificationStatus.Pending)
            throw new InvalidOperationException(
                "Can only send pending notifications");

        Status = NotificationStatus.Sent;
        SentAt = DateTime.UtcNow;

        AddDomainEvent(new NotificationSentEvent(Id, SentAt.Value));
    }

    public void MarkAsFailed(string reason, bool canRetry)
    {
        if (Status != NotificationStatus.Pending)
            throw new InvalidOperationException(
                "Can only fail pending notifications");

        Status = canRetry
            ? NotificationStatus.RetryScheduled
            : NotificationStatus.Failed;

        AddDomainEvent(new NotificationFailedEvent(Id, reason, canRetry));
    }
}
```

**Punti chiave:**
1. `private set` → stato modificabile solo dall'interno
2. Factory method `Schedule()` → costruzione controllata
3. Metodi `MarkAsSent()`, `MarkAsFailed()` → nomi che esprimono intent
4. Domain Events → side effects espliciti

---

## Collegamenti

- [[domain-events]] - Come comunicare i cambiamenti
- [[value-objects]] - Garantire validità dei dati
- [[clean-architecture]] - Architettura che supporta Rich Domain Model
- [[adr-architecture-decision-records]] - ADR-002 documenta questa scelta

---

## Domande dalla Sessione

### D: Dove sta la logica per marcare una notifica come "Sent"?

**R:** Dentro il metodo `MarkAsSent()` della Notification entity. Non in un Service esterno.

---

### D: Un junior può fare `notification.Status = "Sent"` nel nostro modello?

**R:** No! Il setter è `private`. L'unico modo è chiamare `MarkAsSent()`, che applica le regole di business.

---

### D: Perché Fowler chiama Anemic un "anti-pattern"?

**R:** Perché viola il principio OOP fondamentale: oggetti = dati + comportamento. Nell'Anemic hai dati da una parte e comportamento dall'altra, perdendo i vantaggi dell'incapsulamento.

---

## Quiz

### Q1: Qual è il problema principale dell'Anemic Domain Model?

<details>
<summary>Risposta</summary>

**Logica sparsa e responsabilità confuse.**

Quando l'entity è solo un contenitore di dati:
- Più Service possono modificare lo stato
- Difficile capire "chi è responsabile di cosa"
- Validazione duplicata in più punti
- Stati invalidi possibili

</details>

---

### Q2: Come il Rich Domain Model previene stati invalidi?

<details>
<summary>Risposta</summary>

**Tre meccanismi:**

1. **Private setters** → stato modificabile solo dall'interno
2. **Factory methods** → costruzione controllata
3. **Metodi con validazione** → `MarkAsSent()` verifica le precondizioni

Esempio: non puoi fare `Status = "Banana"` perché:
- `Status` ha `private set`
- È un enum `NotificationStatus`, non una stringa

</details>

---

### Q3: Un'entity può avere dipendenze iniettate (es. IEmailService)?

<details>
<summary>Risposta</summary>

**No!** Le entity devono essere **pure** - solo dati e logica di business.

Perché:
- Entity vengono ricostruite da EF Core (no costruttore con DI)
- Entity devono essere testabili senza mock
- Side effects vanno nei Domain Event handlers, non nell'entity

**Invece:** L'entity genera un Domain Event, un handler esterno usa IEmailService.

</details>

---

### Q4: Quando è accettabile usare Anemic Domain Model?

<details>
<summary>Risposta</summary>

**Casi limitati:**

- CRUD puro senza logica di business
- Tabelle di lookup/configurazione
- Prototipi usa-e-getta
- DTO per trasferimento dati (ma non sono entity!)

**Attenzione:** La maggior parte dei "CRUD semplici" evolve in dominio complesso. Meglio partire Rich.

</details>

---

## Risorse per Approfondire

- **[AnemicDomainModel - Martin Fowler](https://martinfowler.com/bliki/AnemicDomainModel.html)** - L'articolo originale che spiega perché è un anti-pattern. Essenziale.

- **[Domain-Driven Design - Eric Evans](https://www.domainlanguage.com/ddd/)** - Il libro che ha definito Rich Domain Model. Capitoli 5-6.

- **[Implementing DDD - Vaughn Vernon](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577)** - Implementazione pratica con esempi di codice.

- **[ADR-002: Rich Domain Model](../../../Projects/notification-service/docs/adr/ADR-002-rich-domain-model.md)** - La nostra decisione documentata.

---

*Creata: 2026-02-11*
*Argomenti: Rich Domain Model, Anemic Domain Model, DDD, Domain-Driven Design*
