---
tags:
  - solid
  - architecture
  - from/book
  - status/learned
aliases:
  - OCP
  - Open Closed
  - aperto chiuso
created: 2026-02-06
updated: 2026-02-06
source: "Clean Architecture (Robert C. Martin) - Capitolo 8"
---

# Open/Closed Principle (OCP)

> **One-liner:** Un modulo dovrebbe essere aperto per estensione, chiuso per modifica - puoi aggiungere funzionalità senza modificare codice esistente.

## La Definizione

> **"Aperto per estensione, chiuso per modifica"**
>
> Dovresti poter aggiungere nuove funzionalità SENZA modificare il codice esistente.

---

## OCP a Livello di Classe (Classico)

L'esempio classico con le shape:

```csharp
// ❌ VIOLA OCP - Devo modificare per ogni nuovo tipo
public class AreaCalculator
{
    public double Calculate(object shape)
    {
        if (shape is Rectangle r)
            return r.Width * r.Height;
        else if (shape is Circle c)
            return Math.PI * c.Radius * c.Radius;
        // Nuovo Triangle? Devo MODIFICARE qui!
    }
}

// ✅ RISPETTA OCP - Aggiungo tipi senza toccare il calcolatore
public interface IShape
{
    double Area();
}

public class Rectangle : IShape
{
    public double Area() => Width * Height;
}

public class Circle : IShape
{
    public double Area() => Math.PI * Radius * Radius;
}

// Nuovo Triangle? Nuova classe, nessuna modifica!
public class Triangle : IShape
{
    public double Area() => Base * Height / 2;
}
```

---

## OCP a Livello Architetturale - Il Vero Potere

A livello di **architettura**, OCP risponde a questa domanda:

> **"Se il componente A deve essere PROTETTO dai cambiamenti del componente B, chi deve dipendere da chi?"**

### La Regola Fondamentale

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Se A deve essere PROTETTO da cambiamenti in B:               │
│                                                                 │
│                    B ──────► A                                  │
│                                                                 │
│   B dipende da A, NON il contrario!                            │
│   La direzione della dipendenza determina chi è protetto.      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Esempio Architetturale

Sistema con: Controller, Interactor (business logic), Database, Presenter.

**Domanda:** Cosa vogliamo PROTEGGERE di più?

La **business logic** (Interactor). Non deve cambiare se:
- Cambiamo da REST a GraphQL (Controller)
- Cambiamo da PostgreSQL a MongoDB (Database)
- Cambiamo il formato output (Presenter)

### Soluzione: Le Dipendenze Puntano Verso l'Interactor

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                      ┌──────────────┐                          │
│                      │  Controller  │                          │
│                      └──────┬───────┘                          │
│                             │ dipende da                       │
│                             ▼                                   │
│    ┌────────────────────────────────────────────────────┐      │
│    │                    INTERACTOR                       │      │
│    │              (Business Logic)                       │      │
│    │                                                     │      │
│    │   IPresenter ◄──────────────── IRepository         │      │
│    │       ▲                              ▲              │      │
│    └───────┼──────────────────────────────┼─────────────┘      │
│            │                              │                     │
│            │ implementa                   │ implementa          │
│    ┌───────┴───────┐              ┌───────┴───────┐            │
│    │   Presenter   │              │   Database    │            │
│    └───────────────┘              └───────────────┘            │
│                                                                 │
│    Le frecce puntano VERSO l'Interactor                        │
│    → L'Interactor è PROTETTO dai cambiamenti esterni           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Risultato Pratico

| Se cambia... | L'Interactor cambia? |
|--------------|---------------------|
| Controller (REST → GraphQL) | NO |
| Database (PostgreSQL → MongoDB) | NO |
| Presenter (JSON → XML) | NO |
| Business rules | SÌ (giustamente!) |

---

## OCP = Dependency Rule

Questo è esattamente il **Dependency Rule** di Clean Architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ESTERNO (Dettagli)          INTERNO (Policy)                │
│                                                                 │
│    ┌─────────────┐            ┌─────────────┐                  │
│    │   Database  │ ─────────► │   Domain    │                  │
│    │     API     │ ─────────► │   Business  │                  │
│    │     UI      │ ─────────► │   Rules     │                  │
│    └─────────────┘            └─────────────┘                  │
│                                                                 │
│    I dettagli dipendono dalle policy                           │
│    Le policy sono PROTETTE dai dettagli                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Come si Implementa OCP Architetturale?

Con le **interfacce** definite dal componente da proteggere:

```csharp
// L'Interactor DEFINISCE le interfacce nel suo layer
namespace Application
{
    public interface IOrderRepository
    {
        Order GetById(int id);
        void Save(Order order);
    }

    public class ProcessOrderUseCase
    {
        private readonly IOrderRepository _repository;

        public ProcessOrderUseCase(IOrderRepository repository)
        {
            _repository = repository;
        }

        public void Execute(int orderId)
        {
            var order = _repository.GetById(orderId);
            // Business logic...
            _repository.Save(order);
        }
    }
}

// L'implementazione sta in Infrastructure
namespace Infrastructure
{
    public class SqlOrderRepository : IOrderRepository
    {
        public Order GetById(int id) { /* SQL */ }
        public void Save(Order order) { /* SQL */ }
    }
}
```

**Risultato:** Cambio `SqlOrderRepository` → `MongoOrderRepository` senza toccare `ProcessOrderUseCase`.

---

## Plugin Architecture

OCP porta naturalmente alla **Plugin Architecture**:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                    ┌─────────────────┐                         │
│                    │   CORE SYSTEM   │                         │
│                    │  (Business Rules)│                         │
│                    │                  │                         │
│                    │  Defines:        │                         │
│                    │  - Interfaces    │                         │
│                    │  - Contracts     │                         │
│                    └────────┬─────────┘                         │
│                             │                                   │
│              ┌──────────────┼──────────────┐                   │
│              │              │              │                    │
│              ▼              ▼              ▼                    │
│    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │
│    │  Plugin A   │ │  Plugin B   │ │  Plugin C   │             │
│    │ (PostgreSQL)│ │  (SendGrid) │ │   (Stripe)  │             │
│    └─────────────┘ └─────────────┘ └─────────────┘             │
│                                                                 │
│    I plugin dipendono dal core                                 │
│    → Aggiungi/cambi plugin senza toccare il core               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## La Connessione tra i Principi

```
OCP (voglio proteggere A da B)
         │
         ▼
DIP (B dipende da interfaccia definita da A)
         │
         ▼
Dependency Rule (dipendenze verso l'interno)
         │
         ▼
Clean Architecture!
```

---

## Riassunto

| Livello | OCP significa... | Come si implementa |
|---------|------------------|-------------------|
| **Classe** | Aggiungo comportamenti senza modificare | Interfacce, Strategy, Polimorfismo |
| **Architettura** | Componenti importanti protetti da cambiamenti esterni | DIP, Dependency Rule |

---

## Collegamenti

- [[dependency-inversion-principle|DIP]] - Il meccanismo che abilita OCP
- [[single-responsibility-principle|SRP]] - Complementare: separa per attore
- [[clean-architecture]] - OCP è il cuore della Dependency Rule (da creare)
- [[facade-pattern|Facade]] - Può essere un punto di estensione
- [[liskov-substitution-principle]] — LSP garantisce che le estensioni OCP funzionino
- [[interface-segregation-principle]] — Interfacce piccole facilitano estensioni OCP
- [[factory-pattern]] — Factory è un meccanismo comune per estendere senza modificare

---

## Quiz

### Q1: OCP Architetturale

Hai un sistema dove il `PaymentService` (business logic) usa direttamente `StripeClient`. Il CEO dice: "Aggiungiamo anche PayPal".

Cosa c'è di sbagliato nell'architettura attuale? Come la risolvi per rispettare OCP?

**Mia risposta:** Violiamo OCP. PaymentService non dovrebbe essere un servizio concreto, ma un'interfaccia (`IPaymentService`) che contiene la business logic (es. `Pay()`). Vogliamo proteggere questa logica da modifiche ma aprirla per estensioni. StripeClient dovrebbe dipendere da IPaymentService, non il contrario (DIP), diventando un servizio "plug and play". PayPal diventa un'altra implementazione di IPaymentService - un'estensione, non una modifica.

✅ **Corretto** - Pattern completo: interfaccia nel layer business, implementazioni come plugin.

---

### Q2: Direzione delle Dipendenze

Se vuoi che il tuo `OrderProcessor` sia PROTETTO da cambiamenti nel `DatabaseRepository`, chi deve dipendere da chi?

- A) OrderProcessor dipende da DatabaseRepository
- B) DatabaseRepository dipende da OrderProcessor (tramite interfaccia)
- C) Entrambi dipendono da un terzo modulo
- D) Non ha importanza

**Mia risposta:** B

✅ **Corretto** - L'interfaccia è definita da OrderProcessor, DatabaseRepository la implementa.

---

### Q3: Plugin Architecture

Spiega perché la Plugin Architecture è una conseguenza naturale di OCP. Fai un esempio pratico.

**Mia risposta:** Perché "dismettere o aggiungere servizi" diventa semplice - i servizi diventano "plugin" dipendenti dal core che non cambia mai. NON IL CONTRARIO.

✅ **Corretto** - Il core definisce i contratti, i plugin li implementano. Aggiungi/rimuovi plugin senza toccare il core.

---

*Creato durante Sedimentazione Week 1*
