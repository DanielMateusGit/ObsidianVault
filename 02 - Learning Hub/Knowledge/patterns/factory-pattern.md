---
tags:
  - patterns
  - creational
  - dip
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - Factory
  - Abstract Factory
  - Factory Method
created: 2026-02-20
source: "Clean Architecture - Cap. 11 (DIP)"
---

# Factory Pattern

> **One-liner:** Delega la creazione di oggetti concreti a una Factory, permettendo al codice di alto livello di dipendere solo da astrazioni.

## Il Problema che Risolve

DIP dice: "dipendi da astrazioni, non da concrezioni". Ma **qualcuno** deve pur creare gli oggetti concreti!

```csharp
// ❌ Il problema: per creare devo conoscere il concreto
public class OrderService
{
    private readonly IOrderRepository _repository;

    public OrderService()
    {
        // 💀 Qui DEVO conoscere SqlOrderRepository!
        _repository = new SqlOrderRepository(); // Viola DIP!
    }
}
```

Anche se uso l'interfaccia, nel momento del `new` ho una dipendenza dal concreto.

## La Soluzione: Factory

La Factory **isola** la creazione di oggetti concreti in un punto controllato.

```csharp
// ✅ Factory che crea l'oggetto concreto
public interface IOrderRepositoryFactory
{
    IOrderRepository Create();
}

public class SqlOrderRepositoryFactory : IOrderRepositoryFactory
{
    public IOrderRepository Create() => new SqlOrderRepository();
}

// Il codice di alto livello dipende solo da astrazioni
public class OrderService
{
    private readonly IOrderRepository _repository;

    public OrderService(IOrderRepositoryFactory factory)
    {
        _repository = factory.Create(); // Non conosco il tipo concreto!
    }
}
```

## Dove Vivono le Factory?

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Application Layer          Infrastructure Layer              │
│   ┌─────────────────┐        ┌─────────────────────────┐       │
│   │                 │        │                         │       │
│   │  IRepository    │◄───────│  SqlRepository          │       │
│   │  (interfaccia)  │        │  (implementazione)      │       │
│   │                 │        │                         │       │
│   │  IFactory       │◄───────│  SqlRepositoryFactory   │       │
│   │  (interfaccia)  │        │  (implementazione)      │       │
│   │                 │        │                         │       │
│   └─────────────────┘        └─────────────────────────┘       │
│                                                                 │
│   Le INTERFACCE delle Factory stanno in Application            │
│   Le IMPLEMENTAZIONI stanno in Infrastructure                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Factory vs Dependency Injection

In pratica moderna, spesso usiamo **DI Container** invece di Factory esplicite:

```csharp
// Con DI Container (il modo moderno)
services.AddScoped<IOrderRepository, SqlOrderRepository>();

// Il container FA da factory automaticamente!
public class OrderService
{
    public OrderService(IOrderRepository repository) // Iniettato dal container
    {
    }
}
```

### Quando Serve Ancora la Factory?

| Situazione | Usa Factory |
|------------|-------------|
| Creazione condizionale (runtime logic) | ✅ Sì |
| Oggetti con parametri dinamici | ✅ Sì |
| Testing senza DI container | ✅ Sì |
| Creazione semplice, sempre lo stesso tipo | ❌ No, usa DI |

```csharp
// Factory utile: logica di creazione complessa
public class NotificationSenderFactory : INotificationSenderFactory
{
    public INotificationSender Create(NotificationType type)
    {
        return type switch
        {
            NotificationType.Email => new EmailSender(),
            NotificationType.Sms => new SmsSender(),
            NotificationType.Push => new PushSender(),
            _ => throw new ArgumentException()
        };
    }
}
```

## Varianti

| Variante | Descrizione |
|----------|-------------|
| **Factory Method** | Metodo in una classe che crea oggetti |
| **Abstract Factory** | Interfaccia per creare famiglie di oggetti correlati |
| **Simple Factory** | Classe dedicata solo alla creazione (non è un pattern GoF) |

## La Regola Chiave

> **Il codice che USA l'oggetto non deve sapere come CREARLO.**
>
> Factory = ponte tra "voglio un'astrazione" e "ecco l'implementazione concreta"

## Collegamenti

- [[dependency-inversion-principle]] - Factory abilita DIP isolando la creazione
- [[clean-architecture]] - Factory vive al confine tra layer
- [[facade-pattern]] — Spesso confusi: Factory crea, Facade semplifica
- [[open-closed-principle]] — Factory permette estensione senza modificare codice esistente
- [[repository-pattern]] — Repository usa spesso factory per creare entities

## Quiz

### Q1: Perché serve una Factory se ho DIP?
<details>
<summary>Risposta</summary>

Perché anche se il codice di alto livello usa un'interfaccia, al momento del `new` serve conoscere il tipo concreto. La Factory isola questa conoscenza in un punto controllato, solitamente in Infrastructure o nel Composition Root.
</details>

### Q2: Factory vs DI Container
Quando preferisci una Factory esplicita rispetto al DI Container?

<details>
<summary>Risposta</summary>

Quando hai logica di creazione condizionale (es. creare sender diversi in base al tipo di notifica), parametri dinamici noti solo a runtime, o quando vuoi testare senza DI container.
</details>
