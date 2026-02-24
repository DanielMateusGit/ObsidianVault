---
tags: [context, quiz, spaced-repetition]
created: 2026-02-05
updated: 2026-02-05
---

# 🧠 Quiz Tracker - Spaced Repetition

> Claude usa questo file per tracciare tutti i quiz e gestire la spaced repetition.

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| **Quiz totali** | 90 |
| **Risposte corrette** | 39 |
| **Risposte parziali** | 3 |
| **Risposte sbagliate** | 1 |
| **Non risposti** | 23 |
| **Challenge completate** | 8 |
| **Streak challenge** | 2 |

---

## 🎯 Sistema Spaced Repetition

### Intervalli (Leitner System semplificato)
| Box | Intervallo | Significato |
|-----|------------|-------------|
| 📦 Box 1 | Ogni sessione | Nuovo o sbagliato di recente |
| 📦 Box 2 | 3 giorni | Risposto correttamente 1 volta |
| 📦 Box 3 | 7 giorni | Risposto correttamente 2 volte |
| 📦 Box 4 | 14 giorni | Risposto correttamente 3 volte |
| 📦 Box 5 | 30 giorni | Padroneggiato |

### Regole
- ✅ Risposta corretta → passa al box successivo
- ❌ Risposta sbagliata → torna a Box 1
- Quiz in Box 5 da 60+ giorni → `status/mastered`

---

## 🎮 Gamification Challenge

| Attività | XP |
|----------|-----|
| Challenge del giorno completata | +5 |
| Risposta corretta | +10 |
| Risposta sbagliata | +2 (per aver provato!) |
| 5 challenge streak | +25 bonus |
| 10 challenge streak | +50 bonus |
| Quiz → Box 5 (padroneggiato) | +30 |

---

## 📚 Quiz per Argomento

### Architecture

#### Clean Architecture Principles
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLEAN-01 | Struttura con controllers/services/repositories - cosa "urla"? | 📦1 | - | Ora | ⬜ Non risposto |
| CLEAN-02 | Caratteristica comune a TUTTE le clean architectures? | 📦1 | - | Ora | ⬜ Non risposto |

#### Components
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COMP-01 | Cos'è un componente? | 📦1 | - | Ora | ⬜ Non risposto |
| COMP-02 | Perché la Legge di Moore ha influenzato l'architettura dei componenti? | 📦1 | - | Ora | ⬜ Non risposto |

#### Component Cohesion
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COH-01 | REP, CCP, o CRP? OrderValidator + OrderRepository + OrderPdfExporter insieme | 📦1 | - | Ora | ⬜ Non risposto |
| COH-02 | All'inizio progetto, quale principio favorire (REP/CCP/CRP)? | 📦1 | - | Ora | ⬜ Non risposto |

#### Component Coupling
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COUP-01 | Ciclo A → B → C → A - come lo rompi con DIP? | 📦1 | - | Ora | ⬜ Non risposto |
| COUP-02 | Domain dipende da Infrastructure - perché è sbagliato (SDP)? | 📦1 | - | Ora | ⬜ Non risposto |
| COUP-03 | Componente stabile ma concreto - perché è un problema (SAP)? | 📦1 | - | Ora | ⬜ Non risposto |

#### Programming Paradigms
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PARA-01 | Secondo Dijkstra, la programmazione è più simile a... | 📦1 | - | Ora | ⬜ Non risposto |
| PARA-02 | Un collega dice "OOP ha inventato l'encapsulation". Come rispondi? | 📦1 | - | Ora | ⬜ Non risposto |
| PARA-03 | Cosa hanno dimostrato Böhm e Jacopini nel 1966? | 📦1 | - | Ora | ⬜ Non risposto |

---

### SOLID

#### Open/Closed Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OCP-01 | PaymentService usa StripeClient, CEO vuole PayPal - cosa c'è di sbagliato? | 📦4 | 2026-02-17 | 2026-03-03 | ✅ Corretto |
| OCP-02 | OrderProcessor protetto da DatabaseRepository - chi dipende da chi? | 📦4 | 2026-02-19 | 2026-03-05 | ✅ Corretto |
| OCP-03 | Perché Plugin Architecture è conseguenza di OCP? | 📦4 | 2026-02-19 | 2026-03-05 | ✅ Corretto |

#### Single Responsibility Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SRP-01 | Qual è la VERA definizione di SRP? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-02 | ReportGenerator con metodi per Sales, HR, Finance - viola SRP? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-03 | Un collega dice che EmployeeFacade viola SRP. Come rispondi? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-04 | CalculateDiscount() per Sales e Finance - duplicazione vera o accidentale? | 📦1 | - | Ora | ⬜ Non risposto |

#### Liskov Substitution Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| LSP-01 | Perché Square extends Rectangle viola LSP, anche se matematicamente un quadrato È un rettangolo? | 📦1 | - | Ora | ⬜ Non risposto |
| LSP-02 | Nel sistema taxi, cosa succede se arriva un terzo provider con API diversa? | 📦1 | - | Ora | ⬜ Non risposto |
| LSP-03 | Come si applica LSP nel pattern Ports & Adapters? | 📦1 | - | Ora | ⬜ Non risposto |

#### Interface Segregation Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| ISP-01 | IWorker con Work(), Eat(), Sleep() per un Robot - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| ISP-02 | Perché ISP architetturale riduce tempi di ricompilazione? | 📦1 | - | Ora | ⬜ Non risposto |
| ISP-03 | PaymentGateway implementa 3 interfacce piccole - viola SRP? | 📦1 | - | Ora | ⬜ Non risposto |

#### Dependency Inversion Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DIP-01 | OrderService usa direttamente SqlServerRepository. Cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| DIP-02 | Differenza tra Dependency Inversion e Dependency Injection? | 📦1 | - | Ora | ⬜ Non risposto |
| DIP-03 | Dove deve stare l'interfaccia IOrderRepository? | 📦3 | 2026-02-19 | 2026-02-26 | ✅ Corretto |

---

### Patterns

#### Factory Pattern
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FACT-01 | Perché serve una Factory se ho già DIP? | 📦1 | - | Ora | ⬜ Non risposto |
| FACT-02 | Factory vs DI Container - quando preferire Factory? | 📦1 | - | Ora | ⬜ Non risposto |

#### Facade Pattern
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FAC-01 | Stripe payment: Facade o Factory? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |
| FAC-02 | PaymentFacade God Object - cosa faresti? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |
| FAC-03 | Sistema legacy 15 classi PDF - quale pattern? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |

---

### Domain Events
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EVT-01 | Perché dispatchiamo eventi DOPO SaveChanges? | 📦1 | 2026-02-13 | 2026-02-13 | 🟡 Parziale |
| EVT-02 | L'Entity può avere dipendenze come IStatsService? Perché? | 📦3 | 2026-02-19 | 2026-02-26 | ✅ Corretto |
| EVT-03 | Quanti handler possono ascoltare lo stesso evento? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-04 | L'entity può dispatchare direttamente l'evento? Perché? | 📦2 | 2026-02-20 | 2026-02-23 | 🟡 Parziale |
| EVT-05 | Cos'è MediatR in relazione ai Domain Events? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-06 | Validazione email: evento o eccezione? Perché? | 📦1 | - | Ora | ⬜ Non risposto |

### CQRS & MediatR
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CQRS-01 | Un Command può ritornare una lista di oggetti? Perché? | 📦3 | 2026-02-20 | 2026-02-27 | ✅ Corretto |
| CQRS-02 | Un Query Handler può chiamare _repository.Delete()? | 📦1 | - | Ora | ⬜ Non risposto |
| CQRS-03 | Come aggiungi logging a tutti gli handler senza modificarli? | 📦1 | - | Ora | ⬜ Non risposto |
| CQRS-04 | Retry(): la logica va nel Domain o nell'Application? Come decidi? | 📦1 | - | Ora | ⬜ Non risposto |

### FluentValidation
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FV-01 | MustAsync con HasPermissionAsync nel Validator - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| FV-02 | Come validi PhoneNumber solo se Channel == Sms? | 📦1 | - | Ora | ⬜ Non risposto |
| FV-03 | In quale layer vive ScheduleNotificationCommandValidator? | 📦1 | - | Ora | ⬜ Non risposto |

### Ports & Adapters
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PORT-01 | IOrderRepository in Infrastructure/Repositories/ - cosa c'è di sbagliato? | 📦3 | 2026-02-20 | 2026-02-27 | ✅ Corretto |
| PORT-02 | "Un'interfaccia per ogni classe rispetta DIP" - vero o falso? | 📦2 | 2026-02-17 | 2026-02-23 | ✅ Corretto |
| PORT-03 | Perché Application deve "possedere" l'interfaccia? | 📦3 | 2026-02-20 | 2026-02-27 | ✅ Corretto |

### CQRS Queries
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| QRY-01 | Query Handler con SaveChangesAsync - cosa c'è di sbagliato? | 📦2 | 2026-02-17 | 2026-02-23 | ✅ Corretto |
| QRY-02 | Perché Query ritorna DTO invece di Entity? | 📦3 | 2026-02-20 | 2026-02-27 | ✅ Corretto |
| QRY-03 | Query senza parametri ha bisogno di validazione? | 📦2 | 2026-02-17 | 2026-02-23 | ✅ Corretto |

### Application Layer
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| APP-01 | Cosa NON fa l'Application Layer? | 📦1 | - | Ora | ⬜ Non risposto |
| APP-02 | Handler dipende da AppDbContext - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| APP-03 | Come ristrutturi un NotificationService con 15 metodi? | 📦1 | - | Ora | ⬜ Non risposto |

### CQRS Commands
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CMD-01 | Return type corretto per CreateProductCommand? | 📦1 | - | Ora | ⬜ Non risposto |
| CMD-02 | Command che legge prima di cancellare viola CQS? | 📦1 | - | Ora | ⬜ Non risposto |
| CMD-03 | Query + Command separati nel Controller - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |

### Unit of Work
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| UOW-01 | Collega mette SaveChanges in ogni repository - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| UOW-02 | Serve UpdateAsync prima di SaveChanges con EF Core? | 📦1 | - | Ora | ⬜ Non risposto |
| UOW-03 | Perché DbContext deve essere Scoped nel DI? | 📦1 | - | Ora | ⬜ Non risposto |

### Testing Seams
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SEAM-01 | Perché DateTime.UtcNow è problematico nei test? | 📦1 | - | Ora | ⬜ Non risposto |
| SEAM-02 | Dove va l'interfaccia IRandomGenerator? | 📦1 | - | Ora | ⬜ Non risposto |
| SEAM-03 | IMathProvider per Add(a,b) - buona idea? | 📦1 | - | Ora | ⬜ Non risposto |

### Composition Root
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DI-01 | Chi può avere riferimenti a tutti i layer? | 📦1 | - | Ora | ⬜ Non risposto |
| DI-02 | DbContext Singleton con richieste concorrenti? | 📦1 | - | Ora | ⬜ Non risposto |
| DI-03 | Perché AddApplication() invece di tutto in Program.cs? | 📦1 | - | Ora | ⬜ Non risposto |

### Testing con Mocks
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MOCK-01 | Perché Arg.Any invece di valore specifico nel Received()? | 📦1 | - | Ora | ⬜ Non risposto |
| MOCK-02 | Verificare SaveChangesAsync - utile o testing il mock? | 📦1 | - | Ora | ⬜ Non risposto |
| MOCK-03 | Quando usare Fake invece di Mock? | 📦1 | - | Ora | ⬜ Non risposto |

### Infrastructure Layer
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INFRA-01 | Direzione dipendenze: Application può dipendere da Infrastructure? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-02 | Cosa NON appartiene a Infrastructure: Repository, DbContext, o IRepository? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-03 | Perché repository NON chiama SaveChangesAsync? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-04 | EF Core o Dapper per report su milioni di record? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-05 | PostgreSQL vs MongoDB: quali domande fare per decidere? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |

### Repository Pattern
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| REPO-01 | Perché esporre IQueryable<T> dal repository è un anti-pattern? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| REPO-02 | Cos'è il problema N+1 e come lo risolvi? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| REPO-03 | Quando ha senso usare RepositoryBase<T>? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### EF Core Migrations
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MIG-01 | Quali sono 3 vantaggi delle migrations rispetto a SQL manuale? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| MIG-02 | Cosa deve contenere Down() se Up() fa CreateTable? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| MIG-03 | Cosa succede se aggiungi una proprietà senza creare migration? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### Value Object Persistence
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OWN-01 | Owned Type vs Entity: perché non creare tabella separata per VO? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| OWN-02 | Perché EF Core richiede costruttore privato senza parametri? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| OWN-03 | Perché Ignore() su Email/Phone nella configurazione? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### Integration Tests
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INT-01 | Perché non usare InMemory provider di EF Core? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| INT-02 | Unit test vs Integration test: bastano solo gli unit test? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| INT-03 | Cosa trova un integration test che un unit test non trova? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

---

### Design
_Nessun quiz ancora_

---

### Documentation
_Nessun quiz ancora (quiz ADR sono nelle Notes del progetto, non in Knowledge)_

---

## 📅 Storico Challenge

> Aggiornato automaticamente da Claude dopo ogni challenge

| Data | Quiz ID | Risultato | XP | Note |
|------|---------|-----------|-----|------|
| 2026-02-06 | DIP-03 | ✅ | +15 | Prima challenge! |
| 2026-02-09 | DIP-03 | ✅ | +15 | Streak 2! Box 2→3 |
| 2026-02-10 | OCP-01 | ✅ | +15 | Streak 3! Box 2→3 |
| 2026-02-11 | OCP-02 | ✅ | +15 | Streak 4! Box 2→3 |
| 2026-02-11 | OCP-03 | ✅ | +40 | Streak 5! Box 2→3, +25 bonus! |
| 2026-02-13 | EVT-01 | 🟡 | +7 | Parziale - mancava consistenza DB |
| 2026-02-16 | DIP-03 | 🟡 | +7 | Parziale - posizione OK, motivazione imprecisa |
| 2026-02-17 | OCP-01 | ✅ | +15 | Streak 2! Box 3→4 |
| 2026-02-17 | CQRS-01 | ✅ | +10 | Nuovo quiz! Box 1→2 |
| 2026-02-17 | EVT-04 | ✅ | +10 | Nuovo quiz! Box 1→2 |
| 2026-02-19 | OCP-02 | ✅ | +10 | Box 3→4 |
| 2026-02-19 | OCP-03 | ✅ | +10 | Box 3→4 |
| 2026-02-19 | DIP-03 | ✅ | +10 | Box 2→3 (era parziale, ora corretto!) |
| 2026-02-19 | EVT-02 | ✅ | +10 | Box 2→3 |
| 2026-02-20 | EVT-04 | 🟡 | +5 | Parziale - deferred OK, mancava "no dipendenze" |
| 2026-02-20 | CQRS-01 | ✅ | +10 | Box 2→3 |
| 2026-02-20 | PORT-01 | ✅ | +10 | Box 2→3 |
| 2026-02-20 | QRY-02 | ✅ | +10 | Box 2→3 |
| 2026-02-20 | PORT-03 | ✅ | +10 | Box 2→3 |

---

## 🔮 Coda Review (Quiz da ripassare oggi)

> Claude aggiorna questa lista all'inizio di ogni sessione

**Prossimi quiz da ripassare:**
1. Tutti i 6 quiz sono nuovi (Box 1) - pronti per la prima risposta!

---

## 🚨 TODO: Quiz da Knowledge/ (IMPORTANTE!)

> **Gap identificato da Dan (2026-02-18):** La spaced repetition attualmente copre solo i quiz dai `Notes/` del progetto, ma NON quelli dalla Knowledge base.

### Quiz Knowledge da Aggiungere
Le seguenti note in `Knowledge/` hanno quiz che devono essere tracciati:

| Nota | Quiz | Status |
|------|------|--------|
| `solid/single-responsibility-principle.md` | 4 quiz (SRP-01 to SRP-04) | ⚠️ Da verificare duplicati |
| `solid/open-closed-principle.md` | 3 quiz (OCP) | ⚠️ Da verificare duplicati |
| `solid/dependency-inversion-principle.md` | 3 quiz (DIP) | ⚠️ Da verificare duplicati |
| `patterns/facade-pattern.md` | 3 quiz (FAC) | ⚠️ Da verificare duplicati |
| `architecture/programming-paradigms.md` | 3 quiz (PARA) | ⚠️ Da verificare duplicati |
| `architecture/domain-events-theory.md` | ? quiz | ⬜ Da aggiungere |

### Prossimi Step
1. [ ] Verificare quali quiz sono già nel tracker (evitare duplicati)
2. [ ] Aggiungere quiz mancanti da Knowledge/
3. [ ] Unificare tracking: Notes/ e Knowledge/ nello stesso sistema

---

## 📝 Note per Claude

### All'inizio di ogni sessione:
1. Leggi questo file
2. Controlla "Coda Review" per quiz in scadenza
3. Proponi "Challenge del giorno!" con UN quiz:
   - Priorità 1: Quiz in scadenza (spaced repetition)
   - Priorità 2: Quiz non ancora risposti
4. Dopo la risposta di Dan:
   - Aggiorna Box, data, status
   - Assegna XP
   - Se corretto: "Esatto! Infatti: {riassunto dalla nota}"
   - Se sbagliato: "Non preoccuparti! Ripasso veloce: {riassunto dalla nota}"

### Quando creo nuovi quiz:
1. Aggiungi alla tabella dell'argomento corretto
2. Assegna ID univoco (TOPIC-XX)
3. Inizia in Box 1
4. Aggiorna contatore "Quiz totali"

### Formato ID Quiz:
- `PARA-XX` = Programming Paradigms
- `DIP-XX` = Dependency Inversion Principle
- `SRP-XX` = Single Responsibility Principle
- `OCP-XX` = Open/Closed Principle
- `LSP-XX` = Liskov Substitution Principle
- `ISP-XX` = Interface Segregation Principle
- `CLEAN-XX` = Clean Architecture
- `C4-XX` = C4 Model
- `ADR-XX` = Architecture Decision Records
- `DEEP-XX` = Deep Modules
- ... (aggiungi altri man mano)

---

*Ultimo aggiornamento: 2026-02-17*
