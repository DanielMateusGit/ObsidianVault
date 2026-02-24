---
tags:
  - solid
  - architecture
  - from/book
  - from/week-01
  - status/learned
aliases:
  - DIP
  - Dependency Inversion
  - inversione delle dipendenze
created: 2026-02-05
updated: 2026-02-20
source: "Clean Architecture (Robert C. Martin) - Capitolo 11"
---

# Dependency Inversion Principle (DIP)

> **One-liner:** I moduli di alto livello non devono dipendere da quelli di basso livello. Entrambi devono dipendere da astrazioni.

## Il Problema: L'Albero delle Dipendenze Tradizionale

Nel codice tradizionale, le dipendenze seguono una struttura **ad albero**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DIPENDENZE TRADIZIONALI                     │
│                                                                 │
│                      ┌─────────────────┐                       │
│                      │   HIGH LEVEL    │                       │
│                      │  (Controller)   │                       │
│                      └────────┬────────┘                       │
│                               │ dipende da                     │
│                               ▼                                │
│                      ┌─────────────────┐                       │
│                      │  MEDIUM LEVEL   │                       │
│                      │   (Service)     │                       │
│                      └────────┬────────┘                       │
│                               │ dipende da                     │
│                               ▼                                │
│                      ┌─────────────────┐                       │
│                      │   LOW LEVEL     │                       │
│                      │  (Repository)   │                       │
│                      └─────────────────┘                       │
│                                                                 │
│    PROBLEMA: Il codice più importante (business logic)         │
│    dipende dal codice meno importante (dettagli tecnici)       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Esempio Concreto del Problema

```csharp
// ❌ SENZA DIP: Alto livello dipende da basso livello

// Low level - dettaglio implementativo
public class SqlServerRepository
{
    public Order GetOrder(int id)
    {
        // Query SQL Server specifica
        using var conn = new SqlConnection(_connectionString);
        // ...
    }
}

// High level - business logic IMPORTANTE
public class OrderService
{
    // 😱 OrderService DIPENDE da SqlServerRepository!
    private readonly SqlServerRepository _repository;

    public OrderService()
    {
        _repository = new SqlServerRepository(); // Accoppiamento stretto!
    }

    public void ProcessOrder(int orderId)
    {
        var order = _repository.GetOrder(orderId);
        // Business logic...
    }
}
```

**Problemi:**
1. Per testare `OrderService` devo avere SQL Server
2. Per cambiare database devo modificare `OrderService`
3. La business logic (importante) dipende da dettagli tecnici (meno importanti)

---

## La Soluzione: Inversione delle Dipendenze

L'idea chiave è inserire un'**interfaccia** tra i due livelli:

```
┌─────────────────────────────────────────────────────────────────┐
│                  DEPENDENCY INVERSION                          │
│                                                                 │
│         ┌─────────────────┐                                    │
│         │   HIGH LEVEL    │                                    │
│         │  (OrderService) │                                    │
│         └────────┬────────┘                                    │
│                  │ dipende da                                  │
│                  ▼                                              │
│      ┌───────────────────────┐  ◄── Owned by high level!      │
│      │     «interface»       │                                 │
│      │   IOrderRepository    │                                 │
│      └───────────────────────┘                                 │
│                  ▲                                              │
│                  │ implementa                                  │
│         ┌────────┴────────┐                                    │
│         │   LOW LEVEL     │                                    │
│         │ SqlServerRepo   │                                    │
│         └─────────────────┘                                    │
│                                                                 │
│    ENTRAMBI dipendono dall'astrazione!                        │
│    La freccia verso SqlServerRepo è INVERTITA                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### L'Inversione Spiegata

```
PRIMA (Tradizionale):           DOPO (DIP):

OrderService                    OrderService
     │                               │
     │ dipende da                    │ dipende da
     ▼                               ▼
SqlServerRepository             IOrderRepository ◄─┐
                                                   │ implementa
                                     SqlServerRepo ─┘

La DIREZIONE della dipendenza verso SqlServerRepo è INVERTITA!
Prima: Service → Repo
Dopo:  Service → Interface ← Repo
```

### Codice con DIP

```csharp
// ✅ CON DIP: Entrambi dipendono dall'astrazione

// L'INTERFACCIA - posseduta dal livello alto (Domain/Application)
public interface IOrderRepository
{
    Order GetOrder(int id);
    void Save(Order order);
}

// HIGH LEVEL - dipende SOLO dall'interfaccia
public class OrderService
{
    private readonly IOrderRepository _repository; // Interfaccia!

    // Dependency Injection nel costruttore
    public OrderService(IOrderRepository repository)
    {
        _repository = repository;
    }

    public void ProcessOrder(int orderId)
    {
        var order = _repository.GetOrder(orderId);
        // Business logic...
    }
}

// LOW LEVEL - IMPLEMENTA l'interfaccia
public class SqlServerOrderRepository : IOrderRepository
{
    public Order GetOrder(int id)
    {
        // Dettagli SQL Server
    }

    public void Save(Order order)
    {
        // Dettagli SQL Server
    }
}

// ALTERNATIVA - Posso cambiare implementazione senza toccare OrderService!
public class MongoOrderRepository : IOrderRepository
{
    public Order GetOrder(int id)
    {
        // Dettagli MongoDB
    }

    public void Save(Order order)
    {
        // Dettagli MongoDB
    }
}
```

---

## Chi "Possiede" l'Interfaccia?

**Punto critico:** L'interfaccia deve essere definita nel **livello alto**, non in quello basso!

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  APPLICATION LAYER (alto livello)                              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  OrderService.cs                                         │  │
│  │  IOrderRepository.cs  ◄── L'interfaccia sta QUI!        │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  INFRASTRUCTURE LAYER (basso livello)                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  SqlServerOrderRepository.cs  (implementa IOrderRepo)    │  │
│  │  MongoOrderRepository.cs      (implementa IOrderRepo)    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Infrastructure DIPENDE da Application, non viceversa!         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Questo è esattamente il **Dependency Rule** di Clean Architecture!

---

## La Storia in C: Come OOP ha Reso DIP Pratico

Prima di OOP, il polimorfismo esisteva ma era manuale e pericoloso:

```c
// Polimorfismo "a mano" in C - funzionava, ma era fragile

// "Interfaccia" definita come struct con puntatori a funzione
typedef struct {
    Order* (*getOrder)(int id);
    void (*save)(Order* order);
} OrderRepositoryVTable;

// "Implementazione" SQL Server
Order* sqlserver_getOrder(int id) { /* ... */ }
void sqlserver_save(Order* order) { /* ... */ }

OrderRepositoryVTable sqlServerRepo = {
    .getOrder = sqlserver_getOrder,
    .save = sqlserver_save
};

// Uso polimorfo
void processOrder(OrderRepositoryVTable* repo, int orderId) {
    Order* order = repo->getOrder(orderId);  // Polimorfismo!
    // ...
}

// MA: Nessun controllo del compilatore! Errori a runtime!
```

**OOP** ha reso questo pattern:
- **Sicuro** (il compilatore verifica che implementi tutti i metodi)
- **Conveniente** (sintassi `class : interface`)
- **Standard** (tutti lo fanno allo stesso modo)

---

## DIP in Clean Architecture

In Clean Architecture, DIP è **IL** principio che permette la Dependency Rule:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                    ┌─────────────────┐                         │
│                    │     DOMAIN      │  Entità, Value Objects  │
│                    │                 │  ZERO dipendenze        │
│                    └────────▲────────┘                         │
│                             │                                   │
│              ┌──────────────┴──────────────┐                   │
│              │        APPLICATION          │  Use Cases        │
│              │  IOrderRepository (qui!)    │  Interfacce       │
│              └──────────────▲──────────────┘                   │
│                             │                                   │
│    ┌────────────────────────┴────────────────────────┐         │
│    │              INFRASTRUCTURE                      │         │
│    │  SqlServerOrderRepository : IOrderRepository    │         │
│    │  SendGridEmailService : IEmailService           │         │
│    └──────────────────────────────────────────────────┘         │
│                                                                 │
│    Le frecce puntano verso l'INTERNO (Dependency Rule)         │
│    Possibile SOLO grazie a DIP!                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Benefici Concreti

| Beneficio | Senza DIP | Con DIP |
|-----------|-----------|---------|
| **Testing** | Serve DB reale | Mock dell'interfaccia |
| **Cambio DB** | Modifica ovunque | Solo nuova implementazione |
| **Sviluppo parallelo** | Bloccato dal DB team | Team indipendenti |
| **Business logic** | Inquinata da dettagli | Pura, isolata |

### Testing con DIP

```csharp
// Test FACILE con DIP - nessun database necessario
public class OrderServiceTests
{
    [Fact]
    public void ProcessOrder_WithValidOrder_CompletesSuccessfully()
    {
        // Arrange - Mock dell'interfaccia
        var mockRepo = new Mock<IOrderRepository>();
        mockRepo.Setup(r => r.GetOrder(1))
                .Returns(new Order { Id = 1, Status = "Pending" });

        var service = new OrderService(mockRepo.Object);

        // Act
        service.ProcessOrder(1);

        // Assert
        mockRepo.Verify(r => r.Save(It.IsAny<Order>()), Times.Once);
    }
}
```

---

## Dependency Inversion vs Dependency Injection

**Non sono la stessa cosa!**

| Concetto | Cos'è | Livello |
|----------|-------|---------|
| **Dependency Inversion** | Principio di design (la "D" di SOLID) | Architetturale |
| **Dependency Injection** | Tecnica per passare dipendenze | Implementativo |

```csharp
// Dependency INVERSION: struttura delle dipendenze
// (OrderService dipende da interfaccia, non implementazione)

// Dependency INJECTION: come passiamo la dipendenza
public class OrderService
{
    private readonly IOrderRepository _repository;

    // Constructor Injection - UNA tecnica di DI
    public OrderService(IOrderRepository repository)
    {
        _repository = repository;
    }
}

// La configurazione DI (es. in Program.cs) è dove le cose si collegano
services.AddScoped<IOrderRepository, SqlServerOrderRepository>();
```

DIP è il **perché**, DI è il **come**.

---

## Quando NON Usare DIP

Non tutto deve essere astratto! Uncle Bob stesso avverte: non creare interfacce per tutto.

**Non serve DIP quando:**
- Classe stabile che non cambierà (es. `String`, `DateTime`)
- Nessun bisogno di testing in isolamento
- Implementazione unica garantita per sempre
- Costo dell'astrazione > beneficio

```csharp
// ❌ OVER-ENGINEERING: interfaccia inutile
public interface IStringHelper
{
    string ToUpper(string s);
}

// ✅ OK: usa direttamente
var upper = myString.ToUpper();
```

---

## Factory: Il Ponte per la Creazione

DIP dice "dipendi da astrazioni", ma **qualcuno** deve pur creare l'oggetto concreto. Qui entra la **Factory**:

```csharp
// ❌ Il problema: per fare new devo conoscere il concreto
_repository = new SqlOrderRepository(); // Viola DIP!

// ✅ La soluzione: Factory isola la creazione
public interface IRepositoryFactory
{
    IOrderRepository Create();
}

// Il codice di alto livello non sa mai quale concreto viene creato
public OrderService(IRepositoryFactory factory)
{
    _repository = factory.Create();
}
```

> **In pratica:** I DI Container moderni fanno da Factory automatica, ma Factory esplicite servono per logica di creazione condizionale.

Vedi: [[factory-pattern]]

---

## Collegamenti

- [[factory-pattern]] - Abilita DIP isolando la creazione di oggetti concreti
- [[programming-paradigms]] - Come OOP ha reso DIP pratico
- [[clean-architecture]] - DIP abilita la Dependency Rule
- [[interface-segregation-principle]] - ISP complementa DIP
- [[open-closed-principle]] - OCP e DIP lavorano insieme

---

## Quiz

### Q1: Hai una classe `OrderService` che usa direttamente `SqlServerRepository`. Cosa c'è di sbagliato e come lo risolvi?

**Mia risposta:** _[Da completare]_

---

### Q2: Qual è la differenza tra Dependency Inversion e Dependency Injection?

- A) Sono la stessa cosa, nomi diversi
- B) Inversion è un principio architetturale, Injection è una tecnica implementativa
- C) Injection è il principio, Inversion è la tecnica
- D) Inversion si usa in Java, Injection in C#

**Mia risposta:** _[Da completare]_

---

### Q3: Dove deve stare l'interfaccia `IOrderRepository`?

- A) Nel layer Infrastructure, vicino all'implementazione
- B) In un progetto "Shared" separato
- C) Nel layer Application/Domain (alto livello)
- D) Non importa, basta che esista

**Mia risposta:** C

✅ **Corretto** - L'interfaccia è "posseduta" dal livello alto. Il livello alto definisce di cosa ha bisogno, il livello basso implementa quel contratto. Così la dipendenza si inverte: Infrastructure dipende da Application.

---

## Ti è piaciuto parlare di DIP? Allora impazzirai per:

- **[The Dependency Inversion Principle](https://web.archive.org/web/20110714224327/http://www.objectmentor.com/resources/articles/dip.pdf)** (Uncle Bob, 1996) - Il paper originale dove DIP è stato formalizzato. Più profondo del libro, con esempi in C++ che mostrano l'evoluzione storica.

- **[Dependency Injection Principles, Practices, and Patterns](https://www.manning.com/books/dependency-injection-principles-practices-patterns)** (Mark Seemann, 2019) - IL libro su DI in .NET. Va oltre il "come" e spiega il "perché". Capitoli su Pure DI vs Container, Composition Root, e anti-pattern comuni.

---

*Creato durante Sedimentazione Week 1*
