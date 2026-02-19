---
tags:
  - p1
  - architecture
  - clean-architecture
  - from/week-04
  - status/learning
aliases:
  - Infrastructure Layer
  - Layer Infrastruttura
created: 2026-02-18
source: "Sessione Week 4 - Infrastructure Layer"
---

# Infrastructure Layer in Clean Architecture

> **One-liner:** Il layer più esterno che implementa i dettagli tecnici (database, API esterne, file system) e collega la business logic al mondo reale attraverso gli Adapter.

## Cos'è

L'Infrastructure Layer è il **layer più esterno** in Clean Architecture. Contiene tutto ciò che è "dettaglio tecnico" - cose che potrebbero cambiare senza modificare la business logic.

```
┌─────────────────────────────────────────────────────────────────┐
│                    INFRASTRUCTURE LAYER                          │
│                                                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   Database      │  │  External APIs  │  │   File System   │ │
│  │   (EF Core,     │  │  (SendGrid,     │  │   (Storage,     │ │
│  │    Dapper)      │  │   Twilio)       │  │    Logging)     │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
│           │                    │                    │           │
│           └────────────────────┼────────────────────┘           │
│                                │                                 │
│                    ┌───────────▼───────────┐                    │
│                    │  IMPLEMENTS INTERFACES │                    │
│                    │  from Application      │                    │
│                    └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼ implements
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
│                                                                  │
│              INotificationRepository  IUnitOfWork               │
│              IEmailSender             ISmsSender                 │
│                          (PORTS)                                 │
└─────────────────────────────────────────────────────────────────┘
```

### La Regola Fondamentale

> **Infrastructure DIPENDE da Application (e Domain), mai il contrario.**

- Infrastructure conosce Application (implementa le sue interfacce)
- Application NON sa nulla di Infrastructure
- Infrastructure può usare le entities di Domain

### Cosa Contiene Infrastructure

| Tipo | Esempi |
|------|--------|
| **Persistence** | EF Core DbContext, Repositories, Migrations |
| **External Services** | SendGrid client, Twilio client, Azure clients |
| **Cross-cutting** | Logging adapters, Caching (Redis), Background jobs |
| **Framework adapters** | ASP.NET specifics, Message queue consumers |

## Quando usarlo

**USA Infrastructure Layer per:**

| Situazione | Esempio |
|------------|---------|
| Database access | `PostgresNotificationRepository : INotificationRepository` |
| API esterne | `SendGridEmailSender : IEmailSender` |
| File system | `FileStorageService : IStorageService` |
| Message queues | `RabbitMqPublisher : IEventPublisher` |
| Caching | `RedisCache : ICache` |

## Quando NON usarlo

| Cosa | Perché | Dove va |
|------|--------|---------|
| Business rules | Non sono dettagli tecnici | Domain |
| Use case orchestration | Non sono dettagli tecnici | Application |
| DTOs/ViewModels | Sono contratti API | Application o API |
| Validation rules | Sono business logic | Application |
| Interfacce (Ports) | Definiscono cosa serve all'App | Application |

## Esempio

### Struttura Cartelle

```
src/
├── Domain/                      ← Nessuna dipendenza
│
├── Application/                 ← Dipende solo da Domain
│   ├── Interfaces/
│   │   ├── INotificationRepository.cs   ← PORT
│   │   ├── ITemplateRepository.cs       ← PORT
│   │   └── IUnitOfWork.cs               ← PORT
│
├── Infrastructure/              ← Dipende da Application + Domain
│   ├── Persistence/
│   │   ├── AppDbContext.cs
│   │   ├── Configurations/
│   │   │   ├── NotificationConfiguration.cs
│   │   │   └── TemplateConfiguration.cs
│   │   ├── Repositories/
│   │   │   ├── PostgresNotificationRepository.cs  ← ADAPTER
│   │   │   └── PostgresTemplateRepository.cs      ← ADAPTER
│   │   ├── UnitOfWork.cs                          ← ADAPTER
│   │   └── Migrations/
│   ├── Services/
│   │   ├── SendGridEmailSender.cs    ← ADAPTER
│   │   └── TwilioSmsSender.cs        ← ADAPTER
│   └── DependencyInjection.cs
│
└── Api/                         ← Composition Root
    └── Program.cs
```

### Repository Implementation (ADAPTER)

```csharp
// Infrastructure/Persistence/Repositories/PostgresNotificationRepository.cs
namespace NotificationService.Infrastructure.Persistence.Repositories;

public class PostgresNotificationRepository : INotificationRepository  // Implementa PORT
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

### DI Registration

```csharp
// Infrastructure/DependencyInjection.cs
namespace NotificationService.Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddInfrastructure(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        // DbContext
        services.AddDbContext<AppDbContext>(options =>
            options.UseNpgsql(configuration.GetConnectionString("DefaultConnection")));

        // Repositories
        services.AddScoped<INotificationRepository, PostgresNotificationRepository>();
        services.AddScoped<ITemplateRepository, PostgresTemplateRepository>();
        services.AddScoped<IUnitOfWork, UnitOfWork>();

        // External Services
        services.AddScoped<IEmailSender, SendGridEmailSender>();
        services.AddScoped<ISmsSender, TwilioSmsSender>();

        return services;
    }
}
```

## Collegamenti

- [[clean-architecture]] - I 4 layer e la Dependency Rule
- [[ports-and-adapters]] - PORT (Application) vs ADAPTER (Infrastructure)
- [[composition-root]] - Dove si registrano i servizi Infrastructure
- [[repository-implementation]] - Dettagli implementazione repository

## Domande dalla Sessione

### D: Posso mettere INotificationRepository in Infrastructure/Interfaces/?
**R:** No! L'interfaccia definisce **cosa serve** all'Application, non come viene implementato. È una PORT che vive in Application. Infrastructure contiene solo gli ADAPTER (implementazioni).

### D: Posso usare SendGridClient direttamente nell'handler?
**R:** No! Questo crea una dipendenza diretta Application → Infrastructure, violando la Dependency Rule. L'handler deve usare `IEmailSender` (interfaccia in Application), e Infrastructure fornisce `SendGridEmailSender : IEmailSender`.

### D: Infrastructure può dipendere da Domain?
**R:** Sì! Infrastructure può (e deve) usare le entities di Domain per salvarle nel database. La Dependency Rule permette dipendenze verso l'interno: Infrastructure → Application → Domain.

### D: Perché il Repository NON chiama SaveChangesAsync()?
**R:** Per il **Unit of Work pattern**. Più repository potrebbero fare modifiche nella stessa transazione:
```csharp
await _notificationRepository.AddAsync(notification);
await _templateRepository.UpdateAsync(template);
await _unitOfWork.SaveChangesAsync();  // UNA transazione, entrambe le modifiche
```
Se ogni repository chiamasse SaveChanges, perderemmo l'atomicità.

### D: Quando usare Dapper invece di EF Core?
**R:** Per **query analitiche complesse** su grandi volumi di dati. EF Core può generare SQL inefficiente per query con molti JOIN e aggregazioni. Dapper ti dà controllo totale sul SQL.

## Quiz

### Q1: Direzione delle dipendenze
Quale affermazione è CORRETTA riguardo alle dipendenze?

A) Application può dipendere da Infrastructure per i repository
B) Infrastructure implementa le interfacce definite in Application
C) Domain può usare INotificationRepository direttamente
D) Infrastructure non deve mai conoscere Domain

<details>
<summary>Risposta</summary>

**B) Infrastructure implementa le interfacce definite in Application**

- A è FALSO: Application non deve MAI dipendere da Infrastructure (Dependency Rule)
- C è FALSO: Domain non dipende da nulla
- D è FALSO: Infrastructure USA le entities di Domain per persistence

La freccia delle dipendenze: Infrastructure → Application → Domain
</details>

### Q2: Cosa va in Infrastructure?
Quale di questi NON appartiene all'Infrastructure Layer?

A) PostgresNotificationRepository
B) SendGridEmailSender
C) INotificationRepository
D) AppDbContext

<details>
<summary>Risposta</summary>

**C) INotificationRepository**

L'interfaccia (PORT) appartiene all'Application Layer perché definisce **cosa serve** all'applicazione. Infrastructure contiene solo le implementazioni (ADAPTER).
</details>

### Q3: Sostituibilità
Perché è importante che Infrastructure implementi interfacce di Application?

<details>
<summary>Risposta</summary>

**Sostituibilità e Testabilità:**

1. **Testing:** Posso mockare `INotificationRepository` nei test senza database reale
2. **Sostituibilità:** Posso passare da PostgreSQL a MongoDB cambiando solo Infrastructure
3. **Isolamento:** Application non sa (e non deve sapere) quale database usiamo
4. **Dependency Rule:** Le dipendenze puntano verso l'interno, mai verso l'esterno
</details>

### Q4: Repository e SaveChanges
Perché il repository NON deve chiamare `SaveChangesAsync()` direttamente?

<details>
<summary>Risposta</summary>

**Unit of Work Pattern:** Più repository potrebbero fare modifiche nella stessa transazione.

```csharp
await _notificationRepository.AddAsync(notification);
await _templateRepository.UpdateAsync(template);
await _unitOfWork.SaveChangesAsync();  // UNA transazione
```

Se ogni repository chiamasse SaveChanges, perderemmo l'atomicità della transazione.
</details>

### Q5: EF Core vs Dapper
Devi generare un report con statistiche aggregate su milioni di notifiche. EF Core è la scelta giusta?

<details>
<summary>Risposta</summary>

**No.** Per query analitiche su grandi volumi di dati, usa **Dapper** o SQL raw.

EF Core può generare SQL inefficiente per query con molti JOIN e aggregazioni. Dapper ti dà controllo totale sul SQL e performance migliori.

**Best practice:** Usa EF Core per CRUD, Dapper per analytics.
</details>

### Q6: PostgreSQL vs MongoDB
Un collega propone MongoDB per "più flessibilità". Quali domande gli faresti?

<details>
<summary>Risposta</summary>

| Domanda | Perché |
|---------|--------|
| "Hai relazioni tra i dati?" | MongoDB non gestisce bene i JOIN |
| "Servono transazioni ACID?" | MongoDB ha limitazioni |
| "Che volume di scritture?" | MongoDB scala meglio in write-heavy |
| "Serve schema flessibile davvero?" | O è solo pigrizia nel design? |
| "Il team conosce MongoDB?" | Learning curve da considerare |
</details>

---

---

## Tecnologie: EF Core + Npgsql

### Entity Framework Core

EF Core è un **ORM (Object-Relational Mapper)** per .NET. Traduce oggetti C# in tabelle database e viceversa.

```
┌─────────────────────────────────────────────────────────────────┐
│   var notification = new Notification("Hello", recipient);      │
│   await _context.Notifications.AddAsync(notification);          │
│   await _context.SaveChangesAsync();                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼  EF Core traduce
┌─────────────────────────────────────────────────────────────────┐
│   INSERT INTO "Notifications" ("Id", "Content", "RecipientId")  │
│   VALUES ('abc-123', 'Hello', 'user-456');                      │
└─────────────────────────────────────────────────────────────────┘
```

#### Caratteristiche Principali

| Feature | Descrizione |
|---------|-------------|
| **Code-First** | Definisci classi C# → EF genera il database |
| **Change Tracking** | EF traccia modifiche agli oggetti automaticamente |
| **LINQ to SQL** | Scrivi query in C#, EF le traduce in SQL |
| **Migrations** | Versionamento dello schema database |

#### LINQ → SQL

```csharp
// C# (LINQ)
var pending = await _context.Notifications
    .Where(n => n.Status == NotificationStatus.Pending)
    .Where(n => n.ScheduledFor <= DateTime.UtcNow)
    .OrderBy(n => n.ScheduledFor)
    .Take(100)
    .ToListAsync();

// EF Core genera:
// SELECT * FROM "Notifications"
// WHERE "Status" = 'Pending' AND "ScheduledFor" <= '2026-02-18'
// ORDER BY "ScheduledFor" LIMIT 100;
```

#### Change Tracking

```csharp
var notification = await _context.Notifications.FindAsync(id);
// State: Unchanged

notification.MarkAsSent();
// State: Modified (EF ha rilevato il cambiamento!)

await _context.SaveChangesAsync();
// UPDATE "Notifications" SET "Status" = 'Sent' WHERE "Id" = '...';
```

### Npgsql

Npgsql è il **provider PostgreSQL per .NET**. È il "ponte" tra EF Core e PostgreSQL.

```
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│   EF Core     │ ──► │    Npgsql     │ ──► │  PostgreSQL   │
│ (ORM generico)│     │ (Driver .NET) │     │  (Database)   │
└───────────────┘     └───────────────┘     └───────────────┘
```

EF Core è **database-agnostic** - i provider traducono per il DB specifico:

| Provider | Database |
|----------|----------|
| `Npgsql.EntityFrameworkCore.PostgreSQL` | PostgreSQL |
| `Microsoft.EntityFrameworkCore.SqlServer` | SQL Server |
| `Microsoft.EntityFrameworkCore.Sqlite` | SQLite |

### Trade-offs: EF Core vs Dapper

| ORM | Pro | Contro | Quando usarlo |
|-----|-----|--------|---------------|
| **EF Core** | Full-featured, LINQ, migrations, change tracking | Performance overhead | Applicazioni domain-rich |
| **Dapper** | Velocissimo, controllo SQL totale | Più codice manuale | Query analitiche, performance critica |

**Best Practice:** Usa entrambi nello stesso progetto!
- EF Core per CRUD e business logic
- Dapper per report e query complesse

### Trade-offs: PostgreSQL vs Altri

| Database | Pro | Contro | Quando usarlo |
|----------|-----|--------|---------------|
| **PostgreSQL** | Open source, feature-rich, JSON | Più complesso | Production, SaaS |
| **SQL Server** | Integrazione Microsoft | Licenze costose | Ambiente Microsoft |
| **MongoDB** | Schema-less, scala orizzontale | No ACID by default | Big data, schema flessibile |

### Setup EF Core + Npgsql

```bash
# Packages da installare
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Npgsql.EntityFrameworkCore.PostgreSQL
dotnet add package Microsoft.EntityFrameworkCore.Design
```

```csharp
// Configurazione
services.AddDbContext<AppDbContext>(options =>
    options.UseNpgsql(connectionString));
```

---

## Risorse per Approfondire

- **[Clean Architecture Cap. 23-24](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)** - Frameworks & Databases are details
- **[EF Core Documentation](https://learn.microsoft.com/en-us/ef/core/)** - Getting started, configuration, migrations
- **[Repository Pattern - Martin Fowler](https://martinfowler.com/eaaCatalog/repository.html)** - Pattern originale
- **[Implementing Infrastructure in Clean Architecture - Jason Taylor](https://jasontaylor.dev/clean-architecture-getting-started/)** - Esempio pratico .NET
- **[Npgsql Documentation](https://www.npgsql.org/doc/index.html)** - PostgreSQL provider per .NET
- **[Dapper Tutorial](https://dapper-tutorial.net/)** - Micro ORM per query complesse
