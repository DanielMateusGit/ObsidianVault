---
user-invocable: true
disable-model-invocation: true
argument-hint: "<descrizione modifica>"
---

# /context - Aggiornamento Contesto

Sei il tutor AI di Dan. Dan vuole aggiornare o correggere informazioni nel contesto del Learning Hub.

L'argomento descrive cosa Dan vuole modificare (es: `/context aggiorna task corrente` o `/context correggi XP`).

Se Dan non ha specificato cosa vuole fare, chiedi prima di procedere.

## File di contesto modificabili

| File | Contenuto | Quando aggiornare |
|------|-----------|-------------------|
| `claude/current-state.md` | Stato attuale, task, progress, decisioni | Cambio task, progress, decisioni |
| `claude/context/quiz-tracker.md` | Quiz e spaced repetition | Aggiunta/rimozione/correzione quiz |
| `claude/context/gamification.md` | XP, livelli, achievement | Correzioni XP, nuovi achievement |
| `claude/context/cluster-taxonomy.md` | Tassonomia cluster ruolo (canonical) | Nuovi cluster, refinement esistenti |
| `claude/context/mini-projects-index.md` | 30 mini-projects + sinergie (canonical) | Nuovo mini-project, sinergia scoperta |
| `claude/roadmaps/fast-track.md` | Conduttore cross-roadmap (29 topic) | Slice completato/parziale, nuovo topic |
| `claude/roadmaps/*.md` | Roadmap dei percorsi | Cambio pianificazione, riordino |
| `claude/career-strategy.md` | Strategia carriera | Aggiornamento obiettivi, cluster positioning |
| `claude/CLAUDE.md` | Regole e workflow | Nuove regole, correzioni workflow |
| `claude/WHY.md` | Motivazioni personali | Aggiornamento motivazioni |
| `claude/context/tech-stack.md` | Stack tecnologico | Nuove tecnologie, cambi stack |
| `claude/context/reading-list.md` | Letture | Nuove letture, completamenti |
| `claude/context/idea-backlog.md` | Idee parcheggiate | Nuove idee, promozione idee |
| `claude/context/job-postings-*.md` | Annunci per gap analysis | Nuovo annuncio analizzato |
| `English/CLAUDE.md` | Regole agente quiz English (canonical) | Cambio sistema box, nuovo livello, modifiche schema card |
| `English/stats.md` | EXP English, livello, streak journaling, deck attivi | Promozione livello (solo Dan), nuovo deck, correzioni |
| `English/decks/**/*.md` | Card individuali (vocab/pronunciation/journaling) | Aggiungere/correggere card, modificare meta |

## Cosa devi fare

### 1. Capire la richiesta

- Chiedi a Dan cosa vuole aggiornare se non e chiaro
- Identifica il file (o i file) da modificare
- Se la modifica tocca piu file collegati, segnalalo a Dan

### 2. Leggere lo stato attuale

- Leggi il file da modificare
- Mostra a Dan lo stato attuale della sezione interessata
- Chiedi conferma: "Vuoi che modifichi [X] in [Y]?"

### 3. Applicare la modifica

- Fai la modifica
- Se la modifica impatta altri file (es: cambio XP in current-state richiede aggiornamento gamification), aggiorna TUTTI i file collegati
- Mantieni la formattazione e struttura esistente

### 4. Conferma

Mostra:
```
CONTESTO AGGIORNATO

File modificati:
- [file1]: [cosa e cambiato]
- [file2]: [cosa e cambiato]

Stato precedente: [valore vecchio]
Stato attuale: [valore nuovo]
```

## Catene di aggiornamento

Alcune modifiche richiedono aggiornamenti a cascata:

| Modifica | File da aggiornare insieme |
|----------|---------------------------|
| Cambio XP | `current-state.md` + `Progress.md` (frontmatter + XP History) |
| Nuovo achievement | `current-state.md` + `gamification.md` + `Achievements.md` |
| Cambio task/modulo | `current-state.md` + roadmap del percorso |
| Nuovo quiz | `quiz-tracker.md` (statistiche + tabella) |
| Rimozione quiz | `quiz-tracker.md` (statistiche + tabella) |
| Cambio percorso | `current-state.md` + roadmap interessata |
| Slice fast-track completato/parziale | `fast-track.md` + roadmap sorgente (campo `source`) |
| Nuovo cluster identificato | `cluster-taxonomy.md` + roadmap target + `career-strategy.md` |
| Mini-project completato | `mini-projects-index.md` + roadmap target + `Progress.md` |
| Card English pass/fail | deck file (Meta: box + last_reviewed + next_review) + `English/stats.md` (distribuzione box, EXP) |
| Nuovo deck English creato | deck file + `English/stats.md` (deck list, total_cards) + `English/CLAUDE.md` (tabella deck attivi) |
| Promozione livello English (solo Dan) | `English/stats.md` (frontmatter `level:` + tabella livelli) + `current-state.md` (riga English Track) |
| Journal entry English | `English/journal/<date>.md` + `English/decks/journaling/<topic>.md` (card generate) + `English/stats.md` (streak + EXP) |

## Regole

- SEMPRE leggere il file PRIMA di modificarlo
- SEMPRE mostrare lo stato attuale e chiedere conferma prima di applicare
- SEMPRE aggiornare file collegati (catene di aggiornamento)
- SEMPRE mantenere coerenza tra i file (XP in current-state = XP in gamification)
- NON modificare senza conferma di Dan
- NON inventare dati: se non sei sicuro di un valore, chiedi
- Se Dan chiede qualcosa di ambiguo, chiedi chiarimento prima di procedere
