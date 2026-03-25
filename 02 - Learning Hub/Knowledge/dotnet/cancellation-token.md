---
tags:
  - dotnet
  - async
  - from/week-05
  - status/learning
aliases:
  - CancellationToken
  - CancellationTokenSource
  - Cooperative Cancellation
created: 2026-03-25
updated: 2026-03-25
source: "Sessione AQ P1 W5 - BackgroundService"
---

# CancellationToken

> **One-liner:** Un segnale cooperativo che dice "smetti di lavorare quando puoi" — non forza lo stop, chiede gentilmente.

## Cos'e

Un `CancellationToken` e un **segnale di cancellazione** passato a operazioni asincrone. Non forza nulla — e **cooperativo**: il codice che lo riceve deve controllarlo e decidere di fermarsi.

Funziona cosi:

```
CancellationTokenSource (il PRODUTTORE)
        │
        │ .Token
        ▼
CancellationToken (il SEGNALE)
        │
        │ passato a metodi async
        ▼
Il codice controlla: "Mi hanno chiesto di fermarmi?"
```

### Chi lo Produce

Il `CancellationToken` non si crea direttamente. Si crea un **`CancellationTokenSource`** e da quello si ottiene il token:

```csharp
// Chi PRODUCE la cancellazione
var cts = new CancellationTokenSource();
CancellationToken token = cts.Token;

// Dopo 5 secondi, o quando serve:
cts.Cancel(); // → il token diventa "cancelled"
```

### Chi lo Fornisce

Dipende dal contesto:

| Contesto | Chi produce il token | Quando viene cancellato |
|----------|---------------------|------------------------|
| **API Controller** | ASP.NET (automatico) | Client chiude la connessione, timeout |
| **BackgroundService** | .NET Host (il `stoppingToken`) | L'applicazione si sta spegnendo (SIGTERM, deploy) |
| **MediatR Handler** | ASP.NET → MediatR (propagato) | Client disconnesso |
| **Test** | Tu (manualmente) | `cts.Cancel()` nel test |
| **Timeout manuale** | Tu | `new CancellationTokenSource(TimeSpan.FromSeconds(30))` |

### Come si Usa

```csharp
// Pattern 1: Passarlo a metodi async (il piu comune)
await _repository.GetByIdAsync(id, cancellationToken);
// Se il token e cancellato, il metodo lancia OperationCanceledException

// Pattern 2: Controllarlo in un loop
while (!cancellationToken.IsCancellationRequested)
{
    await ProcessNextAsync();
}

// Pattern 3: Lanciare eccezione esplicita
cancellationToken.ThrowIfCancellationRequested();
// Lancia OperationCanceledException se cancellato
```

### Cosa Succede Quando si Cancella

```
1. cts.Cancel() viene chiamato
2. Il token passa a IsCancellationRequested = true
3. I metodi async che lo ricevono lanciano OperationCanceledException
4. ASP.NET cattura l'eccezione e ritorna HTTP 499 (Client Closed Request)
   oppure il BackgroundService esce dal loop
```

## Quando usarlo

- **Sempre** nei metodi async — propagalo lungo tutta la catena
- Nei loop di BackgroundService (`while (!stoppingToken.IsCancellationRequested)`)
- Nelle query al DB — cosi se il client disconnette, la query si interrompe
- Nei test — per simulare timeout o cancellazioni

## Quando NON usarlo

- Per forzare lo stop immediato di un thread — non e uno `Thread.Abort()`
- Per gestire errori — usa eccezioni normali, non cancellazione
- Per controllare il flusso logico — e per cancellazione, non per branching

## Esempio — Nel Nostro Notification Worker

```csharp
public class NotificationWorker : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        // stoppingToken e fornito da .NET Host
        // Viene cancellato quando l'app si sta spegnendo

        while (!stoppingToken.IsCancellationRequested)  // ← controlla il segnale
        {
            await ProcessNextMessageAsync(stoppingToken); // ← propaga ai figli
        }

        // Se arriviamo qui, l'app si sta spegnendo
        _logger.LogInformation("Worker stopping gracefully");
    }
}
```

```csharp
// Nell'API — il token arriva automaticamente da ASP.NET
app.MapPost("/notify", async (
    ScheduleNotificationCommand cmd,
    ISender sender,
    CancellationToken ct) =>         // ← ASP.NET lo inietta automaticamente
{
    var id = await sender.Send(cmd, ct);  // ← propagato a MediatR → Handler
    return Results.Created($"/notifications/{id}", id);
});
```

## Analogia

Pensa a un cantiere. Il `CancellationToken` e come un **semaforo rosso** piazzato nel cantiere:
- Non spegne le macchine
- Non blocca fisicamente gli operai
- Ma ogni operaio, prima di iniziare il prossimo compito, lo guarda
- Se e rosso, smette di lavorare e torna a casa ordinatamente
- Se un operaio sta gia facendo qualcosa, finisce quello che sta facendo e poi si ferma

**Cooperativo** = gli operai devono guardare il semaforo. Se non lo guardano, continuano a lavorare.

## Collegamenti

- [[task-type]] - Task e il tipo di ritorno delle operazioni async
- [[coding-assistant-vs-llm]] - BackgroundService usa CancellationToken per graceful shutdown

## Quiz

### Q1: Chi produce il CancellationToken? (CT-01)
Il CancellationToken non si crea con `new CancellationToken()`. Come si produce? Chi decide quando cancellarlo?

**Mia risposta:**

---

### Q2: Cooperativo vs Forzato (CT-02)
Un collega dice: "Il CancellationToken ferma immediatamente l'operazione, come Thread.Abort()". Ha ragione? Perche?

**Mia risposta:**

---

### Q3: Perche propagarlo? (CT-03)
Nel tuo Handler MediatR, ricevi un `CancellationToken ct` e chiami `_repository.GetByIdAsync(id)` SENZA passare `ct`. Cosa succede se il client chiude la connessione durante la query al DB?

**Mia risposta:**

---

### Q4: BackgroundService stoppingToken (CT-04)
Chi fornisce il `stoppingToken` al `BackgroundService.ExecuteAsync()`? Quando viene cancellato? Cosa succede se il worker sta processando un messaggio in quel momento?

**Mia risposta:**

---

### Q5: Timeout manuale (CT-05)
Vuoi che una chiamata HTTP esterna (es. invio email via API) abbia un timeout di 30 secondi. Come usi il CancellationToken per implementarlo?

**Mia risposta:**

---

## Risorse

- [Microsoft Docs - Cancellation in managed threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads) - Documentazione ufficiale
- [Stephen Cleary - Cancellation](https://blog.stephencleary.com/2022/02/cancellation-1-overview.html) - Serie approfondita sul CancellationToken
