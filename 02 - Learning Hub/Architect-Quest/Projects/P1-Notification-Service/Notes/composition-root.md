---
tags:
  - p1
  - architecture
  - dependency-injection
  - from/week-03
  - status/learning
aliases:
  - Composition Root
  - DI Configuration
  - Dependency Injection Setup
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# Composition Root e Dependency Injection

> **One-liner:** Il Composition Root è l'unico posto nell'applicazione dove configuri tutte le dipendenze - il "cablaggio" tra interfacce e implementazioni.

## Cos'è

Il **Composition Root** è il punto di ingresso dell'applicazione dove:
- Configuri il DI container
- Registri tutte le dipendenze (interfaccia → implementazione)
- "Componi" l'applicazione collegando tutti i pezzi

### Il Problema

Hai tante interfacce:

```csharp
public class ScheduleNotificationHandler
{
    public ScheduleNotificationHandler(
        INotificationRepository repository,   // Quale implementazione?
        IUnitOfWork unitOfWork,               // Quale implementazione?
        IDateTimeProvider dateTimeProvider)   // Quale implementazione?
    {
    }
}
```

Chi decide quale implementazione usare? E dove si configura?

### La Soluzione

**Un solo posto** dove fai tutti i "collegamenti":

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPOSITION ROOT                          │
│                   (Program.cs / Startup.cs)                  │
│                                                              │
│   INotificationRepository ──────► PostgresNotificationRepo   │
│   IUnitOfWork ──────────────────► AppDbContext               │
│   IDateTimeProvider ────────────► SystemDateTimeProvider     │
│   ITemplateRepository ──────────► PostgresTemplateRepo       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Dove sta il Composition Root

| Tipo App | Composition Root |
|----------|-----------------|
| ASP.NET Core Web API | `Program.cs` |
| Console App | `Program.cs` / `Main()` |
| Worker Service | `Program.cs` |
| **Test** | Setup del test / `TestFixture` |

### Perché nel Layer più Esterno?

Il Composition Root sta in `Api` (non in Application o Infrastructure) perché:

1. **Dependency Rule**: Solo il layer più esterno può "vedere" tutti gli altri
2. **Api dipende da Application e Infrastructure** - non il contrario
3. È l'unico che conosce sia le interfacce (Application) che le implementazioni (Infrastructure)

```
Api (Composition Root)
  │
  ├──► Application (interfacce)
  │
  └──► Infrastructure (implementazioni)
```

## Implementazione

### 1. Program.cs (Composition Root)

```csharp
// Api/Program.cs
var builder = WebApplication.CreateBuilder(args);

// Registra tutti i layer
builder.Services.AddApplication();                          // Application Layer
builder.Services.AddInfrastructure(builder.Configuration);  // Infrastructure Layer
builder.Services.AddControllers();                          // Api Layer

var app = builder.Build();
app.MapControllers();
app.Run();
```

### 2. Application/DependencyInjection.cs

```csharp
// Application/DependencyInjection.cs
namespace NotificationService.Application;

public static class DependencyInjection
{
    public static IServiceCollection AddApplication(this IServiceCollection services)
    {
        var assembly = typeof(DependencyInjection).Assembly;

        // MediatR - registra tutti gli Handler
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(assembly));

        // FluentValidation - registra tutti i Validators
        services.AddValidatorsFromAssembly(assembly);

        // Pipeline Behaviors
        services.AddTransient(typeof(IPipelineBehavior<,>), typeof(ValidationBehavior<,>));

        return services;
    }
}
```

### 3. Infrastructure/DependencyInjection.cs

```csharp
// Infrastructure/DependencyInjection.cs
namespace NotificationService.Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddInfrastructure(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        // Database Context
        services.AddDbContext<AppDbContext>(options =>
            options.UseNpgsql(configuration.GetConnectionString("Database")));

        // Unit of Work → stesso AppDbContext
        services.AddScoped<IUnitOfWork>(sp =>
            sp.GetRequiredService<AppDbContext>());

        // Repositories
        services.AddScoped<INotificationRepository, PostgresNotificationRepository>();
        services.AddScoped<ITemplateRepository, PostgresTemplateRepository>();

        // Services
        services.AddSingleton<IDateTimeProvider, SystemDateTimeProvider>();

        return services;
    }
}
```

## Service Lifetimes

| Lifetime | Istanze | Quando Usare | Esempio |
|----------|---------|--------------|---------|
| **Singleton** | 1 per app | Stateless, thread-safe | `IDateTimeProvider` |
| **Scoped** | 1 per request | Stato per request, non thread-safe | `DbContext`, Repositories |
| **Transient** | Nuova ogni volta | Leggero, stateless | Behaviors, Validators |

### Perché DbContext è Scoped?

| Lifetime | Problema |
|----------|----------|
| `Singleton` | DbContext non è thread-safe → crash con richieste concorrenti |
| `Transient` | Ogni repository ha DbContext diverso → Unit of Work non funziona |
| `Scoped` ✓ | Tutti i repository nella stessa request condividono lo stesso DbContext |

## Pattern: Extension Methods per Layer

Ogni layer espone un extension method `Add{Layer}()`:

```csharp
// Vantaggi:
// 1. Incapsulamento - i dettagli di registrazione sono nel layer
// 2. Testabilità - puoi chiamare solo AddApplication() nei test
// 3. Leggibilità - Program.cs rimane pulito
// 4. Manutenibilità - aggiungi nuove dipendenze nel layer corretto

builder.Services.AddApplication();
builder.Services.AddInfrastructure(configuration);
```

## Composition Root nei Test

Nei test, TU sei il Composition Root:

```csharp
public class ScheduleNotificationHandlerTests
{
    private readonly INotificationRepository _repository;
    private readonly IUnitOfWork _unitOfWork;
    private readonly IDateTimeProvider _dateTimeProvider;
    private readonly ScheduleNotificationHandler _handler;

    public ScheduleNotificationHandlerTests()
    {
        // TU decidi cosa iniettare
        _repository = Substitute.For<INotificationRepository>();  // Mock
        _unitOfWork = Substitute.For<IUnitOfWork>();              // Mock
        _dateTimeProvider = new FakeDateTimeProvider();           // Fake

        // TU componi l'handler
        _handler = new ScheduleNotificationHandler(
            _repository,
            _unitOfWork,
            _dateTimeProvider
        );
    }
}
```

## Register, Resolve, Release

Il pattern DI si basa su tre fasi:

```
1. REGISTER (Startup)
   ─────────────────────────────────────────────
   services.AddScoped<INotificationRepository, PostgresRepo>();

   "Quando qualcuno chiede INotificationRepository, dagli PostgresRepo"


2. RESOLVE (Runtime - automatico!)
   ─────────────────────────────────────────────
   // Il framework vede che il Controller ha bisogno di Handler
   // L'Handler ha bisogno di INotificationRepository
   // Cerca nel registry → PostgresRepo
   // Crea PostgresRepo e lo inietta

   public class NotificationsController
   {
       public NotificationsController(ISender mediator) // ← Risolto automaticamente
       {
       }
   }


3. RELEASE (Fine request - automatico!)
   ─────────────────────────────────────────────
   // Scoped services vengono disposed alla fine della request
   // Singleton mai disposti (fino a shutdown app)
   // Transient disposti subito dopo l'uso
```

## Quando usarlo

**SEMPRE** in applicazioni con Dependency Injection:
- Centralizza la configurazione
- Rende esplicito il "cablaggio"
- Facilita il testing (sostituisci implementazioni)

## Quando NON usarlo

| Situazione | Alternativa |
|------------|-------------|
| Script veloce senza DI | Crea oggetti direttamente |
| Applicazione piccolissima | `new` esplicito va bene |

## Collegamenti

- [[unit-of-work]] - Registrato come Scoped
- [[ports-and-adapters]] - Interfacce in Application, implementazioni in Infrastructure
- [[testing-seams]] - Sostituisci implementazioni nei test

## Domande dalla Sessione

### D: Perché il Composition Root sta in Api e non in Application?
**R:** Perché è lo strato più esterno della Clean Architecture. Solo il layer più esterno può "vedere" e dipendere da tutti gli altri. Application e Infrastructure non si conoscono - è Api che li collega. Questo rispetta la Dependency Inversion.

### D: DbContext deve essere Scoped, Singleton o Transient?
**R:** **Scoped** - una istanza per request HTTP. Motivazioni:
- `Singleton`: DbContext non è thread-safe → crash con richieste concorrenti
- `Transient`: Ogni repository avrebbe un DbContext diverso → Unit of Work non funzionerebbe
- `Scoped`: Tutti i repository condividono lo stesso DbContext per request ✓

### D: Dove registri le dipendenze nei test?
**R:** Nel setup del test (o TestFixture). Il test è un "mini Composition Root" dove decidi tu cosa iniettare - mock, fake, o implementazioni reali per integration test.

## Quiz

### Q1: Chi conosce tutti i layer?
In Clean Architecture, quale progetto può avere riferimenti sia ad Application che a Infrastructure?

A) Domain
B) Application
C) Infrastructure
D) Api (Composition Root)

<details>
<summary>Risposta</summary>

**D) Api (Composition Root)**

Solo il layer più esterno può vedere tutti gli altri. Domain non vede nessuno, Application vede solo Domain, Infrastructure vede Application e Domain. Solo Api vede tutto e può fare il "cablaggio".
</details>

### Q2: Lifetime sbagliato
```csharp
services.AddSingleton<AppDbContext>();
services.AddSingleton<INotificationRepository, PostgresNotificationRepository>();
```

Cosa succede con richieste HTTP concorrenti?

<details>
<summary>Risposta</summary>

**Crash o comportamento imprevedibile.** DbContext non è thread-safe. Con Singleton, tutte le richieste condividono la stessa istanza → race conditions, dati corrotti, eccezioni.

**Fix:** Usa `AddScoped` per DbContext e repositories.
</details>

### Q3: Extension method
Perché creare `AddApplication()` e `AddInfrastructure()` invece di mettere tutto in Program.cs?

<details>
<summary>Risposta</summary>

Quattro motivi:

1. **Incapsulamento**: I dettagli di registrazione restano nel layer appropriato
2. **Manutenibilità**: Aggiungi nuove dipendenze nel file giusto
3. **Testabilità**: Nei test puoi chiamare solo `AddApplication()` senza Infrastructure
4. **Leggibilità**: Program.cs rimane pulito e chiaro

```csharp
// Pulito e chiaro
builder.Services.AddApplication();
builder.Services.AddInfrastructure(config);

// vs 50 righe di services.Add...() in Program.cs
```
</details>

---

## Risorse per Approfondire

- **[Composition Root - Mark Seemann](https://blog.ploeh.dk/2011/07/28/CompositionRoot/)** - Articolo fondamentale
- **[Dependency Injection in .NET - Mark Seemann](https://www.manning.com/books/dependency-injection-principles-practices-patterns)** - Il libro definitivo
- **[ASP.NET Core DI - Microsoft Docs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection)** - Documentazione ufficiale
- **[Service Lifetimes Explained](https://docs.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#service-lifetimes)** - Singleton vs Scoped vs Transient
