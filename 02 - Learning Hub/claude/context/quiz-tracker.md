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
| **Quiz totali** | 156 |
| **Risposte corrette** | 74 |
| **Risposte parziali** | 8 |
| **Risposte sbagliate** | 2 |
| **Non risposti** | 73 |
| **Challenge completate** | 10 |
| **Streak challenge** | 10 |

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
- **Minimo 2 quiz Box 1 (non risposti) per sessione**, oltre ai quiz scaduti
- **Almeno 1 quiz CLCODE per sessione** (rotazione certificazione)

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
| CLEAN-03 | Cos'è la Dependency Rule? Qual è l'unica direzione permessa per le dipendenze? | 📦1 | - | Ora | ⬜ Non risposto |
| CLEAN-04 | Progetto MVC con Controllers/Services/Repositories — ha "Screaming Architecture"? Perché? | 📦1 | - | Ora | ⬜ Non risposto |

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
| OCP-01 | PaymentService usa StripeClient, CEO vuole PayPal - cosa c'è di sbagliato? | 📦5 | 2026-03-04 | 2026-04-03 | ✅ Padroneggiato |
| OCP-02 | OrderProcessor protetto da DatabaseRepository - chi dipende da chi? | 📦5 | 2026-03-13 | 2026-04-12 | ✅ Padroneggiato |
| OCP-03 | Perché Plugin Architecture è conseguenza di OCP? | 📦5 | 2026-03-16 | 2026-04-15 | ✅ Padroneggiato |

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
| DIP-03 | Dove deve stare l'interfaccia IOrderRepository? | 📦4 | 2026-02-28 | 2026-03-14 | ✅ Corretto |

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
| FAC-01 | Stripe payment: Facade o Factory? | 📦4 | 2026-03-04 | 2026-03-18 | ✅ Corretto |
| FAC-02 | PaymentFacade God Object - cosa faresti? | 📦1 | 2026-03-23 | Ora | ❌ Sbagliato |
| FAC-03 | Sistema legacy 15 classi PDF - quale pattern? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |

---

### Domain Events
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EVT-01 | Perché dispatchiamo eventi DOPO SaveChanges? | 📦4 | 2026-03-13 | 2026-03-27 | ✅ Corretto |
| EVT-02 | L'Entity può avere dipendenze come IStatsService? Perché? | 📦5 | 2026-03-16 | 2026-04-15 | ✅ Padroneggiato |
| EVT-03 | Quanti handler possono ascoltare lo stesso evento? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-04 | L'entity può dispatchare direttamente l'evento? Perché? | 📦2 | 2026-03-23 | 2026-03-26 | 🟡 Parziale |
| EVT-05 | Cos'è MediatR in relazione ai Domain Events? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-06 | Validazione email: evento o eccezione? Perché? | 📦1 | - | Ora | ⬜ Non risposto |

### CQRS & MediatR
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CQRS-01 | Un Command può ritornare una lista di oggetti? Perché? | 📦5 | 2026-03-16 | 2026-04-15 | ✅ Padroneggiato |
| CQRS-02 | Un Query Handler può chiamare _repository.Delete()? | 📦1 | - | Ora | ⬜ Non risposto |
| CQRS-03 | Come aggiungi logging a tutti gli handler senza modificarli? | 📦4 | 2026-03-13 | 2026-03-27 | ✅ Corretto |
| CQRS-04 | Retry(): la logica va nel Domain o nell'Application? Come decidi? | 📦1 | - | Ora | ⬜ Non risposto |
| CQRS-05 | Quando ha senso separare database lettura (es. MongoDB) da scrittura (es. PostgreSQL)? | 📦1 | - | Ora | ⬜ Non risposto |
| BEHAV-01 | Ordine registrazione behaviors = ordine esecuzione? | 📦4 | 2026-03-23 | 2026-04-06 | ✅ Corretto |
| BEHAV-02 | Perché next() solo se validazione passa? | 📦3 | 2026-02-28 | 2026-03-07 | ✅ Corretto |
| BEHAV-03 | Come creare behavior solo per alcuni command? (marker interface) | 📦1 | - | Ora | ⬜ Non risposto |
| BEHAV-04 | Come testi un ValidationBehavior in isolamento? Cosa mocki e cosa verifichi? | 📦1 | - | Ora | ⬜ Non risposto |
| BEHAV-05 | LoggingBehavior chiama _logger.LogError e poi next(). È corretto? Quando NON dovresti chiamare next()? | 📦1 | - | Ora | ⬜ Non risposto |

### FluentValidation
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FV-01 | MustAsync con HasPermissionAsync nel Validator - cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| FV-02 | Come validi PhoneNumber solo se Channel == Sms? | 📦1 | - | Ora | ⬜ Non risposto |
| FV-03 | In quale layer vive ScheduleNotificationCommandValidator? | 📦1 | - | Ora | ⬜ Non risposto |

### Ports & Adapters
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PORT-01 | IOrderRepository in Infrastructure/Repositories/ - cosa c'è di sbagliato? | 📦5 | 2026-03-16 | 2026-04-15 | ✅ Padroneggiato |
| PORT-02 | "Un'interfaccia per ogni classe rispetta DIP" - vero o falso? | 📦4 | 2026-03-04 | 2026-03-18 | ✅ Corretto |
| PORT-03 | Perché Application deve "possedere" l'interfaccia? | 📦5 | 2026-03-16 | 2026-04-15 | ✅ Padroneggiato |

### CQRS Queries
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| QRY-01 | Query Handler con SaveChangesAsync - cosa c'è di sbagliato? | 📦2 | 2026-03-23 | 2026-03-26 | ✅ Corretto |
| QRY-02 | Perché Query ritorna DTO invece di Entity? | 📦2 | 2026-03-02 | 2026-03-05 | 🟡 Parziale |
| QRY-03 | Query senza parametri ha bisogno di validazione? | 📦3 | 2026-02-24 | 2026-03-03 | ✅ Corretto |

### Application Layer
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| APP-01 | Cosa NON fa l'Application Layer? | 📦1 | - | Ora | ⬜ Non risposto |
| APP-02 | Handler dipende da AppDbContext - cosa c'è di sbagliato? | 📦3 | 2026-03-13 | 2026-03-20 | ✅ Corretto |
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
| UOW-01 | Collega mette SaveChanges in ogni repository - cosa c'è di sbagliato? | 📦3 | 2026-03-13 | 2026-03-20 | ✅ Corretto |
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

---

### Claude Code (Corso)

#### Fundamentals
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-01 | Perché serve un Coding Assistant invece di usare direttamente il LLM? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-02 | Preferenza personale async/await: CLAUDE.md, CLAUDE.local.md o ~/.claude/CLAUDE.md? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-03 | Fix bug login: quale approccio contesto è migliore? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-10 | /init su nuovo progetto: cosa crea automaticamente? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-11 | @file.ts vs @docs/ vs @url: quando usare ciascuno? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-12 | Contesto troppo: quali sono i sintomi? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-13 | Tool nativi (Read/Write) vs MCP: quando preferire MCP? | 📦1 | - | Ora | ⬜ Non risposto |

#### Advanced Features
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-04 | Quick refactoring 3 linee: Opus+High, Sonnet+Medium, o Haiku+Off? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-06 | Claude usa .then() invece di async/await: cosa fai? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-14 | Planning Mode + Thinking High: quando usare questa combo? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-15 | Screenshot Ctrl+V: 3 use cases pratici? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-16 | ESC vs ESC+ESC vs /compact vs /clear: quale quando? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-17 | Custom command con argomenti: sintassi nel file .md? | 📦1 | - | Ora | ⬜ Non risposto |

#### MCP & Automation
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-05 | Workflow ADO→Claude→GitHub: qual è il ruolo critico dell'umano? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-18 | Setup MCP GitHub: dove va la configurazione? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-19 | MCP locale vs remoto: esempi di ciascuno? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-20 | Workflow semi-automatizzato: quale % automazione vs controllo umano? | 📦1 | - | Ora | ⬜ Non risposto |

#### Hooks & SDK
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-07 | TypeScript check post-edit: come configuri l'hook? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-08 | Claude SDK hook vs linter: qual è il vantaggio? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-09 | Quale NON dovrebbe essere un hook? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-21 | Hook matcher: "**/*.ts" vs "**/src/**" - differenza? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-22 | Hook feedback: error vs warning vs info - quando usare ciascuno? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-23 | Hook chain (tsc→lint→test): come configurare l'ordine? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-24 | Claude SDK in hook: esempio pratico di code review automatico? | 📦1 | - | Ora | ⬜ Non risposto |
| CLCODE-25 | Pattern TDD con hook: descrivi il loop automatico | 📦1 | - | Ora | ⬜ Non risposto |

### Infrastructure Layer
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INFRA-01 | Direzione dipendenze: Application può dipendere da Infrastructure? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-02 | Cosa NON appartiene a Infrastructure: Repository, DbContext, o IRepository? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-03 | Perché repository NON chiama SaveChangesAsync? | 📦4 | 2026-03-04 | 2026-03-18 | ✅ Corretto |
| INFRA-04 | EF Core o Dapper per report su milioni di record? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |
| INFRA-05 | PostgreSQL vs MongoDB: quali domande fare per decidere? | 📦2 | 2026-02-18 | 2026-02-21 | ✅ Corretto |

### Repository Pattern
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| REPO-01 | Perché esporre IQueryable<T> dal repository è un anti-pattern? | 📦2 | 2026-03-23 | 2026-03-26 | 🟡 Parziale |
| REPO-02 | Cos'è il problema N+1 e come lo risolvi? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| REPO-03 | Quando ha senso usare RepositoryBase<T>? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### EF Core Migrations
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MIG-01 | Quali sono 3 vantaggi delle migrations rispetto a SQL manuale? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| MIG-02 | Cosa deve contenere Down() se Up() fa CreateTable? | 📦3 | 2026-02-25 | 2026-03-04 | ✅ Corretto |
| MIG-03 | Cosa succede se aggiungi una proprietà senza creare migration? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### Value Object Persistence
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OWN-01 | Owned Type vs Entity: perché non creare tabella separata per VO? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| OWN-02 | Perché EF Core richiede costruttore privato senza parametri? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| OWN-03 | Perché Ignore() su Email/Phone nella configurazione? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

### DbContext (EF Core)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DBC-01 | Change Tracker: traccia in memoria o confronta il DB? | 📦2 | 2026-03-24 | 2026-03-27 | ✅ Corretto |
| DBC-02 | DbContext Singleton con richieste concorrenti — cosa succede? | 📦2 | 2026-03-24 | 2026-03-27 | ✅ Corretto |
| DBC-03 | OnModelCreating con 15 Entity — problema e soluzione? | 📦2 | 2026-03-24 | 2026-03-27 | ✅ Corretto |
| DBC-04 | Perché AppDbContext implementa IUnitOfWork? | 📦2 | 2026-03-24 | 2026-03-27 | ✅ Corretto |

### Integration Tests
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INT-01 | Perché non usare InMemory provider di EF Core? | 📦3 | 2026-02-25 | 2026-03-04 | ✅ Corretto |
| INT-02 | Unit test vs Integration test: bastano solo gli unit test? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |
| INT-03 | Cosa trova un integration test che un unit test non trova? | 📦2 | 2026-02-19 | 2026-02-22 | ✅ Corretto |

---

### Design (A Philosophy of Software Design)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DEEP-01 | FileProcessor con OpenFile/ReadHeader/ReadBody/ReadFooter/CloseFile - deep o shallow? | 📦1 | - | Ora | ⬜ Non risposto |
| DEEP-02 | INotificationSender con SmtpSettings, retryCount, timeout - qual è il problema? | 📦1 | - | Ora | ⬜ Non risposto |
| DEEP-03 | "Ho modificato il formato data e ho cambiato 12 file" - quale sintomo di complessità? | 📦1 | - | Ora | ⬜ Non risposto |
| DEEP-04 | PM chiede feature per domani, sai che il modo veloce crea debito tecnico - cosa fai? | 📦1 | - | Ora | ⬜ Non risposto |

### Validation in DDD
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| VAL-01 | Perché TryExecute viola CQS mentre CanExecute/Execute no? | 📦1 | - | Ora | ⬜ Non risposto |
| VAL-02 | Form CRUD 10 campi: quale approccio per validazione Domain? | 📦1 | - | Ora | ⬜ Non risposto |
| VAL-03 | Email 'test@test' passa FluentValidation ma il Domain la rifiuta. È un bug? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| VAL-04 | Costruttore con 10 parametri validati vs Factory Method + private constructor. Quale preferisci e perché? | 📦1 | - | Ora | ⬜ Non risposto |
| VAL-05 | Il domain model lancia eccezioni per OGNI input invalido (email, telefono, nome). Qual è il problema? | 📦1 | - | Ora | ⬜ Non risposto |

### Smart Enum (Senior P1)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SENUM-01 | Perché il costruttore di uno Smart Enum deve essere privato? | 📦1 | - | Ora | ⬜ Non risposto |
| SENUM-02 | Quando vengono costruite le istanze static readonly dal CLR? | 📦1 | - | Ora | ⬜ Non risposto |
| SENUM-03 | Quando useresti enum normale invece di Smart Enum? | 📦1 | - | Ora | ⬜ Non risposto |

---

### Value Objects (Senior P1)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| VO-01 | Indirizzo Email con stesso valore di un altro Email: sono lo stesso oggetto o due diversi? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| VO-02 | Money.Add(other) modifica this o ritorna un nuovo Money? Perché l'immutabilità è importante? | 📦1 | - | Ora | ⬜ Non risposto |
| VO-03 | Perché devi fare override di Equals() E GetHashCode() in un Value Object? Cosa succede se non lo fai? | 📦1 | - | Ora | ⬜ Non risposto |

### .NET Project Structure (Senior P1)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DOTNET-01 | FluentAssertions va nel .csproj di test o di production? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| DOTNET-02 | Qual è il comando per TDD watch mode con dotnet? | 📦1 | - | Ora | ⬜ Non risposto |
| DOTNET-03 | Infrastructure referenzia Application. Può accedere ai tipi Domain? Come? | 📦1 | - | Ora | ⬜ Non risposto |

### Exam-Derived (Weak Areas)
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EXAM-01 | Entity con public setters e `new Entity {}` — perché viola Always-Valid Domain Model? Come correggi? | 📦1 | - | Ora | ⬜ Non risposto |
| EXAM-02 | Cancel() lancia eccezione se Status == Cancelled. Alternativa con CanExecute/Execute? Pro e contro? | 📦1 | - | Ora | ⬜ Non risposto |
| EXAM-03 | Retry logic notifiche (1s, 5s, 30s): le regole vanno in Domain, Application o Infrastructure? E l'orchestrazione? | 📦1 | - | Ora | ⬜ Non risposto |

### AI - Context Management
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CTX-01 | Quali sono i 3 livelli di contesto in Claude Code? Quando usare ciascuno? | 📦1 | - | Ora | ⬜ Non risposto |
| CTX-02 | CLAUDE.md nel progetto vs ~/.claude/CLAUDE.md — quale per preferenze globali, quale per regole progetto? | 📦1 | - | Ora | ⬜ Non risposto |
| CTX-03 | File da 5000 righe come contesto: come gestisci per non saturare la context window? | 📦1 | - | Ora | ⬜ Non risposto |

### AI - Model Selection Strategy
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MSEL-01 | Bug complesso cross-file con side effects: quale modello + thinking level scegli? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| MSEL-02 | Genera boilerplate CRUD (controller + service + repo): Opus, Sonnet o Haiku? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| MSEL-03 | Thinking "high" costa 3x in token. Quando vale la pena? Quando è spreco? | 📦1 | - | Ora | ⬜ Non risposto |

### AI - Coding Assistant vs LLM
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CALV-01 | Differenza architetturale tra un LLM raw e un Coding Assistant (Claude Code)? Cosa aggiunge il "harness"? | 📦1 | - | Ora | ⬜ Non risposto |
| CALV-02 | Il Coding Assistant legge file, esegue comandi, edita codice. L'LLM raw può farlo? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| CALV-03 | "Agentic loop": cos'è e perché è fondamentale per un Coding Assistant? | 📦1 | - | Ora | ⬜ Non risposto |

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
| 2026-02-24 | EVT-04 | ✅ | +10 | Box 2→3 |
| 2026-02-24 | PORT-02 | ✅ | +10 | Box 2→3 |
| 2026-02-24 | QRY-01 | 🟡 | +5 | Box 2→1 (Query con side effects) |
| 2026-02-24 | QRY-03 | ✅ | +10 | Box 2→3 |
| 2026-02-25 | FAC-01 | ✅ | +10 | Box 2→3 |
| 2026-02-25 | INFRA-03 | ✅ | +10 | Box 2→3 |
| 2026-02-25 | REPO-01 | ❌ | +2 | Box 2→1 (non ricordava) |
| 2026-02-25 | MIG-02 | ✅ | +10 | Box 2→3 |
| 2026-02-25 | INT-01 | ✅ | +10 | Box 2→3 |
| 2026-02-25 | BEHAV-01 | ✅ | +10 | Nuovo - ordine behaviors |
| 2026-02-25 | BEHAV-02 | ✅ | +10 | Nuovo - next() e validazione |
| 2026-02-28 | CQRS-03 | ✅ | +10 | Box 2→3 |
| 2026-02-28 | BEHAV-01 | ✅ | +10 | Box 2→3 |
| 2026-02-28 | BEHAV-02 | ✅ | +10 | Box 2→3 |
| 2026-02-28 | REPO-01 | ✅ | +10 | Box 1→2 RECUPERATO! |
| 2026-02-28 | DIP-03 | ✅ | +35 | Box 3→4, 5 streak bonus! |
| 2026-03-02 | EVT-01 | ✅ | +10 | Box 1→2 (recuperato!) |
| 2026-03-02 | EVT-02 | ✅ | +10 | Box 3→4 |
| 2026-03-02 | CQRS-01 | ✅ | +10 | Box 3→4 |
| 2026-03-02 | PORT-01 | ✅ | +10 | Box 3→4 |
| 2026-03-02 | PORT-03 | ✅ | +10 | Box 3→4 |
| 2026-03-02 | QRY-02 | 🟡 | +5 | Box 3→2 (parziale - encapsulation) |
| 2026-03-04 | OCP-01 | ✅ | +10 | Box 4→5 🎉 PRIMO PADRONEGGIATO! |
| 2026-03-04 | EVT-04 | 🟡 | +5 | Box 3→2 (parziale - mancava "no dipendenze") |
| 2026-03-04 | INFRA-03 | ✅ | +10 | Box 3→4 |
| 2026-03-04 | FAC-01 | ✅ | +10 | Box 3→4 |
| 2026-03-04 | PORT-02 | ✅ | +10 | Box 3→4 |
| 2026-03-04 | UOW-01 | ✅ | +10 | Box 1→2 (primo UoW!) |
| 2026-03-04 | APP-02 | ✅ | +10 | Box 1→2 |
| 2026-03-04 | EVT-01 | ✅ | +10 | Box 2→3 |
| 2026-03-13 | EVT-01 | ✅ | +10 | Box 3→4 |
| 2026-03-13 | UOW-01 | ✅ | +10 | Box 2→3 |
| 2026-03-13 | OCP-02 | ✅ | +40 | Box 4→5 🎉 PADRONEGGIATO + 5 streak bonus! |
| 2026-03-13 | CQRS-03 | ✅ | +10 | Box 3→4 |
| 2026-03-13 | APP-02 | ✅ | +10 | Box 2→3 |
| 2026-03-16 | EVT-02 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-16 | CQRS-01 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-16 | PORT-01 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-16 | PORT-03 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-16 | OCP-03 | ✅ | +35 | Box 4→5 🎉 PADRONEGGIATO + 10 streak bonus! |
| 2026-03-23 | QRY-01 | ✅ | +10 | Box 1→2 RECUPERATO da parziale! |
| 2026-03-23 | EVT-04 | 🟡 | +5 | Box 2→2 (parziale - ancora manca "no dipendenze") |
| 2026-03-23 | FAC-02 | ❌ | +2 | Box 2→1 (confuso facade con soluzione) |
| 2026-03-23 | REPO-01 | 🟡 | +5 | Box 2→2 (parziale - solo tech leak, mancano altri motivi) |
| 2026-03-23 | BEHAV-01 | ✅ | +10 | Box 3→4 |

---

## 🔮 Coda Review (Quiz da ripassare oggi)

> Claude aggiorna questa lista all'inizio di ogni sessione

**Prossimi quiz da ripassare:**
1. FAC-02 (Ora) - Box 1, da recuperare
2. EVT-04 (2026-03-26), QRY-01 (2026-03-26), REPO-01 (2026-03-26) - Box 2
3. EVT-01 (2026-03-27), CQRS-03 (2026-03-27) - Box 4
4. BEHAV-01 (2026-04-06) - Box 4
5. Scaduti non ancora ripassati: FAC-01, PORT-02, INFRA-03, DIP-03, APP-02, UOW-01, BEHAV-02, QRY-03, FAC-03, + molti Box 2 da febbraio

### Priorita Certificazione: CLCODE (almeno 1/giorno)

> I quiz CLCODE hanno priorita alta. Dan deve ripassare **almeno 1 concetto al giorno** dalla certificazione Claude Code in Action. Claude seleziona 1-2 quiz CLCODE ad ogni sessione, anche se non sono in scadenza.

**Rotazione giornaliera suggerita (ciclo su 25 quiz):**
- Fundamentals: CLCODE-01, 02, 03, 10, 11, 12, 13
- Advanced: CLCODE-04, 06, 14, 15, 16, 17
- MCP & Automation: CLCODE-05, 18, 19, 20
- Hooks & SDK: CLCODE-07, 08, 09, 21, 22, 23, 24, 25

---

## ✅ Knowledge Quiz Integration (COMPLETATA 2026-03-24)

> **Gap identificato da Dan (2026-02-18)**, risolto il **2026-03-24**.
> Tutti i quiz da Knowledge/ e Senior-Engineer/Notes/ sono ora tracciati.
> Vedi "Source Mapping" in fondo per la mappa completa quiz→nota.

### Azioni completate:
1. [x] Verificati duplicati tra Knowledge/ e tracker (vedi "Overlap noti")
2. [x] Aggiunti 25 nuovi quiz: VO-01/02/03, DOTNET-01/02/03, EXAM-01/02/03, CTX-01/02/03, MSEL-01/02/03, CALV-01/02/03, CLEAN-03/04, VAL-03/04/05, CQRS-05, BEHAV-04/05
3. [x] Nomenclatura con Source Mapping per evitare futuri duplicati
4. [x] Regola "2 Box 1 per sessione" aggiunta

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
- `VAL-XX` = Validation in DDD
- `SENUM-XX` = Smart Enum
- `VO-XX` = Value Objects
- `DOTNET-XX` = .NET Project Structure
- `EXAM-XX` = Derivato da esame (weak areas)
- `CTX-XX` = Context Management (AI)
- `MSEL-XX` = Model Selection Strategy (AI)
- `CALV-XX` = Coding Assistant vs LLM (AI)
- `EVT-XX` = Domain Events
- `CQRS-XX` = CQRS & MediatR
- `BEHAV-XX` = Pipeline Behaviors
- `FV-XX` = FluentValidation
- `CMD-XX` = CQRS Commands
- `QRY-XX` = CQRS Queries
- `PORT-XX` = Ports & Adapters
- `APP-XX` = Application Layer
- `UOW-XX` = Unit of Work
- `REPO-XX` = Repository Pattern
- `INFRA-XX` = Infrastructure Layer
- `MIG-XX` = EF Core Migrations
- `OWN-XX` = Value Object Persistence (Owned Types)
- `INT-XX` = Integration Tests
- `SEAM-XX` = Testing Seams
- `MOCK-XX` = Testing con Mocks
- `DI-XX` = Composition Root / DI
- `FACT-XX` = Factory Pattern
- `FAC-XX` = Facade Pattern
- `CLCODE-XX` = Claude Code (Corso Anthropic)

### Source Mapping (Origine Quiz)

> Per evitare duplicati e sapere da dove viene ogni quiz.
> Formato: `ID → source_file`

| Prefisso | Source principale | Note secondarie |
|----------|------------------|-----------------|
| CLEAN | `Knowledge/architecture/clean-architecture-principles.md` | — |
| COMP | `Knowledge/architecture/components.md` | — |
| COH | `Knowledge/architecture/component-cohesion.md` | — |
| COUP | `Knowledge/architecture/component-coupling.md` | — |
| PARA | `Knowledge/architecture/programming-paradigms.md` | — |
| EVT | `Knowledge/architecture/domain-events-theory.md` | `Senior-Engineer/.../domain-events.md` |
| VAL | `Knowledge/architecture/validation-vs-invariants.md` | — |
| OCP | `Knowledge/solid/open-closed-principle.md` | — |
| SRP | `Knowledge/solid/single-responsibility-principle.md` | — |
| LSP | `Knowledge/solid/liskov-substitution-principle.md` | — |
| ISP | `Knowledge/solid/interface-segregation-principle.md` | — |
| DIP | `Knowledge/solid/dependency-inversion-principle.md` | — |
| DEEP | `Knowledge/design/deep-modules.md` | — |
| FAC | `Knowledge/patterns/facade-pattern.md` | — |
| FACT | `Knowledge/patterns/factory-pattern.md` | — |
| REPO | `Knowledge/patterns/repository-pattern.md` | `Senior-Engineer/.../repository-interfaces.md` |
| UOW | `Knowledge/patterns/unit-of-work-pattern.md` | — |
| BEHAV | `Knowledge/patterns/mediatr-pipeline-behaviors.md` | `Senior-Engineer/.../W1-queries-validation-behaviors.md` |
| CQRS | `Knowledge/architecture/cqrs-pattern.md` | — |
| SENUM | `Senior-Engineer/.../smart-enum.md` | `Senior-Engineer/.../domain-building-blocks.md` |
| VO | `Senior-Engineer/.../value-objects.md` | — |
| DOTNET | `Senior-Engineer/.../dotnet-project-structure.md` | — |
| EXAM | `Exams/esame_2026-02-28.md` | Weak areas da esami |
| CTX | `Knowledge/ai/context-management.md` | — |
| MSEL | `Knowledge/ai/model-selection-strategy.md` | Overlap con CLCODE-04 |
| CALV | `Knowledge/ai/coding-assistant-vs-llm.md` | Overlap con CLCODE-01 |
| CLCODE | Corso Anthropic "Claude Code in Action" | Overlap con Knowledge/ai/* |
| FV | `Knowledge/architecture/validation-vs-invariants.md` | AQ P1 Notes |
| CMD/QRY | `Knowledge/architecture/cqrs-pattern.md` | Senior P1 Notes |
| PORT | `Knowledge/solid/dependency-inversion-principle.md` | AQ P1 Notes |
| APP | AQ P1 Notes | — |
| INFRA/MIG/OWN/INT | AQ P1 Notes (Week 4) | — |
| SEAM/MOCK/DI | AQ P1 Notes | — |

### Overlap noti (NON duplicati)

> Quiz che coprono argomenti simili da fonti diverse. Tenuti entrambi perché angolazioni diverse.

| Quiz A | Quiz B | Perché non è duplicato |
|--------|--------|----------------------|
| CLCODE-01 | CALV-01 | CLCODE: pratico (tool). CALV: teorico (architettura) |
| CLCODE-04 | MSEL-01 | CLCODE: scenario specifico. MSEL: strategia generale |
| CLCODE-12 | CTX-03 | CLCODE: sintomi. CTX: soluzione |
| EVT-01/02/03 | Senior P1 domain-events.md Q1/Q2/Q3 | Stessi concetti, già unificati sotto EVT-xx |
| REPO-01/02/03 | Senior P1 repository-interfaces.md Q1/Q2/Q3 | Stessi concetti, già unificati sotto REPO-xx |

---

*Ultimo aggiornamento: 2026-03-24*
