# 💻 Roadmap Completa: Senior Engineer Path

> Percorso 18 mesi da mid-level a senior engineer internazionale

## 🎯 Obiettivo Finale

- Padroneggiare TDD e design patterns (sapere QUANDO usarli)
- Essere esperto Redis (da caching a primary DB)
- Implementare CQRS e Event Sourcing
- Avere portfolio pronto per aziende internazionali
- **Superare system design interviews** 🎤
- **Comunicare efficacemente in team remoti** 🌍
- **Target:** Ruolo senior €90k-130k remote

---

## 📅 Timeline Overview

```
Settimane 1-2:   P1 - Task Manager (Clean Arch, TDD, Redis basics)
Settimana 3:     P1.5 - Auth & Security 🔐 (JWT, OWASP basics)
Settimane 4-6:   P2 - Chat App (SignalR, Redis Pub/Sub)
Settimane 7-10:  P3 - E-commerce Cart (CQRS, Event Sourcing)
Settimane 11-13: P4 - Alert Gateway (Microservices, Circuit Breaker) ← RINOMINATO
Settimane 14-16: P5 - URL Shortener (Redis as Primary DB)
Mesi 6-16:       P6 - Capstone: Academic Knowledge Hub
Mesi 17-18:      Job Search + Portfolio
```

### 🔄 Rinforzo con Architect Quest
```
Senior P1 (Task Manager)     ←→  Architect P1 (Notification) = Clean Arch
Senior P1.5 (Auth)           ←→  Architect P2 (Azure AD B2C) = Auth patterns
Senior P3 (E-commerce)       ←→  Architect P2 (NutriPlan) = CQRS, Event Sourcing
Senior P4 (Alert Gateway)    ←→  Architect P3 (BookingHub) = Microservices, Saga
Senior P2 (Chat)             ←→  Architect P4 (FamilyBudget) = Real-time, SignalR
```

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

## ✅ PROGETTO 1: Task Manager API (Settimane 1-2)

### Obiettivo
REST API per gestire task con TDD, Redis caching, design patterns base.

### Stack
- .NET 8 Web API
- SQL Server
- Redis (caching)
- xUnit, FluentAssertions, Moq

### Cosa Impari
- Clean Architecture in pratica
- TDD workflow (Red → Green → Refactor)
- Repository Pattern
- Factory Pattern
- Strategy Pattern
- Redis per caching

### Design Patterns Introdotti

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Repository** | Astrae l'accesso ai dati |
| **Factory** | Crea task con configurazioni diverse |
| **Strategy** | Algoritmi diversi di prioritizzazione |

### Settimane

**Week 1: Setup + TDD**
- Setup struttura Clean Architecture
- TDD basics: Red → Green → Refactor
- Domain model con TDD (TaskItem entity)
- Repository Pattern

**Week 2: API + Redis + Patterns**
- CRUD API endpoints
- Redis caching
- Factory Pattern
- Strategy Pattern per prioritizzazione

### Deliverables
- [ ] REST API CRUD completa
- [ ] 80%+ test coverage
- [ ] Redis caching funzionante
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

### Settimane

**Week 4: SignalR Basics**
- Setup SignalR hub
- Basic chat functionality
- Message persistence

**Week 5: Redis + Scaling**
- Redis backplane per scaling
- Redis Pub/Sub
- Presence (chi è online)

**Week 6: Frontend + Polish**
- React + TypeScript frontend
- UI completa
- Load testing 1000+ users

### Deliverables
- [ ] Chat funzionante real-time
- [ ] Scala a 1000+ utenti
- [ ] Frontend React completo
- [ ] Redis Pub/Sub implementato

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

**Week 9: Concurrency + Inventory**
- Redis distributed locks
- Inventory management
- Optimistic concurrency

**Week 10: Saga + Polish**
- Checkout saga
- Integration tests
- Load testing

### Deliverables
- [ ] CQRS funzionante
- [ ] Event Sourcing con replay
- [ ] Distributed locking
- [ ] Saga per checkout

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

**Week 11: Service Decomposition**
- Identificare bounded contexts
- Setup 3 services: Gateway, Processor, Sender
- RabbitMQ communication
- Docker Compose per local dev

**Week 12: Resilience Patterns**
- Circuit Breaker con Polly
- Retry policies con exponential backoff
- Fallback strategies
- Bulkhead pattern

**Week 13: Gateway + Observability**
- YARP API Gateway
- Health checks per ogni service
- Structured logging cross-service (correlation ID)
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

## 🎓 PROGETTO 6: Capstone - Academic Knowledge Hub (Mesi 6-16)

### Obiettivo
Piattaforma educativa enterprise-level che integra TUTTO quello imparato.

### Stack
Tutto: .NET 8, React, Redis, SQL Server, SignalR, Kubernetes, etc.

### Features
- User management + authentication
- Course management con CQRS
- Real-time collaboration (SignalR)
- Note versioning (Event Sourcing)
- Full-text search (Elasticsearch)
- Microservices architecture
- Kubernetes deployment
- Full observability

### Fasi

**Mesi 6-8: Foundation**
- Clean Architecture setup
- User management
- Course CRUD

**Mesi 9-11: Advanced Features**
- CQRS per courses
- Event Sourcing per notes
- Real-time collaboration

**Mesi 12-14: Microservices**
- Service decomposition
- Message queuing
- API Gateway

**Mesi 15-16: Production**
- Kubernetes deployment
- Observability
- Performance optimization

### 🏆 Boss Battle: "Open Source Contribution"

**Scenario:** Il Capstone È la Boss Battle! Ma aggiungi: contribuisci a un progetto OSS reale.

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | Proponi una feature/fix per progetto OSS (RFC/Issue) |
| **B. Implementazione** | PR merged su progetto OSS (anche piccolo fix) |
| **C. Testing** | Tests per la tua contribution |
| **D. Documentation** | README del tuo Capstone pronto per portfolio |

**Reward speciale:** +500 XP (Capstone completato) + achievement 🌍 **Open Source Contributor**

### 🤖 AI Feature: Full AI Study Assistant

> **Obbligatorio nel Capstone:** Il progetto finale è AI-powered!

**Cosa fa:**
- Quiz generation dalle note del corso
- Concept explanation personalizzata
- "Non ho capito X" → spiegazione adattata al tuo livello
- Study plan suggestions
- Progress-based recommendations

**Il Capstone diventa la dimostrazione di TUTTE le AI skills:**
```
CAPSTONE = Academic Knowledge Hub + AI
────────────────────────────────────────
✅ RAG (query course materials)
✅ Embeddings (semantic search notes)
✅ Classification (categorize questions)
✅ Generation (quiz, explanations)
✅ Personalization (adapt to user level)
✅ Evaluation (grade quiz answers)
```

---

## 🚀 CAREER BOOST MODULE (Parallelo, Mesi 3-18)

> **Nuovo!** Modulo trasversale per passare da "bravo developer" a "hired senior"

### 🎤 System Design Practice (Mesi 3-12)

**Obiettivo:** Saper spiegare e progettare sistemi "on the whiteboard"

**Cadenza:** 1 system design / settimana (30-45 min)

#### System Design Topics

| # | Topic | Progetto Collegato | Quando |
|---|-------|-------------------|--------|
| 1 | URL Shortener | Senior P5 | Mese 3 |
| 2 | Rate Limiter | Senior P1.5 | Mese 3 |
| 3 | Chat System | Senior P2 | Mese 4 |
| 4 | Notification System | Architect P1 | Mese 5 |
| 5 | E-commerce Cart | Senior P3 | Mese 6 |
| 6 | Booking System | Architect P3 | Mese 7 |
| 7 | Social Feed | 🆕 Standalone | Mese 8 |
| 8 | Search Autocomplete | 🆕 Standalone | Mese 9 |
| 9 | Distributed Cache | Senior P5 (Redis) | Mese 10 |
| 10 | Video Streaming | 🆕 Standalone | Mese 11 |
| 11 | Payment System | Senior P3 | Mese 12 |
| 12 | Ride Sharing (Uber) | 🆕 Standalone | Mese 12 |

#### System Design Template

Per ogni design, documenta:
```markdown
# System Design: [Nome]

## 1. Requirements (5 min)
### Functional
- User can...
- System should...

### Non-Functional
- Scale: X users, Y requests/sec
- Latency: < X ms
- Availability: 99.X%

## 2. Capacity Estimation (5 min)
- Storage: X GB/year
- Bandwidth: X MB/s
- Servers: ~X instances

## 3. High-Level Design (10 min)
[Diagramma ASCII o draw.io]

## 4. Deep Dive (15 min)
- Database schema
- API design
- Key algorithms

## 5. Trade-offs Discussed
- SQL vs NoSQL: chose X because...
- Caching strategy: X because...

## 6. Bottlenecks & Solutions
- Bottleneck: X → Solution: Y
```

#### XP System Design
| Attività | XP |
|----------|-----|
| Design documentato | +25 |
| Mock interview (con peer/Claude) | +50 |
| Design presentato in < 45 min | +30 |

---

### 🗣️ Communication Skills (Ongoing)

**Obiettivo:** Comunicare efficacemente in team remoti internazionali

#### Code Review Best Practices

```markdown
## Quando fai review:
✅ "Consider using X because Y" (suggerimento con motivo)
✅ "I don't understand this part, could you explain?" (chiedere)
✅ "Nice approach! I learned something" (positivo)
❌ "This is wrong" (no contesto)
❌ "Why didn't you do X?" (accusatorio)

## Quando ricevi review:
✅ "Good point, I'll change it"
✅ "I chose this because X, but your suggestion is better"
✅ Chiedere chiarimenti se non capisci
❌ Difendere il codice senza ascoltare
```

#### Technical Writing Templates

| Documento | Quando | Template |
|-----------|--------|----------|
| **RFC (Request for Comments)** | Proporre cambio significativo | Problem → Proposal → Alternatives → Decision |
| **ADR** | Decisione architetturale | ✅ Già coperto in Architect |
| **Post-mortem** | Dopo incident | What happened → Impact → Root cause → Action items |
| **Tech Spec** | Prima di feature grande | Context → Goals → Design → Milestones |

#### English Technical Vocabulary

Crea flashcard per questi termini:
```
Scalability, Throughput, Latency, Availability
Trade-off, Bottleneck, Single point of failure
Eventual consistency, Strong consistency
Sharding, Replication, Partitioning
Circuit breaker, Bulkhead, Retry
Idempotent, Stateless, Immutable
```

#### Async Communication Best Practices

```markdown
## Slack/Teams Messages
✅ Fornisci contesto completo (non "hi, can I ask you something?")
✅ Includi: What I tried → What happened → What I need
✅ Usa thread per discussioni
✅ Rispetta timezone (no urgenza finta)

## Written Updates
✅ Bullet points > wall of text
✅ Lead with conclusion
✅ Link a docs/PRs rilevanti
```

---

### 📄 API Mastery (Mese 4-5)

**Obiettivo:** Progettare API che altri developer AMANO usare

#### OpenAPI Spec Practice

Ogni progetto deve avere OpenAPI spec completa:
```yaml
openapi: 3.0.0
info:
  title: Task Manager API
  version: 1.0.0
paths:
  /tasks:
    get:
      summary: List all tasks
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, completed, all]
      responses:
        '200':
          description: List of tasks
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'
```

#### API Versioning Strategy

```
Option A: URL versioning     → /api/v1/tasks, /api/v2/tasks
Option B: Header versioning  → Accept: application/vnd.api+json;version=1
Option C: Query param        → /api/tasks?version=1

Raccomandato per REST: URL versioning (più esplicito)
```

#### API Design Checklist

- [ ] Nomi risorse plurali (`/tasks`, non `/task`)
- [ ] HTTP verbs corretti (GET=read, POST=create, PUT=replace, PATCH=update, DELETE=remove)
- [ ] Status codes appropriati (201 Created, 204 No Content, 404 Not Found, 422 Unprocessable)
- [ ] Pagination per liste (`?page=1&limit=20`)
- [ ] Filtering/Sorting (`?status=pending&sort=-createdAt`)
- [ ] Error response consistente (`{ "error": { "code": "...", "message": "..." } }`)
- [ ] Versioning strategy definita
- [ ] Rate limiting headers (`X-RateLimit-Remaining`)

---

### 🎯 Interview Prep (Mesi 15-18)

**Obiettivo:** Passare interview per ruoli €90k-130k

#### Behavioral Questions (STAR Method)

Prepara 5+ storie con questo formato:
```
Situation: Descrivi il contesto
Task: Qual era il tuo compito/obiettivo
Action: Cosa HAI FATTO tu specificamente
Result: Qual è stato il risultato (numeri se possibile)
```

**Domande comuni:**
1. "Tell me about a challenging technical problem you solved"
2. "Describe a time you disagreed with a teammate"
3. "Tell me about a project you're proud of"
4. "Describe a time you had to learn something quickly"
5. "Tell me about a failure and what you learned"

#### Technical Questions Bank

**Domande frequenti senior .NET:**
- Explain dependency injection and its benefits
- What's the difference between IEnumerable and IQueryable?
- How does async/await work under the hood?
- Explain the difference between SQL and NoSQL databases
- What is CQRS and when would you use it?
- Explain the CAP theorem
- How would you handle distributed transactions?
- What's the difference between optimistic and pessimistic locking?

#### "Walk Me Through Your Project" Template

```markdown
1. **Context** (30 sec)
   "I built a [type] system that [does what] for [who]"

2. **Architecture** (1 min)
   "It uses [stack]. Here's the high-level design..."
   [Disegna diagramma semplice]

3. **Interesting Challenge** (2 min)
   "The most interesting problem was [X]. I solved it by [Y]"

4. **Results** (30 sec)
   "It handles [X] requests/sec with [Y] latency"

5. **What I'd Do Differently** (30 sec)
   "If I rebuilt it, I'd [improvement]"
```

#### Salary Negotiation Basics

```markdown
## Research
- Glassdoor, Levels.fyi, Blind per range
- Considera: base + bonus + equity + benefits

## Quando chiedono "What's your expected salary?"
✅ "Based on my research, roles like this in [location] range €X-Y.
    I'm flexible depending on the total package."
❌ Mai dire il primo numero se possibile
❌ Mai dire il tuo stipendio attuale

## Dopo l'offerta
✅ "Thank you! I'm excited about this opportunity.
    I was hoping for something closer to €X. Is there flexibility?"
✅ Sempre chiedere (gentilmente). Il peggio è "no".
```

#### Portfolio Presentation

- [ ] GitHub profile curato (README, pinned repos)
- [ ] Ogni progetto ha README con: What, Why, How, Demo
- [ ] LinkedIn aggiornato (headline: "Senior .NET Engineer | ...")
- [ ] 1-page resume (no more!)
- [ ] Personal website/blog (opzionale ma utile)

---

### 📊 Career Boost XP

| Attività | XP |
|----------|-----|
| System design documentato | +25 |
| Mock interview completata | +50 |
| Behavioral story scritta (STAR) | +15 |
| API spec OpenAPI completa | +30 |
| Code review su OSS project | +40 |
| Tech blog post pubblicato | +75 |
| Conference talk (anche meetup locale) | +150 |

### 🏆 Career Boost Achievements

| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 🎤 | **Interview Ready** | 10 system designs + 5 mock interviews | +200 |
| 📝 | **Technical Writer** | 3 blog posts pubblicati | +150 |
| 🌍 | **Open Source Contributor** | 3 PR merged su progetti OSS | +200 |
| 💼 | **Offer Accepted** | Ricevi offerta €90k+ | +500 |

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

## 📊 Riepilogo Miglioramenti v3.0

| Miglioramento | Dettaglio |
|---------------|-----------|
| **P1.5 Auth & Security** | Nuova settimana dedicata |
| **P4 Rinominato** | "Alert Gateway" (no confusione con Architect P1) |
| **Testing Checklist** | Aggiunta a ogni progetto |
| **Resilience Patterns** | Espliciti in P4 (Bulkhead, etc.) |
| **Redis Progression** | Documentata evoluzione P1→P5 |
| **Rinforzo Architect** | Link espliciti tra progetti |
| **Career Boost Module** | System Design, Communication, API, Interview Prep |
| **System Design Practice** | Integrato in ogni progetto (P1-P5) |
| **Boss Battle System** | Verifica autonoma per ogni progetto (P1-P6) |
| **🤖 AI Features** | Ogni progetto ha una AI feature bonus! |

### 🤖 AI Features per Progetto
| Progetto | AI Feature | Skill AI |
|----------|------------|----------|
| P1 Task Manager | Smart Prioritization | Ollama base, prompt engineering |
| P2 Chat | Message Summarization | Streaming, chunking |
| P3 E-commerce | Product Recommendations | Embeddings, vector similarity |
| P4 Alert Gateway | Alert Triage & Grouping | Classification, pattern analysis |
| P5 URL Shortener | Link Preview Generator | Web scraping, structured output |
| P6 Capstone | Full AI Study Assistant | RAG, evaluation, personalization |

---

*Ultimo aggiornamento: 2026-02-12*
*Versione: 3.0 - AI Features + Boss Battle + Career Boost*