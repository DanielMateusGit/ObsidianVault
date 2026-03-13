---
tags: [architect-quest, project, p4, flutter, offline-first, sync]
status: locked
duration: 4 months
start: M15
end: M18
uses: [notification-service, ai-gateway]
---

# 💰 Progetto 4: FamilyBudget

## 📋 Overview
App mobile per budget familiare. Offline-first, sync, real-time.

**Durata:** 4 mesi (Mesi 15-18) | **Focus:** Flutter, Offline-first, Sync Protocols

**Tipo:** Domain Project - Impara Flutter/Offline + integra ENTRAMBI i servizi shared

---

## 🎯 Obiettivo
Costruire un'app mobile completa con architettura offline-first e sync robusto.

---

## 🛠️ Stack
- Flutter (mobile)
- .NET 8 (backend)
- PostgreSQL, Redis
- SignalR (real-time)
- **📧 Notification Service (P1)** per alert e reminder
- **🤖 AI Gateway (P2.5)** per categorizzazione e consigli

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| Flutter Development | UI, state management, local DB |
| Offline-first Architecture | Local-first, sync later |
| Sync Protocols | Conflict resolution, merge strategies |
| Conflict Resolution | Last-write-wins, CRDT concepts |
| Real-time | SignalR per sync live |
| Mobile Deployment | App Store, Play Store |
| Service Integration Mobile | SDK usage in Flutter |

---

## 🔗 Integrazione Notification Service

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

---

## 🔗 Integrazione AI Gateway

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

---

## 📅 Piano Mesi

### Mese 15: Flutter + Offline
- [ ] W1-2: Flutter basics, local DB (Drift)
- [ ] W3-4: Offline-first architecture

### Mese 16: Backend + Sync
- [ ] W5-6: Backend API con sync endpoint
- [ ] W7-8: Conflict resolution

### Mese 17: Real-time + AI Features
- [ ] W9-10: SignalR integration
- [ ] W11: AI expense categorization & queries
- [ ] W12: AI budget advisor

### Mese 18: Polish + Launch
- [ ] W13-14: UI polish, testing
- [ ] W15-16: Store preparation, Boss Battle

---

## 📦 Deliverables

- [ ] Flutter app funzionante
- [ ] Offline-first con local DB
- [ ] Sync protocol implementato
- [ ] Conflict resolution
- [ ] Real-time updates (SignalR)
- [ ] AI categorization
- [ ] AI budget advisor
- [ ] Push notifications integrate
- [ ] App Store / Play Store ready

---

## ✅ Testing Checklist

- [ ] Unit tests - Flutter widgets, business logic
- [ ] Integration tests - Sync protocol
- [ ] Offline tests - Full functionality offline
- [ ] Conflict tests - Concurrent modifications
- [ ] E2E test - Full expense tracking flow

---

## 🏆 Boss Battle: "Shared Shopping List"

**Scenario:** Progetta un'app per lista della spesa condivisa con offline-first e sync (dominio semplice, stessi pattern).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (conflict resolution strategy), ADR-002 (sync protocol), C4 Context + Container |
| **B. Domain Model** | ShoppingList aggregate, Item VO, sync events, conflict resolution rules |
| **C. API Spec** | OpenAPI per sync endpoint + WebSocket spec per real-time |
| **D. Implementazione** | Aggiungi "Receipt scanning con OCR" a FamilyBudget (AI-powered) |

**Performance Goal:** 4 utenti offline, modifiche concorrenti, sync senza perdita dati

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 🎤 System Design Practice

Dopo P4, pratica spiegare **"Design an Offline-First Mobile App"**:
- Functional: Expense tracking, budgets, shared access, AI suggestions
- Non-functional: Works offline, syncs when online, handles conflicts
- Discussi: Offline-first architecture, sync protocols, CRDT, mobile deployment

---

## 💡 Nota: Rispolverare Flutter

Dan ha esperienza Flutter (2021), basi solide. Questa è un'opportunità per:
- Rispolverare le basi
- Imparare le novità (Dart 3, Flutter 3.x)
- Applicare pattern architetturali moderni

---

*Ultimo aggiornamento: 2026-03-04*
