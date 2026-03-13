---
tags: [senior-engineer, notes, p1, entity, value-object, ddd]
created: 2026-03-03
---

# Domain Building Blocks - Implementazione C#

> Teoria: [[clean-architecture-principles]], [[validation-vs-invariants]]

---

## Entity

```csharp
public class TaskItem
{
    // Identità - readonly, solo nel costruttore
    public Guid Id { get; }
    public DateTime CreatedAt { get; }

    // Stato mutabile - solo dall'interno
    public string Title { get; private set; }
    public Priority Priority { get; private set; }
    public DateTime? CompletedAt { get; private set; }

    // Computed property
    public bool IsCompleted => CompletedAt.HasValue;

    // Costruttore con validazione
    public TaskItem(string title, Priority priority)
    {
        if (string.IsNullOrWhiteSpace(title))
            throw new EmptyTaskTitleException();

        Id = Guid.NewGuid();
        Title = title;
        Priority = priority;
        CreatedAt = DateTime.UtcNow;
    }

    // Comportamento con invarianti
    public void Complete()
    {
        if (IsCompleted) throw new TaskAlreadyCompletedException(Id);
        CompletedAt = DateTime.UtcNow;
    }

    public void UpdateTitle(string newTitle)
    {
        if (string.IsNullOrWhiteSpace(newTitle))
            throw new EmptyTaskTitleException();
        Title = newTitle;
    }
}
```

**Pattern chiave:**
- `{ get; }` = immutabile (solo costruttore)
- `{ get; private set; }` = mutabile internamente
- `=>` = computed, ricalcolato ogni accesso
- Guard clause in costruttore + metodi

---

## Value Object (semplice)

```csharp
// Smart Enum - istanze limitate
public class Priority
{
    public static readonly Priority Low = new("Low", 1);
    public static readonly Priority Medium = new("Medium", 2);
    public static readonly Priority High = new("High", 3);

    public string Name { get; }
    public int Value { get; }

    private Priority(string name, int value)
    {
        Name = name;
        Value = value;
    }
}
```

---

## Value Object (con comportamento)

```csharp
public class DueDate
{
    public DateTime Value { get; }

    // Computed - ricalcolato ogni volta
    public bool IsOverdue => Value < DateTime.UtcNow;

    // Costruttore PRIVATO
    private DueDate(DateTime value) => Value = value;

    // Factory method con validazione
    public static DueDate FromDateTime(DateTime date)
    {
        if (date < DateTime.UtcNow)
            throw new PastDueDateException();
        return new DueDate(date);
    }

    // Comportamento
    public int DaysRemaining() => (Value - DateTime.UtcNow).Days;
}
```

**Quando Factory Method:**
- Validazione che può fallire
- Logica di creazione complessa

**Quando Costruttore pubblico:**
- Sempre valido, semplice

---

## Sintassi C# - Cheat Sheet

| Sintassi | Comportamento |
|----------|---------------|
| `{ get; }` | Solo costruttore |
| `{ get; private set; }` | Set interno |
| `{ get; } = expr` | Inizializzato UNA volta |
| `=> expr` | Ricalcolato OGNI accesso |

```csharp
// ❌ Valutato una volta alla creazione
public bool IsOverdue { get; } = Value < DateTime.UtcNow;

// ✅ Valutato ogni volta che accedi
public bool IsOverdue => Value < DateTime.UtcNow;
```

---

## Eccezioni Domain

```csharp
// Validazione input
public class EmptyTaskTitleException : ArgumentException
{
    public EmptyTaskTitleException()
        : base("Task title cannot be empty") {}
}

// Operazione non valida
public class TaskAlreadyCompletedException : InvalidOperationException
{
    public Guid TaskId { get; }

    public TaskAlreadyCompletedException(Guid taskId)
        : base($"Task {taskId} is already completed")
    {
        TaskId = taskId;
    }
}
```

**Convenzione:** estendi `ArgumentException` o `InvalidOperationException`, non creare gerarchia custom.

---

*Creato: 2026-03-03*
