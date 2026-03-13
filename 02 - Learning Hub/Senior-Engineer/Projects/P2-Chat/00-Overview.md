---
tags: [senior-engineer, project, p2, signalr, realtime]
status: locked
duration: 3 weeks
---

# 💬 Progetto 2: Real-Time Chat

## 📋 Overview
Applicazione chat real-time scalabile a 1000+ utenti concorrenti.

**Durata:** 3 settimane | **Focus:** SignalR, Redis Pub/Sub, React

---

## 🎯 Obiettivo
Costruire un sistema real-time scalabile con WebSocket e Redis backplane.

---

## 🛠️ Stack
- .NET 8 + SignalR
- Redis (Pub/Sub, backplane)
- React + TypeScript
- SQL Server

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| SignalR | Real-time bidirectional communication |
| Redis Pub/Sub | Message distribution tra server |
| WebSocket Scaling | Horizontal scaling con backplane |
| Observer Pattern | Notify subscribers di nuovi messaggi |
| Presence | Chi è online |
| React + TypeScript | Frontend moderno |

---

## 🎨 Patterns

| Pattern | Problema che Risolve |
|---------|---------------------|
| **Observer** | Notifica subscribers di nuovi messaggi |
| **Pub/Sub** | Distribuzione messaggi tra server |

---

## 📅 Piano Settimane

### Week 1: SignalR Basics
- [ ] Setup SignalR hub
- [ ] Basic chat functionality
- [ ] Message persistence
- [ ] Connection management

### Week 2: Redis + Scaling
- [ ] Redis backplane per scaling
- [ ] Redis Pub/Sub
- [ ] Presence (chi è online)
- [ ] Group chat
- [ ] Message history

### Week 3: Frontend + Polish
- [ ] React + TypeScript frontend
- [ ] UI completa
- [ ] Typing indicators
- [ ] Read receipts
- [ ] Load testing 1000+ users

---

## 📦 Deliverables

- [ ] Chat funzionante real-time
- [ ] Scala a 1000+ utenti
- [ ] Frontend React completo
- [ ] Redis Pub/Sub implementato
- [ ] Presence system
- [ ] Message persistence

---

## ✅ Testing Checklist

- [ ] Unit tests - Hub logic
- [ ] Integration tests - SignalR connections (TestServer)
- [ ] Load test - 1000 concurrent connections (k6/NBomber)

---

## 🎤 System Design Practice

Dopo P2, pratica spiegare **"Design a Real-Time Chat System"**:
- Functional: 1:1 chat, group chat, presence, message history
- Non-functional: 1000+ concurrent users, < 100ms delivery latency
- Discussi: WebSocket vs polling, Redis backplane, message ordering, horizontal scaling

---

## 🏆 Boss Battle: "Live Notification Feed"

**Scenario:** Implementa un feed di notifiche real-time (simile a chat, focus su broadcast).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per notification fanout strategy |
| **B. Implementazione** | SignalR hub + Redis Pub/Sub + notification types + read/unread |
| **C. Testing** | Load test 500 concurrent connections |
| **D. Performance** | Notification delivery < 100ms to all subscribers |

---

## 🤖 AI Feature (Bonus): Message Summarization

**Cosa fa:**
- Riassume conversazioni lunghe per chi entra tardi
- "Catch up" button: "Negli ultimi 50 messaggi si è parlato di..."
- Highlight messaggi importanti automaticamente

**Cosa Impari:**
- Streaming responses
- Chunking conversazioni lunghe
- Context window management

---

*Ultimo aggiornamento: 2026-03-04*
