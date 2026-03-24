---
tags:
  - design
  - complexity
  - from/book
  - status/learning
aliases:
  - Deep Modules
  - Shallow Modules
  - Information Hiding
  - A Philosophy of Software Design
created: 2026-02-25
source: "A Philosophy of Software Design - John Ousterhout (Cap. 1-5)"
---

# Deep Modules

> **One-liner:** Un buon modulo ha un'interfaccia semplice che nasconde un'implementazione complessa - massimo valore, minimo costo cognitivo.

## Cos'è

**Deep Module** è il concetto centrale del libro "A Philosophy of Software Design" di John Ousterhout. Rappresenta il modo ideale di progettare moduli software.

### La Metafora Visiva

```
DEEP MODULE (buono)              SHALLOW MODULE (cattivo)
┌──────────────────┐             ┌──────────────────────────────┐
│    Interfaccia   │ ← piccola   │         Interfaccia          │ ← grande
├──────────────────┤             ├──────────────────────────────┤
│                  │             │      Implementazione         │ ← piccola
│                  │             └──────────────────────────────┘
│ Implementazione  │ ← grande
│                  │             Il costo (interfaccia) è quasi
│                  │             uguale al beneficio (impl.)
└──────────────────┘
Tanto valore nascosto
dietro interfaccia semplice
```

### Esempio Classico: Unix File I/O

Solo 5 system call nascondono TUTTA la complessità del filesystem:
- `open()`, `read()`, `write()`, `lseek()`, `close()`

Dietro queste 5 funzioni ci sono: gestione disco, caching, permessi, locking, journaling, filesystem diversi...

**Questo è un deep module perfetto.**

## La Complessità: Il Nemico

### Definizione
La complessità è tutto ciò che rende il software **difficile da capire o modificare**.

### I 3 Sintomi della Complessità

| Sintomo | Descrizione | Come si Manifesta |
|---------|-------------|-------------------|
| **Change Amplification** | Piccola modifica → modifiche in tanti posti | "Devo cambiare 15 file per aggiungere un campo" |
| **Cognitive Load** | Devi sapere troppe cose per fare una modifica | "Devo capire 5 classi prima di toccare questa" |
| **Unknown Unknowns** | Non sai cosa non sai (il peggiore!) | "Ho modificato X e si è rotto Y" |

### Le 2 Cause della Complessità

1. **Dependencies** - Il codice non può essere capito/modificato in isolamento
2. **Obscurity** - Informazioni importanti non sono ovvie

## Strategic vs Tactical Programming

| Tactical | Strategic |
|----------|-----------|
| "Fammi finire sta feature" | "Come facilito le modifiche future?" |
| Quick fixes, hack | Investi nel design |
| Veloce oggi, lento domani | 10-20% tempo extra oggi |
| Debito tecnico si accumula | Veloce nel medio termine |

> *"Working code isn't enough"* - deve essere anche facile da evolvere.

## Information Hiding

La tecnica più importante per creare deep modules.

### Principio
Ogni modulo dovrebbe **nascondere**:
- Decisioni di design
- Strutture dati interne
- Meccanismi di implementazione

### Information Leakage (il nemico)

| Tipo di Leakage | Esempio | Problema |
|-----------------|---------|----------|
| **Temporal decomposition** | `readHeader()`, `readBody()`, `readFooter()` | Chi chiama deve conoscere il formato |
| **Leaky interface** | `send(headers, body, timeout, retries, ...)` | Troppi dettagli esposti |
| **Shared knowledge** | Due classi che "sanno" lo stesso formato | Cambi formato → modifichi entrambe |

### Come Riconoscerlo
- Modifichi un dettaglio interno → devi modificare chi chiama? **Leakage!**
- Chi chiama deve "sapere" come funziona internamente? **Leakage!**

## Quando Usarlo

- **SEMPRE** quando progetti un'API, un servizio, una classe
- Quando crei **interfacce** (nel senso di contratti)
- Quando decidi cosa esporre e cosa nascondere
- Quando fai **refactoring** per ridurre complessità

### Domande da Farti

1. "L'interfaccia è più semplice dell'implementazione?"
2. "Chi usa questo modulo deve sapere COME funziona internamente?"
3. "Se cambio un dettaglio interno, devo cambiare anche chi chiama?"

## Quando NON Usarlo

- **Over-engineering**: Non creare deep modules per operazioni banali
- **Premature abstraction**: Se non sai ancora cosa nascondere, aspetta
- **Quando la semplicità basta**: Una funzione utility di 3 righe non ha bisogno di essere "deep"

## Esempio Pratico

### Shallow (cattivo)
```csharp
// Interfaccia grande quanto implementazione
public class UserValidator
{
    public bool IsValidEmail(string email) => email.Contains("@");
    public bool IsValidName(string name) => !string.IsNullOrEmpty(name);
    public bool IsValidAge(int age) => age > 0 && age < 150;
}

// Chi chiama deve sapere TUTTI i metodi e chiamarli tutti
if (validator.IsValidEmail(email) &&
    validator.IsValidName(name) &&
    validator.IsValidAge(age)) { ... }
```

### Deep (buono)
```csharp
// Interfaccia semplice, complessità nascosta
public class UserValidator
{
    public ValidationResult Validate(UserDto user)
    {
        // Tutta la logica nascosta qui dentro
        // Email, nome, età, regole business, etc.
    }
}

// Chi chiama: semplice!
var result = validator.Validate(user);
if (result.IsValid) { ... }
```

## Collegamenti

- [[clean-architecture-principles]] - Clean Architecture usa deep modules nei layer
- [[single-responsibility-principle]] - SRP aiuta a definire cosa nascondere
- [[dependency-inversion-principle]] - Le interfacce DIP devono essere "deep"
- [[repository-pattern]] - Un buon repository è un deep module
- [[facade-pattern]] — Facade è l'esempio perfetto di deep module
- [[interface-segregation-principle]] — ISP e deep modules: esponi solo ciò che serve

## Quiz

### Q1: Deep vs Shallow
Un collega crea una classe `FileProcessor` con questi metodi pubblici:
- `OpenFile(path)`
- `ReadHeader()`
- `ReadBody()`
- `ReadFooter()`
- `CloseFile()`

È un deep module o shallow? Perché?

<details>
<summary>Risposta</summary>

**Shallow module** con **temporal decomposition**.

Chi chiama deve:
1. Conoscere l'ordine delle chiamate
2. Sapere che il file ha header/body/footer
3. Gestire apertura/chiusura

**Soluzione deep:**
```csharp
public FileContent Process(string path);
```
Una chiamata, tutto nascosto.
</details>

### Q2: Information Leakage
```csharp
public interface INotificationSender
{
    Task SendAsync(string recipient, string message,
        SmtpSettings smtpSettings, int retryCount, TimeSpan timeout);
}
```

Qual è il problema? Come lo risolvi?

<details>
<summary>Risposta</summary>

**Information leakage**: L'interfaccia espone dettagli implementativi (SMTP settings, retry, timeout).

Chi chiama deve sapere che usiamo SMTP e gestire configurazioni tecniche.

**Soluzione:**
```csharp
public interface INotificationSender
{
    Task SendAsync(string recipient, string message);
}
```

SMTP settings, retry, timeout sono dettagli interni - vanno nella configurazione del servizio, non nell'interfaccia.
</details>

### Q3: Identificare la Complessità
Un developer dice: "Ho modificato il formato della data nel DTO e ho dovuto cambiare 12 file."

Quale sintomo di complessità è? Qual è probabilmente la causa?

<details>
<summary>Risposta</summary>

**Sintomo:** Change Amplification

**Causa probabile:**
- **Dependencies** eccessive - troppi componenti dipendono dal formato specifico
- **Information leakage** - il formato della data non è incapsulato in un unico punto

**Soluzione:** Creare un Value Object `FormattedDate` o un servizio `DateFormatter` che nasconde il formato.
</details>

### Q4: Strategic vs Tactical
Un PM ti chiede una feature per domani. Sai che il modo "veloce" creerà debito tecnico. Cosa fai?

<details>
<summary>Risposta</summary>

**Approccio Strategic:**
1. Comunica il trade-off al PM
2. Proponi: "Posso farlo in modo pulito in 2 giorni, o hackerarlo per domani ma poi serviranno 3 giorni per sistemarlo"
3. Se deve essere domani, **documenta** il debito tecnico e **pianifica** il refactoring

**Mai** fare tactical senza consapevolezza. Il debito tecnico nascosto è il killer dei progetti.
</details>

---

## Risorse per Approfondire

- **[A Philosophy of Software Design - John Ousterhout](https://www.amazon.com/Philosophy-Software-Design-John-Ousterhout/dp/1732102201)** - Il libro completo (altamente consigliato)
- **[John Ousterhout Talk @ Google](https://www.youtube.com/watch?v=bmSAYlu0NcY)** - L'autore presenta i concetti chiave (1h)
- **[Summary & Notes by Kislay Verma](https://kislayverma.com/programming/a-philosophy-of-software-design-notes/)** - Riassunto capitolo per capitolo

---

*Capitoli coperti: 1-5*
*Prossimi: Cap. 6+ (Different Layer, Different Abstraction; Pull Complexity Downwards; etc.)*
