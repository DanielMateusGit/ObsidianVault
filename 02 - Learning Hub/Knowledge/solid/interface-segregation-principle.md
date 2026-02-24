---
tags:
  - solid
  - isp
  - architecture
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - ISP
  - Interface Segregation
  - Segregazione Interfacce
created: 2026-02-20
source: "Clean Architecture - Cap. 10 + Sessione con Claude"
---

# Interface Segregation Principle (ISP)

> **One-liner:** Nessun client dovrebbe essere forzato a dipendere da metodi che non usa - preferisci interfacce piccole e focalizzate.

## Cos'è

ISP afferma che è meglio avere **molte interfacce piccole e specifiche** piuttosto che **poche interfacce grandi e generiche**.

> *"Clients should not be forced to depend on methods they do not use."*
> — Robert C. Martin

### Il Segnale d'Allarme

Se vedi `NotImplementedException` o `NotSupportedException` in un'implementazione di interfaccia → **stai violando ISP**.

```csharp
// ❌ Questo è un SMELL che indica violazione ISP
public void Scan() => throw new NotImplementedException();
```

## Il Problema: "Fat Interface"

```csharp
// ❌ VIOLA ISP - Interfaccia "grassa"
public interface IMultiFunctionPrinter
{
    void Print();
    void Scan();
    void Fax();
    void Staple();
}

// Una stampante semplice è FORZATA a implementare metodi inutili
public class SimplePrinter : IMultiFunctionPrinter
{
    public void Print() => /* ok */;
    public void Scan() => throw new NotSupportedException();  // 💀
    public void Fax() => throw new NotSupportedException();   // 💀
    public void Staple() => throw new NotSupportedException(); // 💀
}
```

## La Soluzione: Interfacce Segregate

```csharp
// ✅ RISPETTA ISP - Interfacce piccole e focalizzate
public interface IPrinter { void Print(); }
public interface IScanner { void Scan(); }
public interface IFax { void Fax(); }
public interface IStapler { void Staple(); }

// Stampante semplice - implementa SOLO ciò che sa fare
public class SimplePrinter : IPrinter
{
    public void Print() => /* ok */;
}

// Stampante multifunzione - compone le interfacce che servono
public class MultiFunctionPrinter : IPrinter, IScanner, IFax
{
    public void Print() => /* ok */;
    public void Scan() => /* ok */;
    public void Fax() => /* ok */;
}
```

## ISP a Livello Architetturale

ISP non riguarda solo le interfacce C#, ma anche le **dipendenze tra moduli**.

### Problema: Dipendenze Non Necessarie

```
                    ┌─────────────────────────────────┐
                    │              OPS                │
                    │  ┌─────┐ ┌─────┐ ┌─────┐       │
                    │  │ op1 │ │ op2 │ │ op3 │       │
                    │  └─────┘ └─────┘ └─────┘       │
                    └─────────────────────────────────┘
                         ▲         ▲         ▲
                         │         │         │
                      User1     User2     User3
                     (usa op1) (usa op2) (usa op3)
```

**Problema:** Se cambio `op2`, devo ricompilare/redeployare OPS. Ma anche User1 e User3 sono impattati, anche se non usano `op2`!

### Soluzione: Segregazione

```
                    ┌─────────────────────────────────┐
                    │              OPS                │
                    │  (implementa tutte le ops)      │
                    └─────────────────────────────────┘
                         ▲         ▲         ▲
                         │         │         │
                    ┌────┴────┐ ┌──┴──┐ ┌────┴────┐
                    │  I_Op1  │ │I_Op2│ │  I_Op3  │
                    └────┬────┘ └──┬──┘ └────┬────┘
                         │         │         │
                      User1     User2     User3
```

**Risultato:**
- User1 dipende SOLO da `I_Op1`
- Se cambio `op2` → solo User2 è impattato
- Meno ricompilazioni, meno redeploy, meno rischi!

## Quando Usarlo

| Situazione | Applica ISP? |
|------------|--------------|
| Interfaccia con metodi che alcuni implementatori non usano | ✅ Sì |
| Classi che lanciano `NotImplementedException` | ✅ Sì, urgente! |
| Modulo A dipende da modulo B ma usa solo il 20% | ✅ Sì |
| Interfaccia piccola e coesa (3-5 metodi correlati) | ❌ No, va bene così |

## Quando NON Esagerare

```csharp
// ❌ TROPPO segregato - overkill!
public interface ICanAdd { void Add(); }
public interface ICanRemove { void Remove(); }
public interface ICanUpdate { void Update(); }
public interface ICanGet { Item Get(); }

// ✅ Giusto equilibrio - metodi COESI che vanno insieme
public interface IRepository<T>
{
    void Add(T item);
    void Remove(T item);
    void Update(T item);
    T GetById(int id);
}
```

**Regola:** Segrega quando i metodi servono **clienti diversi**. Non segregare metodi che **vanno sempre insieme**.

## Esempio Pratico: IUserService

```csharp
// ❌ VIOLA ISP - Mescola responsabilità diverse
public interface IUserService
{
    void CreateUser();
    void DeleteUser();
    void SendWelcomeEmail();      // Client diverso!
    void GenerateMonthlyReport(); // Client diverso!
}

// ✅ RISPETTA ISP - Segregato per client
public interface IUserService
{
    void CreateUser();
    void DeleteUser();
}

public interface IEmailService
{
    void SendWelcomeEmail();
}

public interface IReportGenerator
{
    void GenerateMonthlyReport();
}
```

## ISP vs SRP: La Differenza Chiave

> **Domanda comune:** "Se una classe implementa molte interfacce piccole, non viola SRP?"

**Risposta: NO!** Guardano cose diverse:

| Principio | Cosa Guarda | Domanda Chiave |
|-----------|-------------|----------------|
| **SRP** | Chi CHIEDE modifiche alla classe | "Quanti ATTORI servo?" |
| **ISP** | Chi USA l'interfaccia | "Forzo dipendenze inutili?" |

### Esempio: Rispetta Entrambi

```csharp
// ✅ Implementa 3 interfacce MA rispetta SRP
public class SqlOrderRepository : IOrderReader, IOrderWriter, IOrderDeleter
{
    public Order GetById(int id) { /* ... */ }  // IOrderReader
    public void Save(Order order) { /* ... */ } // IOrderWriter
    public void Delete(int id) { /* ... */ }    // IOrderDeleter
}
```

**Perché rispetta SRP?**
- Tutte le interfacce servono lo **stesso attore**: Application Layer (data access)
- La classe è **coesa**: tutto riguarda "persistenza ordini"

### Esempio: Viola SRP

```csharp
// ❌ Implementa 3 interfacce E viola SRP
public class UserManager : IUserAuth, IUserReporting, IUserEmailing
{
    public bool Login() { /* ... */ }        // → Security Team
    public Report Generate() { /* ... */ }   // → Analytics Team
    public void SendEmail() { /* ... */ }    // → Marketing Team
}
```

**Perché viola SRP?**
- **3 attori diversi** chiedono modifiche
- Cambiamento per Marketing può rompere Security

### La Regola

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ISP: Interfacce piccole → per i CLIENT (chi le usa)          │
│   SRP: Classi coese → per gli ATTORI (chi chiede modifiche)    │
│                                                                 │
│   Una classe può implementare MOLTE interfacce piccole         │
│   E rispettare comunque SRP                                    │
│   SE tutte quelle interfacce servono LO STESSO ATTORE          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Collegamenti

- [[single-responsibility-principle]] - SRP guarda gli attori, ISP guarda i client
- [[liskov-substitution-principle]] - Violazioni ISP spesso causano violazioni LSP
- [[dependency-inversion-principle]] - ISP + DIP = dipendenze pulite
- [[open-closed-principle]] - Interfacce piccole facilitano estensioni

## Quiz

### Q1: Fat Interface
Hai un'interfaccia `IWorker` con metodi `Work()`, `Eat()`, `Sleep()`. Devi implementarla per un `Robot`. Cosa c'è di sbagliato e come lo risolvi?

<details>
<summary>Risposta</summary>

**Problema:** Robot è forzato a implementare `Eat()` e `Sleep()` che non hanno senso, probabilmente con `NotImplementedException`.

**Soluzione:** Segregare in interfacce più piccole:
- `IWorkable` con `Work()`
- `IFeedable` con `Eat()` (solo per esseri che mangiano)
- `ISleepable` con `Sleep()` (solo per esseri che dormono)

Robot implementa solo `IWorkable`.
</details>

### Q2: ISP Architetturale
Perché ISP a livello architetturale riduce i tempi di ricompilazione e redeploy?

<details>
<summary>Risposta</summary>

Se un modulo dipende solo da un'interfaccia piccola (invece che da un modulo "fat"), quando cambia una parte che NON usa, non deve essere ricompilato.

Esempio: User1 usa solo `I_Op1`. Se cambia `op2` nel modulo OPS, User1 non viene ricompilato perché non dipende da `I_Op2`.

Meno dipendenze = meno cascate di ricompilazione.
</details>

### Q3: ISP vs SRP
Una classe `PaymentGateway` implementa `IPaymentProcessor`, `IRefundProcessor`, `IPaymentValidator`. Viola SRP?

<details>
<summary>Risposta</summary>

**Probabilmente NO**, se tutte e tre le interfacce servono lo stesso attore (il team che gestisce i pagamenti).

Le interfacce sono segregate per i CLIENT (qualcuno potrebbe voler solo validare, altri solo processare), ma la classe è coesa e serve UN attore.

**Violerebbe SRP** se `IPaymentValidator` servisse il team Compliance, `IRefundProcessor` il team Customer Service, etc. In quel caso, tre attori diversi = tre classi diverse.
</details>

---

## Risorse per Approfondire

- **[Clean Architecture - Cap. 10](libro)** - Spiegazione originale Uncle Bob
- **[Interface Segregation Principle - Milan Jovanovic](https://www.milanjovanovic.tech/blog/interface-segregation-principle)** - Esempi .NET pratici
- **[SOLID Principles - Mark Seemann](https://blog.ploeh.dk/2011/02/28/Interfacesareaccessmodifiers/)** - Prospettiva avanzata su interfacce
