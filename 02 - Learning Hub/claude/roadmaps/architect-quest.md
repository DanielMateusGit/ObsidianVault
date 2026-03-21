# 🏛️ Roadmap Completa: Architect Quest

> Percorso 30-36 mesi per diventare System Architect AI-Native
> *(10-15 ore/settimana con lavoro full-time. Progetti CORE = obbligatori, STRETCH = se tempo/energia)*

## 🎯 Obiettivo Finale

Essere capace di:
- Progettare sistemi enterprise complessi da zero
- Produrre documentazione (C4, ADR, OpenAPI) così precisa che AI agents possono implementare
- Deployare su cloud enterprise (Azure, Kubernetes)
- Prendere decisioni architetturali e giustificarle
- **Costruire un ecosystem di microservizi riutilizzabili**

---

## 🔗 ARCHITETTURA ECOSYSTEM

> **Filosofia:** Costruisci servizi generici riutilizzabili, poi usali nei progetti di dominio.

```
┌─────────────────────────────────────────────────────────────────┐
│                    🔧 SHARED SERVICES                            │
│              (Costruiti una volta, riusati ovunque)              │
│                                                                  │
│  ┌────────────────────┐       ┌────────────────────┐            │
│  │ 📧 NOTIFICATION    │       │ 🤖 AI GATEWAY      │            │
│  │    SERVICE         │       │                    │            │
│  │    (P1)            │       │    (P2.5)          │            │
│  │                    │       │                    │            │
│  │ • Multi-channel    │       │ • Provider abstraction          │
│  │ • Templates        │       │ • Ollama/Claude/OpenAI          │
│  │ • Retry/DLQ        │       │ • Cost tracking    │            │
│  │ • Delivery tracking│       │ • Rate limiting    │            │
│  └─────────┬──────────┘       └─────────┬──────────┘            │
│            │                            │                        │
└────────────┼────────────────────────────┼────────────────────────┘
             │                            │
             ▼                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    📦 DOMAIN PROJECTS                            │
│           (Imparano concetti nuovi + usano shared services)      │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ 🥗 NutriPlan │  │ 📅 BookingHub│  │ 💰 Family    │           │
│  │    (P2)      │  │    (P3)      │  │    Budget    │           │
│  │              │  │              │  │    (P4)      │           │
│  │ IMPARA:      │  │ IMPARA:      │  │ IMPARA:      │           │
│  │ • DDD        │  │ • Saga       │  │ • Flutter    │           │
│  │ • CQRS       │  │ • Kubernetes │  │ • Offline    │           │
│  │ • Event Src  │  │ • Observabil.│  │ • Sync       │           │
│  │              │  │              │  │              │           │
│  │ USA:         │  │ USA:         │  │ USA:         │           │
│  │ 📧 Notif.    │  │ 📧 Notif.    │  │ 📧 Notif.    │           │
│  │              │  │ 🤖 AI GW     │  │ 🤖 AI GW     │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

### Vantaggi dell'Ecosystem
- **Portfolio reale**: "Ho costruito un ecosystem di microservizi che comunicano"
- **Esperienza integration**: Non solo costruisci, ma INTEGRI servizi
- **Pensiero da architect**: Progetti servizi per essere riusati
- **Complessità progressiva**: Ogni progetto aggiunge servizi all'ecosystem

---

## 📅 Timeline Overview (30-36 Mesi)

> **Nota:** A 10-15 ore/settimana con lavoro full-time, la timeline reale è 30-36 mesi.
> I mesi indicati sono approssimativi. Progetti CORE vanno completati, STRETCH sono opzionali.

```
SHARED SERVICES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mesi 1-5:   P1 - Notification Service 📧 [SHARED SERVICE] ⭐ MINIMO
Mesi 6-8:   P2.5 - AI Gateway 🤖 [SHARED SERVICE] ⭐ MINIMO

DOMAIN PROJECTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mesi 6-12:  P2 - NutriPlan (DDD, CQRS) ← USA: Notification ⭐ MINIMO
Mesi 13-18: P3 - BookingHub (Saga, K8s) ← USA: Notif + AI GW 🔶 PRIMO COMPLETO
Mesi 19-24: P4 - FamilyBudget (Flutter) ← USA: Notif + AI GW 🔹 COMPLETO

CAPSTONE REALE 🏆
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mesi 25-30: P5 - FitHub 🏋️ (REALE!) ← UNISCE TUTTO 🔹 COMPLETO
            └── Backend: Multi-tenant + AI + Subscriptions
            └── Flutter app: Senior Frontend Track

AI-FIRST TRACK 🧠 (Parallelo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mesi 20-22: AI-2 - AI Interview Coach 🎤 (pre-job search) 🔹 COMPLETO
Mesi 31-33: AI-3 - Personal Copilot 🤖 (post-FitHub) 🔹 COMPLETO
```

> ⭐ **MINIMO** = Obbligatorio per primo colloquio €85k+
> 🔶 **PRIMO COMPLETO** = Primo progetto da fare dopo aver ottenuto il lavoro
> 🔹 **COMPLETO** = Percorso completo 30-36 mesi

> **Nota AI-1:** AI Second Brain è stato unito al Capstone Senior Engineer (P6).
> Vedi `senior-engineer.md` per dettagli.

---

## 🏆 SISTEMA BOSS BATTLE

> **Filosofia:** Dopo ogni progetto, verifica autonoma per dimostrare che sai fare le cose DA SOLO.

### Cos'è
Una "prova finale" dove Dan lavora in **autonomia** su un mini-progetto simile a quello appena completato. Claude è disponibile solo per domande "bloccanti", non per guida passo-passo.

### Struttura (Focus: 70% Design, 30% Code)

| Parte | Peso | Cosa Produci |
|-------|------|--------------|
| **A. Design** | 40% | ADR, C4 Diagrams (Context + Container) |
| **B. Domain Model** | 30% | Entities, Value Objects, Domain Events |
| **C. API Spec** | 15% | OpenAPI spec delle API principali |
| **D. Implementazione** | 15% | Feature/estensione sul progetto esistente |

### Criteri Valutazione (30 punti)

| Criterio | Punti | Cosa Valuto |
|----------|-------|-------------|
| **Architettura** | 10 | ADR sensati, C4 corretti, layer separation |
| **Domain Model** | 8 | Entities, Value Objects, aggregates corretti |
| **Trade-off Awareness** | 6 | Sa spiegare PERCHÉ ha scelto X invece di Y |
| **API Design** | 4 | RESTful, naming, error handling |
| **Completezza** | 2 | Tutti i deliverable richiesti |

### Durata
1-2 settimane (più leggero del progetto principale)

### XP & Achievement

| Risultato | XP | Achievement |
|-----------|-----|-------------|
| ≥24/30 (Superata) | +300 | 🎖️ **Battle Won** |
| ≥28/30 (Con lode) | +500 | 👑 **Battle Master** |
| Tutte e 4 superate | +1000 | 🏆 **Architect Champion** |

---

## 🔔 PROGETTO 1: Notification Service (Mesi 1-4) 📧 SHARED SERVICE

> **Tipo:** Shared Service - Sarà riutilizzato da P2, P3, P4

### Obiettivo
Sistema notifiche multi-canale (email, SMS, push, webhook) con retry, template, tracking.
**Progettato per essere consumato come servizio esterno dagli altri progetti.**

### Stack
- .NET 8, PostgreSQL, Redis
- Azure Service Bus (o RabbitMQ locale)
- Docker, Terraform, GitHub Actions

### Cosa Impari
- Clean Architecture in pratica
- Event-driven design
- Message queue con retry/dead letter
- Docker e containerization
- CI/CD pipeline
- Terraform basics
- Azure deployment
- **Progettare API per riusabilità** (SDK client, OpenAPI)

### Come Sarà Riusato
```
P2 NutriPlan   → Reminder piani alimentari, notifiche dietista
P3 BookingHub  → Conferme prenotazioni, SMS reminder, email receipt
P4 FamilyBudget → Alert budget superato, reminder spese ricorrenti
```

### Settimane

**Mese 1: Setup + Clean Architecture**
- W1: Project setup, struttura Clean Architecture, Docker Compose
- W2: Domain model (Notification, Template, DeliveryAttempt)
- W3: Application layer (use cases, ports/interfaces)
- W4: Infrastructure - Database con EF Core

**Mese 2: Event-Driven + Canali**
- W5: Message queue (Azure Service Bus o RabbitMQ)
- W6: Channel implementations (Email, SMS, Push, Webhook)
- W7: Template engine (Scriban)
- W8: Dead letter queue, retry logic

**Mese 3: API + DevOps**
- W9: REST API design, OpenAPI spec
- W10: Docker containerization production-ready
- W11: CI/CD pipeline (GitHub Actions)
- W12: Documentation (C4, ADR, README)

**Mese 4: Cloud + Production**
- W13-14: Terraform per Azure
- W15-16: Deployment, monitoring, Boss Battle

### 🏆 Boss Battle: "Reminder Service"

**Scenario:** Progetta un servizio di reminder per appuntamenti (diverso da notifiche, focus su scheduling).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (stack), ADR-002 (storage strategy), C4 Context + Container |
| **B. Domain Model** | Reminder entity, RecurrenceRule VO, ReminderTriggeredEvent |
| **C. API Spec** | OpenAPI per CRUD reminder + trigger endpoint |
| **D. Implementazione** | Aggiungi "Webhook" channel al Notification Service esistente |

**Performance Goal:** 10,000 notifiche in 5 min senza perdite (test sul progetto esistente)

### Deliverables
- [ ] Codebase Clean Architecture
- [ ] Message queue con retry/dead letter
- [ ] API REST con OpenAPI spec
- [ ] **Client SDK (.NET) per consumare il servizio**
- [ ] Docker Compose + Dockerfile
- [ ] CI/CD pipeline
- [ ] Terraform modules
- [ ] C4 diagrams (tutti i livelli)
- [ ] 4+ ADRs
- [ ] Sistema deployato su Azure

---

## 🤖 PROGETTO 2.5: AI Gateway (Mesi 5-6) 🤖 SHARED SERVICE

> **Tipo:** Shared Service - Sarà riutilizzato da P3, P4
> **Dettagli completi:** [[roadmaps/ai-skills|AI Skills Roadmap]]

### Obiettivo
Gateway AI provider-agnostic che astrae Ollama, Claude, OpenAI.
**Progettato per essere consumato come servizio dagli altri progetti.**

### Stack
- .NET 8 Minimal API (backend)
- Flutter (mobile app) 📱
- Ollama (locale), Claude API, OpenAI API
- PostgreSQL, Redis
- MCP Server (TypeScript)

### Cosa Impari
- AI Provider Abstraction (`IAIProvider`)
- AI Router (decide quale provider usare)
- Prompt Engineering
- Function Calling / Tool Use
- MCP Protocol
- Cost tracking & optimization
- RAG (Retrieval-Augmented Generation)

### Come Sarà Riusato
```
P3 BookingHub  → Assistente prenotazioni, query naturali staff
P4 FamilyBudget → Categorizzazione spese, consigli budget
```

### Core Architecture
```csharp
// Interface universale (funziona con qualsiasi provider)
public interface IAIGateway
{
    Task<AIResponse> ChatAsync(AIRequest request);
    Task<string> ClassifyAsync(ClassifyRequest request);
    Task<AIResponse> ChatWithToolsAsync(AIRequest request, List<Tool> tools);
}

// Router decide automaticamente il provider
public class AIRouter : IAIGateway
{
    public async Task<AIResponse> ChatAsync(AIRequest request)
    {
        if (request.RequiresComplexReasoning)
            return await _claudeProvider.ChatAsync(request);

        if (request.RequiresPrivacy || request.Budget == Budget.Low)
            return await _ollamaProvider.ChatAsync(request);

        return await _defaultProvider.ChatAsync(request);
    }
}
```

### 🏆 Boss Battle: "Document Q&A Service"

**Scenario:** Progetta un servizio RAG per fare domande su documenti PDF/Word.

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (embedding strategy), ADR-002 (vector DB choice), C4 Context + Container |
| **B. Domain Model** | Document entity, Chunk VO, QueryResult, EmbeddingGeneratedEvent |
| **C. API Spec** | OpenAPI per upload document, query, list documents |
| **D. Implementazione** | Aggiungi "conversation memory" all'AI Gateway esistente |

**Performance Goal:** Query con risposta in < 3 secondi su documento 50 pagine

---

## 🥗 PROGETTO 2: NutriPlan (Mesi 5-9) ← USA: 📧 Notification

> **Tipo:** Domain Project - Impara DDD/CQRS + integra Notification Service

### Obiettivo
Piattaforma SaaS per dietisti e pazienti. Piani alimentari, tracking, analytics.

### Stack
- .NET 8 + Aspire
- PostgreSQL + Marten (Event Sourcing)
- Meilisearch per search
- Azure AD B2C
- Blazor o React frontend
- **📧 Notification Service (P1)** per reminder e comunicazioni

### Cosa Impari
- Event Storming
- Strategic DDD (Bounded Contexts, Context Mapping)
- Tactical DDD (Aggregates, Entities, Value Objects)
- Event Sourcing con Marten
- CQRS (Command Query Responsibility Segregation)
- Multi-tenancy (schema-per-tenant)
- GraphQL API
- **Integrazione con servizi esterni (consume Notification API)**

### Integrazione Notification Service
```csharp
// Quando un dietista assegna un piano, notifica il paziente
await _notificationClient.SendAsync(new NotificationRequest
{
    Channel = NotificationChannel.Email,
    Recipient = patient.Email,
    Template = "new-meal-plan",
    Data = new { PatientName = patient.Name, PlanName = plan.Name }
});

// Reminder giornaliero pasti
await _notificationClient.ScheduleAsync(new ScheduledNotification
{
    Channel = NotificationChannel.Push,
    Recipient = patient.DeviceToken,
    Template = "meal-reminder",
    ScheduledFor = DateTime.Today.AddHours(12) // Pranzo
});
```

### Settimane

**Mese 5: Domain Discovery**
- W1-2: Event Storming completo
- W3-4: Context Mapping, Bounded Contexts

**Mese 6: Core Domain**
- W5-6: Aggregate design (MealPlan)
- W7-8: Event Sourcing con Marten

**Mese 7: CQRS + Persistence**
- W9-10: CQRS implementation, Read Models
- W11-12: Multi-tenancy

**Mese 8: API + Frontend**
- W13-14: GraphQL API (HotChocolate)
- W15-16: Frontend MVP

**Mese 9: Polish + Production**
- W17-18: Food database integration (ACL)
- W19-20: Deployment, Boss Battle

### 🏆 Boss Battle: "Fitness Tracker"

**Scenario:** Progetta un sistema per tracking workout con Event Sourcing (dominio diverso, stessi pattern DDD/CQRS).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (Event Sourcing vs CRUD), ADR-002 (aggregate boundaries), C4 Context + Container |
| **B. Domain Model** | Workout aggregate, Exercise VO, WorkoutCompletedEvent, read models |
| **C. API Spec** | GraphQL schema per query workout history + mutations |
| **D. Implementazione** | Aggiungi "Meal Photo Recognition" a NutriPlan (integration con AI Gateway) |

**Performance Goal:** 50 utenti attivi, tracking giornaliero, query < 100ms

---

## 📅 PROGETTO 3: BookingHub (Mesi 10-14) ← USA: 📧 Notification + 🤖 AI Gateway

> **Tipo:** Domain Project - Impara Saga/K8s + integra ENTRAMBI i servizi shared

### Obiettivo
Sistema prenotazioni per studi professionali. Calendar sync, pagamenti, notifiche.

### Stack
- .NET 8 + Aspire
- PostgreSQL, Redis
- MassTransit (Saga)
- Azure Kubernetes Service (AKS)
- Stripe, Google Calendar, Microsoft Graph
- **📧 Notification Service (P1)** per conferme e reminder
- **🤖 AI Gateway (P2.5)** per assistente prenotazioni

### Cosa Impari
- Saga Pattern (Orchestration)
- Compensating transactions
- External service integration
- Kubernetes deployment
- Full observability (OpenTelemetry, Grafana)
- Production operations
- **Orchestrazione di più servizi shared**

### Integrazione Notification Service
```csharp
// Saga: dopo pagamento confermato, invia notifiche
public class BookingSaga : MassTransitStateMachine<BookingState>
{
    // Step 3: Pagamento OK → Notifica cliente + professionista
    During(PaymentConfirmed,
        When(PaymentSucceeded)
            .Then(ctx => _notificationClient.SendAsync(new NotificationRequest
            {
                Channel = NotificationChannel.Email,
                Recipient = ctx.Data.CustomerEmail,
                Template = "booking-confirmed",
                Data = new { ... }
            }))
            .TransitionTo(Confirmed));
}

// SMS reminder 24h prima
await _notificationClient.ScheduleAsync(new ScheduledNotification
{
    Channel = NotificationChannel.SMS,
    Recipient = booking.CustomerPhone,
    Template = "appointment-reminder-24h",
    ScheduledFor = booking.DateTime.AddHours(-24)
});
```

### Integrazione AI Gateway
```csharp
// Assistente AI per prenotazioni (usa AI Gateway)
var response = await _aiGateway.ChatAsync(new AIRequest
{
    Provider = AIProvider.Auto, // Router decide Ollama vs Claude
    Messages = conversation,
    Tools = new[] { "find_available_slots", "create_booking", "cancel_booking" }
});

// Query naturale staff
// "Chi ha cancellato negli ultimi 7 giorni?"
var answer = await _aiGateway.QueryAsync(userQuestion, context: bookingData);
```

### Settimane

**Mese 10: Domain + Saga**
- W1-2: Event Storming, Saga design
- W3-4: Saga implementation con MassTransit

**Mese 11: Integrazioni**
- W5-6: Calendar integration (Google, Outlook)
- W7-8: Payment integration (Stripe)

**Mese 12: Kubernetes**
- W9-10: AKS setup con Terraform
- W11-12: Helm charts, Ingress, TLS

**Mese 13: Observability**
- W13-14: OpenTelemetry, Grafana stack
- W15-16: Alerting, SLI/SLO

**Mese 14: AI Integration + Production** 🤖
- W17: AI Assistant MVP (patient-facing, staff queries)
- W18: Smart scheduling con AI
- W19-20: Load testing, security audit, Boss Battle

### 🏆 Boss Battle: "Event Ticketing System"

**Scenario:** Progetta un sistema di prenotazione biglietti eventi con Saga pattern (dominio diverso, stessi pattern).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (Saga orchestration vs choreography), ADR-002 (payment failure handling), C4 Context + Container |
| **B. Domain Model** | Ticket aggregate, Seat VO, BookingSaga state machine, compensating transactions |
| **C. API Spec** | OpenAPI per book ticket, cancel, refund |
| **D. Implementazione** | Aggiungi "Waitlist con notifica automatica" a BookingHub |

**Performance Goal:** 100 prenotazioni simultanee con failure scenarios gestiti correttamente

---

## 💰 PROGETTO 4: FamilyBudget (Mesi 15-18) ← USA: 📧 Notification + 🤖 AI Gateway

> **Tipo:** Domain Project - Impara Flutter/Offline + integra ENTRAMBI i servizi shared

### Obiettivo
App mobile per budget familiare. Offline-first, sync, real-time.

### Stack
- Flutter (mobile)
- .NET 8 (backend)
- PostgreSQL, Redis
- SignalR (real-time)
- **📧 Notification Service (P1)** per alert e reminder
- **🤖 AI Gateway (P2.5)** per categorizzazione e consigli

### Cosa Impari
- Flutter development
- Offline-first architecture
- Sync protocols
- Conflict resolution
- Real-time con SignalR
- Mobile deployment (App Store, Play Store)
- **Integrazione servizi in app mobile**

### Integrazione Notification Service
```csharp
// Alert quando budget superato
await _notificationClient.SendAsync(new NotificationRequest
{
    Channel = NotificationChannel.Push,
    Recipient = user.DeviceToken,
    Template = "budget-exceeded",
    Data = new {
        Category = "Ristoranti",
        Spent = 320,
        Budget = 300
    }
});

// Reminder spese ricorrenti (affitto, bollette)
await _notificationClient.ScheduleAsync(new ScheduledNotification
{
    Channel = NotificationChannel.Push,
    Template = "recurring-expense-reminder",
    ScheduledFor = expense.DueDate.AddDays(-3)
});
```

### Integrazione AI Gateway
```csharp
// Categorizzazione automatica spese (Ollama - veloce, locale)
var category = await _aiGateway.ClassifyAsync(new ClassifyRequest
{
    Provider = AIProvider.Ollama, // Sempre locale per privacy
    Text = "Pagamento POS Esselunga Milano",
    Categories = new[] { "Supermercato", "Ristoranti", "Trasporti", ... }
});

// Consigli budget (Claude - reasoning complesso)
var advice = await _aiGateway.ChatAsync(new AIRequest
{
    Provider = AIProvider.Claude, // Reasoning avanzato
    SystemPrompt = "Sei un consulente finanziario familiare...",
    Messages = new[] {
        new Message("Posso permettermi un MacBook da 2000€?")
    },
    Context = userBudgetData
});
```

### Settimane

**Mese 15: Flutter + Offline**
- W1-2: Flutter basics, local DB (Drift)
- W3-4: Offline-first architecture

**Mese 16: Backend + Sync**
- W5-6: Backend API con sync endpoint
- W7-8: Conflict resolution

**Mese 17: Real-time + AI Features** 🤖
- W9-10: SignalR integration
- W11: AI expense categorization & queries
- W12: AI budget advisor

**Mese 18: Polish + Launch**
- W13-14: UI polish, testing
- W15-16: Store preparation, Boss Battle

### 🏆 Boss Battle: "Shared Shopping List"

**Scenario:** Progetta un'app per lista della spesa condivisa con offline-first e sync (dominio semplice, stessi pattern).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (conflict resolution strategy), ADR-002 (sync protocol), C4 Context + Container |
| **B. Domain Model** | ShoppingList aggregate, Item VO, sync events, conflict resolution rules |
| **C. API Spec** | OpenAPI per sync endpoint + WebSocket spec per real-time |
| **D. Implementazione** | Aggiungi "Receipt scanning con OCR" a FamilyBudget (AI-powered) |

**Performance Goal:** 4 utenti offline, modifiche concorrenti, sync senza perdita dati

---

## 🏋️ PROGETTO 5: FitHub (Mesi 19-22) 🏋️ CAPSTONE REALE

> **Tipo:** Capstone Project - UNISCE TUTTO! Progetto reale monetizzabile.
> **Cross-progetto:** Usa patterns e servizi da P1, P2, P2.5, P3, P4
> **Monetizzazione:** ⭐⭐⭐⭐⭐ - Dan può proporlo alla palestra dove lavora!

### Obiettivo
App fitness multi-versione (Yoga/Stretching, CrossFit, Palestra) con:
- **B2B:** Palestre come clienti (gestione allenatori, turni, abbonamenti)
- **B2C:** Utenti singoli (allenamento casa, tracking progressi)
- **White-label:** Una codebase, multiple skin per mercati verticali
- **AI:** Assistenza personalizzata per allenamenti e nutrizione

### Stack
- .NET 8 + Aspire (backend)
- PostgreSQL + Redis
- Azure Service Bus (events)
- **📧 Notification Service (P1)** per reminder e comunicazioni
- **🤖 AI Gateway (P2.5)** per workout planning e consigli
- Multi-tenant architecture (da P3)
- Subscription billing (da P3)

### Cosa Impari (Consolidamento)
- **Multi-tenant Architecture** avanzata (schema-per-tenant)
- **White-label Patterns** (stessa codebase, diverse UI/branding)
- **AI Workout Planning** (usa AI Gateway)
- **Subscription Management** (Stripe, piani diversi per palestre/utenti)
- **Role-based Access** complesso (owner, coach, member)
- **Real-world Product Development** (da progetto didattico a prodotto reale)

### Architettura Cross-Progetto
```
┌─────────────────────────────────────────────────────────────────┐
│                    🏋️ FITHUB                                    │
│              (Unisce TUTTO quello che hai imparato)             │
│                                                                  │
│  DA P1 NOTIFICATION SERVICE:                                    │
│  └── Reminder allenamenti, notifiche coach, alert abbonamenti   │
│                                                                  │
│  DA P2 NUTRIPLAN:                                               │
│  └── AI meal suggestions per atleti, tracking nutrition         │
│                                                                  │
│  DA P2.5 AI GATEWAY:                                            │
│  └── Workout generation, form analysis, progress insights       │
│                                                                  │
│  DA P3 BOOKINGHUB:                                              │
│  └── Multi-tenant, subscription billing, scheduling             │
│                                                                  │
│  DA P4 FAMILYBUDGET:                                            │
│  └── Flutter basics, offline-first patterns                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Versioni App (White-label)
```
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ 🧘 YOGA/STRETCH  │  │ 🏋️ CROSSFIT      │  │ 💪 GYM           │
│                  │  │                  │  │                  │
│ - Routine yoga   │  │ - WOD generator  │  │ - Schede workout │
│ - Flexibility    │  │ - Box management │  │ - Nutrition AI   │
│ - Meditation     │  │ - Leaderboards   │  │ - Progress track │
│ - Breathing      │  │ - PR tracking    │  │ - Personal trainer│
└──────────────────┘  └──────────────────┘  └──────────────────┘
         │                    │                    │
         └────────────────────┴────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │  SHARED CODEBASE  │
                    │  (90% common)     │
                    └───────────────────┘
```

### Settimane

**Mese 19: Architecture & Core**
- W1-2: Multi-tenant setup, tenant isolation
- W3-4: Core domain (Workout, Exercise, Member, Coach, Subscription)

**Mese 20: Features & AI**
- W5-6: AI workout generation (usa AI Gateway)
- W7-8: Subscription management, billing (Stripe)

**Mese 21: White-label & Roles**
- W9-10: White-label infrastructure (theming, feature flags)
- W11-12: Coach dashboard, member app, owner analytics

**Mese 22: Polish & Launch**
- W13-14: Integration tests, load testing
- W15: Documentation, deployment
- W16: Boss Battle + **PROPONI ALLA TUA PALESTRA!** 💰

### Integrazione Notification Service
```csharp
// Reminder allenamento
await _notificationClient.ScheduleAsync(new ScheduledNotification
{
    Channel = NotificationChannel.Push,
    Recipient = member.DeviceToken,
    Template = "workout-reminder",
    Data = new { WorkoutName = "Upper Body", Time = "18:00" },
    ScheduledFor = workout.ScheduledTime.AddMinutes(-30)
});

// Notifica coach su nuovo iscritto
await _notificationClient.SendAsync(new NotificationRequest
{
    Channel = NotificationChannel.Email,
    Recipient = coach.Email,
    Template = "new-member-assigned",
    Data = new { MemberName = member.Name, Plan = subscription.Plan }
});
```

### Integrazione AI Gateway
```csharp
// AI genera workout personalizzato
var workout = await _aiGateway.ChatAsync(new AIRequest
{
    Provider = AIProvider.Auto, // Ollama per velocità, Claude per complessità
    SystemPrompt = "Sei un personal trainer esperto...",
    Messages = new[] {
        new Message($"Genera un allenamento {workoutType} per {member.FitnessLevel}")
    },
    Tools = new[] { "get_member_history", "get_exercise_database" }
});

// AI analizza form da video (futuro)
var formFeedback = await _aiGateway.AnalyzeAsync(new AnalyzeRequest
{
    Type = AnalysisType.Video,
    Content = videoFrame,
    Prompt = "Analizza la forma dello squat e suggerisci correzioni"
});
```

### 🏆 Boss Battle: "Gym Chain Platform"

**Scenario:** Estendi FitHub per supportare catene di palestre (multi-location).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (tenant hierarchy: chain → location → member), C4 Context + Container |
| **B. Domain Model** | Chain aggregate, Location VO, cross-location membership |
| **C. API Spec** | OpenAPI per chain management, location analytics |
| **D. Implementazione** | Cross-location member transfer feature |

**Performance Goal:** 5 locations, 100 members each, real-time sync

### Deliverables
- [ ] Multi-tenant backend completo
- [ ] AI workout generation funzionante
- [ ] Subscription billing con Stripe
- [ ] 3 skin white-label (Yoga, CrossFit, Gym)
- [ ] Coach + Member + Owner dashboards
- [ ] Integration con Notification Service
- [ ] Integration con AI Gateway
- [ ] **PROPOSTA COMMERCIALE per la tua palestra!** 💰

### 💰 Piano Monetizzazione

| Modello | Prezzo Indicativo | Target |
|---------|-------------------|--------|
| **Palestra singola** | €50-100/mese | Box CrossFit, studi yoga |
| **Multi-location** | €200-500/mese | Catene palestre |
| **Enterprise** | Custom | Grandi franchising |
| **Utente singolo** | €5-10/mese o freemium | Home fitness |

**Revenue potenziale anno 1:** Se 5 palestre × €100/mese = €6.000/anno
**Revenue potenziale anno 3:** Se 50 palestre × €150/mese = €90.000/anno

---

## 🧠 AI-1: AI Second Brain → Unito al Capstone Senior

> **NOTA:** AI Second Brain è stato unito al Progetto 6 (Capstone) del Senior Engineer Path.
> È il capstone ideale perché combina RAG, vector DB, embeddings con tutti i pattern Senior
> (TDD, CQRS, Redis, Docker, SignalR, Microservices).
>
> Vedi: `roadmaps/senior-engineer.md` → Progetto 6

---

## 🎤 AI-2: AI Interview Coach (Mesi 15-16) 🎤 AI-FIRST

> **Tipo:** AI-First Project - Ti prepara per i colloqui €90k-130k!
> **Parallelo a:** P4 FamilyBudget

### Obiettivo
Il tuo personal coach per superare technical interviews. System design, coding, behavioral.

### Stack
- .NET 8 + Blazor (web UI)
- Claude API (complex reasoning per evaluation)
- Whisper + TTS (voice, opzionale)
- PostgreSQL (progress tracking)

### Cosa Impari
- **AI Evaluation** (grading risposte, feedback strutturato)
- **Structured Output** (JSON mode, schema validation)
- **Multi-turn conversations** (context management)
- **Voice AI** (speech-to-text, text-to-speech)
- **Prompt engineering per assessment**

### Features

```
┌─────────────────────────────────────────────────────────────┐
│                 AI INTERVIEW COACH                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🎯 SYSTEM DESIGN MODE                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "Design a URL shortener like bit.ly"                │   │
│  │                                                      │   │
│  │ [Your answer...]                                     │   │
│  │                                                      │   │
│  │ 📊 Evaluation:                                       │   │
│  │ • Requirements gathering: 8/10                       │   │
│  │ • High-level design: 7/10                           │   │
│  │ • Deep dive: 6/10                                   │   │
│  │ • Trade-offs: 9/10                                  │   │
│  │                                                      │   │
│  │ 💡 Feedback: "Consider discussing database          │   │
│  │    sharding strategy for scale..."                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  🗣️ BEHAVIORAL MODE (STAR)                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "Tell me about a time you disagreed with your team" │   │
│  │                                                      │   │
│  │ 📊 STAR Analysis:                                    │   │
│  │ • Situation: ✅ Clear                               │   │
│  │ • Task: ✅ Defined                                  │   │
│  │ • Action: ⚠️ Could be more specific                 │   │
│  │ • Result: ❌ Missing metrics                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  💻 TECHNICAL MODE                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ "Explain the difference between CQRS and CRUD"      │   │
│  │                                                      │   │
│  │ [Your answer...]                                     │   │
│  │                                                      │   │
│  │ 📊 Score: 8/10                                       │   │
│  │ 💡 "Good! Also mention read/write model separation" │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📈 PROGRESS TRACKING                                       │
│  System Design: ████████░░ 80%                             │
│  Behavioral:    ██████░░░░ 60%                             │
│  Technical:     █████████░ 90%                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Settimane

**Mese 15: Core Features**
- W1: System design interview simulator
- W2: Evaluation prompts + scoring
- W3: Behavioral (STAR) mode
- W4: Technical questions bank

**Mese 16: Polish + Voice**
- W5: Progress tracking, weak areas identification
- W6: Voice input/output (Whisper + TTS)
- W7: Mock interview mode (full simulation)
- W8: Boss Battle

### 🏆 Boss Battle: "Peer Interview Platform"

**Scenario:** Estendi per permettere mock interviews tra utenti (peer-to-peer).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (matching algorithm), C4 Container per multi-user |
| **B. Domain Model** | Interview, Participant, Feedback, MatchingRequest |
| **C. API Spec** | OpenAPI per schedule interview, submit feedback |
| **D. Implementazione** | Video call integration (Daily.co o simile) |

### Deliverables
- [ ] System design simulator con evaluation
- [ ] Behavioral STAR analyzer
- [ ] Technical questions con feedback
- [ ] Progress tracking dashboard
- [ ] Voice mode (opzionale ma figo)

---

## 🤖 AI-3: Personal Copilot (Mesi 23-24) 🤖 AI-FIRST

> **Tipo:** AI-First Project - Il TUO assistente coding!
> **Dopo:** P4 FamilyBudget completato

### Obiettivo
Un Copilot personalizzato che conosce il TUO stile di codice e i TUOI progetti.

### Stack
- MCP Server (TypeScript) - già conosci da P2.5
- GitHub API
- AST parsing (Roslyn per C#)
- Claude API con tool use
- VS Code extension

### Cosa Impari
- **MCP avanzato** (complex tools, multi-step workflows)
- **Code analysis** (AST parsing, static analysis)
- **GitHub integrations** (PR review, commit analysis)
- **Personalization** (learning user patterns)
- **VS Code extension development**

### Features

```
┌─────────────────────────────────────────────────────────────┐
│                   PERSONAL COPILOT                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔍 CODE REVIEW                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ PR #42: "Add notification retry logic"              │   │
│  │                                                      │   │
│  │ 🤖 Review:                                           │   │
│  │ • ✅ Good: Follows your retry pattern from P1       │   │
│  │ • ⚠️ Suggestion: Consider exponential backoff       │   │
│  │ • ❌ Issue: Missing null check line 45              │   │
│  │ • 💡 Style: You usually use guard clauses here      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  🧪 TEST GENERATION                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Selected: NotificationService.SendAsync()           │   │
│  │                                                      │   │
│  │ 🤖 Generated tests:                                  │   │
│  │ • SendAsync_ValidNotification_ReturnsSuccess        │   │
│  │ • SendAsync_NullRecipient_ThrowsArgumentException   │   │
│  │ • SendAsync_ChannelUnavailable_RetriesThreeTimes    │   │
│  │                                                      │   │
│  │ [Apply to project] [Edit] [Regenerate]              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📝 REFACTORING SUGGESTIONS                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ File: NotificationHandler.cs                        │   │
│  │                                                      │   │
│  │ 🤖 Suggestions based on YOUR patterns:              │   │
│  │ • Extract method: lines 45-67 → ValidateRequest()   │   │
│  │ • This class has 8 methods, you usually keep < 6    │   │
│  │ • Consider splitting into Handler + Validator       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  💬 CHAT (Context-aware)                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ You: "How did I implement retry in P1?"             │   │
│  │                                                      │   │
│  │ 🤖: "In P1 Notification Service, you used Polly    │   │
│  │     with exponential backoff. Here's the code:      │   │
│  │     [code from your actual project]                 │   │
│  │     Want me to apply the same pattern here?"        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Settimane

**Mese 19: Core Features**
- W1: MCP server con GitHub integration
- W2: Code review automation
- W3: Test generation con AST parsing
- W4: Refactoring suggestions

**Mese 20: Personalization + VS Code**
- W5: Learn user patterns (analyze past commits)
- W6: VS Code extension
- W7: Chat mode con project context
- W8: Boss Battle

### 🏆 Boss Battle: "Team Copilot"

**Scenario:** Estendi per supportare team (shared patterns, team style guide enforcement).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (team patterns storage), C4 Container |
| **B. Domain Model** | Team, StyleGuide, Pattern, Violation |
| **C. API Spec** | OpenAPI per team management, pattern CRUD |
| **D. Implementazione** | Style guide enforcement in PR review |

### Deliverables
- [ ] MCP server con tool use avanzato
- [ ] GitHub PR review automation
- [ ] Test generation
- [ ] Refactoring suggestions
- [ ] VS Code extension
- [ ] Chat con context dei tuoi progetti

---

## 📚 Libri Chiave (in ordine)

1. **"Designing Data-Intensive Applications"** - Kleppmann (FONDAMENTALE)
2. **"Fundamentals of Software Architecture"** - Richards & Ford
3. **"Clean Architecture"** - Martin
4. **"Domain-Driven Design Distilled"** - Vernon
5. **"Building Microservices"** - Newman
6. **"Software Architecture: The Hard Parts"** - Richards & Ford
7. **"Implementing Domain-Driven Design"** - Vernon
8. **"Terraform: Up & Running"** - Brikman

---

## 🎯 Competenze Finali

Alla fine del percorso:

### Architecture & Design
- [ ] Clean Architecture
- [ ] Event-driven design
- [ ] DDD (Strategic + Tactical)
- [ ] CQRS + Event Sourcing
- [ ] Saga Pattern
- [ ] **Microservices ecosystem design** 🔗
- [ ] **API design for reusability** (SDK, OpenAPI) 🔗

### Infrastructure & DevOps
- [ ] Kubernetes deployment
- [ ] Full observability
- [ ] Infrastructure as Code (Terraform)
- [ ] CI/CD pipelines

### Documentation
- [ ] C4 documentation
- [ ] ADR writing

### API & Integration
- [ ] REST API design
- [ ] GraphQL API
- [ ] **Service integration patterns** 🔗
- [ ] **Consuming external services** 🔗

### Mobile & Frontend
- [ ] Mobile (Flutter)
- [ ] Offline-first architecture

### AI Skills 🤖
- [ ] AI Provider Abstraction
- [ ] AI Integration (Ollama, Claude, OpenAI)
- [ ] RAG, function calling, prompt engineering
- [ ] AI-Native system design

### AI-First Skills 🧠 (NEW!)
- [ ] **RAG completo** (chunking, embeddings, retrieval)
- [ ] **Vector databases** (Qdrant, ChromaDB)
- [ ] **Semantic search** vs keyword search
- [ ] **AI Evaluation** (grading, structured feedback)
- [ ] **Voice AI** (Whisper, TTS)
- [ ] **MCP avanzato** (complex tools, multi-step)
- [ ] **Code analysis con AI** (AST + LLM)
- [ ] **VS Code extension development**

### 🔗 = Skill dall'ecosystem | 🧠 = Skill da AI-First Track

---

*Ultimo aggiornamento: 2026-03-13*
*Versione: 5.0 - Timeline realistica (30-36 mesi), AI-1 unito a Senior P6, progetti CORE vs STRETCH*