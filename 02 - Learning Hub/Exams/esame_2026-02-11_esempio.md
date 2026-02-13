---
tags: [exam, p1, week-02, domain-model, esempio]
date: 2026-02-11
tipo: mini-verifica
punti_totali: 15
argomenti:
  - "Clean Architecture"
  - "Domain Model (Entities, Value Objects)"
  - "Domain Events"
voto: null
status: pending
---

# 🎓 Mini-Verifica - Week 2: Domain Model

> **Tempo stimato:** ~15 minuti
> **Argomenti:** Clean Architecture, Entities, Value Objects, Domain Events

---

## 📝 PARTE A: Domande Aperte (6 punti)

### A1. Clean Architecture - Dependency Rule (2 punti)

Spiega la **Dependency Rule** di Clean Architecture. In quale direzione devono andare le dipendenze e perché?

**Risposta:**
> _[Scrivi qui la tua risposta]_

---

### A2. Entity vs Value Object (2 punti)

Qual è la differenza fondamentale tra un **Entity** e un **Value Object**? Fai un esempio concreto dal progetto Notification Service.

**Risposta:**
> _[Scrivi qui la tua risposta]_

---

### A3. Domain Events - Perché? (2 punti)

Perché usiamo i Domain Events invece di chiamare direttamente i servizi esterni (es. inviare email) dall'interno dell'Entity?

**Risposta:**
> _[Scrivi qui la tua risposta]_

---

## ✅ PARTE B: Domande Chiuse (4 punti)

### B1. Quale layer contiene le business rules in Clean Architecture? (1 punto)
- [ ] A) Infrastructure Layer
- [ ] B) Application Layer
- [ ] C) Domain Layer
- [ ] D) Presentation Layer

### B2. Un Value Object... (1 punto)
- [ ] A) Ha sempre un ID univoco
- [ ] B) Può essere modificato dopo la creazione
- [ ] C) È definito solo dai suoi attributi (immutabile)
- [ ] D) Deve ereditare da una classe base Entity

### B3. Quando viene "dispatchato" un Domain Event? (1 punto)
- [ ] A) Immediatamente quando l'Entity cambia stato
- [ ] B) Dopo il SaveChanges del database
- [ ] C) Prima della validazione
- [ ] D) Solo se l'utente lo richiede esplicitamente

### B4. Nel Rich Domain Model, dove sta la logica di business? (1 punto)
- [ ] A) Nei Controller
- [ ] B) Nei Service esterni al dominio
- [ ] C) Dentro le Entity stesse
- [ ] D) Nel database tramite stored procedures

---

## 💻 PARTE C: Codice (5 punti)

### C1. Trova l'errore (2 punti)

Questo codice viola un principio del Rich Domain Model. Qual è il problema e come lo correggeresti?

```csharp
// NotificationService.cs (Application Layer)
public class NotificationService
{
    public void SendNotification(Notification notification)
    {
        // Cambio lo stato direttamente
        notification.Status = NotificationStatus.Sent;
        notification.SentAt = DateTime.UtcNow;

        _repository.Update(notification);
    }
}
```

**Problema identificato:**
> _[Scrivi qui]_

**Correzione:**
```csharp
// Scrivi qui il codice corretto
```

---

### C2. Completa il Value Object (3 punti)

Completa questo Value Object `EmailAddress` seguendo le best practices (immutabilità, validazione nel costruttore, uguaglianza per valore):

```csharp
public class EmailAddress
{
    // Completa l'implementazione
    // Deve:
    // 1. Essere immutabile
    // 2. Validare il formato email
    // 3. Implementare uguaglianza per valore



}
```

**La tua implementazione:**
```csharp
// Scrivi qui
```

---

## 📊 VALUTAZIONE (compilare dopo correzione)

| Parte | Punti Max | Punti Ottenuti |
|-------|-----------|----------------|
| A - Domande Aperte | 6 | |
| B - Domande Chiuse | 4 | |
| C - Codice | 5 | |
| **TOTALE** | **15** | |

### Voto Finale: __/15

### Soglie:
- ≥13/15: Eccellente (+75 XP)
- ≥11/15: Buono (+50 XP)
- ≥9/15: Sufficiente (+30 XP)
- <9/15: Ripasso consigliato (+15 XP)

### Feedback Claude:
> _[Da compilare dopo la correzione]_

### Aree da Ripassare:
- [ ] _[Da compilare se necessario]_

---

**Istruzioni:**
1. Compila le risposte direttamente in questo file
2. Per le domande chiuse, metti una `x` nella casella: `- [x]`
3. Quando hai finito, dì a Claude: "Ho finito l'esame"
4. Claude correggerà e assegnerà il voto

---

*Creato: 2026-02-11 | Argomenti: Week 1-2 P1 Notification Service*
