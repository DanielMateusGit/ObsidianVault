---
tags:
  - architecture
  - components
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - ADP
  - SDP
  - SAP
  - Component Coupling
  - Acyclic Dependencies
created: 2026-02-20
source: "Clean Architecture - Cap. 14"
---

# Component Coupling (ADP, SDP, SAP)

> **One-liner:** Tre principi per gestire le dipendenze tra componenti: niente cicli, dipendi verso la stabilità, stabile = astratto.

## La Domanda Centrale

> "Come gestisco le DIPENDENZE tra componenti?"

## I Tre Principi

### 1. ADP - Acyclic Dependencies Principle

> **"Non ci devono essere CICLI nel grafo delle dipendenze."**

#### Il Problema

```
     A ──────► B
     ▲         │
     │         │
     │         ▼
     └──────── C

A → B → C → A = CICLO! 💀
```

**Conseguenze:**
- Per compilare A serve B e C
- Per compilare B serve C e A
- Per compilare C serve A e B
- **Risultato:** Devo compilare TUTTO insieme → addio deploy indipendente!

#### Soluzioni

**Opzione 1: DIP - Inverti con interfaccia**
```
     A ──────► B
     ▲         │
     │         │
  «IA»         ▼
     ▲──────── C

C dipende da IA (interfaccia), A implementa IA
Il ciclo è rotto!
```

**Opzione 2: Estrai componente comune**
```
     A ──────► B
     │         │
     ▼         ▼
     D ◄─────── C

Le parti condivise vanno in D
```

### 2. SDP - Stable Dependencies Principle

> **"Dipendi nella direzione della STABILITÀ."**

#### Cos'è la Stabilità?

| Componente | Stabile se... | Instabile se... |
|------------|---------------|-----------------|
| **Definizione** | Molti dipendono da lui, lui da pochi | Pochi dipendono da lui, lui da molti |
| **Cambiare** | Difficile (romperebbe molti) | Facile (nessuno si rompe) |
| **Esempio** | Domain layer | Controllers API |

```
       STABILE                    INSTABILE

   ┌─────────────┐            ┌─────────────┐
   │   Domain    │            │     Api     │
   └─────────────┘            └─────────────┘
     ▲   ▲   ▲                      │
     │   │   │                      ▼
    App Infra Tests              Application
                                    │
   Tutti dipendono da Domain        ▼
   → Domain è STABILE              Domain

                               Api dipende da molti
                               → Api è INSTABILE
```

#### La Regola

```
INSTABILE ────────────────────► STABILE
(cambia spesso)                 (cambia raramente)

✅ Api → Application → Domain
❌ Domain → Infrastructure (MAI!)
```

#### Errore Comune

Se `Domain` (stabile) dipende da `Infrastructure` (instabile):
- Domain dovrebbe essere indipendente
- Ma ogni cambio in Infrastructure forza cambio in Domain
- La "stabilità" di Domain è falsa!

**Fix:** Invertire! Infrastructure dipende da Domain.

### 3. SAP - Stable Abstractions Principle

> **"I componenti STABILI dovrebbero essere ASTRATTI."**

#### Il Ragionamento

- Componente **stabile** = difficile da cambiare
- Se è stabile MA concreto = sei bloccato!
- Se è stabile E astratto = puoi estendere senza modificare (OCP!)

#### La Regola

| Stabilità | Astrattezza | Risultato |
|-----------|-------------|-----------|
| Alta | Alta | ✅ Ideale (Domain, interfacce) |
| Alta | Bassa | ❌ Zona di dolore (rigido) |
| Bassa | Alta | ❌ Inutile (astrazioni non usate) |
| Bassa | Bassa | ✅ OK (implementazioni concrete) |

#### In Clean Architecture

| Layer | Stabilità | Astrattezza | Perché |
|-------|-----------|-------------|--------|
| **Domain** | Molto alta | Molto alta | Entities + Interfaces |
| **Application** | Alta | Media | Use Cases + Port interfaces |
| **Infrastructure** | Bassa | Bassa | Implementazioni concrete |
| **Api** | Molto bassa | Bassa | Controllers concreti |

## Tool .NET per Rispettare Questi Principi

### 1. NetArchTest (Gratuito)

Test di architettura come unit test. Perfetto per CI/CD.

```csharp
// Verifica che Domain non dipenda da Infrastructure
[Fact]
public void Domain_Should_Not_Depend_On_Infrastructure()
{
    var result = Types.InAssembly(typeof(Order).Assembly)
        .Should()
        .NotHaveDependencyOn("MyApp.Infrastructure")
        .GetResult();

    Assert.True(result.IsSuccessful);
}

// Verifica che Infrastructure dipenda da Application
[Fact]
public void Infrastructure_Should_Depend_On_Application()
{
    var result = Types.InAssembly(typeof(SqlOrderRepository).Assembly)
        .Should()
        .HaveDependencyOn("MyApp.Application")
        .GetResult();

    Assert.True(result.IsSuccessful);
}
```

**NuGet:** `NetArchTest.Rules`

### 2. ArchUnitNET (Gratuito)

Simile a NetArchTest, sintassi più fluente.

```csharp
[Fact]
public void No_Cycles_Between_Layers()
{
    IArchRule rule = Types()
        .That().ResideInNamespace("Domain")
        .Should().NotDependOnAny(
            Types().That().ResideInNamespace("Infrastructure")
        );

    rule.Check(Architecture);
}
```

**NuGet:** `ArchUnitNET`

### 3. NDepend (Commerciale, Potente)

Analisi completa: cicli, stabilità, astrattezza, metriche.

```
Features:
✅ Dependency Graph visuale
✅ Rileva cicli automaticamente
✅ Calcola metriche stabilità/astrattezza
✅ Integrazione CI/CD
✅ Trend nel tempo
```

**Costo:** ~€400/dev/anno, ma trial gratuito.

### 4. Visual Studio Enterprise

Dependency diagrams e layer validation inclusi.

```
Features:
✅ Layer Diagrams
✅ Dependency Validation
✅ Code Maps
```

### 5. JetBrains Rider / ReSharper

Dependency diagrams, trova cicli.

```
Features:
✅ Type Dependency Diagram
✅ Project Dependency Diagram
✅ Find usages avanzato
```

### Raccomandazione

| Budget | Tool |
|--------|------|
| **Gratis** | NetArchTest in CI + Rider |
| **Enterprise** | NDepend (il più completo) |

## Collegamenti

- [[components]] - Cos'è un componente
- [[component-cohesion]] - Cosa mettere in un componente
- [[dependency-inversion-principle]] - DIP rompe i cicli
- [[open-closed-principle]] - SAP abilita OCP

## Quiz

### Q1: Rompi il ciclo
Hai: A → B → C → A. Come lo risolvi con DIP?

<details>
<summary>Risposta</summary>

Fai implementare ad A un'interfaccia `IA`. C dipende da `IA` invece che da A direttamente. Il ciclo è rotto: A → B → C → IA ← A.
</details>

### Q2: Errore architetturale
Il tuo Domain layer dipende da Infrastructure. Perché è sbagliato secondo SDP?

<details>
<summary>Risposta</summary>

Domain dovrebbe essere STABILE (molti dipendono da lui, lui da nessuno). Se dipende da Infrastructure (instabile), ogni cambio in Infrastructure forza cambi in Domain. La stabilità di Domain diventa falsa. **Fix:** Inverti! Infrastructure deve dipendere da Domain.
</details>

### Q3: SAP
Un componente è molto stabile ma contiene solo classi concrete. Perché è un problema?

<details>
<summary>Risposta</summary>

Se è stabile = difficile da cambiare (molti dipendono da lui). Se è concreto = non estendibile. Risultato: sei BLOCCATO. Non puoi aggiungere funzionalità senza modificare il componente, rompendo tutti i dipendenti. **Fix:** Rendi il componente astratto (interfacce), così gli altri possono estendere senza modificare.
</details>
