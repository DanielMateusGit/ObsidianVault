---
tags:
  - p1
  - dotnet
  - worker
  - async
  - from/week-05
  - status/learning
aliases:
  - BackgroundService
  - Worker Service
  - IHostedService
created: 2026-03-25
source: "Sessione Week 5 - BackgroundService"
---

# BackgroundService in .NET

> **One-liner:** BackgroundService e una classe base .NET per processi in background — il nostro worker che ascolta la queue e processa messaggi, separato dal ciclo request/response HTTP.

---

## Cos'e

L'API ASP.NET risponde a richieste HTTP. Ma chi ascolta la queue? Serve un processo che giri **in continuazione**, in background. In .NET si usa `BackgroundService` (namespace `Microsoft.Extensions.Hosting`).

```csharp
public class NotificationWorker : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            await ProcessNextMessageAsync(stoppingToken);
        }
    }
}
```

**Punti chiave:**
- `ExecuteAsync` viene chiamato **una volta** all'avvio dell'applicazione
- Il `stoppingToken` viene triggerato quando l'app si spegne (graceful shutdown)
- Gira in un **thread separato** — non blocca le richieste HTTP

---

## Dove Vive il Worker

### Approccio 1: Stesso processo dell'API (il nostro caso)

```
┌────────────────────────────────────────┐
│           ASP.NET Application          │
│                                        │
│  ┌──────────────┐  ┌────────────────┐  │
│  │  API          │  │  Worker        │  │
│  │  (HTTP)       │  │  (Background)  │  │
│  │  Riceve       │  │  Ascolta       │  │
│  │  richieste    │  │  la queue      │  │
│  └──────────────┘  └────────────────┘  │
└────────────────────────────────────────┘

Pro: Semplice, un solo deploy
Contro: Se l'API crasha, il worker muore con lei
```

### Approccio 2: Processo separato (Worker Service)

```
┌──────────────────┐    ┌──────────────────┐
│  ASP.NET API     │    │  Worker Service   │
│  (HTTP)          │    │  (Console App)    │
└──────────────────┘    └──────────────────┘

Pro: Scalabili indipendentemente, isolati
Contro: Due deploy, piu infrastruttura
```

**Quando passare all'Approccio 2:** piu traffico da gestire, serve scalare worker e API separatamente (es. 10 worker, 2 API), o serve isolamento (crash del worker non tocca l'API).

---

## Registrazione nel DI

```csharp
builder.Services.AddHostedService<NotificationWorker>();
```

Una riga. .NET gestisce avvio, shutdown e lifecycle automaticamente.

---

## La Trappola del Singleton: IServiceScopeFactory

Il `BackgroundService` e registrato come **Singleton** (vive per tutta l'app). Ma `DbContext` e i repository sono **Scoped** (vivono per una singola richiesta).

Iniettare un DbContext nel costruttore del worker → eccezione:
```
Cannot consume scoped service 'AppDbContext' from singleton 'NotificationWorker'
```

**Soluzione:** `IServiceScopeFactory` — crea uno scope manuale per ogni messaggio:

```csharp
public class NotificationWorker : BackgroundService
{
    private readonly IServiceScopeFactory _scopeFactory;
    private readonly ILogger<NotificationWorker> _logger;

    public NotificationWorker(
        IServiceScopeFactory scopeFactory,
        ILogger<NotificationWorker> logger)
    {
        _scopeFactory = scopeFactory;
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _logger.LogInformation("NotificationWorker started");

        while (!stoppingToken.IsCancellationRequested)
        {
            // Il consumer RabbitMQ gestisce l'attesa (event-driven)
            await Task.Delay(100, stoppingToken); // placeholder
        }

        _logger.LogInformation("NotificationWorker stopping");
    }

    private async Task ProcessMessageAsync(string notificationId)
    {
        // Crea uno scope per i servizi Scoped
        using var scope = _scopeFactory.CreateScope();
        var repository = scope.ServiceProvider
            .GetRequiredService<INotificationRepository>();
        var unitOfWork = scope.ServiceProvider
            .GetRequiredService<IUnitOfWork>();

        // 1. Carica dal DB
        var notification = await repository.GetByIdAsync(
            Guid.Parse(notificationId));

        // 2. Check idempotenza
        if (notification.Status == NotificationStatus.Sent)
            return;

        // 3. Invia
        // ... logica di invio ...

        // 4. Aggiorna status
        notification.MarkAsSent();
        await unitOfWork.SaveChangesAsync();

        // 5. ACK alla queue (gestito dal consumer RabbitMQ)
    }
}
```

**Il pattern:**
```
Worker (Singleton) → crea Scope → risolve DbContext (Scoped) → processa → dispose Scope
                     → crea Scope → risolve DbContext (Scoped) → processa → dispose Scope
                     → ...ogni messaggio ha il suo scope isolato
```

---

## Graceful Shutdown e CancellationToken

Quando l'app si spegne (deploy, restart, SIGTERM):

1. .NET triggera il `stoppingToken`
2. Il worker esce dal loop `while`
3. Se sta processando un messaggio e non ha ancora mandato ACK → il messaggio torna visibile in coda (invisibility timeout)
4. Al prossimo avvio, il worker lo riprende

Il `stoppingToken` da al worker un po' di tempo per finire il messaggio corrente. CancellationToken e ACK lavorano insieme per garantire zero perdite.

---

## Event-Driven vs Polling

Il worker **non fa polling**. RabbitMQ usa un modello **push/event-driven**:

```
POLLING (NON facciamo cosi):
  while (true)
      var msg = queue.Check()       // chiedi ogni 100ms
      if (msg != null) Process(msg)
      await Task.Delay(100)

EVENT-DRIVEN (facciamo cosi):
  consumer.OnMessageReceived += async (msg) =>
      await ProcessMessageAsync(msg) // RabbitMQ chiama noi
```

Zero traffico quando la queue e vuota, reazione immediata quando arriva un messaggio.

---

## Ciclo di Vita Completo

```
Applicazione si avvia
        │
        ├── Kestrel (web server) → ascolta HTTP
        │
        └── NotificationWorker.ExecuteAsync() → ascolta Queue
                │
                ├── while (!stoppingToken.IsCancellationRequested)
                │       │
                │       ├── Ricevi messaggio (event-driven)
                │       ├── Crea scope (IServiceScopeFactory)
                │       ├── Risolvi servizi (repo, uow)
                │       ├── Check idempotenza
                │       ├── Processa (DB → invio → update)
                │       ├── ACK alla queue
                │       ├── Dispose scope
                │       └── Ripeti
                │
                └── stoppingToken triggerato → esce dal loop
                                              (graceful shutdown)
```

---

## Quiz

### Q1: Singleton vs Scoped (BG-01)
Il NotificationWorker e Singleton. Vuoi usare INotificationRepository (Scoped). Come fai? Perche non iniettarlo nel costruttore?

**Mia risposta:**

---

### Q2: Graceful Shutdown (BG-02)
L'app si sta spegnendo. Il worker sta processando un messaggio. Come garantisci che il messaggio non si perda?

**Mia risposta:**

---

### Q3: Separare il worker (BG-03)
Worker nello stesso processo dell'API vs processo separato: quando ha senso separarli?

**Mia risposta:**

---

### Q4: AddHostedService (BG-04)
Cosa fa `builder.Services.AddHostedService<NotificationWorker>()`? Con quale lifetime registra il servizio?

**Mia risposta:**

---

### Q5: Event-driven vs Polling (BG-05)
Il worker usa un loop `while` con `Task.Delay(100)` per controllare la queue ogni 100ms. E una buona idea? Come miglioreresti?

**Mia risposta:**

---

## Risorse

- [Microsoft Docs - BackgroundService](https://learn.microsoft.com/en-us/dotnet/core/extensions/workers) - Documentazione ufficiale Worker Services
- [Microsoft Docs - IHostedService](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services) - Hosted services in ASP.NET Core
- [Andrew Lock - BackgroundService gotchas](https://andrewlock.net/avoiding-async-void-with-a-backgroundservice/) - Trappole comuni
