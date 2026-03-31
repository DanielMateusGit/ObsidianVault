# 💻 Roadmap Completa: Senior Engineer Path

> Percorso 30-36 mesi da mid-level a senior engineer internazionale
> *(10-15 ore/settimana con lavoro full-time. Tempo reale varia.)*

## 🎯 Obiettivo Finale

- Padroneggiare TDD e design patterns (sapere QUANDO usarli)
- Essere esperto Redis (da caching a primary DB)
- Implementare CQRS e Event Sourcing
- Avere portfolio pronto per aziende internazionali
- **Superare system design interviews** 🎤
- **Comunicare efficacemente in team remoti** 🌍
- **Target:** AI Engineer / Senior Engineer €90k-130k+ remote
- **Nota:** Le skill Senior sono la BASE solida su cui costruisci il ruolo AI Engineer (vedi `ai-skills.md`)

---

## 📅 Timeline Overview

```
Settimane 1-3:   P1 - Task Manager (Clean Arch, TDD, CQRS, Redis cache) ⭐ MINIMO
Settimana 4:     P1.5 - Auth & Security 🔐 (JWT, OWASP basics) ⭐ MINIMO
Settimane 5-7:   P2 - Chat App (SignalR, Redis Pub/Sub) ⭐ MINIMO
Settimane 8-11:  P3 - E-commerce Cart (CQRS, Event Sourcing) ⭐ MINIMO
Settimane 12-14: P4 - Alert Gateway (Microservices, Circuit Breaker) 🔹 COMPLETO
Settimane 15-17: P5 - URL Shortener (Redis as Primary DB) 🔹 COMPLETO
Mesi 6-16:       P6 - Capstone: AI Second Brain (RAG + tutti i pattern) 🔹 COMPLETO
```

> ⭐ **MINIMO** = Obbligatorio per primo colloquio €85k+
> 🔹 **COMPLETO** = Percorso completo 30-36 mesi

> **Nota:** Le settimane sopra sono una stima ottimistica. A 10-15 ore/settimana,
> ogni "settimana" di progetto puo richiedere 2-3 settimane reali.
> Career Boost Module è separato: vedi `roadmaps/career-boost.md`

### 🔄 Rinforzo con Architect Quest
```
Senior P1 (Task Manager)     ←→  Architect P1 (Notification) = Clean Arch
Senior P1.5 (Auth)           ←→  Architect P2 (Azure AD B2C) = Auth patterns
Senior P3 (E-commerce)       ←→  Architect P2 (NutriPlan) = CQRS, Event Sourcing
Senior P4 (Alert Gateway)    ←→  Architect P3 (BookingHub) = Microservices, Saga
Senior P2 (Chat)             ←→  Architect P4 (FamilyBudget) = Real-time, SignalR
```

### 📨 Progressione Messaging (cross-progetto)
```
P1 W3:  Redis Pub/Sub           → messaging in-process, semplice
P2 W5:  RabbitMQ base           → broker esterno, un producer/consumer
P3 W10: Outbox Pattern (TDD)    → consistenza DB/Queue, costruito da zero
P4 W11: Messaging completo      → multi-service, DLQ, circuit breaker + queue
```
> In AQ hai PROGETTATO messaging (W5). In SE lo IMPLEMENTI con TDD, progressivamente.

---

## 🏆 SISTEMA BOSS BATTLE

> **Filosofia:** Dopo ogni progetto, verifica autonoma per dimostrare che sai IMPLEMENTARE da solo.

### Cos'è
Una "prova finale" dove Dan implementa in **autonomia** un mini-progetto o feature. Claude è disponibile solo per domande "bloccanti", non per guida passo-passo.

### Struttura (Focus: 30% Design, 70% Code)

| Parte | Peso | Cosa Produci |
|-------|------|--------------|
| **A. Design** | 15% | Breve ADR + diagramma architettura |
| **B. Implementazione** | 50% | Codice funzionante con pattern richiesti |
| **C. Testing** | 25% | Unit tests + integration tests (TDD) |
| **D. Performance** | 10% | Benchmark che dimostra i requisiti |

### Criteri Valutazione (30 punti)

| Criterio | Punti | Cosa Valuto |
|----------|-------|-------------|
| **TDD Discipline** | 10 | Test-first, coverage, test quality |
| **Pattern Implementation** | 8 | Pattern applicati correttamente |
| **Code Quality** | 6 | Clean code, SOLID, no smell |
| **Performance** | 4 | Meets requirements (req/sec, latency) |
| **Completezza** | 2 | Tutti i requisiti implementati |

### Durata
1 settimana (più veloce rispetto ad Architect, focus su codice)

### XP & Achievement

| Risultato | XP | Achievement |
|-----------|-----|-------------|
| ≥24/30 (Superata) | +300 | ⚔️ **Code Warrior** |
| ≥28/30 (Con lode) | +500 | 🗡️ **Code Master** |
| Tutte e 6 superate | +1500 | 🏆 **Senior Champion** |

---

## ✅ PROGETTO 1: Task Manager API (Settimane 1-3)

### Obiettivo
REST API per gestire task con TDD, Redis caching, design patterns base.

### Stack
- .NET 8 Web API
- PostgreSQL
- Redis (caching)
- xUnit, FluentAssertions, NSubstitute

### Cosa Impari
- Clean Architecture in pratica
- TDD workflow (Red → Green → Refactor)
- Repository Pattern + UnitOfWork
- Factory Pattern
- Strategy Pattern
- Redis per caching
- CQRS con MediatR

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Repository** | Astrae l'accesso ai dati |
| **UnitOfWork** | Gestisce transazioni atomiche |
| **Factory** | Crea task con configurazioni diverse |
| **Strategy** | Algoritmi diversi di prioritizzazione |

### Settimane

**Week 1: Domain + Application Layer**
- Domain model con TDD (Entities, VO, Events)
- Repository Interfaces + IUnitOfWork
- MediatR setup
- Commands (Create, Update, Complete, Delete Task)
- Queries (GetById, GetAll, GetByStatus)
- DTOs + FluentValidation
- Behaviors (Validation, Logging)

**Week 2: Infrastructure + API Layer**
- Git workflow avanzato (rebase interattivo, bisect, cherry-pick) — mini-topic
- AppDbContext + Entity Configurations
- Repository implementations
- UnitOfWork implementation
- EF Core Migrations
- Controllers (Tasks, Projects, Tags)
- Exception handling middleware
- Serilog structured logging + correlation ID middleware
- Swagger/OpenAPI
- Integration tests (TestContainers)
- API tests (WebApplicationFactory)

**Week 3: Redis + Messaging Base + Patterns + Boss Battle**
- Redis caching setup
- Cache-aside pattern
- **Redis Pub/Sub + BackgroundService** (task scadute → evento → worker aggiorna status)
  - Rinforzo AQ W5: implementi messaging in-process da zero con TDD
  - Primo contatto con async processing nel percorso SE
- Factory Pattern (TaskFactory)
- Strategy Pattern (prioritization algorithms)
- Performance tests
- 80%+ test coverage
- Boss Battle: Note-Taking API

### Deliverables
- [ ] REST API CRUD completa
- [ ] 80%+ test coverage
- [ ] Redis caching funzionante
- [ ] Redis Pub/Sub + BackgroundService per task scadute
- [ ] 3 design patterns applicati
- [ ] Serilog structured logging
- [ ] EF Core migrations setup

### Testing Checklist ✅
- [ ] Unit tests (TDD) - 50+ tests
- [ ] Integration tests (TestContainers) - 5+ tests
- [ ] API tests (WebApplicationFactory) - 10+ tests

### 🎤 System Design Practice
Dopo P1, pratica spiegare **"Design a Task Management System"**:
- Functional: CRUD, prioritization, filtering, due dates
- Non-functional: 10K users, < 100ms latency
- Discussi: Caching strategy, database choice, API design

### 🏆 Boss Battle: "Note-Taking API"

**Scenario:** Implementa un'API per appunti con tagging e search (simile a Task Manager, pattern diversi).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per search strategy (DB vs Elasticsearch) |
| **B. Implementazione** | CRUD notes + tags + full-text search + Redis caching |
| **C. Testing** | 60+ tests (TDD), integration tests con TestContainers |
| **D. Performance** | Search < 50ms su 10K notes |

### 🤖 AI Feature: Smart Task Prioritization

> **Bonus:** Implementa DOPO aver completato i deliverables core

**Cosa fa:**
- Analizza task e suggerisce priorità automaticamente
- "Questa task sembra urgente perché contiene 'deadline'..."
- Categorizzazione automatica (work, personal, urgent)

**Implementazione:**
```csharp
// Aggiungi al TaskService
public async Task<PrioritySuggestion> SuggestPriorityAsync(TaskItem task)
{
    var prompt = $"Analyze this task and suggest priority (1-5): {task.Title} - {task.Description}";
    var response = await _ollamaClient.CompleteAsync(prompt);
    return ParsePrioritySuggestion(response);
}
```

**Cosa Impari:**
- Ollama integration base
- Prompt engineering semplice
- TDD su AI responses (mock LLM)

---

## 🔐 PROGETTO 1.5: Authentication & Security (Settimana 3)

> **Nuovo!** Colma il buco security. Rinforza Azure AD B2C di Architect con implementazione custom.

### Obiettivo
Implementare autenticazione JWT da zero. Capire cosa fa Azure AD B2C "under the hood".

### Stack
- .NET 8 Web API
- JWT Bearer Authentication
- BCrypt password hashing
- Refresh tokens in Redis

### Cosa Impari
- JWT structure (header, payload, signature)
- Access tokens vs Refresh tokens
- Password hashing (BCrypt, never SHA/MD5!)
- Secure cookie handling
- OWASP Top 10 awareness
- Rate limiting per login

### Settimana 3: Security Deep Dive

**Days 1-2: JWT From Scratch**
```csharp
// Capisci COME funziona JWT
public string GenerateToken(User user)
{
    var claims = new[]
    {
        new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()),
        new Claim(ClaimTypes.Email, user.Email),
        new Claim(ClaimTypes.Role, user.Role)
    };

    var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_config["Jwt:Secret"]));
    var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

    var token = new JwtSecurityToken(
        issuer: _config["Jwt:Issuer"],
        audience: _config["Jwt:Audience"],
        claims: claims,
        expires: DateTime.UtcNow.AddMinutes(15), // Short-lived!
        signingCredentials: credentials
    );

    return new JwtSecurityTokenHandler().WriteToken(token);
}
```

**Days 3-4: Refresh Tokens + Redis**
```csharp
// Refresh token in Redis con expiry
public async Task<string> CreateRefreshToken(Guid userId)
{
    var refreshToken = Convert.ToBase64String(RandomNumberGenerator.GetBytes(64));

    await _redis.SetStringAsync(
        $"refresh:{refreshToken}",
        userId.ToString(),
        new DistributedCacheEntryOptions
        {
            AbsoluteExpirationRelativeToNow = TimeSpan.FromDays(7)
        });

    return refreshToken;
}
```

**Day 5: OWASP Checklist**
- [ ] SQL Injection → Parameterized queries (EF Core OK)
- [ ] XSS → Input validation, output encoding
- [ ] CSRF → Anti-forgery tokens
- [ ] Broken Auth → Secure password policy
- [ ] Sensitive Data → HTTPS, no secrets in code
- [ ] Rate Limiting → Per IP/User

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Token Pattern** | Stateless authentication |
| **Decorator** | Aggiunge auth a qualsiasi handler |

### Deliverables
- [ ] JWT authentication funzionante
- [ ] Refresh token rotation
- [ ] Password hashing con BCrypt
- [ ] Rate limiting su login (5 tentativi/minuto)
- [ ] OWASP checklist completata
- [ ] 20+ security-focused tests

### Come Rinforza Architect
```
ARCHITECT P2: Azure AD B2C (managed)    SENIOR P1.5: JWT (custom)
─────────────────────────────────────────────────────────────
"Configura Azure AD B2C"          →    "Implementa JWT da zero"
"Usa token forniti"               →    "Genera e valida token"
"Managed refresh"                 →    "Scrivi refresh logic"

RISULTATO: Capisci COSA fa Azure AD B2C internamente
```

### 🏆 Boss Battle: "API Key Management"

**Scenario:** Implementa un sistema di API key per third-party access (complementa JWT per user auth).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per API key storage (hashed vs encrypted) |
| **B. Implementazione** | Generate, revoke, rotate API keys + rate limiting per key |
| **C. Testing** | Security tests (key leak, brute force protection) |
| **D. Performance** | Key validation < 5ms (Redis lookup) |

---

## 💬 PROGETTO 2: Real-Time Chat (Settimane 4-6)

> **Rinforza:** Architect P4 (FamilyBudget) SignalR/Real-time

### Obiettivo
Applicazione chat real-time scalabile a 1000+ utenti concorrenti.

### Stack
- .NET 8 + SignalR
- Redis (Pub/Sub, backplane)
- React + TypeScript
- SQL Server

### Cosa Impari
- SignalR per real-time
- Redis Pub/Sub
- Observer Pattern
- WebSocket scaling
- React + TypeScript frontend

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Observer** | Notifica subscribers di nuovi messaggi |
| **Pub/Sub** | Distribuzione messaggi tra server |
| **Circuit Breaker** | Gestisce fallimenti Redis/servizi esterni senza crash |
| **Retry + Backoff** | Riconnessione intelligente dopo failure temporanei |

### Settimane

**Week 4: SignalR Basics**
- Setup SignalR hub
- Basic chat functionality
- Message persistence

**Week 5: Redis + Scaling + Resilience + RabbitMQ**
- Redis backplane per scaling
- Redis Pub/Sub
- Presence (chi è online)
- **📨 RabbitMQ per notifiche offline** (~3-4 ore)
  - User offline → messaggio in RabbitMQ queue → email/push quando torna
  - Producer (ChatHub) + Consumer (NotificationWorker)
  - Rinforzo AQ W5: primo broker esterno nel percorso SE, implementato con TDD
  - Confronto pratico: Redis Pub/Sub (P1 W3) vs RabbitMQ (qui) — quando usare quale
- **🛡️ Resilience Patterns con Polly** (mini-topic, ~2-3 ore)
  - Circuit Breaker: Redis va giu → il chat degrada, non crasha
  - Retry with exponential backoff: connessione persa → riprova intelligentemente
  - Timeout policy: nessuna operazione blocca per sempre
  - Perche qui: stai scalando un sistema real-time, i failure sono inevitabili. Meglio impararlo su un progetto dove li VEDI succedere

**Week 6: Frontend + Polish**
- React + TypeScript frontend
- UI completa
- Load testing 1000+ users

### Deliverables
- [ ] Chat funzionante real-time
- [ ] Scala a 1000+ utenti
- [ ] Frontend React completo
- [ ] Redis Pub/Sub implementato
- [ ] RabbitMQ per notifiche offline

### Testing Checklist ✅
- [ ] Unit tests - Hub logic
- [ ] Integration tests - SignalR connections (TestServer)
- [ ] Load test - 1000 concurrent connections (k6/NBomber)

### 🎤 System Design Practice
Dopo P2, pratica spiegare **"Design a Real-Time Chat System"**:
- Functional: 1:1 chat, group chat, presence, message history
- Non-functional: 1000+ concurrent users, < 100ms delivery latency
- Discussi: WebSocket vs polling, Redis backplane, message ordering, horizontal scaling

### 🏆 Boss Battle: "Live Notification Feed"

**Scenario:** Implementa un feed di notifiche real-time (simile a chat, focus su broadcast).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per notification fanout strategy |
| **B. Implementazione** | SignalR hub + Redis Pub/Sub + notification types + read/unread |
| **C. Testing** | Load test 500 concurrent connections |
| **D. Performance** | Notification delivery < 100ms to all subscribers |

### 🤖 AI Feature: Message Summarization

> **Bonus:** Implementa DOPO aver completato i deliverables core

**Cosa fa:**
- Riassume conversazioni lunghe per chi entra tardi
- "Catch up" button: "Negli ultimi 50 messaggi si è parlato di..."
- Highlight messaggi importanti automaticamente

**Implementazione:**
```csharp
// Aggiungi al ChatService
public async Task<string> SummarizeConversationAsync(List<Message> messages)
{
    var conversation = string.Join("\n", messages.Select(m => $"{m.Author}: {m.Text}"));
    var prompt = $"Summarize this conversation in 2-3 bullet points:\n{conversation}";

    // Streaming response per UX migliore
    await foreach (var chunk in _claudeClient.StreamAsync(prompt))
    {
        await _hubContext.Clients.Caller.SendAsync("SummaryChunk", chunk);
    }
}
```

**Cosa Impari:**
- Streaming responses
- Chunking conversazioni lunghe
- Context window management

---

## 🛒 PROGETTO 3: E-Commerce Cart & Inventory (Settimane 7-10)

> **Rinforza:** Architect P2 (NutriPlan) CQRS, Event Sourcing

### Obiettivo
Sistema carrello e inventario con CQRS, Event Sourcing, gestione concorrenza.

### Stack
- .NET 8 + MediatR
- EventStore o Marten
- Redis (distributed locks)
- SQL Server (read models)

### Cosa Impari
- CQRS (Command Query Responsibility Segregation)
- Event Sourcing
- Saga Pattern (base)
- Distributed locking con Redis
- Concurrency handling

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Command** | Separa richieste da esecuzione |
| **CQRS** | Ottimizza read e write separatamente |
| **Event Sourcing** | Audit trail completo, rebuild state |
| **Saga** | Transazioni distribuite |

### Settimane

**Week 7: CQRS Basics**
- MediatR setup
- Commands e Queries separati
- Read/Write models

**Week 8: Event Sourcing**
- Event store setup
- Cart aggregate con eventi
- Event replay

**Week 9: Concurrency + Inventory + DB Design**
- Redis distributed locks
- Inventory management
- Optimistic concurrency
- **Query optimization & database design** (indexing, query plans, N+1 prevention)

**Week 10: Saga + Outbox Pattern + Polish**
- Checkout saga
- **📨 Outbox Pattern implementato da zero con TDD**
  - OrderPlaced → OutboxMessage → RabbitMQ → InventoryService, PaymentService
  - Rinforzo AQ W5: in AQ l'hai progettato, qui lo costruisci tu da solo
  - Event Sourcing + Outbox = eventi dal domain store pubblicati sulla queue
- Integration tests
- Load testing

### Deliverables
- [ ] CQRS funzionante
- [ ] Event Sourcing con replay
- [ ] Distributed locking
- [ ] Saga per checkout
- [ ] Outbox Pattern implementato con TDD

### Testing Checklist ✅
- [ ] Unit tests - Aggregates, Commands, Queries
- [ ] Integration tests - Event Store persistence
- [ ] Concurrency tests - Distributed locks
- [ ] E2E test - Full checkout flow

### 🎤 System Design Practice
Dopo P3, pratica spiegare **"Design an E-Commerce Cart & Inventory System"**:
- Functional: Add to cart, checkout, inventory tracking, order history
- Non-functional: 100K products, handle flash sales (10K concurrent), eventual consistency OK
- Discussi: CQRS trade-offs, Event Sourcing for audit, distributed locks for inventory, saga pattern for checkout

### 🏆 Boss Battle: "Auction System"

**Scenario:** Implementa un sistema di aste con bidding (CQRS + Event Sourcing + concurrency).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per bid conflict resolution |
| **B. Implementazione** | Auction aggregate, Bid events, auto-close, winner selection |
| **C. Testing** | Concurrency tests (100 bids simultanei su stessa auction) |
| **D. Performance** | Bid processing < 50ms, no lost bids |

### 🤖 AI Feature: Product Recommendations

> **Bonus:** Implementa DOPO aver completato i deliverables core

**Cosa fa:**
- "Chi ha comprato X ha comprato anche Y"
- Recommendations basate su embeddings prodotti
- "Prodotti simili" usando similarity search

**Implementazione:**
```csharp
// ProductRecommendationService
public async Task<List<Product>> GetSimilarProductsAsync(Guid productId)
{
    var product = await _productRepo.GetByIdAsync(productId);

    // 1. Get embedding del prodotto (cached)
    var embedding = await _embeddingService.GetOrCreateAsync(product);

    // 2. Similarity search
    var similarIds = await _vectorDb.SearchSimilarAsync(embedding, limit: 5);

    // 3. Fetch products
    return await _productRepo.GetByIdsAsync(similarIds);
}
```

**Cosa Impari:**
- Embeddings per prodotti (testo → vettore)
- Similarity search con vector DB
- Caching embeddings per performance

---

## 🚨 PROGETTO 4: Alert Gateway (Settimane 11-13) ← RINOMINATO

> **Rinforza:** Architect P3 (BookingHub) Microservices, Saga, Resilience
> **Nota:** Rinominato da "Notification Service" per evitare confusione con Architect P1

### Obiettivo
Sistema di alerting multi-canale con microservices, message queue, circuit breaker.
Focus su **resilience patterns** e **service communication**.

### Stack
- .NET 8 (multiple services)
- RabbitMQ
- Redis (queues, health tracking)
- Hangfire (background jobs)
- YARP (API Gateway)
- Polly (resilience)

### Cosa Impari
- Microservices architecture
- Message queuing
- Circuit Breaker pattern
- API Gateway
- Background jobs
- Health checks & readiness probes

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Circuit Breaker** | Gestisce fallimenti di servizi esterni |
| **Retry with Backoff** | Resilienza temporanea con exponential backoff |
| **Bulkhead** | Isola fallimenti per evitare cascading |
| **API Gateway** | Single entry point, routing |

### Settimane

**Week 11: Service Decomposition + Messaging Completo**
- Identificare bounded contexts
- Setup 3 services: Gateway, Processor, Sender
- RabbitMQ communication tra servizi (Exchange types, routing)
- **📨 Messaging inter-service completo con TDD**
  - Outbox Pattern per ogni servizio (consistenza cross-service)
  - Dead Letter Queue (DLQ applicativa + DLQ RabbitMQ per confronto)
  - Retry con DeliveryAttempts + backoff controllato
  - Il "boss finale" del messaging: tutto quello imparato in P1-P3 applicato a multi-service
- Docker Compose per local dev

**Week 12: Resilience Patterns**
- Circuit Breaker con Polly
- Retry policies con exponential backoff
- Fallback strategies
- Bulkhead pattern
- Integrazione resilience + messaging (Circuit Breaker su RabbitMQ connection)

**Week 13: Gateway + Observability**
- YARP API Gateway
- Health checks per ogni service (readiness + liveness probes)
- Structured logging cross-service (Serilog + correlation ID)
- **Basic observability:** health check endpoints, structured logs, correlation ID propagation
- End-to-end testing

### Deliverables
- [ ] 3+ microservices comunicanti
- [ ] RabbitMQ message queue
- [ ] Circuit breaker + retry + bulkhead
- [ ] API Gateway con routing
- [ ] Health checks su tutti i servizi
- [ ] Correlation ID per distributed tracing

### Testing Checklist ✅
- [ ] Unit tests - Each service isolated
- [ ] Integration tests - RabbitMQ messaging
- [ ] Resilience tests - Chaos testing (service down)
- [ ] E2E test - Full alert flow through gateway

### Differenza da Architect P1 (Notification Service)
```
ARCHITECT P1                          SENIOR P4 (Alert Gateway)
─────────────────────────────────────────────────────────────────
Focus: Clean Architecture             Focus: Microservices
Focus: Event-driven design            Focus: Resilience patterns
Focus: Single deployable              Focus: Multiple services
Output: ADR, C4, documentation        Output: Working distributed system
```

### 🎤 System Design Practice
Dopo P4, pratica spiegare **"Design an Alert/Notification Gateway"**:
- Functional: Multi-channel alerts (email, SMS, push), priority levels, retry logic
- Non-functional: 10K alerts/min, 99.9% delivery, graceful degradation
- Discussi: Circuit breaker pattern, message queue (RabbitMQ vs Kafka), API Gateway, bulkhead isolation, correlation IDs

### 🏆 Boss Battle: "Health Check Dashboard"

**Scenario:** Implementa un servizio di health monitoring per microservices (resilience patterns).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per health check aggregation strategy |
| **B. Implementazione** | Health collector service + Circuit breaker + alerting on degradation |
| **C. Testing** | Chaos tests (simula service down, verifica alerting) |
| **D. Performance** | Health check round-trip < 500ms per 10 services |

### 🤖 AI Feature: Alert Triage & Grouping

> **Bonus:** Implementa DOPO aver completato i deliverables core

**Cosa fa:**
- Classifica automaticamente severità alert
- Raggruppa alert correlati ("questi 5 alert sono lo stesso problema")
- Suggerisce root cause: "Probabilmente è un problema di rete"

**Implementazione:**
```csharp
// AlertTriageService
public async Task<TriageResult> TriageAlertAsync(Alert alert)
{
    // 1. Classify severity
    var severity = await _classifier.ClassifyAsync(alert.Message,
        categories: ["critical", "warning", "info"]);

    // 2. Find related alerts (semantic similarity)
    var relatedAlerts = await _alertRepo.FindSimilarAsync(alert, timeWindow: TimeSpan.FromHours(1));

    // 3. Suggest root cause if pattern detected
    if (relatedAlerts.Count > 3)
    {
        var rootCause = await _aiService.AnalyzePatternAsync(relatedAlerts);
        return new TriageResult(severity, relatedAlerts, rootCause);
    }

    return new TriageResult(severity, relatedAlerts);
}
```

**Cosa Impari:**
- Classification con LLM
- Semantic deduplication
- Pattern analysis con AI

---

## 🔗 PROGETTO 5: URL Shortener with Analytics (Settimane 14-16)

> **Culmina:** Tutto il Redis imparato in P1, P2, P3, P4 → ora PRIMARY DATABASE

### Obiettivo
Sistema high-performance con Redis come database primario. Target: 1000+ req/sec.

### Stack
- .NET 8 Minimal APIs
- Redis (PRIMARY database!)
- Redis Streams (analytics)
- HyperLogLog, Bloom filters

### Cosa Impari
- Redis come database primario
- Redis data structures avanzate
- High-performance design
- Minimal APIs
- Analytics real-time

### Redis Avanzato

| Struttura | Uso |
|-----------|-----|
| **Strings** | URL mappings |
| **HyperLogLog** | Unique visitors (probabilistico) |
| **Bloom Filter** | Check esistenza URL |
| **Streams** | Event log per analytics |
| **Sorted Sets** | Leaderboard URL popolari |

### Settimane

**Week 14: Core + Redis**
- Minimal API setup
- Redis come primary store
- URL shortening logic
- Base62 encoding

**Week 15: Analytics**
- Redis Streams per eventi
- HyperLogLog per unique visitors
- Real-time analytics dashboard
- Sorted Sets per leaderboard

**Week 16: Performance**
- Load testing con k6/NBomber
- Optimization (connection pooling, pipelining)
- Target 1000+ req/sec
- Redis persistence strategies (RDB vs AOF)

### Deliverables
- [ ] URL shortener funzionante
- [ ] Redis come primary DB (no SQL!)
- [ ] Analytics real-time con HyperLogLog
- [ ] 1000+ req/sec verified

### Testing Checklist ✅
- [ ] Unit tests - Shortening logic, Base62
- [ ] Integration tests - Redis operations
- [ ] Performance tests - 1000+ req/sec benchmark
- [ ] Analytics accuracy tests - HyperLogLog error margin

### 🎤 System Design Practice
Dopo P5, pratica spiegare **"Design a URL Shortener with Analytics"**:
- Functional: Shorten URL, redirect, click analytics, custom aliases
- Non-functional: 1000+ req/sec read, 100M URLs stored, real-time analytics
- Discussi: Base62 encoding, Redis as primary DB, HyperLogLog for unique visitors, read-heavy optimization, caching strategy

### 🏆 Boss Battle: "Feature Flags Service"

**Scenario:** Implementa un servizio di feature flags con targeting (Redis as primary DB + analytics).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per flag evaluation strategy (user targeting, % rollout) |
| **B. Implementazione** | Flag CRUD + user targeting + analytics (who saw what) |
| **C. Testing** | Performance tests per flag evaluation |
| **D. Performance** | Flag evaluation < 5ms, 2000+ req/sec |

### 🤖 AI Feature: Smart Link Preview Generator

> **Bonus:** Implementa DOPO aver completato i deliverables core

**Cosa fa:**
- Genera titolo e descrizione SEO-friendly per link
- Preview card automatica (come Twitter/LinkedIn)
- Categorizzazione automatica link

**Implementazione:**
```csharp
// LinkPreviewService
public async Task<LinkPreview> GeneratePreviewAsync(string url)
{
    // 1. Fetch page content
    var html = await _httpClient.GetStringAsync(url);
    var text = ExtractMainContent(html);

    // 2. Generate preview with AI
    var prompt = $"""
        Generate a link preview for this content:
        {text.Truncate(2000)}

        Return JSON: {{"title": "...", "description": "...", "category": "..."}}
        """;

    var preview = await _ollamaClient.CompleteAsync<LinkPreview>(prompt);

    // 3. Cache in Redis
    await _redis.SetAsync($"preview:{url.ToShortHash()}", preview, TimeSpan.FromDays(7));

    return preview;
}
```

**Cosa Impari:**
- Web scraping + content extraction
- JSON mode / structured output
- Caching AI responses

### Progressione Redis nel Percorso
```
P1 (Task Manager):     Redis = Cache
P1.5 (Auth):           Redis = Refresh Token Store
P2 (Chat):             Redis = Pub/Sub Backplane
P3 (E-commerce):       Redis = Distributed Locks
P4 (Alert Gateway):    Redis = Queue + Health
P5 (URL Shortener):    Redis = PRIMARY DATABASE 🎯
```

---

## 🧠 PROGETTO 6: Capstone - AI Second Brain (Mesi 6-16)

> **Unisce:** Ex-P6 Academic Knowledge Hub + Ex-AI-1 (AI Second Brain da Architect Quest)
> **Tipo:** Capstone AI-powered - Il tuo Obsidian vault diventa queryabile con AI

### Obiettivo
Sistema RAG sul tuo Obsidian vault che integra TUTTI i pattern Senior + AI skills.
Il tuo "secondo cervello" che risponde a domande sulle TUE note.

### Stack
- .NET 8 Minimal API (backend)
- React + TypeScript (web UI)
- Qdrant o ChromaDB (vector DB)
- Ollama embeddings (locale) + Claude per query complesse
- Redis (caching embeddings, session)
- PostgreSQL (metadata, history)
- SignalR (real-time quiz mode)
- Docker multi-service

### Cosa Impari (Consolidamento di TUTTO)
- **RAG completo** (chunking, embeddings, retrieval, generation)
- **Vector databases** (similarity search, indexing)
- **CQRS** (write = index notes, read = semantic search)
- **Redis** (cache embeddings, cache risposte frequenti)
- **SignalR** (quiz real-time)
- **Microservices** (indexer service + query service + quiz service)
- **TDD** su AI responses (mock LLM)
- **Docker** multi-container deployment

### Features
- Semantic search sulle TUE note Obsidian
- Q&A con contesto (RAG)
- Quiz auto-generation dalle note
- "Related notes" suggestions
- Study progress tracking
- CLI o Obsidian plugin

### Fasi

**Mesi 6-8: RAG Foundation**
- Vector DB setup, embedding pipeline
- Chunking strategies, Obsidian vault indexing
- Retrieval + basic Q&A
- Prompt optimization, context window management

**Mesi 9-11: Advanced Features**
- Quiz generation dalle note
- "Related notes" suggestions
- CQRS per index/query separation
- Redis caching layer

**Mesi 12-14: Multi-Service + Real-time**
- Service decomposition (indexer, query, quiz)
- SignalR per quiz real-time
- Docker Compose setup

**Mesi 15-16: Production + Polish**
- Performance optimization
- CLI o Obsidian plugin
- Documentation, testing
- Boss Battle

### 🏆 Boss Battle: "Documentation Q&A + Open Source"

**Scenario:** Estendi Second Brain per queryare documentazione tecnica esterna + contribuisci a un progetto OSS.

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per chunking strategy docs tecniche, C4 Container |
| **B. Implementazione** | Web scraper + indexer per docs esterne (Microsoft Docs, MDN) |
| **C. Testing** | Query performance < 3 sec su documento 50 pagine |
| **D. Open Source** | PR merged su progetto OSS reale (anche piccolo fix) |

**Reward speciale:** +500 XP (Capstone completato) + achievement 🌍 **Open Source Contributor**

### AI Skills dimostrate nel Capstone
```
CAPSTONE = AI Second Brain
────────────────────────────────────────
✅ RAG (query your notes)
✅ Embeddings (semantic search)
✅ Vector DB (Qdrant/ChromaDB)
✅ Classification (categorize questions)
✅ Generation (quiz, explanations)
✅ Prompt engineering avanzato
✅ Tutti i pattern Senior (TDD, CQRS, Redis, Docker, SignalR)
```

---

## Career Boost Module

> Estratto in file separato: `roadmaps/career-boost.md`
> Contiene: System Design Practice, Communication Skills, API Mastery, Interview Prep, XP e Achievement.

---

## 📚 Libri Chiave

1. **"Clean Architecture"** - Martin
2. **"Test-Driven Development"** - Beck
3. **"Designing Data-Intensive Applications"** - Kleppmann
4. **"Building Microservices"** - Newman
5. **"Redis in Action"** - Carlson
6. **"System Design Interview"** - Alex Xu 🆕 (MUST per interviews)

---

## 🎨 Design Patterns Completi

### Creational
- [ ] Factory, Abstract Factory
- [ ] Builder
- [ ] Singleton (via DI)

### Structural
- [ ] Adapter
- [ ] Decorator
- [ ] Facade
- [ ] Proxy

### Behavioral
- [ ] Strategy
- [ ] Observer
- [ ] Command
- [ ] Chain of Responsibility
- [ ] Template Method
- [ ] Mediator
- [ ] State

### Architectural
- [ ] Repository
- [ ] Unit of Work
- [ ] Specification
- [ ] Saga
- [ ] Circuit Breaker
- [ ] API Gateway

---

## 🎯 Competenze Finali

### Core Skills
- [ ] TDD rigoroso (test-first mindset)
- [ ] Tutti i design patterns (sapere QUANDO usarli)
- [ ] Redis expert (cache → pub/sub → locks → primary DB)
- [ ] CQRS + Event Sourcing

### Architecture
- [ ] Microservices architecture
- [ ] Resilience patterns (Circuit Breaker, Retry, Bulkhead)
- [ ] Real-time (SignalR)
- [ ] API Gateway

### Security 🔐 (NUOVO)
- [ ] JWT authentication from scratch
- [ ] Refresh token rotation
- [ ] OWASP Top 10 awareness
- [ ] Rate limiting

### Testing 🧪 (ESPLICITO)
- [ ] Unit testing (TDD)
- [ ] Integration testing (TestContainers)
- [ ] E2E testing
- [ ] Load/Performance testing (k6, NBomber)

### DevOps
- [ ] Docker multi-service
- [ ] Kubernetes deployment
- [ ] Health checks & readiness probes

### Portfolio
- [ ] 6+ progetti completi
- [ ] Pronto per interview senior
- [ ] Target: €90k-130k remote

---

## Riepilogo Miglioramenti

| Versione | Miglioramento |
|----------|---------------|
| v3.0 | P1.5 Auth, P4 rinominato, Testing Checklist, Resilience Patterns, Redis Progression, Career Boost, Boss Battles, AI Features |
| v4.0 | P6 unito con AI Second Brain (RAG), Career Boost estratto in file separato, Timeline realistica (30-36 mesi) |

### AI Features per Progetto
| Progetto | AI Feature | Skill AI |
|----------|------------|----------|
| P1 Task Manager | Smart Prioritization | Ollama base, prompt engineering |
| P2 Chat | Message Summarization | Streaming, chunking |
| P3 E-commerce | Product Recommendations | Embeddings, vector similarity |
| P4 Alert Gateway | Alert Triage & Grouping | Classification, pattern analysis |
| P5 URL Shortener | Link Preview Generator | Web scraping, structured output |
| P6 AI Second Brain | RAG + Quiz + Semantic Search | RAG completo, vector DB, embeddings |

---

*Ultimo aggiornamento: 2026-03-24 (refactor — target aggiornato con AI Engineer)*
*Versione: 4.1*