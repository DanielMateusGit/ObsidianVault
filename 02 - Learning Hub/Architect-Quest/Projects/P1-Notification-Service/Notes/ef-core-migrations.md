---
tags:
  - p1
  - infrastructure
  - ef-core
  - database
  - from/week-04
  - status/learning
aliases:
  - EF Core Migrations
  - Database Migrations
  - Code-First Migrations
created: 2026-02-19
source: "Sessione Week 4 - Infrastructure Layer"
---

# EF Core Migrations

> **One-liner:** Sistema di versionamento dello schema database che genera automaticamente SQL dalle tue entity C#, permettendo rollback e storico delle modifiche.

## Cos'è

Le Migrations sono il sistema di EF Core per **versionare lo schema del database**. Invece di scrivere SQL a mano, definisci le entity in C# e EF Core genera le modifiche necessarie.

```
┌─────────────────────────────────────────────────────────────────┐
│                        MIGRATIONS                               │
│                                                                 │
│   1. Legge le tue Entity + Configurations                       │
│   2. Confronta con lo stato attuale del DB (ModelSnapshot)      │
│   3. Genera codice C# che descrive le modifiche                 │
│   4. Può generare SQL equivalente                               │
│   5. Applica le modifiche al database                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Struttura di una Migration

```csharp
public partial class InitialCreate : Migration
{
    // Cosa fare per APPLICARE la migration
    protected override void Up(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.CreateTable(
            name: "notifications",
            columns: table => new
            {
                id = table.Column<Guid>(nullable: false),
                recipient = table.Column<string>(maxLength: 500),
            },
            constraints: table =>
            {
                table.PrimaryKey("PK_notifications", x => x.id);
            });
    }

    // Cosa fare per ANNULLARE la migration (rollback)
    protected override void Down(MigrationBuilder migrationBuilder)
    {
        migrationBuilder.DropTable(name: "notifications");
    }
}
```

### Il ModelSnapshot

EF Core mantiene un file `ModelSnapshot.cs` che rappresenta lo stato **attuale** del modello. Quando crei una nuova migration, confronta:

```
Nuovo modello C#  vs  ModelSnapshot  =  Differenze da applicare
```

## Quando usarlo

| Situazione | Esempio |
|------------|---------|
| **Sviluppo iniziale** | `add InitialCreate` per creare tutte le tabelle |
| **Nuova colonna** | `add AddColumnX` |
| **Nuova entity** | `add AddEntityY` |
| **Modifica relazione** | `add UpdateRelationship` |
| **Team con Git** | Migrations versionati insieme al codice |

## Quando NON usarlo

| Situazione | Perché | Alternativa |
|------------|--------|-------------|
| **Database legacy esistente** | Rischio di conflitti | `Scaffold-DbContext` (reverse engineering) |
| **Dati sensibili in produzione** | Migrations possono fallire | Script SQL manuali + review |
| **Modifiche distruttive** | `DropColumn` perde dati | Backup + script manuale |
| **Performance critica** | EF genera SQL generico | SQL ottimizzato manuale |

## Esempio

### Comandi Principali

```bash
# Genera una nuova migration
dotnet ef migrations add NomeMigration --project Infrastructure --startup-project Api

# Applica tutte le migrations pendenti
dotnet ef database update --project Infrastructure --startup-project Api

# Genera SQL senza applicarlo (per review)
dotnet ef migrations script --project Infrastructure --startup-project Api

# Rimuove l'ultima migration (se non ancora applicata)
dotnet ef migrations remove --project Infrastructure --startup-project Api

# Rollback a una migration specifica
dotnet ef database update NomeMigration --project Infrastructure --startup-project Api
```

### Workflow Tipico

```
1. Modifica Entity/Configuration in C#
2. dotnet ef migrations add DescrizioneModifica
3. Controlla il file generato (Up e Down)
4. dotnet ef database update
5. Commit migration + codice insieme
```

## Collegamenti

- [[infrastructure-layer]] - Il layer dove vivono le migrations
- [[repository-pattern]] - I repository usano il DB creato dalle migrations
- [[clean-architecture]] - Le migrations sono un dettaglio di Infrastructure

## Domande dalla Sessione

### D: Perché le migrations sono meglio di scrivere SQL a mano?
**R:**
- **Automatico** - EF Core genera il SQL
- **Versionato** - Storico di tutte le modifiche
- **Rollback** - Puoi tornare indietro con Down()
- **Sincronizzato** - Lo stato del DB segue il codice C#
- **Team-friendly** - Migrations committate con il codice

### D: Cosa contiene Down() e quando viene eseguito?
**R:** Down() contiene le operazioni inverse di Up(). Viene eseguito quando fai rollback a una migration precedente con `database update NomeMigrationPrecedente`.

### D: Cosa succede se modifico una entity senza creare una migration?
**R:** L'app crasha! EF Core si aspetta colonne/tabelle che non esistono nel DB (schema mismatch). Errore tipico: `Invalid column name 'NuovaColonna'`.

## Quiz

### Q1: Migrations vs SQL manuale
Quali sono 3 vantaggi delle migrations rispetto a scrivere SQL a mano?

<details>
<summary>Risposta</summary>

1. **Automatico** - EF Core genera SQL dalle entity C#
2. **Versionato** - Storico completo delle modifiche allo schema
3. **Rollback** - Puoi tornare a versioni precedenti con Down()
4. **Sincronizzato** - DB e codice evolvono insieme
5. **Portabile** - Funziona con diversi database (PostgreSQL, SQL Server, etc.)
</details>

### Q2: Up e Down
Una migration ha questi metodi:
```csharp
Up()   { CreateTable("users"); }
Down() { ??? }
```

Cosa deve contenere Down()?

<details>
<summary>Risposta</summary>

```csharp
Down() { DropTable("users"); }
```

Down() deve contenere l'operazione **inversa** di Up(). Se Up() crea una tabella, Down() la elimina. Questo permette il rollback.
</details>

### Q3: Schema Mismatch
Aggiungi una proprietà `Priority` a Notification ma dimentichi di creare la migration. Cosa succede?

<details>
<summary>Risposta</summary>

**L'app crasha** quando prova a usare Notification. EF Core genera query SQL con la colonna `priority`, ma questa non esiste nel database.

Errore tipico: `Npgsql.PostgresException: column "priority" does not exist`

Soluzione: `dotnet ef migrations add AddPriorityColumn` + `dotnet ef database update`
</details>

---

## Risorse per Approfondire

- **[EF Core Migrations - Official Docs](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/)** - Guida completa Microsoft
- **[Migrations in Team Environments](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/teams)** - Come gestire migrations con Git
- **[Applying Migrations at Runtime](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying)** - Quando applicare: startup vs deploy script

---

*Ultimo aggiornamento: 2026-02-19*
