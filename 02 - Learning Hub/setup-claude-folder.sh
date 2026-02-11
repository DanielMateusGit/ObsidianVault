#!/bin/bash

# 🎓 Learning Hub Setup Script
# Esegui: chmod +x setup-learning-hub.sh && ./setup-learning-hub.sh

BASE="/Users/Dan/Documents/Obsidian Vault/02 - Learning Hub"

echo "🎓 Creando struttura Learning Hub..."

# Crea cartelle
mkdir -p "$BASE/Daily"
mkdir -p "$BASE/Weekly"
mkdir -p "$BASE/Books"
mkdir -p "$BASE/Templates"
mkdir -p "$BASE/Architect-Quest/Projects/P1-Notification-Service/Architecture"
mkdir -p "$BASE/Architect-Quest/Projects/P1-Notification-Service/Tasks"
mkdir -p "$BASE/Architect-Quest/Projects/P1-Notification-Service/Notes"
mkdir -p "$BASE/Architect-Quest/Projects/P2-NutriPlan"
mkdir -p "$BASE/Architect-Quest/Projects/P3-BookingHub"
mkdir -p "$BASE/Architect-Quest/Projects/P4-FamilyBudget"
mkdir -p "$BASE/Senior-Engineer/Projects/P1-Task-Manager/Tasks"
mkdir -p "$BASE/Senior-Engineer/Projects/P1-Task-Manager/Notes"
mkdir -p "$BASE/Senior-Engineer/Projects/P2-Chat-App"
mkdir -p "$BASE/Senior-Engineer/Projects/P3-Ecommerce"
mkdir -p "$BASE/Senior-Engineer/Projects/P4-Notifications"
mkdir -p "$BASE/Senior-Engineer/Projects/P5-URL-Shortener"
mkdir -p "$BASE/Senior-Engineer/Projects/P6-Capstone"

echo "✅ Cartelle create"

# === ARCHITECT QUEST ===

cat > "$BASE/Architect-Quest/00-Overview.md" << 'EOF'
---
tags: [learning, architect-quest]
status: active
started: 2025-01-29
current_project: P1
current_week: W1
---

# 🏛️ Architect Quest

> *Diventare System Architect capace di progettare sistemi che AI agents possono implementare.*

## 🎯 Obiettivo (18 mesi)
- Progettare sistemi complessi da zero
- Documentazione C4, ADR, OpenAPI
- Cloud enterprise (Azure/Kubernetes)
- Dirigere AI per implementazione

## 🗺️ I 4 Progetti

| # | Progetto | Focus | Durata |
|---|----------|-------|--------|
| 1 | [[Projects/P1-Notification-Service/00-Overview\|Notification Service]] | Clean Arch, Event-driven | 4 mesi |
| 2 | [[Projects/P2-NutriPlan/00-Overview\|NutriPlan]] | DDD, CQRS, Event Sourcing | 5 mesi |
| 3 | [[Projects/P3-BookingHub/00-Overview\|BookingHub]] | Saga, Kubernetes | 5 mesi |
| 4 | [[Projects/P4-FamilyBudget/00-Overview\|FamilyBudget]] | Flutter, Offline-first | 4 mesi |

## 📚 Libri Chiave
- [ ] Designing Data-Intensive Applications - Kleppmann
- [ ] Fundamentals of Software Architecture - Richards & Ford
- [ ] Domain-Driven Design Distilled - Vernon
- [ ] Clean Architecture - Martin

[[Projects/P1-Notification-Service/00-Overview|▶️ Inizia Progetto 1]]
EOF

cat > "$BASE/Architect-Quest/Projects/P1-Notification-Service/00-Overview.md" << 'EOF'
---
tags: [architect-quest, project, p1]
status: not-started
---

# 🔔 Progetto 1: Sistema Notifiche

## 📋 Overview
Servizio che invia notifiche multi-canale (email, SMS, push, webhook) con retry, template, e tracking.

**Durata:** 4 mesi | **Focus:** Clean Architecture, Event-driven

## 🛠️ Stack
- .NET 8, PostgreSQL, Redis
- Azure Service Bus, Docker
- Terraform, GitHub Actions

## 📅 Timeline
| Mese | Focus |
|------|-------|
| 1 | Setup + Clean Architecture |
| 2 | Event-Driven + Canali |
| 3 | API + DevOps |
| 4 | Cloud + Production |

## 🏆 Boss Battle
10,000 notifiche in 5 min senza perdite = +500 XP

[[Tasks/Week-01|▶️ Inizia Week 1]]
EOF

cat > "$BASE/Architect-Quest/Projects/P1-Notification-Service/Tasks/Week-01.md" << 'EOF'
---
tags: [architect-quest, p1, week-01]
status: not-started
xp_available: 320
---

# 📅 Week 1: Project Setup

## 🎯 Obiettivo
Creare struttura Clean Architecture + ambiente dev.

## 📋 Tasks

### Setup (Day 1-2)
- [ ] Crea repo GitHub `notification-service`
- [ ] Solution .NET 8:
  - NotificationService.Domain
  - NotificationService.Application
  - NotificationService.Infrastructure
  - NotificationService.Api
- [ ] Docker Compose (PostgreSQL + Redis)

### Clean Architecture (Day 3-4)
- [ ] Definisci dipendenze tra progetti
- [ ] Scrivi ADR-001: "Perché Clean Architecture"

### Docs (Day 5)
- [ ] README.md
- [ ] C4 Context Diagram

## 📖 Letture
- [ ] "Clean Architecture" Cap. 1-14
- [ ] "A Philosophy of Software Design" Cap. 1-5

## ✅ XP
| Deliverable | XP |
|-------------|-----|
| Repo + struttura | +50 |
| Docker Compose | +50 |
| ADR-001 | +75 |
| C4 Diagram | +60 |
| README | +25 |
| Letture | +60 |

[[Week-02|Week 2 →]]
EOF

echo "✅ Architect Quest creato"

# === SENIOR ENGINEER ===

cat > "$BASE/Senior-Engineer/00-Overview.md" << 'EOF'
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

## 🗺️ I 6 Progetti

| # | Progetto | Focus | Durata |
|---|----------|-------|--------|
| 1 | [[Projects/P1-Task-Manager/00-Overview\|Task Manager]] | TDD, Redis basics | 2 sett |
| 2 | [[Projects/P2-Chat-App/00-Overview\|Chat App]] | SignalR, Pub/Sub | 3 sett |
| 3 | [[Projects/P3-Ecommerce/00-Overview\|E-Commerce]] | CQRS, Event Sourcing | 4 sett |
| 4 | [[Projects/P4-Notifications/00-Overview\|Notifications]] | Microservices | 3 sett |
| 5 | [[Projects/P5-URL-Shortener/00-Overview\|URL Shortener]] | Redis Primary DB | 3 sett |
| 6 | [[Projects/P6-Capstone/00-Overview\|Capstone]] | Everything | 6 mesi |

## 🛠️ Stack
.NET 8, React, TypeScript, Redux Toolkit, SQL Server, Redis

[[Projects/P1-Task-Manager/00-Overview|▶️ Inizia Progetto 1]]
EOF

cat > "$BASE/Senior-Engineer/Projects/P1-Task-Manager/00-Overview.md" << 'EOF'
---
tags: [senior-engineer, project, p1]
status: not-started
---

# ✅ Progetto 1: Task Manager API

## 📋 Overview
REST API per task con TDD, caching Redis, design patterns.

**Durata:** 2 settimane | **Focus:** Clean Arch, TDD, Patterns

## 🎯 Cosa Imparerai
- Clean Architecture
- TDD (Red → Green → Refactor)
- Repository, Factory, Strategy patterns
- Redis caching

## ✅ Features
- [ ] CRUD Task
- [ ] Categorie e priorità
- [ ] Filtering/sorting
- [ ] Redis cache
- [ ] 80%+ test coverage

## 🎨 Patterns
| Pattern | Problema |
|---------|----------|
| Repository | Astrae accesso dati |
| Factory | Crea task diversi |
| Strategy | Prioritizzazione |

[[Tasks/Week-01|▶️ Inizia Week 1]]
EOF

echo "✅ Senior Engineer creato"

# === TEMPLATES ===

cat > "$BASE/Templates/Daily-Template.md" << 'EOF'
---
tags: [daily]
date: {{date:YYYY-MM-DD}}
completed: false
hours: 0
minutes: 0
xp_earned: 0
focus: ""
---

# 📅 {{date:dddd, DD MMMM YYYY}}

## 🎯 Focus
- [ ] 

## ⏱️ Sessioni
| Progetto | Tempo | Attività |
|----------|-------|----------|
| | min | |

## ✅ Completato
- [ ] 

## 📖 Imparato
> 

## ⭐ XP
| Attività | XP |
|----------|-----|
| | |
| **TOTALE** | 0 |

**Streak:** 30+ min? → `completed: true`
EOF

cat > "$BASE/Templates/Weekly-Template.md" << 'EOF'
---
tags: [weekly]
week: {{date:YYYY-[W]WW}}
total_xp: 0
---

# 📆 Week {{date:WW}}

## 📊 Stats
| Ore | XP | Streak |
|-----|-----|--------|
| | | /7 |

## ✅ Completato
- 

## 🔍 Retrospettiva
**Bene:** 
**Migliorare:** 

## 🎯 Prossima Settimana
- [ ] 
EOF

cat > "$BASE/Templates/ADR-Template.md" << 'EOF'
---
tags: [adr]
status: proposed
date: {{date:YYYY-MM-DD}}
---

# ADR-XXX: [Titolo]

## Status
Proposed

## Context
_Problema?_

## Decision
_Decisione?_

## Consequences
**Pro:** 
**Contro:** 
EOF

echo "✅ Templates creati"

echo ""
echo "🎉 FATTO! Struttura completa creata."
echo ""
echo "Prossimi passi:"
echo "1. Apri Obsidian e verifica la struttura"
echo "2. Configura Periodic Notes per usare i template"
echo "3. Esegui: python3 coach.py check"
echo ""