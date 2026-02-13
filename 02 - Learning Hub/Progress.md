---
tags: [learning, progress, gamification]
xp: 1577
level: 3
title: "Pattern Seeker"
streak: 9
longest_streak: 9
architect_quest_week: "P1-W2"
senior_engineer_week: "P1-W1"
---

# 📈 Progress Tracker

## 👤 Status Attuale

| Stat | Valore |
|------|--------|
| **Level** | `=this.level` |
| **Title** | `=this.title` |
| **Total XP** | `=this.xp` |
| **Streak** | `=this.streak` giorni 🔥 |
| **Best Streak** | `=this.longest_streak` giorni |

---

## 🎚️ Sistema Livelli

| Lv | XP | Titolo | Status |
|----|-----|--------|--------|
| 1 | 0 | Apprentice Developer | ✅ |
| 2 | 500 | Code Crafter | |
| 3 | 1,200 | Pattern Seeker | |
| 4 | 2,000 | Module Builder | |
| 5 | 3,000 | Service Architect | |
| 6 | 4,200 | Domain Master | |
| 7 | 5,600 | System Designer | |
| 8 | 7,200 | Cloud Engineer | |
| 9 | 9,000 | Principal Developer | |
| 10 | 11,000 | Staff Engineer | |
| 11 | 15,000 | Senior Architect | |
| 12 | 20,000 | **AI-Native Architect** 👑 | |

---

## 📊 XP per Progetto

### 🏛️ Architect Quest
```dataviewjs
dv.paragraph("**Settimana corrente:** " + dv.current().architect_quest_week);
// XP totali da questo progetto verranno calcolati
```

### 💻 Senior Engineer
```dataviewjs
dv.paragraph("**Settimana corrente:** " + dv.current().senior_engineer_week);
```

---

## 🧮 Come Guadagni XP

### Attività Quotidiane
| Attività | XP |
|----------|-----|
| Daily log completato | +10 |
| 30+ minuti di studio | +20 |
| 1+ ora di studio | +40 |
| 2+ ore di studio | +60 |
| Commit con progressi | +15 |

### Progressi Progetti
| Attività | XP |
|----------|-----|
| Task completato | +50 |
| Deliverable completato | +100 |
| Settimana completata | +150 |
| Progetto completato | +500 |
| Boss Battle vinta | +300 |

### Studio e Documentazione
| Attività | XP |
|----------|-----|
| Capitolo libro letto | +30 |
| Capitolo + appunti | +45 |
| Concetto documentato | +40 |
| ADR scritto | +75 |
| Diagramma C4 | +60 |

### Coding
| Attività | XP |
|----------|-----|
| Test coverage >80% (modulo) | +50 |
| Deploy funzionante | +100 |
| Refactoring pulito | +40 |
| Bug fix in prod | +30 |

### Streak Bonus
| Streak | Bonus |
|--------|-------|
| 7 giorni | +100 |
| 14 giorni | +200 |
| 30 giorni | +500 |
| 60 giorni | +1000 |

### Side Quest
| Difficoltà | XP |
|------------|-----|
| ⭐ Easy | +50 |
| ⭐⭐ Medium | +100 |
| ⭐⭐⭐ Hard | +200 |

---

## 📝 XP History

> Aggiungi nuove entry in cima. L'agente può farlo automaticamente.

| Data | Attività | Progetto | XP | Totale |
|------|----------|----------|-----|--------|
| 2026-02-13 | 🎉 **Week 2 Completata!** | P1-W2 | +150 | 1577 |
| 2026-02-13 | 📄 README Domain Model overview (8f3a9f4) | P1-W2 | +25 | 1427 |
| 2026-02-13 | 📝 Nota Knowledge: Domain Events Theory | Sedimentazione | +20 | 1402 |
| 2026-02-13 | 📚 4 articoli Domain Events (Fowler, MS, Bogard, Jovanović) | P1-W2 | +60 | 1382 |
| 2026-02-13 | 🎯 Challenge EVT-01 (parziale) | Spaced Repetition | +7 | 1322 |
| 2026-02-12 | C4 Container Diagram ✅ (31e0abd) | P1-W2 | +20 | 1315 |
| 2026-02-12 | ADR-002: Rich vs Anemic Domain Model ✅ (804d8de) | P1-W2 | +30 | 1295 |
| 2026-02-11 | 🎉 LEVEL UP → Pattern Seeker (Lv.3) | - | - | 1265 |
| 2026-02-11 | 🔥 Achievement: On Fire (7 giorni streak) | - | +100 | 1265 |
| 2026-02-11 | Domain Events + 13 tests ✅ (d7eb134) | P1-W2 | +40 | 1165 |
| 2026-02-10 | Nota Domain Model Patterns (6 quiz) | P1-W2 | +20 | 1125 |
| 2026-02-10 | Value Objects (Email, Phone, Recipient) + 71 tests ✅ | P1-W2 | +50 | 1105 |
| 2026-02-10 | DeliveryAttempt entity + 24 tests ✅ | P1-W2 | +60 | 1055 |
| 2026-02-10 | Template entity + 39 tests ✅ | P1-W2 | +70 | 995 |
| 2026-02-10 | Challenge OCP-01 ✅ (Box 2→3) | Spaced Repetition | +15 | 925 |
| 2026-02-09 | Notification entity + 31 tests ✅ | P1-W2 | +80 | 910 |
| 2026-02-09 | Nota Entities + Clean Arch (cap 20-22) | P1-W2 | +60 | 830 |
| 2026-02-09 | Lettura Clean Architecture cap 20-22 | P1-W2 | +30 | 770 |
| 2026-02-09 | Challenge DIP-03 ✅ (Box 2→3) | Spaced Repetition | +15 | 740 |
| 2026-02-09 | 🎯 Kickoff Week 2: Domain Model | P1-W2 | - | 725 |
| 2026-02-06 | Quiz OCP 3/3 ✅ | Sedimentazione | +30 | 725 |
| 2026-02-06 | Nota OCP (architetturale) | Sedimentazione | +20 | 695 |
| 2026-02-06 | Nota SRP (architetturale) | Sedimentazione | +20 | 675 |
| 2026-02-06 | Challenge DIP-03 ✅ | Spaced Repetition | +15 | 655 |
| 2026-02-06 | Nota Facade Pattern + Quiz 3/3 | Sedimentazione | +30 | 640 |
| 2026-02-05 | 🧠 Achievement: Knowledge Seeker | Sedimentazione | +50 | 610 |
| 2026-02-05 | 2 Note Knowledge (Paradigms + DIP) | Sedimentazione | +40 | 560 |
| 2026-02-03 | 🎉 LEVEL UP → Code Crafter | - | - | 520 |
| 2026-02-03 | Letture (overview + quiz 4/4) | P1-W1 | +60 | 520 |
| 2026-02-03 | README.md + .env.example | P1-W1 | +25 | 460 |
| 2026-02-03 | 🔥 Achievement: Spark (3 giorni streak) | - | +50 | 435 |
| 2026-02-03 | 📐 Achievement: Architect Apprentice | - | +50 | 385 |
| 2026-02-03 | C4 Context Diagram | P1-W1 | +60 | 335 |
| 2026-02-02 | 🐳 Achievement: Docker Newbie | - | +50 | 275 |
| 2026-02-02 | 🌱 Achievement: First Commit | - | +50 | 225 |
| 2026-02-02 | ADR-001: Clean Architecture | P1-W1 | +75 | 175 |
| 2026-02-02 | Docker Compose (PostgreSQL + Redis) | P1-W1 | +50 | 100 |
| 2026-02-02 | Repo GitHub + struttura .NET 8 | P1-W1 | +50 | 50 |

---

## 📆 Weekly Stats

```dataviewjs
// Calcola XP dell'ultima settimana dai daily logs
const logs = dv.pages('"🎓 Learning-Hub/📅 Daily"')
  .sort(p => p.file.name, 'desc')
  .limit(7);

let weekXp = 0;
let weekHours = 0;
let weekMinutes = 0;
let streakDays = 0;

for (let log of logs) {
  weekXp += log.xp_earned || 0;
  weekHours += log.hours || 0;
  weekMinutes += log.minutes || 0;
  if (log.completed) streakDays++;
}

const totalMinutes = weekHours * 60 + weekMinutes;
const displayHours = Math.floor(totalMinutes / 60);
const displayMins = totalMinutes % 60;

dv.paragraph(`**Ultimi 7 giorni:**`);
dv.paragraph(`⭐ XP: +${weekXp}`);
dv.paragraph(`⏱️ Tempo: ${displayHours}h ${displayMins}m`);
dv.paragraph(`🔥 Giorni attivi: ${streakDays}/7`);
```

---

## 🎯 Prossimi Obiettivi

### Prossimo Livello
```dataviewjs
const xp = dv.current().xp || 0;
const levels = [0,500,1200,2000,3000,4200,5600,7200,9000,11000,15000,20000];
const nextXp = levels.find(l => l > xp) || 20000;
const remaining = nextXp - xp;

dv.paragraph(`**XP mancanti:** ${remaining}`);
dv.paragraph(`📖 ~${Math.ceil(remaining/30)} capitoli di libro`);
dv.paragraph(`✅ ~${Math.ceil(remaining/50)} task completati`);
```

---

[[📊 Dashboard|← Torna alla Dashboard]]
