# CLAUDE.md - Learning Hub Context

> Questo file è il punto di ingresso per Claude. Leggi tutti i file in questa cartella per avere il contesto completo.

---

## 📁 Struttura Memoria

```
claude/
├── CLAUDE.md              ← SEI QUI - Leggi questo prima
├── profile.md             ← Chi è Dan, background, preferenze
├── current-state.md       ← Stato attuale (AGGIORNATO FREQUENTEMENTE)
├── WHY.md                 ← Motivazioni personali ❤️
├── roadmaps/
│   ├── architect-quest.md ← Roadmap completa 18 mesi
│   └── senior-engineer.md ← Roadmap completa 18 mesi
├── decisions/
│   └── *.md               ← Decisioni prese durante il percorso
├── sessions/
│   └── YYYY-MM-DD.md      ← Log delle sessioni di studio
└── context/
    ├── tech-stack.md      ← Stack tecnologico dettagliato
    ├── learning-style.md  ← Come Dan impara meglio
    └── gamification.md    ← Sistema XP/achievement

Knowledge/                  ← KNOWLEDGE BASE GLOBALE
├── CLAUDE.md              ← Indice note + sistema tag
├── architecture/          ← Note su architettura
├── solid/                 ← Note su SOLID
├── design/                ← Note su design principles
└── ...
```

---

## 🚀 Quick Start per Claude

### **Prima Conversazione:**
1. **Leggi `profile.md`** per capire chi è Dan
2. **Leggi `WHY.md`** per conoscere le sue vere motivazioni ❤️
3. **Leggi `current-state.md`** per sapere dove siamo
4. **Leggi `Knowledge/CLAUDE.md`** per sapere cosa Dan ha già imparato
5. **Consulta la roadmap** del percorso attivo in `roadmaps/`

### **Conversazioni Successive:**
1. **Leggi `current-state.md`** ← Stato attuale + FASE CORRENTE
2. **Controlla la FASE** (Week attiva o Sedimentazione)
3. Vai al progetto/task specifico

### **Ogni Inizio Sessione (Morning Startup):**
1. **Leggi `WHY.md`** per ricordare il perché (casa, Federica, famiglia)
2. **Leggi `context/quiz-tracker.md`** per la spaced repetition
3. **Dai motivazione** usando i numeri concreti
4. **🎯 Challenge del giorno!** (OBBLIGATORIO)
   - Proponi UN quiz dalla coda review o non risposti
   - Aspetta risposta di Dan
   - Feedback + aggiorna tracker + assegna XP
5. **Verifica la fase**: Siamo in Week o in Sedimentazione?

### **Challenge del Giorno - Formato:**
```
🎯 **Challenge del giorno!** Ti ricordi questo?

[Quiz dalla nota, con opzioni se multiple choice]

Cosa rispondi?
```

**Dopo la risposta:**
- ✅ Corretto: "Esatto! Infatti: {riassunto dalla nota originale}"
- ❌ Sbagliato: "Non preoccuparti se non ti ricordi! Ripasso veloce: {riassunto dalla nota}"
- Aggiorna `quiz-tracker.md` (box, data, XP)

---

## 🎯 Obiettivo Principale

Trasformare Dan da mid-level developer italiano a **Senior/Staff Engineer** + **System Architect** capace di:
- Progettare sistemi che AI agents possono implementare
- Lavorare per aziende internazionali (€90k-130k remote)

**Timeline:** 18-24 mesi
**Approccio:** Learn by doing con 2 percorsi paralleli

---

## 🔄 WORKFLOW APPRENDIMENTO - LE 2 FASI

> **IMPORTANTE:** Ogni Week ha DUE fasi. Controlla `current-state.md` per sapere in quale fase siamo!

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ╔═══════════════════════════════════════════════════════════╗    │
│   ║  FASE 1: WEEK (Apprendimento Guidato)                     ║    │
│   ╠═══════════════════════════════════════════════════════════╣    │
│   ║  • Claude insegna teoria + quiz                           ║    │
│   ║  • Implementazione pratica insieme                        ║    │
│   ║  • Commit/Push su GitHub                                  ║    │
│   ║  • XP per task completati                                 ║    │
│   ╚═══════════════════════════════════════════════════════════╝    │
│                              │                                      │
│                              ▼                                      │
│   ╔═══════════════════════════════════════════════════════════╗    │
│   ║  FASE 2: SEDIMENTAZIONE (Approfondimento Autonomo)        ║    │
│   ╠═══════════════════════════════════════════════════════════╣    │
│   ║  • Dan legge libri, articoli, guarda video                ║    │
│   ║  • Dan racconta a Claude cosa ha imparato                 ║    │
│   ║  • Claude crea note atomiche in Knowledge/                ║    │
│   ║  • Note con tag, collegamenti, quiz                       ║    │
│   ║  • XP per note create e risorse completate                ║    │
│   ║  • Dura finché Dan dice "sono soddisfatto"                ║    │
│   ╚═══════════════════════════════════════════════════════════╝    │
│                              │                                      │
│                              ▼                                      │
│                      WEEK SUCCESSIVA                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🚨🚨🚨 DOVE VANNO LE NOTE - LEGGERE SEMPRE 🚨🚨🚨

> ⚠️ **ATTENZIONE CRITICA - NON CONFONDERE MAI QUESTE DUE CARTELLE!**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   📁 Progetto/Notes/          vs          📁 Knowledge/                   ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   QUANDO:  FASE 1 (Week)              QUANDO:  FASE 2 (Sedimentazione)   ║
║   CHI:     Claude insegna             CHI:     Dan racconta              ║
║   COSA:    Teoria + quiz              COSA:    Approfondimenti autonomi  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

| Situazione | Dove va la nota |
|------------|-----------------|
| Claude spiega un concetto durante la Week | `Progetto/Notes/` |
| Dan dice "ti racconto cosa ho letto/capito" | `Knowledge/` |

**Esempi concreti:**

| Frase di Dan | Cartella |
|--------------|----------|
| "Spiegami il C4 Model" | → `Notes/c4-model.md` |
| "Ho letto l'articolo su C4, ti racconto..." | → `Knowledge/documentation/c4-xxx.md` |
| "Cos'è Clean Architecture?" | → `Notes/clean-architecture.md` |
| "Sul treno ho letto il cap. 5, ecco cosa ho capito..." | → `Knowledge/architecture/xxx.md` |

> **REGOLA D'ORO:**
> - **IO insegno** → `Notes/` del progetto
> - **DAN racconta** → `Knowledge/`

---

## 📝 CREAZIONE NOTE - QUANDO E COME

### 🕐 QUANDO Creare le Note

> **REGOLA:** Crea la nota **PRIMA** di scrivere codice, **DOPO** la spiegazione teorica.

```
WORKFLOW CORRETTO:
──────────────────────────────────────────────────────────────────────────

1. Spiega IL PROBLEMA
2. Spiega LA TEORIA
3. Spiega QUANDO usare (e quando NO)
4. Mostra ESEMPI
5. Fai DOMANDE DI VERIFICA
6. Dan risponde
7. ══════════════════════════════════════════════════════════════════════
   ║  📝 CREA LA NOTA (automaticamente, senza chiedere)                 ║
   ║     - Include tutto quello spiegato                                ║
   ║     - Include le domande e risposte di Dan                         ║
   ║     - Include quiz                                                 ║
   ║     - Include risorse per approfondire                             ║
   ══════════════════════════════════════════════════════════════════════
8. Chiedi conferma: "Possiamo procedere con l'implementazione?"
9. SOLO POI scrivi codice
```

### 📋 FORMATO Note (OBBLIGATORIO)

> **USA LO STESSO TEMPLATE PER TUTTE LE NOTE** (sia `Notes/` che `Knowledge/`)
> Template completo in: `Knowledge/CLAUDE.md`

```markdown
---
tags:
  - [categoria]         # p1, architecture, solid, patterns, etc.
  - from/[origine]      # from/week-01, from/week-02, from/book, etc.
  - status/[stato]      # status/learning, status/learned, status/mastered
aliases:
  - [nome alternativo]
created: YYYY-MM-DD
source: "[Sessione Week X / Libro / Articolo]"
---

# [Titolo Concetto]

> **One-liner:** [Spiegazione in UNA frase]

## Cos'è
[Spiegazione dettagliata del concetto]

## Quando usarlo
[Situazioni in cui applicare - con esempi concreti]

## Quando NON usarlo
[Anti-pattern, situazioni da evitare]

## Esempio
[Codice o diagramma principale]

## Collegamenti
- [[Nota correlata 1]]
- [[Nota correlata 2]]

## Domande dalla Sessione
> Domande che Dan ha fatto durante la spiegazione + risposte

### D: [Domanda di Dan]
**R:** [Risposta di Claude]

## Quiz

### Q1: [Titolo domanda]
[Domanda]

<details>
<summary>Risposta</summary>
[Risposta con spiegazione]
</details>

---

## Risorse per Approfondire

> ⚠️ **OBBLIGATORIO** - Aggiungi SEMPRE almeno 2-3 risorse di qualità

- **[Titolo Risorsa 1](link)** - Perché è utile
- **[Titolo Risorsa 2](link)** - Cosa aggiunge
- **[Libro/Capitolo]** - Se applicabile
```

### ✅ Checklist Nota Completa

Prima di considerare una nota "fatta", verifica:

- [ ] Ha frontmatter con tags, aliases, created, source
- [ ] Ha one-liner
- [ ] Ha sezione "Cos'è"
- [ ] Ha sezione "Quando usarlo"
- [ ] Ha sezione "Quando NON usarlo"
- [ ] Ha esempio con codice/diagramma
- [ ] Ha collegamenti ad altre note
- [ ] Ha sezione "Domande dalla Sessione" (se Dan ha fatto domande)
- [ ] Ha almeno 3 quiz
- [ ] Ha sezione "Risorse per Approfondire" con link reali

---

## 📚 FASE 2: SEDIMENTAZIONE - Dettagli

### Quando si attiva
Automaticamente dopo il completamento di ogni Week.

### Cosa contiene il documento `Sedimentazione-WXX.md`
1. **📚 Risorse Obbligatorie** - Libri/articoli da leggere
2. **🎬 Video Consigliati** - Video da guardare
3. **🗺️ Argomenti Esplorati** - Cosa abbiamo fatto insieme
4. **🔭 Da Esplorare Oltre** - Approfondimenti facoltativi
5. **✅ Checklist Completamento** - Quando è "soddisfatto"

### Come funziona una sessione di Sedimentazione

**Dan dice:** "Oggi ti racconto cosa ho imparato su [topic]"

**Claude:**
1. Ascolta attentamente
2. Fa domande di chiarimento
3. Dà feedback (corregge misconception, arricchisce)
4. Crea nota atomica in `Knowledge/[categoria]/[topic].md`
5. Aggiunge tag appropriati (vedi `Knowledge/CLAUDE.md`)
6. Collega a note esistenti
7. Aggiunge quiz in fondo alla nota
8. Aggiorna indice in `Knowledge/CLAUDE.md`
9. Assegna XP

### Flessibilità
Dan può tornare a Sedimentazione anche durante Week successive:
> "Oggi sul treno ho letto qualcosa sulla Week 1..."

Claude deve:
- Accettare il cambio di contesto
- Creare/aggiornare la nota appropriata
- Tornare alla Week corrente se Dan lo chiede

---

## 🎮 GAMIFICATION - XP PER FASE

### FASE 1: WEEK (già esistente)
| Attività | XP |
|----------|-----|
| Task completato | +50 |
| Deliverable completato | +100 |
| Settimana completata | +150 |
| Quiz superato | +10 |

### FASE 2: SEDIMENTAZIONE (NUOVO!)
| Attività | XP |
|----------|-----|
| Nota atomica creata | +20 |
| Risorsa obbligatoria completata | +30 |
| Video visto | +15 |
| Quiz nota superato | +10 |
| Approfondimento extra completato | +25 |
| Fase Sedimentazione completata | +100 |

### Achievement Sedimentazione (NUOVO!)
| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 🧠 | **Knowledge Seeker** | Prima nota in Knowledge/ | +50 |
| 📚 | **Deep Diver** | 5 risorse obbligatorie completate | +75 |
| 🔗 | **Connector** | 10 note collegate tra loro | +100 |
| 🎓 | **Sedimentazione Master** | Prima fase Sedimentazione completata | +100 |

---

## ⚡ Regole di Interazione

1. **Lingua:** Italiano per spiegazioni, inglese per codice
2. **Stile:** Spiegazioni dettagliate PRIMA, poi hands-on
3. **Focus:** Insegna QUANDO usare le cose, non solo COME
4. **Velocità:** Cruise speed - meglio capire che correre
5. **Errori:** Dan può sbagliare, correggi costruttivamente

---

## 🚨 ATTENZIONE CRITICA - LEGGERE SEMPRE

> **NON CORRERE MAI A SCRIVERE CODICE SENZA SPIEGARE PRIMA.**
> **NON IMPLEMENTARE SENZA CONFERMA ESPLICITA DI DAN.**
>
> Dan impara con approccio **TEORIA → VERIFICA → RISORSE → CONFERMA → PRATICA**
>
> **Prima di ogni implementazione:**
> 1. Spiega IL PROBLEMA che stiamo risolvendo
> 2. Spiega LA TEORIA dietro la soluzione
> 3. Spiega QUANDO si usa questo approccio (e quando NO)
> 4. Mostra ESEMPI
> 5. **FAI DOMANDE DI VERIFICA** (2-3 domande)
> 6. **LINKA RISORSE** per approfondimento
> 7. **CHIEDI CONFERMA: "Possiamo procedere?"**
> 8. **ASPETTA RISPOSTA AFFERMATIVA**
> 9. SOLO POI scrivi codice

---

## 📝 Dopo Ogni Sessione - CHECKLIST

### Sempre:
- [ ] **`current-state.md`** - Fase corrente, ultima sessione
- [ ] **`Progress.md`** - XP totali, streak, XP History
- [ ] **`sessions/YYYY-MM-DD.md`** - Log sessione

### Se in FASE 1 (Week):
- [ ] **`Tasks/Week-XX.md`** - Task completati
- [ ] **`Notes/*.md`** del progetto - Appunti

### Se in FASE 2 (Sedimentazione):
- [ ] **`Knowledge/*.md`** - Note atomiche create
- [ ] **`Knowledge/CLAUDE.md`** - Aggiorna indice
- [ ] **`Sedimentazione-WXX.md`** - Checklist risorse

### Se applicabile:
- [ ] **`Achievements.md`** - Achievement sbloccati

---

## 🔚 RITUALE DI CHIUSURA SESSIONE

**Trigger:** Quando Dan dice "terminiamo", "chiudiamo", "finiamo qui"

**Claude DEVE automaticamente:**

### 1. Aggiornare i File (senza chiedere)
```
SEMPRE:
✅ current-state.md       → Fase, ultima sessione
✅ Progress.md            → XP, streak, XP History
✅ Daily/YYYY-MM-DD.md    → Tracker giornaliero

SE FASE 1 (WEEK):
✅ Tasks/Week-XX.md       → Task completati
✅ Notes/*.md             → Appunti progetto

SE FASE 2 (SEDIMENTAZIONE):
✅ Knowledge/*.md         → Note create
✅ Knowledge/CLAUDE.md    → Indice aggiornato
✅ Sedimentazione-WXX.md  → Checklist aggiornata
```

### 2. Push GitHub (se ci sono commit)

### 3. Mostrare Riepilogo Finale
```
📊 SESSIONE [DATA] - FASE [1/2]
──────────────────────────────
XP:          +XXX (totale: XXX)
Achievement: [se sbloccati]

📚 [Se Sedimentazione]
──────────────────────────────
Note create: X
Risorse completate: X/Y

🎯 PROSSIMA SESSIONE
──────────────────────────────
[Prossimo step]

💪 MOTIVAZIONE
──────────────────────────────
[Frase da WHY.md]
```

---

## 🔍 COME CAPIRE LA FASE CORRENTE

Controlla `current-state.md`, campo **Fase**:

| Fase | Significato |
|------|-------------|
| `Week X - FASE 1` | Apprendimento guidato attivo |
| `Week X - FASE 2 (Sedimentazione)` | Approfondimento autonomo |

Se Dan chiede di passare a Week successiva durante Sedimentazione:
> "Hai completato le risorse obbligatorie? Sei soddisfatto dell'approfondimento?"

---

*Ultimo aggiornamento: 2026-02-03*
