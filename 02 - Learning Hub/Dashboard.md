---
tags: [learning, dashboard]
---

# 🎓 Learning Hub - Dashboard

> *"Non ti insegno solo a codificare. Ti insegno a PENSARE come senior engineer."*

---

## 👤 Player Status

```dataviewjs
const progress = dv.page("🎓 Learning-Hub/📈 Progress");
if (progress) {
  const xp = progress.xp || 0;
  const level = progress.level || 1;
  const title = progress.title || "Apprentice";
  const streak = progress.streak || 0;
  
  const levels = [0,500,1200,2000,3000,4200,5600,7200,9000,11000,15000,20000];
  const nextLevelXp = levels.find(l => l > xp) || 20000;
  const prevLevelXp = levels.filter(l => l <= xp).pop() || 0;
  const progress_pct = Math.floor((xp - prevLevelXp) / (nextLevelXp - prevLevelXp) * 100);
  const bar = "█".repeat(Math.floor(progress_pct/5)) + "░".repeat(20-Math.floor(progress_pct/5));
  
  dv.paragraph(`## Lv.${level} — ${title}`);
  dv.paragraph(`**XP:** ${xp} / ${nextLevelXp}`);
  dv.paragraph(`\`${bar}\` ${progress_pct}%`);
  dv.paragraph(`🔥 **Streak:** ${streak} giorni`);
} else {
  dv.paragraph("⚠️ Crea il file Progress.md");
}
```

---

## 📊 Oggi

```dataviewjs
const today = dv.date("today").toFormat("yyyy-MM-dd");
const todayLog = dv.page(`🎓 Learning-Hub/📅 Daily/${today}`);

if (todayLog) {
  dv.paragraph(`⏱️ **Tempo:** ${todayLog.hours || 0}h ${todayLog.minutes || 0}m`);
  dv.paragraph(`⭐ **XP guadagnati:** +${todayLog.xp_earned || 0}`);
  dv.paragraph(`✅ **Completato:** ${todayLog.completed ? "Sì" : "Non ancora"}`);
} else {
  dv.paragraph("📝 [Crea il daily log di oggi](📅 Daily/)");
}
```

### Task di Oggi
```dataview
TASK
FROM "🎓 Learning-Hub"
WHERE !completed AND contains(tags, "today")
LIMIT 5
```

---

## 🛤️ I Tre Percorsi

### 🏛️ Architect Quest
*System design, cloud enterprise, progettare per AI agents*
*Include: P2.5 AI Calendar System (Claude-Native + Provider-Agnostic)* 🤖

```dataviewjs
const projects = ["P1-Notification-Service","P2-NutriPlan","P3-BookingHub","P4-FamilyBudget"];
let completed = 0;
let total = 4;

// Simplified progress
dv.paragraph(`**Progetti:** ${completed}/${total} completati`);

const pct = Math.floor(completed/total*100);
const bar = "█".repeat(Math.floor(pct/5)) + "░".repeat(20-Math.floor(pct/5));
dv.paragraph(`\`${bar}\` ${pct}%`);
```

**Settimana corrente:** [[🏛️ Architect-Quest/Projects/P1-Notification-Service/02-Tasks/Week-01|P1 Week 1]]

---

### 💻 Senior Engineer Path  
*Coding hands-on, patterns, TDD, Redis mastery*

```dataviewjs
const projects = ["P1-Task-Manager","P2-Chat-App","P3-Ecommerce","P4-Notifications","P5-URL-Shortener","P6-Capstone"];
let completed = 0;
let total = 6;

dv.paragraph(`**Progetti:** ${completed}/${total} completati`);

const pct = Math.floor(completed/total*100);
const bar = "█".repeat(Math.floor(pct/5)) + "░".repeat(20-Math.floor(pct/5));
dv.paragraph(`\`${bar}\` ${pct}%`);
```

**Settimana corrente:** [[💻 Senior-Engineer/Projects/P1-Task-Manager/01-Tasks/Week-01|P1 Week 1]]

---

### 🔬 AI Frontier Exploration Lab
*Esplora nuove AI tech man mano escono - indipendente dai progetti*

**Q1 2026 Queue:**
- OpenAI o3-mini (reasoning economico)
- Gemini 2.0 Flash (thinking gratis)
- LangGraph (framework vs custom)

**Status:** Pronto per sessioni quarterly (4-6 ore/quarter)

[[AI-Frontier/README|→ Vai al Frontier Lab]] | [[AI-Frontier/2026/Q1/exploration-queue|Q1 Queue]]

---

## 🏆 Achievement Recenti

```dataview
TABLE WITHOUT ID
  badge AS "🏆",
  achievement AS "Nome",
  date AS "📅"
FROM "🎓 Learning-Hub/🏆 Achievements"
WHERE unlocked = true
SORT date DESC
LIMIT 5
```

[[🏆 Achievements|→ Tutti gli achievement]]

---

## 📅 Ultimi 7 Giorni

```dataview
TABLE WITHOUT ID
  file.link AS "📅",
  hours + "h " + minutes + "m" AS "⏱️",
  xp_earned AS "⭐",
  choice(completed, "✅", "❌") AS "Streak",
  focus AS "🎯 Focus"
FROM "🎓 Learning-Hub/📅 Daily"
SORT file.name DESC
LIMIT 7
```

---

## 📚 In Lettura

```dataview
TABLE WITHOUT ID
  file.link AS "📖",
  progress AS "Progresso",
  project AS "Per"
FROM "🎓 Learning-Hub/📚 Books"
WHERE status = "reading"
```

---

## 🔗 Quick Links

| Architect Quest | Senior Engineer | AI & Generale |
|-----------------|-----------------|---------------|
| [[🏛️ Architect-Quest/00-Overview\|📋 Overview]] | [[💻 Senior-Engineer/00-Overview\|📋 Overview]] | [[📈 Progress\|📈 XP & Level]] |
| [[🏛️ Architect-Quest/01-Roadmap\|🗺️ Roadmap]] | [[💻 Senior-Engineer/01-Roadmap\|🗺️ Roadmap]] | [[🏆 Achievements\|🏆 Achievements]] |
| [[🏛️ Architect-Quest/Concepts/\|💡 Concepts]] | [[💻 Senior-Engineer/Concepts/\|💡 Concepts]] | [[claude/roadmaps/ai-skills\|🤖 AI Roadmap]] |
| | | [[AI-Frontier/README\|🔬 Frontier Lab]] |

---

## 🤖 Coach Command

```bash
# 💪 INIZIA SEMPRE CON QUESTO
./coach motivation       # Ricordati il PERCHÉ (casa, Federica, famiglia)

# Briefing giornaliero
./coach briefing

# Quiz su concetti recenti
./coach quiz

# Cosa studiare oggi
./coach suggest

# Status completo
./coach status
```

---

## 💪 IL TUO PERCHÉ

[[claude/WHY|→ Leggi WHY.md]] quando la motivazione cala

**Quick reminder:**
- 🏡 Casa per te e Federica: fattibile in 2-3 anni
- 👨‍👩‍👧‍👧 Supportare mamma, papà, sorelle senza stress
- 👶 Futuro sicuro per eventuali figli
- 💰 +€2k/mese netto = libertà finanziaria

**18 mesi di impegno = 40 anni di tranquillità** ❤️
