o# Clean Architecture - Appunti

> **Data:** 2026-02-02
> **Sessione:** Week 1 - Setup
> **XP guadagnati:** +100 (Repo + Docker Compose)

---

## Cos'è Clean Architecture?

Pattern architetturale creato da **Robert C. Martin (Uncle Bob)** che organizza il codice in cerchi concentrici con dipendenze che puntano verso il centro.

### Il Problema che Risolve

Senza una struttura chiara:
- Codice database mischiato con logica business
- Cambiare database = toccare 200 file
- Impossibile testare senza infrastruttura reale
- Duplicazione di logica ovunque

### La Soluzione: Cerchi Concentrici

```
        ┌─────────────────────────────────────┐
        │            API / UI                 │  ← Esterno: come entri nel sistema
        │  ┌─────────────────────────────┐    │
        │  │      Infrastructure         │    │  ← Dettagli tecnici (DB, Redis, email)
        │  │  ┌─────────────────────┐    │    │
        │  │  │    Application      │    │    │  ← Use cases: "cosa fa il sistema"
        │  │  │  ┌─────────────┐    │    │    │
        │  │  │  │   Domain    │    │    │    │  ← Core: regole business pure
        │  │  │  └─────────────┘    │    │    │
        │  │  └─────────────────────┘    │    │
        │  └─────────────────────────────┘    │
        └─────────────────────────────────────┘
```

---

## La Regola d'Oro: Dependency Rule

> **Le dipendenze puntano SOLO verso il centro (Domain).**
> I layer interni NON conoscono i layer esterni.

```
Api ──────► Application ──────► Domain
               ▲
Infrastructure─┘
```

---

## I 4 Layer

### 1. Domain (Il Cuore)

**Cosa contiene:** Entità business pure, value objects, regole di dominio.

**Dipendenze:** ZERO - non referenzia nulla.

**Esempio:**
```csharp
public class Notification
{
    public Guid Id { get; private set; }
    public string Recipient { get; private set; }
    public NotificationStatus Status { get; private set; }

    // Solo logica business pura
    public bool CanRetry() => Status == NotificationStatus.Failed
                              && RetryCount < MaxRetries;
}
```

**QUANDO lo usi:** Sempre. Se cambi database, framework, o API - questo layer NON cambia.

---

### 2. Application (I Casi d'Uso)

**Cosa contiene:** Use cases, comandi, query, interfacce (porte).

**Dipendenze:** Solo Domain.

**Esempio:**
```csharp
// Definisce l'INTERFACCIA (porta)
public interface IEmailSender
{
    Task<Result> Send(string to, string subject, string body);
}

// Use case che orchestra
public class SendNotificationUseCase
{
    private readonly INotificationRepository _repo;
    private readonly IEmailSender _emailSender;

    public async Task<Result> Execute(SendNotificationCommand cmd)
    {
        var notification = Notification.Create(cmd.Recipient, cmd.Message);
        await _repo.Save(notification);
        await _emailSender.Send(notification);
        return Result.Success();
    }
}
```

**QUANDO lo usi:** Un use case = un'azione utente. Orchestrazione senza dettagli implementativi.

---

### 3. Infrastructure (I Dettagli Tecnici)

**Cosa contiene:** Implementazioni concrete di DB, cache, servizi esterni.

**Dipendenze:** Application (implementa le interfacce).

**Esempio:**
```csharp
// IMPLEMENTA l'interfaccia definita in Application
public class SendGridEmailSender : IEmailSender
{
    public async Task<Result> Send(string to, string subject, string body)
    {
        var client = new SendGridClient("API_KEY");
        // Codice specifico SendGrid
    }
}

public class PostgresNotificationRepository : INotificationRepository
{
    private readonly DbContext _db;

    public async Task Save(Notification notification)
    {
        await _db.Notifications.AddAsync(notification);
        await _db.SaveChangesAsync();
    }
}
```

**QUANDO lo usi:** Per tutto ciò che è "dettaglio tecnico". Se cambi provider, modifichi SOLO qui.

---

### 4. Api (Entry Point)

**Cosa contiene:** Controller, middleware, configurazione DI.

**Dipendenze:** Application + Infrastructure.

**Esempio:**
```csharp
[ApiController]
[Route("api/notifications")]
public class NotificationsController : ControllerBase
{
    private readonly SendNotificationUseCase _useCase;

    [HttpPost]
    public async Task<IActionResult> Send(SendNotificationRequest request)
    {
        var result = await _useCase.Execute(request.ToCommand());
        return result.IsSuccess ? Ok() : BadRequest(result.Error);
    }
}
```

**QUANDO lo usi:** Solo per HTTP/API. Il controller non contiene logica business.

---

## Violazioni da Evitare

### 1. Domain che dipende da Infrastructure

```csharp
// ❌ SBAGLIATO
using Microsoft.EntityFrameworkCore;

public class Notification
{
    [Column("recipient_email")]  // EF Core nel Domain!
    public string Recipient { get; set; }
}
```

**Problema:** Domain deve essere puro. Se conosce EF Core, non puoi testarlo senza DB.

---

### 2. Application che chiama servizi esterni direttamente

```csharp
// ❌ SBAGLIATO
using SendGrid;

public class SendNotificationUseCase
{
    public async Task Execute(...)
    {
        var client = new SendGridClient("KEY");  // Accoppiato!
        await client.SendEmailAsync(...);
    }
}
```

**Problema:** Application deve usare interfacce, non implementazioni concrete.

---

### 3. Controller con logica business

```csharp
// ❌ SBAGLIATO
[HttpPost]
public async Task<IActionResult> Send(SendRequest request)
{
    // Validazione, creazione entità, salvataggio, invio email
    // TUTTO nel controller!
    if (notification.RetryCount > 3) { ... }
    await _dbContext.SaveChangesAsync();
    await _sendGrid.SendEmailAsync(...);
}
```

**Problema:** Logica duplicata se aggiungi altri entry point (worker, CLI).

---

### 4. Bypass di Application

```csharp
// ❌ SBAGLIATO - Controller chiama diretto il DB
[HttpGet("{id}")]
public async Task<IActionResult> Get(Guid id)
{
    var notif = await _dbContext.Notifications.FindAsync(id);
    return Ok(notif);
}
```

**Problema:** Perdi il punto centrale per authorization, logging, caching.

---

## Schema Chi Conosce Chi

| Layer | Può Conoscere |
|-------|--------------|
| **Domain** | Nessuno |
| **Application** | Domain |
| **Infrastructure** | Application (e Domain transitivo) |
| **Api** | Application, Infrastructure |

---

## Vantaggi

| Vantaggio | Spiegazione |
|-----------|-------------|
| **Testabilità** | Domain e Application testabili senza DB/servizi |
| **Sostituibilità** | Cambi SendGrid con Mailgun modificando 1 classe |
| **Manutenibilità** | Sai sempre dove trovare/mettere il codice |
| **Indipendenza** | Il business non dipende da framework |

---

## Risorse

- [The Clean Architecture - Uncle Bob (Originale)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Breaking Down Clean Architecture - Medium](https://medium.com/@tales.of.di.official/breaking-down-clean-architecture-by-uncle-bob-part-i-d1fc54add73f)
- [Summary of Clean Architecture - GitHub Gist](https://gist.github.com/ygrenzinger/14812a56b9221c9feca0b3621518635b)
- Libro: "Clean Architecture" di Robert C. Martin

---

## Struttura del Nostro Progetto

```
notification-service/
├── NotificationService.sln
├── docker-compose.yml
└── src/
    ├── NotificationService.Domain/           ← Zero dipendenze
    ├── NotificationService.Application/      ← → Domain
    ├── NotificationService.Infrastructure/   ← → Application
    └── NotificationService.Api/              ← → Application + Infrastructure
```

**Repo GitHub:** https://github.com/DanielMateusGit/notification-service

---

## Quiz di Verifica (2026-02-02)

### Q1: Dove metteresti un'interfaccia `IEmailSender`? In quale layer e perché?

**Mia risposta:** Nel layer Application: perché si decide cosa deve fare il sistema e si progetta per interfacce. Application mi dice cosa fa il sistema o "chi fa cosa" tramite un'interfaccia. In questo caso sto dicendo "il sistema deve mandare delle Email e sarà IEmailSender a farlo".

✅ **Perfetto!** Application definisce le **porte** (interfacce). Infrastructure fornisce gli **adattatori** (implementazioni).

```
Application/
└── Interfaces/
    └── IEmailSender.cs    ← "Il sistema deve poter inviare email"

Infrastructure/
└── Email/
    └── SendGridEmailSender.cs : IEmailSender  ← "Ecco COME lo fa"
```

---

### Q2: Un junior vuole aggiungere `using Microsoft.EntityFrameworkCore;` nel Domain. Cosa gli dici?

**Mia risposta:** Che il layer Domain è quello che contiene le regole di business pure, le entità scambiate e basta. Qui non abbiamo logiche, ed ogni entità registrata è agnostica al resto dell'applicazione. Domain potrebbe vivere per conto suo. Potrei usare Domain per costruire l'applicazione A e l'applicazione B → tutto ciò che si costruisce attorno a Domain è dipendente da Domain, ma Domain stesso "il core" rimane agnostico.

✅ **Eccellente!** L'analogia è perfetta:
- Domain = il "cuore" riutilizzabile
- Potrei usare lo stesso Domain per: API REST, CLI tool, Worker service, App mobile
- Se Domain dipende da EF Core, questa flessibilità si perde

**Cosa dire al junior:** "Se aggiungi EF Core al Domain, ogni progetto che usa questo Domain sarà costretto a portarsi dietro EF Core, anche se usa MongoDB o Dapper."

---

### Q3: Devi cambiare da SendGrid a Mailgun. Quali layer modifichi?

**Mia risposta:** Infrastructure: questo è quello che implementa quanto specificato in Application. Se Application dice "cosa deve fare l'applicazione" Infrastructure mi dice "come lo fa". Quindi dovrei cambiare Infrastructure.

✅ **Corretto!**

| Layer | Modifiche |
|-------|-----------|
| Domain | ❌ Nessuna |
| Application | ❌ Nessuna (l'interfaccia `IEmailSender` resta uguale) |
| Infrastructure | ✅ Creo `MailgunEmailSender : IEmailSender` |
| Api | ✅ Cambio 1 riga nel DI |

**Questo è il potere della Clean Architecture:** cambi provider modificando 1 classe + 1 riga di configurazione.

---

### Q4: Differenza tra Application e Infrastructure in 30 secondi?

**Mia risposta:** Application = cosa deve fare l'applicazione. Infrastructure = come lo fa.

✅ **Perfetto!** Risposta da senior.

**Versione ancora più concisa:**
> "Application definisce le regole del gioco. Infrastructure gioca la partita."

---

## Principio Fondamentale

> **Le dipendenze puntano VERSO IL CENTRO (Domain). Mai il contrario.**

Questo garantisce:
- **Testabilità** - Domain e Application testabili senza DB/servizi esterni
- **Sostituibilità** - Cambi provider modificando solo Infrastructure
- **Manutenibilità** - Chiaro dove mettere ogni tipo di codice

---

*Ultimo aggiornamento: 2026-02-02*
