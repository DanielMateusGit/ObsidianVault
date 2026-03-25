---
tags:
  - dotnet
  - async
  - from/week-05
  - status/learning
aliases:
  - Task
  - "Task<T>"
  - async/await
  - Asynchronous Programming
created: 2026-03-25
updated: 2026-03-25
source: "Sessione AQ P1 W5 - BackgroundService"
---

# Task e Programmazione Asincrona

> **One-liner:** `Task` rappresenta un'operazione in corso (o completata) — e la "promessa" che un risultato arrivera, permettendo al thread di fare altro nel frattempo.

## Cos'e

`Task` e il tipo di ritorno di un'operazione asincrona in .NET. Rappresenta un **lavoro in corso** — non il risultato, ma la promessa che il risultato arrivera.

```csharp
// Sincrono — il thread ASPETTA (bloccato)
string data = GetDataFromDatabase();    // thread fermo per 500ms

// Asincrono — il thread e LIBERO di fare altro
Task<string> promise = GetDataFromDatabaseAsync();  // ritorna subito
string data = await promise;                        // riprende quando pronto
```

### Due Varianti

| Tipo | Significato | Esempio |
|------|-------------|---------|
| `Task` | Operazione senza risultato (come `void`) | `SaveChangesAsync()` — salva, non ritorna nulla |
| `Task<T>` | Operazione con risultato di tipo T | `GetByIdAsync()` → ritorna `Task<Notification?>` |

### Come Funziona (Senza Magia)

```
Thread 1: Handler.Handle()
    │
    │── await _repo.GetByIdAsync(id, ct)
    │       │
    │       └── Parte la query al DB (I/O operation)
    │           Thread 1 e LIBERO → torna al thread pool
    │           Puo servire altre richieste HTTP!
    │
    │   ... 50ms dopo, la query e completa ...
    │
    │── Thread pool assegna un thread (puo essere Thread 1 o un altro)
    │   Il codice RIPRENDE da dove era rimasto
    │
    │── continua con il risultato
```

**Punto chiave:** `await` NON blocca il thread. Lo **libera**. Quando il risultato e pronto, il codice riprende (possibilmente su un thread diverso). Questo e fondamentale per la scalabilita: un web server con 100 thread puo gestire migliaia di richieste concorrenti perche i thread non restano bloccati ad aspettare il DB.

### async/await — Le Keyword

```csharp
// "async" dice al compilatore: "questo metodo conterra degli await"
public async Task<Guid> Handle(CreateTaskCommand cmd, CancellationToken ct)
{
    // "await" dice: "aspetta il risultato, ma libera il thread nel frattempo"
    var task = await _repository.GetByIdAsync(cmd.Id, ct);

    // Dopo l'await, il codice continua normalmente
    task.Complete();
    await _unitOfWork.SaveChangesAsync(ct);

    return task.Id;  // Task<Guid> → il Guid viene wrappato in un Task
}
```

**Regole:**
1. Se un metodo ha `await`, DEVE essere `async`
2. Se un metodo e `async`, DEVE ritornare `Task`, `Task<T>`, o `ValueTask<T>`
3. `async void` → **MAI** (tranne event handler UI). Usa `async Task`

### Task vs Thread

| | Task | Thread |
|---|------|--------|
| **Cos'e** | Un'unita di lavoro asincrona | Un filo di esecuzione del SO |
| **Peso** | Leggero (oggetto in memoria) | Pesante (~1MB di stack) |
| **Gestione** | Thread pool automatico | Manuale |
| **Quantita** | Migliaia contemporaneamente | Centinaia al massimo |
| **Uso** | `await GetDataAsync()` | Raramente diretto in .NET moderno |

Non crei un Thread per ogni Task — il thread pool di .NET gestisce pochi thread che servono migliaia di Task in rotazione.

## Quando usarlo

- **Sempre** per operazioni I/O (database, HTTP, file, queue) — e lo standard in .NET moderno
- In ogni handler MediatR (Commands e Queries)
- Nei repository (`GetByIdAsync`, `AddAsync`, ecc.)
- Nei BackgroundService (`ExecuteAsync`)

## Quando NON usarlo

- Per calcoli pesanti CPU-bound (es. crittografia, compressione) — li non c'e I/O da aspettare, `await` non aiuta. Usa `Task.Run()` per spostarli su un thread separato
- Non fare `task.Result` o `task.Wait()` — **bloccano il thread** e annullano il vantaggio dell'async. Usa sempre `await`

## Esempio — I pattern che usi gia

```csharp
// Pattern 1: Handler MediatR (lo usi gia!)
public async Task<Guid> Handle(CreateTaskItemCommand cmd, CancellationToken ct)
{
    var item = new TaskItem(cmd.Title, cmd.Priority);
    await _repository.AddAsync(item, ct);       // Task (void)
    await _unitOfWork.SaveChangesAsync(ct);      // Task<int>
    return item.Id;                              // wrappato in Task<Guid>
}

// Pattern 2: Repository
public async Task<TaskItem?> GetByIdAsync(Guid id, CancellationToken ct)
{
    return await _dbContext.Tasks
        .FirstOrDefaultAsync(t => t.Id == id, ct);  // Task<TaskItem?>
}

// Pattern 3: BackgroundService
protected override async Task ExecuteAsync(CancellationToken stoppingToken)
{
    while (!stoppingToken.IsCancellationRequested)
    {
        await ProcessNextAsync(stoppingToken);  // Task (void)
    }
}
```

## Analogia

`Task` e come un **ordine al ristorante**:
- Tu (il thread) ordini la pasta (chiami `GetDataAsync()`)
- Il cameriere ti da un **numeretto** (il `Task`) — "ti avviso quando e pronto"
- Tu sei libero di chiacchierare, guardare il telefono (il thread fa altro)
- Quando la pasta e pronta, il cameriere ti chiama (il Task si completa)
- Tu riprendi a mangiare (`await` restituisce il risultato)

Se invece fosse **sincrono**: resti in piedi davanti alla cucina a fissare il cuoco finche la pasta non e pronta. Il ristorante servirebbe 1 cliente alla volta.

## Collegamenti

- [[cancellation-token]] - CancellationToken per cancellare operazioni async
- [[coding-assistant-vs-llm]] - L'agentic loop e concettualmente asincrono

## Quiz

### Q1: Task vs Thread (TASK-01)
Un collega dice: "Ogni Task crea un nuovo Thread". Ha ragione? Quanti thread servono per gestire 1000 richieste async contemporanee?

**Mia risposta:**

---

### Q2: Await non blocca (TASK-02)
`await _repo.GetByIdAsync(id)` — cosa succede al thread durante i 50ms che il DB impiega a rispondere? Il thread sta fermo ad aspettare?

**Mia risposta:**

---

### Q3: async void (TASK-03)
Un metodo e dichiarato `async void DoSomething()`. Perche e pericoloso? Cosa succederebbe se lanciasse un'eccezione?

**Mia risposta:**

---

### Q4: .Result e il deadlock (TASK-04)
Invece di `await _repo.GetByIdAsync(id)` scrivi `_repo.GetByIdAsync(id).Result`. Funziona? Quali sono i rischi?

**Mia risposta:**

---

### Q5: Task vs Task<T> (TASK-05)
`SaveChangesAsync()` ritorna `Task<int>`. `AddAsync()` ritorna `Task`. Qual e la differenza semantica? Quando usi l'uno e quando l'altro?

**Mia risposta:**

---

## Risorse

- [Microsoft Docs - Asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/) - Guida ufficiale async/await
- [Stephen Cleary - There Is No Thread](https://blog.stephencleary.com/2013/11/there-is-no-thread.html) - Articolo fondamentale: perche async non crea thread
- [Stephen Cleary - Async Best Practices](https://learn.microsoft.com/en-us/archive/msdn-magazine/2013/march/async-await-best-practices-in-asynchronous-programming) - Le regole d'oro
