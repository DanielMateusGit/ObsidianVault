---
tags:
  - architect-quest
  - p1
  - week-01
  - architecture
  - clean-architecture
  - solid
aliases:
  - Clean Arch
  - Onion Architecture
  - Hexagonal Architecture
created: 2026-02-03
updated: 2026-02-03
source: "Clean Architecture - Robert C. Martin (Cap. 1-14) + Sessione Week 1"
---

# Clean Architecture

> **One-liner:** Un'architettura dove le regole di business sono isolate e indipendenti da framework, database e UI - le dipendenze puntano sempre verso l'interno.

## Il Libro: Struttura (Cap. 1-14)

| Parte | Capitoli | Contenuto |
|-------|----------|-----------|
| I | 1-2 | Cos'è il Design |
| II | 3-6 | Paradigmi di Programmazione |
| III | 7-14 | Principi SOLID |

---

## PARTE I: Cos'è il Design? (Cap. 1-2)

### Il Goal dell'Architettura

> "The goal of software architecture is to **minimize the human resources** required to build and maintain the required system."

**Traduzione:** Una buona architettura rende facile aggiungere feature e correggere bug. Una cattiva architettura rende ogni modifica sempre più costosa.

### Il Segnale d'Allarme

Se ogni nuova feature richiede sempre più tempo, l'architettura sta fallendo:

```
Feature 1:  2 giorni
Feature 2:  3 giorni
Feature 3:  5 giorni   ← Debito tecnico
Feature 4:  8 giorni   ← che cresce
Feature 5: 13 giorni   ← esponenzialmente
```

### I Due Valori del Software

| Valore | Descrizione | Chi lo vuole |
|--------|-------------|--------------|
| **Behavior** | Cosa fa il software | Business (oggi) |
| **Structure** | Come è fatto | Business (domani) |

**Il conflitto:** I manager spingeranno sempre per behavior (feature ora!). Tu devi proteggere la structure (modificabilità futura).

### La Matrice di Eisenhower applicata

|  | Urgente | Non Urgente |
|--|---------|-------------|
| **Importante** | Behavior (bug critici) | **Structure** |
| **Non Importante** | Behavior (feature) | - |

> La Structure è **importante ma non urgente** - viene sempre rimandata, ma è ciò che determina la sopravvivenza del progetto.

---

## PARTE II: Paradigmi (Cap. 3-6)

Tre paradigmi, ognuno **toglie** qualcosa al programmatore:

### Structured Programming (Cap. 4)
**Toglie:** `goto` (salti arbitrari)
**Guadagni:** Flusso prevedibile (if/else, while, for)

### Object-Oriented Programming (Cap. 5)
**Toglie:** Accesso diretto alle funzioni (function pointers)
**Guadagni:**
- Encapsulation
- Inheritance
- **Polymorphism** ← IL più importante

**Perché OOP è fondamentale per architettura:**
Il polimorfismo permette la **Dependency Inversion** - il cuore di Clean Architecture.

```csharp
// SENZA polimorfismo: high-level dipende da low-level
class NotificationHandler {
    private SendGridClient _client;  // Dipendenza concreta!
}

// CON polimorfismo: high-level dipende da astrazione
class NotificationHandler {
    private IEmailSender _sender;    // Astrazione!
}
```

### Functional Programming (Cap. 6)
**Toglie:** Mutabilità (stato che cambia)
**Guadagni:**
- Niente race conditions
- Testabilità
- Predicibilità

---

## PARTE III: SOLID (Cap. 7-14)

I 5 principi per design a livello di classe/modulo.

### S - Single Responsibility Principle (Cap. 7)

> "Un modulo dovrebbe avere **una sola ragione per cambiare**"

**ATTENZIONE:** NON significa "una classe fa una sola cosa"!
**SIGNIFICA:** Una classe risponde a **un solo attore/stakeholder**.

```csharp
// ❌ MALE: Employee risponde a 3 attori
class Employee {
    CalculatePay()    // → CFO (Finance)
    ReportHours()     // → COO (Operations)
    Save()            // → CTO (Tech)
}

// ✅ BENE: Separati per attore
class PayCalculator { }      // Finance
class HourReporter { }       // Operations
class EmployeeRepository { } // Tech
```

**Perché importa:** Se Finance chiede una modifica a CalculatePay, rischi di rompere ReportHours che usa codice condiviso.

Vedi: [[srp|Single Responsibility Principle (dettaglio)]]

---

### O - Open/Closed Principle (Cap. 8)

> "Aperto per **estensione**, chiuso per **modifica**"

Dovresti poter aggiungere behavior senza modificare codice esistente.

```csharp
// ❌ MALE: Devo modificare per ogni nuovo canale
void Send(Notification n) {
    if (n.Channel == "email") SendEmail(n);
    else if (n.Channel == "sms") SendSms(n);
    // Aggiungo qui per ogni nuovo canale...
}

// ✅ BENE: Aggiungo nuova classe, non modifico nulla
interface INotificationSender { void Send(Notification n); }

class EmailSender : INotificationSender { }
class SmsSender : INotificationSender { }
class PushSender : INotificationSender { }  // NUOVO! Zero modifiche
```

Vedi: [[ocp|Open/Closed Principle (dettaglio)]]

---

### L - Liskov Substitution Principle (Cap. 9)

> "I sottotipi devono essere **sostituibili** ai loro tipi base"

Se `B` eredita da `A`, ovunque usi `A` devi poter usare `B` **senza sorprese**.

```csharp
// ❌ MALE: Square viola LSP
class Rectangle {
    virtual void SetWidth(int w) { width = w; }
    virtual void SetHeight(int h) { height = h; }
}

class Square : Rectangle {
    override void SetWidth(int w) {
        width = w;
        height = w;  // SORPRESA! Cambia anche height
    }
}

// Il chiamante si aspetta comportamento Rectangle
Rectangle r = new Square();
r.SetWidth(5);
r.SetHeight(10);
// r.Area() == 50? NO! È 100
```

Vedi: [[lsp|Liskov Substitution Principle (dettaglio)]]

---

### I - Interface Segregation Principle (Cap. 10)

> "I client non dovrebbero dipendere da metodi che **non usano**"

```csharp
// ❌ MALE: Interfaccia grassa
interface INotificationService {
    void SendEmail();
    void SendSms();
    void SendPush();
    void GenerateReport();  // Perché è qui?!
}

// ✅ BENE: Interfacce piccole e specifiche
interface IEmailSender { void SendEmail(); }
interface ISmsSender { void SendSms(); }
interface IReportGenerator { void GenerateReport(); }
```

Vedi: [[isp|Interface Segregation Principle (dettaglio)]]

---

### D - Dependency Inversion Principle (Cap. 11)

> "Dipendi da **astrazioni**, non da concretizzazioni"

**Questo è IL principio chiave di Clean Architecture.**

```csharp
// ❌ MALE: High-level dipende da low-level
class NotificationHandler {
    private SendGridClient _sendgrid = new SendGridClient();

    void Handle() {
        _sendgrid.Send(...);  // Accoppiato a SendGrid!
    }
}

// ✅ BENE: High-level dipende da astrazione
class NotificationHandler {
    private IEmailSender _sender;

    NotificationHandler(IEmailSender sender) {
        _sender = sender;  // Iniettato dall'esterno
    }
}

// L'implementazione concreta sta in Infrastructure
class SendGridEmailSender : IEmailSender { }
```

**Risultato:** Puoi cambiare SendGrid con Mailgun senza toccare `NotificationHandler`.

Vedi: [[dip|Dependency Inversion Principle (dettaglio)]]

---

## I 4 Layer di Clean Architecture

```
┌─────────────────────────────────────────┐
│              API Layer                  │  ← Controllers, Endpoints
│           (più esterno)                 │
├─────────────────────────────────────────┤
│          Infrastructure Layer           │  ← DB, External Services
│                                         │
├─────────────────────────────────────────┤
│          Application Layer              │  ← Use Cases, Commands
│                                         │
├─────────────────────────────────────────┤
│            Domain Layer                 │  ← Entities, Business Rules
│           (più interno)                 │  ← ZERO dipendenze esterne
└─────────────────────────────────────────┘
```

### La Dependency Rule

> **Le dipendenze puntano sempre verso l'INTERNO**

- Domain non dipende da nulla
- Application dipende solo da Domain
- Infrastructure dipende da Application e Domain
- API dipende da tutti

### Violazioni Comuni

| Violazione | Perché è male |
|------------|---------------|
| Domain importa EF Core | Domain accoppiato al database |
| Application chiama HttpClient | Application accoppiato a dettagli HTTP |
| Use case contiene SQL | Business logic mescolata con persistence |

---

## Collegamenti

- [[srp|Single Responsibility Principle]]
- [[ocp|Open/Closed Principle]]
- [[lsp|Liskov Substitution Principle]]
- [[isp|Interface Segregation Principle]]
- [[dip|Dependency Inversion Principle]]
- [[c4-model|C4 Model]] - per documentare Clean Architecture
- [[deep-modules|Deep Modules]] - complementare da Philosophy of Software Design

---

## Quiz

**Q1:** Secondo Uncle Bob, qual è il GOAL dell'architettura software?

- A) Massimizzare le performance
- B) Minimizzare le risorse umane per build e maintain
- C) Usare i design pattern corretti
- D) Seguire le best practice del framework

<details>
<summary>Risposta</summary>

**B) Minimizzare le risorse umane per build e maintain**

L'architettura è buona se rende facile modificare il sistema. Se ogni feature costa sempre di più, l'architettura sta fallendo.

</details>

---

**Q2:** Cosa significa REALMENTE il Single Responsibility Principle?

- A) Una classe ha un solo metodo
- B) Una classe fa una sola operazione
- C) Una classe risponde a un solo attore/stakeholder
- D) Una classe ha meno di 100 righe

<details>
<summary>Risposta</summary>

**C) Una classe risponde a un solo attore/stakeholder**

"Una sola ragione per cambiare" significa che solo UN attore (es. Finance, Operations, Tech) dovrebbe richiedere modifiche a quella classe.

</details>

---

**Q3:** In Clean Architecture, quale layer NON ha dipendenze esterne?

- A) API
- B) Infrastructure
- C) Application
- D) Domain

<details>
<summary>Risposta</summary>

**D) Domain**

Il Domain layer è il più interno e contiene solo entità e regole di business. Non dipende da framework, database, o servizi esterni.

</details>

---

**Q4:** Quale principio SOLID è il fondamento di Clean Architecture?

- A) Single Responsibility
- B) Open/Closed
- C) Liskov Substitution
- D) Dependency Inversion

<details>
<summary>Risposta</summary>

**D) Dependency Inversion**

DIP permette ai layer interni di definire interfacce che i layer esterni implementano. Questo inverte la direzione delle dipendenze e isola il business logic.

</details>

---

*Nota creata durante Week 1 - P1 Notification Service*
*Fonte: Clean Architecture (Robert C. Martin) Cap. 1-14*
