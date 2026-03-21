/* ═══════════════════════════════════════════════════════════
   FILE 1: claude/context/tech-stack.md
   ═══════════════════════════════════════════════════════════ */

# 🛠️ Tech Stack Reference

## Backend

| Tecnologia | Versione | Note |
|------------|----------|------|
| .NET | 8 | NON versioni precedenti |
| C# | 12 | |
| Entity Framework Core | 8 | |
| MediatR | Latest | Per CQRS |
| FluentValidation | Latest | |
| AutoMapper | Latest | |
| Serilog | Latest | Logging |
| Polly | Latest | Resilience |
| MassTransit | Latest | Message bus, Sagas |

## Frontend

| Tecnologia | Note |
|------------|------|
| React | 18 |
| TypeScript | Strict mode |
| Redux Toolkit | NON Zustand! Dan lo conosce già |
| RTK Query | Per API calls |
| React Hook Form + Zod | Forms |
| Tailwind CSS | Styling |
| Vite | Build tool |

## Data

| Tecnologia | Uso |
|------------|-----|
| SQL Server | Primary DB (Senior path) |
| PostgreSQL | Primary DB (Architect path) |
| Redis | Caching → Pub/Sub → Primary DB |
| Marten | Event Sourcing in .NET |
| Elasticsearch | Full-text search |
| Meilisearch | Alternative search (più semplice) |

## Infrastructure

| Tecnologia | Uso |
|------------|-----|
| Docker | Containerization |
| Docker Compose | Local development |
| Kubernetes | Production (AKS) |
| Helm | K8s packaging |
| Terraform | Infrastructure as Code |
| GitHub Actions | CI/CD |

## Messaging

| Tecnologia | Uso |
|------------|-----|
| Azure Service Bus | Production |
| RabbitMQ | Local dev alternative |
| Redis Streams | Event streaming |

## Observability

| Tecnologia | Uso |
|------------|-----|
| OpenTelemetry | Instrumentation |
| Prometheus | Metrics |
| Grafana | Dashboards |
| Jaeger | Distributed tracing |
| Serilog + Seq | Logging |

## Testing

| Tecnologia | Uso |
|------------|-----|
| xUnit | Test framework |
| FluentAssertions | Assertions |
| Moq | Mocking |
| Testcontainers | Integration tests |
| k6 | Load testing |

---

/* ═══════════════════════════════════════════════════════════
   FILE 2: claude/context/learning-style.md
   ═══════════════════════════════════════════════════════════ */

# 🧠 Learning Style & Teaching Methodology

## Come Dan Impara Meglio

### Sequenza Preferita
1. **Contesto e problema** (10%) - Perché questo è importante
2. **Spiegazione concettuale** (15%) - Teoria con diagrammi/analogie
3. **Implementazione guidata** (50%) - Costruiamo insieme
4. **Pratica autonoma** (20%) - Esercizi da solo
5. **Review e refactor** (5%) - Cosa migliorare

### Principi Chiave

**Pattern Recognition > Memorizzazione**
```
❌ "Ecco il Factory Pattern, memorizzalo"
✅ "Hai un problema: devi creare notifiche diverse. 
    Proviamo prima la soluzione naive... vedi il problema?
    Il Factory Pattern lo risolve così..."
```

**Problem-First Learning**
```
1. Incontra problema reale
2. Prova soluzione naive
3. Vedi perché non scala
4. Introduci pattern/architettura
5. Refactora insieme
6. Capisce il "quando" usarlo
```

**Fail-Safe Environment**
- Può sbagliare senza giudizio
- Può dire "non ho capito"
- Può chiedere di rallentare
- Domande "stupide" benvenute

## Adattare la Difficoltà

### Task Facili (Dan conosce già)
- Spiegazione veloce
- Codice completo con commenti
- "Prova qualcosa di simile"
- Review rapido

### Task Medi (Nuovo ma simile)
- Contesto più profondo
- Costruire step-by-step
- Esercizi di estensione
- Review dettagliato

### Task Difficili (Completamente nuovo)
- Teoria estensiva prima
- Molte analogie ed esempi
- Baby steps nell'implementazione
- Molte domande di verifica
- Review approfondito

## Metodo Socratico

Preferire domande a risposte dirette:
- "Cosa succederebbe se...?"
- "Perché pensi che...?"
- "Come risolveresti...?"
- "Cosa potrebbe andare storto?"

---

/* ═══════════════════════════════════════════════════════════
   FILE 3: claude/context/gamification.md
   ═══════════════════════════════════════════════════════════ */

# 🎮 Sistema Gamification

## Overview

Il sistema usa XP, livelli, achievement e streak per mantenere la motivazione durante i 18 mesi di apprendimento.

## 📊 XP System

### Attività Quotidiane
| Attività | XP |
|----------|-----|
| Daily log completato | +10 |
| 30+ minuti studio | +20 |
| 1+ ora studio | +40 |
| 2+ ore studio | +60 |
| Commit con progressi | +15 |

### Progressi Progetti
| Attività | XP |
|----------|-----|
| Task completato | +50 |
| Deliverable | +100 |
| Settimana completata | +150 |
| Progetto completato | +500 |
| Boss Battle vinta | +300 |

### Studio
| Attività | XP |
|----------|-----|
| Capitolo libro | +30 |
| Capitolo + appunti | +45 |
| Concetto documentato | +40 |
| ADR scritto | +75 |
| Diagramma C4 | +60 |

### Streak Bonus
| Streak | Bonus |
|--------|-------|
| 7 giorni | +100 |
| 14 giorni | +200 |
| 30 giorni | +500 |
| 60 giorni | +1000 |

## 🎚️ Livelli

| Lv | XP | Titolo |
|----|-----|--------|
| 1 | 0 | Apprentice Developer |
| 2 | 500 | Code Crafter |
| 3 | 1,200 | Pattern Seeker |
| 4 | 2,000 | Module Builder |
| 5 | 3,000 | Service Architect |
| 6 | 4,200 | Domain Master |
| 7 | 5,600 | System Designer |
| 8 | 7,200 | Cloud Engineer |
| 9 | 9,000 | Principal Developer |
| 10 | 11,000 | Staff Engineer |
| 11 | 15,000 | Senior Architect |
| 12 | 20,000 | AI-Native Architect 👑 |

## 🔥 Streak

Per mantenere lo streak serve UNO di:
- 30+ minuti di studio
- 1 commit con progressi
- 1 task completato

Nel daily log: `completed: true`

## 🏆 Achievement Tiers

- 🥉 Bronze: Primi passi
- 🥈 Silver: Competenze solide
- 🥇 Gold: Mastery
- 💎 Diamond: Elite
- 🌈 Secret: Sorprese

## 🤖 Coach Locale

Comandi:
```bash
python3 coach.py briefing  # Briefing giornaliero
python3 coach.py status    # XP, level, streak
python3 coach.py suggest   # Cosa studiare
python3 coach.py quiz      # Quiz su concetti
python3 coach.py add-xp N "motivo"
python3 coach.py streak    # Check streak
```