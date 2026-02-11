# 🏛️ Roadmap Completa: Architect Quest

> Percorso 18 mesi per diventare System Architect AI-Native

## 🎯 Obiettivo Finale

Essere capace di:
- Progettare sistemi enterprise complessi da zero
- Produrre documentazione (C4, ADR, OpenAPI) così precisa che AI agents possono implementare
- Deployare su cloud enterprise (Azure, Kubernetes)
- Prendere decisioni architetturali e giustificarle

---

## 📅 Timeline Overview

```
Mesi 1-4:   P1 - Notification Service (Clean Arch, Event-driven)
Mesi 5-9:   P2 - NutriPlan (DDD, CQRS, Event Sourcing)
            P2.5 - AI Calendar Assistant 🤖 (Ollama, AI-Native Skills)
Mesi 10-14: P3 - BookingHub (Saga, Kubernetes, Observability + AI Integration 🤖)
Mesi 15-18: P4 - FamilyBudget (Flutter, Offline-first, Sync + AI Integration 🤖)
```

**🤖 = Include AI locale con Ollama** | [[roadmaps/ai-skills|→ AI Skills Roadmap]]

---

## 🔔 PROGETTO 1: Notification Service (Mesi 1-4)

### Obiettivo
Sistema notifiche multi-canale (email, SMS, push, webhook) con retry, template, tracking.

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

### Boss Battle
10,000 notifiche in 5 min senza perdite. **Reward: +500 XP**

### Deliverables
- [ ] Codebase Clean Architecture
- [ ] Message queue con retry/dead letter
- [ ] API REST con OpenAPI spec
- [ ] Docker Compose + Dockerfile
- [ ] CI/CD pipeline
- [ ] Terraform modules
- [ ] C4 diagrams (tutti i livelli)
- [ ] 4+ ADRs
- [ ] Sistema deployato su Azure

---

## 🥗 PROGETTO 2: NutriPlan (Mesi 5-9)

### Obiettivo
Piattaforma SaaS per dietisti e pazienti. Piani alimentari, tracking, analytics.

### Stack
- .NET 8 + Aspire
- PostgreSQL + Marten (Event Sourcing)
- Meilisearch per search
- Azure AD B2C
- Blazor o React frontend

### Cosa Impari
- Event Storming
- Strategic DDD (Bounded Contexts, Context Mapping)
- Tactical DDD (Aggregates, Entities, Value Objects)
- Event Sourcing con Marten
- CQRS (Command Query Responsibility Segregation)
- Multi-tenancy (schema-per-tenant)
- GraphQL API

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

### Boss Battle
50 pazienti attivi, piani complessi, tracking giornaliero. **Reward: +500 XP**

---

## 📅 PROGETTO 3: BookingHub (Mesi 10-14)

### Obiettivo
Sistema prenotazioni per studi professionali. Calendar sync, pagamenti, notifiche.

### Stack
- .NET 8 + Aspire
- PostgreSQL, Redis
- MassTransit (Saga)
- Azure Kubernetes Service (AKS)
- Stripe, Google Calendar, Microsoft Graph

### Cosa Impari
- Saga Pattern (Orchestration)
- Compensating transactions
- External service integration
- Kubernetes deployment
- Full observability (OpenTelemetry, Grafana)
- Production operations

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

### Boss Battle
100 prenotazioni simultanee con failure scenarios. **Reward: +500 XP**

---

## 💰 PROGETTO 4: FamilyBudget (Mesi 15-18)

### Obiettivo
App mobile per budget familiare. Offline-first, sync, real-time.

### Stack
- Flutter (mobile)
- .NET 8 (backend)
- PostgreSQL, Redis
- SignalR (real-time)
- Notification Service (riuso P1!)

### Cosa Impari
- Flutter development
- Offline-first architecture
- Sync protocols
- Conflict resolution
- Real-time con SignalR
- Mobile deployment (App Store, Play Store)

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

### Boss Battle
4 persone offline, modifiche concorrenti, sync corretto. **Reward: +500 XP**

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

Alla fine dei 18 mesi:

- [ ] Clean Architecture
- [ ] Event-driven design
- [ ] DDD (Strategic + Tactical)
- [ ] CQRS + Event Sourcing
- [ ] Saga Pattern
- [ ] Kubernetes deployment
- [ ] Full observability
- [ ] Infrastructure as Code (Terraform)
- [ ] C4 documentation
- [ ] ADR writing
- [ ] API design (REST, GraphQL)
- [ ] Mobile (Flutter basics)
- [ ] Offline-first architecture
- [ ] **AI Integration (Ollama, RAG, function calling)** 🤖
- [ ] **AI-Native system design** 🤖

---

*Ultimo aggiornamento: 2025-01-29*