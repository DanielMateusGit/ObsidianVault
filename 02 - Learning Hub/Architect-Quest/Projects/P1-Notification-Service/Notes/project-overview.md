o# Notification Service - Panoramica Progetto

> **Data:** 2026-02-02
> **Progetto:** P1 - Architect Quest
> **Durata:** 4 mesi

---

## Il Problema

Applicazioni diverse (e-commerce, mobile, banking) devono inviare notifiche agli utenti.

**Senza un servizio centralizzato:**
```
App E-commerce ──► Chiama SendGrid direttamente
App Mobile ──► Chiama Firebase direttamente
App Banking ──► Chiama Twilio direttamente
```

**Problemi:**
- Ogni app gestisce retry, fallimenti, template separatamente
- Duplicazione di logica
- Impossibile tracciare globalmente
- Se un provider va giù, tutto si blocca

---

## La Soluzione: Notification Service

Un servizio **centralizzato** che gestisce tutte le notifiche.

```
┌─────────────┐     ┌─────────────────────────┐     ┌──────────────┐
│ E-commerce  │────►│                         │────►│   SendGrid   │
├─────────────┤     │   NOTIFICATION SERVICE  │     ├──────────────┤
│ Mobile App  │────►│                         │────►│   Twilio     │
├─────────────┤     │   • Riceve richieste    │     ├──────────────┤
│ Banking App │────►│   • Applica template    │────►│   Firebase   │
└─────────────┘     │   • Invia al canale     │     ├──────────────┤
                    │   • Gestisce retry      │────►│   Webhook    │
                    │   • Traccia delivery    │     └──────────────┘
                    └─────────────────────────┘
```

---

## Funzionalità da Implementare

| Feature | Descrizione | Mese |
|---------|-------------|------|
| **Multi-canale** | Email, SMS, Push, Webhook | 2 |
| **Template Engine** | Variabili dinamiche (Scriban) | 2 |
| **Retry con backoff** | 1min → 5min → 15min | 2 |
| **Dead Letter Queue** | Notifiche fallite per analisi | 2 |
| **Tracking** | pending → sent → delivered/failed | 1-2 |
| **API REST** | `POST /api/notifications` | 3 |
| **Scheduling** | Invio programmato | 3 |
| **CI/CD** | GitHub Actions | 3 |
| **Terraform** | Infrastructure as Code | 4 |
| **Azure Deploy** | Produzione | 4 |

---

## Esempio di Utilizzo

### Request
```http
POST /api/notifications
Content-Type: application/json

{
  "channel": "email",
  "recipient": "dan@example.com",
  "template": "order_confirmation",
  "data": {
    "nome": "Dan",
    "ordine_id": "ORD-12345",
    "totale": "€129.99"
  },
  "schedule_at": null
}
```

### Response
```json
{
  "id": "notif_abc123",
  "status": "pending",
  "channel": "email",
  "created_at": "2026-02-02T21:30:00Z"
}
```

### Template (Scriban)
```
Ciao {{nome}},

Il tuo ordine {{ordine_id}} è stato confermato.
Totale: {{totale}}

Grazie per l'acquisto!
```

---

## Stack Tecnologico

| Componente | Tecnologia | Perché |
|------------|------------|--------|
| **Backend** | .NET 8 | Moderno, performante, familiare |
| **Database** | PostgreSQL 16 | Open source, ottimo per cloud |
| **Cache** | Redis 7 | Caching, Pub/Sub, Queue |
| **Message Queue** | Azure Service Bus | Enterprise, retry built-in |
| **Template** | Scriban | Veloce, sicuro, Liquid-like |
| **Container** | Docker | Ambiente consistente |
| **IaC** | Terraform | Infrastructure as Code |
| **CI/CD** | GitHub Actions | Integrato con repo |
| **Cloud** | Azure | Familiare, enterprise |

---

## Boss Battle

> **10,000 notifiche in 5 minuti senza perdite**

Questo test ci obbliga a costruire:
- Sistema scalabile (message queue)
- Resilienza (retry, dead letter)
- Osservabilità (metriche, logging)

**Reward:** +500 XP

---

## Cosa Imparo con Questo Progetto

| Concetto | Applicazione |
|----------|--------------|
| Clean Architecture | Struttura 4 layer |
| Event-Driven | Message queue per disaccoppiare |
| Retry Patterns | Gestione fallimenti con backoff |
| Template Engine | Scriban/Liquid |
| Docker/Compose | Ambiente dev |
| CI/CD | GitHub Actions pipeline |
| Terraform | Azure infrastructure |
| C4 Diagrams | Documentazione architetturale |
| ADR | Documentare decisioni |

---

## Timeline

| Mese | Focus | Settimane |
|------|-------|-----------|
| **1** | Setup + Clean Architecture | W1-W4 |
| **2** | Event-Driven + Canali | W5-W8 |
| **3** | API + DevOps | W9-W12 |
| **4** | Cloud + Production | W13-W16 |

---

## Repo

**GitHub:** https://github.com/DanielMateusGit/notification-service

---

*Creato durante sessione Week 1 - 2026-02-02*
