---
tags:
  - patterns
  - domain
  - value-object
  - from/senior-p1-week-01
  - status/learning
aliases:
  - Enumeration Class
  - Type-Safe Enum
created: 2026-03-02
source: "Sessione Senior P1 Week 1"
---
1
# Smart Enum (Enumeration Class)

> **One-liner:** Un pattern che combina la type-safety degli enum con la flessibilità delle classi (metodi, validazione, comportamento).

## Cos'è

Uno **Smart Enum** è una classe che simula un enum ma con superpoteri:
- Ha un set **fisso** di istanze predefinite (come enum)
- Ogni istanza è un **oggetto vero** (può avere metodi, proprietà, logica)
- Il costruttore è **privato** (nessuno può creare istanze arbitrarie)
- Le istanze sono **static readonly** (create una volta dal CLR)

### Struttura Base

```csharp
public class Priority
{
    // Istanze predefinite (il "set fisso" di valori)
    public static readonly Priority Low = new Priority("Low", 1);
    public static readonly Priority Medium = new Priority("Medium", 2);
    public static readonly Priority High = new Priority("High", 3);
    public static readonly Priority Critical = new Priority("Critical", 4);

    // Stato interno
    public string Name { get; }
    public int Value { get; }

    // Costruttore PRIVATO - impossibile fare "new Priority()" da fuori
    private Priority(string name, int value)
    {
        Name = name;
        Value = value;
    }

    // Comportamento! (impossibile con enum normale)
    public bool IsUrgent() => Value >= 3;

    public override string ToString() => Name;
}
```

### Quando vengono create le istanze?

Il **CLR** (runtime .NET) le crea automaticamente la **prima volta** che qualcuno accede alla classe:

```
App parte → Priority non esiste in memoria
    ↓
Qualcuno scrive: var p = Priority.High;
    ↓
CLR inizializza TUTTI i campi static readonly
    ↓
Da ora in poi, Priority.High restituisce sempre la STESSA istanza
```

**Non c'è un punto esplicito nel codice dove "inizializzi" - è automatico.**

## Quando usarlo

| Situazione | Usa Smart Enum |
|------------|----------------|
| Serve **comportamento** associato ai valori | ✅ |
| Serve **validazione** custom | ✅ |
| Valori devono essere **comparabili** con logica | ✅ |
| Vuoi **factory methods** (`FromString`, `FromValue`) | ✅ |
| Set di valori fisso ma con **logica di business** | ✅ |

### Esempi reali

```csharp
// Priority con metodi
Priority.High.IsUrgent();              // true
Priority.Low.CompareTo(Priority.High); // -1

// Status con transizioni valide
OrderStatus.Pending.CanTransitionTo(OrderStatus.Shipped); // true
OrderStatus.Delivered.CanTransitionTo(OrderStatus.Pending); // false

// PaymentMethod con logica
PaymentMethod.CreditCard.CalculateFee(100m); // 2.50m
PaymentMethod.BankTransfer.CalculateFee(100m); // 0.50m
```

## Quando NON usarlo

| Situazione | Usa invece |
|------------|------------|
| Solo valori senza comportamento | `enum` normale |
| Valori dinamici (da database) | Entity o lookup table |
| Troppe varianti (50+) | Probabilmente il design è sbagliato |
| Performance critica (hot path) | `enum` (più leggero) |

### Enum normale è sufficiente quando:

```csharp
// Nessun comportamento, solo etichetta
public enum Color { Red, Green, Blue }

// Nessuna logica associata
public enum FileType { Pdf, Doc, Txt }
```

## Esempio Completo

```csharp
public class Priority : IEquatable<Priority>, IComparable<Priority>
{
    // === ISTANZE PREDEFINITE ===
    public static readonly Priority Low = new("Low", 1);
    public static readonly Priority Medium = new("Medium", 2);
    public static readonly Priority High = new("High", 3);
    public static readonly Priority Critical = new("Critical", 4);

    // === STATO ===
    public string Name { get; }
    public int Value { get; }

    // === COSTRUTTORE PRIVATO ===
    private Priority(string name, int value)
    {
        Name = name;
        Value = value;
    }

    // === COMPORTAMENTO ===
    public bool IsUrgent() => Value >= 3;

    // === FACTORY METHODS ===
    public static Priority FromString(string name)
    {
        return name.ToLowerInvariant() switch
        {
            "low" => Low,
            "medium" => Medium,
            "high" => High,
            "critical" => Critical,
            _ => throw new ArgumentException($"Invalid priority: {name}")
        };
    }

    public static Priority FromValue(int value)
    {
        return value switch
        {
            1 => Low,
            2 => Medium,
            3 => High,
            4 => Critical,
            _ => throw new ArgumentException($"Invalid priority value: {value}")
        };
    }

    // === EQUALITY ===
    public bool Equals(Priority? other) => other is not null && Value == other.Value;
    public override bool Equals(object? obj) => Equals(obj as Priority);
    public override int GetHashCode() => Value.GetHashCode();

    public static bool operator ==(Priority? left, Priority? right)
        => left?.Equals(right) ?? right is null;
    public static bool operator !=(Priority? left, Priority? right)
        => !(left == right);

    // === COMPARISON ===
    public int CompareTo(Priority? other) => other is null ? 1 : Value.CompareTo(other.Value);

    public static bool operator <(Priority left, Priority right) => left.CompareTo(right) < 0;
    public static bool operator >(Priority left, Priority right) => left.CompareTo(right) > 0;

    // === TO STRING ===
    public override string ToString() => Name;
}
```

## Confronto: Enum vs Smart Enum

| Aspetto | `enum` | Smart Enum |
|---------|--------|------------|
| Type safety | ✅ | ✅ |
| Metodi custom | ❌ | ✅ |
| Validazione | ❌ | ✅ |
| Factory methods | ❌ | ✅ |
| Equality custom | ❌ | ✅ |
| Peso in memoria | Leggero (int) | Oggetto |
| Serializzazione | Automatica | Da implementare |

## Librerie esistenti

Se non vuoi implementarlo a mano:

```bash
dotnet add package Ardalis.SmartEnum
```

```csharp
public class Priority : SmartEnum<Priority>
{
    public static readonly Priority Low = new(nameof(Low), 1);
    public static readonly Priority High = new(nameof(High), 3);

    private Priority(string name, int value) : base(name, value) { }
}
```

## Collegamenti

- [[value-objects]] - Smart Enum è un tipo di Value Object
- [[factory-pattern]] - I factory methods sono un'alternativa
- [[ddd-building-blocks]] - Fa parte dei building blocks DDD

## Quiz

### Q1: Costruttore pubblico o privato?
Perché il costruttore di uno Smart Enum deve essere **privato**?

<details>
<summary>Risposta</summary>

Perché vogliamo un **set fisso** di valori. Se il costruttore fosse pubblico, chiunque potrebbe fare `new Priority("SuperHigh", 99)` e creare valori non previsti, rompendo la garanzia che esistano solo Low, Medium, High, Critical.

</details>

### Q2: Quando usa il CLR per creare le istanze?
Quando vengono effettivamente costruite le istanze `Priority.Low`, `Priority.High`, etc.?

<details>
<summary>Risposta</summary>

La **prima volta** che qualcuno accede alla classe `Priority`. Il CLR inizializza tutti i campi `static readonly` in quel momento. Non c'è un punto esplicito nel codice - è automatico.

</details>

### Q3: Enum normale vs Smart Enum
Quando useresti un `enum` normale invece di uno Smart Enum?

<details>
<summary>Risposta</summary>

Quando non serve comportamento associato ai valori. Se hai solo bisogno di etichette type-safe senza metodi (es. `Color { Red, Green, Blue }`), un enum normale è più semplice e leggero.

</details>

---

## Risorse per Approfondire

- **[Jimmy Bogard - Smart Enum](https://lostechies.com/jimmybogard/2008/08/12/enumeration-classes/)** - L'articolo originale del pattern
- **[Ardalis.SmartEnum GitHub](https://github.com/ardalis/SmartEnum)** - Libreria NuGet popolare
- **[Microsoft Docs - Enumeration Classes](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/enumeration-classes-over-enum-types)** - Documentazione ufficiale

---

*Creato durante: Senior P1 Week 1 - Task Manager*
