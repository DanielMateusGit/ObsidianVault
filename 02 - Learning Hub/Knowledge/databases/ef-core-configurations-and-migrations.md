---
tags:
  - databases
  - dotnet
  - from/practice
  - status/learning
  - project/p1-taskmanager
aliases:
  - Entity Configurations
  - EF Core Migrations
  - IEntityTypeConfiguration
  - Fluent API
created: 2026-05-07
updated: 2026-05-07
source: "Senior Engineer P1 - TaskManager M2 (Infrastructure setup + Integration Tests session)"
---

# EF Core — Entity Configurations & Migrations

> **One-liner:** Le **Entity Configurations** descrivono come le entità del Domain vengono mappate alle tabelle del DB; le **Migrations** sono codice C# auto-generato che traduce queste configurazioni in operazioni SQL eseguibili.

## Cos'è

EF Core decide la struttura di ogni colonna del DB consultando **3 fonti**, in ordine di priorità crescente:

```
   ┌─────────────────────────────────────────┐
1. │ Conventions (default di EF Core)        │  ← sempre presenti, più deboli
   │  property "Id" → primary key             │
   │  string → varchar senza limiti           │
   │  DbSet<TaskItem> → tabella "TaskItems"   │
   └─────────────────────────────────────────┘
                    ▼ override da ▼
   ┌─────────────────────────────────────────┐
2. │ Data Annotations (attributi sulla classe)│  ← inquinano il Domain, evitare
   │  [Required] [MaxLength(100)]             │
   │  public string Title { get; set; }       │
   └─────────────────────────────────────────┘
                    ▼ override da ▼
   ┌─────────────────────────────────────────┐
3. │ Fluent API in IEntityTypeConfiguration  │  ← scelta canonica ✅
   │  builder.Property(t => t.Title)          │
   │      .HasMaxLength(100).IsRequired();    │
   └─────────────────────────────────────────┘
```

**Perché Fluent API è la scelta giusta in Clean Architecture:** mantiene il Domain **puro** — le entity non sanno (e non devono sapere) che verranno persistite. Tutta la logica di mapping vive in `Infrastructure/Persistence/Configurations/`.

### IEntityTypeConfiguration\<T\>

Una classe per entità, ognuna implementa `Configure(EntityTypeBuilder<T> builder)`:

```csharp
// Infrastructure/Persistence/Configurations/TaskItemConfiguration.cs
public class TaskItemConfiguration : IEntityTypeConfiguration<TaskItem>
{
    public void Configure(EntityTypeBuilder<TaskItem> builder)
    {
        builder.Property(t => t.Title).HasMaxLength(100).IsRequired();
        builder.Property(t => t.Priority).HasConversion(
            priority => priority.Value,         // Priority → int (write)
            value => Priority.FromValue(value)  // int → Priority (read)
        );
        builder.Property(t => t.CreatedAt).IsRequired();
        builder.Ignore(t => t.DomainEvents);    // NON è una colonna
    }
}
```

Caricate automaticamente in `OnModelCreating` con:
```csharp
modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
```

### Cosa è una Migration

Una migration è un **file C# auto-generato** che contiene operazioni SQL espresse come metodi `MigrationBuilder`:

```csharp
public partial class InitialCreate : Migration
{
    protected override void Up(MigrationBuilder mb)    // forward
    {
        mb.CreateTable(name: "TaskItems", columns: table => new {
            Id = table.Column<Guid>(type: "uuid", nullable: false),
            Title = table.Column<string>(type: "character varying(100)",
                                         maxLength: 100, nullable: false),
            // ...
        });
    }

    protected override void Down(MigrationBuilder mb)  // rollback
    {
        mb.DropTable(name: "TaskItems");
    }
}
```

**Non è un commento, non è "documentazione".** È codice eseguibile, compilato nell'assembly, che EF Core esegue per evolvere lo schema del DB.

### Come EF Core GENERA una migration

Quando lanci `dotnet ef migrations add NomeMigration`, EF Core:

1. **Costruisce il modello in memoria** leggendo:
   - DbSet\<T\> in AppDbContext
   - Le classi entity (TaskItem, Project, Tag)
   - Le conventions di default
   - Le tue IEntityTypeConfiguration (Fluent API)
2. **Confronta** il modello con il **Model Snapshot** (`AppDbContextModelSnapshot.cs` — la "memoria" dell'ultima migration)
3. **Calcola la diff** (cosa è cambiato)
4. **Genera** il file di migration con le operazioni `Up()`/`Down()` corrispondenti
5. **Aggiorna** il Model Snapshot per la prossima volta

Migration applicata = SQL eseguito sul DB target (qualunque esso sia: prod, staging, test container).

## Quando usarlo

- **Sempre** in progetti EF Core: ogni cambiamento di schema deve passare per una migration tracciata in git.
- Quando devi propagare modifiche (nuova colonna, nuova FK, indice, vincolo) tra dev/staging/prod in modo riproducibile.
- Quando vuoi un audit trail dello schema (ogni migration ha un timestamp, un autore implicito via git, una storia).

## Quando NON usarlo

- **Mai modificare uno schema in produzione con SQL ad-hoc** che non passi da una migration → si crea drift tra l'aspettativa di EF e la realtà del DB.
- **Mai editare a mano una migration già applicata in altri ambienti** → invece, crea una nuova migration "fix-X" che corregge.
- Non usare le Migrations come "data seeding" pesante — per dati iniziali grandi usa script SQL separati o tool dedicati (es. `dotnet ef migrations` per schema, separate seeding scripts per dati).
- Non confondere `EnsureCreatedAsync()` con `MigrateAsync()`: il primo costruisce lo schema **bypassando le migrations** (utile solo per prototipi); il secondo le applica davvero (l'unico approccio production-grade e da usare anche nei test integration).

## Esempio — Flusso completo: aggiungere una colonna

Supponi di voler aggiungere `Description` (max 500 char, nullable) a `TaskItem`.

### Step 1 — Modifica l'entity (Domain)
```csharp
// Domain/Entities/TaskItem.cs
public class TaskItem
{
    public string? Description { get; private set; }   // ← aggiunto
    // ... resto invariato
    public void UpdateDescription(string? d) => Description = d;
}
```

### Step 2 — Modifica la Configuration (Infrastructure)
```csharp
public class TaskItemConfiguration : IEntityTypeConfiguration<TaskItem>
{
    public void Configure(EntityTypeBuilder<TaskItem> builder)
    {
        builder.Property(t => t.Title).HasMaxLength(100).IsRequired();
        builder.Property(t => t.Description).HasMaxLength(500);  // ← aggiunto
        // ... resto invariato
    }
}
```

### Step 3 — Genera la migration
```bash
dotnet ef migrations add AddDescriptionToTaskItem \
    -p src/TaskManager.Infrastructure \
    -s src/TaskManager.Api
```

EF Core legge il modello, confronta con lo snapshot, calcola la diff. Genera:

```csharp
public partial class AddDescriptionToTaskItem : Migration
{
    protected override void Up(MigrationBuilder mb)
    {
        mb.AddColumn<string>(
            name: "Description",
            table: "TaskItems",
            type: "character varying(500)",
            maxLength: 500,
            nullable: true);
    }

    protected override void Down(MigrationBuilder mb)
    {
        mb.DropColumn(name: "Description", table: "TaskItems");
    }
}
```

### Step 4 — Applica
```bash
dotnet ef database update \
    -p src/TaskManager.Infrastructure \
    -s src/TaskManager.Api
```

Oppure a runtime: `await DbContext.Database.MigrateAsync();` (è ciò che fa `PostgresFixture` nei test).

### Mappa visiva del flusso
```
Domain entity (TaskItem)            "shape che il business usa"
        ▼
IEntityTypeConfiguration            "regole di persistenza"
        ▼
ApplyConfigurationsFromAssembly     "registra tutte le configurations"
        ▼
┌────────────────────────────┐
│ EF Core costruisce MODEL   │   ← in memoria, ad ogni avvio
└────────────────────────────┘
        │
        ├── confronto con Snapshot ──► dotnet ef migrations add → file migration
        │
        └── usato a runtime per ──────► tradurre LINQ in SQL, materializzare entities
```

## Collegamenti

- [[databases/ef-core-dbcontext|DbContext (EF Core)]] — la classe che orchestra tutto
- [[patterns/repository-pattern|Repository Pattern]] — come incapsulare le query EF
- [[patterns/unit-of-work-pattern|Unit of Work]] — perché Repository non chiama SaveChanges
- [[architecture/clean-architecture-principles|Clean Architecture]] — perché Configurations vivono in Infrastructure
- [[solid/single-responsibility-principle|SRP]] — una Configuration per entity, non un God Method

## Quiz

### Q1: Le 3 fonti di regole per le colonne del DB

EF Core decide il tipo, la nullability e i constraint di una colonna consultando 3 fonti. Quali sono, in ordine di priorità crescente?

**Mia risposta:** 1) Conventions di default di EF Core, 2) Data Annotations come `[Required]` e `[MaxLength]` sulle property dell'entity, 3) Fluent API tramite `IEntityTypeConfiguration<T>` — la più potente perché tiene il Domain pulito.

✅ **Corretto** - Conventions < Data Annotations < Fluent API. La scelta canonica in Clean Architecture è Fluent API perché evita di "sporcare" il Domain con attributi EF-specifici. Le Data Annotations vanno bene per progetti veloci/CRUD ma rompono la separazione di concerns appena il Domain cresce.

---

### Q2: Cosa succede quando lanci `dotnet ef migrations add Foo`?

Descrivi il processo che porta dalla tua modifica dell'entity al file `.cs` di migration generato.

**Mia risposta:** EF Core costruisce il modello in memoria leggendo DbSet, entity classes, conventions e Configurations. Poi confronta questo modello con l'AppDbContextModelSnapshot (la memoria dell'ultima migration). Calcola la diff e genera il file di migration con i metodi `Up()` e `Down()` corrispondenti. Aggiorna anche lo snapshot per la prossima volta.

✅ **Corretto** - Esatto. Il punto chiave è: la migration è un **diff** tra due stati del modello. Senza lo snapshot, EF non saprebbe cosa è cambiato — proverebbe a ricreare tutto da zero.

---

### Q3: Una migration è un commento o è codice eseguibile?

Spiega la differenza e cosa contiene una tipica migration.

**Mia risposta:** Una migration è codice C# vero e proprio, compilato nell'assembly. Contiene due metodi: `Up()` con le operazioni per andare avanti (es. `CreateTable`, `AddColumn`) e `Down()` per il rollback (es. `DropTable`, `DropColumn`). EF Core la esegue quando lanci `dotnet ef database update` o quando il codice chiama `Database.MigrateAsync()`. L'unico "commento" è il nome (`AddDescriptionToTaskItem`) — descrittivo ma non funzionale.

✅ **Corretto** - Le migration sono codice. Pinned in git, versionate, applicate in ordine timestamp. Il nome descrittivo è solo per readability — EF identifica le migrations dal timestamp + classe, non dal nome.

---

### Q4: `EnsureCreatedAsync()` vs `MigrateAsync()` — quale usare nei test integration?

Hai un Postgres container fresco. Devi creare lo schema. Quale dei due metodi usi e perché?

**Mia risposta:** Uso `MigrateAsync()`. `EnsureCreatedAsync()` costruisce lo schema bypassando le migrations — utile per prototipi velocissimi, ma se domani le migrations hanno un bug (es. il nome di una colonna, un constraint mancante) i test non lo catturerebbero perché stanno costruendo lo schema in modo diverso dalla produzione. `MigrateAsync()` esegue le stesse migrations che girano in prod → realistico, e testa anche le migrations stesse.

✅ **Corretto** - Regola d'oro: **test e produzione devono passare per lo stesso percorso**. `EnsureCreatedAsync` lo rompe; `MigrateAsync` lo rispetta. Bonus: se aggiungi una migration buggy e i test girano con `MigrateAsync`, il test che era verde diventa rosso → bug catturato prima del deploy.

---

## Ti è piaciuto parlare di EF Core Migrations? Allora impazzirai per:

- [Microsoft Learn — EF Core migrations overview](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/) — il riferimento ufficiale, ben scritto, copre anche scenari avanzati (multi-context, custom operations).
- [Migrations gotchas — Andrew Lock](https://andrewlock.net/series/an-introduction-to-entity-framework-core-migrations/) — serie di articoli su edge case (ridenominazione colonna, data seeding, ambienti multipli).
