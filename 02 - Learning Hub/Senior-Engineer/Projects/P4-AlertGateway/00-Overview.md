---
tags: [senior-engineer, project, p4, microservices, resilience]
status: locked
duration: 3 weeks
---

# 🚨 Progetto 4: Alert Gateway

## 📋 Overview
Sistema di alerting multi-canale con microservices, message queue, circuit breaker.

**Durata:** 3 settimane | **Focus:** Microservices, Resilience Patterns, RabbitMQ

---

## 🎯 Obiettivo
Costruire un sistema distribuito resiliente con multiple services comunicanti.

---

## 🛠️ Stack
- .NET 8 (multiple services)
- RabbitMQ
- Redis (queues, health tracking)
- Hangfire (background jobs)
- YARP (API Gateway)
- Polly (resilience)
- Docker Compose

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| Microservices | Service decomposition, bounded contexts |
| Message Queuing | RabbitMQ patterns |
| Circuit Breaker | Gestisce fallimenti di servizi esterni |
| Retry Policies | Exponential backoff |
| Bulkhead | Isola fallimenti |
| API Gateway | Single entry point, routing |
| Health Checks | Readiness/liveness probes |
| Correlation IDs | Distributed tracing |

---

## 🎨 Patterns

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Circuit Breaker** | Gestisce fallimenti di servizi esterni |
| **Retry with Backoff** | Resilienza temporanea con exponential backoff |
| **Bulkhead** | Isola fallimenti per evitare cascading |
| **API Gateway** | Single entry point, routing |

---

## 📅 Piano Settimane

### Week 1: Service Decomposition
- [ ] Identificare bounded contexts
- [ ] Setup 3 services: Gateway, Processor, Sender
- [ ] RabbitMQ communication
- [ ] Docker Compose per local dev
- [ ] Basic message flow

### Week 2: Resilience Patterns
- [ ] Circuit Breaker con Polly
- [ ] Retry policies con exponential backoff
- [ ] Fallback strategies
- [ ] Bulkhead pattern
- [ ] Timeout policies

### Week 3: Gateway + Observability
- [ ] YARP API Gateway
- [ ] Health checks per ogni service
- [ ] Structured logging cross-service (correlation ID)
- [ ] End-to-end testing
- [ ] Chaos testing

---

## 📦 Deliverables

- [ ] 3+ microservices comunicanti
- [ ] RabbitMQ message queue
- [ ] Circuit breaker + retry + bulkhead
- [ ] API Gateway con routing
- [ ] Health checks su tutti i servizi
- [ ] Correlation ID per distributed tracing
- [ ] Docker Compose setup

---

## ✅ Testing Checklist

- [ ] Unit tests - Each service isolated
- [ ] Integration tests - RabbitMQ messaging
- [ ] Resilience tests - Chaos testing (service down)
- [ ] E2E test - Full alert flow through gateway

---

## 🔗 Differenza da Architect P1 (Notification Service)

```
ARCHITECT P1                          SENIOR P4 (Alert Gateway)
─────────────────────────────────────────────────────────────────
Focus: Clean Architecture             Focus: Microservices
Focus: Event-driven design            Focus: Resilience patterns
Focus: Single deployable              Focus: Multiple services
Output: ADR, C4, documentation        Output: Working distributed system
```

---

## 🎤 System Design Practice

Dopo P4, pratica spiegare **"Design an Alert/Notification Gateway"**:
- Functional: Multi-channel alerts (email, SMS, push), priority levels, retry logic
- Non-functional: 10K alerts/min, 99.9% delivery, graceful degradation
- Discussi: Circuit breaker pattern, message queue (RabbitMQ vs Kafka), API Gateway, bulkhead isolation, correlation IDs

---

## 🏆 Boss Battle: "Health Check Dashboard"

**Scenario:** Implementa un servizio di health monitoring per microservices.

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per health check aggregation strategy |
| **B. Implementazione** | Health collector service + Circuit breaker + alerting on degradation |
| **C. Testing** | Chaos tests (simula service down, verifica alerting) |
| **D. Performance** | Health check round-trip < 500ms per 10 services |

---

## 🤖 AI Feature (Bonus): Alert Triage & Grouping

**Cosa fa:**
- Classifica automaticamente severità alert
- Raggruppa alert correlati ("questi 5 alert sono lo stesso problema")
- Suggerisce root cause

**Cosa Impari:**
- Classification con LLM
- Semantic deduplication
- Pattern analysis con AI

---

*Ultimo aggiornamento: 2026-03-04*
