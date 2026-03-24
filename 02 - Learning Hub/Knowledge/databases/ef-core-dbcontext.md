---
tags:
  - databases
  - dotnet
  - from/practice
  - status/learned
  - project/p1-notification
aliases:
  - DbContext
  - AppDbContext
  - Entity Framework DbContext
created: 2026-03-24
updated: 2026-03-24
source: "Architect Quest P1 - NotificationService W4 + Senior Engineer P1 - TaskManager"
---

# DbContext (EF Core)

> **One-liner:** Il DbContext è la classe principale di EF Core — è il ponte tra le tue Entity C# e il database relazionale.

## Cos'è

Il DbContext è il cuore di Entity Framework Core. Ha **3 responsabilità**:

1. **DbSet\<T\>** — espone le Entity come collezioni queryabili (traducono LINQ in SQL)
2. **Change Tracking** — traccia lo stato di ogni Entity in memoria (Added, Modified, Deleted, Unchanged)
3. **SaveChangesAsync** — genera le query SQL basandosi sugli stati tracciati e le esegue in una **transazione atomica**

```csharp
public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<TaskItem> TaskItems => Set<TaskItem>();
    public DbSet<Notification> Notifications => Set<Notification>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Carica TUTTE le Entity Configurations dall'assembly
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(AppDbContext).Assembly);
    }
}
```

### Change Tracker — come funziona

Il Change Tracker **non rilegge il DB** per confrontare. Traccia lo stato delle Entity **in memoria**:

```
repository.Add(entity)     → stato: Added     → INSERT
entity.Title = "nuovo"     → stato: Modified   → UPDATE
repository.Delete(entity)  → stato: Deleted    → DELETE
nessuna modifica            → stato: Unchanged  → niente SQL
```

Quando chiami `SaveChangesAsync()`:
1. EF Core legge gli stati dal Change Tracker
2. Genera le query SQL corrispondenti
3. Le esegue in una **transazione** — tutto o niente
4. Se fallisce → ROLLBACK automatico

### OnModelCreating e Entity Configurations

`OnModelCreating` è dove dici a EF Core **come** mappare Entity su tabelle. Ma se metti tutto lì, con 10 Entity diventa un God Method di 500+ righe.

La soluzione: **Entity Configurations** — una classe separata per Entity, ognuna con la propria mappatura:

```csharp
// Una classe per Entity — rispetta SRP
public class NotificationConfiguration : IEntityTypeConfiguration<Notification>
{
    public void Configure(EntityTypeBuilder<Notification> builder)
    {
        builder.HasKey(n => n.Id);
        builder.Property(n => n.Title).IsRequired().HasMaxLength(200);
        // Value Objects, relazioni, indici...
    }
}
```

`ApplyConfigurationsFromAssembly` le trova e le applica tutte automaticamente.

## Quando usarlo

- **Sempre** in applicazioni .NET che parlano con un DB relazionale
- Quando vuoi un ORM che gestisce Change Tracking, migrazioni, LINQ-to-SQL
- In Clean Architecture: vive in **Infrastructure** (è un dettaglio di persistenza)

## Quando NON usarlo

- Per query di reporting su milioni di record → Dapper è più performante (SQL puro)
- Se il progetto è molto semplice e non serve un ORM
- Non usarlo mai come **Singleton** — deve essere **Scoped** (uno per HTTP request)

### Perché Scoped e non Singleton?

Se fosse Singleton:
- Il Change Tracker accumulerebbe Entity di **tutte** le request
- Consumo di memoria crescente
- Conflitti tra utenti concorrenti che modificano le stesse Entity
- Un request che fallisce potrebbe "sporcare" lo stato per gli altri

Scoped = un'istanza per HTTP request = Change Tracker pulito ogni volta.

## Dove vive in Clean Architecture

```
Domain         → Entity, Value Objects (no dipendenze)
Application    → IUnitOfWork (interfaccia)
Infrastructure → AppDbContext : DbContext, IUnitOfWork (implementazione)
API            → Registrazione DI (services.AddDbContext<AppDbContext>)
```

Il DbContext può implementare `IUnitOfWork` direttamente — ha già `SaveChangesAsync()`. Se domani cambi ORM (es. Dapper), cambi solo l'implementazione; Application non sa nulla.

## Collegamenti

- [[patterns/repository-pattern|Repository Pattern]] — il repository usa il DbContext internamente
- [[patterns/unit-of-work-pattern|Unit of Work]] — SaveChangesAsync è il pattern UoW
- [[architecture/clean-architecture-principles|Clean Architecture]] — dove vive ogni pezzo
- [[solid/dependency-inversion-principle|DIP]] — perché Application definisce IUnitOfWork, non Infrastructure

## Quiz

### Q1: Cosa fa il Change Tracker?

Traccia lo stato delle Entity in memoria o confronta il DB ad ogni operazione?

**Mia risposta:** Traccia lo stato delle Entity in memoria.

✅ **Corretto** - Non rilegge mai il DB per confrontare. Traccia Added/Modified/Deleted/Unchanged in memoria e genera SQL solo al SaveChanges.

---

### Q2: Perché il DbContext deve essere Scoped?

Cosa succede se lo registri come Singleton nel DI container?

**Mia risposta:** Perché se lo registro come Singleton non vive "ad ogni diversa richiesta HTTP", ma per tutto il ciclo di vita dell'applicazione. Non rispetterebbe REST. Avrebbe chissà quanti conflitti in memoria.

✅ **Corretto** - Singleton = Change Tracker che accumula Entity di tutte le request, memoria crescente, conflitti tra utenti concorrenti.

---

### Q3: OnModelCreating con 15 Entity — qual è il problema e come lo risolvi?

**Mia risposta:** Significa che abbiamo una God Class. Meglio risolvere spezzando le mappature delle Entity con le configurazioni delle Entity (IEntityTypeConfiguration).

✅ **Corretto** - God Method da 500+ righe → una classe IEntityTypeConfiguration<T> per Entity, caricate con ApplyConfigurationsFromAssembly. SRP rispettato.

---

### Q4: AppDbContext implementa IUnitOfWork. Perché è una buona decisione architetturale?

**Mia risposta:** Perché se cambio EFCore domani per qualsiasi altra tecnologia mi basta modificare la DI e non spaccare tutto.

✅ **Corretto** - L'Application dipende da IUnitOfWork (interfaccia), non da AppDbContext. Cambio ORM = cambio solo l'implementazione in Infrastructure + registrazione DI. Zero modifiche nei layer superiori.

---
