---
tags:
  - ddd
  - entity
  - domain
  - from/senior-p1-week-01
  - status/learning
aliases:
  - Task Entity
  - Entity Pattern
created: 2026-03-03
source: "Sessione Senior P1 Week 1"
---

# TaskItem Entity

> **One-liner:** Un'Entity è un oggetto con identità univoca, stato mutabile e comportamento che protegge le invarianti di business.

## Cos'è un'Entity

Un'Entity è diversa da un Value Object:

| Aspetto | Value Object | Entity |
|---------|--------------|--------|
| **Identità** | NO (uguali se stessi valori) | SÌ (uguali se stesso ID) |
| **Mutabilità** | Immutabile | Mutabile (stato cambia) |
| **Equality** | Per valore | Per ID |
| **Esempio** | `Priority`, `Email` | `TaskItem`, `User` |

### La differenza chiave

```csharp
// Value Object: due Priority "High" sono LA STESSA COSA
Priority.High == Priority.High  // true (stesso valore)

// Entity: due Task con stesso titolo sono DIVERSI
var task1 = new TaskItem("Buy milk");
var task2 = new TaskItem("Buy milk");
task1 == task2  // FALSE! ID diversi
```

## Struttura di TaskItem

### Proprietà

```csharp
public class TaskItem
{
    public Guid Id { get; }                    // Identità - immutabile
    public string Title { get; private set; }  // Può cambiare internamente
    public string? Description { get; private set; }
    public Priority Priority { get; private set; }  // Value Object!
    public bool IsCompleted { get; private set; }
    public DateTime CreatedAt { get; }         // Immutabile
    public DateTime? CompletedAt { get; private set; }
}
```

### Differenza tra `get;` e `private set;`

| Sintassi | Significato |
|----------|-------------|
| `{ get; }` | Readonly - si setta SOLO nel costruttore |
| `{ get; private set; }` | Modificabile, ma SOLO dall'interno della classe |

## Comportamento (non solo dati!)

Un'Entity ha **metodi che esprimono intenzioni di business**:

```csharp
// ✅ GIUSTO: nome che il business capisce
public void Complete()
{
    if (IsCompleted)
        throw new InvalidOperationException("Task already completed");

    IsCompleted = true;
    CompletedAt = DateTime.UtcNow;
}

// ❌ SBAGLIATO: "setter stile Java" - nessun significato business
public void SetIsCompleted(bool value) { IsCompleted = value; }
```

### Altri metodi comportamentali

```csharp
public void UpdateTitle(string newTitle)
{
    if (string.IsNullOrWhiteSpace(newTitle))
        throw new ArgumentException("Title cannot be empty");

    Title = newTitle;
}

public void ChangePriority(Priority newPriority)
{
    Priority = newPriority;
}
```

## Invarianti

**Invariante** = condizione che deve essere SEMPRE vera per l'oggetto.

| Invariante | Dove si applica |
|------------|-----------------|
| Title non può essere vuoto | Costruttore + `UpdateTitle()` |
| Non puoi completare un task già completato | `Complete()` |
| CompletedAt è null se non completato | `Complete()` |
| Id è sempre valorizzato | Costruttore |

### Il costruttore protegge le invarianti

```csharp
public TaskItem(string title, Priority priority)
{
    if (string.IsNullOrWhiteSpace(title))
        throw new ArgumentException("Title cannot be empty");

    Id = Guid.NewGuid();
    Title = title;
    Priority = priority;
    IsCompleted = false;
    CreatedAt = DateTime.UtcNow;
}
```

**Regola:** Se un oggetto viene creato, è SEMPRE in uno stato valido.

## Quando usarlo

- Oggetti che hanno un **ciclo di vita** (nascono, cambiano, muoiono)
- Oggetti che devono essere **tracciati** nel tempo
- Oggetti dove l'**identità** conta più dei valori
- Aggregate Root in DDD

## Quando NON usarlo

- Oggetti senza identità (usa Value Object)
- Oggetti immutabili (usa Value Object)
- DTO per trasferimento dati (usa record/class semplice)

## TDD: Come costruirlo test-first

### Ciclo 1: Creazione base
```
🔴 TEST: TaskItem_WhenCreated_HasCorrectTitle
🟢 CODE: Costruttore con Title
```

### Ciclo 2: ID univoco
```
🔴 TEST: TaskItem_WhenCreated_HasUniqueId
🟢 CODE: Id = Guid.NewGuid()
```

### Ciclo 3: Validazione title
```
🔴 TEST: TaskItem_WithEmptyTitle_ThrowsException
🟢 CODE: Guard clause nel costruttore
```

### Ciclo 4: Complete()
```
🔴 TEST: TaskItem_WhenCompleted_IsCompletedIsTrue
🟢 CODE: Metodo Complete()
```

### Ciclo 5: Invariante completamento
```
🔴 TEST: TaskItem_WhenCompletedTwice_ThrowsException
🟢 CODE: Guard in Complete()
```

## Collegamenti

- [[smart-enum]] - Priority è uno Smart Enum (Value Object)
- [[value-objects]] - Differenza con Entity
- [[domain-events]] - TaskCompletedEvent quando si completa

## Quiz

### Q1: private set vs get

Perché `Title` ha `private set` mentre `Id` ha solo `get`?

**Mia risposta:** Id si genera una sola volta ed è immutabile, Title può cambiare ma solo dall'interno della classe.

✅ **Corretto**

---

### Q2: Equality

Se due TaskItem hanno lo stesso titolo "Buy milk", sono uguali?

**Mia risposta:** No, perché l'identità di un'Entity è determinata dall'ID, non dai valori.

✅ **Corretto**

---

### Q3: Complete() vs SetIsCompleted()

Perché il metodo si chiama `Complete()` e non `SetIsCompleted(true)`?

**Mia risposta:** Complete() esprime un'intenzione di business e contiene logica (validazione, timestamp). SetIsCompleted è solo manipolazione di stato senza significato.

✅ **Corretto** - I metodi di un'Entity devono avere nomi che il business capisce.

---

*Creato durante: Senior P1 Week 1 - Task Manager*
