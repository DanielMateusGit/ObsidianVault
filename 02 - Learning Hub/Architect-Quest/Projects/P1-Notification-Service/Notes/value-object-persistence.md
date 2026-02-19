---
tags:
  - p1
  - infrastructure
  - ef-core
  - ddd
  - value-objects
  - from/week-04
  - status/learned
aliases:
  - Owned Types
  - Value Object Persistence
  - EF Core Owned Types
created: 2026-02-19
source: "Sessione Week 4 - Infrastructure Layer"
---

# Value Object Persistence con Owned Types

> **One-liner:** EF Core Owned Types permettono di persistere Value Objects come colonne nella tabella dell'entity owner, mantenendo la separazione concettuale del Domain.

## Cos'è

Un **Owned Type** in EF Core è un tipo che:
- Non ha identità propria (no `Id`)
- "Appartiene" a un'entity (non può esistere da solo)
- Viene salvato nella **stessa tabella** dell'entity owner

```
┌─────────────────────────────────────────────────────────────────┐
│  TABELLA: notifications                                         │
│                                                                 │
│  id | content | recipient_value | recipient_channel | ...       │
│                │                 │                              │
│                └─────────────────┴── Da Recipient (Owned Type)  │
└─────────────────────────────────────────────────────────────────┘
```

### Owned Type vs Value Converter

| Approccio | Come Funziona | Quando Usarlo |
|-----------|---------------|---------------|
| **Value Converter** | `EmailAddress ↔ string` | VO con singola proprietà |
| **Owned Type** | VO → multiple colonne | VO con più proprietà |

## Quando usarlo

| Situazione | Usa Owned Types |
|------------|-----------------|
| Value Object con 2+ proprietà | ✅ |
| VO che appartiene a una sola entity | ✅ |
| Vuoi colonne nella stessa tabella | ✅ |
| Vuoi mantenere la modellazione DDD | ✅ |

## Quando NON usarlo

| Situazione | Perché | Alternativa |
|------------|--------|-------------|
| VO con singola proprietà string | Over-engineering | Value Converter |
| VO usato come FK | Owned non supporta FK | Entity separata |
| Collection di VO | Più complesso | `OwnsMany` con tabella separata |

## Esempio

### Value Object nel Domain

```csharp
// Domain/ValueObjects/Recipient.cs
public class Recipient
{
    public string Value { get; }
    public NotificationChannel Channel { get; }
    public EmailAddress? Email { get; }
    public PhoneNumber? Phone { get; }

    // Factory methods: ForEmail(), ForSms(), etc.
}
```

### Entity che usa il VO

```csharp
// Domain/Entities/Notification.cs
public class Notification : Entity
{
    public Guid Id { get; private set; }
    public Recipient Recipient { get; private set; }  // Value Object!
    public string Content { get; private set; }
    // ...
}
```

### Configurazione EF Core

```csharp
// Infrastructure/Persistence/Configurations/NotificationConfiguration.cs
public void Configure(EntityTypeBuilder<Notification> builder)
{
    builder.ToTable("notifications");

    // Owned Type per Recipient
    builder.OwnsOne(n => n.Recipient, recipient =>
    {
        recipient.Property(r => r.Value)
            .HasColumnName("recipient_value")
            .HasMaxLength(500)
            .IsRequired();

        recipient.Property(r => r.Channel)
            .HasColumnName("recipient_channel")
            .HasConversion<string>()
            .HasMaxLength(50)
            .IsRequired();

        // Ignora le proprietà di navigazione interne
        recipient.Ignore(r => r.Email);
        recipient.Ignore(r => r.Phone);
    });
}
```

### Risultato nel Database

```sql
CREATE TABLE notifications (
    id UUID PRIMARY KEY,
    recipient_value VARCHAR(500) NOT NULL,
    recipient_channel VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    -- altre colonne...
);
```

## Requisiti EF Core per Owned Types

1. **Costruttore privato senza parametri** - EF Core deve poter creare l'oggetto
2. **Proprietà con setter privato** - EF Core deve poter impostare i valori

```csharp
public class Recipient
{
    // Per EF Core
    private Recipient() { }

    public string Value { get; private set; }
    public NotificationChannel Channel { get; private set; }
}
```

## Collegamenti

- [[repository-pattern]] - I repository persistono entity con Owned Types
- [[ef-core-migrations]] - Le migrations generano le colonne per Owned Types
- [[infrastructure-layer]] - Owned Types sono configurati in Infrastructure

## Domande dalla Sessione

### D: Differenza tra Owned Type e Value Converter?
**R:**
- **Value Converter**: Converte un tipo a un altro (es. `EmailAddress → string`). Una colonna.
- **Owned Type**: Il VO genera più colonne nella tabella dell'entity owner. Mantiene la struttura del VO.

### D: Cosa cambia nella tabella con Owned Types?
**R:** Le proprietà del Value Object diventano colonne nella tabella dell'entity. Se `Recipient` ha `Value` e `Channel`, la tabella avrà `recipient_value` e `recipient_channel`.

### D: Perché scegliere Owned Types?
**R:** Migliore modellazione DDD, type safety, separazione concettuale. Il database riflette la struttura del Domain.

## Quiz

### Q1: Owned Type vs Entity
Un collega suggerisce di creare una tabella separata `recipients` con FK. Perché Owned Type è meglio per un Value Object?

<details>
<summary>Risposta</summary>

I Value Objects **non hanno identità** - non dovrebbero avere una tabella propria con PK. Owned Types rispettano questo principio: il VO viene salvato come colonne nell'entity owner, senza identità propria.

Una tabella separata con FK implica identità, che viola la definizione di Value Object.
</details>

### Q2: Costruttore Privato
Perché EF Core richiede un costruttore privato senza parametri per gli Owned Types?

<details>
<summary>Risposta</summary>

EF Core deve **materializzare** gli oggetti quando legge dal database. Non può usare i factory methods o costruttori con validazione. Il costruttore privato permette a EF di creare l'oggetto e poi impostare le proprietà via reflection.

Il costruttore è `private` per non esporlo all'uso normale - solo EF lo usa.
</details>

### Q3: Ignore delle proprietà
Perché facciamo `recipient.Ignore(r => r.Email)` nella configurazione?

<details>
<summary>Risposta</summary>

`Email` e `Phone` sono proprietà calcolate/derivate del Recipient che non vogliamo salvare nel database. Contengono riferimenti ad altri Value Objects che servono solo a runtime.

Salviamo solo `Value` e `Channel` - da questi possiamo ricostruire `Email`/`Phone` quando serve.
</details>

---

## Risorse per Approfondire

- **[EF Core Owned Types - Official Docs](https://learn.microsoft.com/en-us/ef/core/modeling/owned-entities)** - Documentazione completa
- **[Value Objects in DDD - Martin Fowler](https://martinfowler.com/bliki/ValueObject.html)** - Definizione pattern
- **[Implementing Value Objects - Vladimir Khorikov](https://enterprisecraftsmanship.com/posts/value-objects-ef-core/)** - Best practices con EF Core

---

*Ultimo aggiornamento: 2026-02-19*
