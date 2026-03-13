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

### 2. Analizza lo stato

Da `current-state.md` estrai:
- Percorso attivo e progetto corrente
- Week corrente e fase (1 = Week, 2 = Sedimentazione)
- Task corrente
- XP totali, livello, streak

Da `quiz-tracker.md` conta:
- Quiz in scadenza (data prossima review <= oggi)
- Quiz Box 1 non ancora risposti
- Quiz con status parziale da recuperare

### 3. Mostra output strutturato

```
INIZIALIZZAZIONE COMPLETATA

Stato:
- Percorso: [da current-state]
- Progetto: [nome progetto]
- Week: [numero]
- Fase: [1 = Week / 2 = Sedimentazione]
- Task corrente: [descrizione]

Progress:
- XP: [totale] | Livello: [N] - [titolo] | Streak: [N] giorni

Spaced Repetition:
- Quiz in scadenza: [N]
- Quiz Box 1 non risposti: [N]
- Quiz parziali da recuperare: [N]

Workflow reminder: TEORIA → DOMANDE → NOTA → CONFERMA → CODICE

Iniziamo con la spaced repetition? (usa /quiz per avviarla)
```

### 4. Proponi le opzioni per la sessione

Dopo lo stato, proponi:
1. Spaced repetition (OBBLIGATORIA se ci sono quiz in scadenza)
2. Le opzioni da "Prossima sessione" in `current-state.md`

## Regole

- NON saltare mai la lettura di nessun file
- NON iniziare a lavorare senza aver mostrato lo stato
- Se ci sono quiz in scadenza, la spaced repetition è OBBLIGATORIA prima di altro
- Lingua: italiano per spiegazioni, inglese per codice
