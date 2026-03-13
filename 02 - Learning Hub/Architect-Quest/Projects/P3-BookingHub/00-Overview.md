---
tags: [architect-quest, project, p3, saga, kubernetes, observability]
status: locked
duration: 5 months
start: M10
end: M14
uses: [notification-service, ai-gateway]
---

# 📅 Progetto 3: BookingHub

## 📋 Overview
Sistema prenotazioni per studi professionali. Calendar sync, pagamenti, notifiche.

**Durata:** 5 mesi (Mesi 10-14) | **Focus:** Saga Pattern, Kubernetes, Observability

**Tipo:** Domain Project - Impara Saga/K8s + integra ENTRAMBI i servizi shared

---

## 🎯 Obiettivo
Costruire un sistema distribuito con transazioni complesse, deployment Kubernetes, e full observability.

---

## 🛠️ Stack
- .NET 8 + Aspire
- PostgreSQL, Redis
- MassTransit (Saga)
- Azure Kubernetes Service (AKS)
- Stripe, Google Calendar, Microsoft Graph
- **📧 Notification Service (P1)** per conferme e reminder
- **🤖 AI Gateway (P2.5)** per assistente prenotazioni

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| Saga Pattern | Orchestration con MassTransit |
| Compensating Transactions | Rollback distribuito |
| External Service Integration | Calendar APIs, Payment APIs |
| Kubernetes | AKS deployment, Helm charts |
| Full Observability | OpenTelemetry, Grafana, Prometheus |
| Production Operations | SLI/SLO, alerting |
| Multi-Service Orchestration | Coordina Notification + AI Gateway |

---

## 🔗 Integrazione Notification Service

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

---

## 🔗 Integrazione AI Gateway

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

---

## 📅 Piano Mesi

### Mese 10: Domain + Saga
- [ ] W1-2: Event Storming, Saga design
- [ ] W3-4: Saga implementation con MassTransit

### Mese 11: Integrazioni
- [ ] W5-6: Calendar integration (Google, Outlook)
- [ ] W7-8: Payment integration (Stripe)

### Mese 12: Kubernetes
- [ ] W9-10: AKS setup con Terraform
- [ ] W11-12: Helm charts, Ingress, TLS

### Mese 13: Observability
- [ ] W13-14: OpenTelemetry, Grafana stack
- [ ] W15-16: Alerting, SLI/SLO

### Mese 14: AI Integration + Production
- [ ] W17: AI Assistant MVP (patient-facing, staff queries)
- [ ] W18: Smart scheduling con AI
- [ ] W19-20: Load testing, security audit, Boss Battle

---

## 📦 Deliverables

- [ ] Saga pattern funzionante (booking flow)
- [ ] Calendar sync (Google + Outlook)
- [ ] Payment processing (Stripe)
- [ ] Kubernetes deployment (AKS)
- [ ] Helm charts completi
- [ ] Full observability (traces, metrics, logs)
- [ ] SLI/SLO definiti
- [ ] AI Assistant per prenotazioni
- [ ] Integration con entrambi i servizi shared

---

## ✅ Testing Checklist

- [ ] Unit tests - Saga state machine
- [ ] Integration tests - External APIs (mocked)
- [ ] Chaos tests - Service failures, compensation
- [ ] E2E test - Full booking flow
- [ ] Load tests - Concurrent bookings

---

## 🏆 Boss Battle: "Event Ticketing System"

**Scenario:** Progetta un sistema di prenotazione biglietti eventi con Saga pattern (dominio diverso, stessi pattern).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (Saga orchestration vs choreography), ADR-002 (payment failure handling), C4 Context + Container |
| **B. Domain Model** | Ticket aggregate, Seat VO, BookingSaga state machine, compensating transactions |
| **C. API Spec** | OpenAPI per book ticket, cancel, refund |
| **D. Implementazione** | Aggiungi "Waitlist con notifica automatica" a BookingHub |

**Performance Goal:** 100 prenotazioni simultanee con failure scenarios gestiti correttamente

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 🎤 System Design Practice

Dopo P3, pratica spiegare **"Design a Booking System with Payments"**:
- Functional: Book appointments, calendar sync, payments, reminders
- Non-functional: 10K bookings/day, 99.9% availability, PCI compliance
- Discussi: Saga pattern, distributed transactions, Kubernetes scaling, observability

---

*Ultimo aggiornamento: 2026-03-04*
