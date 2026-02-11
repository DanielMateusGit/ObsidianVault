---
tags:
  - p1
  - domain
  - entities
  - value-objects
  - patterns
  - from/week-02
  - status/learned
aliases:
  - Domain Model Patterns
  - Entity vs Value Object
  - Rich Domain Model
created: 2026-02-10
source: "Sessione Week 2 - P1 Notification Service"
---

# Domain Model Patterns

> **One-liner:** Patterns fondamentali per modellare il Domain Layer distinguendo tra Entities (hanno identità) e Value Objects (definiti solo dai loro valori), mantenendo il dominio ricco di comportamento.

---

## 🎯 Entity vs Value Object

### La Differenza Fondamentale

| Caratteristica | Entity | Value Object |
|----------------|--------|--------------|
| **Identità** | Ha un ID univoco | Definito solo dai suoi valori |
| **Mutabilità** | Può cambiare stato | Immutabile |
| **Equality** | Confronto per ID | Confronto per valore |
| **Ciclo di vita** | Persiste nel tempo | Usa e getta |

### Entity: Ha Identità

Un'**Entity** mantiene la sua identità anche se i suoi attributi cambiano.

```csharp
// 🏛️ ENTITY: Notification
var notification1 = new Notification(...);
notification1.Send();  // Cambia stato, ma è SEMPRE la stessa notification

// Anche se due notification avessero gli stessi dati...
var notificationA = new Notification("user@email.com", ...);
var notificationB = new Notification("user@email.com", ...);
// ...sono DUE notification DIVERSE (ID diversi)
```

**Quando usare Entity:**
- Ha un ciclo di vita (nasce, vive, muore)
- Viene tracciato nel tempo
- Ha un ID nel database
- Esempio: `User`, `Order`, `Notification`, `Template`

### Value Object: È il Suo Valore

Un **Value Object** è definito completamente dai suoi attributi. Due VO con gli stessi valori sono identici.

```csharp
// 💎 VALUE OBJECT: EmailAddress
var email1 = new EmailAddress("test@example.com");
var email2 = new EmailAddress("test@example.com");

email1 == email2  // TRUE! Stesso valore = stesso oggetto (concettualmente)
```

**Quando usare Value Object:**
- Rappresenta un concetto senza identità propria
- È immutabile (una volta creato, non cambia)
- Ha regole di validazione
- Esempio: `EmailAddress`, `Money`, `DateRange`, `Coordinates`

### Analogia del Mondo Reale

| Concetto | Entity o VO? | Perché |
|----------|--------------|--------|
| Persona | Entity | Marco Rossi rimane Marco Rossi anche se cambia indirizzo |
| Indirizzo | Value Object | "Via Roma 1, Milano" è uguale a "Via Roma 1, Milano" |
| Conto Bancario | Entity | Il conto #12345 esiste anche se il saldo cambia |
| Importo €100 | Value Object | €100 è uguale a €100, non ha identità propria |

---

## 💎 Value Objects in Dettaglio

### Caratteristiche Fondamentali

1. **Immutabilità** - Una volta creato, non cambia
2. **Self-validating** - Se non è valido, non esiste
3. **Equality by value** - Confronto basato sugli attributi
4. **Side-effect free** - Metodi che restituiscono nuovi oggetti

### Esempio: EmailAddress

```csharp
public class EmailAddress : IEquatable<EmailAddress>
{
    public string Value { get; }  // Solo getter, immutabile

    public EmailAddress(string email)
    {
        // Self-validating: invalido? Exception!
        if (!IsValidEmail(email))
            throw new ArgumentException("Invalid email");

        Value = email.ToLowerInvariant();  // Normalizzazione
    }

    // Equality by value
    public bool Equals(EmailAddress? other) => Value == other?.Value;

    // Helper methods (side-effect free)
    public string Domain => Value.Split('@')[1];
}
```

### Perché Value Objects Separati?

**❌ Sbagliato: String primitivo**
```csharp
public string Email { get; set; }  // Nessuna validazione!
// Qualcuno può passare "ciao" come email
```

**✅ Corretto: Value Object**
```csharp
public EmailAddress Email { get; }  // Sempre valido!
// new EmailAddress("ciao") → Exception immediata
```

**Vantaggi:**
- Validazione centralizzata (scrivi una volta, usi ovunque)
- Impossibile avere stato invalido
- Self-documenting (il tipo dice cosa contiene)
- Metodi helper dove servono (`email.Domain`)

---

## 📋 Template Pattern

### Il Problema

Senza template, i messaggi sono hardcoded:

```csharp
// ❌ Hardcoded ovunque
var body = $"Ciao {user.Name}, ordine #{order.Id} spedito!";
// Problemi: Marketing non può modificare, duplicazione, nessun versioning
```

### La Soluzione

**Template** = contenitore di contenuto parametrizzato con placeholder.

```csharp
// ✅ Template separato
var template = new Template(
    name: "order-shipped",
    body: "Ciao {{userName}}, ordine #{{orderId}} spedito!"
);

var data = new TemplateData(new Dictionary<string, string> {
    ["userName"] = "Mario",
    ["orderId"] = "12345"
});

var rendered = template.Render(data);
// "Ciao Mario, ordine #12345 spedito!"
```

### Quando Usare Template

| Situazione | Approccio |
|------------|-----------|
| Messaggi che cambiano spesso | ✅ Template |
| Contenuto gestito da non-dev | ✅ Template |
| Notifiche transazionali | ✅ Template |
| Log interni, alert tecnici | ❌ Hardcoded ok |
| Prototipo/MVP veloce | ❌ Hardcoded ok |

### Template è Entity, TemplateData è Value Object

- **Template** ha identità (ID, nome univoco, può essere modificato nel tempo)
- **TemplateData** è immutabile, definito solo dai suoi valori

---

## 🔄 Retry Pattern con DeliveryAttempt

### Il Problema

Quando una notifica fallisce, vogliamo ritentare. Ma dobbiamo tracciare:
- Quanti tentativi?
- Perché sono falliti?
- Quando?

### La Soluzione

**DeliveryAttempt** = record immutabile di un singolo tentativo.

```
Notification #123 (Priority: High → max 5 retry)
├── Attempt #1: Failed - "SMTP timeout"     (10:00)
├── Attempt #2: Failed - "SMTP timeout"     (10:05)
├── Attempt #3: Failed - "Connection refused" (10:10)
└── Attempt #4: Success                     (10:15) ✅
```

### Separazione delle Responsabilità

```csharp
// Notification: DECIDE se fare retry
public bool CanRetry(int attemptNumber) {
    var maxRetries = Priority switch {
        Priority.Low => 2,
        Priority.Normal => 3,
        Priority.High => 5,
        Priority.Critical => 10
    };
    return attemptNumber < maxRetries;
}

// DeliveryAttempt: REGISTRA il tentativo (non sa nulla di retry logic)
public class DeliveryAttempt {
    public void MarkAsSuccess() { ... }
    public void MarkAsFailed(string error) { ... }
}
```

**Notification** orchestra, **DeliveryAttempt** registra.

### DeliveryAttempt è Entity

Anche se sembra un "log", DeliveryAttempt è un'**Entity** perché:
- Ha un ID univoco
- Rappresenta un evento specifico nel tempo
- Due attempt con gli stessi dati sono comunque DUE attempt diversi

---

## 🏗️ Relazioni nel Domain Model

### Notification Service - Domain Model

```
┌─────────────────────────────────────────────────────────────┐
│                      ENTITIES                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐      ┌──────────────┐                     │
│  │ Notification │──1:N─│DeliveryAttempt│                     │
│  └──────┬───────┘      └──────────────┘                     │
│         │                                                    │
│         │ usa                                                │
│         ▼                                                    │
│  ┌──────────────┐                                           │
│  │   Template   │                                           │
│  └──────────────┘                                           │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                    VALUE OBJECTS                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐         │
│  │ Recipient   │  │TemplateData │  │ EmailAddress │         │
│  └─────────────┘  └─────────────┘  └──────────────┘         │
│                                                              │
│  ┌─────────────┐                                            │
│  │ PhoneNumber │                                            │
│  └─────────────┘                                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## ❓ Quiz di Verifica

### Q1: Entity o Value Object?
**Una transazione bancaria con ID, importo, data, e descrizione.**

<details>
<summary>Risposta</summary>

**Entity** - Ha un ID, rappresenta un evento specifico, tracciata nel tempo. Due transazioni con stesso importo e data sono comunque DUE transazioni diverse.

</details>

---

### Q2: Perché EmailAddress e PhoneNumber sono VO separati?

<details>
<summary>Risposta</summary>

Perché sono **concetti di dominio distinti** con regole di validazione diverse:
- EmailAddress: formato email, normalizzazione lowercase
- PhoneNumber: formato E.164, prefisso paese

Accorparli in `ContactInfo` forzerebbe logica condizionale interna → viola SRP.

</details>

---

### Q3: Chi decide se fare retry?
**Notification o DeliveryAttempt?**

<details>
<summary>Risposta</summary>

**Notification** decide (ha `CanRetry(attemptNumber)` che conosce la Priority).

**DeliveryAttempt** registra solo il singolo tentativo - non sa nemmeno di essere usato per retry. Separazione delle responsabilità!

</details>

---

### Q4: Questo codice è corretto?
```csharp
var email = new EmailAddress("test@example.com");
email.Value = "altro@example.com";  // Modifica
```

<details>
<summary>Risposta</summary>

**No!** Un Value Object è **immutabile**. `Value` ha solo getter, non setter.

Per "cambiare" email, crei un nuovo oggetto:
```csharp
var newEmail = new EmailAddress("altro@example.com");
```

</details>

---

### Q5: Template entity - quale metodo NON dovrebbe avere?

A) `Render(data)`
B) `SaveToDatabase()`
C) `Activate()`
D) `GetPlaceholders()`

<details>
<summary>Risposta</summary>

**B) SaveToDatabase()**

Un'Entity nel Domain Layer non sa che esiste un database! La persistenza è responsabilità dell'Infrastructure Layer (Repository pattern).

Il Domain è puro: business logic only, zero dipendenze esterne.

</details>

---

### Q6: Cosa succede qui?
```csharp
var recipient = Recipient.ForEmail("invalid-email");
```

<details>
<summary>Risposta</summary>

**ArgumentException!**

`Recipient.ForEmail()` crea internamente un `EmailAddress`, che è self-validating. Se l'email non è valida, l'oggetto non può esistere.

Questo è il vantaggio dei Value Objects: stato invalido = impossibile.

</details>

---

## Collegamenti

- [[clean-architecture]] - Dove si posiziona il Domain Model nell'architettura
- [[entities-and-clean-architecture]] - Approfondimento su Entities e Business Rules
- [[domain-events]] - Come le Entities comunicano cambiamenti di stato

---

## Risorse per Approfondire

- **Libro: "Domain-Driven Design" - Eric Evans, Cap. 5-6** - La fonte originale per Entities e Value Objects. Fondamentale.

- **[Martin Fowler - Value Object](https://martinfowler.com/bliki/ValueObject.html)** - Spiegazione concisa e pratica dei Value Objects.

- **[Martin Fowler - Domain Model](https://martinfowler.com/eaaCatalog/domainModel.html)** - Pattern catalog entry sul Domain Model.

- **Libro: "Implementing Domain-Driven Design" - Vaughn Vernon, Cap. 5-6** - Implementazione pratica con esempi .NET/Java.

- **[Effective Aggregate Design - Vaughn Vernon](https://www.dddcommunity.org/library/vernon_2011/)** - Serie di articoli su come progettare Aggregates (il prossimo step dopo Entities).

- **Libro: "Domain-Driven Design Distilled" - Vaughn Vernon** - Versione condensata per chi vuole i concetti chiave rapidamente.

---

*Creata: 2026-02-10*
*Argomenti: Entity vs Value Object, Template Pattern, Retry Pattern, Value Objects*
