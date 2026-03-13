---
tags: [architect-quest, project, p5, capstone, real-project, monetization]
status: locked
duration: 4 months
start: M19
end: M22
uses: [notification-service, ai-gateway, nutriplan-patterns, bookinghub-patterns, familybudget-patterns]
monetization: 5-stars
---

# 🏋️ Progetto 5: FitHub - CAPSTONE REALE

## 📋 Overview
App fitness multi-versione (Yoga/Stretching, CrossFit, Palestra) con AI e subscription.

**Durata:** 4 mesi (Mesi 19-22) | **Focus:** TUTTO + White-label + Monetizzazione

**Tipo:** CAPSTONE REALE - Unisce TUTTO quello imparato. Progetto monetizzabile!

---

## 🎯 Obiettivo
Costruire un prodotto REALE che Dan può proporre alla palestra dove lavora!

### Business Model
- **B2B:** Palestre come clienti (gestione allenatori, turni, abbonamenti)
- **B2C:** Utenti singoli (allenamento casa, tracking progressi)
- **White-label:** Una codebase, multiple skin per mercati verticali

---

## 🛠️ Stack
- .NET 8 + Aspire (backend)
- PostgreSQL + Redis
- Azure Service Bus (events)
- **📧 Notification Service (P1)** per reminder e comunicazioni
- **🤖 AI Gateway (P2.5)** per workout planning e consigli
- Multi-tenant architecture (da P3)
- Subscription billing (Stripe)

---

## 📚 Cosa Imparerai (Consolidamento)

| Topic | Dettaglio | Da Progetto |
|-------|-----------|-------------|
| Multi-tenant | Schema-per-tenant avanzato | P3 BookingHub |
| White-label | Stessa codebase, diverse UI/branding | Nuovo |
| AI Workout Planning | Generazione personalizzata | P2.5 AI Gateway |
| Subscription Management | Piani, billing, trial | P3 BookingHub |
| Role-based Access | Owner, coach, member | Nuovo |
| Product Development | Da progetto a prodotto | Nuovo |

---

## 🏗️ Architettura Cross-Progetto

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

---

## 🎨 Versioni White-label

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

---

## 🔗 Integrazione Notification Service

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

---

## 🔗 Integrazione AI Gateway

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

---

## 📅 Piano Mesi

### Mese 19: Architecture & Core
- [ ] W1-2: Multi-tenant setup, tenant isolation
- [ ] W3-4: Core domain (Workout, Exercise, Member, Coach, Subscription)

### Mese 20: Features & AI
- [ ] W5-6: AI workout generation (usa AI Gateway)
- [ ] W7-8: Subscription management, billing (Stripe)

### Mese 21: White-label & Roles
- [ ] W9-10: White-label infrastructure (theming, feature flags)
- [ ] W11-12: Coach dashboard, member app, owner analytics

### Mese 22: Polish & Launch
- [ ] W13-14: Integration tests, load testing
- [ ] W15: Documentation, deployment
- [ ] W16: Boss Battle + **PROPONI ALLA TUA PALESTRA!** 💰

---

## 📦 Deliverables

- [ ] Multi-tenant backend completo
- [ ] AI workout generation funzionante
- [ ] Subscription billing con Stripe
- [ ] 3 skin white-label (Yoga, CrossFit, Gym)
- [ ] Coach + Member + Owner dashboards
- [ ] Integration con Notification Service
- [ ] Integration con AI Gateway
- [ ] **PROPOSTA COMMERCIALE per la tua palestra!** 💰

---

## 🏆 Boss Battle: "Gym Chain Platform"

**Scenario:** Estendi FitHub per supportare catene di palestre (multi-location).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (tenant hierarchy: chain → location → member), C4 Context + Container |
| **B. Domain Model** | Chain aggregate, Location VO, cross-location membership |
| **C. API Spec** | OpenAPI per chain management, location analytics |
| **D. Implementazione** | Cross-location member transfer feature |

**Performance Goal:** 5 locations, 100 members each, real-time sync

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 💰 Piano Monetizzazione

| Modello | Prezzo Indicativo | Target |
|---------|-------------------|--------|
| **Palestra singola** | €50-100/mese | Box CrossFit, studi yoga |
| **Multi-location** | €200-500/mese | Catene palestre |
| **Enterprise** | Custom | Grandi franchising |
| **Utente singolo** | €5-10/mese o freemium | Home fitness |

### Revenue Potenziale
```
Anno 1: 5 palestre × €100/mese = €6.000/anno
Anno 3: 50 palestre × €150/mese = €90.000/anno
```

---

## 🎯 Perché Questo Progetto è Speciale

1. **È REALE** - Dan può proporlo alla palestra dove lavora
2. **È MONETIZZABILE** - Revenue potenziale concreta
3. **UNISCE TUTTO** - Tutti i pattern e servizi costruiti
4. **È PORTFOLIO** - Dimostra capacità end-to-end
5. **È SCALABILE** - White-label per espandersi

---

## ❤️ Connessione al WHY

Questo progetto può contribuire direttamente agli obiettivi di Dan:
- 🏡 Revenue extra per la casa
- 💰 Business proprio, non solo stipendio
- 🚀 Libertà finanziaria

---

*Ultimo aggiornamento: 2026-03-04*
