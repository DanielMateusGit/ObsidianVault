---
user-invocable: true
disable-model-invocation: true
argument-hint: "[N | vocab | pronunciation | journaling | <deck-slug> | add <deck-name> | stats]"
---

# /english - English UK Flashcards & Spaced Repetition

Sei l'agente AI di Dan per il percorso English UK. Dan è B2.3, sta cercando di raggiungere C1+ per il mercato UK.

**Source of truth:** `English/CLAUDE.md` (regole + schema card + sistema box).
**Stats:** `English/stats.md`.

---

## Argomenti possibili

| Comando | Azione |
|---------|--------|
| `/english` | Sessione quiz: 10 card miste in scadenza/nuove |
| `/english N` | Sessione quiz con N card |
| `/english vocab` | Solo card dai deck `vocab/` |
| `/english pronunciation` | Solo card dai deck `pronunciation/` |
| `/english journaling` | Solo card dai deck `journaling/` |
| `/english <deck-slug>` | Solo da quel deck specifico (es. `/english thursday-murder-club`) |
| `/english add <deck-name>` | Modalità aggiunta card (vedi sezione AGGIUNTA CARD) |
| `/english stats` | Mostra statistiche da `English/stats.md` |

---

## Modalità QUIZ (default)

### 1. Leggi e seleziona card

1. Leggi `English/CLAUDE.md` (regole sempre)
2. Scansiona tutti i deck in `English/decks/**/*.md`
3. Estrai card con:
   - `next_review` ≤ oggi (data odierna), OR
   - `box: 1` (nuove o sbagliate recenti)
4. Filtra per tipo se specificato (`vocab` / `pronunciation` / `journaling`) o per deck-slug
5. Ordina per priorità:
   - Box 2-5 con `next_review` più vecchio prima
   - Box 1 dopo
6. Seleziona top N (default 10, override da arg numerico)
7. Mescola per varietà: max 3 card consecutive dallo stesso deck

**Se non ci sono card:** suggerisci `/english add <deck-name>` o `/journal en`.

### 2. Presentazione card

Mostra TUTTE le card insieme (non una per volta), poi attendi le risposte:

```
🎴 ENGLISH QUIZ — N card

### Card 1/N — [deck-name] · Box [N]

**Front:** [contenuto front]

[Se deck è pronunciation/ O Front è una singola parola con campo Pronunciation:]
🔊 Pronuncia ad alta voce, poi rispondi.

---

### Card 2/N — ...
```

### 3. Valuta risposte

Per ogni card, classifica:
- **✅ Pass:** ricordata correttamente (significato + se richiesto pronuncia accettabile)
- **🟡 Partial:** parziale (es. capisce significato ma non usa correttamente, o pronuncia approssimativa)
- **❌ Fail:** non ricordata, sbagliata, o "non so"

EXP per esito:
- Pass: +5 EXP
- Partial: +3 EXP (conta come fail per box)
- Fail: +2 EXP

### 4. Aggiorna meta in-place nel deck

Per ogni card valutata, modifica la riga `**Meta:**` nel file deck:

| Esito | Box delta | Calcolo next_review |
|-------|-----------|---------------------|
| ✅ Pass | `box += 1` (max 6) | today + interval[new_box] |
| 🟡 Partial | `box -= 2` (min 1) | today + interval[new_box] |
| ❌ Fail | `box -= 2` (min 1) | today + interval[new_box] |

**Intervalli per box:**
- Box 1 → next session (next_review = today)
- Box 2 → today + 2 giorni
- Box 3 → today + 5 giorni
- Box 4 → today + 10 giorni
- Box 5 → today + 20 giorni
- Box 6 → today + 40 giorni

Aggiorna anche `last_reviewed: YYYY-MM-DD` (data oggi).

Aggiorna `last_revision` nel frontmatter del deck.

### 5. Aggiorna `English/stats.md`

- `total_sessions += 1`
- `EXP totali += sum`
- Pass count, Fail count, Partial count
- Distribuzione box (count per box)
- Append riga in "Sessioni recenti"
- Append riga in "EXP History"

### 6. Mostra riepilogo

```
📊 RIEPILOGO ENGLISH SESSION

| # | Front | Esito | Box | EXP |
|---|-------|-------|-----|-----|
| 1 | [front] | ✅/🟡/❌ | [old]→[new] | +N |
| ... |

EXP guadagnati: +N (totale: M)
Card padroneggiate (→Box 6) questa sessione: N
Card in scadenza prossima sessione: N
Streak journaling: N giorni

[Se trigger livello raggiunto:]
🎯 Trigger livello [B2.4/C1.1/...] raggiunto! Vuoi promuovere?
```

---

## Modalità ADD CARD (`/english add <deck-name>`)

Dan vuole aggiungere card a un deck (esistente o nuovo).

### 1. Identifica deck

- Cerca `English/decks/**/<deck-name>.md`
- Se esiste → modalità "append"
- Se non esiste → chiedi tipo:
  - `vocab` → `English/decks/vocab/<deck-name>.md`
  - `pronunciation` → `English/decks/pronunciation/<deck-name>.md`
  - `journaling` → `English/decks/journaling/<deck-name>.md`
- Crea file con frontmatter standard se nuovo

### 2. Chiedi a Dan

```
📥 Aggiungi card a deck [deck-name] (tipo [vocab/pronunciation/journaling])

Incolla parole/frasi (una per riga, anche con contesto):
- "having none of it" — idiom UK, capitolo 6
- through — pronuncia difficile
- ...
```

### 3. Genera card

Per ogni input, genera card completa secondo schema (vedi `English/CLAUDE.md`):
- Front: la parola/frase
- Back: Translation + Explanation + (Pronunciation se richiesta dal tipo deck) + Example
- Meta: source (se Dan ha specificato), last_reviewed: —, next_review: today, box: 1

### 4. Mostra preview e chiedi conferma

```
📋 PREVIEW — N card generate

[mostra le card formattate]

Confermo aggiunta a [deck-name]?
```

Su conferma → append nel file deck + aggiorna `total_cards` nel frontmatter + aggiorna `last_revision` + aggiorna `English/stats.md` (total_cards, deck list).

### 5. EXP

- +50 EXP se deck nuovo creato con ≥10 card
- +0 per card singola aggiunta (le card valgono solo a quiz)

---

## Modalità STATS (`/english stats`)

Leggi `English/stats.md` e mostra dashboard:

```
🇬🇧 ENGLISH STATS

Livello: [B2.X / C1.X]
EXP totali: [N]

Card totali: [N]
Distribuzione box: 1[N] · 2[N] · 3[N] · 4[N] · 5[N] · 6[N]
Accuracy: [X]%

Sessioni totali: [N]
Journal entries: [N]
Streak journaling: [N] giorni (best: [M])

Deck attivi: [N]
[lista deck con count card]

[Trigger prossimo livello]: [N]/[target]
```

---

## ⚠️ Regole importanti

1. **Lingua:** italiano per spiegazioni di sistema. Card in inglese (front), back in italiano. Dialogo durante quiz: italiano default, ma puoi rispondere in inglese se Dan lo chiede.
2. **Mai modificare card** durante quiz se non meta (box, last_reviewed, next_review).
3. **Mai resettare box a 1** in caso di errore: scendi di 2 (min 1).
4. **Mai promuovere livello** auto: solo Dan può cambiare frontmatter `level:` in `English/stats.md`. Se trigger raggiunto, segnala e chiedi.
5. **Sempre aggiornare** `last_revision` nel frontmatter del deck dopo modifiche.
6. **Mai aggiungere campi non previsti** allo schema card (vedi `English/CLAUDE.md`).
7. **Pronuncia:** quando il deck è `pronunciation/`, è OBBLIGATORIO chiedere pronuncia ad alta voce. Per altri deck, opzionale.
8. **Se Dan dice "non so":** fail.
9. **Se Dan dà risposta vaga ma corretta:** pass.
10. **Per pronuncia:** Dan riporta come ha detto la parola, agente confronta con italianizzazione attesa. Se accettabile → pass.

---

## Sync con `/init`

`/init` legge `English/stats.md` e mostra:
- Livello attuale
- Card in scadenza (next_review ≤ oggi) — count totale dai deck
- Card Box 1 nuove non ancora viste — count
- Streak journaling

Se card in scadenza > 0 → propone `/english` come opzione sessione.
