---
tags:
  - p1
  - infrastructure
  - testing
  - testcontainers
  - integration-tests
  - from/week-04
  - status/learning
aliases:
  - Integration Tests
  - Testcontainers
  - Repository Tests
created: 2026-02-19
source: "Sessione Week 4 - Infrastructure Layer"
---

# Integration Tests con Testcontainers

> **One-liner:** Testcontainers avvia container Docker temporanei per testare i repository con un database PostgreSQL reale, garantendo che EF Core e le migrations funzionino correttamente.

## Cos'è

Un **integration test** verifica che più componenti funzionino insieme correttamente. Nel nostro caso: Repository + EF Core + PostgreSQL.

**Testcontainers** è una libreria che:
- Avvia container Docker temporanei per i test
- Fornisce connection string dinamiche
- Distrugge i container dopo i test
- Garantisce isolamento tra test run

```
Test Start → Docker avvia PostgreSQL → Migrations → Test → Container distrutto
```

## Unit Test vs Integration Test

| Aspetto | Unit Test | Integration Test |
|---------|-----------|------------------|
| **Cosa testa** | Logica in isolamento | Componenti insieme |
| **Database** | Mock (NSubstitute) | PostgreSQL reale |
| **Velocità** | Millisecondi | Secondi |
| **Trova** | Bug di logica | Bug di configurazione |
| **Esempio** | `Notification.Send()` | `Repository.AddAsync()` |

## Quando usarlo

| Situazione | Tipo Test |
|------------|-----------|
| Logica di business pura (Entity methods) | Unit Test |
| Repository CRUD operations | **Integration Test** |
| Query LINQ complesse | **Integration Test** |
| Verificare che migrations funzionano | **Integration Test** |
| Owned Types / Value Converters | **Integration Test** |
| Transazioni | **Integration Test** |

## Perché NON usare InMemory Provider

EF Core ha un provider InMemory, ma:

| InMemory | PostgreSQL Reale |
|----------|------------------|
| Non valida SQL | Valida SQL reale |
| Ignora constraint | Applica constraint |
| LINQ diverso | LINQ tradotto in SQL |
| No transazioni vere | Transazioni reali |
| Comportamento diverso | Stesso comportamento di prod |

**Regola:** Testa con lo stesso database che usi in produzione.

## Esempio

### Setup Test Fixture

```csharp
public class DatabaseFixture : IAsyncLifetime
{
    private PostgreSqlContainer _postgres = null!;
    public AppDbContext Context { get; private set; } = null!;

    public async Task InitializeAsync()
    {
        // Avvia PostgreSQL in Docker
        _postgres = new PostgreSqlBuilder()
            .WithImage("postgres:16-alpine")
            .Build();

        await _postgres.StartAsync();

        // Crea DbContext
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseNpgsql(_postgres.GetConnectionString())
            .Options;

        Context = new AppDbContext(options);
        await Context.Database.MigrateAsync();
    }

    public async Task DisposeAsync()
    {
        await Context.DisposeAsync();
        await _postgres.DisposeAsync();
    }
}
```

### Integration Test

```csharp
public class NotificationRepositoryTests : IClassFixture<DatabaseFixture>
{
    private readonly AppDbContext _context;
    private readonly PostgresNotificationRepository _repository;

    public NotificationRepositoryTests(DatabaseFixture fixture)
    {
        _context = fixture.Context;
        _repository = new PostgresNotificationRepository(_context);
    }

    [Fact]
    public async Task AddAsync_SavesNotificationToDatabase()
    {
        // Arrange
        var recipient = Recipient.ForEmail("test@example.com");
        var notification = new Notification(recipient, "Content", subject: "Subject");

        // Act
        await _repository.AddAsync(notification);
        await _context.SaveChangesAsync();

        // Assert - Verifica nel database reale!
        var saved = await _context.Notifications.FindAsync(notification.Id);
        Assert.NotNull(saved);
        Assert.Equal("test@example.com", saved.Recipient.Value);
        Assert.Equal(NotificationChannel.Email, saved.Recipient.Channel);
    }
}
```

## Pacchetti NuGet Necessari

```xml
<PackageReference Include="Testcontainers.PostgreSql" Version="3.x" />
<PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.x" />
```

## Best Practices

1. **Un container per classe di test** - Usa `IClassFixture` per condividere
2. **Pulisci tra test** - Ogni test deve partire da stato pulito
3. **Non troppi integration test** - Sono lenti, usa unit test per la logica
4. **CI/CD** - Assicurati che Docker sia disponibile nel CI

## Collegamenti

- [[repository-pattern]] - I repository che testiamo
- [[ef-core-migrations]] - Le migrations applicate nei test
- [[value-object-persistence]] - Owned Types verificati con integration test

## Domande dalla Sessione

### D: Perché non usare InMemory di EF Core?
**R:** InMemory non si comporta come un database reale: non valida SQL, ignora constraint, traduce LINQ diversamente. Testcontainers usa PostgreSQL reale = stesso comportamento di produzione.

### D: Bastano gli unit test?
**R:** No, testano aspetti diversi. Unit test = logica isolata. Integration test = componenti insieme. Servono entrambi.

### D: Cosa trova un integration test che un unit test non trova?
**R:** Bug di configurazione EF Core: Owned Types sbagliati, mapping colonne errato, query LINQ tradotte male in SQL.

## Quiz

### Q1: Container per test
Quale strategia usiamo per il container PostgreSQL nei test?

<details>
<summary>Risposta</summary>

Usiamo `IClassFixture<DatabaseFixture>` per **condividere un container** tra tutti i test della classe. Avviare un container per ogni test sarebbe troppo lento.

Il container viene avviato in `InitializeAsync` e distrutto in `DisposeAsync`.
</details>

### Q2: Migrations nei test
Perché chiamiamo `Database.MigrateAsync()` nel setup del test?

<details>
<summary>Risposta</summary>

Il container PostgreSQL parte **vuoto**. Dobbiamo applicare le migrations per creare le tabelle prima di poter testare i repository.

Questo verifica anche che le migrations funzionino correttamente!
</details>

### Q3: Isolamento tra test
Come garantiamo che un test non influenzi gli altri?

<details>
<summary>Risposta</summary>

Opzioni:
1. **Transaction rollback** - Ogni test in una transazione che viene rollbackata
2. **Pulizia esplicita** - Cancella i dati tra test
3. **Container separati** - Un container per test (lento)

L'approccio più comune è il transaction rollback o la pulizia esplicita.
</details>

---

## Risorse per Approfondire

- **[Testcontainers for .NET - Official Docs](https://dotnet.testcontainers.org/)** - Documentazione ufficiale
- **[Integration Testing with EF Core](https://learn.microsoft.com/en-us/ef/core/testing/)** - Microsoft Docs
- **[Testing Repository Pattern](https://www.youtube.com/watch?v=5SqzNQ1yZJQ)** - Video pratico

---

*Ultimo aggiornamento: 2026-02-19*
