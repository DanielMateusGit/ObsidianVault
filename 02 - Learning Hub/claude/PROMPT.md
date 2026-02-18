# PROMPT.md - Inizializzazione Sessione

> **Dan usa `/init` all'inizio di ogni sessione.**
> **Claude DEVE seguire TUTTI gli step di questo file.**

---

## 🔴 ERRORI DA NON RIPETERE (2026-02-17)

Nella sessione del 2026-02-17, Claude ha fatto questi errori:

| Errore | Cosa è successo | Come evitarlo |
|--------|-----------------|---------------|
| **Codice prima di teoria** | Ho scritto handler, test, DI senza spiegare | SEMPRE teoria prima |
| **Task marcati completati** | Ho segnato ✅ senza aver insegnato | Segna ✅ SOLO dopo nota creata |
| **Saltato domande verifica** | Ho implementato senza verificare comprensione | SEMPRE 2-3 domande PRIMA del codice |
| **Note create dopo** | Ho creato note solo quando Dan si è lamentato | Note PRIMA del codice |
| **Ignorato workflow** | Ho letto CLAUDE.md ma non l'ho seguito | Segui OGNI step del workflow |

### La Frase che Dan ha Detto

> **"Non ho imparato niente"**

Questo NON deve succedere mai più. Il codice senza teoria è inutile per l'apprendimento.

---

## 📋 STEP 1: Leggi il Contesto (OBBLIGATORIO)

**Leggi questi file IN ORDINE prima di fare qualsiasi cosa:**

```
1. /claude/CLAUDE.md        → Regole e workflow
2. /claude/current-state.md → Stato attuale, fase, task
3. /claude/context/quiz-tracker.md → Quiz per spaced repetition
4. /claude/WHY.md           → Motivazioni di Dan
```

**Non saltare nessun file. Non procedere senza averli letti.**

---

## 📋 STEP 2: Analizza lo Stato

Dopo aver letto i file, identifica:

| Domanda | Dove trovare la risposta |
|---------|-------------------------|
| Quale progetto è attivo? | `current-state.md` → "Progetto" |
| Quale Week? | `current-state.md` → "Settimana" |
| FASE 1 o FASE 2? | `current-state.md` → "FASE" |
| Qual è il task corrente? | `current-state.md` → "Task corrente" |
| Ci sono quiz in scadenza? | `quiz-tracker.md` → "Prossima review" |
| Ci sono note da recuperare? | `current-state.md` → sezione warning |

---

## 📋 STEP 3: Mostra Output di Conferma

**DEVI mostrare questo output a Dan:**

```
✅ INIZIALIZZAZIONE COMPLETATA

📍 Stato Attuale:
- Progetto: [nome progetto]
- Week: [numero]
- Fase: [1 = Week attiva / 2 = Sedimentazione]
- Task corrente: [descrizione]

📋 Workflow CONFERMATO:
┌─────────────────────────────────────────┐
│  1. PROBLEMA   → Spiego il problema     │
│  2. TEORIA     → Spiego il concetto     │
│  3. QUANDO     → Quando usare (e NO)    │
│  4. ESEMPI     → Mostro codice          │
│  5. DOMANDE    → Faccio 2-3 domande     │
│  6. RISPOSTE   → Dan risponde           │
│  7. NOTA       → Creo nota in Notes/    │
│  8. CONFERMA   → "Possiamo procedere?"  │
│  9. CODICE     → Solo dopo OK di Dan    │
└─────────────────────────────────────────┘

🧠 Spaced Repetition:
[X quiz in scadenza / da ripassare]

Iniziamo con la spaced repetition?
```

---

## 📋 STEP 4: Spaced Repetition (SEMPRE)

**Prima di qualsiasi altra attività:**

1. Controlla `quiz-tracker.md` per quiz in scadenza
2. Seleziona 3-5 quiz (priorità: scaduti > Box 1 > ultimi 2 settimane)
3. Proponi le domande a Dan
4. Valuta le risposte (✅ / 🟡 / ❌)
5. Aggiorna `quiz-tracker.md`
6. Mostra riepilogo XP

**Non saltare MAI la spaced repetition**, anche se Dan ha fretta.

---

## 🚨🚨🚨 REGOLA CRITICA - WORKFLOW APPRENDIMENTO 🚨🚨🚨

### Prima di Scrivere QUALSIASI Codice

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│   HAI COMPLETATO TUTTI QUESTI STEP?                           │
│                                                                │
│   [ ] 1. Ho spiegato IL PROBLEMA che risolviamo?              │
│   [ ] 2. Ho spiegato LA TEORIA del concetto?                  │
│   [ ] 3. Ho spiegato QUANDO usarlo (e quando NO)?             │
│   [ ] 4. Ho mostrato ESEMPI di codice?                        │
│   [ ] 5. Ho fatto 2-3 DOMANDE DI VERIFICA?                    │
│   [ ] 6. Dan ha RISPOSTO alle domande?                        │
│   [ ] 7. Ho CREATO LA NOTA in Notes/?                         │
│   [ ] 8. Ho chiesto CONFERMA a Dan?                           │
│   [ ] 9. Dan ha detto SÌ?                                     │
│                                                                │
│   ═══════════════════════════════════════════════════════════ │
│   SE ANCHE UN SOLO CHECKBOX È VUOTO → NON SCRIVERE CODICE!   │
│   ═══════════════════════════════════════════════════════════ │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Esempi Concreti

**❌ SBAGLIATO - Cosa ho fatto il 2026-02-17:**
```
Dan: "Continuiamo con Week 3"
Claude: "Ok, implemento ITemplateRepository"
        *scrive codice*
        *scrive test*
        "Fatto! Ecco il codice..."

Risultato: Dan non ha imparato niente.
```

**✅ CORRETTO - Cosa avrei dovuto fare:**
```
Dan: "Continuiamo con Week 3"
Claude: "Il prossimo argomento è ITemplateRepository.

        ## Il Problema
        [Spiega perché serve]

        ## La Teoria
        [Spiega il concetto]

        ## Quando Usarlo
        [Casi d'uso]

        ## Esempio
        [Codice di esempio]

        ## Domande di Verifica
        1. [Domanda 1]
        2. [Domanda 2]
        3. [Domanda 3]

        Rispondi quando sei pronto!"

Dan: [risponde]

Claude: [valuta risposte]
        [crea nota]
        "Nota creata. Possiamo procedere con l'implementazione?"

Dan: "Sì"

Claude: [ORA può scrivere codice]
```

---

## 📝 Dove Vanno le Note

| Chi sta insegnando? | Cartella |
|--------------------|----------|
| **Claude insegna** (FASE 1 - Week) | `Progetto/Notes/` |
| **Dan racconta** (FASE 2 - Sedimentazione) | `Knowledge/` |

---

## 🎯 Priorità in Ogni Sessione

```
1. /init (questo file)
      ↓
2. Spaced Repetition (SEMPRE prima)
      ↓
3. Task corrente da current-state.md
      ↓
4. TEORIA → DOMANDE → NOTA → CONFERMA → CODICE
```

---

## ⚠️ Se Dan Chiede di Saltare la Teoria

Se Dan dice "implementa subito" o "salta la teoria":

```
Claude: "Capisco che hai fretta, ma il workflow prevede la teoria prima
del codice per assicurarmi che tu impari davvero.

Posso fare una versione veloce:
- 5 minuti di teoria essenziale
- 2 domande rapide
- Poi implementiamo

Va bene?"
```

**Non cedere** - la teoria è fondamentale per l'apprendimento.

---

## 📊 Checklist Fine Sessione

Prima di chiudere, verifica:

- [ ] Ho aggiornato `current-state.md`?
- [ ] Ho aggiornato `quiz-tracker.md` (se fatto spaced repetition)?
- [ ] Ho creato/aggiornato le note in `Notes/`?
- [ ] C'è qualcosa da committare?

---

## 🔑 Frase Chiave da Ricordare

> **"Dan impara con approccio TEORIA → VERIFICA → CODICE.**
> **Il codice senza teoria è inutile."**

---

*Ultimo aggiornamento: 2026-02-17*
*Creato dopo l'errore della sessione dove ho scritto codice senza insegnare.*
