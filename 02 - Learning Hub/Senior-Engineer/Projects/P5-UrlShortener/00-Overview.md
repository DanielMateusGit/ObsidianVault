---
tags: [senior-engineer, project, p5, redis, performance]
status: locked
duration: 3 weeks
---

# 🔗 Progetto 5: URL Shortener with Analytics

## 📋 Overview
Sistema high-performance con Redis come database primario. Target: 1000+ req/sec.

**Durata:** 3 settimane | **Focus:** Redis as Primary DB, Performance, Minimal APIs

---

## 🎯 Obiettivo
Culminare tutto il Redis imparato in P1-P4. Ora Redis è il DATABASE PRIMARIO (no SQL!).

---

## 🛠️ Stack
- .NET 8 Minimal APIs
- Redis (PRIMARY database!)
- Redis Streams (analytics)
- HyperLogLog, Bloom filters, Sorted Sets

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| Redis as Primary DB | No SQL, tutto in Redis |
| Redis Data Structures | Strings, HyperLogLog, Bloom, Streams, Sorted Sets |
| High-Performance Design | 1000+ req/sec |
| Minimal APIs | Lightweight .NET endpoints |
| Base62 Encoding | Short URL generation |
| Real-time Analytics | Click tracking, unique visitors |

---

## 🗄️ Redis Data Structures

| Struttura | Uso |
|-----------|-----|
| **Strings** | URL mappings (shortcode → original) |
| **HyperLogLog** | Unique visitors (probabilistico, ~0.81% error) |
| **Bloom Filter** | Check esistenza URL (no false negatives) |
| **Streams** | Event log per analytics |
| **Sorted Sets** | Leaderboard URL popolari |

---

## 📅 Piano Settimane

### Week 1: Core + Redis
- [ ] Minimal API setup
- [ ] Redis come primary store
- [ ] URL shortening logic
- [ ] Base62 encoding
- [ ] Redirect endpoint
- [ ] Basic persistence

### Week 2: Analytics
- [ ] Redis Streams per click events
- [ ] HyperLogLog per unique visitors
- [ ] Real-time analytics dashboard
- [ ] Sorted Sets per leaderboard
- [ ] Bloom filter per URL existence check

### Week 3: Performance
- [ ] Load testing con k6/NBomber
- [ ] Optimization (connection pooling, pipelining)
- [ ] Target 1000+ req/sec
- [ ] Redis persistence strategies (RDB vs AOF)
- [ ] Benchmarking e profiling

---

## 📦 Deliverables

- [ ] URL shortener funzionante
- [ ] Redis come primary DB (no SQL!)
- [ ] Analytics real-time con HyperLogLog
- [ ] 1000+ req/sec verified
- [ ] Leaderboard URL popolari
- [ ] Click tracking con Streams

---

## ✅ Testing Checklist

- [ ] Unit tests - Shortening logic, Base62
- [ ] Integration tests - Redis operations
- [ ] Performance tests - 1000+ req/sec benchmark
- [ ] Analytics accuracy tests - HyperLogLog error margin

---

## 📈 Progressione Redis nel Percorso

```
P1 (Task Manager):     Redis = Cache
P1.5 (Auth):           Redis = Refresh Token Store
P2 (Chat):             Redis = Pub/Sub Backplane
P3 (E-commerce):       Redis = Distributed Locks
P4 (Alert Gateway):    Redis = Queue + Health
P5 (URL Shortener):    Redis = PRIMARY DATABASE 🎯
```

---

## 🎤 System Design Practice

Dopo P5, pratica spiegare **"Design a URL Shortener with Analytics"**:
- Functional: Shorten URL, redirect, click analytics, custom aliases
- Non-functional: 1000+ req/sec read, 100M URLs stored, real-time analytics
- Discussi: Base62 encoding, Redis as primary DB, HyperLogLog for unique visitors, read-heavy optimization, caching strategy

---

## 🏆 Boss Battle: "Feature Flags Service"

**Scenario:** Implementa un servizio di feature flags con targeting (Redis as primary DB + analytics).

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR per flag evaluation strategy (user targeting, % rollout) |
| **B. Implementazione** | Flag CRUD + user targeting + analytics (who saw what) |
| **C. Testing** | Performance tests per flag evaluation |
| **D. Performance** | Flag evaluation < 5ms, 2000+ req/sec |

---

## 🤖 AI Feature (Bonus): Smart Link Preview Generator

**Cosa fa:**
- Genera titolo e descrizione SEO-friendly per link
- Preview card automatica (come Twitter/LinkedIn)
- Categorizzazione automatica link

**Cosa Impari:**
- Web scraping + content extraction
- JSON mode / structured output
- Caching AI responses

---

*Ultimo aggiornamento: 2026-03-04*
