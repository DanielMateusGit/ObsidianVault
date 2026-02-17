---
tags:
  - p1
  - testing
  - application-layer
  - from/week-03
  - status/learning
aliases:
  - Unit Testing
  - Mocking
  - NSubstitute
  - AAA Pattern
created: 2026-02-17
source: "Sessione Week 3 - Application Layer"
---

# Testing con Mocks (NSubstitute)

> **One-liner:** I mock sono oggetti "finti" che simulano dipendenze, permettendo di testare la logica in isolamento e verificare le interazioni tra componenti.

## Cos'è

Un **mock** è un oggetto generato da una libreria che:
1. Implementa un'interfaccia senza logica reale
2. Può essere configurato per ritornare valori specifici
3. Può verificare se/quante volte i suoi metodi sono stati chiamati

### Il Problema

```csharp
public class ScheduleNotificationHandler
{
    public ScheduleNotificationHandler(
        INotificationRepository repository,  // Connesso a PostgreSQL!
        IUnitOfWork unitOfWork,              // Transazioni DB!
        IDateTimeProvider dateTimeProvider)  // Tempo reale!
    {
    }
}
```

Come testi **solo la logica dell'handler** senza:
- Database reale (lento, richiede setup)
- Tempo reale (non deterministico)
- Side effects (dati persistenti tra test)

### La Soluzione

```csharp
// Sostituisci le dipendenze reali con mock
var mockRepository = Substitute.For<INotificationRepository>();
var mockUnitOfWork = Substitute.For<IUnitOfWork>();
var fakeDateTimeProvider = new FakeDateTimeProvider();

// Testa l'handler in isolamento
var handler = new ScheduleNotificationHandler(
    mockRepository,
    mockUnitOfWork,
    fakeDateTimeProvider);
```

## Mock vs Fake vs Stub

| Tipo | Creato da | Logica | Scopo |
|------|-----------|--------|-------|
| **Mock** | Libreria (NSubstitute) | Nessuna | Verificare interazioni (`Received()`) |
| **Fake** | Te, manualmente | Semplificata ma reale | Fornire comportamento controllato |
| **Stub** | Libreria o manuale | Solo return values | Fornire dati per il test |

```csharp
// MOCK - creato da NSubstitute
var mockRepo = Substitute.For<INotificationRepository>();
// Nessuna logica - devi configurare tutto con .Returns()
// Puoi verificare chiamate con .Received()

// FAKE - classe che scrivi tu
public class FakeDateTimeProvider : IDateTimeProvider
{
    public DateTime UtcNow { get; set; } = new DateTime(2026, 1, 1);
    // Ha logica reale! Ritorna il valore che imposti.
}

// STUB - mock configurato solo per ritornare valori
var stubRepo = Substitute.For<INotificationRepository>();
stubRepo.GetByIdAsync(Arg.Any<Guid>(), Arg.Any<CancellationToken>())
    .Returns(someNotification);
// Usi solo .Returns(), non verifichi chiamate
```

## Pattern AAA (Arrange-Act-Assert)

Ogni unit test segue questa struttura:

```csharp
[Fact]
public async Task Should_CreateNotification_WhenCommandIsValid()
{
    // ========== ARRANGE ==========
    // Prepara mock, fake, e l'oggetto da testare
    var mockRepository = Substitute.For<INotificationRepository>();
    var mockUnitOfWork = Substitute.For<IUnitOfWork>();
    var fakeDateTimeProvider = new FakeDateTimeProvider
    {
        UtcNow = new DateTime(2026, 2, 17, 12, 0, 0)
    };

    var handler = new ScheduleNotificationHandler(
        mockRepository,
        mockUnitOfWork,
        fakeDateTimeProvider);

    var command = new ScheduleNotificationCommand(
        Recipient: "test@example.com",
        Channel: NotificationChannel.Email,
        Content: "Test content",
        Subject: "Test",
        Priority: NotificationPriority.Normal,
        ScheduledAt: null
    );

    // ========== ACT ==========
    // Esegui l'operazione da testare
    var result = await handler.Handle(command, CancellationToken.None);

    // ========== ASSERT ==========
    // Verifica il risultato e le interazioni
    Assert.NotEqual(Guid.Empty, result);

    await mockRepository.Received(1).AddAsync(
        Arg.Any<Notification>(),
        Arg.Any<CancellationToken>());

    await mockUnitOfWork.Received(1).SaveChangesAsync(
        Arg.Any<CancellationToken>());
}
```

## NSubstitute - Operazioni

### Creare un Mock

```csharp
var mockRepo = Substitute.For<INotificationRepository>();
```

### Configurare Return Values

```csharp
// Ritorna un valore specifico
mockRepo.GetByIdAsync(Arg.Any<Guid>(), Arg.Any<CancellationToken>())
    .Returns(new Notification(...));

// Ritorna null (simula "non trovato")
mockRepo.GetByIdAsync(Arg.Any<Guid>(), Arg.Any<CancellationToken>())
    .Returns((Notification?)null);

// Ritorna valori diversi per chiamate successive
mockRepo.GetByIdAsync(Arg.Any<Guid>(), Arg.Any<CancellationToken>())
    .Returns(notification1, notification2, notification3);
```

### Verificare Chiamate

```csharp
// Verifica che sia stato chiamato esattamente 1 volta
await mockRepo.Received(1).AddAsync(
    Arg.Any<Notification>(),
    Arg.Any<CancellationToken>());

// Verifica che NON sia stato chiamato
await mockRepo.DidNotReceive().DeleteAsync(
    Arg.Any<Notification>(),
    Arg.Any<CancellationToken>());

// Verifica chiamato almeno una volta
await mockRepo.Received().AddAsync(
    Arg.Any<Notification>(),
    Arg.Any<CancellationToken>());
```

### Catturare Argomenti

```csharp
// Cattura l'oggetto passato al mock
Notification? capturedNotification = null;

await mockRepo.AddAsync(
    Arg.Do<Notification>(n => capturedNotification = n),
    Arg.Any<CancellationToken>());

// Dopo l'Act, puoi ispezionare l'oggetto
await handler.Handle(command, CancellationToken.None);

Assert.Equal("test@example.com", capturedNotification!.Recipient);
Assert.Equal(NotificationChannel.Email, capturedNotification.Channel);
```

### Perché Arg.Any<> nel Received()?

```csharp
// ❌ NON FUNZIONA - notification non esiste qui!
var notification = ???  // Creata DENTRO l'handler
await mockRepo.Received(1).AddAsync(notification, ct);

// ✅ CORRETTO - verifica che sia stato chiamato con UNA qualsiasi notifica
await mockRepo.Received(1).AddAsync(Arg.Any<Notification>(), Arg.Any<CancellationToken>());
```

L'oggetto `Notification` viene creato **dentro** l'handler - non hai accesso ad esso nel test. `Arg.Any<>()` verifica che il metodo sia stato chiamato con un argomento di quel tipo.

## Cosa Testare

### Sì - Testa Questi

| Scenario | Cosa Verifichi |
|----------|----------------|
| **Happy path** | Command valido → risultato atteso |
| **Entity non trovata** | `GetById` ritorna null → comportamento corretto |
| **Business rules** | Cancellare notifica già inviata → eccezione |
| **Interazioni** | `AddAsync` e `SaveChangesAsync` chiamati |
| **Edge cases** | Input al limite, valori nulli |

### No - Non Testare Questi

| Cosa | Perché |
|------|--------|
| Che il mock funzioni | Stai testando NSubstitute, non il tuo codice |
| Implementazione interna | Testa comportamento, non dettagli |
| Il repository reale | Quello è integration test |
| Getter/setter banali | Nessuna logica da testare |

## Perché Verificare SaveChangesAsync?

```csharp
await mockUnitOfWork.Received(1).SaveChangesAsync(Arg.Any<CancellationToken>());
```

**Questa verifica È utile!** Stai testando che l'handler:
1. Chiami `SaveChangesAsync` quando deve
2. Lo chiami il numero corretto di volte
3. Non dimentichi di persistere le modifiche

Se rimuovi la chiamata a `SaveChanges` nell'handler, il test **fallisce** - hai catturato un bug!

Non stai "testando il mock" - stai testando che il tuo codice **interagisca correttamente** con le dipendenze.

## Esempio Completo

```csharp
public class CancelNotificationHandlerTests
{
    private readonly INotificationRepository _mockRepository;
    private readonly IUnitOfWork _mockUnitOfWork;
    private readonly CancelNotificationHandler _handler;

    public CancelNotificationHandlerTests()
    {
        _mockRepository = Substitute.For<INotificationRepository>();
        _mockUnitOfWork = Substitute.For<IUnitOfWork>();
        _handler = new CancelNotificationHandler(_mockRepository, _mockUnitOfWork);
    }

    [Fact]
    public async Task Should_ReturnTrue_WhenNotificationExists()
    {
        // Arrange
        var notificationId = Guid.NewGuid();
        var notification = CreateTestNotification(notificationId);

        _mockRepository.GetByIdAsync(notificationId, Arg.Any<CancellationToken>())
            .Returns(notification);

        // Act
        var result = await _handler.Handle(
            new CancelNotificationCommand(notificationId),
            CancellationToken.None);

        // Assert
        Assert.True(result);
        await _mockRepository.Received(1).UpdateAsync(notification, Arg.Any<CancellationToken>());
        await _mockUnitOfWork.Received(1).SaveChangesAsync(Arg.Any<CancellationToken>());
    }

    [Fact]
    public async Task Should_ReturnFalse_WhenNotificationNotFound()
    {
        // Arrange
        _mockRepository.GetByIdAsync(Arg.Any<Guid>(), Arg.Any<CancellationToken>())
            .Returns((Notification?)null);

        // Act
        var result = await _handler.Handle(
            new CancelNotificationCommand(Guid.NewGuid()),
            CancellationToken.None);

        // Assert
        Assert.False(result);
        await _mockRepository.DidNotReceive().UpdateAsync(
            Arg.Any<Notification>(),
            Arg.Any<CancellationToken>());
        await _mockUnitOfWork.DidNotReceive().SaveChangesAsync(
            Arg.Any<CancellationToken>());
    }

    private static Notification CreateTestNotification(Guid id)
    {
        // Helper per creare notifiche di test
        return new Notification(
            "test@example.com",
            NotificationChannel.Email,
            "Test content");
    }
}
```

## Collegamenti

- [[testing-seams]] - IDateTimeProvider e altre seams
- [[composition-root]] - Come il DI aiuta il testing
- [[cqrs-commands]] - Gli handler che testiamo

## Domande dalla Sessione

### D: Perché usi Arg.Any<Notification>() nel Received()?
**R:** Perché la `Notification` viene creata **dentro** l'handler - non hai accesso ad essa nel test. `Arg.Any<>()` verifica che il metodo sia stato chiamato con un argomento di quel tipo, senza specificare quale istanza esatta.

### D: Verificare SaveChangesAsync è utile o stai testando il mock?
**R:** **È utile!** Stai testando che l'handler interagisca correttamente con le dipendenze. Se dimentichi di chiamare SaveChanges, il test fallisce - hai catturato un bug. Non stai testando che il mock funzioni, stai testando che il tuo codice faccia la cosa giusta.

### D: Differenza tra Mock e Fake?
**R:**
- **Mock**: Creato da libreria (NSubstitute), nessuna logica propria. Serve per configurare return values e verificare interazioni.
- **Fake**: Classe che scrivi tu con implementazione semplificata ma reale. Es. `FakeDateTimeProvider` ha logica vera - ritorna il valore che imposti.

## Quiz

### Q1: Arg.Any vs valore specifico
```csharp
await mockRepo.Received(1).AddAsync(notification, ct);  // ❌
await mockRepo.Received(1).AddAsync(Arg.Any<Notification>(), Arg.Any<CancellationToken>());  // ✅
```

Perché la prima riga non funziona?

<details>
<summary>Risposta</summary>

La `Notification` viene creata **dentro l'handler** - non esiste una variabile `notification` nel test a cui fare riferimento. `Arg.Any<>()` dice "verifica che sia stato chiamato con UN oggetto di questo tipo, non mi interessa quale specifico".

Se vuoi ispezionare l'oggetto creato, usa `Arg.Do<>()` per catturarlo.
</details>

### Q2: Verifica interazione
```csharp
[Fact]
public async Task Test()
{
    // ... arrange ...
    await handler.Handle(command, ct);

    await mockUnitOfWork.Received(1).SaveChangesAsync(Arg.Any<CancellationToken>());
}
```

Questa verifica è utile o stai "testando il mock"?

<details>
<summary>Risposta</summary>

**È utile!** Stai verificando che l'handler chiami `SaveChangesAsync` - se qualcuno rimuove quella chiamata, il test fallisce.

Non stai testando che il mock funzioni. Stai testando che il tuo codice **collabori correttamente** con le dipendenze. Le verifiche di interazione sono parte legittima del testing.
</details>

### Q3: Mock vs Fake
Quando useresti un Fake invece di un Mock?

<details>
<summary>Risposta</summary>

Usa un **Fake** quando:
- Hai bisogno di logica reale semplificata (es. `FakeDateTimeProvider` che ritorna un tempo controllato)
- Il comportamento è semplice da implementare
- Vuoi evitare di configurare molti `.Returns()`

Usa un **Mock** quando:
- Devi verificare interazioni (`Received()`, `DidNotReceive()`)
- L'interfaccia ha molti metodi e ti serve solo configurarne alcuni
- Vuoi catturare argomenti con `Arg.Do<>()`

In pratica: Fake per dipendenze semplici (tempo, config), Mock per dipendenze complesse (repository, servizi esterni).
</details>

---

## Risorse per Approfondire

- **[NSubstitute Documentation](https://nsubstitute.github.io/)** - Documentazione ufficiale
- **[The Art of Unit Testing](https://www.manning.com/books/the-art-of-unit-testing-third-edition)** - Roy Osherove
- **[Unit Testing Best Practices - Microsoft](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)** - Best practices ufficiali
- **[Mocks Aren't Stubs - Martin Fowler](https://martinfowler.com/articles/mocksArentStubs.html)** - Differenze tra test doubles
