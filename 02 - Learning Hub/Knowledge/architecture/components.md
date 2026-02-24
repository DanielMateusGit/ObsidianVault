---
tags:
  - architecture
  - components
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - Component
  - Componenti
  - DLL
  - JAR
created: 2026-02-20
source: "Clean Architecture - Cap. 12"
---

# Components

> **One-liner:** Un componente è la più piccola unità deployabile/compilabile di un sistema - il "granello di sabbia" del software.

## Cos'è un Componente

Un componente è l'unità minima che può essere:
- **Compilata** indipendentemente
- **Deployata** indipendentemente
- **Linkata** ad altre unità

| Linguaggio/Piattaforma | Componente |
|------------------------|------------|
| **.NET** | DLL (Dynamic Link Library) |
| **Java** | JAR (Java Archive) |
| **Ruby** | Gem |
| **Node.js** | npm package |
| **Go** | Module |

## Componenti Ben Progettati

Un componente è **ben progettato** quando:
- È **compilabile indipendentemente** (non richiede altri componenti per compilare)
- È **deployabile indipendentemente** (può essere aggiornato senza ricompilare tutto)
- Ha **responsabilità coese** (non fa troppe cose)

## Evoluzione Storica (Breve)

```
┌─────────────────────────────────────────────────────────────────┐
│                    EVOLUZIONE DEI COMPONENTI                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. ERA PDP-8 (anni '60)                                       │
│     └─> Memoria allocata manualmente all'inizio del file       │
│     └─> Programmatore gestiva indirizzi a mano                 │
│                                                                 │
│  2. FUNCTION LIBRARIES                                          │
│     └─> Separazione tra applicazione e librerie condivise      │
│     └─> Ma ancora linking statico                              │
│                                                                 │
│  3. LOADER + LINKER                                             │
│     └─> Loading: carica in memoria                             │
│     └─> Linking: risolve riferimenti tra componenti            │
│     └─> Due fasi separate di compilazione                      │
│                                                                 │
│  4. LEGGE DI MOORE                                              │
│     └─> Hardware sempre più veloce                             │
│     └─> Permette metodi "lenti" ma flessibili                  │
│     └─> Dynamic linking diventa pratico                        │
│                                                                 │
│  5. COMPONENT PLUGIN ARCHITECTURE                               │
│     └─> Componenti come plugin intercambiabili                 │
│     └─> Deploy indipendente                                    │
│     └─> Hot-swapping possibile                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Component Plugin Architecture

L'evoluzione naturale: i componenti diventano **plugin** che possono essere:
- Aggiunti senza ricompilare il core
- Rimossi senza impatto
- Sostituiti a runtime (in alcuni sistemi)

```
┌─────────────────────────────────────────────────────────────────┐
│                         CORE SYSTEM                             │
│                    (definisce interfacce)                       │
└───────────────────────────┬─────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
      ┌──────────┐    ┌──────────┐    ┌──────────┐
      │ Plugin A │    │ Plugin B │    │ Plugin C │
      │  (.dll)  │    │  (.dll)  │    │  (.dll)  │
      └──────────┘    └──────────┘    └──────────┘

      Ogni plugin è un COMPONENTE indipendente
```

## Collegamento con Clean Architecture

In Clean Architecture, i **layer** sono spesso organizzati come componenti separati:

```
Solution/
├── MyApp.Domain/           ← Componente (DLL)
├── MyApp.Application/      ← Componente (DLL)
├── MyApp.Infrastructure/   ← Componente (DLL)
└── MyApp.Api/              ← Componente (DLL)
```

Le dipendenze tra componenti seguono la **Dependency Rule**.

## Collegamenti

- [[dependency-inversion-principle]] - DIP permette componenti indipendenti
- [[open-closed-principle]] - OCP abilita plugin architecture
- [[component-cohesion]] - Come decidere cosa va in un componente (Cap. 13)
- [[component-coupling]] - Come gestire dipendenze tra componenti (Cap. 14)

## Quiz

### Q1: Cos'è un componente?
<details>
<summary>Risposta</summary>

La più piccola unità deployabile/compilabile di un sistema. In .NET sono le DLL, in Java i JAR. Sono "ben progettati" quando sono compilabili e deployabili indipendentemente.
</details>

### Q2: Perché la Legge di Moore ha influenzato l'architettura dei componenti?
<details>
<summary>Risposta</summary>

Hardware più veloce ha permesso di adottare tecniche "lente" ma flessibili come il dynamic linking. Prima, il linking dinamico era troppo costoso in termini di performance. Moore's Law ha reso pratico il trade-off tra flessibilità e velocità.
</details>
