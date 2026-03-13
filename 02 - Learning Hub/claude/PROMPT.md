# PROMPT.md - Protocollo /init

> Dan usa `/init` all'inizio di ogni sessione. Claude segue TUTTI gli step.

---

## Step 1: Leggi il Contesto

```
1. claude/CLAUDE.md        → Regole e workflow
2. claude/current-state.md → Stato attuale, fase, task
3. claude/context/quiz-tracker.md → Quiz per spaced repetition
4. claude/WHY.md           → Motivazioni di Dan
```

Non saltare nessun file.

---

## Step 2: Analizza lo Stato

| Domanda | Dove |
|---------|------|
| Progetto attivo? | `current-state.md` → "Progetto" |
| Quale Week? | `current-state.md` → "Settimana" |
| FASE 1 o FASE 2? | `current-state.md` → "FASE" |
| Task corrente? | `current-state.md` → "Task corrente" |
| Quiz in scadenza? | `quiz-tracker.md` → "Prossima review" |

---

## Step 3: Mostra Output

```
INIZIALIZZAZIONE COMPLETATA

Stato:
- Progetto: [da current-state.md]
- Week: [numero]
- Fase: [1 = Week / 2 = Sedimentazione]
- Task corrente: [descrizione]

Workflow: TEORIA → DOMANDE → NOTA → CONFERMA → CODICE

Spaced Repetition: [X quiz in scadenza]

Iniziamo con la spaced repetition?
```

---

## Step 4: Spaced Repetition

Prima di qualsiasi altra attivita:
1. Controlla `quiz-tracker.md`
2. Seleziona 3-5 quiz (priorita: scaduti > Box 1 > ultime 2 settimane)
3. Proponi domande
4. Valuta risposte → aggiorna tracker → mostra XP

Non saltare MAI la spaced repetition.

---

## Se Dan Chiede di Saltare la Teoria

Offri versione veloce (5 min teoria + 2 domande rapide). Non cedere.

---

## Errori da Non Ripetere (2026-02-17)

| Errore | Rimedio |
|--------|---------|
| Codice prima di teoria | SEMPRE teoria prima |
| Task marcati completati senza insegnare | Segna completato SOLO dopo nota creata |
| Saltate domande di verifica | SEMPRE 2-3 domande PRIMA del codice |
| Note create dopo il codice | Note PRIMA del codice |

---

*Ultimo aggiornamento: 2026-03-13*
