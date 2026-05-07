# ⚡ Quick Reference - Learning Hub Structure

> **Per Claude:** Leggi questo per orientarti rapidamente nel progetto.
> **Source of truth dinamica:** `claude/current-state.md`. Qui solo info statiche / strutturali.

## 📁 **Struttura File System**

```
02 - Learning Hub/
│
├── claude/                      ← Memoria di Claude
│   ├── CLAUDE.md               ← START HERE (regole + workflow)
│   ├── profile.md              ← Chi è Dan
│   ├── WHY.md                  ← Motivazioni (casa, Federica, famiglia)
│   ├── current-state.md        ← Stato attuale (SOURCE OF TRUTH)
│   ├── career-strategy.md      ← Strategia carriera + Cluster Positioning
│   ├── QUICK-REFERENCE.md      ← Questo file
│   ├── roadmaps/
│   │   ├── fast-track.md       ← ⭐ Conduttore cross-roadmap (29 topic CV-ROI)
│   │   ├── architect-quest.md  ← Roadmap AQ (5 progetti + AI track)
│   │   ├── senior-engineer.md  ← Roadmap SE (6 progetti + 6 cluster)
│   │   ├── ai-skills.md        ← Roadmap AI Skills (4 cluster)
│   │   ├── senior-frontend.md  ← Side track FE + Flutter (6 cluster)
│   │   └── career-boost.md     ← System Design, Communication, Interview Prep
│   ├── context/
│   │   ├── cluster-taxonomy.md      ← canonical (4+6+6 cluster)
│   │   ├── mini-projects-index.md   ← canonical (30 mini-projects)
│   │   ├── tech-stack.md
│   │   ├── learning-style.md
│   │   ├── gamification.md
│   │   ├── reading-list.md
│   │   ├── quiz-tracker.md          ← Spaced repetition (sessioni-based)
│   │   ├── idea-backlog.md
│   │   ├── monetization-potential.md
│   │   ├── files.md                 ← Indice context
│   │   └── job-postings-*.md        ← Annunci analizzati (4 file)
│   └── sessions/
│       └── YYYY-MM-DD.md       ← Log sessioni
│
├── Knowledge/                  ← Note atomiche (Sedimentazione)
│   └── CLAUDE.md              ← Indice + tag schema
│
├── Certifications/             ← Tracker certificazioni
│   ├── README.md
│   └── [cert-slug]/tracker.md
│
├── Architect-Quest/            ← Progetti AQ
│   └── Projects/P1-P5/
│
├── Senior-Engineer/            ← Progetti SE
│   └── Projects/P1-P6/
│
├── AI-Frontier/                ← Exploration Lab (cadenza libera)
│
├── Exams/                      ← Esami /30
├── .claude/skills/             ← Slash commands (init, quiz, end, nota, ask, exam, context, refactor)
├── .claude/hooks/              ← validate-note.sh
├── Dashboard.md, Progress.md, Achievements.md
└── coach.py
```

## 🎯 **Flow di Lettura Consigliato**

### **Prima conversazione**
1. `claude/CLAUDE.md` → Regole + workflow
2. `claude/profile.md` → Chi è Dan
3. `claude/WHY.md` → Motivazioni ❤️
4. `claude/current-state.md` → Dove siamo

### **Sessione progetto**
1. `claude/current-state.md`
2. `claude/roadmaps/[percorso].md` (o `fast-track.md` per sessioni corte)
3. Progetto in `Architect-Quest/` o `Senior-Engineer/`

### **Sessione corta / "ho poco tempo"**
1. `claude/current-state.md`
2. `claude/roadmaps/fast-track.md` → pesca XS/S item da Fase 1
3. Sync bidirezionale alla roadmap sorgente quando completi

## 🔑 **Key Info**

### **Dan's Profile**
- **Ruolo attuale:** Mid-level Full-Stack (.NET + React)
- **Obiettivo:** AI Engineer (primario) + Senior/Staff Engineer
- **Modalità:** Self-paced (no timeline, completion-based)
- **Target:** €90-130k EU, €110-160k US
- **PERCHÉ:** Casa per Federica, supportare famiglia ❤️
- **Time:** 10-15 ore/settimana
- **Lingua:** Italiano per spiegazioni, inglese per codice

### **Tech Stack** (vedi `context/tech-stack.md` per full list)
- BE primario: .NET 8 + C# 12
- BE secondario (on-the-job): Java/Spring Boot, Node/TS BE
- BE AI: Python (FastAPI + LangChain/LangGraph) — solo per Python AI Bridge
- FE: React + TS, Redux Toolkit (NON Zustand)
- DB: PostgreSQL (AQ), SQL Server (SE), Redis ovunque, pgvector per RAG
- Cloud: Azure primario, AWS/GCP awareness
- AI: Ollama + Claude API + MCP + LangGraph + Ragas + Langfuse

### **Regole d'oro**
1. Italiano per spiegazioni, inglese per codice
2. Spiega il **QUANDO usare**, non solo COME
3. **No fretta** — velocità crociera (no scadenze)
4. n8n Prototype Practice (sandwich da P2 in poi)
5. Aggiorna `current-state.md` dopo ogni sessione
6. Redis progressivo in tutti i progetti
7. TDD rigoroso in Senior Engineer
8. C4 + ADR in Architect Quest
9. **Sync bidirezionale fast-track ↔ roadmap sorgente**

## 🤖 **AI Skills Track - Quick Summary**

### **Filosofia**
- ~92% skill generiche (provider-agnostic)
- 8% Claude-specific (vantaggio competitivo)
- Migrazione ad altro provider: 2-3 giorni

### **Cluster di ruolo (4 AI cluster, vedi `cluster-taxonomy.md`)**
- **#4 AI-Augmented SWE** ⭐ bridge 3-6 mesi (€40-65k IT / £70-100k UK)
- **#3 Full-Stack AI-First** 6-12 mesi (£90-110k)
- **#2 AI Engineer GenAI/LLMOps** 12-18 mesi (€80-120k / £100-200k)
- **#1 AI Tech Lead Enterprise** 18-30+ mesi (€70-100k+)

### **AI Frontier Lab**
Esplorazioni quando Dan ha voglia (no cadenza fissa). Vedi `AI-Frontier/README.md`.

## 📊 **Current Status**

> **Non duplicare dati dinamici qui.** Consulta sempre `current-state.md` per:
> - XP, livello, streak, modulo corrente
> - Task corrente, ultima sessione
> - Decisioni attive
>
> Avere snapshot qui crea divergenza. Source of truth: `claude/current-state.md`.

## 🎮 **XP System Quick Reference**

> Tabelle complete: `claude/context/gamification.md`

### **Main**
| Activity | XP |
|----------|-----|
| Task completato | +50 |
| Modulo completato | +150 |
| Progetto completato | +500 |
| Boss Battle 24/30+ | +300-500 |

### **Esami /30**
| Voto | XP |
|------|-----|
| ≥27 (Lode) | +200 |
| ≥24 (Merito) | +150 |
| ≥18 (Superato) | +100 |

### **Livelli (12 totali)**
1. Apprentice (0) → 7. System Designer (5.6k) → 8. Cloud Engineer (7.2k) → 12. AI-Native Architect 👑 (20k)

## 🚨 **File da Aggiornare Dopo Sessione**

> Lista canonica: `claude/CLAUDE.md` sezione "Checklist Fine Sessione". La skill `/end` esegue tutto automaticamente.

**Sempre:**
- [ ] `claude/current-state.md`
- [ ] `Progress.md` (XP + frontmatter + History)
- [ ] `claude/sessions/YYYY-MM-DD.md`
- [ ] `claude/context/quiz-tracker.md` (se fatta spaced repetition: decrementa contatori Box 2+)

**Se applicabile:**
- [ ] `Knowledge/CLAUDE.md` (se note nuove)
- [ ] `Achievements.md`
- [ ] `claude/context/reading-list.md`
- [ ] `claude/roadmaps/fast-track.md` + roadmap sorgente (sync bidirezionale)

## 📝 **Note per Claude**

### **Do's**
- ✅ Read `current-state.md` FIRST every session
- ✅ **TEORIA → DOMANDE → NOTA → CONFERMA → CODICE** (mai saltare)
- ✅ Spiega WHY e WHEN, non solo HOW
- ✅ Velocità crociera (Dan preferisce capire bene)
- ✅ Connect technical learning to WHY.md (€2k/mese, casa)
- ✅ Italian explanations, English code
- ✅ Per sessioni corte: pesca da `fast-track.md`

### **Don'ts**
- ❌ NON suggerire Zustand (Dan usa Redux Toolkit)
- ❌ NON usare Visual Studio (Dan usa VS Code)
- ❌ NON saltare TDD in Senior Engineer
- ❌ NON saltare esame fine progetto/milestone
- ❌ NON pressare sui tempi (no scadenze, self-paced)
- ❌ NON iniettare servizi nelle entity (passa il valore)

### **AI-Specific**
- ✅ Provider-agnostic patterns
- ✅ Spiega genericità % per skill
- ✅ Confronta Ollama vs Claude vs OpenAI

## 🔄 **Session Template**

```markdown
1. Read current-state.md (+ quiz-tracker.md per spaced rep count)
2. Mostra stato (output /init style)
3. Se quiz Box 2+ in coda → spaced repetition OBBLIGATORIA
4. Multi-step task → TaskCreate
5. Esegui (teoria → domande → nota → codice)
6. /end per chiudere (aggiorna tutto + git push)
```

## 🎓 **Exam Workflow**

| Trigger | Tipo | Obbligatorio |
|---------|------|--------------|
| Fine 2-3 Moduli stesso topic | Esame tematico /30 | Opzionale |
| Fine Progetto | Boss Battle /30 | **OBBLIGATORIO** |
| Pre-certificazione | Simulazione /30+ | Su richiesta |

> Nessun esame ha data fissa. Trigger = prerequisiti completati + Dan pronto.

## 🚀 **Comando per Iniziare Sessione**

Comando consigliato: `/init`

In alternativa testuale:
```
Leggi /claude in "02 - Learning Hub", motivami e riprendiamo da dove eravamo.
```

---

*Last updated: 2026-05-05 (refactor — rimosse timeline, Week→Modulo, aggiunti fast-track + canonical sources, TodoWrite→TaskCreate, AI Frontier no quarterly)*
*Structure version: 4.0*
