---
tags:
  - solid
  - architecture
  - from/book
  - status/learned
aliases:
  - SRP
  - Single Responsibility
  - responsabilità singola
created: 2026-02-06
updated: 2026-02-06
source: "Clean Architecture (Robert C. Martin) - Capitolo 7"
---

# Single Responsibility Principle (SRP)

> **One-liner:** Un modulo dovrebbe essere responsabile verso un solo attore (stakeholder), non "fare una sola cosa".

## Il Fraintendimento Più Comune

La definizione "classica" che molti conoscono:

> *"Un modulo dovrebbe fare una sola cosa"*

**Questo è SBAGLIATO** - o meglio, è il principio di una **funzione**, non di un modulo/classe.

---

## La Vera Definizione (Uncle Bob)

### Versione 1 (incompleta):
> *"Un modulo dovrebbe avere un solo motivo per cambiare"*

### Versione 2 (completa):
> *"Un modulo dovrebbe essere responsabile verso un solo attore (stakeholder)"*

---

## La Differenza Chiave: Gli Attori

Non si tratta di "quante cose fa" il codice, ma di **chi lo usa** e **chi può chiedere modifiche**.

### Esempio: La Classe Employee che Viola SRP

```csharp
// ❌ VIOLA SRP - Serve TRE attori diversi!
public class Employee
{
    public decimal CalculatePay()    // → CFO (Contabilità)
    { /* ... */ }

    public HoursReport ReportHours() // → COO (Operations)
    { /* ... */ }

    public void Save()               // → CTO (Tecnico)
    { /* ... */ }
}
```

```
┌─────────────────────────────────────────────────────────────────┐
│  Classe Employee (VIOLA SRP)                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  calculatePay()     → serve il CFO (Contabilità)               │
│  reportHours()      → serve il COO (Operations)                │
│  save()             → serve il CTO (Tecnico)                   │
│                                                                 │
│  TRE attori diversi = TRE motivi per cambiare!                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Problema concreto:** Se il CFO chiede di modificare il calcolo degli straordinari, potresti accidentalmente rompere il report che serve al COO (usano lo stesso metodo interno per calcolare le ore).

---

## La Soluzione: Separare per Attore

```csharp
// ✅ RISPETTA SRP - Un servizio per attore

// Serve SOLO il CFO
public class PayCalculator
{
    public decimal CalculatePay(int employeeId)
    {
        // Se il CFO cambia le regole → modifico SOLO qui
    }
}

// Serve SOLO il COO
public class HourReporter
{
    public HoursReport GetHours(int employeeId)
    {
        // Se il COO vuole nuovo formato → modifico SOLO qui
    }
}

// Serve SOLO il CTO
public class EmployeeRepository
{
    public void Save(Employee employee)
    {
        // Se il CTO cambia database → modifico SOLO qui
    }
}
```

---

## SRP a Livello Architetturale

Il principio si scala a tutti i livelli:

| Livello | SRP significa... |
|---------|------------------|
| **Funzione** | Fa una sola cosa |
| **Classe** | Responsabile verso un solo attore |
| **Componente/Modulo** | Cambia per richieste di un solo gruppo di stakeholder |
| **Servizio** | Serve un solo bounded context / dominio |

### Esempio Architetturale

```
❌ MALE: Un servizio "PayrollService" che gestisce:
   - Calcolo stipendi (HR)
   - Report fiscali (Legal)
   - Previsioni budget (Finance)

✅ BENE: Tre servizi separati:
   - SalaryCalculationService → HR
   - TaxReportingService → Legal
   - BudgetForecastService → Finance
```

---

## Facade Pattern: Raggruppare senza Violare SRP

Come organizzi codice relativo allo stesso dominio (Employee) senza violare SRP?

**Usi una Facade** che raggruppa per dominio ma delega a servizi separati per attore.

```csharp
// La Facade: entry point semplificato
public class EmployeeFacade
{
    private readonly PayCalculator _payCalculator;
    private readonly HourReporter _hourReporter;
    private readonly EmployeeRepository _repository;

    public EmployeeFacade(
        PayCalculator payCalculator,
        HourReporter hourReporter,
        EmployeeRepository repository)
    {
        _payCalculator = payCalculator;
        _hourReporter = hourReporter;
        _repository = repository;
    }

    // DELEGA - la Facade non contiene logica!
    public decimal GetPay(int employeeId)
        => _payCalculator.CalculatePay(employeeId);

    public HoursReport GetHoursReport(int employeeId)
        => _hourReporter.GetHours(employeeId);

    public void SaveEmployee(Employee employee)
        => _repository.Save(employee);
}
```

### Schema Visivo

```
┌─────────────────────────────────────────────────────────────────┐
│                        CODICE CLIENT                            │
│                    (Controller, altri servizi)                  │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                      EmployeeFacade                             │
│         Entry point semplificato - raggruppa per DOMINIO        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  GetPay()   │  │ GetHours()  │  │   Save()    │   DELEGA    │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  PayCalculator  │ │  HourReporter   │ │ EmployeeRepo    │
│     (CFO)       │ │     (COO)       │ │     (CTO)       │
│                 │ │                 │ │                 │
│  LOGICA QUI!    │ │  LOGICA QUI!    │ │  LOGICA QUI!    │
│  Rispetta SRP   │ │  Rispetta SRP   │ │  Rispetta SRP   │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

### Perché la Facade non viola SRP?

| Aspetto | Facade | Servizi interni |
|---------|--------|-----------------|
| **Contiene logica?** | No, solo delega | Sì, tutta la logica |
| **Cambia se CFO chiede modifiche?** | No | Solo PayCalculator |
| **Cambia se COO chiede modifiche?** | No | Solo HourReporter |

La Facade è un **layer sottile di delega** - non ha "motivi per cambiare" legati agli attori.

---

## Riassunto: SRP Classico vs Architetturale

| Aspetto | "Classico" (sbagliato) | Uncle Bob (corretto) |
|---------|------------------------|----------------------|
| **Focus** | Cosa fa il codice | Chi usa il codice |
| **Domanda** | "Fa una sola cosa?" | "Serve un solo attore?" |
| **Metrica** | Numero di responsabilità | Numero di stakeholder |
| **Cambio** | "Cambia per un motivo" | "Cambia per richiesta di un solo gruppo" |

---

## Duplicazione Vera vs Accidentale

### Il Dilemma Pratico

> "Se 3 attori (X, Y, Z) oggi vogliono la stessa identica cosa, duplico il codice in 3 servizi?"

**Risposta:** Dipende dal TIPO di duplicazione.

### Duplicazione VERA (True Duplication)

Il codice è uguale **E cambierà insieme** per tutti gli attori.

```csharp
// Esempio: ValidateEmail() - se cambia, TUTTI vorranno la modifica
public class EmailValidator  // Condiviso - OK!
{
    public bool Validate(string email) { /* ... */ }
}
```

→ **Non duplicare.** Un servizio condiviso va bene.

### Duplicazione ACCIDENTALE (Accidental Duplication)

Il codice è uguale **OGGI**, ma potrebbe **divergere domani** perché serve attori diversi.

```csharp
// Esempio: CalculateRegularHours()
// - PayCalculator la usa per il CFO
// - HourReporter la usa per il COO

// OGGI: identiche
// DOMANI:
//   CFO: "Gli straordinari weekend valgono 1.5x"
//   COO: "A me serve il conteggio grezzo"
// → DIVERGONO!
```

→ **Separa** (anche con duplicazione iniziale).

### La Domanda Chiave

> **"Se l'attore X chiede una modifica, gli attori Y e Z vorranno la STESSA modifica?"**

| Risposta | Cosa fai |
|----------|----------|
| **Sì, sempre** | Servizio condiviso |
| **No, potrebbero divergere** | Servizi separati |
| **Non sono sicuro** | Approccio pragmatico |

### Approccio Pragmatico (Real World)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  1. INIZIA con codice condiviso (se oggi è identico)           │
│                 │                                               │
│                 ▼                                               │
│  2. MONITORA: un attore chiede qualcosa di diverso?            │
│                 │                                               │
│          ┌──────┴──────┐                                       │
│          │             │                                        │
│         NO            SÌ                                        │
│          │             │                                        │
│          ▼             ▼                                        │
│    Resta condiviso   SEPARA ORA                                │
│                      (refactoring)                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### DRY vs SRP

> **"Non aver paura della duplicazione se serve a disaccoppiare attori diversi."**
> — Uncle Bob

**DRY** (Don't Repeat Yourself) è importante, ma **non deve mai vincere su SRP**.

Duplicare codice che serve attori diversi ti **protegge** dal cambiare accidentalmente qualcosa per un attore quando ne modifichi un altro.

---

## La Regola d'Oro

> **Raggruppa per dominio, separa per attore.**
>
> L'API può essere unificata (Facade), ma l'implementazione deve rispettare SRP.

---

## Collegamenti

- [[facade-pattern|Facade Pattern]] - Pattern per raggruppare senza violare SRP
- [[dependency-inversion-principle|DIP]] - Complementare a SRP per architettura pulita
- [[clean-architecture]] - SRP applicato ai layer (da creare)

---

## Quiz

### Q1: Qual è la VERA definizione di SRP?

- A) Un modulo dovrebbe fare una sola cosa
- B) Un modulo dovrebbe avere un solo metodo pubblico
- C) Un modulo dovrebbe essere responsabile verso un solo attore
- D) Un modulo dovrebbe avere meno di 100 righe

**Mia risposta:**

---

### Q2: Violazione SRP

Hai una classe `ReportGenerator` con questi metodi:
- `GenerateSalesReport()` - usato dal team Sales
- `GenerateHRReport()` - usato dal team HR
- `GenerateFinanceReport()` - usato dal team Finance

Viola SRP? Se sì, come lo risolveresti?

**Mia risposta:**

---

### Q3: Facade e SRP

Un collega dice: "La EmployeeFacade viola SRP perché ha metodi che servono attori diversi". Come rispondi?

**Mia risposta:**

---

### Q4: Duplicazione Vera vs Accidentale

Hai una funzione `CalculateDiscount()` usata da:
- Team Sales (per preventivi clienti)
- Team Finance (per report margini)

Oggi è identica. È duplicazione vera o accidentale? Come decidi se separarla?

**Mia risposta:**

---

*Creato durante Sedimentazione Week 1*
