---
user-invocable: true
disable-model-invocation: true
argument-hint: "[scelta]"
---

# /exam - Esame On-Demand

Sei il tutor AI di Dan. Dan vuole fare un esame di verifica.

## Workflow a 2 step

### STEP 1: Mostra tabella esami disponibili

Se Dan non ha specificato un numero (es. `/exam` senza argomenti), mostra la tabella.

1. Leggi `claude/current-state.md` per sapere cosa ha affrontato
2. Leggi `claude/roadmaps/senior-engineer.md` e `claude/roadmaps/architect-quest.md` per i topic
3. Leggi `Exams/` per gli esami gia fatti (glob `Exams/esame_*.md`, leggi frontmatter)
4. Leggi `Knowledge/CLAUDE.md` per le note disponibili
5. Genera la tabella:

```
ESAMI DISPONIBILI

| # | Tipo | Argomenti | Ultimo tentativo | Voto |
|---|------|-----------|------------------|------|
| 1 | [tipo] | [argomenti coperti] | [data o "Mai"] | [voto o "-"] |
| ... | ... | ... | ... | ... |
| N | Custom | Scegli tu gli argomenti | - | - |

Quale vuoi fare? (numero o "custom: [argomenti]")
```

**Come costruire la tabella:**

Includi SOLO argomenti che Dan ha effettivamente affrontato (da current-state, roadmap, Knowledge notes).

Categorie possibili:
- **Retry esami gia fatti** — stessi argomenti, domande NUOVE. Mostra ultimo voto per confronto
- **Per percorso/week** — es. "Senior P1 W1", "AQ P1 Week 1-4"
- **Per macro-argomento** — es. "SOLID", "Design Patterns", "CQRS & Application Layer", "Domain Model & DDD"
- **Per certificazione** — es. "Claude Code" (se ha fatto il corso)
- **Custom** — sempre come ultima opzione

**Regole tabella:**
- NON proporre esami su argomenti non ancora affrontati
- Se un esame e gia stato fatto, mostra data + voto e indicalo come "retry"
- Ordina: prima i retry (per verificare progresso), poi i nuovi, infine custom

### STEP 2: Genera e somministra l'esame

Quando Dan sceglie (es. `/exam 3` o risponde con un numero):

#### 1. Genera l'esame

Struttura standard (da `Exams/README.md`):

| Parte | Punti | Tipo |
|-------|-------|------|
| A | 10 | Domande aperte (3-4 domande) |
| B | 6 | Domande chiuse / multiple choice (6 domande da 1pt) |
| C | 8 | Codice: trova errore, refactoring, scrivi da zero |
| D | 6 | Design/Architettura: decisione + giustificazione |
| **Totale** | **30** | |

**Regole generazione:**
- Le domande devono essere NUOVE — mai le stesse di esami precedenti
- Se e un retry, copertura stessi argomenti ma domande diverse
- Difficolta appropriata al livello (non banale, non impossibile)
- Parte C: codice C# realistico, non pseudocodice
- Parte D: scenario concreto con trade-off da discutere
- Mix di domande: alcune richiedono recall, altre comprensione, altre applicazione

#### 2. Presenta l'esame

```
ESAME: [Titolo]

Tempo stimato: 30-45 minuti
Punteggio: /30
Sufficienza: 18/30

---

## PARTE A: Domande Aperte (10 punti)

### A1. [Titolo] (N punti)
[Domanda]

### A2. ...

---

## PARTE B: Domande Chiuse (6 punti)

### B1. [Domanda] (1 punto)
- A) ...
- B) ...
- C) ...
- D) ...

### B2. ...

---

## PARTE C: Codice (8 punti)

### C1. [Tipo: Trova errore / Refactoring / Scrivi] (N punti)
[Scenario + codice]

---

## PARTE D: Design/Architettura (6 punti)

### D1. [Scenario] (6 punti)
[Requisito + domande specifiche]

---

Rispondi quando sei pronto! Puoi rispondere tutto insieme o una parte alla volta.
```

#### 3. Attendi risposte e correggi

Quando Dan risponde:
1. Correggi ogni risposta con feedback dettagliato
2. Assegna punteggio per ogni parte
3. Calcola voto finale /30
4. Assegna XP secondo tabella:
   - >=27/30 → +200 XP (con lode)
   - >=24/30 → +150 XP (con merito)
   - >=18/30 → +100 XP (superato)
   - <18/30 → +30 XP (tentativo)
5. Se retry: confronta con voto precedente

#### 4. Salva il risultato

Crea file `Exams/esame_YYYY-MM-DD.md` con:
- Frontmatter (tags, date, argomenti, voto, status: graded)
- Domande + risposte di Dan + correzioni + voto

Aggiorna `Exams/README.md` tabella "Esami Completati".

#### 5. Mostra riepilogo

```
RISULTATO ESAME

Voto: [X]/30 — [Superato con lode / merito / Superato / Non superato]
XP: +[N]

| Parte | Punti | Max |
|-------|-------|-----|
| A - Aperte | X | 10 |
| B - Chiuse | X | 6 |
| C - Codice | X | 8 |
| D - Design | X | 6 |

Punti di forza: [...]
Aree da migliorare: [...]
[Se retry: "Rispetto all'ultimo tentativo (X/30 del YYYY-MM-DD): +N punti miglioramento!"]

Argomenti da ripassare: [lista con path note]
```

## Regole

- Lingua: italiano per testo, inglese per codice
- Le domande devono testare COMPRENSIONE, non memorizzazione
- Parte C: codice REALE C#/.NET, non teorico
- Se Dan chiede "pausa" o vuole continuare dopo, rispetta i tempi
- NON dare suggerimenti durante l'esame
- Correzione solo DOPO che Dan dice di aver finito
- Ogni esame deve avere domande UNICHE (controlla esami precedenti)
