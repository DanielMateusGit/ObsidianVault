---
tags: [learning, senior-engineer]
status: active
started: 2025-01-29
current_project: P1
current_week: W1
---

# 💻 Senior Engineer Path

> *Da mid-level a senior internazionale con progetti hands-on.*

## 🎯 Obiettivo (18 mesi)
- TDD e design patterns (QUANDO usarli)
- Esperto Redis
- CQRS e Event Sourcing
- Portfolio per aziende internazionali
- Target: €90k-130k remote

## 🗺️ I 7 Progetti

| # | Progetto | Focus | Durata | Status |
|---|----------|-------|--------|--------|
| 1 | [[Projects/P1-Task-Manager/00-Overview\|Task Manager]] | TDD, CQRS, Redis cache | 3 sett | 🟢 In corso |
| 1.5 | [[Projects/P1.5-Auth/00-Overview\|Auth & Security]] | JWT, OWASP, Refresh tokens | 1 sett | 🔒 |
| 2 | [[Projects/P2-Chat/00-Overview\|Real-Time Chat]] | SignalR, Redis Pub/Sub, React | 3 sett | 🔒 |
| 3 | [[Projects/P3-Ecommerce/00-Overview\|E-Commerce Cart]] | CQRS, Event Sourcing, Saga | 4 sett | 🔒 |
| 4 | [[Projects/P4-AlertGateway/00-Overview\|Alert Gateway]] | Microservices, RabbitMQ, Polly | 3 sett | 🔒 |
| 5 | [[Projects/P5-UrlShortener/00-Overview\|URL Shortener]] | Redis Primary DB, 1000+ req/sec | 3 sett | 🔒 |
| 6 | [[Projects/P6-Capstone/00-Overview\|Capstone]] | Everything + AI + K8s | 10 mesi | 🔒 |

## 🛠️ Stack
.NET 8, React, TypeScript, Redux Toolkit, SQL Server, Redis

---

## 🎯 APPROCCIO SENIOR ENGINEER

> **Focus:** 70% coding, 30% teoria. Dan scrive, Claude guida.

### Workflow per Argomento

```
1. Claude spiega brevemente il concetto
2. Domande di verifica (2-3)
3. Nota creata
4. TDD: Dan scrive test → rosso → codice → verde → refactor
5. ═══════════════════════════════════════════════════════
   ║  🎯 ESERCIZIO RECAP (Compartimento Stagno)          ║
   ║  - Claude dà specifica simile                       ║
   ║  - Dan fa TUTTO da solo (zero aiuto)                ║
   ║  - Claude valuta solo il risultato finale           ║
   ═══════════════════════════════════════════════════════
```

### 🏋️ Esercizi Recap - Regole

| Regola | Descrizione |
|--------|-------------|
| **Zero aiuto** | Claude non risponde a domande durante l'esercizio |
| **Isolato** | Può essere in cartella separata o nel progetto |
| **Tempo libero** | Nessun limite, ma tracciamo quanto ci metti |
| **Valutazione** | Claude corregge solo alla fine |

### 🎮 Gamification Esercizi

| Risultato | XP |
|-----------|-----|
| ✅ Esercizio completato correttamente | +50 |
| 🟡 Parzialmente corretto (fix minori) | +25 |
| ❌ Da rifare (errori concettuali) | +10 (per aver provato) |
| 🚀 Completato al primo tentativo | +25 bonus |
| ⚡ Completato in < 15 min | +15 bonus |

### Achievement Esercizi

| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 🏋️ | **First Solo** | Primo esercizio completato | +30 |
| 💪 | **Solo Streak** | 5 esercizi corretti consecutivi | +75 |
| 🎯 | **Perfect Form** | 10 esercizi al primo tentativo | +150 |
| 🏆 | **Independent Dev** | Tutti gli esercizi di un progetto | +200 |

---

## 📦 GIT & PUBBLICAZIONE

> Ogni progetto è pubblicato su GitHub come portfolio.

### Per ogni sessione

```bash
# Commit frequenti con messaggi chiari
git add .
git commit -m "feat(domain): add TaskItem entity with TDD"
```

### Struttura README (ogni progetto)

```markdown
# Project Name

## What I Learned
- [Concetto 1]
- [Concetto 2]

## Tech Stack
- .NET 8, xUnit, FluentAssertions, etc.

## How to Run
dotnet run --project src/ProjectName.Api

## Tests
dotnet test
```

### Commit Convention

| Prefisso | Uso |
|----------|-----|
| `feat` | Nuova feature |
| `test` | Aggiunta test |
| `refactor` | Refactoring |
| `docs` | Documentazione |
| `fix` | Bug fix |

---

[[Projects/P1-Task-Manager/00-Overview|▶️ Inizia Progetto 1]]
