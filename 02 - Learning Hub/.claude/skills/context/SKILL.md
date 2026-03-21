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
| `claude/roadmaps/*.md` | Roadmap dei percorsi | Cambio pianificazione, riordino |
| `claude/career-strategy.md` | Strategia carriera | Aggiornamento obiettivi/timeline |
| `claude/CLAUDE.md` | Regole e workflow | Nuove regole, correzioni workflow |
| `claude/WHY.md` | Motivazioni personali | Aggiornamento motivazioni |
| `claude/context/tech-stack.md` | Stack tecnologico | Nuove tecnologie, cambi stack |
| `claude/context/reading-list.md` | Letture | Nuove letture, completamenti |
| `claude/context/idea-backlog.md` | Idee parcheggiate | Nuove idee, promozione idee |

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
| Cambio XP | `current-state.md` + `gamification.md` |
| Nuovo achievement | `current-state.md` + `gamification.md` |
| Cambio task/week | `current-state.md` + roadmap del percorso |
| Nuovo quiz | `quiz-tracker.md` (statistiche + tabella) |
| Rimozione quiz | `quiz-tracker.md` (statistiche + tabella) |
| Cambio percorso | `current-state.md` + roadmap interessata |

## Regole

- SEMPRE leggere il file PRIMA di modificarlo
- SEMPRE mostrare lo stato attuale e chiedere conferma prima di applicare
- SEMPRE aggiornare file collegati (catene di aggiornamento)
- SEMPRE mantenere coerenza tra i file (XP in current-state = XP in gamification)
- NON modificare senza conferma di Dan
- NON inventare dati: se non sei sicuro di un valore, chiedi
- Se Dan chiede qualcosa di ambiguo, chiedi chiarimento prima di procedere
