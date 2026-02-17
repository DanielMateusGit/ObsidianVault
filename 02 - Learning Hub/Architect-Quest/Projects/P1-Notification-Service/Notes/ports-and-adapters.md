---
tags:
  - p1
  - architecture
  - clean-architecture
  - from/week-03
  - status/learning
aliases:
  - Hexagonal Architecture
  - Ports and Adapters
  - Porte e Adattatori
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# Ports & Adapters (Hexagonal Architecture)

> **One-liner:** Pattern architetturale che isola la business logic dal mondo esterno attraverso interfacce (Ports) definite dall'Application e implementazioni concrete (Adapters) nell'Infrastructure.

## Cos'è

**Ports & Adapters** (anche chiamata Hexagonal Architecture, coniata da Alistair Cockburn nel 2005) è un pattern che separa:

- **Port (Interfaccia):** "Cosa voglio fare" - contratto astratto definito da chi ha bisogno del servizio
- **Adapter (Implementazione):** "Come lo faccio" - implementazione concreta con dettagli tecnici

### Il Problema che Risolve

```csharp
// ❌ SBAGLIATO: Dipendenza diretta da Infrastructure
public class ScheduleNotificationHandler
{
    private readonly PostgresNotificationRepository _repository;

    public async Task<Guid> Handle(ScheduleNotificationCommand command)
    {
        await _repository.AddAsync(notification);  // Legato a PostgreSQL!
    }
}
```

Problemi:
1. **Non testabile** senza database reale
2. **Non sostituibile** - cambiare DB richiede modificare l'handler
3. **Viola Dependency Rule** - Application conosce Infrastructure

### La Soluzione

```csharp
// ✅ CORRETTO: Dipendenza da astrazione
public class ScheduleNotificationHandler
{
    private readonly INotificationRepository _repository;  // PORT

    public async Task<Guid> Handle(ScheduleNotificationCommand command)
    {
        await _repository.AddAsync(notification);  // Non sa se è Postgres, Mongo, o mock!
    }
}
```

### Dove Vivono Port e Adapter

```
┌─────────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                         │
│                                                                  │
│  ┌─────────────────┐         ┌─────────────────────────────┐   │
│  │     Handler     │ ──────► │  INotificationRepository    │   │
│  │  (Use Case)     │         │        (PORT)               │   │
│  └─────────────────┘         └──────────────▲──────────────┘   │
│                                             │                   │
└─────────────────────────────────────────────┼───────────────────┘
                                              │ implements
┌─────────────────────────────────────────────┼───────────────────┐
│                     INFRASTRUCTURE LAYER    │                   │
│                                                                  │
│                              ┌──────────────┴──────────────┐   │
│                              │  PostgresNotificationRepo   │   │
│                              │        (ADAPTER)            │   │
│                              └─────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**La freccia delle dipendenze punta VERSO L'INTERNO** (verso Application).

## Perché l'interfaccia sta nell'Application?

Questa è la domanda chiave. L'intuizione sbagliata è: "L'interfaccia descrive il repository, il repository sta in Infrastructure, quindi l'interfaccia va in Infrastructure".

**La risposta corretta:** L'interfaccia definisce **ciò di cui l'Application ha bisogno**. È l'Application che "chiede" un servizio, quindi l'interfaccia è **di proprietà dell'Application**.

| Chi | Ruolo | Dove |
|-----|-------|------|
| Application | Definisce il contratto (cosa mi serve) | Interface qui |
| Infrastructure | Implementa il contratto (come lo faccio) | Classe qui |

Questo è **Dependency Inversion Principle** in azione:
- Moduli di alto livello (Application) NON dipendono da quelli di basso livello (Infrastructure)
- Entrambi dipendono da astrazioni
- L'astrazione è **posseduta** dal modulo di alto livello

## Quando usarlo

**USA Ports & Adapters quando:**
- Vuoi testare business logic senza database/servizi esterni
- Potresti cambiare tecnologia (PostgreSQL → MongoDB, SendGrid → Mailgun)
- Vuoi rispettare Clean Architecture
- Hai team separati su Application e Infrastructure

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| Progetto piccolissimo | Overhead inutile |
| Prototipo usa-e-getta | Non vale la complessità |
| CRUD banale senza logica | Overkill |
| "Un'interfaccia per ogni classe" | Anti-pattern! |

### Anti-pattern: Interfacce Inutili

```csharp
// ❌ SBAGLIATO: Interfaccia che segue la classe
public interface IEmailFormatter { string Format(Email e); }
public class EmailFormatter : IEmailFormatter { ... }
// Se c'è UNA sola implementazione e non serve per test... perché l'interfaccia?

// ✅ CORRETTO: Interfaccia per necessità reale
public interface INotificationSender { Task SendAsync(Notification n); }
public class EmailSender : INotificationSender { ... }
public class SmsSender : INotificationSender { ... }
public class MockSender : INotificationSender { ... }  // Per test!
```

**Regola:** Crea un'interfaccia quando hai bisogno di:
1. Più implementazioni (strategia)
2. Testabilità (mock)
3. Inversione delle dipendenze tra layer

## Esempio

### Port (Application Layer)

```csharp
// Application/Interfaces/INotificationRepository.cs
namespace NotificationService.Application.Interfaces;

public interface INotificationRepository
{
    Task<Notification?> GetByIdAsync(Guid id, CancellationToken ct = default);
    Task<IReadOnlyList<Notification>> GetByStatusAsync(NotificationStatus status, CancellationToken ct = default);
    Task AddAsync(Notification notification, CancellationToken ct = default);
    Task UpdateAsync(Notification notification, CancellationToken ct = default);
}
```

### Adapter (Infrastructure Layer)

```csharp
// Infrastructure/Persistence/PostgresNotificationRepository.cs
namespace NotificationService.Infrastructure.Persistence;

public class PostgresNotificationRepository : INotificationRepository
{
    private readonly AppDbContext _context;

    public PostgresNotificationRepository(AppDbContext context)
    {
        _context = context;
    }

    public async Task<Notification?> GetByIdAsync(Guid id, CancellationToken ct = default)
    {
        return await _context.Notifications.FindAsync(new object[] { id }, ct);
    }

    public async Task AddAsync(Notification notification, CancellationToken ct = default)
    {
        await _context.Notifications.AddAsync(notification, ct);
    }

    // ... altre implementazioni
}
```

### Uso nell'Handler

```csharp
// Application/Commands/ScheduleNotificationHandler.cs
public class ScheduleNotificationHandler : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    private readonly INotificationRepository _repository;  // Dipende dal PORT
    private readonly IUnitOfWork _unitOfWork;

    public ScheduleNotificationHandler(
        INotificationRepository repository,  // Iniettato via DI
        IUnitOfWork unitOfWork)
    {
        _repository = repository;
        _unitOfWork = unitOfWork;
    }

    public async Task<Guid> Handle(ScheduleNotificationCommand command, CancellationToken ct)
    {
        var notification = new Notification(...);
        await _repository.AddAsync(notification, ct);  // Non sa quale implementazione!
        await _unitOfWork.SaveChangesAsync(ct);
        return notification.Id;
    }
}
```

## Collegamenti

- [[clean-architecture]] - I 4 layer e la Dependency Rule
- [[cqrs-and-mediatr]] - Come gli Handler usano i Ports
- [[dependency-inversion-principle]] - Il principio SOLID dietro questo pattern

## Domande dalla Sessione

### D: Dove deve stare IUserRepository se la classe PostgresUserRepository sta in Infrastructure?
**R:** L'interfaccia `IUserRepository` deve stare in **Application**, non in Infrastructure. L'interfaccia definisce "di cosa ha bisogno" l'Application, l'Infrastructure definisce "come lo implementa". Il contratto appartiene a chi lo richiede.

### D: Un collega dice "Creo un'interfaccia per ogni classe, così rispetto DIP". Ha ragione?
**R:** No. La Dependency Inversion non significa "tante interfacce". Significa che l'astrazione guida l'implementazione, non il contrario. Se crei un'interfaccia per ogni classe stai facendo il contrario: l'interfaccia segue la classe. Crea interfacce quando servono: testabilità, più implementazioni, o inversione tra layer.

### D: Perché è importante che Application "possieda" l'interfaccia?
**R:** Perché Application contiene gli Use Cases - il "cosa deve fare" l'applicazione. Gli Use Cases definiscono anche "di cosa hanno bisogno per farlo", ma in modo astratto. Infrastructure è solo l'implementazione di questo disegno. Se Infrastructure possedesse l'interfaccia, sarebbe lei a dettare il contratto e Application dipenderebbe da Infrastructure (violando la Dependency Rule).

## Quiz

### Q1: Posizionamento dell'interfaccia
Hai questo codice:
```
Infrastructure/
  Repositories/
    IOrderRepository.cs      ← Interfaccia qui
    PostgresOrderRepository.cs
```
Cosa c'è di sbagliato e come lo correggi?

<details>
<summary>Risposta</summary>

L'interfaccia `IOrderRepository` deve stare in **Application/Interfaces/**, non in Infrastructure.

```
Application/
  Interfaces/
    IOrderRepository.cs      ← Corretto!
Infrastructure/
  Repositories/
    PostgresOrderRepository.cs
```

L'interfaccia definisce ciò di cui Application ha bisogno. È Application a "possedere" il contratto.
</details>

### Q2: Interfaccia necessaria o no?
```csharp
public interface IDateFormatter
{
    string Format(DateTime date);
}

public class ItalianDateFormatter : IDateFormatter
{
    public string Format(DateTime date) => date.ToString("dd/MM/yyyy");
}
```
Questa interfaccia è utile o è overkill? Quando sarebbe giustificata?

<details>
<summary>Risposta</summary>

Dipende dal contesto:

**Overkill se:**
- C'è solo una implementazione e non cambierà mai
- Non serve per testing (è una utility pura)

**Giustificata se:**
- Più formati (ItalianDateFormatter, USDateFormatter, ISODateFormatter)
- Serve mockare nei test (improbabile per un formatter)
- È un "Port" verso un servizio esterno

In questo caso specifico, probabilmente overkill. Un semplice metodo statico o extension method basterebbe.
</details>

### Q3: Chi dipende da chi?
Nel pattern Ports & Adapters, quale affermazione è corretta?

A) Infrastructure definisce l'interfaccia, Application la usa
B) Application definisce l'interfaccia, Infrastructure la implementa
C) Domain definisce tutte le interfacce
D) Le interfacce vanno in un progetto separato "Contracts"

<details>
<summary>Risposta</summary>

**B) Application definisce l'interfaccia, Infrastructure la implementa**

- Application "possiede" l'interfaccia perché definisce di cosa ha bisogno
- Infrastructure implementa il contratto definito da Application
- Le frecce delle dipendenze puntano verso l'interno (verso Domain/Application)

L'opzione D (progetto Contracts separato) si vede in alcuni progetti enterprise ma non è il pattern standard e può creare complessità inutile.
</details>

---

## Risorse per Approfondire

- **[Hexagonal Architecture - Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)** - L'articolo originale del 2005
- **[Ports and Adapters - Mark Seemann](https://blog.ploeh.dk/2013/12/03/layers-onions-ports-adapters-its-all-the-same/)** - Confronto con Onion Architecture
- **[Clean Architecture Cap. 22](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)** - Uncle Bob sui boundaries
- **[DIP in the Wild - Martin Fowler](https://martinfowler.com/articles/dipInTheWild.html)** - Dependency Inversion in pratica
