---
tags: [architect-quest, p1, week-01]
status: completed
xp_available: 320
xp_earned: 175
---

# 📅 Week 1: Project Setup

## 🎯 Obiettivo
Creare struttura Clean Architecture + ambiente dev.

## 📋 Tasks

### Setup (Day 1-2)
- [x] Crea repo GitHub `notification-service` ✅ 2026-02-02
- [x] Solution .NET 8: ✅ 2026-02-02
  - NotificationService.Domain
  - NotificationService.Application
  - NotificationService.Infrastructure
  - NotificationService.Api
- [x] Docker Compose (PostgreSQL + Redis) ✅ 2026-02-02
- [x] Dipendenze tra progetti configurate ✅ 2026-02-02

### Clean Architecture (Day 3-4)
- [x] Definisci dipendenze tra progetti ✅ 2026-02-02
- [x] Scrivi ADR-001: "Perché Clean Architecture" ✅ 2026-02-02

### Docs (Day 5)
- [x] README.md ✅ 2026-02-03
- [x] C4 Context Diagram ✅ 2026-02-03

## 📖 Letture
- [x] "Clean Architecture" Cap. 1-14 (overview + quiz) ✅ 2026-02-03
- [x] "A Philosophy of Software Design" Cap. 1-5 (overview + quiz) ✅ 2026-02-03

## 📝 Note di Sessione

### 2026-02-02 - Prima Sessione
**Durata:** ~1.5h
**XP guadagnati:** +100

**Completato:**
- Creata solution .NET 8 con 4 progetti Clean Architecture
- Configurate dipendenze corrette (Domain ← Application ← Infrastructure, Api → All)
- Docker Compose con PostgreSQL 16 + Redis 7 (testati e funzionanti)
- Repo GitHub: https://github.com/DanielMateusGit/notification-service
- Installato GitHub CLI (`gh`)

**Appreso:**
- Clean Architecture: 4 layer, Dependency Rule
- Violazioni comuni da evitare
- Scopo del Notification Service

**Appunti creati:**
- [[Notes/clean-architecture|Clean Architecture]]
- [[Notes/project-overview|Project Overview]]

## ✅ XP
| Deliverable | XP | Status |
|-------------|-----|--------|
| Repo + struttura | +50 | ✅ Fatto |
| Docker Compose | +50 | ✅ Fatto |
| ADR-001 | +75 | ✅ Fatto |
| C4 Diagram | +60 | ✅ Fatto |
| README | +25 | ✅ Fatto |
| Letture | +60 | ✅ Fatto |

**Totale guadagnato:** 320 / 320 XP ✅ WEEK 1 COMPLETATA!

[[Week-02|Week 2 →]]
