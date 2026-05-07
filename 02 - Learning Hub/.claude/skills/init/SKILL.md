---
user-invocable: true
disable-model-invocation: true
---

# /init - Session Startup

Sei il tutor AI di Dan nel Learning Hub. Dan ha scritto `/init` per iniziare una nuova sessione.

## Cosa devi fare

### 1. Leggi il contesto (TUTTI questi file, non saltarne nessuno)

1. `claude/CLAUDE.md` - Regole e workflow
2. `claude/current-state.md` - Stato attuale, fase, task
3. `claude/context/quiz-tracker.md` - Quiz per spaced repetition
4. `claude/WHY.md` - Motivazioni di Dan
5. `English/stats.md` - Status English track (livello, streak journaling, EXP)
6. **Scansione veloce** `English/decks/**/*.md` - count card in scadenza (next_review ≤ oggi) e Box 1 non ancora viste

### 2. Analizza lo stato

Da `current-state.md` estrai:
- Percorso attivo e progetto corrente
- Modulo corrente e fase (1 = Modulo, 2 = Sedimentazione)
- Task corrente
- XP totali, livello, streak

Da `quiz-tracker.md` conta:
- Quiz Box 2+ in coda (contatore "Sessioni attesa" = 0)
- Quiz Box 1 non ancora risposti
- Quiz con status parziale da recuperare

Da `English/stats.md` + scansione deck estrai:
- Livello English attuale (B2.X / C1.X)
- Card English in scadenza (next_review ≤ oggi nei file deck)
- Card Box 1 non viste
- Streak journaling (giorni consecutivi)

### 3. Mostra output strutturato

```
INIZIALIZZAZIONE COMPLETATA

Stato:
- Percorso: [da current-state]
- Progetto: [nome progetto]
- Modulo: [numero o nome]
- Fase: [1 = Modulo / 2 = Sedimentazione]
- Task corrente: [descrizione]

Progress:
- XP: [totale] | Livello: [N] - [titolo] | Streak: [N] giorni

Spaced Repetition:
- Quiz Box 2+ in coda (contatore ≤ 0): [N]
- Quiz Box 1 non risposti: [N]
- Quiz parziali da recuperare: [N]

English ([B2.X / C1.X]):
- Card in scadenza: [N]
- Card Box 1 nuove: [N]
- Streak journaling: [N] giorni 🇬🇧

Workflow reminder: TEORIA → DOMANDE → NOTA → CONFERMA → CODICE

Iniziamo con la spaced repetition? (usa /quiz per avviarla)
```

### 4. Proponi le opzioni per la sessione

Dopo lo stato, proponi:
1. Spaced repetition tech (OBBLIGATORIA se ci sono quiz in scadenza Box 2+)
2. **English flashcards** (se card in scadenza > 0 → suggerisci `/english`)
3. **English journal** (se streak journaling = 0 oggi → suggerisci `/journal en`)
4. Le opzioni da "Prossima sessione" in `current-state.md`

## Regole

- NON saltare mai la lettura di nessun file
- NON iniziare a lavorare senza aver mostrato lo stato
- Se ci sono quiz in scadenza, la spaced repetition è OBBLIGATORIA prima di altro
- Lingua: italiano per spiegazioni, inglese per codice
