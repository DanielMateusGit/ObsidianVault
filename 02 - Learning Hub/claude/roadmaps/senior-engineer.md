# 💻 Roadmap Completa: Senior Engineer Path

> Percorso self-paced da mid-level a senior engineer internazionale
> *(Nessuna scadenza. Si procede per completamento, non per calendario.)*

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

## 🧭 6 Cluster di Ruolo Senior IC Targetizzabili (data-driven da analisi mercato)

> Derivato da analisi 12 annunci UK + remote (vedi `context/job-postings-senior.md`). Il mercato Senior IC ha **6 cluster distinti** con stack, accessibilità e salary diversi.

| Cluster | Esempio | Stack chiave | Salary range | Accessibilità Dan |
|---------|---------|--------------|--------------|--------------------|
| **#1 AI-Native Backend** ⭐ | Nothing, Paloma | Node/Python/.NET + LangGraph + MCP + RAG + Claude Code | £85k+ UK | **6-12 mesi** (richiede AI Mini-Projects + LangGraph hands-on) |
| **#2 Fintech Low-Latency** | TP ICAP | .NET/C# + low-latency + observability + TDD + DAPR | £80-130k UK | **9-12 mesi** (richiede low-latency + DAPR + observability) |
| **#3 Infrastructure / SRE-leaning** | Spotify | Java + cloud + distributed + on-call + CDN | £80-120k UK | **12+ mesi** (richiede on-call exp + Java) |
| **#4 Fintech Java Backend** | NatWest, Deutsche Bank | Java + Spring Boot + Kafka + K8s + AWS / Big Data | £70-110k UK | **6-9 mesi** (porting concettuale .NET → Java) |
| **#5 Modern Full-Stack** ⭐ | Trainline, Freetrade, Elliptic | Node/TS + React + AWS/GCP + microservices + Postgres | £52-90k UK | **3-6 mesi** ⭐ (stack moderno + cloud) |
| **#6 Consulting Polyglot** | Accenture | React + Node + Python + Java + cloud + AI cert OBBLIGATORIA | £60-100k UK | **9-12 mesi** (richiede AI cert + multi-stack) |

### Path strategico Senior IC per Dan

```
[OGGI] .NET solido + Architect Quest in corso + Senior P1 in corso
    ↓
[3-6 MESI] Cluster #5 Modern Full-Stack accessibile (UK £52-90k)
    Required: completamento P1-P2 + esposizione cloud + 2-3 mini-projects GitHub
    ↓
[6-9 MESI] Cluster #4 Fintech Java Backend OR #1 AI-Native Backend
    Required: porting concettuale Java/Spring Boot OR LangGraph+MCP hands-on
    ↓
[9-12 MESI] Cluster #2 Fintech Low-Latency OR #6 Consulting Polyglot
    Required: low-latency + observability OR AI cert + multi-stack
    ↓
[12+ MESI] Cluster #3 Infrastructure/SRE
    Required: on-call experience + reliability mindset + Java
```

### Portfolio richiesto per cluster

| Cluster | Cosa devi avere su GitHub |
|---------|---------------------------|
| #1 AI-Native | LangGraph agent + MCP server + RAG production-grade + AI cert |
| #2 Fintech Low-Latency | Microservices con observability stack + benchmark latency + TDD |
| #3 Infrastructure / SRE | Distributed system + on-call simulation + post-mortem docs |
| #4 Fintech Java | 1 progetto Java/Spring Boot + Kafka + K8s deployed |
| #5 Modern Full-Stack | Full-stack project (React + Node/Python BE) deployato cloud |
| #6 Consulting Polyglot | Stack-switching evidente (3+ linguaggi) + AI cert + casi d'uso |

### Sinergia con altre roadmap

- **Cluster #1 AI-Native Backend** = intersezione perfetta con `ai-skills.md` (Cluster #2/#3 AI Engineer)
- **Cluster #5 Modern Full-Stack** = sinergia con `senior-frontend.md` (Cluster #4 Founding FE)
- **Architect Quest** insegna design + leadership; **Senior Engineer** insegna implementation + ownership IC

---

## 📋 Sequenza Progetti

```
Step 1: P1 - Task Manager (Clean Arch, TDD, CQRS, Redis cache) ⭐ MINIMO
Step 2: P1.5 - Auth & Security 🔐 (JWT, OWASP basics) ⭐ MINIMO
Step 3: P2 - Chat App (SignalR, Redis Pub/Sub) ⭐ MINIMO
Step 4: P3 - E-commerce Cart (CQRS, Event Sourcing) ⭐ MINIMO
Step 5: P4 - Alert Gateway (Microservices, Circuit Breaker) 🔹 COMPLETO
Step 6: P5 - URL Shortener (Redis as Primary DB) 🔹 COMPLETO
Step 7: P6 - Capstone: AI Second Brain (RAG + tutti i pattern) 🔹 COMPLETO
```

> ⭐ **MINIMO** = Obbligatorio per primo colloquio €85k+
> 🔹 **COMPLETO** = Parte del Percorso Completo
> **Principio:** nessuna timeline. Ogni progetto si sblocca al completamento del precedente.

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
P1 M3:  Redis Pub/Sub           → messaging in-process, semplice
P2 M5:  RabbitMQ base           → broker esterno, un producer/consumer
P3 M10: Outbox Pattern (TDD)    → consistenza DB/Queue, costruito da zero
P4 M11: Messaging completo      → multi-service, DLQ, circuit breaker + queue
```
> In AQ hai PROGETTATO messaging (M5). In SE lo IMPLEMENTI con TDD, progressivamente.

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

### Scope
Più veloce rispetto ad Architect, focus su codice.

### XP & Achievement

| Risultato | XP | Achievement |
|-----------|-----|-------------|
| ≥24/30 (Superata) | +300 | ⚔️ **Code Warrior** |
| ≥28/30 (Con lode) | +500 | 🗡️ **Code Master** |
| Tutte e 6 superate | +1500 | 🏆 **Senior Champion** |

### Achievement Trasversali (Moduli M-T) 🆕

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 🌐 **Polyglot** | Porting di 1 modulo SE in 2nd linguaggio (Java/Node/Python) + ADR | +400 |
| 📊 **Observability Master** | OpenTelemetry + Prometheus + Grafana + Jaeger in 1 progetto | +350 |
| ☁️ **Cloud Native Deployer** | 1 progetto SE deployato su AWS/GCP managed (production-grade) | +400 |
| 🔧 **IaC Practitioner** | Terraform completo per 1 progetto (VPC + compute + DB + secrets) | +300 |
| 🚀 **CI/CD Builder** | GitHub Actions su tutti i progetti core (lint + test + build + deploy) | +250 |
| 🆔 **Identity Federator** | OAuth2/OIDC + Auth0/Keycloak + SCIM endpoint integrati | +350 |
| 🤖 **AI-Native Backend** | LangGraph agent + MCP server + RAG production-grade + AI cert | +500 |
| 📦 **Mini Builder** | 5 SE mini-projects pubblicati GitHub | +500 |
| 🚀 **Portfolio Pro** | 10 SE mini-projects + repo pinned curato | +750 |
| 🌍 **Cluster Ready** | Tutti i requirement portfolio per 1 cluster Senior IC raggiunti | +1000 |

---

## 🧪 MODULI TRASVERSALI (applicare a tutti i progetti)

> **Razionale:** Mercato Senior IC 2026 (12 annunci) richiede skill che attraversano TUTTI i progetti. Non sono moduli separati ma **mindset/practice** da applicare in ogni progetto della roadmap.

### M-T1: Stack Polyglot Awareness (cluster #4, #6 — *concetti, non hands-on upfront*)

> **Razionale:** Mercato Senior IC distribuisce su Node.js/TS (7/12), .NET (4/12), Java (4/12), Python (4/12). Tuttavia, Java/Spring Boot e Python si imparano **on-the-job in 2-4 settimane** se cluster target lo richiede.
> **Filosofia Dan:** non investire upfront in Java/Spring Boot mastery. Focus su **concetti universali** (DI, Repository, CQRS, EDA) trasferibili facilmente. Stack secondario = pickup on-the-job.

**Topics (awareness, no hands-on profondo):**
- **Concetti universali**: identifica i pattern (DI, Repository, CQRS, EDA) **indipendenti dal linguaggio**
- **Confronto sintassi**: come si esprime lo stesso pattern in C# vs Java vs Node/TS vs Python (lettura, non scrittura)
- **Ecosistemi paralleli (awareness)**:
  - .NET → ASP.NET Core, EF Core, MediatR ✅ stack primario Dan
  - Java → Spring Boot / Micronaut, JPA/Hibernate (pickup on-the-job se serve)
  - Node/TS → NestJS / Express, TypeORM / Prisma (pickup on-the-job)
  - Python → FastAPI / SQLAlchemy ✅ già coperto da Python AI Bridge Project

**Esercizio opzionale (NO obbligatorio):**
- Se cluster target è SE #4 Fintech Java: leggi 1-2 esempi di Spring Boot REST API + scrivi ADR concettuale "ASP.NET Core vs Spring Boot — cosa è universale, cosa cambia". **No porting completo.**
- Se cluster target è SE #5 Modern Full-Stack: lettura comparativa Express/NestJS sufficiente.

**Da applicare in:** opzionale. Priority bassa rispetto a M-T2 → M-T6.

---

### M-T2: Modern Observability Stack ⭐

> **Razionale:** 4/12 annunci espliciti su observability stack moderno (New Relic, ELK, Prometheus, Grafana, distributed tracing). Roadmap copre solo health checks + Serilog + correlation ID — insufficiente per ruoli £80k+.

**Stack standard 2026:**
- **OpenTelemetry** — vendor-neutral instrumentation (traces, metrics, logs)
- **Prometheus + Grafana** — metrics + dashboards
- **Jaeger / Tempo** — distributed tracing
- **ELK Stack** (Elasticsearch + Logstash + Kibana) OR **New Relic** awareness
- **Loki** — log aggregation cloud-native

**Topics:**
- Three pillars: logs + metrics + traces (cosa fanno, quando usarli)
- Trace propagation cross-service (W3C Trace Context)
- SLI/SLO/SLA basics
- Alerting rules pragmatiche (signal vs noise)
- Performance dashboards utili (golden signals: latency, traffic, errors, saturation)

**Da applicare in:** P4 Alert Gateway (microservices) come PRIMARY observability layer + retrofit P2 e P3

---

### M-T3: Cloud-Native Deployment ⭐

> **Razionale:** Tutti progetti su Docker locale, zero deploy su cloud managed. Mercato 8/12 AWS, 3/12 GCP. Senza esposizione cloud, portfolio sembra "studio", non "production".

**Topics:**
- **AWS basics**: Lambda + ECS + SQS + SNS + DynamoDB + RDS + S3 + EventBridge
- **GCP basics**: Cloud Run + Cloud Functions + Pub/Sub + Firestore + Cloud SQL
- **Azure basics** awareness: App Service + Functions + Service Bus + Cosmos DB
- **Decision framework**: Lambda vs ECS vs container orchestration (when use what)
- **Managed databases** vs self-hosted (cost vs ops trade-off)
- **Cloud-native patterns**: 12-factor app, externalized config, secrets management

**Esercizio obbligatorio:**
- Almeno **1 progetto SE deployato su cloud managed** (consigliato P5 URL Shortener su AWS Lambda + DynamoDB OR P1 Task Manager su Cloud Run)
- Documentare costi stimati + cold start considerations

**Da applicare in:** P1 minimum (deploy production), P5 raccomandato (Redis come primary su ElastiCache/Memorystore)

---

### M-T4: Infrastructure as Code (IaC) ⭐

> **Razionale:** 3/12 annunci espliciti (Trainline + Elliptic Terraform, Paloma Pulumi). Skill standard 2026 per Senior.

**Topics:**
- **Terraform basics**: state, modules, providers, workspaces, plan/apply
- **Pulumi awareness** (.NET-friendly, scrivi infra in C#)
- **CDK** (AWS) — opzionale
- **Best practices**: state remoto, lock, secrets out of state, environment promotion
- **GitOps fundamentals** (ArgoCD/Flux awareness)

**Esercizio obbligatorio:**
- **1 progetto SE con infra Terraform** (consigliato lo stesso del modulo M-T3 cloud deployment)
- IaC deve descrivere: VPC + compute + database + secrets + monitoring

**Da applicare in:** P1 o P5 (lo stesso del cloud deployment)

---

### M-T5: CI/CD Pipelines ⭐

> **Razionale:** Standard mercato 2026, mai esplicitato in roadmap. Tutti i progetti dovrebbero avere CI/CD reale.

**Stack standard:**
- **GitHub Actions** (de facto OSS standard)
- **Azure DevOps Pipelines** (enterprise alt)
- **GitLab CI** (awareness)

**Topics:**
- Pipeline fundamentals: lint → test → build → deploy
- **Trunk-based development** (vs GitFlow legacy)
- **PR validation** (pre-merge checks)
- **Deployment strategies**: blue/green, canary, rolling
- **Secret management** in pipeline (vault, GitHub secrets)
- **Caching dependencies** per pipeline veloci
- **Release engineering** basics (semantic versioning, changelogs)

**Da applicare in:** TUTTI i progetti P1-P6 da subito (no "lo aggiungo dopo")

---

### M-T6: AI Engineering Integration ⭐⭐ (PROMOSSO da bonus a CORE)

> **Razionale CRITICA:** Mercato 2026 richiede AI come HARD requirement (Accenture cert OBBLIGATORIA, Paloma chiede LangGraph + MCP per nome). AI non è più "bonus dopo deliverables core" — è prerequisito candidatura per cluster #1 e #6.

**Stack AI standard 2026 (sinergia con `ai-skills.md`):**
- **AI coding tools**: Claude Code (Dan ✅ cert), Cursor, Windsurf, GitHub Copilot
- **Spec-driven dev workflow**: scrivi spec → AI implementa → tu rifinisci
- **LangChain + LangGraph** (agent frameworks production)
- **MCP servers** (estendi Claude/agenti con tool custom — Dan ✅ cert)
- **RAG patterns** (vector DB + embeddings + retrieval)
- **Eval pipelines** (Ragas, DeepEval) — testare output non-deterministico
- **Provider abstraction** (LiteLLM, custom IAIProvider)

**Skill obbligatorie per Cluster #1 AI-Native Backend:**
- LangGraph agent in production (non solo prototipo)
- MCP server pubblicato GitHub
- RAG pipeline con eval metrics
- Spec-driven dev documentato (workflow, prompts, output)

**AI come "core" nei progetti SE:**
- Le AI Features per progetto (P1-P6) NON sono più "bonus" → sono **deliverable richiesto** per chi punta cluster #1
- Sinergia: ogni AI Feature SE è un mini-portfolio piece per cluster AI

**Da applicare in:** TUTTI i progetti se target cluster #1, opzionale altrove

---

## ✅ PROGETTO 1: Task Manager API

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

### Moduli

**Modulo 1: Domain + Application Layer**
- Domain model con TDD (Entities, VO, Events)
- Repository Interfaces + IUnitOfWork
- MediatR setup
- Commands (Create, Update, Complete, Delete Task)
- Queries (GetById, GetAll, GetByStatus)
- DTOs + FluentValidation
- Behaviors (Validation, Logging)

**Modulo 2: Infrastructure + API Layer**
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

**Modulo 2 — Workflow refactor TDD-driven (6 FASI)** ⭐ deciso 2026-05-07

Dopo audit codice esistente (M1 + M2 happy path già implementati ma con incoerenze: DueDate VO orfano, Project/Tag isolate, Description nullable mismatch, dispatch eventi mancante), il Modulo 2 è strutturato in 6 FASI atomiche con safety net TDD-first. NO rollback — refactor consapevole sul codice esistente.

| FASE | Focus | Status |
|------|-------|--------|
| FASE 1 | Safety Net (Testcontainers PostgreSQL fixture + primo integration test verde) | ✅ COMPLETATA 2026-05-07 |
| FASE 2 | Domain extension (Description, DueDate VO, Project/Tag relations) + Domain tests | ⬜ NEXT |
| FASE 3 | Persistence aggiornata (TaskItemConfiguration con OwnsOne/HasOne/HasMany + nuova Migration) | ⬜ |
| FASE 4 | Domain Events dispatch (override SaveChangesAsync + handler scheletri) | ⬜ |
| FASE 5 | Application cleanup (TaskNotFoundException + rimuovi Update superfluo + Commands esteso) | ⬜ |
| FASE 6 | API hardening (Exception Middleware + Serilog + Correlation ID + Swagger arricchito + API tests) | ⬜ |

**Riferimenti:** workflow + dettagli in `claude/sessions/2026-05-07.md`. Decisione strategica in `claude/current-state.md` > Decisioni Attive.

**Modulo 3: Redis + Messaging Base + Patterns + Boss Battle**
- Redis caching setup
- Cache-aside pattern
- **Redis Pub/Sub + BackgroundService** (task scadute → evento → worker aggiorna status)
  - Rinforzo AQ M5: implementi messaging in-process da zero con TDD
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

## 🔐 PROGETTO 1.5: Authentication & Security

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

### Modulo Aggiuntivo: Enterprise Identity Standards ⭐ (cluster #5 Customer Platform)

> **Razionale:** Annuncio Elliptic (Customer Platform) richiede Auth0 + OAuth2 + SAML + SCIM + OIDC. Skill differenziante per Customer Platform / SaaS multi-tenant. P1.5 attuale copre solo JWT custom — insufficiente per fascia £80k+ Customer Platform.

**Topics:**
- **OAuth 2.0 + OIDC**: authorization code flow + PKCE, refresh token rotation, scopes, claims
- **OpenID Connect**: identity layer su OAuth2, ID token, userinfo endpoint
- **SAML 2.0** awareness: SP-initiated vs IdP-initiated SSO, assertions, metadata exchange
- **SCIM** awareness: user provisioning standard (Okta/Azure AD → app), CRUD via REST
- **Auth0 / Keycloak hands-on**: configurare tenant, applicazioni, social login, custom rules
- **Multi-tenant SaaS patterns**: tenant isolation (DB-per-tenant vs shared schema vs row-level)
- **API Gateway auth**: JWT validation at gateway (Kong/Envoy/YARP)

**Esercizio:**
- Aggiungere a P1.5 (o Boss Battle): integrare **Auth0 OR Keycloak** come Identity Provider esterno + OIDC flow + scopes-based authorization
- Implementare **basic SCIM endpoint** per user provisioning (POST /Users, GET /Users/:id, PATCH)
- ADR: confronto JWT custom vs IdP esterno (when use what)

### Modulo: Security Deep Dive

**Step 1: JWT From Scratch**
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

**Step 2: Refresh Tokens + Redis**
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

**Step 3: OWASP Checklist**
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

## 💬 PROGETTO 2: Real-Time Chat

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

### Moduli

**Modulo 1: SignalR Basics**
- Setup SignalR hub
- Basic chat functionality
- Message persistence

**Modulo 2: Redis + Scaling + Resilience + RabbitMQ**
- Redis backplane per scaling
- Redis Pub/Sub
- Presence (chi è online)
- **📨 RabbitMQ per notifiche offline** (~3-4 ore)
  - User offline → messaggio in RabbitMQ queue → email/push quando torna
  - Producer (ChatHub) + Consumer (NotificationWorker)
  - Rinforzo AQ M5: primo broker esterno nel percorso SE, implementato con TDD
  - Confronto pratico: Redis Pub/Sub (P1 M3) vs RabbitMQ (qui) — quando usare quale
- **🛡️ Resilience Patterns con Polly** (mini-topic, ~2-3 ore)
  - Circuit Breaker: Redis va giu → il chat degrada, non crasha
  - Retry with exponential backoff: connessione persa → riprova intelligentemente
  - Timeout policy: nessuna operazione blocca per sempre
  - Perche qui: stai scalando un sistema real-time, i failure sono inevitabili. Meglio impararlo su un progetto dove li VEDI succedere

**Modulo 3: Frontend + Polish**
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

## 🛒 PROGETTO 3: E-Commerce Cart & Inventory

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

### Moduli

**Modulo 1: CQRS Basics**
- MediatR setup
- Commands e Queries separati
- Read/Write models

**Modulo 2: Event Sourcing**
- Event store setup
- Cart aggregate con eventi
- Event replay

**Modulo 3: Concurrency + Inventory + DB Design**
- Redis distributed locks
- Inventory management
- Optimistic concurrency
- **Query optimization & database design** (indexing, query plans, N+1 prevention)

**Modulo 4: Saga + Outbox Pattern + Polish**
- Checkout saga
- **📨 Outbox Pattern implementato da zero con TDD**
  - OrderPlaced → OutboxMessage → RabbitMQ → InventoryService, PaymentService
  - Rinforzo AQ M5: in AQ l'hai progettato, qui lo costruisci tu da solo
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

## 🚨 PROGETTO 4: Alert Gateway ← RINOMINATO

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

### Moduli

**Modulo 1: Service Decomposition + Messaging Completo**
- Identificare bounded contexts
- Setup 3 services: Gateway, Processor, Sender
- RabbitMQ communication tra servizi (Exchange types, routing)
- **📨 Messaging inter-service completo con TDD**
  - Outbox Pattern per ogni servizio (consistenza cross-service)
  - Dead Letter Queue (DLQ applicativa + DLQ RabbitMQ per confronto)
  - Retry con DeliveryAttempts + backoff controllato
  - Il "boss finale" del messaging: tutto quello imparato in P1-P3 applicato a multi-service
- Docker Compose per local dev

**Modulo 2: Resilience Patterns**
- Circuit Breaker con Polly
- Retry policies con exponential backoff
- Fallback strategies
- Bulkhead pattern
- Integrazione resilience + messaging (Circuit Breaker su RabbitMQ connection)

**Modulo 3: Gateway + Observability**
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

## 🔗 PROGETTO 5: URL Shortener with Analytics

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

### Moduli

**Modulo 1: Core + Redis**
- Minimal API setup
- Redis come primary store
- URL shortening logic
- Base62 encoding

**Modulo 2: Analytics**
- Redis Streams per eventi
- HyperLogLog per unique visitors
- Real-time analytics dashboard
- Sorted Sets per leaderboard

**Modulo 3: Performance**
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

## 🧠 PROGETTO 6: Capstone - AI Second Brain

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

### Fasi (sequenziali, no date)

**Fase 1: RAG Foundation**
- Vector DB setup, embedding pipeline
- Chunking strategies, Obsidian vault indexing
- Retrieval + basic Q&A
- Prompt optimization, context window management

**Fase 2: Advanced Features**
- Quiz generation dalle note
- "Related notes" suggestions
- CQRS per index/query separation
- Redis caching layer

**Fase 3: Multi-Service + Real-time**
- Service decomposition (indexer, query, quiz)
- SignalR per quiz real-time
- Docker Compose setup

**Fase 4: Production + Polish**
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

## 📦 SE MINI-PROJECTS PORTFOLIO (GitHub) ⭐ MARKET-CRITICAL

> **Razionale (data-driven):** 3+ annunci Senior chiedono GitHub portfolio in application (Accenture cert/portfolio AI obbligatorio, Paloma project AI built, Elliptic open-source contributions plus). Roadmap produce 6 progetti core grossi, ma manca cadenza di **mini-progetti backend pubblicabili** (1-2 settimane) per mostrare versatilità.

### Obiettivo

Costruire **5-10 micro-progetti backend standalone** (1-2 settimane ciascuno) **built with AI tools** (Claude Code, Cursor), pubblicati su GitHub con README pro + demo deployata cloud.

### Filosofia (allineata ad AI Mini-Projects + FE Mini-Projects)

- **Small but shipped > big but unfinished**
- **Built with AI**, not just **about AI** (documentare workflow Claude Code/Cursor nel README)
- **Production-grade signals**: tests, observability, IaC, CI/CD anche su mini-project
- **Business angle** chiaro nel README

### Backlog idee (SE-specific)

| # | Idea | Cluster target | Stack | Effort |
|---|------|----------------|-------|--------|
| 1 | **Distributed rate limiter** (token bucket + Redis) — pubblicare come npm/NuGet package | #5, #2 | .NET o Node + Redis | 1 settimana |
| 2 | **Event store mini** (write-only log + projections) | #2 | .NET o Java + Postgres | 2 settimane |
| 3 | **MCP server pubblico** (es. notes / git tools / database query) | #1 | TypeScript + MCP SDK | 1 settimana |
| 4 | **RAG agent backend** (FastAPI + LangGraph + pgvector) | #1 | Python + FastAPI + LangGraph | 2 settimane |
| 5 | **Distributed lock service** (Redlock implementation) | #5 | .NET o Go + Redis | 1 settimana |
| 6 | **Outbox library standalone** (riusabile in qualsiasi progetto) | #2, #4 | .NET + EF Core + RabbitMQ | 1-2 settimane |
| 7 | **Webhook gateway** (verifying + retry + DLQ) | #5, #6 | Node + AWS Lambda + SQS | 1 settimana |
| 8 | **DAPR sidecar demo** (state + pub/sub + bindings) — .NET-friendly distintivo | #2 | .NET + DAPR + K8s locale | 1-2 settimane |
| 9 | **Observability sample** (Prometheus + Grafana + Jaeger demo) | #2, #3 | qualsiasi BE + OpenTelemetry | 1 settimana |
| 10 | **OAuth2/OIDC playground** (Auth0 integration + SCIM endpoint) | #5 | .NET o Node + Auth0 SDK | 1 settimana |

### Regole esecuzione

1. **Build with AI tools obbligatorio** (Claude Code primario)
2. **Time-box stretto:** ≤2 settimane → tagli scope, non procrastini
3. **Public GitHub** + README + demo live (Vercel/Railway/Fly.io free tier o cloud managed)
4. **Production-grade signals visible**: tests, IaC, CI/CD, observability
5. **Business angle** + AI tools workflow doc nel README

### XP

- Mini-project completato + GitHub README pro: +150
- Demo live deployata cloud (AWS/GCP): +75
- README con AI tools workflow doc: +30
- Mini-project con engagement (stars/issues/fork): +100
- Mini-project pubblicato come **library/package** (npm/NuGet): +200
- 5 mini-projects raggiunti: **Boss Battle "SE Portfolio Built" +500 XP + 📦 Mini Builder**
- 10 mini-projects raggiunti: **Boss Battle "SE Portfolio Pro" +750 XP + 🚀 Portfolio Pro**

### Sinergia con altre Mini-Projects

Alcuni mini-projects sono **dual o triple-use** (SE + AI + FE):
- #3 MCP server pubblico = AI Mini #6 (MCP showcase) + SE Mini #3
- #4 RAG agent backend = AI Mini #2 (Document Q&A chatbot lato BE) + Python AI Bridge
- #7 Webhook gateway = #5 modern serverless con FE dashboard separato

→ ottimizza tempo: 1 progetto, 2-3 portfolio.

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

### Security 🔐
- [ ] JWT authentication from scratch
- [ ] Refresh token rotation
- [ ] OWASP Top 10 awareness
- [ ] Rate limiting

### Identity Standards Enterprise 🆔 🆕 (M-T extension)
- [ ] OAuth 2.0 + OIDC implementazione (authorization code + PKCE)
- [ ] SAML 2.0 awareness (SP-initiated SSO, assertions)
- [ ] SCIM awareness (user provisioning REST)
- [ ] Auth0 / Keycloak hands-on (almeno 1)
- [ ] Multi-tenant SaaS patterns (DB-per-tenant vs shared)
- [ ] API Gateway auth (JWT validation at gateway)

### Testing 🧪
- [ ] Unit testing (TDD)
- [ ] Integration testing (TestContainers)
- [ ] E2E testing
- [ ] Load/Performance testing (k6, NBomber)

### DevOps
- [ ] Docker multi-service
- [ ] Kubernetes deployment hands-on (almeno 1 progetto)
- [ ] Health checks & readiness probes

### Cloud-Native ☁️ 🆕 (M-T3)
- [ ] AWS basics: Lambda + ECS + SQS + SNS + DynamoDB + RDS + S3 + EventBridge
- [ ] GCP basics: Cloud Run + Cloud Functions + Pub/Sub + Firestore + Cloud SQL
- [ ] Azure basics awareness
- [ ] Decision framework: Lambda vs ECS vs container orchestration
- [ ] Almeno **1 progetto deployato su cloud managed** (production-grade)
- [ ] 12-factor app + externalized config + secrets management

### Infrastructure as Code 🔧 🆕 (M-T4)
- [ ] **Terraform** basics (state, modules, plan/apply)
- [ ] Pulumi awareness (.NET-friendly)
- [ ] Best practices (state remoto, secrets out of state)
- [ ] Almeno **1 progetto con infra Terraform** completa

### CI/CD Pipelines 🚀 🆕 (M-T5)
- [ ] **GitHub Actions** workflow per ogni progetto (lint + test + build + deploy)
- [ ] Azure DevOps Pipelines awareness
- [ ] **Trunk-based development** practices
- [ ] PR validation + pre-merge checks
- [ ] Deployment strategies: blue/green, canary, rolling
- [ ] Secret management in pipeline

### Modern Observability Stack 📊 🆕 (M-T2)
- [ ] **OpenTelemetry** instrumentation (traces + metrics + logs)
- [ ] **Prometheus + Grafana** (metrics + dashboards)
- [ ] **Jaeger / Tempo** distributed tracing
- [ ] ELK Stack OR New Relic awareness
- [ ] SLI/SLO/SLA basics
- [ ] Golden signals dashboard (latency, traffic, errors, saturation)

### Stack Polyglot Awareness 🌐 🆕 (M-T1)
- [ ] Concetti universali identificati indipendenti dal linguaggio
- [ ] Confronto sintassi: C# vs Java vs Node/TS vs Python
- [ ] Ecosistemi paralleli awareness (Spring Boot, NestJS, FastAPI)
- [ ] **Esercizio porting**: 1 modulo SE riscritto in Java/Spring Boot OR Node/NestJS + ADR comparativa

### AI Engineering Integration 🤖 🆕 (M-T6 — promosso da bonus a CORE)
- [ ] **AI coding tools mastery**: Claude Code (cert ✅), Cursor, Windsurf
- [ ] **Spec-driven dev workflow** documentato
- [ ] **LangChain + LangGraph** production (non solo prototipo)
- [ ] **MCP server pubblicato** GitHub
- [ ] **RAG pipeline** con eval metrics (Ragas/DeepEval)
- [ ] **Provider abstraction** (LiteLLM o custom IAIProvider)
- [ ] AI cert ottenuta o portfolio AI visibile
- [ ] AI integration in 3+ progetti SE come deliverable (non bonus)

### Portfolio
- [ ] 6+ progetti core completi
- [ ] **5-10 SE Mini-Projects** pubblicati GitHub (M-T applicato)
- [ ] **GitHub portfolio pubblico** con repo pinned curati
- [ ] Pronto per interview senior
- [ ] Target: €90k-130k remote

---

## Riepilogo Miglioramenti

| Versione | Miglioramento |
|----------|---------------|
| v3.0 | P1.5 Auth, P4 rinominato, Testing Checklist, Resilience Patterns, Redis Progression, Career Boost, Boss Battles, AI Features |
| v4.0 | P6 unito con AI Second Brain (RAG), Career Boost estratto in file separato |
| v5.0 | Self-paced refactor: rimossa timeline, Week→Modulo, sequenza per prerequisiti |
| **v6.0** | **Job-postings-driven enrichment (12 annunci UK/remote): aggiunti 6 cluster di ruolo Senior IC, 6 moduli trasversali (Polyglot + Observability + Cloud-Native + IaC + CI/CD + AI Engineering Integration), espansione P1.5 con Enterprise Identity Standards, SE Mini-Projects Portfolio, expanded Competenze Finali, 10 nuovi achievement trasversali** |

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

*Ultimo aggiornamento: 2026-05-07 (v6.2 — Modulo 2 esteso con sotto-sezione "Workflow refactor TDD-driven (6 FASI)": FASE 1 ✅ completata 2026-05-07 con Testcontainers + integration test verde; FASI 2-6 da fare. Decisione strategica refactor consapevole — vedi `current-state.md` Decisioni Attive)*
*Versione precedente: 2026-04-23 (v6.1 — Refactor pulizia: M-T1 Stack Polyglot depriorizzato a "awareness on-the-job" (no porting Java obbligatorio); SE Mini-Project #8 Java→DAPR demo; cluster taxonomy referenzia `context/cluster-taxonomy.md`; Mini-Projects link `context/mini-projects-index.md`)*
*Versione: 6.2*