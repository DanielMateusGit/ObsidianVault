# ⚡ Quick Reference - Learning Hub Structure

> **Per Claude:** Leggi questo per orientarti rapidamente nel progetto

## 📁 **Struttura File System**

```
02 - Learning Hub/
│
├── claude/                      ← Memoria di Claude
│   ├── CLAUDE.md               ← START HERE (ingresso principale)
│   ├── profile.md              ← Chi è Dan
│   ├── current-state.md        ← Stato attuale (AGGIORNATO FREQUENTEMENTE!)
│   ├── QUICK-REFERENCE.md      ← Questo file
│   ├── roadmaps/
│   │   ├── architect-quest.md  ← Roadmap AQ (5 progetti + AI track)
│   │   ├── senior-engineer.md  ← Roadmap SE (6 progetti)
│   │   ├── ai-skills.md        ← Roadmap AI Skills (integrata nei progetti)
│   │   ├── career-boost.md     ← System Design, Communication, Interview Prep
│   │   └── senior-frontend.md  ← Side track React + Flutter
│   ├── context/
│   │   ├── tech-stack.md       ← Stack tecnologico
│   │   ├── learning-style.md   ← Come Dan impara + workflow esami
│   │   ├── gamification.md     ← XP system + esami + letture
│   │   ├── reading-list.md     ← 🆕 Tutte le letture tracciate
│   │   ├── quiz-tracker.md     ← Spaced repetition (Leitner boxes)
│   │   └── files.md            ← Context files consolidati
│   └── sessions/
│       └── YYYY-MM-DD.md       ← Log sessioni
│
├── Architect-Quest/            ← Percorso 1 (System Design)
│   └── Projects/
│       ├── P1-Notification-Service/
│       ├── P2.5-AI-Calendar-Assistant/  ← AI Project (Mesi 5-6)
│       ├── P2-NutriPlan/
│       ├── P3-BookingHub/
│       └── P4-FamilyBudget/
│
├── Senior-Engineer/            ← Percorso 2 (Hands-on Coding)
│   └── Projects/
│       ├── P1-Task-Manager/
│       ├── P2-Chat-App/
│       ├── P3-Ecommerce/
│       ├── P4-Alert-Gateway/
│       ├── P5-URL-Shortener/
│       └── P6-Capstone/
│
├── AI-Frontier/                ← 🆕 Exploration Lab (Quarterly)
│   ├── README.md               ← Metodologia completa
│   ├── Templates/
│   │   └── experiment-template.md
│   ├── 2026/
│   │   └── Q1/
│   │       ├── exploration-queue.md  ← Tech da esplorare Q1
│   │       └── example-*.md          ← Esempi esperimenti
│   └── Archive/
│
├── Exams/                      ← 🆕 Esami e verifiche conoscenze
│   ├── README.md              ← Guida sistema esami
│   └── esame_YYYY-MM-DD.md    ← Esami (voto in trentesimi)
│
├── Dashboard.md                ← Vista Obsidian principale
├── Progress.md                 ← XP, livello, streak
├── coach.py                    ← Coach Agent (Ollama)
└── complete-guide.md           ← Guida completa sistema
```

---

## 🎯 **Flow di Lettura Consigliato**

### **Al Primo Accesso (Prima Conversazione):**
1. `claude/CLAUDE.md` → Panoramica sistema
2. `claude/profile.md` → Chi è Dan, come impara
3. `claude/WHY.md` → Il VERO perché (casa, Federica, famiglia) ❤️
4. `claude/current-state.md` → Dove siamo ADESSO

### **Durante Sessione Progetto:**
1. `claude/current-state.md` → Stato attuale
2. `claude/roadmaps/[percorso].md` → Roadmap del percorso attivo
3. Progetto specifico in `Architect-Quest/` o `Senior-Engineer/`

### **Durante Sessione AI Exploration:**
1. `AI-Frontier/README.md` → Metodologia
2. `AI-Frontier/2026/QX/exploration-queue.md` → Cosa esplorare
3. `AI-Frontier/Templates/experiment-template.md` → Template

---

## 🔑 **Key Info - Always Remember**

### **Dan's Profile (Snapshot)**
- **Ruolo:** Mid-level Full-Stack (.NET + React)
- **Obiettivo:** AI Engineer (target primario) + Senior/Staff Engineer (18-24 mesi)
- **Target:** €90k-130k remote EU, €110-160k US
- **PERCHÉ:** Casa per Federica, supportare famiglia, futuro per eventuali figli ❤️
- **Learning style:** Spiegazione dettagliata PRIMA, poi hands-on
- **Time:** 10-15 ore/settimana (weekdays sera + weekend)
- **Lingua:** Italiano per spiegazioni, inglese per codice

### **Tech Stack Core**
- Backend: .NET 8, C#
- Frontend: React + TypeScript, Redux Toolkit (NON Zustand!)
- DB: PostgreSQL (Architect), SQL Server (Senior), Redis (everywhere)
- Cloud: Azure
- AI: Ollama (local), Claude API, MCP

### **Regole d'Oro**
1. ✅ Italiano per spiegazioni, inglese per codice
2. ✅ Spiega il "QUANDO usare", non solo "COME"
3. ✅ No fretta - velocità crociera preferita
4. ✅ n8n Prototype Practice (prima e dopo ogni progetto, da P2+)
5. ✅ Aggiorna `current-state.md` dopo ogni sessione
6. ✅ Redis è focus importante (usalo ovunque progressivamente)
7. ✅ TDD rigoroso nei progetti Senior Engineer
8. ✅ C4 + ADR in progetti Architect Quest

---

## 🤖 **AI Skills Track - Quick Summary**

### **Filosofia**
- **90% skill generiche** (funzionano con qualsiasi LLM)
- **10% Claude-specific** (vantaggio competitivo)
- Provider-agnostic architecture (migra ad altri provider in 2-3 giorni)

### **Componenti**

#### 1. **AI Projects Integration** (Mesi 5-18)
- **P2.5** (M6-8): AI Gateway
  - Phase 1: Ollama (100% universale)
  - Phase 2: Claude + MCP (80% universale)
  - Phase 3: Multi-provider (95% universale)
- **P3** (M10-14): BookingHub + AI
- **P4** (M15-18): FamilyBudget + AI

#### 2. **AI Frontier Lab** (Quarterly, 4-6 ore)
- Esplora nuove tech man mano escono
- Metodologia: Quick Assessment → Hands-on → Decision
- Q1 2026: o3-mini, Gemini 2.0 Flash, LangGraph
- **Separato dai progetti** = zero rischi

### **Transferability Matrix**
| Skill | Genericità | Transfer Time |
|-------|------------|---------------|
| Prompt Engineering | 🟢 100% | 0 giorni |
| Function Calling | 🟢 95% | 1-2 giorni |
| RAG | 🟢 100% | 0 giorni |
| Claude API | 🟡 85% | 2-3 giorni |
| MCP | 🟡 70% | 3-5 giorni |
| AI Router | 🟢 100% | 0 giorni |

---

## 📊 **Current Status**

> **Non duplicare dati dinamici qui.** Consulta sempre `current-state.md` per lo stato aggiornato.
>
> Dati come XP, livello, streak, week corrente cambiano ogni sessione.
> Averli qui crea divergenza. Fonte di verita: `claude/current-state.md`.

---

## 🎮 **XP System Quick Reference**

### **Main Activities**
| Activity | XP |
|----------|-----|
| Task completato | +50 |
| Settimana completata | +150 |
| Progetto completato | +500 |
| Boss Battle | +300-500 |

### **🎓 Esami (NUOVO!)**
| Voto | XP |
|------|-----|
| ≥27/30 (Lode) | +200 |
| ≥24/30 (Merito) | +150 |
| ≥18/30 (Superato) | +100 |
| <18/30 (Tentativo) | +30 |

### **📚 Letture**
| Tipo | XP |
|------|-----|
| Articolo breve | +15 |
| Capitolo libro | +30 |
| Video | +15 |

### **AI Frontier**
| Activity | XP |
|----------|-----|
| Quick assessment | +25 |
| Hands-on experiment | +75 |
| POC integration | +100 |
| Tech adopted | +200 |

### **Levels**
1. Apprentice (0) → 2. Code Crafter (500) → 3. Pattern Seeker (1.2k) → ... → 12. AI-Native Architect (20k)

---

## 🚨 **Files da Aggiornare Dopo Sessione**

**SEMPRE:**
- [ ] `claude/current-state.md` → Stato, progressi, prossimi passi
- [ ] `Progress.md` → XP totali, streak, XP History
- [ ] `claude/context/reading-list.md` → 🆕 Letture consigliate/completate
- [ ] `claude/sessions/YYYY-MM-DD.md` → Log sessione Claude (dettagliato)
- [ ] `Daily/YYYY-MM-DD.md` → Tracker giornaliero (per streak)

**SE APPLICABILE:**
- [ ] `Tasks/Week-XX.md` del progetto → Task completati
- [ ] `Achievements.md` → Sblocca achievement guadagnati
- [ ] `Notes/*.md` del progetto → Appunti con quiz
- [ ] `Exams/*.md` → 🆕 Se esame proposto/completato

**A FINE PROGETTO/MILESTONE:**
- [ ] 🎓 **ESAME OBBLIGATORIO** → `Exams/esame_YYYY-MM-DD.md`

**A FINE SETTIMANA (Domenica o ultima sessione):**
- [ ] `Weekly/YYYY-WXX.md` → Retrospettiva settimanale

**VERIFICA FINALE:**
- [ ] Commit pushati su GitHub?
- [ ] XP coerenti tra Progress.md e XP History?
- [ ] Letture aggiornate in reading-list.md?
- [ ] Prossimi task chiari?

---

## 📝 **Note per Claude (Self-Reminders)**

### **Do's**
- ✅ Read `current-state.md` FIRST every session
- ✅ Read `WHY.md` for motivation context (casa, Federica, famiglia)
- ✅ **🚨 TEORIA PRIMA, PRATICA DOPO** - Mai correre a scrivere codice!
- ✅ Explain WHY and WHEN, not just HOW
- ✅ Be patient - Dan prefers "cruise speed"
- ✅ When Dan is tired/demotivated → remind him of WHY.md
- ✅ Connect technical learning to personal goals (€2k/mese, casa in 2-3 anni)
- ✅ Update current-state.md after session
- ✅ Italian explanations, English code

### **Don'ts**
- ❌ Don't suggest Zustand (Dan knows Redux Toolkit!)
- ❌ Don't rush - Dan prefers quality > speed
- ❌ Don't use Visual Studio (Dan uses VS Code)
- ❌ Don't assume - ask if unclear
- ❌ Don't skip TDD in Senior Engineer projects
- ❌ Don't skip exam at end of milestone/project
- ❌ Don't forget to update reading-list.md when suggesting readings

### **AI-Specific**
- ✅ Emphasize provider-agnostic patterns
- ✅ Explain genericità % for each skill
- ✅ Compare Ollama vs Claude vs OpenAI when relevant
- ✅ Mention "Tempo per migrare ad altro provider" quando possibile

---

## 🔄 **Session Template**

```markdown
1. Read current-state.md
2. Understand context (dove siamo? cosa stiamo facendo?)
3. If multi-step task → TodoWrite
4. Execute work (explain → code → test → review)
5. Update current-state.md
6. Update Progress.md if XP earned
7. Update reading-list.md if readings suggested
```

---

## 🎓 **Exam Workflow (NUOVO!)**

### Quando Proporre Esami
| Trigger | Azione |
|---------|--------|
| **Fine milestone/progetto** | OBBLIGATORIO - Crea esame |
| **Weekend/Lunedì** | Chiedi "Sei pronto per una verifica?" |
| **Dan chiede ripasso** | Crea esame su argomenti richiesti |
| **Pre-certificazione** | Simula esame reale |

### Processo
```
1. Claude: "Sei pronto per una verifica? Argomenti: [X, Y, Z]"
2. Dan: "Sì"
3. Claude: Crea Exams/esame_YYYY-MM-DD.md
4. Dan: Compila risposte nel file
5. Dan: "Ho finito l'esame"
6. Claude: Legge, corregge, voto /30, feedback
7. Claude: Assegna XP in base al voto
```

### Struttura Esame (30 punti)
- **A** (10pt): Domande aperte
- **B** (6pt): Multiple choice
- **C** (8pt): Codice (fix/refactor/write)
- **D** (6pt): Design/Architettura

---

## 📞 **Quick Contacts**

**For Dan:**
- Obsidian: Main workspace
- Coach: `./coach.py motivation|briefing|status|suggest|quiz`
- Motivation: `./coach.py motivation` ← **INIZIA SEMPRE DA QUI** 💪

**For Claude:**
- Start: `claude/CLAUDE.md`
- Current: `claude/current-state.md`
- Why: `claude/WHY.md` ← Leggi quando serve motivazione
- This file: Quick orientation

---

## 🚀 **Comando per Iniziare Sessione**

Quando apri un nuovo terminale Claude, usa questo comando:

```
Leggi la cartella /claude nella Obsidian Vault "02 - Learning Hub" e avvia la sessione di studio. Motivami e dimmi dove siamo rimasti.
```

**Oppure versione breve:**
```
Leggi /claude in "02 - Learning Hub", motivami e riprendiamo da dove eravamo.
```

Questo farà:
1. ✅ Leggere il contesto (CLAUDE.md, current-state.md, WHY.md)
2. ✅ Darti motivazione (casa, Federica, obiettivi)
3. ✅ Mostrarti dove sei rimasto
4. ✅ Proporti il prossimo task

---

*Last updated: 2026-03-26 (refactor — fix TodoWrite, P4 name, aggiunto n8n)*
*Structure version: 3.1*
