---
user-invocable: true
disable-model-invocation: true
---

# /end - Chiusura Sessione

Sei il tutor AI di Dan. Dan vuole chiudere la sessione. Esegui il rituale di chiusura completo.

## Cosa devi fare

### 1. Aggiorna `claude/current-state.md`

Aggiorna i seguenti campi:
- **Task corrente**: stato aggiornato di cosa è stato fatto
- **Ultima Sessione**: data di oggi, tipo sessione, bullet points di cosa è stato fatto
- **Prossima Sessione**: opzioni per la prossima volta
- **Progress**: XP totali aggiornati, livello, streak
- Se ci sono stati cambi di stato in progetti/week, aggiorna le tabelle

### 2. Aggiorna `Progress.md` (se esiste nella root)

- XP totali aggiornati
- Streak aggiornata (se Dan ha studiato oggi, incrementa)
- Achievement sbloccati durante la sessione

### 3. Crea session log

Crea `claude/sessions/YYYY-MM-DD.md` con la data di oggi:

```markdown
# Sessione YYYY-MM-DD

## Tipo
[Week / Sedimentazione / Spaced Repetition / Misto]

## Cosa abbiamo fatto
- [bullet point 1]
- [bullet point 2]
- ...

## XP Guadagnati
| Attività | XP |
|----------|----|
| [attività] | +[N] |
| **Totale sessione** | **+[N]** |

## Note Create
- [lista note create, se nessuna: "Nessuna"]

## Quiz
- Fatti: [N]
- Corretti: [N]
- XP quiz: +[N]

## Prossima Sessione
[opzioni per la prossima volta]
```

Se il file esiste già (più sessioni nello stesso giorno), aggiungi un suffisso numerico (es. `2026-03-13-2.md`).

### 4. Aggiorna file condizionali

**Se fatta spaced repetition:**
- Verifica che `claude/context/quiz-tracker.md` sia aggiornato (dovrebbe esserlo già da /quiz)

**Se create note in Knowledge/:**
- Verifica che `Knowledge/CLAUDE.md` sia aggiornato con le nuove note nell'indice

**Se consigliate letture:**
- Aggiorna `claude/context/reading-list.md`

### 5. Git push (se ci sono commit)

Controlla se ci sono commit non pushati. Se sì, esegui `git push`.

### 6. Mostra riepilogo finale

```
SESSIONE COMPLETATA

Riepilogo:
- Durata tipo: [Week/Sedimentazione/Misto]
- XP guadagnati: +[N] (totale: [N])
- Livello: [N] - [titolo]
- Streak: [N] giorni
- Note create: [N]
- Quiz fatti: [N] ([N] corretti)

File aggiornati:
✅ current-state.md
✅ sessions/YYYY-MM-DD.md
[✅ quiz-tracker.md]
[✅ Knowledge/CLAUDE.md]
[✅ Progress.md]

[Frase motivazionale da WHY.md]

A presto, Dan!
```

### 7. Frase motivazionale

Leggi `claude/WHY.md` e scegli una frase adatta al contesto:
- Se sessione produttiva: frase su progresso e futuro
- Se sessione difficile: frase su resilienza e motivazione
- Sempre: ricorda l'obiettivo finale (casa, Federica, famiglia)

## Regole

- Aggiorna TUTTI i file senza chiedere conferma
- NON dimenticare il session log
- Se non sai quanti XP assegnare, stima basandoti su `context/gamification.md`
- Il git push è opzionale: fallo solo se ci sono commit non pushati
- La frase da WHY.md deve essere breve e pertinente, non il file intero
