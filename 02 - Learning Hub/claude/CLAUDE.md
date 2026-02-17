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

Exams/                      ← ESAMI E VERIFICHE
├── esame_YYYY-MM-DD.md    ← Esami per verifica conoscenze
└── ...                    ← Orientati anche a certificazioni reali
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
3. **Dai motivazione** breve usando i numeri concreti
4. **🧠 Spaced Repetition Session** (OBBLIGATORIO - vedi sotto)
5. **Verifica la fase**: Siamo in Week o in Sedimentazione?

---

## 🧠 SPACED REPETITION SESSION - Inizio Sessione

> **Obiettivo:** Rinfrescare la memoria sui concetti appresi. Zero pressione, è per NON dimenticare.

### Quando farla
**SEMPRE** all'inizio di ogni sessione, PRIMA di iniziare nuovo materiale.

### Quante domande
| Situazione | Domande |
|------------|---------|
| Quiz in scadenza (da quiz-tracker) | Tutti quelli in scadenza |
| Nessun quiz in scadenza | 3-5 domande di ripasso generale |
| Dan chiede di più/meno | Adatta al suo tempo disponibile |

### Come selezionare le domande
**Priorità:**
1. Quiz in scadenza (spaced repetition dal tracker)
2. Quiz Box 1 non ancora risposti
3. Concetti delle ultime 2 settimane (ripasso generale)
4. Mix di argomenti diversi (non solo SOLID, non solo Domain, etc.)

### Formato Sessione
```
🧠 **Spaced Repetition** - Rinfreschiamo la memoria!

Nessuna pressione, è per consolidare. Rispondi come preferisci.

---

**1. [Argomento]**
[Domanda]

**2. [Argomento]**
[Domanda]

**3. [Argomento]**
[Domanda]

---

Quando hai finito, dimmi le tue risposte!
```

### Dopo le risposte - WORKFLOW
1. **Valuta ogni risposta** (✅ Corretto / 🟡 Parziale / ❌ Sbagliato)
2. **Aggiorna `quiz-tracker.md`** per ogni quiz
3. **Calcola XP totali** della sessione
4. **Se ci sono errori:**
   - Spiega brevemente dove ha sbagliato
   - **Indica le note da rileggere** (path esatto)
   - NON rispiegare tutto - basta il link alla nota
5. **Mostra riepilogo** (vedi sotto)

### Riepilogo Finale Spaced Repetition
```
📊 **Risultato Spaced Repetition**

| # | Argomento | Risultato | XP |
|---|-----------|-----------|-----|
| 1 | [Topic] | ✅ | +10 |
| 2 | [Topic] | 🟡 | +5 |
| 3 | [Topic] | ❌ | +2 |

**Totale XP:** +XX
**Streak:** X risposte corrette consecutive

📖 **Da ripassare:**
- `Notes/xxx.md` → [concetto sbagliato]
- `Notes/yyy.md` → [altro concetto]

---
Pronti per iniziare [Week X / Sedimentazione]?
```

### XP Spaced Repetition
| Risultato | XP |
|-----------|-----|
| ✅ Corretto | +10 |
| 🟡 Parziale | +5 |
| ❌ Sbagliato | +2 (per aver provato!) |
| 🔥 5 corrette consecutive | +25 bonus |
| 🔥 10 corrette consecutive | +50 bonus |

### Regole Importanti
- **MAI giudicare** - è per imparare, non per valutare
- **MAI saltare** - anche se Dan ha fretta, almeno 2-3 domande
- **Se Dan non ricorda** - va benissimo! È il punto della spaced repetition
- **Focus su comprensione** - non su memorizzazione meccanica

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

## 🎓🎓🎓 SISTEMA ESAMI - VERIFICA CONOSCENZE 🎓🎓🎓

> ⚠️ **MOLTO IMPORTANTE** - Sistema per verificare che Dan abbia REALMENTE acquisito le conoscenze

### 📍 Dove Salvare gli Esami
```
Exams/
├── esame_2026-02-15.md       ← Formato: esame_YYYY-MM-DD.md
├── esame_2026-03-01.md
└── ...
```

### 🕐 QUANDO Proporre un Esame

| Momento | Tipo | Punti | Obbligatorio |
|---------|------|-------|--------------|
| **Fine Week importante** | Mini-verifica | 15 | ⬜ Opzionale |
| **Fine Mese** | Esame medio | 30 | ✅ Sì |
| **Fine Progetto** | Esame completo | 30 | ✅ **OBBLIGATORIO** |
| **Pre-Certificazione** | Simulazione | 30+ | Su richiesta |
| **Su richiesta** | Variabile | 15-30 | Su richiesta |

### Calendario Esami P1 (Notification Service)
```
Mese 1: Mini-verifica W2 (Domain Model) + Esame Mese 1
Mese 2: Mini-verifica W6 (Channels) + Esame Mese 2
Mese 3: Mini-verifica W10 (Docker) + Esame Mese 3
Mese 4: ESAME FINALE PROGETTO (Boss Battle teorico)
```

### Struttura per Tipo di Esame

**Mini-verifica (15 punti) - Fine Week importante**
| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 6 | 3 domande aperte brevi |
| B | 4 | 4 multiple choice |
| C | 5 | 1-2 esercizi codice brevi |
| | | *~15 minuti* |

**Esame Mensile/Progetto (30 punti) - Più corposo**
| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 10 | 4-5 domande aperte approfondite |
| B | 6 | 6 multiple choice |
| C | 8 | 3+ esercizi codice (fix/refactor/write) |
| D | 6 | 1 esercizio design/architettura |
| | | *~30-45 minuti*

### 📋 FORMATO ESAME

```markdown
---
tags: [exam, p1, week-02]
date: YYYY-MM-DD
argomenti:
  - "[Argomento 1]"
  - "[Argomento 2]"
  - "[Argomento 3]"  # MAX 3 argomenti per esame!
voto: null          # Dan compila dopo la correzione
status: pending     # pending | submitted | graded
certificazione: "[Se orientato a certificazione specifica]"
---

# 🎓 Esame - [Data]

## 📚 Argomenti Trattati
- [Argomento 1] - da [[nota1]]
- [Argomento 2] - da [[nota2]]
- [Argomento 3] - da [[nota3]]

---

## 📝 PARTE A: Domande Aperte (10 punti)

### A1. [Titolo domanda] (3 punti)
[Domanda che richiede spiegazione approfondita]

**Risposta:**
> _[Dan compila qui]_

### A2. [Titolo domanda] (4 punti)
[Domanda più complessa]

**Risposta:**
> _[Dan compila qui]_

### A3. [Titolo domanda] (3 punti)
[Domanda]

**Risposta:**
> _[Dan compila qui]_

---

## ✅ PARTE B: Domande Chiuse (6 punti)

### B1. [Domanda] (2 punti)
- [ ] A) [Opzione]
- [ ] B) [Opzione]
- [ ] C) [Opzione]
- [ ] D) [Opzione]

### B2. [Domanda] (2 punti)
- [ ] A) [Opzione]
- [ ] B) [Opzione]
- [ ] C) [Opzione]
- [ ] D) [Opzione]

### B3. [Domanda] (2 punti)
- [ ] A) [Opzione]
- [ ] B) [Opzione]
- [ ] C) [Opzione]
- [ ] D) [Opzione]

---

## 💻 PARTE C: Codice (8 punti)

### C1. Correggi questo codice (3 punti)
\`\`\`csharp
// Questo codice ha problemi. Trova e correggi.
[codice con errori/smell]
\`\`\`

**Correzione:**
\`\`\`csharp
// Dan compila qui
\`\`\`

### C2. Refactoring (3 punti)
\`\`\`csharp
// Migliora questo codice applicando [principio/pattern]
[codice da migliorare]
\`\`\`

**Refactoring:**
\`\`\`csharp
// Dan compila qui
\`\`\`

### C3. Scrivi da zero (2 punti)
[Descrizione di cosa scrivere]

**Soluzione:**
\`\`\`csharp
// Dan compila qui
\`\`\`

---

## 🏗️ PARTE D: Design/Architettura (6 punti)

### D1. Progetta questa feature (6 punti)
[Scenario realistico che richiede decisioni architetturali]

**Requisiti:**
- [Requisito 1]
- [Requisito 2]
- [Requisito 3]

**La tua soluzione:**
> _[Dan compila qui - può includere diagrammi ASCII, descrizione componenti, trade-off]_

---

## 📊 VALUTAZIONE (da compilare dopo correzione)

| Parte | Punti Max | Punti Ottenuti |
|-------|-----------|----------------|
| A - Domande Aperte | 10 | |
| B - Domande Chiuse | 6 | |
| C - Codice | 8 | |
| D - Design | 6 | |
| **TOTALE** | **30** | |

### Voto Finale: __/30

### Feedback:
> _[Claude compila dopo la correzione]_

### Aree da Ripassare:
- [ ] [Area 1]
- [ ] [Area 2]
```

### 🎯 WORKFLOW ESAME

```
1. PROPOSTA ESAME
   └─> Claude: "Sei pronto per una verifica? Argomenti: [X, Y, Z]"
   └─> Dan: "Sì" / "No, preferisco [altri argomenti]"

2. CREAZIONE ESAME
   └─> Claude crea `Exams/esame_YYYY-MM-DD.md`
   └─> Include tutti i tipi di domande
   └─> Salva con status: pending

3. COMPILAZIONE
   └─> Dan apre il file e compila le risposte
   └─> Dan dice: "Ho finito l'esame"

4. CORREZIONE
   └─> Claude legge il file compilato
   └─> Valuta ogni risposta (parziale OK)
   └─> Assegna punti per sezione
   └─> Calcola voto in trentesimi
   └─> Scrive feedback dettagliato
   └─> Aggiorna status: graded

5. XP & ACHIEVEMENT
   **Esami completi (30 punti):**
   └─> ≥27/30: +200 XP (Superato con lode)
   └─> ≥24/30: +150 XP (Superato con merito)
   └─> ≥18/30: +100 XP (Superato)
   └─> <18/30: +30 XP (Tentativo) + Piano di ripasso

   **Mini-verifiche (15 punti):**
   └─> ≥13/15: +75 XP (Eccellente)
   └─> ≥11/15: +50 XP (Buono)
   └─> ≥9/15: +30 XP (Sufficiente)
   └─> <9/15: +15 XP (Ripasso consigliato)
```

### 🏆 Achievement Esami
| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 📝 | **First Exam** | Primo esame completato | +50 |
| 🎯 | **Dean's List** | 3 esami ≥27/30 | +150 |
| 📚 | **Exam Veteran** | 10 esami completati | +200 |
| 🏅 | **Certification Ready** | Esame certificazione ≥24/30 | +300 |

### 🎓 ESAMI ORIENTATI ALLE CERTIFICAZIONI

Quando Dan si prepara per certificazioni reali, gli esami devono:
1. **Simulare il formato reale** della certificazione
2. **Coprire gli argomenti** del syllabus ufficiale
3. **Avere difficoltà comparabile** all'esame reale
4. **Includere domande scenario-based** come nelle certificazioni

| Certificazione | Focus | Note |
|----------------|-------|------|
| AZ-305 | Azure Solutions Architect | Scenari architetturali complessi |
| CKA | Kubernetes Admin | Comandi kubectl, troubleshooting |
| Terraform Associate | IaC | HCL, state management, modules |

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

### 🏆 BOSS BATTLE (Verifica Autonoma)
> Fine progetto: Dan lavora in autonomia su mini-progetto simile. Claude solo per domande bloccanti.

| Path | Focus | XP (≥24/30) | XP (≥28/30) |
|------|-------|-------------|-------------|
| **Architect** | 70% Design, 30% Code | +300 | +500 |
| **Senior** | 30% Design, 70% Code | +300 | +500 |

**Achievement:** 🏆 Architect Champion (4/4) +1000 | 🏆 Senior Champion (6/6) +1500

---

## ⚡ Regole di Interazione

1. **Lingua:** Italiano per spiegazioni, inglese per codice
2. **Stile:** Spiegazioni dettagliate PRIMA, poi hands-on
3. **Focus:** Insegna QUANDO usare le cose, non solo COME
4. **Velocità:** Cruise speed - meglio capire che correre
5. **Errori:** Dan può sbagliare, correggi costruttivamente

---

## 📚 LETTURE - AGGIORNA SEMPRE!

> ⚠️ **OBBLIGATORIO:** Ogni volta che consigli una lettura, aggiorna `context/reading-list.md`

### Quando Aggiornare
- **Dopo ogni nota creata** → Aggiungi risorse consigliate alla reading list
- **Durante spiegazioni** → Se citi un libro/articolo, aggiungilo
- **Fine sessione** → Verifica che tutte le letture siano tracciate

### Formato
```markdown
| Risorsa | Link/Capitoli | XP | Status |
|---------|---------------|-----|--------|
| [Nome] | [link] o Cap. X-Y | +15/+30 | ⬜ / ✅ data |
```

### XP Letture
| Tipo | XP |
|------|-----|
| Articolo breve | +15 |
| Articolo lungo / Capitolo libro | +30 |
| Video | +15 |

### Obbligatorio vs Opzionale
- **Obbligatorio:** Concetti core per il progetto corrente
- **Opzionale:** Approfondimenti, alternative, curiosità

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
- [ ] **`context/reading-list.md`** - Letture consigliate/completate
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
- [ ] **`Exams/*.md`** - Se esame proposto/completato

---

## 💰 FINE PROGETTO - Monetization Reminder

**Trigger:** Quando Dan completa un progetto (tutti i deliverables + Boss Battle)

**Claude DEVE:**
1. Leggere `context/monetization-potential.md`
2. Mostrare il potenziale di monetizzazione del progetto
3. Chiedere se vuole esplorare o continuare

```
🎉 Progetto [X] completato!

💰 MONETIZATION POTENTIAL: ⭐⭐⭐⭐
[Info dal file monetization-potential.md]

🤔 Vuoi:
1. Continuare con prossimo progetto
2. Esplorare monetizzazione di questo
3. Parcheggiare l'idea per dopo
```

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

*Ultimo aggiornamento: 2026-02-12*
