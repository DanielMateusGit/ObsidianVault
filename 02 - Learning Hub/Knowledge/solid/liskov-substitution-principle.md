---
tags:
  - solid
  - lsp
  - architecture
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - LSP
  - Liskov
  - Principio di Sostituzione
created: 2026-02-20
source: "Clean Architecture - Cap. 9"
---

# Liskov Substitution Principle (LSP)

> **One-liner:** Se puoi sostituire un oggetto di tipo S con uno di tipo T senza rompere il comportamento del sistema, allora S e T sono sottotipi della stessa astrazione.

## Cos'è

Il Liskov Substitution Principle, formulato da Barbara Liskov nel 1988, definisce una proprietà fondamentale della sostituibilità:

> *"Se per ogni oggetto o1 di tipo S esiste un oggetto o2 di tipo T tale che, per tutti i programmi P definiti in termini di T, il comportamento di P rimane invariato quando o1 viene sostituito con o2, allora S è un sottotipo di T."*

**In parole semplici:** Le classi derivate devono essere sostituibili con le loro classi base senza alterare il comportamento corretto del programma.

### Dalla OOP all'Architettura

LSP nasce come principio per gestire l'**ereditarietà** in modo corretto, ma Uncle Bob lo estende all'**architettura software**:

- **OOP Level:** Classi e interfacce interscambiabili
- **Architecture Level:** Servizi, API, componenti intercambiabili (Ports & Adapters)

Il pattern **Ports & Adapters** è l'applicazione architettonica di LSP: una Port (interfaccia) con molti Adapters (implementazioni) sostituibili.

## Quando usarlo

- **Sempre** quando definisci gerarchie di tipi (interfacce, classi astratte)
- Quando progetti **plugin architecture** (più implementazioni intercambiabili)
- Quando definisci **API contracts** che altri devono rispettare
- Nel pattern **Strategy** (strategie intercambiabili)
- In **Dependency Injection** (le implementazioni devono rispettare il contratto)

## Quando NON usarlo (violazioni da evitare)

- **Mai** creare sottotipi che "quasi" rispettano il contratto
- **Mai** aggiungere eccezioni/if speciali per gestire un sottotipo specifico
- **Mai** restringere il comportamento della classe base in un sottotipo

## Esempio 1: License (Corretto)

```csharp
// ✅ LSP rispettato - entrambe le licenze sono intercambiabili
public interface ILicense
{
    decimal CalculateFee();
}

public class PersonalLicense : ILicense
{
    public decimal CalculateFee() => 99.00m;
}

public class BusinessLicense : ILicense
{
    private readonly int _userCount;

    public BusinessLicense(int userCount) => _userCount = userCount;

    public decimal CalculateFee() => _userCount * 49.00m;
}

// Il BillingSystem funziona con QUALSIASI ILicense
// Non sa e non gli importa quale implementazione sta usando
public class BillingSystem
{
    public Invoice CreateInvoice(ILicense license)
    {
        var fee = license.CalculateFee(); // Funziona sempre!
        return new Invoice(fee);
    }
}
```

**Perché funziona:** `PersonalLicense` e `BusinessLicense` rispettano completamente il contratto di `ILicense`. Il `BillingSystem` può usare indifferentemente l'una o l'altra.

## Esempio 2: Rectangle/Square (Violazione Classica)

```csharp
// ❌ VIOLAZIONE LSP - L'esempio classico
public class Rectangle
{
    public virtual int Width { get; set; }
    public virtual int Height { get; set; }

    public int Area() => Width * Height;
}

public class Square : Rectangle
{
    public override int Width
    {
        set { base.Width = value; base.Height = value; }
    }

    public override int Height
    {
        set { base.Width = value; base.Height = value; }
    }
}
```

**Il problema:**

```csharp
void ProcessRectangle(Rectangle r)
{
    r.Width = 5;
    r.Height = 10;

    // Mi aspetto Area = 50
    Debug.Assert(r.Area() == 50); // ❌ FALLISCE con Square! (Area = 100)
}

// Square rompe le aspettative di chi usa Rectangle
ProcessRectangle(new Rectangle()); // ✅ OK - Area = 50
ProcessRectangle(new Square());    // ❌ BOOM - Area = 100
```

**Perché viola LSP:** Un `Square` non può sostituire un `Rectangle` senza rompere il comportamento. Anche se matematicamente un quadrato È un rettangolo, nel codice il `Square` cambia il comportamento atteso (settare Width non deve modificare Height).

**Soluzione:** Non usare ereditarietà. Creare un'interfaccia `IShape` con `Area()` e due implementazioni separate.

## Esempio 3: Taxi Dispatch (Violazione Architettonica)

Scenario dal libro: Un sistema di dispatch taxi che aggrega più compagnie.

```
Sistema Dispatch
      │
      ▼
┌─────────────────────────────────────────────────┐
│           REST API Contract                     │
│  PUT /driver/{id}/destination                   │
│  { "destination": "123 Main St" }               │
└─────────────────────────────────────────────────┘
      │
      ├──► Acme Taxi     ✅ PUT /driver/{id}/destination
      ├──► Purple Cab    ✅ PUT /driver/{id}/destination
      └──► Bob's Taxi    ❌ PUT /driver/{id}/dest  ← VIOLAZIONE!
```

**Il problema:**

```csharp
// Il sistema deve gestire l'eccezione
public class TaxiDispatcher
{
    public void SendDestination(string driverId, string destination, string company)
    {
        if (company == "BobsTaxi")
        {
            // ❌ Eccezione! Codice speciale per un solo provider
            _http.Put($"/driver/{driverId}/dest", destination);
        }
        else
        {
            // Tutti gli altri seguono il contratto
            _http.Put($"/driver/{driverId}/destination", destination);
        }
    }
}
```

**Conseguenze della violazione:**
1. **Codice speciale** per gestire l'eccezione
2. **Se arriva un altro** provider non conforme → altro `if`
3. **Entropia crescente** → il sistema diventa ingestibile
4. **Bug nascosti** → ogni nuovo caso speciale può introdurre errori

**Lezione:** LSP a livello architetturale significa che tutti i servizi/componenti devono rispettare lo stesso **contratto API**. Chi non lo rispetta crea entropia nel sistema.

## Collegamenti

- [[open-closed-principle]] - LSP abilita OCP (sostituibilità senza modifiche)
- [[dependency-inversion-principle]] - DIP usa LSP (le implementazioni rispettano il contratto)
- [[interface-segregation-principle]] - ISP previene violazioni LSP (interfacce troppo grandi)
- [[ports-and-adapters]] - Applicazione architettonica di LSP

## Insight Personale (Dan)

> "Mi ha colpito che ancora una volta i principi SOLID si estendono all'architettura. Questa roba mi è capitata davvero lavorando - si creavano 'eccezioni' all'LSP che poi crescevano."

Questo è il punto cruciale: le violazioni LSP raramente sono ovvie all'inizio. Sembrano "piccole eccezioni" ma crescono nel tempo, creando **entropia architettonica**.

## Quiz

### Q1: Rectangle/Square
Perché `Square extends Rectangle` viola LSP, anche se matematicamente un quadrato È un rettangolo?

<details>
<summary>Risposta</summary>

Perché il **comportamento** è diverso: in un `Rectangle` ci si aspetta che `Width` e `Height` siano indipendenti. `Square` rompe questa aspettativa facendo sì che settare `Width` modifichi anche `Height`.

LSP riguarda il **comportamento sostituibile**, non le relazioni matematiche. Nel codice, ciò che conta è: "Posso usare B ovunque uso A senza sorprese?" Se no → violazione.
</details>

### Q2: Taxi Dispatch
Nel sistema taxi, cosa succede se arriva un terzo provider con API diversa (`/pickup-location` invece di `/destination`)?

<details>
<summary>Risposta</summary>

Si aggiunge un altro `if` speciale, aumentando l'entropia del sistema. Ogni eccezione:
- Aggiunge complessità
- Aumenta il rischio di bug
- Rende il sistema più difficile da testare
- Viola OCP (devi modificare il dispatcher per ogni nuovo provider)

**Soluzione:** Rifiutare provider non conformi, o creare un **Adapter** che traduce la loro API nel contratto standard (ma l'adapter isola il problema, non lo elimina).
</details>

### Q3: Architettura
Come si applica LSP nel pattern Ports & Adapters?

<details>
<summary>Risposta</summary>

La **Port** (interfaccia) definisce il contratto. Ogni **Adapter** (implementazione) deve rispettare quel contratto perfettamente.

Esempio: `INotificationSender` (Port) con `EmailAdapter`, `SmsAdapter`, `PushAdapter`. Il sistema usa la Port senza sapere quale Adapter c'è dietro. Se un Adapter non rispetta il contratto (es. `SmsAdapter` che fallisce silenziosamente invece di lanciare eccezione), viola LSP e rompe le aspettative del sistema.
</details>

---

## Risorse per Approfondire

- **[Clean Architecture - Cap. 9](libro)** - Spiegazione originale Uncle Bob
- **[Liskov Substitution Principle - Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)** - Definizione formale
- **[SOLID Principles - Milan Jovanovic](https://www.milanjovanovic.tech/blog/liskov-substitution-principle)** - Esempi pratici .NET
- **[The Liskov Substitution Principle - Uncle Bob](https://web.archive.org/web/20151128004108/http://www.objectmentor.com/resources/articles/lsp.pdf)** - Paper originale Object Mentor
