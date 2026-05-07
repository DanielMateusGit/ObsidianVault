---
tags: [context, quiz, spaced-repetition]
created: 2026-02-05
updated: 2026-04-24
---

# 🧠 Quiz Tracker - Spaced Repetition

> Claude usa questo file per tracciare tutti i quiz e gestire la spaced repetition.

> **Sync XP:** le statistiche qui sotto sono locali al modulo quiz. Il totale XP globale (incluso quiz + moduli + note + ecc.) vive in `claude/current-state.md` > Progress > XP. Aggiornato ogni `/end` session.

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| **Quiz totali** | 206 |
| **Box 2-5 (Corretti almeno 1 volta)** | 58 |
| **Box 1 - Parziali** | 22 |
| **Box 1 - Sbagliati di recente** | 7 |
| **Box 1 - Non risposti** | 119 |
| **Box 5 - Padroneggiati** | 13 |
| **Challenge completate** | 24 |
| **Streak challenge** | 2 |

> **Nota:** valori sopra sono snapshot del current state. La distribuzione cambia ogni sessione `/quiz`.

---

## 🎯 Sistema Spaced Repetition (a Rotazione, NO date)

### Sessioni di Attesa (Leitner System self-paced)
| Box | Sessioni attesa | Significato |
|-----|-----------------|-------------|
| 📦 Box 1 | 0 (sempre in coda) | Nuovo o sbagliato di recente |
| 📦 Box 2 | 2 sessioni | Risposto correttamente 1 volta |
| 📦 Box 3 | 4 sessioni | Risposto correttamente 2 volte |
| 📦 Box 4 | 8 sessioni | Risposto correttamente 3 volte |
| 📦 Box 5 | 16 sessioni | Padroneggiato |

**Come funziona:**
- La colonna "Sessioni attesa" di ogni quiz contiene un contatore.
- **Contatore = 0** (oppure "0 (in coda)") → il quiz è **in coda** per la prossima sessione.
- **Contatore > 0** → il quiz aspetta. A ogni sessione di spaced repetition: contatore -1.
- Quando il contatore arriva a 0 → il quiz entra automaticamente in coda.

### Regole
- ✅ Risposta corretta → passa al box successivo, reset contatore (Box 2=2, Box 3=4, Box 4=8, Box 5=16)
- ❌ Risposta sbagliata → torna a Box 1, contatore = 0 (in coda)
- 🟡 Parziale → resta nello stesso Box, contatore = 0 (in coda prossima sessione)
- Quiz in Box 5 che ha fatto più di 2 cicli completi → `status/mastered`
- A fine sessione: decrementa di 1 il contatore di TUTTI i quiz Box 2+ con contatore > 0
- **Minimo 10 quiz Box 1 (non risposti) per sessione**, oltre ai quiz in coda
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
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLEAN-01 | Struttura con controllers/services/repositories - cosa "urla"? | 📦1 | 2026-03-25 | 0 (in coda) | 🟡 Parziale |
| CLEAN-02 | Caratteristica comune a TUTTE le clean architectures? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLEAN-03 | Cos'è la Dependency Rule? Qual è l'unica direzione permessa per le dipendenze? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLEAN-04 | Progetto MVC con Controllers/Services/Repositories — ha "Screaming Architecture"? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Components
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COMP-01 | Cos'è un componente? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| COMP-02 | Perché la Legge di Moore ha influenzato l'architettura dei componenti? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Component Cohesion
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COH-01 | REP, CCP, o CRP? OrderValidator + OrderRepository + OrderPdfExporter insieme | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| COH-02 | All'inizio progetto, quale principio favorire (REP/CCP/CRP)? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Component Coupling
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| COUP-01 | Ciclo A → B → C → A - come lo rompi con DIP? | 📦3 | 2026-04-10 | 2 | ✅ Corretto |
| COUP-02 | Domain dipende da Infrastructure - perché è sbagliato (SDP)? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| COUP-03 | Componente stabile ma concreto - perché è un problema (SAP)? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Programming Paradigms
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PARA-01 | Secondo Dijkstra, la programmazione è più simile a... | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| PARA-02 | Un collega dice "OOP ha inventato l'encapsulation". Come rispondi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| PARA-03 | Cosa hanno dimostrato Böhm e Jacopini nel 1966? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

---

### SOLID

#### Open/Closed Principle
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OCP-01 | PaymentService usa StripeClient, CEO vuole PayPal - cosa c'è di sbagliato? | 📦5 | 2026-03-04 | 14 | ✅ Padroneggiato |
| OCP-02 | OrderProcessor protetto da DatabaseRepository - chi dipende da chi? | 📦5 | 2026-03-13 | 14 | ✅ Padroneggiato |
| OCP-03 | Perché Plugin Architecture è conseguenza di OCP? | 📦5 | 2026-03-16 | 14 | ✅ Padroneggiato |

#### Single Responsibility Principle
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SRP-01 | Qual è la VERA definizione di SRP? | 📦4 | 2026-05-06 | 7 | ✅ Corretto |
| SRP-02 | ReportGenerator con metodi per Sales, HR, Finance - viola SRP? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| SRP-03 | Un collega dice che EmployeeFacade viola SRP. Come rispondi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| SRP-04 | CalculateDiscount() per Sales e Finance - duplicazione vera o accidentale? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Liskov Substitution Principle
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| LSP-01 | Perché Square extends Rectangle viola LSP, anche se matematicamente un quadrato È un rettangolo? | 📦1 | 2026-04-10 | 0 (in coda) | 🟡 Parziale |
| LSP-02 | Nel sistema taxi, cosa succede se arriva un terzo provider con API diversa? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| LSP-03 | Come si applica LSP nel pattern Ports & Adapters? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Interface Segregation Principle
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| ISP-01 | IWorker con Work(), Eat(), Sleep() per un Robot - cosa c'è di sbagliato? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| ISP-02 | Perché ISP architetturale riduce tempi di ricompilazione? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| ISP-03 | PaymentGateway implementa 3 interfacce piccole - viola SRP? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Dependency Inversion Principle
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DIP-01 | OrderService usa direttamente SqlServerRepository. Cosa c'è di sbagliato? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| DIP-02 | Differenza tra Dependency Inversion e Dependency Injection? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| DIP-03 | Dove deve stare l'interfaccia IOrderRepository? | 📦5 | 2026-03-25 | 14 | ✅ Padroneggiato |

---

### Patterns

#### Factory Pattern
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FACT-01 | Perché serve una Factory se ho già DIP? | 📦2 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| FACT-02 | Factory vs DI Container - quando preferire Factory? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Facade Pattern
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FAC-01 | Stripe payment: Facade o Factory? | 📦5 | 2026-03-25 | 14 | ✅ Padroneggiato |
| FAC-02 | PaymentFacade God Object - cosa faresti? | 📦4 | 2026-05-06 | 7 | ✅ Corretto |
| FAC-03 | Sistema legacy 15 classi PDF - quale pattern? | 📦4 | 2026-04-01 | 6 | ✅ Corretto |

---

### Domain Events
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EVT-01 | Perché dispatchiamo eventi DOPO SaveChanges? | 📦5 | 2026-03-27 | 14 | ✅ Padroneggiato |
| EVT-02 | L'Entity può avere dipendenze come IStatsService? Perché? | 📦5 | 2026-03-16 | 14 | ✅ Padroneggiato |
| EVT-03 | Quanti handler possono ascoltare lo stesso evento? | 📦4 | 2026-05-07 | 8 | ✅ Corretto |
| EVT-04 | L'entity può dispatchare direttamente l'evento? Perché? | 📦1 | 2026-04-01 | 0 (in coda) | 🟡 Parziale |
| EVT-05 | Cos'è MediatR in relazione ai Domain Events? | 📦3 | 2026-03-28 | 0 (in coda) | ✅ Corretto |
| EVT-06 | Validazione email: evento o eccezione? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### CQRS & MediatR
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CQRS-01 | Un Command può ritornare una lista di oggetti? Perché? | 📦5 | 2026-03-16 | 14 | ✅ Padroneggiato |
| CQRS-02 | Un Query Handler può chiamare _repository.Delete()? | 📦2 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| CQRS-03 | Come aggiungi logging a tutti gli handler senza modificarli? | 📦5 | 2026-03-27 | 14 | ✅ Padroneggiato |
| CQRS-04 | Retry(): la logica va nel Domain o nell'Application? Come decidi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CQRS-05 | Quando ha senso separare database lettura (es. MongoDB) da scrittura (es. PostgreSQL)? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| BEHAV-01 | Ordine registrazione behaviors = ordine esecuzione? | 📦4 | 2026-03-23 | 6 | ✅ Corretto |
| BEHAV-02 | Perché next() solo se validazione passa? | 📦4 | 2026-03-25 | 6 | ✅ Corretto |
| BEHAV-03 | Come creare behavior solo per alcuni command? (marker interface) | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| BEHAV-04 | Come testi un ValidationBehavior in isolamento? Cosa mocki e cosa verifichi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| BEHAV-05 | LoggingBehavior chiama _logger.LogError e poi next(). È corretto? Quando NON dovresti chiamare next()? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |

### FluentValidation
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FV-01 | MustAsync con HasPermissionAsync nel Validator - cosa c'è di sbagliato? | 📦1 | 2026-04-01 | 0 (in coda) | ❌ Sbagliato |
| FV-02 | Come validi PhoneNumber solo se Channel == Sms? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| FV-03 | In quale layer vive ScheduleNotificationCommandValidator? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Ports & Adapters
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PORT-01 | IOrderRepository in Infrastructure/Repositories/ - cosa c'è di sbagliato? | 📦5 | 2026-03-16 | 14 | ✅ Padroneggiato |
| PORT-02 | "Un'interfaccia per ogni classe rispetta DIP" - vero o falso? | 📦5 | 2026-03-25 | 14 | ✅ Padroneggiato |
| PORT-03 | Perché Application deve "possedere" l'interfaccia? | 📦5 | 2026-03-16 | 14 | ✅ Padroneggiato |

### CQRS Queries
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| QRY-01 | Query Handler con SaveChangesAsync - cosa c'è di sbagliato? | 📦4 | 2026-04-10 | 6 | ✅ Corretto |
| QRY-02 | Perché Query ritorna DTO invece di Entity? | 📦4 | 2026-04-01 | 6 | ✅ Corretto |
| QRY-03 | Query senza parametri ha bisogno di validazione? | 📦4 | 2026-03-25 | 6 | ✅ Corretto |

### Application Layer
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| APP-01 | Cosa NON fa l'Application Layer? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| APP-02 | Handler dipende da AppDbContext - cosa c'è di sbagliato? | 📦4 | 2026-03-25 | 6 | ✅ Corretto |
| APP-03 | Come ristrutturi un NotificationService con 15 metodi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### CQRS Commands
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CMD-01 | Return type corretto per CreateProductCommand? | 📦1 | 2026-05-06 | 0 (in coda) | ❌ Sbagliato |
| CMD-02 | Command che legge prima di cancellare viola CQS? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CMD-03 | Query + Command separati nel Controller - cosa c'è di sbagliato? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Unit of Work
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| UOW-01 | Collega mette SaveChanges in ogni repository - cosa c'è di sbagliato? | 📦4 | 2026-03-25 | 6 | ✅ Corretto |
| UOW-02 | Serve UpdateAsync prima di SaveChanges con EF Core? | 📦1 | 2026-04-10 | 0 (in coda) | ❌ Sbagliato |
| UOW-03 | Perché DbContext deve essere Scoped nel DI? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Testing Seams
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SEAM-01 | Perché DateTime.UtcNow è problematico nei test? | 📦1 | 2026-03-28 | 0 (in coda) | 🟡 Parziale |
| SEAM-02 | Dove va l'interfaccia IRandomGenerator? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| SEAM-03 | IMathProvider per Add(a,b) - buona idea? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Composition Root
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DI-01 | Chi può avere riferimenti a tutti i layer? | 📦2 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| DI-02 | DbContext Singleton con richieste concorrenti? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| DI-03 | Perché AddApplication() invece di tutto in Program.cs? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Testing con Mocks
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MOCK-01 | Perché Arg.Any invece di valore specifico nel Received()? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| MOCK-02 | Verificare SaveChangesAsync - utile o testing il mock? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MOCK-03 | Quando usare Fake invece di Mock? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

---

### Claude Code (Corso)

#### Fundamentals
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-01 | Perché serve un Coding Assistant invece di usare direttamente il LLM? | 📦1 | 2026-05-06 | 0 (in coda) | ❌ Sbagliato |
| CLCODE-02 | Preferenza personale async/await: CLAUDE.md, CLAUDE.local.md o ~/.claude/CLAUDE.md? | 📦3 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| CLCODE-03 | Fix bug login: quale approccio contesto è migliore? | 📦3 | 2026-03-28 | 0 (in coda) | ✅ Corretto |
| CLCODE-10 | /init su nuovo progetto: cosa crea automaticamente? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| CLCODE-11 | @file.ts vs @docs/ vs @url: quando usare ciascuno? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-12 | Contesto troppo: quali sono i sintomi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-13 | Tool nativi (Read/Write) vs MCP: quando preferire MCP? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Advanced Features
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-04 | Quick refactoring 3 linee: Opus+High, Sonnet+Medium, o Haiku+Off? | 📦1 | 2026-04-01 | 0 (in coda) | 🟡 Parziale |
| CLCODE-06 | Claude usa .then() invece di async/await: cosa fai? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-14 | Planning Mode + Thinking High: quando usare questa combo? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-15 | Screenshot Ctrl+V: 3 use cases pratici? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-16 | ESC vs ESC+ESC vs /compact vs /clear: quale quando? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-17 | Custom command con argomenti: sintassi nel file .md? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### MCP & Automation
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-05 | Workflow ADO→Claude→GitHub: qual è il ruolo critico dell'umano? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-18 | Setup MCP GitHub: dove va la configurazione? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-19 | MCP locale vs remoto: esempi di ciascuno? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-20 | Workflow semi-automatizzato: quale % automazione vs controllo umano? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Hooks & SDK
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CLCODE-07 | TypeScript check post-edit: come configuri l'hook? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-08 | Claude SDK hook vs linter: qual è il vantaggio? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-09 | Quale NON dovrebbe essere un hook? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-21 | Hook matcher: "**/*.ts" vs "**/src/**" - differenza? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-22 | Hook feedback: error vs warning vs info - quando usare ciascuno? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-23 | Hook chain (tsc→lint→test): come configurare l'ordine? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-24 | Claude SDK in hook: esempio pratico di code review automatico? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CLCODE-25 | Pattern TDD con hook: descrivi il loop automatico | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

---

### Claude Code 101 (Cert)

> Cert in corso. Tracker: `Certifications/claude-code-101/tracker.md`. Note correlate: `Knowledge/ai/agentic-loop.md` (+ future).

#### Lesson 1.1 — How Claude Works (Agentic Loop)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CL101-01 | Le 4 fasi dell'agentic loop in ordine + ruolo di ciascuna | 📦1 | 2026-05-06 | 0 (in coda) | ❌ Sbagliato |
| CL101-02 | Auto-accept mode: per quali azioni Claude chiede ancora conferma? (Edit/Bash/Read) | 📦1 | 2026-05-07 | 0 (in coda) | 🟡 Parziale |
| CL101-03 | Perché serve il passo Verify? Esempio concreto di cosa va male senza | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### EF Core Configurations & Migrations (SE M2 — Knowledge note 2026-05-07)

> Nota: `Knowledge/databases/ef-core-configurations-and-migrations.md`

| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EFCM-01 | Le 3 fonti di regole per le colonne DB (in ordine di priorità crescente)? | 📦1 | 2026-05-07 | 0 (in coda) | ❌ Sbagliato |
| EFCM-02 | Cosa succede quando lanci `dotnet ef migrations add Foo`? Descrivi il flusso modello → snapshot → diff → file generato | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| EFCM-03 | Una migration è un commento o codice eseguibile? Cosa contiene Up()/Down()? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| EFCM-04 | `EnsureCreatedAsync()` vs `MigrateAsync()` — quale usare nei test integration e perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Infrastructure Layer
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INFRA-01 | Direzione dipendenze: Application può dipendere da Infrastructure? | 📦4 | 2026-04-01 | 6 | ✅ Corretto |
| INFRA-02 | Cosa NON appartiene a Infrastructure: Repository, DbContext, o IRepository? | 📦2 | 2026-02-18 | 0 (in coda) | ✅ Corretto |
| INFRA-03 | Perché repository NON chiama SaveChangesAsync? | 📦5 | 2026-03-25 | 14 | ✅ Padroneggiato |
| INFRA-04 | EF Core o Dapper per report su milioni di record? | 📦1 | 2026-04-10 | 0 (in coda) | 🟡 Parziale |
| INFRA-05 | PostgreSQL vs MongoDB: quali domande fare per decidere? | 📦2 | 2026-02-18 | 0 (in coda) | ✅ Corretto |

### Repository Pattern
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| REPO-01 | Perché esporre IQueryable<T> dal repository è un anti-pattern? | 📦1 | 2026-05-07 | 0 (in coda) | 🟡 Parziale |
| REPO-02 | Cos'è il problema N+1 e come lo risolvi? | 📦2 | 2026-04-01 | 0 (in coda) | ✅ Corretto |
| REPO-03 | Quando ha senso usare RepositoryBase<T>? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |

### EF Core Migrations
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MIG-01 | Quali sono 3 vantaggi delle migrations rispetto a SQL manuale? | 📦3 | 2026-05-07 | 4 | ✅ Corretto |
| MIG-02 | Cosa deve contenere Down() se Up() fa CreateTable? | 📦4 | 2026-03-25 | 6 | ✅ Corretto |
| MIG-03 | Cosa succede se aggiungi una proprietà senza creare migration? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |

### Value Object Persistence
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OWN-01 | Owned Type vs Entity: perché non creare tabella separata per VO? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |
| OWN-02 | Perché EF Core richiede costruttore privato senza parametri? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |
| OWN-03 | Perché Ignore() su Email/Phone nella configurazione? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |

### DbContext (EF Core)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DBC-01 | Change Tracker: traccia in memoria o confronta il DB? | 📦4 | 2026-05-06 | 7 | ✅ Corretto |
| DBC-02 | DbContext Singleton con richieste concorrenti — cosa succede? | 📦3 | 2026-03-27 | 0 (in coda) | ✅ Corretto |
| DBC-03 | OnModelCreating con 15 Entity — problema e soluzione? | 📦3 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| DBC-04 | Perché AppDbContext implementa IUnitOfWork? | 📦3 | 2026-03-27 | 0 (in coda) | ✅ Corretto |

### Integration Tests
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| INT-01 | Perché non usare InMemory provider di EF Core? | 📦1 | 2026-03-25 | 0 (in coda) | 🟡 Parziale |
| INT-02 | Unit test vs Integration test: bastano solo gli unit test? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |
| INT-03 | Cosa trova un integration test che un unit test non trova? | 📦2 | 2026-02-19 | 0 (in coda) | ✅ Corretto |

---

### Design (A Philosophy of Software Design)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DEEP-01 | FileProcessor con OpenFile/ReadHeader/ReadBody/ReadFooter/CloseFile - deep o shallow? | 📦1 | 2026-03-28 | 0 (in coda) | 🟡 Parziale (x3) |
| DEEP-02 | INotificationSender con SmtpSettings, retryCount, timeout - qual è il problema? | 📦1 | 2026-03-27 | 0 (in coda) | 🟡 Parziale |
| DEEP-03 | "Ho modificato il formato data e ho cambiato 12 file" - quale sintomo di complessità? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| DEEP-04 | PM chiede feature per domani, sai che il modo veloce crea debito tecnico - cosa fai? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Validation in DDD
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| VAL-01 | Perché TryExecute viola CQS mentre CanExecute/Execute no? | 📦1 | 2026-05-06 | 0 (in coda) | ❌ Sbagliato |
| VAL-02 | Form CRUD 10 campi: quale approccio per validazione Domain? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| VAL-03 | Email 'test@test' passa FluentValidation ma il Domain la rifiuta. È un bug? Perché? | 📦1 | 2026-03-27 | 0 (in coda) | 🟡 Parziale |
| VAL-04 | Costruttore con 10 parametri validati vs Factory Method + private constructor. Quale preferisci e perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| VAL-05 | Il domain model lancia eccezioni per OGNI input invalido (email, telefono, nome). Qual è il problema? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Smart Enum (Senior P1)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SENUM-01 | Perché il costruttore di uno Smart Enum deve essere privato? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| SENUM-02 | Quando vengono costruite le istanze static readonly dal CLR? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| SENUM-03 | Quando useresti enum normale invece di Smart Enum? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

---

### Value Objects (Senior P1)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| VO-01 | Indirizzo Email con stesso valore di un altro Email: sono lo stesso oggetto o due diversi? Perché? | 📦3 | 2026-03-28 | 0 (in coda) | ✅ Corretto |
| VO-02 | Money.Add(other) modifica this o ritorna un nuovo Money? Perché l'immutabilità è importante? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| VO-03 | Perché devi fare override di Equals() E GetHashCode() in un Value Object? Cosa succede se non lo fai? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### .NET Project Structure (Senior P1)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DOTNET-01 | FluentAssertions va nel .csproj di test o di production? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| DOTNET-02 | Qual è il comando per TDD watch mode con dotnet? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| DOTNET-03 | Infrastructure referenzia Application. Può accedere ai tipi Domain? Come? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Exam-Derived (Weak Areas)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EXAM-01 | Entity con public setters e `new Entity {}` — perché viola Always-Valid Domain Model? Come correggi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| EXAM-02 | Cancel() lancia eccezione se Status == Cancelled. Alternativa con CanExecute/Execute? Pro e contro? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| EXAM-03 | Retry logic notifiche (1s, 5s, 30s): le regole vanno in Domain, Application o Infrastructure? E l'orchestrazione? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### AI - Context Management
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CTX-01 | Quali sono i 3 livelli di contesto in Claude Code? Quando usare ciascuno? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CTX-02 | CLAUDE.md nel progetto vs ~/.claude/CLAUDE.md — quale per preferenze globali, quale per regole progetto? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CTX-03 | File da 5000 righe come contesto: come gestisci per non saturare la context window? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### AI - Model Selection Strategy
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MSEL-01 | Bug complesso cross-file con side effects: quale modello + thinking level scegli? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MSEL-02 | Genera boilerplate CRUD (controller + service + repo): Opus, Sonnet o Haiku? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MSEL-03 | Thinking "high" costa 3x in token. Quando vale la pena? Quando è spreco? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### AI - Coding Assistant vs LLM
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CALV-01 | Differenza architetturale tra un LLM raw e un Coding Assistant (Claude Code)? Cosa aggiunge il "harness"? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CALV-02 | Il Coding Assistant legge file, esegue comandi, edita codice. L'LLM raw può farlo? Perché? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CALV-03 | "Agentic loop": cos'è e perché è fondamentale per un Coding Assistant? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Message Queues (AQ P1 W5)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| MQ-01 | Invio email sincrono nell'handler: quali sono almeno 3 problemi concreti? | 📦1 | 2026-03-25 | 0 (in coda) | 🟡 Parziale |
| MQ-02 | Perché il messaggio nella queue contiene solo l'ID e non tutti i dettagli della notifica? | 📦3 | 2026-05-06 | 0 (in coda) | 🟡 Parziale |
| MQ-03 | ACK vs NACK: differenza e cosa succede al messaggio per ciascuno? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| MQ-04 | Worker crasha durante il processing: cosa succede al messaggio? Chi garantisce che non si perda? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| MQ-05 | Worker invia email, crasha prima dell'ACK. Come impedisci doppio invio? (idempotenza) | 📦2 | 2026-03-31 | 0 (in coda) | ✅ Corretto |
| MQ-06 | Nel check idempotenza, perché controlliamo Status == Sent e non == Pending? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-07 | DB vs Queue: chi fa cosa? Completa "Il DB è ______, la Queue è ______" | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-08 | Messaggio fallisce 3 volte: cosa succede? Dove finisce? A cosa serve? (DLQ) | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-09 | Perché IMessagePublisher nell'Application invece di usare direttamente il client RabbitMQ? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-10 | Invisibility timeout: cosa significa? Cosa succede se scade senza ACK? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-11 | At-least-once vs exactly-once: perché non exactly-once? Qual è il trade-off? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-12 | Ordina le operazioni del worker: Invia email, Legge dal DB, Aggiorna status, ACK, Check idempotenza | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| MQ-13 | Flusso completo da POST /notify fino all'email nella inbox — descrivi tutti e 3 gli attori | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### BackgroundService (AQ P1 W5)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| BG-01 | Worker Singleton, Repository Scoped: come li usi insieme? Perché non iniettare nel costruttore? | 📦3 | 2026-03-28 | 0 (in coda) | ✅ Corretto |
| BG-02 | App si spegne, worker sta processando: come garantisci zero perdite? (CancellationToken + ACK) | 📦1 | 2026-04-01 | 0 (in coda) | ❌ Sbagliato |
| BG-03 | Worker stesso processo vs separato: quando separarli? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| BG-04 | AddHostedService: cosa fa? Con quale lifetime registra il servizio? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| BG-05 | Worker con Task.Delay(100) polling: buona idea? Come migliorare? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Outbox Pattern (AQ P1 W5)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OUTBOX-01 | Cos'è il Dual Write Problem? Fai un esempio concreto con DB + RabbitMQ | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| OUTBOX-02 | Outbox Pattern: dove finisce il messaggio PRIMA di arrivare alla queue? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| OUTBOX-03 | OutboxProcessor pubblica in RabbitMQ e crasha prima di aggiornare ProcessedAt. Cosa succede? È un problema? | 📦1 | 2026-04-01 | 0 (in coda) | 🟡 Parziale |
| OUTBOX-04 | "Metto il Publish dentro la transazione DB così è atomico" — perché non funziona? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| OUTBOX-05 | Quando NON serve l'Outbox Pattern? Fai 2 esempi | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| OUTBOX-06 | Outbox vs Compensazione (Publish-then-Save): perché l'Outbox vince? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### RabbitMQ (AQ P1 W5)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| RMQ-01 | Perché il produttore manda all'Exchange e non direttamente alla Queue? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-02 | Queue separate per email e SMS: quale Exchange type e come configuri i binding? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-03 | 1000 msg/s, worker processa 100/s: come risolvi? RabbitMQ crea worker automaticamente? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-04 | Queue durable ma messaggio non persistent: cosa succede al restart di RabbitMQ? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-05 | Topic Exchange con 3 binding (email.*, sms.*, push.*): routing key email.scheduled → quante queue? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-06 | NotificationSent deve arrivare sia ad Analytics che a Billing: Direct o Fanout? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RMQ-07 | Prefetch count = 10: cosa significa? Cosa cambia con prefetch = 1? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### Retry + Error Handling (AQ P1 W5)
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| RETRY-01 | Perché il Worker fa sempre ACK anche quando l'invio fallisce? | 📦1 | 2026-03-31 | 0 (in coda) | 🟡 Parziale |
| RETRY-02 | Notifica Normal fallisce al tentativo 3. Cosa succede? Dove finisce? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RETRY-03 | Worker crasha dopo Fail() ma prima di SaveChanges(). Cosa succede al messaggio? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| RETRY-04 | DLQ applicativa vs DLQ RabbitMQ: perché scegliamo quella applicativa? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

### .NET Fundamentals (Knowledge)

#### CancellationToken
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| CT-01 | CancellationToken: come si produce? Chi decide quando cancellarlo? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CT-02 | "CancellationToken ferma immediatamente l'operazione come Thread.Abort()" — vero o falso? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CT-03 | Handler chiama GetByIdAsync() SENZA passare il ct. Client disconnette durante la query. Cosa succede? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CT-04 | Chi fornisce stoppingToken al BackgroundService? Quando viene cancellato? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| CT-05 | Timeout 30s su chiamata HTTP esterna: come implementi con CancellationToken? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

#### Task & Async
| ID | Domanda | Box | Ultima risposta | Sessioni attesa | Status |
|----|---------|-----|-----------------|-----------------|--------|
| TASK-01 | "Ogni Task crea un nuovo Thread" — vero o falso? Quanti thread per 1000 request async? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| TASK-02 | await GetByIdAsync(): cosa fa il thread durante i 50ms di attesa DB? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| TASK-03 | async void DoSomething(): perché è pericoloso? Cosa succede con un'eccezione? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| TASK-04 | .Result invece di await: funziona? Quali rischi? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |
| TASK-05 | Task vs Task<T>: differenza semantica? Quando usi l'uno e quando l'altro? | 📦1 | - | 0 (in coda) | ⬜ Non risposto |

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
| 2026-03-25 | DIP-03 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-25 | FAC-01 | ✅ | +10 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-25 | APP-02 | ✅ | +10 | Box 3→4 |
| 2026-03-25 | BEHAV-02 | ✅ | +10 | Box 3→4 |
| 2026-03-25 | QRY-02 | ✅ | +10 | Box 2→3 (recuperato da parziale!) |
| 2026-03-25 | EVT-03 | 🟡 | +5 | Box 1→1 (parziale - INotificationHandler vs IRequestHandler) |
| 2026-03-25 | CLCODE-01 | 🟡 | +5 | Box 1→1 (parziale - mancava agentic loop/tool use) |
| 2026-03-25 | PORT-02 | ✅ | +40 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-25 | INFRA-03 | ✅ | +40 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-25 | UOW-01 | ✅ | +10 | Box 3→4 |
| 2026-03-25 | QRY-03 | ✅ | +10 | Box 3→4 |
| 2026-03-25 | EVT-03 | ✅ | +10 | Box 1→2 RECUPERATO da parziale! |
| 2026-03-25 | CLCODE-01 | ✅ | +10 | Box 1→2 RECUPERATO da parziale! |
| 2026-03-25 | CLCODE-02 | ❌ | +2 | Box 1→1 (non conosceva livelli contesto) |
| 2026-03-25 | MQ-01 | 🟡 | +5 | Box 1→1 (parziale - problemi generici, non specifici sincrono) |
| 2026-03-25 | CLEAN-01 | 🟡 | +5 | Box 1→1 (parziale - capito tech, mancava "dovrebbe urlare dominio") |
| 2026-03-25 | DEEP-01 | ❌ | +2 | Box 1→1 (non conosceva deep vs shallow) |
| 2026-03-25 | CMD-01 | 🟡 | +5 | Box 1→1 (parziale - void ok generico, ma Create→Guid) |
| 2026-03-25 | VO-01 | ✅ | +10 | Box 1→2 |
| 2026-03-25 | FAC-03 | ✅ | +10 | Box 2→3 (scaduto, recuperato!) |
| 2026-03-25 | INFRA-01 | ✅ | +10 | Box 2→3 (scaduto, recuperato!) |
| 2026-03-25 | REPO-02 | ❌ | +2 | Box 2→1 (non ricordava N+1) |
| 2026-03-25 | MIG-02 | ✅ | +10 | Box 3→4 |
| 2026-03-25 | INT-01 | 🟡 | +5 | Box 3→1 (parziale - mancava limitazioni tecniche InMemory) |
| 2026-03-25 | FAC-02 | ✅ | +10 | Box 1→2 RECUPERATO da sbagliato! |
| 2026-03-25 | DEEP-01 | ❌ | +2 | Box 1→1 (non ricorda deep/shallow, x2) |
| 2026-03-25 | CLCODE-03 | ✅ | +10 | Box 1→2 |
| 2026-03-25 | MQ-02 | ✅ | +10 | Box 1→2 |
| 2026-03-25 | SRP-01 | ✅ | +10 | Box 1→2 |
| 2026-03-25 | EVT-05 | ✅ | +10 | Box 1→2 |
| 2026-03-25 | BG-01 | ✅ | +10 | Box 1→2 |
| 2026-03-27 | EVT-01 | ✅ | +40 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-27 | CQRS-03 | ✅ | +40 | Box 4→5 🎉 PADRONEGGIATO! |
| 2026-03-27 | DBC-02 | ✅ | +10 | Box 2→3 |
| 2026-03-27 | EVT-04 | 🟡 | +5 | Box 2→2 (parziale - ancora manca "no dipendenze entity") |
| 2026-03-27 | REPO-01 | 🟡 | +5 | Box 2→2 (parziale - solo tech leak, manca encapsulation/query leak) |
| 2026-03-27 | DBC-01 | ✅ | +10 | Box 2→3 |
| 2026-03-27 | DBC-03 | 🟡 | +5 | Box 2→2 (parziale - intuizione giusta, manca IEntityTypeConfiguration) |
| 2026-03-27 | DBC-04 | ✅ | +10 | Box 2→3 |
| 2026-03-27 | QRY-01 | ✅ | +10 | Box 2→3 |
| 2026-03-27 | CLCODE-02 | ✅ | +10 | Box 1→2 RECUPERATO da sbagliato! |
| 2026-03-27 | MQ-03 | ✅ | +10 | Box 1→2 |
| 2026-03-27 | SEAM-01 | ❌ | +2 | Box 1→1 (non ricordava IDateTimeProvider) |
| 2026-03-27 | VAL-03 | 🟡 | +5 | Box 1→1 (parziale - capito i livelli ma non che NON è un bug) |
| 2026-03-27 | VO-02 | ✅ | +10 | Box 1→2 |
| 2026-03-27 | DEEP-02 | 🟡 | +5 | Box 1→1 (parziale - confuso con DIP, è shallow interface) |
| 2026-03-28 | SRP-01 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | EVT-03 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | EVT-05 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | FAC-02 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | CLCODE-01 | ✅ | +35 | Box 2→3, 5 streak bonus! |
| 2026-03-28 | CLCODE-03 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | MQ-02 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | BG-01 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | VO-01 | ✅ | +10 | Box 2→3 |
| 2026-03-28 | SEAM-01 | 🟡 | +5 | Box 1→1 (parziale - troppo vago, manca static/IDateTimeProvider) |
| 2026-03-28 | REPO-02 | ❌ | +2 | Box 1→1 (non ricorda N+1, x2) |
| 2026-03-28 | DEEP-01 | 🟡 | +5 | Box 1→1 (parziale x3 - intuizione giusta ma label invertito) |
| 2026-03-28 | MQ-04 | ✅ | +10 | Box 1→2 |
| 2026-03-28 | OUTBOX-01 | ✅ | +10 | Box 1→2 |
| 2026-03-28 | RETRY-01 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | EVT-04 | ❌ | +2 | Box 2→1 (ancora manca "no dipendenze") |
| 2026-03-31 | CLCODE-02 | ✅ | +10 | Box 2→3 |
| 2026-03-31 | MQ-03 | 🟡 | +5 | Box 2→1 (parziale - confuso retry con requeue) |
| 2026-03-31 | VO-02 | 🟡 | +5 | Box 2→1 (parziale - esempio equality non immutabilità) |
| 2026-03-31 | REPO-01 | 🟡 | +5 | Box 2→1 (parziale - solo tech leak, manca testabilità/N+1) |
| 2026-03-31 | DBC-03 | ✅ | +10 | Box 2→3 |
| 2026-03-31 | OUTBOX-01 | 🟡 | +5 | Box 2→1 (parziale - mancava esempio concreto Save✅/Publish❌) |
| 2026-03-31 | MQ-04 | 🟡 | +5 | Box 2→1 (parziale - impreciso su visibility timeout/broker) |
| 2026-03-31 | RETRY-01 | 🟡 | +5 | Box 2→1 (parziale - idea giusta ma confusa) |
| 2026-03-31 | COUP-01 | ❌ | +2 | Box 1→1 (non conosce inversione dipendenza per rompere cicli) |
| 2026-03-31 | LSP-01 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | FACT-01 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | CQRS-02 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | FV-01 | ❌ | +2 | Box 1→1 (non sapeva: authorization ≠ validation) |
| 2026-03-31 | DI-01 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | CLCODE-10 | 🟡 | +5 | Box 1→1 (parziale - CLAUDE.md ok, manca struttura completa) |
| 2026-03-31 | MQ-05 | ✅ | +10 | Box 1→2 |
| 2026-03-31 | OUTBOX-02 | 🟡 | +5 | Box 1→1 (parziale - confuso tabella DB con "coda outbox") |
| 2026-04-01 | FAC-03 | ✅ | +10 | Box 3→4 |
| 2026-04-01 | QRY-02 | ✅ | +10 | Box 3→4 |
| 2026-04-01 | INFRA-01 | ✅ | +10 | Box 3→4 |
| 2026-04-01 | EVT-04 | 🟡 | +5 | Box 1→1 (parziale - "può farlo" sbagliato, manca "no dipendenze") |
| 2026-04-01 | COUP-01 | ✅ | +10 | Box 1→2 RECUPERATO da sbagliato! |
| 2026-04-01 | FV-01 | ❌ | +2 | Box 1→1 (ancora non sa: authorization ≠ validation) |
| 2026-04-01 | REPO-02 | ✅ | +10 | Box 1→2 RECUPERATO da sbagliato! (N+1 + Include) |
| 2026-04-01 | SRP-02 | ✅ | +10 | Box 1→2 |
| 2026-04-01 | ISP-01 | ✅ | +10 | Box 1→2 |
| 2026-04-01 | DIP-02 | ✅ | +10 | Box 1→2 (DIP=principio, DI=meccanismo) |
| 2026-04-01 | UOW-02 | ❌ | +2 | Box 1→1 (pensava serve Update prima di SaveChanges) |
| 2026-04-01 | BEHAV-05 | ✅ | +10 | Box 1→2 (logging sempre next, validation blocca) |
| 2026-04-01 | CLCODE-04 | 🟡 | +5 | Box 1→1 (parziale - Haiku per refactoring, era Sonnet+Medium) |
| 2026-04-01 | OUTBOX-03 | 🟡 | +5 | Box 1→1 (parziale - confuso su cosa fa il Worker) |
| 2026-04-01 | BG-02 | ❌ | +2 | Box 1→1 (non sapeva CancellationToken + graceful shutdown) |
| 2026-04-01 | MOCK-01 | ✅ | +10 | Box 1→2 (Arg.Any = verifico comportamento, non valore) |
| 2026-04-01 | DI-02 | ✅ | +10 | Box 1→2 (Singleton non thread-safe, serve Scoped) |
| 2026-04-10 | INFRA-04 | 🟡 | +5 | Box 2→1 (parziale - ragionamento su JOIN, manca Change Tracker overhead) |
| 2026-04-10 | LSP-01 | 🟡 | +5 | Box 2→1 (parziale - asimmetria matematica OK, manca postcondizioni/comportamento runtime) |
| 2026-04-10 | COUP-01 | ✅ | +10 | Box 2→3 (interfaccia per invertire + DI container) |
| 2026-04-10 | QRY-01 | ✅ | +10 | Box 3→4 (Query = solo lettura, zero side effects) |
| 2026-04-10 | UOW-02 | ❌ | +2 | Box 1→1 (ancora non sa: Change Tracker traccia automaticamente, no Update needed) |
| 2026-05-06 | SRP-01 | ✅ | +10 | Box 3→4 (definizione moderna Bob: un solo attore) |
| 2026-05-06 | FAC-02 | ✅ | +10 | Box 3→4 (split God Facade in Facade specializzate) |
| 2026-05-06 | DBC-01 | ✅ | +10 | Box 3→4 (in memoria via ChangeTracker, no DB roundtrip) |
| 2026-05-06 | MQ-02 | 🟡 | +5 | Box 3→3 (DB source ok, manca stale data + queue size + idempotenza) |
| 2026-05-06 | CLCODE-01 | ❌ | +2 | Box 3→1 (confuso con prompt eng — manca harness/tools/agentic loop) |
| 2026-05-06 | CMD-01 | ❌ | +2 | Box 1→1 (Create deve ritornare ID, non void/bool — era parziale) |
| 2026-05-06 | VAL-01 | ❌ | +2 | Box 1→1 (non sa CQS / TryExecute side effects) |
| 2026-05-06 | CL101-01 | ❌ | +2 | Box 1→1 (non sa 4 fasi: Gather/Action/Verify/Repeat) |
| 2026-05-07 | EFCM-01 | ❌ | +2 | Box 1→1 (confuso componenti del modello EF [DbContext/DbSet/Domain] con gerarchia priorità regole [Conventions<DataAnnotations<FluentAPI]) |
| 2026-05-07 | EVT-03 | ✅ | +10 | Box 3→4 (handler illimitati per evento, "as many as are registered") |
| 2026-05-07 | MIG-01 | ✅ | +10 | Box 2→3 (3 vantaggi: code-DB consistency + versioning + Up/Down rollback) |
| 2026-05-07 | CL101-02 | 🟡 | +5 | Box 1→1 (parziale - sa Bash ancora chiede, manca Edit/Write/Read auto-approved) |
| 2026-05-07 | REPO-01 | 🟡 | +5 | Box 1→1 (5° parziale - tech leak ok, "DIP" è ripetizione del primo. Manca encapsulation/N+1/testability/perf surprises) |

---

## 🔮 Coda Review (Quiz da ripassare oggi)

> Claude aggiorna questa lista all'inizio di ogni sessione

**Prossimi quiz da ripassare (aggiornato 2026-04-10):**

Scaduti (overdue, Box 2 da febbraio — da fare ASAP):
- INFRA-02, INFRA-05, REPO-03, MIG-01, MIG-03, OWN-01, OWN-02, OWN-03, INT-02, INT-03

Scaduti (overdue, Box 2 da 07-08/04):
- FACT-01, CQRS-02, DI-01, MQ-05 (07/04)
- SRP-02, ISP-01, DIP-02, BEHAV-05, REPO-02, MOCK-01, DI-02 (08/04)

Oggi/domani (2026-04-10 — 2026-04-11):
- Box 3: DBC-01, DBC-02, DBC-04 (10/04)
- Box 3: SRP-01, FAC-02, EVT-03, EVT-05, CLCODE-01, CLCODE-03, MQ-02, BG-01, VO-01 (11/04)

Settimana 2026-04-14 — 2026-04-24:
- Box 3: CLCODE-02, DBC-03 (14/04)
- Box 4: BEHAV-01 (22/04)
- Box 3: COUP-01 (24/04)
- Box 4: QRY-03, BEHAV-02, APP-02, UOW-01, MIG-02 (24/04)

Dopo il 2026-04-24:
- Box 4: FAC-03, QRY-02, INFRA-01 (01/05)
- Box 5: OCP-01 (03/05), OCP-02 (12/05), QRY-01 (10/05), OCP-03/EVT-02/CQRS-01/PORT-01/PORT-03 (15/05), DIP-03/FAC-01/PORT-02/INFRA-03 (24/05), EVT-01/CQRS-03 (26/05)

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
2. Raccogli tutti i quiz con "Sessioni attesa" = 0 (in coda) — priorità Box 2+ più "vecchi in coda"
3. Proponi "Challenge del giorno!" con UN quiz alla volta:
   - Priorità 1: Quiz Box 2+ in coda (contatore = 0)
   - Priorità 2: Quiz Box 1 non ancora risposti (minimo 10 per sessione)
   - Priorità 3: 1 quiz CLCODE (rotazione certificazione)
4. Dopo la risposta di Dan:
   - Aggiorna Box, data ultima risposta, status, contatore "Sessioni attesa"
   - Assegna XP
   - Se corretto: "Esatto! Infatti: {riassunto dalla nota}"
   - Se sbagliato: "Non preoccuparti! Ripasso veloce: {riassunto dalla nota}"
5. A fine sessione spaced repetition: decrementa di 1 "Sessioni attesa" per tutti i quiz Box 2+ con contatore > 0

### Quando creo nuovi quiz:
1. Aggiungi alla tabella dell'argomento corretto
2. Assegna ID univoco (TOPIC-XX)
3. Inizia in Box 1, Sessioni attesa = "0 (in coda)"
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

*Ultimo aggiornamento: 2026-04-17 (sistema a rotazione self-paced: "Prossima review" → "Sessioni attesa", no date)*
