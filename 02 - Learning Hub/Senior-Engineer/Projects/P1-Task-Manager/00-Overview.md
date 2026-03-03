---
tags: [senior-engineer, project, p1]
status: in-progress
started: 2026-03-02
---

# ✅ Progetto 1: Task Manager API

## 📋 Overview
REST API per task con TDD, caching Redis, design patterns.

**Durata:** 2 settimane | **Focus:** Clean Arch, TDD, Patterns

## 🔴🟢🔵 APPROCCIO: TDD RIGOROSO

> **IMPORTANTE:** Questo progetto segue TDD rigoroso.
>
> 1. **🔴 RED** - Dan scrive il TEST prima
> 2. **🔴 RED** - Verifica che fallisce
> 3. **🟢 GREEN** - Dan scrive il CODICE minimo
> 4. **🟢 GREEN** - Verifica che passa
> 5. **🔵 REFACTOR** - Migliora insieme
>
> **MAI scrivere codice senza test che fallisce prima!**

## 📍 Percorso Codice
`/Projects/TaskManager/` (separato dalle note)

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

---

## 🎯 ESERCIZI RECAP

> Dopo ogni argomento TDD, Dan fa un esercizio simile **da solo**.

| # | Argomento | Esercizio | Status | XP |
|---|-----------|-----------|--------|-----|
| 1 | Entity (TaskItem) | Creare `Project` entity | ⬜ | - |
| 2 | Value Object (Priority) | Creare `DueDate` VO | ⬜ | - |
| 3 | Domain Events | Creare `TaskCompletedEvent` | ⬜ | - |
| 4 | Repository Pattern | Creare `IProjectRepository` | ⬜ | - |

---

## 📦 GIT

**Repository:** `/Projects/TaskManager/`

### Commit effettuati
| Data | Commit | Descrizione |
|------|--------|-------------|
| - | - | - |

---

[[Tasks/Week-01|▶️ Inizia Week 1]]
