---
tags:
  - p1
  - architecture
  - clean-architecture
  - from/week-03
  - status/learning
aliases:
  - Application Layer
  - Use Cases Layer
  - Orchestration Layer
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# Application Layer in Clean Architecture

> **One-liner:** Il layer che contiene gli Use Cases dell'applicazione - orchestra Entity, Repository e servizi senza conoscere i dettagli implementativi.

## Cos'è

L'**Application Layer** è il secondo cerchio nella Clean Architecture di Uncle Bob. Contiene la logica applicativa - il "cosa fa" il sistema, non il "come lo fa".

### Posizione nell'Architettura

```
┌─────────────────────────────────────────────────┐
│                   FRAMEWORKS                     │  ← API, CLI, UI, Database
│               (Controllers, EF Core)             │
└─────────────────────┬───────────────────────────┘
                      │ chiama
                      ▼
┌─────────────────────────────────────────────────┐
│              APPLICATION LAYER                   │  ← USE CASES (SEI QUI)
│    ScheduleNotification, CancelNotification      │
│         GetPendingNotifications, etc.            │
└─────────────────────┬───────────────────────────┘
                      │ orchestra
                      ▼
┌─────────────────────────────────────────────────┐
│                DOMAIN LAYER                      │  ← BUSINESS RULES
│          Notification, Template, etc.            │
└─────────────────────────────────────────────────┘
```

### Responsabilità

| Responsabilità | Esempio | NON fa |
|---------------|---------|--------|
| **Orchestrazione** | Coordina Entity + Repository + Servizi | Business rules (Domain) |
| **Validazione input** | Email valida? Campi obbligatori? | Validazione invarianti Entity |
| **Transazioni** | UnitOfWork, SaveChanges | Dettagli SQL/DB |
| **DTO Mapping** | Entity → DTO per response | Serializzazione JSON |
| **Autorizzazione** | L'utente può fare questa operazione? | Autenticazione (chi sei) |

### Use Case = Handler = Una Classe

Ogni operazione del sistema è una classe separata:

```csharp
// UN Use Case = UNA classe
public class ScheduleNotificationHandler : IRequestHandler<ScheduleNotificationCommand, Guid>
{
    private readonly INotificationRepository _repository;  // Interfaccia!
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Guid> Handle(ScheduleNotificationCommand command, CancellationToken ct)
    {
        // 1. Crea Entity (Domain decide le regole di business)
        var notification = new Notification(
            command.Recipient,
            command.Channel,
            command.Content
        );

        // 2. Persisti (ma non sa COME - usa interfaccia)
        await _repository.AddAsync(notification, ct);
        await _unitOfWork.SaveChangesAsync(ct);

        // 3. Ritorna risultato
        return notification.Id;
    }
}
```

## Dependency Rule

La regola fondamentale di Clean Architecture:

> **Le dipendenze puntano solo verso l'interno (verso Domain)**

```
Frameworks → Application → Domain
    ↓              ↓
    ✗              ✗         Domain non dipende da nessuno
```

L'Application Layer:
- **Dipende da:** Domain (usa Entity, Value Objects, Domain Events)
- **NON dipende da:** Infrastructure, API, Database, framework specifici

### Come Rispettarla

```csharp
// ❌ VIOLA Dependency Rule
public class ScheduleNotificationHandler
{
    private readonly PostgresNotificationRepository _repository;  // Conosce Infrastructure!
    private readonly AppDbContext _context;  // Conosce EF Core!
}

// ✅ RISPETTA Dependency Rule
public class ScheduleNotificationHandler
{
    private readonly INotificationRepository _repository;  // Interfaccia in Application
    private readonly IUnitOfWork _unitOfWork;  // Interfaccia in Application
}
```

## Quando usarlo

**USA un Application Layer separato quando:**

| Situazione | Perché |
|------------|--------|
| Hai logica di business | Serve orchestrazione |
| Stessa logica da API + CLI + Jobs | Riuso senza duplicazione |
| Vuoi testare senza framework | Handler testabili con mock |
| Team separati su API e business logic | Boundaries chiari |
| Progetto medio-grande | Struttura paga nel tempo |

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| CRUD banale senza logica | Overhead inutile |
| Prototipo veloce | Troppa struttura |
| Progetto piccolissimo (< 1 mese) | Overkill |
| Entity = DTO | Se non hai Domain, non serve orchestrarlo |

## Esempio Completo

### Struttura Cartelle

```
Application/
├── Commands/
│   └── Notifications/
│       ├── ScheduleNotificationCommand.cs
│       └── ScheduleNotificationHandler.cs
├── Queries/
│   └── Notifications/
│       ├── GetNotificationByIdQuery.cs
│       └── GetNotificationByIdHandler.cs
├── Interfaces/
│   ├── INotificationRepository.cs
│   └── IUnitOfWork.cs
├── DTOs/
│   └── NotificationDto.cs
├── Validators/
│   └── ScheduleNotificationCommandValidator.cs
└── Behaviors/
    └── ValidationBehavior.cs
```

### Flusso Tipico

```
API Controller
      │
      ▼
┌─────────────────┐
│ MediatR.Send()  │  ← Dispatch al giusto Handler
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ValidationBeh.  │  ← Pipeline: valida input
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LoggingBehavior │  ← Pipeline: logga request/response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Handler      │  ← Esegue Use Case
│  (Application)  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────────┐
│Domain │ │Repository │  ← Interfaccia (Port)
│Entity │ │(Interface)│
└───────┘ └─────┬─────┘
                │ implementata da
                ▼
         ┌─────────────┐
         │Infrastructure│  ← Adapter (PostgreSQL, etc.)
         └─────────────┘
```

## Collegamenti

- [[clean-architecture]] - I 4 layer e la Dependency Rule
- [[cqrs-and-mediatr]] - Come strutturare Commands e Queries
- [[ports-and-adapters]] - Pattern per le interfacce
- [[fluentvalidation]] - Validazione input nell'Application

## Domande dalla Sessione

### D: Dove va la validazione dell'email - Domain o Application?
**R:** Dipende dal TIPO di validazione:
- **Domain:** Validazione di invarianti/stato (`email != null`, formato base) - l'Entity deve essere sempre valida
- **Application:** Validazione che richiede dipendenze esterne (`await _repo.EmailExistsAsync(email)`) - il Domain non può avere dipendenze

### D: Come fa l'Handler a salvare su PostgreSQL senza violare Dependency Rule?
**R:** Usa Ports & Adapters:
1. Handler dipende da `INotificationRepository` (interfaccia in Application)
2. `PostgresNotificationRepository` implementa l'interfaccia (in Infrastructure)
3. DI container fa il binding `INotificationRepository → PostgresNotificationRepository`
4. Handler non sa (e non deve sapere) che usa PostgreSQL

### D: Perché Use Cases separati invece di un NotificationService monolitico?
**R:** Quattro motivi:
1. **SRP** - ogni handler ha una sola responsabilità
2. **No God Class** - evita classi con 50 metodi
3. **Testabilità** - testi un use case alla volta, mock semplici
4. **Modificabilità** - cambi un handler senza toccare gli altri

## Quiz

### Q1: Cosa NON fa l'Application Layer?
Quale di queste NON è responsabilità dell'Application Layer?

A) Orchestrare Entity e Repository
B) Validare input della request
C) Decidere le business rules dell'Entity
D) Mappare Entity a DTO

<details>
<summary>Risposta</summary>

**C) Decidere le business rules dell'Entity**

Le business rules vivono nel Domain Layer. L'Application Layer orchestra, ma non decide le regole. Esempio: "una notifica può essere cancellata solo se è Pending" è una regola del Domain (metodo `Cancel()` nell'Entity), non dell'Application.
</details>

### Q2: Trova l'errore
```csharp
public class ScheduleNotificationHandler
{
    private readonly AppDbContext _context;

    public async Task<Guid> Handle(ScheduleNotificationCommand cmd, CancellationToken ct)
    {
        var notification = new Notification(cmd.Recipient, cmd.Channel, cmd.Content);
        _context.Notifications.Add(notification);
        await _context.SaveChangesAsync(ct);
        return notification.Id;
    }
}
```

<details>
<summary>Risposta</summary>

L'handler dipende direttamente da `AppDbContext` (EF Core) invece che da un'interfaccia.

**Problemi:**
1. Viola Dependency Rule (Application conosce Infrastructure)
2. Non testabile senza database reale
3. Accoppiato a EF Core - cambiare ORM = riscrivere handler

**Fix:**
```csharp
public class ScheduleNotificationHandler
{
    private readonly INotificationRepository _repository;
    private readonly IUnitOfWork _unitOfWork;
    // ...
}
```
</details>

### Q3: God Service
Hai questa classe con 15 metodi:

```csharp
public class NotificationService
{
    public async Task<Guid> Schedule(...) { }
    public async Task Cancel(...) { }
    public async Task Retry(...) { }
    public async Task<NotificationDto> GetById(...) { }
    public async Task<List<NotificationDto>> GetPending(...) { }
    public async Task<List<NotificationDto>> GetByStatus(...) { }
    // ... altri 9 metodi
}
```

Come la ristrutturi seguendo Clean Architecture?

<details>
<summary>Risposta</summary>

Separa in Use Cases individuali (un handler per operazione):

```
Commands/
├── ScheduleNotificationCommand + Handler
├── CancelNotificationCommand + Handler
└── RetryNotificationCommand + Handler

Queries/
├── GetNotificationByIdQuery + Handler
├── GetPendingNotificationsQuery + Handler
└── GetNotificationsByStatusQuery + Handler
```

Ogni handler:
- Ha una sola responsabilità
- È testabile in isolamento
- Può evolvere indipendentemente
- È facile da trovare (naming esplicito)
</details>

---

## Risorse per Approfondire

- **[The Clean Architecture - Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** - L'articolo originale
- **[Clean Architecture Cap. 20-22](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)** - Capitoli su Use Cases
- **[Screaming Architecture - Uncle Bob](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html)** - Perché la struttura deve "urlare" lo scopo
- **[MediatR + Clean Architecture - Jason Taylor](https://jasontaylor.dev/clean-architecture-getting-started/)** - Implementazione pratica in .NET
