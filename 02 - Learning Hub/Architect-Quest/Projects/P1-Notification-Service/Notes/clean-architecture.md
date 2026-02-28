---
tags:
  - p1
  - architecture
  - clean-architecture
  - from/week-01
  - status/learned
aliases:
  - Clean Architecture
  - Architettura Pulita
  - Uncle Bob Architecture
created: 2026-02-02
source: "Sessione Week 1 - P1 Notification Service"
---
x
# Clean Architecture

> **One-liner:** Pattern architetturale che organizza il codice in cerchi concentrici con dipendenze che puntano verso il centro (Domain), rendendo il sistema testabile, manutenibile e indipendente da framework.

---

## Cos'è

**Clean Architecture** è un pattern architetturale creato da **Robert C. Martin (Uncle Bob)** che organizza il codice in **4 layer concentrici** con una regola fondamentale: le dipendenze puntano SOLO verso il centro.

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

### La Regola d'Oro: Dependency Rule

> **Le dipendenze puntano SOLO verso il centro (Domain). I layer interni NON conoscono i layer esterni.**

```
Api ──────► Application ──────► Domain
               ▲
Infrastructure─┘
```

---

## Quando Usarlo

| Scenario | Adatto? |
|----------|---------|
| Progetti enterprise con logica business complessa | ✅ Sì |
| Sistemi che devono durare anni | ✅ Sì |
| Team multipli che lavorano su parti diverse | ✅ Sì |
| Progetti dove prevedi cambi di tecnologia | ✅ Sì |
| Microservizi con bounded context chiari | ✅ Sì |
| API con business rules importanti | ✅ Sì |

---

## Quando NON Usarlo

| Scenario | Perché |
|----------|--------|
| Script one-off o tool CLI semplici | Overkill, troppa struttura |
| Prototipi/MVP veloci | Rallenta lo sviluppo iniziale |
| CRUD semplice senza logica business | I 4 layer sono ridondanti |
| Progetti personali piccoli | Complessità non giustificata |
| Deadline strettissime | Setup iniziale richiede tempo |

**Regola pratica:** Se non hai business logic significativa, Clean Architecture è probabilmente overkill.

---

## Esempio

### I 4 Layer nel Dettaglio

#### 1. Domain (Il Cuore)

**Cosa contiene:** Entità business pure, value objects, regole di dominio.
**Dipendenze:** ZERO - non referenzia nulla.

```csharp
public class Notification
{
    public Guid Id { get; private set; }
    public NotificationStatus Status { get; private set; }

    // Solo logica business pura
    public bool CanRetry() => Status == NotificationStatus.Failed
                              && RetryCount < MaxRetries;
}
```

#### 2. Application (I Casi d'Uso)

**Cosa contiene:** Use cases, comandi, query, interfacce (porte).
**Dipendenze:** Solo Domain.

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

#### 3. Infrastructure (I Dettagli Tecnici)

**Cosa contiene:** Implementazioni concrete di DB, cache, servizi esterni.
**Dipendenze:** Application (implementa le interfacce).

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
```

#### 4. Api (Entry Point)

**Cosa contiene:** Controller, middleware, configurazione DI.
**Dipendenze:** Application + Infrastructure.

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

### Schema Chi Conosce Chi

| Layer | Può Conoscere |
|-------|--------------|
| **Domain** | Nessuno |
| **Application** | Domain |
| **Infrastructure** | Application (e Domain transitivo) |
| **Api** | Application, Infrastructure |

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

### 2. Application che chiama servizi esterni direttamente

```csharp
// ❌ SBAGLIATO
using SendGrid;

public class SendNotificationUseCase
{
    public async Task Execute(...)
    {
        var client = new SendGridClient("KEY");  // Accoppiato!
    }
}
```

### 3. Controller con logica business

```csharp
// ❌ SBAGLIATO
[HttpPost]
public async Task<IActionResult> Send(SendRequest request)
{
    if (notification.RetryCount > 3) { ... }  // Business logic qui!
    await _dbContext.SaveChangesAsync();
}
```

---

## Collegamenti

- [[entities-and-clean-architecture]] - Approfondimento su Entities in Clean Architecture
- [[domain-model-patterns]] - Entity vs Value Object
- [[adr-architecture-decision-records]] - Come documentare decisioni architetturali
- [[domain-events]] - Come comunicare tra layer senza accoppiamento

---

## Domande dalla Sessione

### D: Dove metteresti un'interfaccia `IEmailSender`? In quale layer e perché?

**R:** Nel layer Application: definisce "cosa deve fare il sistema" (porta). Infrastructure fornisce "come lo fa" (adattatore).

```
Application/Interfaces/IEmailSender.cs    ← "Il sistema deve poter inviare email"
Infrastructure/Email/SendGridEmailSender.cs : IEmailSender  ← "Ecco COME lo fa"
```

---

### D: Un junior vuole aggiungere `using Microsoft.EntityFrameworkCore;` nel Domain. Cosa gli dici?

**R:** Il Domain è il core riutilizzabile. Potrei usarlo per costruire l'applicazione A e l'applicazione B. Se dipende da EF Core, ogni progetto che usa questo Domain sarà costretto a portarsi dietro EF Core, anche se usa MongoDB o Dapper.

---

### D: Devi cambiare da SendGrid a Mailgun. Quali layer modifichi?

**R:** Solo Infrastructure (creo `MailgunEmailSender : IEmailSender`) + 1 riga nel DI. Domain e Application = zero modifiche. **Questo è il potere della Clean Architecture.**

---

### D: Differenza tra Application e Infrastructure in 30 secondi?

**R:** Application = cosa deve fare il sistema. Infrastructure = come lo fa.

> "Application definisce le regole del gioco. Infrastructure gioca la partita."

---

## Quiz

### Q1: Dove metteresti un'interfaccia `INotificationRepository`?

A) Domain
B) Application
C) Infrastructure
D) Api

<details>
<summary>Risposta</summary>

**A) Domain** (o B) Application - entrambi accettabili)

L'interfaccia è un'astrazione che il Domain/Application possiede. Infrastructure la implementa. Questo è il Dependency Inversion Principle.

</details>

---

### Q2: Un junior vuole aggiungere EF Core attributes nel Domain. È corretto?

<details>
<summary>Risposta</summary>

**No!** Il Domain deve essere puro, senza dipendenze da framework. Se aggiungi EF Core al Domain, perdi la possibilità di cambiare ORM senza toccare il Domain.

</details>

---

### Q3: Devi cambiare da SendGrid a Mailgun. Quali layer modifichi?

<details>
<summary>Risposta</summary>

| Layer | Modifiche |
|-------|-----------|
| Domain | ❌ Nessuna |
| Application | ❌ Nessuna (l'interfaccia resta uguale) |
| Infrastructure | ✅ Creo `MailgunEmailSender : IEmailSender` |
| Api | ✅ Cambio 1 riga nel DI |

</details>

---

### Q4: Quale dipendenza è CORRETTA?

A) Domain dipende da Infrastructure
B) Application dipende da Domain
C) Domain dipende da Application
D) Infrastructure dipende da Api

<details>
<summary>Risposta</summary>

**B) Application dipende da Domain**

Le dipendenze puntano verso il centro. Application può usare Domain, ma non viceversa.

</details>

---

## Risorse per Approfondire

- **[The Clean Architecture - Uncle Bob (Originale)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** - L'articolo che ha definito il pattern. Breve e fondamentale.

- **[Clean Architecture with ASP.NET Core - Jason Taylor](https://jasontaylor.dev/clean-architecture-getting-started/)** - Template pratico per .NET con esempi reali.

- **Libro: "Clean Architecture" - Robert C. Martin** - Cap. 20-22 in particolare. Il testo completo con tutti i dettagli.

- **[Summary of Clean Architecture - GitHub Gist](https://gist.github.com/ygrenzinger/14812a56b9221c9feca0b3621518635b)** - Riassunto visivo eccellente.

- **[Clean Architecture Solution Template](https://github.com/jasontaylordev/CleanArchitecture)** - Template GitHub pronto all'uso per .NET.

---

*Creata: 2026-02-02*
*Argomenti: Clean Architecture, Dependency Rule, 4 Layer, Uncle Bob*
