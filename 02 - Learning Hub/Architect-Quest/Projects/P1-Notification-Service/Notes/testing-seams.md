---
tags:
  - p1
  - testing
  - application-layer
  - from/week-03
  - status/learning
aliases:
  - Testing Seams
  - IDateTimeProvider
  - Abstraction for Testing
  - Dependency Injection for Tests
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# Testing Seams (IDateTimeProvider e simili)

> **One-liner:** Le seams sono punti di astrazione che permettono di sostituire dipendenze non deterministiche (tempo, random, I/O) con versioni controllate nei test.

## Cos'è

Una **seam** (cucitura) è un punto nel codice dove puoi alterare il comportamento senza modificare il codice stesso. Si ottiene estraendo le dipendenze "statiche" in interfacce iniettabili.

### Il Problema

```csharp
public class ScheduleNotificationHandler
{
    public async Task<Guid> Handle(ScheduleNotificationCommand cmd, CancellationToken ct)
    {
        var notification = new Notification(
            cmd.Recipient,
            cmd.Channel,
            cmd.Content,
            scheduledAt: cmd.ScheduledAt ?? DateTime.UtcNow  // ← PROBLEMA!
        );
        // ...
    }
}
```

**Perché è un problema?**

```csharp
[Fact]
public async Task Should_UseCurrentTime_WhenScheduledAtIsNull()
{
    var command = new ScheduleNotificationCommand(..., ScheduledAt: null);
    var result = await _handler.Handle(command, CancellationToken.None);

    // Come verifichi che ScheduledAt == "now"?
    // DateTime.UtcNow cambia ogni millisecondo!
    // Test NON deterministico - a volte passa, a volte fallisce
}
```

### La Soluzione

Estrai `DateTime.UtcNow` in un'interfaccia:

```csharp
// Application/Interfaces/IDateTimeProvider.cs
public interface IDateTimeProvider
{
    DateTime UtcNow { get; }
}

// Handler usa l'interfaccia
public class ScheduleNotificationHandler
{
    private readonly IDateTimeProvider _dateTimeProvider;

    public async Task<Guid> Handle(ScheduleNotificationCommand cmd, CancellationToken ct)
    {
        var notification = new Notification(
            cmd.Recipient,
            cmd.Channel,
            cmd.Content,
            scheduledAt: cmd.ScheduledAt ?? _dateTimeProvider.UtcNow  // ← Testabile!
        );
        // ...
    }
}
```

## Dipendenze che Beneficiano di Seams

| Dipendenza Diretta | Con Seam | Perché |
|-------------------|----------|--------|
| `DateTime.UtcNow` | `IDateTimeProvider` | Tempo non deterministico |
| `Guid.NewGuid()` | `IGuidGenerator` | GUID casuali |
| `Random.Next()` | `IRandomGenerator` | Numeri casuali |
| `File.ReadAllText()` | `IFileSystem` | Dipendenza da file system |
| `HttpClient.GetAsync()` | `IHttpClient` | Chiamate di rete |
| `Environment.GetEnvironmentVariable()` | `IEnvironmentProvider` | Variabili ambiente |

### Regola Generale

> **Astrai tutto ciò che è non deterministico o ha side effects esterni.**

Se chiamare lo stesso metodo due volte può dare risultati diversi, hai bisogno di una seam.

## Implementazione Completa

### 1. Interfaccia (Application Layer)

```csharp
// Application/Interfaces/IDateTimeProvider.cs
namespace NotificationService.Application.Interfaces;

public interface IDateTimeProvider
{
    DateTime UtcNow { get; }
}
```

### 2. Implementazione Reale (Infrastructure)

```csharp
// Infrastructure/Services/SystemDateTimeProvider.cs
namespace NotificationService.Infrastructure.Services;

public class SystemDateTimeProvider : IDateTimeProvider
{
    public DateTime UtcNow => DateTime.UtcNow;
}
```

### 3. Implementazione Fake (Test Project)

```csharp
// Tests/Fakes/FakeDateTimeProvider.cs
namespace NotificationService.Tests.Fakes;

public class FakeDateTimeProvider : IDateTimeProvider
{
    public DateTime UtcNow { get; set; } = new DateTime(2026, 1, 1, 12, 0, 0, DateTimeKind.Utc);
}
```

### 4. Registrazione DI

```csharp
// Infrastructure/DependencyInjection.cs
services.AddSingleton<IDateTimeProvider, SystemDateTimeProvider>();
```

### 5. Uso nel Test

```csharp
[Fact]
public async Task Should_UseCurrentTime_WhenScheduledAtIsNull()
{
    // Arrange - tempo controllato!
    var fixedTime = new DateTime(2026, 2, 17, 12, 0, 0, DateTimeKind.Utc);
    var fakeDateTimeProvider = new FakeDateTimeProvider { UtcNow = fixedTime };

    var handler = new ScheduleNotificationHandler(
        _mockRepository,
        _mockUnitOfWork,
        fakeDateTimeProvider  // Inietta il fake
    );

    var command = new ScheduleNotificationCommand(
        Recipient: "test@example.com",
        Channel: NotificationChannel.Email,
        Content: "Test",
        Subject: null,
        Priority: NotificationPriority.Normal,
        ScheduledAt: null  // Usa "now"
    );

    // Act
    var notificationId = await handler.Handle(command, CancellationToken.None);

    // Assert - deterministico!
    var savedNotification = await _mockRepository.GetByIdAsync(notificationId);
    Assert.Equal(fixedTime, savedNotification.ScheduledAt);
}
```

## Dove Vivono le Parti

```
Application/
├── Interfaces/
│   └── IDateTimeProvider.cs    ← Interfaccia (definisce il bisogno)

Infrastructure/
├── Services/
│   └── SystemDateTimeProvider.cs  ← Implementazione reale

Tests/
├── Fakes/
│   └── FakeDateTimeProvider.cs    ← Implementazione per test
```

**Perché l'interfaccia in Application?**
L'interfaccia definisce "di cosa ha bisogno l'Application Layer". L'Infrastructure fornisce "come lo implementa". Questo segue la Dependency Rule: Application non dipende da Infrastructure.

## Quando usarlo

**USA seams quando:**
- La dipendenza è non deterministica (tempo, random, GUID)
- La dipendenza ha side effects (file, network, database)
- Vuoi test veloci e deterministici
- Vuoi isolare la logica di business

## Quando NON usarlo

| Situazione | Perché |
|------------|--------|
| Logica pura (calcoli matematici) | Non serve, già testabile |
| Metodi statici che vuoi testare 1 volta | Overkill per casi rari |
| Prototipo veloce | Troppo overhead iniziale |

## Altri Esempi di Seams

### IGuidGenerator

```csharp
public interface IGuidGenerator
{
    Guid NewGuid();
}

public class SystemGuidGenerator : IGuidGenerator
{
    public Guid NewGuid() => Guid.NewGuid();
}

public class FakeGuidGenerator : IGuidGenerator
{
    public Guid NewGuid() => new Guid("12345678-1234-1234-1234-123456789012");
}
```

### IFileSystem

```csharp
public interface IFileSystem
{
    string ReadAllText(string path);
    void WriteAllText(string path, string content);
    bool Exists(string path);
}

// In test: InMemoryFileSystem che non tocca il disco
```

## Collegamenti

- [[unit-of-work]] - Altra interfaccia per testabilità
- [[ports-and-adapters]] - Le seams sono Ports
- [[application-layer]] - Dove vivono le interfacce

## Domande dalla Sessione

### D: Quali dipendenze beneficiano di un'astrazione per i test?
**R:** Tutte quelle non deterministiche o con side effects:
- Tempo (`DateTime.UtcNow`)
- Casualità (`Guid.NewGuid()`, `Random`)
- File system (`File.ReadAllText()`)
- Network (`HttpClient`)
- Environment (`Environment.GetEnvironmentVariable()`)

La regola: se chiamare lo stesso metodo due volte può dare risultati diversi, serve un'astrazione.

### D: Dove vive IDateTimeProvider - Application o Infrastructure?
**R:** **Application**, perché l'interfaccia definisce "di cosa ha bisogno l'applicazione". Infrastructure contiene l'implementazione reale (`SystemDateTimeProvider`). Questo rispetta la Dependency Rule.

### D: Come usi FakeDateTimeProvider nel test?
**R:**
1. Crei un'istanza con un tempo fisso: `var fake = new FakeDateTimeProvider { UtcNow = fixedTime };`
2. La inietti nell'handler al posto dell'implementazione reale
3. Esegui l'operazione
4. Verifichi che il risultato usi esattamente quel tempo fisso

Il test diventa deterministico - passa sempre o fallisce sempre, non dipende da quando lo esegui.

## Quiz

### Q1: Perché DateTime.UtcNow è problematico nei test?
```csharp
var notification = new Notification(scheduledAt: DateTime.UtcNow);
Assert.Equal(DateTime.UtcNow, notification.ScheduledAt);  // ???
```

<details>
<summary>Risposta</summary>

Il test è **non deterministico**. Tra la creazione della Notification e l'Assert passano alcuni millisecondi, quindi `DateTime.UtcNow` sarà diverso. Il test potrebbe passare o fallire casualmente.

**Soluzione:** Usa `IDateTimeProvider` con un valore fisso nel test.
</details>

### Q2: Dove va l'interfaccia?
Stai creando `IRandomGenerator` per astrarre `Random.Next()`. In quale progetto/layer va l'interfaccia?

A) Domain
B) Application
C) Infrastructure
D) Tests

<details>
<summary>Risposta</summary>

**B) Application**

Le interfacce che definiscono "di cosa ha bisogno l'applicazione" vivono in Application. L'implementazione reale (`SystemRandomGenerator`) va in Infrastructure, quella fake va in Tests.

Questo rispetta la Dependency Rule: Application definisce il contratto, Infrastructure lo implementa.
</details>

### Q3: Troppa astrazione?
Un collega crea `IMathProvider` con metodo `Add(int a, int b)` per poter mockare le addizioni. È una buona idea?

<details>
<summary>Risposta</summary>

**No, è overkill.**

`a + b` è:
- **Deterministico** - sempre lo stesso risultato
- **Senza side effects** - non tocca nulla di esterno
- **Veloce** - non rallenta i test

Non serve astrarre. Le seams sono per dipendenze non deterministiche o con side effects, non per logica pura.
</details>

---

## Risorse per Approfondire

- **[Working Effectively with Legacy Code - Michael Feathers](https://www.oreilly.com/library/view/working-effectively-with/0131177052/)** - Il libro che ha definito "seams"
- **[Testing on the Toilet: Don't Overuse Mocks](https://testing.googleblog.com/2013/05/testing-on-toilet-dont-overuse-mocks.html)** - Google Testing Blog
- **[TimeProvider in .NET 8](https://learn.microsoft.com/en-us/dotnet/api/system.timeprovider)** - Microsoft ha aggiunto `TimeProvider` in .NET 8!
- **[Mocking DateTime in .NET](https://blog.stephencleary.com/2020/04/mocking-datetime.html)** - Stephen Cleary
