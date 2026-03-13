---
tags: [senior-engineer, project, p3, cqrs, event-sourcing]
status: locked
duration: 4 weeks
---

# 🛒 Progetto 3: E-Commerce Cart & Inventory

## 📋 Overview
Sistema carrello e inventario con CQRS, Event Sourcing, gestione concorrenza.

**Durata:** 4 settimane | **Focus:** CQRS, Event Sourcing, Saga, Distributed Locks

---

## 🎯 Obiettivo
Padroneggiare CQRS e Event Sourcing con scenari reali di concorrenza.

---

## 🛠️ Stack
- .NET 8 + MediatR
- EventStore o Marten
- Redis (distributed locks)
- SQL Server (read models)

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| CQRS | Command Query Responsibility Segregation |
| Event Sourcing | Audit trail completo, rebuild state |
| Saga Pattern | Transazioni distribuite |
| Distributed Locking | Redis per concurrency |
| Optimistic Concurrency | Gestione conflitti |
| Eventual Consistency | Trade-offs |

---

## 🎨 Patterns

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Command** | Separa richieste da esecuzione |
| **CQRS** | Ottimizza read e write separatamente |
| **Event Sourcing** | Audit trail completo, rebuild state |
| **Saga** | Transazioni distribuite |

---

## 📅 Piano Settimane

### Week 1: CQRS Basics
- [ ] MediatR setup avanzato
- [ ] Commands e Queries separati
- [ ] Read/Write models
- [ ] Projections

### Week 2: Event Sourcing
- [ ] Event store setup (EventStore o Marten)
- [ ] Cart aggregate con eventi
- [ ] Event replay
- [ ] Snapshots per performance

### Week 3: Concurrency + Inventory
- [ ] Redis distributed locks
- [ ] Inventory management
- [ ] Optimistic concurrency
- [ ] Stock reservation

### Week 4: Saga + Polish
- [ ] Checkout saga
- [ ] Compensation logic
- [ ] Integration tests
- [ ] Load testing

---

## 📦 Deliverables

- [ ] CQRS funzionante
- [ ] Event Sourcing con replay
- [ ] Distributed locking
- [ ] Saga per checkout
- [ ] Inventory con stock management
- [ ] Concurrency handling

---

## ✅ Testing Checklist

- [ ] Unit tests - Aggregates, Commands, Queries
- [ ] Integration tests - Event Store persistence
- [ ] Concurrency tests - Distributed locks
- [ ] E2E test - Full checkout flow

---

## 🎤 System Design Practice

Dopo P3, pratica spiegare **"Design an E-Commerce Cart & Inventory System"**:
- Functional: Add to cart, checkout, inventory tracking, order history
- Non-functional: 100K products, handle flash sales (10K concurrent), eventual consistency OK
- Discussi: CQRS trade-offs, Event Sourcing for audit, distributed locks for inventory, saga pattern for checkout

---

## 🏆 Boss Battle: "Auction System"

**Scenario:** Implementa un sistema di aste con bidding (CQRS + Event Sourcing + concurrency).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per bid conflict resolution |
| **B. Implementazione** | Auction aggregate, Bid events, auto-close, winner selection |
| **C. Testing** | Concurrency tests (100 bids simultanei su stessa auction) |
| **D. Performance** | Bid processing < 50ms, no lost bids |

---

## 🤖 AI Feature (Bonus): Product Recommendations

**Cosa fa:**
- "Chi ha comprato X ha comprato anche Y"
- Recommendations basate su embeddings prodotti
- "Prodotti simili" usando similarity search

**Cosa Impari:**
- Embeddings per prodotti (testo → vettore)
- Similarity search con vector DB
- Caching embeddings per performance

---

*Ultimo aggiornamento: 2026-03-04*
