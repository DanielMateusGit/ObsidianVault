# W1 - Application Layer Setup

> **Data:** 2026-03-16
> **Fase:** Week 1 - Domain + Application Layer

---

## Cosa abbiamo fatto

### 1. IUnitOfWork Interface

Creata l'interfaccia `IUnitOfWork` in `Application/Interfaces/`:

```csharp
public interface IUnitOfWork
{
    Task<int> SaveChangesAsync(CancellationToken cancellationToken = default);
}
```

**Decisione architetturale:** L'interfaccia sta in Application (non Domain) perché:
- È l'Application Layer che chiama `SaveChangesAsync()` negli Handler
- Il Domain rimane puro (solo business logic)
- Segue il pattern Ports & Adapters: l'interfaccia è il PORT, l'implementazione (DbContext) sarà l'ADAPTER in Infrastructure

---

### 2. Primo Command con TDD

**Ciclo TDD completato:**

1. **Red** - Test scritto prima del codice (non compilava)
2. **Green** - Creato Command e Handler per far passare il test
3. **Refactor** - (non necessario in questo caso)

#### CreateTaskItemCommand

```csharp
public record CreateTaskItemCommand(string Title, Priority Priority) : IRequest<Guid>;
```

- `record` = classe immutabile semplificata (C# 9+)
- `IRequest<Guid>` = interfaccia MediatR, ritorna l'ID del task creato

#### CreateTaskItemHandler

```csharp
public class CreateTaskItemHandler : IRequestHandler<CreateTaskItemCommand, Guid>
{
    private readonly ITaskRepository _repository;
    private readonly IUnitOfWork _unitOfWork;

    public CreateTaskItemHandler(ITaskRepository repository, IUnitOfWork unitOfWork)
    {
        _repository = repository;
        _unitOfWork = unitOfWork;
    }

    public async Task<Guid> Handle(CreateTaskItemCommand request, CancellationToken cancellationToken)
    {
        TaskItem newTask = new TaskItem(request.Title, request.Priority);
        await _repository.AddAsync(newTask, cancellationToken);
        await _unitOfWork.SaveChangesAsync(cancellationToken);

        return newTask.Id;
    }
}
```

**Pattern applicati:**
- Dependency Injection (repository e UoW iniettati nel costruttore)
- Unit of Work (SaveChanges separato dal repository)
- CQRS (Command separato dalla Query)

---

### 3. Test con NSubstitute

```csharp
[Fact]
public async Task Handle_ValidCommand_ShouldAddTaskAndSaveChanges()
{
    // Arrange
    var repo = Substitute.For<ITaskRepository>();
    var uow = Substitute.For<IUnitOfWork>();
    var command = new CreateTaskItemCommand("test", Priority.High);
    var handler = new CreateTaskItemHandler(repo, uow);

    // Act
    await handler.Handle(command, CancellationToken.None);

    // Assert
    await repo.Received(1).AddAsync(Arg.Any<TaskItem>(), Arg.Any<CancellationToken>());
    await uow.Received(1).SaveChangesAsync(Arg.Any<CancellationToken>());
}
```

---

### 4. CompleteTaskCommand (Recap #5 - fatto da solo!)

#### CompleteTaskItemCommand

```csharp
public record CompleteTaskItemCommand(Guid TaskId) : IRequest<Guid>;
```

#### CompleteTaskItemHandler

```csharp
public class CompleteTaskItemHandler : IRequestHandler<CompleteTaskItemCommand, Guid>
{
    private readonly ITaskRepository _repository;
    private readonly IUnitOfWork _unitOfWork;

    public async Task<Guid> Handle(CompleteTaskItemCommand request, CancellationToken cancellationToken)
    {
        TaskItem t = await _repository.GetByIdAsync(request.TaskId, cancellationToken)
            ?? throw new InvalidOperationException();
        t.Complete();
        await _unitOfWork.SaveChangesAsync(cancellationToken);

        return t.Id;
    }
}
```

**Lezione imparata:** Quando il mock deve ritornare un oggetto, bisogna configurarlo:
```csharp
repo.GetByIdAsync(taskItemId, Arg.Any<CancellationToken>()).Returns(taskItem);
```

---

### 5. Update() nel Repository - Decisione Architetturale

**Problema identificato:** L'handler modificava l'entity (`task.Complete()`) e poi chiamava `SaveChangesAsync()`. Questo funziona con EF Core (Change Tracking), ma **non con SQL puro/Dapper**.

**Domanda chiave:** Come fa il DB a sapere che l'oggetto è stato modificato?

| Tecnologia | Come traccia le modifiche |
|------------|---------------------------|
| **EF Core** | Change Tracking automatico - "vede" le modifiche |
| **Dapper/SQL** | Non traccia niente - devi fare UPDATE esplicito |

**Soluzione:** Aggiungere `Update()` a `ITaskRepository` per essere **agnostici dalla tecnologia**:

```csharp
public interface ITaskRepository
{
    Task<TaskItem?> GetByIdAsync(Guid id, CancellationToken ct = default);
    Task<IEnumerable<TaskItem>> GetAllAsync(CancellationToken ct = default);
    Task AddAsync(TaskItem task, CancellationToken ct = default);
    void Update(TaskItem task);  // ← AGGIUNTO per essere agnostici!
    void Remove(TaskItem task);
}
```

**Pattern negli Handler:**
```csharp
var task = await _repository.GetByIdAsync(id, ct);
task.Complete();              // modifica in memoria
_repository.Update(task);     // segnala la modifica (agnostico!)
await _unitOfWork.SaveChangesAsync(ct);  // persiste
```

**Implementazioni possibili:**
- **EF Core:** `_dbContext.Tasks.Update(task)` (o no-op)
- **Dapper:** `connection.Execute("UPDATE Tasks SET ... WHERE Id=@Id", task)`

---

## Concetti chiave

| Concetto | Spiegazione |
|----------|-------------|
| `record` | Classe immutabile in una riga. Perfetto per DTO, Commands, Queries |
| `IRequest<T>` | Interfaccia MediatR per command/query che ritorna T |
| `IRequestHandler<TRequest, TResponse>` | Handler che processa il command |
| `Substitute.For<T>()` | NSubstitute crea un mock dell'interfaccia |
| `Received(1)` | Verifica che il metodo sia stato chiamato 1 volta |
| `Arg.Any<T>()` | Accetta qualsiasi argomento di tipo T |
| `Returns(value)` | Configura il mock per ritornare un valore specifico |
| `Update()` nel repo | Rende il codice agnostico dalla tecnologia (EF Core vs Dapper) |

---

## Prossimi step

- [x] CompleteTaskCommand (Recap #5 - da solo) ✅
- [x] UpdateTaskCommand ✅
- [x] DeleteTaskCommand ✅
- [ ] Queries (GetById, GetAll, GetByStatus)
- [ ] FluentValidation sui commands

---

*Ultimo aggiornamento: 2026-03-16*
