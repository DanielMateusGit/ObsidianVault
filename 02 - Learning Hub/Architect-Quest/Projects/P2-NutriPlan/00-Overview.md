---
tags: [architect-quest, project, p2, ddd, cqrs, event-sourcing]
status: locked
duration: 5 months
start: M5
end: M9
uses: [notification-service]
---

# 🥗 Progetto 2: NutriPlan

## 📋 Overview
Piattaforma SaaS per dietisti e pazienti. Piani alimentari, tracking, analytics.

**Durata:** 5 mesi (Mesi 5-9) | **Focus:** DDD, CQRS, Event Sourcing, Multi-tenancy

**Tipo:** Domain Project - Impara DDD/CQRS + integra Notification Service

---

## 🎯 Obiettivo
Padroneggiare DDD e Event Sourcing con scenari reali di gestione nutrizione.

---

## 🛠️ Stack
- .NET 8 + Aspire
- PostgreSQL + Marten (Event Sourcing)
- Meilisearch per search
- Azure AD B2C
- Blazor o React frontend
- **📧 Notification Service (P1)** per reminder e comunicazioni

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| Event Storming | Workshop collaborativo per domain discovery |
| Strategic DDD | Bounded Contexts, Context Mapping |
| Tactical DDD | Aggregates, Entities, Value Objects |
| Event Sourcing | Con Marten, audit trail completo |
| CQRS | Command Query Responsibility Segregation |
| Multi-tenancy | Schema-per-tenant |
| GraphQL API | Con HotChocolate |
| Service Integration | Consume Notification API |

---

## 🔗 Integrazione Notification Service

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

---

## 📅 Piano Mesi

### Mese 5: Domain Discovery
- [ ] W1-2: Event Storming completo
- [ ] W3-4: Context Mapping, Bounded Contexts

### Mese 6: Core Domain
- [ ] W5-6: Aggregate design (MealPlan)
- [ ] W7-8: Event Sourcing con Marten

### Mese 7: CQRS + Persistence
- [ ] W9-10: CQRS implementation, Read Models
- [ ] W11-12: Multi-tenancy

### Mese 8: API + Frontend
- [ ] W13-14: GraphQL API (HotChocolate)
- [ ] W15-16: Frontend MVP

### Mese 9: Polish + Production
- [ ] W17-18: Food database integration (ACL)
- [ ] W19-20: Deployment, Boss Battle

---

## 📦 Deliverables

- [ ] Event Storming documentation
- [ ] Bounded Contexts con Context Map
- [ ] Event Sourcing funzionante con Marten
- [ ] CQRS con read models
- [ ] Multi-tenant architecture
- [ ] GraphQL API
- [ ] Integration con Notification Service
- [ ] Frontend MVP

---

## ✅ Testing Checklist

- [ ] Unit tests - Aggregates, Commands, Queries
- [ ] Integration tests - Event Store persistence
- [ ] Multi-tenancy tests - Tenant isolation
- [ ] E2E test - Full meal plan flow

---

## 🏆 Boss Battle: "Fitness Tracker"

**Scenario:** Progetta un sistema per tracking workout con Event Sourcing (dominio diverso, stessi pattern DDD/CQRS).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (Event Sourcing vs CRUD), ADR-002 (aggregate boundaries), C4 Context + Container |
| **B. Domain Model** | Workout aggregate, Exercise VO, WorkoutCompletedEvent, read models |
| **C. API Spec** | GraphQL schema per query workout history + mutations |
| **D. Implementazione** | Aggiungi "Meal Photo Recognition" a NutriPlan (integration con AI Gateway) |

**Performance Goal:** 50 utenti attivi, tracking giornaliero, query < 100ms

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 🎤 System Design Practice

Dopo P2, pratica spiegare **"Design a Nutrition Tracking Platform"**:
- Functional: Meal plans, tracking, dietist-patient communication, analytics
- Non-functional: Multi-tenant, 1000+ dietists, eventual consistency OK
- Discussi: DDD bounded contexts, Event Sourcing for audit, CQRS trade-offs

---

*Ultimo aggiornamento: 2026-03-04*
