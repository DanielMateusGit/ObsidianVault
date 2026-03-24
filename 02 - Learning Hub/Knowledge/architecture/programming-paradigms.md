---
tags:
  - architecture
  - from/book
  - from/week-01
  - status/learned
aliases:
  - paradigmi di programmazione
  - structured programming
  - paradigma strutturato
created: 2026-02-05
updated: 2026-02-05
source: "Clean Architecture (Robert C. Martin) - Capitoli 3-6"
---

# Programming Paradigms

> **One-liner:** I tre paradigmi (Structured, OOP, Functional) non aggiungono capacità al programmatore, ma *rimuovono* capacità - e proprio questo li rende potenti.

## La Tesi di Uncle Bob

Uncle Bob presenta un'osservazione chiave: ogni paradigma **toglie qualcosa** al programmatore:

| Paradigma | Cosa rimuove | Disciplina imposta |
|-----------|--------------|-------------------|
| **Structured** | `goto` | Controllo di flusso disciplinato |
| **OOP** | Puntatori a funzione diretti | Trasferimento indiretto del controllo |
| **Functional** | Assignment | Nessuna mutazione di stato |

> Questi tre paradigmi sono tutto ciò che abbiamo. Non ne sono stati inventati altri dal 1968 (Functional).

---

## Structured Programming

### La Storia: Dijkstra vs GOTO

**Edsger Dijkstra** (anni '60) aveva un obiettivo ambizioso: dimostrare **matematicamente** che un programma è corretto, come si fa con i teoremi.

Il problema? Il `goto` rendeva i programmi impossibili da analizzare formalmente.

```
// Con GOTO: flusso imprevedibile
10 IF X > 5 GOTO 40
20 X = X + 1
30 GOTO 10
40 PRINT X
50 GOTO 20    // Dove siamo? Cosa vale X?
```

### Bohm e Jacopini (1966)

Dimostrarono matematicamente che **qualsiasi programma** può essere scritto usando solo tre strutture:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. SEQUENZA          2. SELEZIONE         3. ITERAZIONE      │
│                                                                 │
│      ┌───┐                ┌───┐               ┌───┐            │
│      │ A │              ┌─┤ ? ├─┐             │ ? │◄───┐       │
│      └─┬─┘              │ └───┘ │             └─┬─┘    │       │
│        │               ▼       ▼               │      │       │
│      ┌───┐           ┌───┐   ┌───┐           ┌───┐    │       │
│      │ B │           │ A │   │ B │           │ A ├────┘       │
│      └─┬─┘           └─┬─┘   └─┬─┘           └───┘            │
│        │               └───┬───┘                               │
│        ▼                   ▼                                   │
│                                                                 │
│   Statement      if/then/else         while/for                │
│   dopo statement                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### L'Insight Rivoluzionario: Matematica vs Scienza

Dijkstra voleva **prove matematiche** di correttezza. Ma fallì.

**Il cambio di paradigma:** la programmazione è più simile alla **scienza empirica** che alla matematica:

| Matematica | Scienza |
|------------|---------|
| Dimostra che qualcosa è **vero** | Dimostra che qualcosa è **falso** |
| Prove costruttive | Prove falsificabili |
| "Questo teorema è corretto" | "Questa teoria non è stata ancora smentita" |

> **La scienza non prova verità, dimostra falsità.**
> Una teoria scientifica è "vera" finché non viene falsificata.

### La Connessione con TDD

Questo insight spiega perché **Test-Driven Development** funziona:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   NON possiamo DIMOSTRARE che il codice è corretto             │
│                          │                                      │
│                          ▼                                      │
│   MA possiamo TENTARE DI FALSIFICARLO con i test               │
│                          │                                      │
│                          ▼                                      │
│   Se i test non lo falsificano → è "abbastanza corretto"       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

I test sono **tentativi di falsificazione**:
- Ogni test che passa = un tentativo fallito di dimostrare che il codice è sbagliato
- Più test passano = più fiducia (ma mai certezza assoluta)
- Un test che fallisce = **falsificazione** → il codice è sbagliato

```csharp
// Ogni test è un tentativo di falsificare il codice
[Fact]
public void Sum_WithPositiveNumbers_ReturnsCorrectResult()
{
    // Tento di dimostrare che Sum è sbagliato
    var result = Calculator.Sum(2, 3);

    // Se questo fallisce → ho falsificato il codice
    Assert.Equal(5, result);
}

// Non ho DIMOSTRATO che Sum funziona sempre
// Ho solo FALLITO nel dimostrare che è sbagliato per questo caso
```

---

## Object-Oriented Programming

### Non una Rivoluzione, ma un'Evoluzione

Uncle Bob sfata il mito: OOP non ha "inventato" nulla di nuovo. Tutto esisteva già in C:

| Concetto | Esisteva in C? | Come? |
|----------|----------------|-------|
| Encapsulation | Sì | `struct` opache in header files |
| Inheritance | Sì | Casting di struct con layout comuni |
| Polymorphism | Sì | Puntatori a funzione |

### Encapsulation in C (prima di OOP)

```c
// point.h - Solo dichiarazione, implementazione nascosta
struct Point;  // Forward declaration - dettagli nascosti!
struct Point* makePoint(double x, double y);
double distance(struct Point* p1, struct Point* p2);

// point.c - Implementazione nascosta al client
struct Point {
    double x, y;  // Client non può accedere direttamente
};
```

> Ironia: C aveva encapsulation **migliore** di C++/Java dove i membri privati sono visibili nel header!

### Inheritance in C

```c
// "Eredità" tramite struct con layout comune
struct NamedPoint {
    double x, y;      // Stessi campi di Point, stesso offset
    char* name;
};

// Funziona perché il layout in memoria è identico
struct NamedPoint* np = makeNamedPoint(1.0, 2.0, "origin");
double d = distance((struct Point*)np, anotherPoint);  // Cast funziona!
```

### Polymorphism: L'Unica Vera Novità

Il polimorfismo in C era **possibile** ma **pericoloso**:

```c
// Polimorfismo manuale in C - STDIN, STDOUT sono "polimorfi"
// Ogni device implementa 5 funzioni standard
struct FILE {
    void (*open)(char* name, int mode);
    void (*close)();
    int (*read)();
    void (*write)(char c);
    void (*seek)(long index);
};

// Uso polimorfo - non so quale device, ma so che ha read()
char c = file->read();
```

**Il problema:** gestire manualmente le vtable era error-prone.

**OOP ha reso il polimorfismo *sicuro* e *conveniente***, non l'ha inventato.

---

## Functional Programming

### Il Paradigma più Antico (e più Moderno)

- **1936**: Alonzo Church inventa il lambda calculus
- **1958**: John McCarthy crea LISP (primo linguaggio funzionale)
- **Oggi**: Ritorno prepotente (React, Elixir, Rust, F#)

### Il Principio Fondamentale: Immutabilità

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   In un linguaggio funzionale puro:                            │
│                                                                 │
│   x = x + 1    ← IMPOSSIBILE! x non può essere riassegnato    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Perché l'Immutabilità è Potente?

Tutti i problemi di concorrenza derivano dalla **mutazione di stato condiviso**:

| Problema | Causa | Con immutabilità |
|----------|-------|------------------|
| Race condition | Due thread modificano stesso dato | Impossibile |
| Deadlock | Lock per proteggere stato | Nessun lock necessario |
| Stato inconsistente | Modifica parziale | Impossibile |

```csharp
// PROBLEMA: stato mutabile condiviso
class Counter {
    private int _count = 0;  // Stato mutabile!

    public void Increment() {
        _count++;  // Race condition se multi-thread
    }
}

// SOLUZIONE FUNZIONALE: stato immutabile
record Counter(int Count) {
    public Counter Increment() => new Counter(Count + 1);
    // Nuovo oggetto, originale intatto
}
```

---

## Timeline Storica

```
1936 ──── Lambda Calculus (Church) ───────────────────────► FUNCTIONAL
         │
1958 ──── LISP (McCarthy) ────────────────────────────────►
         │
1966 ──── Böhm-Jacopini ──────────────────────────────────► STRUCTURED
         │
1968 ──── "GOTO Considered Harmful" (Dijkstra) ───────────►
         │
1966 ──── Simula (Dahl & Nygaard) ────────────────────────► OOP
         │
1972 ──── Smalltalk (Kay) ────────────────────────────────►
         │
2020s ─── Hybrid: C#, Kotlin, Rust combinano tutti e tre ─► TODAY
```

---

## Quando Usare Ogni Paradigma

| Paradigma | Usa quando... | Esempio |
|-----------|---------------|---------|
| **Structured** | Sempre (è la base) | Qualsiasi codice |
| **OOP** | Modelli il dominio con entità e comportamenti | Domain model, API |
| **Functional** | Trasformazioni dati, concorrenza, predicibilità | Data pipeline, LINQ |

Nella pratica moderna, **usi tutti e tre insieme**:

```csharp
// OOP: Classe con identità
public class OrderProcessor
{
    // STRUCTURED: Flusso di controllo chiaro
    public Result Process(Order order)
    {
        if (!order.IsValid)
            return Result.Failure("Invalid order");

        // FUNCTIONAL: Trasformazione immutabile con LINQ
        var totals = order.Items
            .Where(i => i.IsActive)
            .Select(i => i.Price * i.Quantity)
            .Sum();

        return Result.Success(totals);
    }
}
```

---

## Collegamenti

- [[dependency-inversion-principle]] - Il contributo più importante di OOP all'architettura
- [[clean-architecture]] - Come i paradigmi influenzano l'architettura
- [[tdd]] - L'approccio scientifico applicato (da creare)
- [[single-responsibility-principle]] — SRP derivato da programmazione strutturata
- [[open-closed-principle]] — OCP derivato da polimorfismo OOP

---

## Quiz

### Q1: Secondo Dijkstra, la programmazione è più simile a:

- A) Matematica - possiamo dimostrare che un programma è corretto
- B) Scienza - possiamo solo tentare di falsificare, mai dimostrare correttezza
- C) Arte - non ci sono regole oggettive
- D) Ingegneria - seguiamo processi standardizzati

**Mia risposta:** _[Da completare]_

---

### Q2: Un collega dice "OOP ha inventato l'encapsulation". Come rispondi?

**Mia risposta:** _[Da completare]_

---

### Q3: Cosa hanno dimostrato Böhm e Jacopini nel 1966?

- A) Che il GOTO è più veloce delle strutture di controllo
- B) Che qualsiasi programma può essere scritto con sole 3 strutture (sequenza, selezione, iterazione)
- C) Che OOP è superiore alla programmazione strutturata
- D) Che i test sono sufficienti per dimostrare correttezza

**Mia risposta:** _[Da completare]_

---

## Ti è piaciuto parlare di Paradigmi? Allora impazzirai per:

- **[Go To Statement Considered Harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)** (Dijkstra, 1968) - La lettera originale che ha iniziato tutto. 2 pagine che hanno cambiato la storia.

- **[Out of the Tar Pit](http://curtclifton.net/papers/MoseschildrensFirth06a.pdf)** (Moseley & Marks, 2006) - Paper che analizza la complessità del software. Argomenta che lo stato mutabile è il nemico principale. Espande l'idea di Dijkstra sul perché functional programming sta tornando.

- **[Simple Made Easy](https://www.youtube.com/watch?v=SxdOUGdseq4)** (Rich Hickey, 2011) - Talk leggendario del creatore di Clojure. Spiega perché "semplice" e "facile" sono cose diverse, e perché i paradigmi che "tolgono" (functional) producono codice migliore.

---

*Creato durante Sedimentazione Week 1*
