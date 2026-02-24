---
tags:
  - architecture
  - components
  - from/book
  - from/clean-architecture
  - status/learned
aliases:
  - REP
  - CCP
  - CRP
  - Component Cohesion
created: 2026-02-20
source: "Clean Architecture - Cap. 13"
---

# Component Cohesion (REP, CCP, CRP)

> **One-liner:** Tre principi in tensione che guidano quali classi mettere insieme nello stesso componente.

## La Domanda Centrale

> "Quali classi metto INSIEME nello stesso componente (DLL)?"

## I Tre Principi

### 1. REP - Reuse/Release Equivalence Principle

> **"Le classi in un componente devono essere rilasciabili insieme."**

Se pubblichi un package, tutte le classi al suo interno devono avere **senso insieme**. Un utente che vuole solo una parte non dovrebbe essere forzato ad aggiornare tutto.

```
❌ MyCompany.Utilities (tutto dentro)
   └─> StringHelper, DateHelper, PdfGenerator, EmailSender

✅ Componenti separati con senso
   └─> MyCompany.Core (String + Date helpers)
   └─> MyCompany.Pdf
   └─> MyCompany.Email
```

**Test:** Se non puoi scrivere un README coerente per il componente, ha troppe responsabilità.

### 2. CCP - Common Closure Principle

> **"Classi che CAMBIANO insieme dovrebbero stare nello stesso componente."**

È **SRP applicato ai componenti**. Un cambiamento dovrebbe impattare UN solo componente.

```
Requisito: "Cambia il formato delle date"

❌ Male: 3 componenti da modificare
   MyApp.Api/DateFormatter.cs
   MyApp.Services/DateHelper.cs
   MyApp.Reports/ReportDateFormatter.cs

✅ Bene: 1 componente da modificare
   MyApp.Core/DateHelpers/* (tutto qui)
```

### 3. CRP - Common Reuse Principle

> **"Classi che si USANO insieme dovrebbero stare nello stesso componente."**

È **ISP applicato ai componenti**. Non forzare dipendenze su cose che non servono.

```
❌ MyApp.Data (tutto insieme)
   └─> IRepository, SqlRepository, MongoRepository, RedisCache, ElasticClient
   └─> Chi vuole solo Sql è forzato a dipendere da tutto!

✅ Separati per uso
   └─> MyApp.Data.Abstractions (IRepository)
   └─> MyApp.Data.Sql
   └─> MyApp.Data.Mongo
   └─> MyApp.Caching.Redis
   └─> MyApp.Search.Elastic
```

## Il Triangolo della Tensione

I tre principi sono in **tensione** tra loro:

```
                        REP
                    (Rilasciabili
                      insieme)
                         △
                        /  \
                       /    \
                      /      \
                     /   😰   \
                    /  Tension \
                   /            \
                  ▽──────────────▽
               CCP                CRP
         (Cambiano             (Usati
          insieme)              insieme)
```

| Troppo focus su... | Rischio |
|-------------------|---------|
| REP + CCP | Componenti troppo grandi |
| CCP + CRP | Troppi micro-componenti |
| REP + CRP | Cambiamenti a cascata |

### Strategia Pragmatica

| Fase Progetto | Focus |
|---------------|-------|
| **Inizio** | CCP (pochi componenti, cambiano insieme) |
| **Maturità** | CRP (più granularità per i consumatori) |

## Esempio: MyApp.Utilities

**Problema:** `StringHelper`, `DateHelper`, `PdfGenerator`, `EmailSender` tutti insieme.

**Violazioni:**
- **REP:** Non rilasciabili insieme (cosa c'entra Email con PDF?)
- **CCP:** Non cambiano insieme (cambiare Email non impatta PDF)
- **CRP:** Non usati insieme (posso voler solo PDF senza Email)

**Soluzione:**
```
MyApp.Core/           ← StringHelper + DateHelper (usati insieme!)
MyApp.Pdf/            ← PdfGenerator (dipende da Core)
MyApp.Email/          ← EmailSender (dipende da Core)
```

StringHelper e DateHelper possono stare insieme perché:
- DateHelper usa StringHelper per formattare
- Cambiano insieme (formato stringa → impatta date)
- Servono lo stesso "attore" (utilities di base)

## Collegamenti

- [[components]] - Cos'è un componente
- [[component-coupling]] - Come gestire dipendenze tra componenti
- [[single-responsibility-principle]] - CCP è SRP per componenti
- [[interface-segregation-principle]] - CRP è ISP per componenti

## Quiz

### Q1: REP, CCP, o CRP?
Hai un componente con `OrderValidator`, `OrderRepository`, `OrderPdfExporter`. Quale principio probabilmente viola?

<details>
<summary>Risposta</summary>

**CRP** - Non sono usati insieme. Chi vuole solo validare non dovrebbe dipendere dal PDF exporter. Meglio separare in `MyApp.Orders.Core` (Validator + Repository) e `MyApp.Orders.Export` (PDF).
</details>

### Q2: Tensione
All'inizio di un nuovo progetto, quale principio dovresti favorire e perché?

<details>
<summary>Risposta</summary>

**CCP** - All'inizio le cose cambiano spesso. Avere meno componenti che cambiano insieme riduce il costo dei cambiamenti. Man mano che il progetto matura e altri team lo usano, sposti il focus verso CRP per dare granularità ai consumatori.
</details>
