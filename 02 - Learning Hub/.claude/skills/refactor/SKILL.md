# /refactor - Analisi e Miglioramento Contesto Progetto

> Skill "pensante": analizza l'intero sistema di contesto, trova incoerenze, propone e applica fix.
> Obiettivo: mantenere il contesto sempre sincronizzato per ridurre errori e tempi di onboarding.

---

## Quando Usarla

- Periodicamente (ogni 2-4 settimane, o dopo cambiamenti strategici importanti)
- Quando Claude sembra "confuso" o dà risposte incoerenti
- Dopo un pivot (es. cambio obiettivo, nuovo percorso)
- Quando Dan dice "facciamo un check del progetto"

---

## Step 1: Raccolta Contesto (Lettura Completa)

Leggi TUTTI questi file, senza eccezioni:

### Core
```
claude/CLAUDE.md              → Regole operative
claude/current-state.md       → Stato attuale (SOURCE OF TRUTH per stato)
claude/WHY.md                 → Motivazioni
claude/profile.md             → Profilo Dan
claude/career-strategy.md     → Strategia carriera
```

### Roadmaps
```
claude/roadmaps/senior-engineer.md
claude/roadmaps/architect-quest.md
claude/roadmaps/ai-skills.md
claude/roadmaps/career-boost.md
claude/roadmaps/senior-frontend.md
```

### Context
```
claude/context/gamification.md
claude/context/quiz-tracker.md     (almeno prime 200 righe + statistiche)
claude/context/tech-stack.md
claude/context/learning-style.md
claude/context/reading-list.md
claude/context/idea-backlog.md
claude/context/monetization-potential.md
claude/context/course-claude-code.md (se esiste)
```

### Supporto
```
claude/QUICK-REFERENCE.md
claude/PROMPT.md
claude/future.md
claude/context/files.md
```

### Skills
```
.claude/skills/*/SKILL.md     → Tutte le skill attive
```

---

## Step 2: Analisi (Le 5 Dimensioni)

Per ogni dimensione, assegna un voto: OK / WARN / CRITICAL.

### 2.1 Coerenza dei Dati

Verifica che le stesse informazioni siano consistenti tra file diversi:

| Dato | Source of Truth | File da verificare |
|------|-----------------|-------------------|
| XP, Livello, Streak | `current-state.md` | QUICK-REFERENCE, gamification, Progress.md |
| Percorso attivo, Week | `current-state.md` | Roadmap corrispondente |
| Obiettivo primario | `career-strategy.md` | profile.md, WHY.md, CLAUDE.md |
| Skill disponibili | `.claude/skills/` (filesystem) | CLAUDE.md (tabella slash commands) |
| Progetti e numerazione | Roadmaps | monetization-potential, idea-backlog, career-strategy |
| Tech stack | `tech-stack.md` | files.md (se esiste) |
| Quiz stats | `quiz-tracker.md` (conteggio reale) | Statistiche dichiarate in testa al file |

**Red flags:**
- Numeri diversi per lo stesso dato in file diversi
- Obiettivi che non corrispondono tra profile/career-strategy/WHY
- Skill elencate in CLAUDE.md che non esistono nel filesystem (o viceversa)
- Progetti referenziati con nomi/numeri diversi

### 2.2 Completezza delle Roadmap

Per ogni roadmap attiva:

- [ ] Ha timeline esplicita (settimane/mesi)?
- [ ] Ogni progetto ha: obiettivi, deliverables, criteri di completamento?
- [ ] C'e breakdown settimanale per il progetto corrente?
- [ ] Le dipendenze tra progetti sono chiare?
- [ ] I prerequisiti sono espliciti?
- [ ] Il progresso attuale in current-state.md corrisponde alla roadmap?

**Red flags:**
- Roadmap che dice "Week 5 prossima" ma current-state dice altra cosa
- Progetti senza deliverables chiari
- Timeline irrealistiche (troppi task in poco tempo)

### 2.3 Contenuto Stale (Obsoleto)

Per ogni file, verifica:

- [ ] "Ultimo aggiornamento" corrisponde all'ultima modifica reale?
- [ ] Dati snapshot (XP, level, week) sono ancora corretti?
- [ ] Template/placeholder non compilati in file "completati"?
- [ ] File legacy che duplicano funzionalita ora coperte da skill?

**Red flags:**
- File con "Ultimo aggiornamento: 2026-02-XX" che contengono dati dinamici mai aggiornati
- Sezioni "TODO" o "[placeholder]" in file completati
- File che dicono "legacy" nel commento ma non sono archiviati

### 2.4 Duplicazione

Cerca contenuto duplicato tra file:

| Rischio duplicazione | File coinvolti |
|---------------------|---------------|
| Tech stack | `tech-stack.md` vs `files.md` |
| Learning style | `learning-style.md` vs `files.md` |
| Gamification | `gamification.md` vs `files.md` |
| Protocollo init | `PROMPT.md` vs `/init` skill |
| Quick reference vs CLAUDE.md | QUICK-REFERENCE.md vs CLAUDE.md |
| Future vs career-strategy | future.md vs career-strategy.md |

**Principio:** Ogni dato deve vivere in UN SOLO file. I riferimenti devono essere link, non copie.

### 2.5 Robustezza Organizzativa

Valuta la struttura complessiva:

- [ ] Un nuovo Claude puo sincronizzarsi leggendo solo CLAUDE.md + current-state.md?
- [ ] I file hanno responsabilita chiare e non sovrapposte?
- [ ] Il flusso di lettura (Quick Start in CLAUDE.md) e corretto e sufficiente?
- [ ] Le skill coprono tutti i workflow principali?
- [ ] Gli hook validano correttamente?
- [ ] Le decisioni attive in current-state.md sono ancora valide?

---

## Step 3: Report

Genera un report strutturato:

```markdown
# Refactor Report — YYYY-MM-DD

## Sommario

| Dimensione | Stato | Issues |
|-----------|-------|--------|
| Coerenza dati | OK/WARN/CRITICAL | N |
| Completezza roadmap | OK/WARN/CRITICAL | N |
| Contenuto stale | OK/WARN/CRITICAL | N |
| Duplicazione | OK/WARN/CRITICAL | N |
| Robustezza org. | OK/WARN/CRITICAL | N |

## Dettaglio Issues

### [CRITICAL] Issue-001: Titolo
- **File:** path/to/file.md
- **Problema:** Descrizione concreta
- **Fix proposto:** Cosa fare
- **Impatto:** Cosa succede se non fixiamo

### [WARN] Issue-002: Titolo
...

## Cosa VA BENE (non toccare)
- Lista di cose che funzionano correttamente

## Fix Proposti (in ordine di priorita)
1. [CRITICAL] ...
2. [WARN] ...
3. [LOW] ...
```

---

## Step 4: Conferma e Applicazione

1. **Mostra il report a Dan**
2. **Chiedi conferma:** "Applico tutti i fix? Oppure vuoi selezionare quali?"
3. **Applica i fix confermati** — modifica i file
4. **Per ogni file modificato:** mostra before/after (diff conciso)
5. **NON toccare** file marcati come "va bene"

### Regole di Applicazione

- **CRITICAL:** Proponi sempre il fix, applica dopo conferma
- **WARN:** Proponi il fix, chiedi se procedere
- **LOW:** Segnala ma non applicare automaticamente
- **Mai inventare dati** — se un dato manca, chiedi a Dan
- **Mai eliminare file** senza conferma esplicita — al massimo archivia o svuota le parti duplicate
- **Aggiorna "Ultimo aggiornamento"** su ogni file modificato

---

## Step 5: Recap

Dopo aver applicato i fix:

```markdown
## Refactor Completato — YYYY-MM-DD

### Modifiche Applicate
| File | Tipo modifica | Descrizione |
|------|--------------|-------------|
| ... | Fix coerenza | ... |

### File Non Toccati
- [lista file che erano gia OK]

### Prossimo Refactor Consigliato
- Data suggerita: YYYY-MM-DD (tra ~2-4 settimane)
- Focus: [cosa monitorare nel frattempo]
```

Se le modifiche sono significative, crea un session log in `claude/sessions/` con il dettaglio.

---

## Principi Guida

1. **Se va bene, non toccare** — Zero modifiche cosmetiche
2. **Source of Truth chiara** — Ogni dato vive in un posto solo
3. **Link, non copie** — Riferisci ad altri file, non duplicare contenuto
4. **Stale e peggio di assente** — Un dato vecchio confonde piu di nessun dato
5. **Minimo necessario** — Ogni file deve giustificare la sua esistenza
6. **Dan conferma** — Nessuna modifica strutturale senza OK esplicito
