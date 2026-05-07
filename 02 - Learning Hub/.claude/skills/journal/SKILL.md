---
user-invocable: true
disable-model-invocation: true
argument-hint: "[en | personal | <custom-tag>]"
---

# /journal - Journaling parametrizzato

Sei l'agente di journaling di Dan. Comando parametrizzato per tipi di diario diversi (English, personale, tag custom).

---

## Argomenti

| Comando | Tipo | Path |
|---------|------|------|
| `/journal` | Senza arg → chiedi: "Su cosa vuoi fare journaling oggi? (en / personal / <tag-libero>)" |
| `/journal en` | English learning journal (con flashcards generate) | `English/journal/YYYY-MM-DD.md` |
| `/journal personal` | Diario personale | `journal/personal/YYYY-MM-DD.md` |
| `/journal <tag>` | Custom tag (es. `travel`, `work`, `gym`) | `journal/<tag>/YYYY-MM-DD.md` |

> Tag riservati: `en`, `personal`. Tutti gli altri sono custom liberi.

---

## Modalità EN (English) — `/journal en`

> **Speciale:** è l'unico tipo che genera flashcards in `English/decks/journaling/`.

### 1. Chiedi cosa Dan ha imparato

```
📔 ENGLISH JOURNAL — [data]

Cosa hai imparato oggi in inglese? (lezioni, conversazioni, parole nuove, errori notati, …)

Puoi scrivere in italiano misto inglese — io poi salvo l'entry corretta in inglese.
```

### 2. Dan scrive (testo libero)

Aspetta input. Può essere lungo o breve.

### 3. Crea entry

Salva in `English/journal/YYYY-MM-DD.md` (se file esiste, usa suffisso `-2.md`, `-3.md`):

```markdown
---
tags: [english, journal]
date: YYYY-MM-DD
type: en
created: YYYY-MM-DD
---

# 📔 English Journal — YYYY-MM-DD

## Cosa ho imparato oggi

[Riscritto in inglese pulito, conservando il senso, con piccole correzioni se Dan ha mischiato italiano]

## Concetti chiave estratti

- [concetto 1]
- [concetto 2]
- [concetto 3]

## Riflessioni / domande

[Se Dan ha lasciato dubbi o domande → li elenchi qui]

## Card generate

- [link a `English/decks/journaling/<topic>.md`]
```

### 4. Estrai concetti chiave + genera 3-5 flashcards

Identifica 3-5 concetti chiave dal journal entry. Per ognuno, genera una flashcard **in inglese** (domanda in inglese, back con spiegazione italiana + esempio inglese).

Esempi formato journaling card:

```markdown
## Card N

**Front:** What is a phrasal verb? Give 3 examples.

**Back:**
- **🇮🇹 Translation:** Cos'è un phrasal verb? Dai 3 esempi.
- **📖 Explanation:** Verbo + particella (preposizione/avverbio) che assume significato idiomatico. Es: *give up* (arrendersi), *look after* (prendersi cura), *put off* (rimandare). Spesso il senso non è deducibile dalle parole singole.
- **🤡 Example:** *I'm going to give up trying to look after this houseplant — I keep putting off watering it.*

**Meta:** source:journal-2026-05-05 · last_reviewed: — · next_review: 2026-05-05 · box: 1
```

Salvale in `English/decks/journaling/<topic-slug>.md`. Se il topic deck esiste già, append; altrimenti crea con frontmatter standard.

**Topic slug:** estrai da concetto principale del journal entry (es. `phrasal-verbs`, `british-idioms`, `tense-rules`, `pronunciation-tricks`). Domanda Dan se incerto.

### 5. Aggiorna stats

In `English/stats.md`:
- `journaling_streak += 1` (se journal di ieri esiste, altrimenti reset a 1)
- `journaling_longest_streak = max(streak, longest)`
- `Journal entries += 1`
- `total_cards += N` (card generate)
- EXP: +20 (entry) + bonus streak se 7/14/30/60 raggiunti

### 6. Riepilogo

```
✅ ENGLISH JOURNAL ENTRY SALVATA

File: English/journal/[date].md

Concetti estratti: N
Card generate: N → English/decks/journaling/<topic>.md

EXP guadagnati: +20 (entry) + [bonus streak]
Streak journaling: N giorni 🔥
Card totali in journaling: N

[Se streak milestone raggiunto:]
🎯 Streak [7/14/30/60] giorni! Bonus +N EXP
```

---

## Modalità PERSONAL — `/journal personal`

Diario personale. **NO flashcards generate.** Solo entry libera.

### 1. Chiedi

```
📔 DIARIO PERSONALE — [data]

Cosa vuoi scrivere oggi? (umore, riflessioni, eventi, gratitudine, dubbi, …)

Tutto privato, nessuna analisi automatica.
```

### 2. Salva entry

In `journal/personal/YYYY-MM-DD.md`:

```markdown
---
tags: [journal, personal]
date: YYYY-MM-DD
type: personal
---

# 📔 Diario — YYYY-MM-DD

[Testo Dan, as-is, nessuna correzione]
```

> Se file già esiste: usa suffisso `-2.md`, `-3.md`.

### 3. Conferma

```
✅ Entry personale salvata: journal/personal/[date].md
```

Nessun XP, nessun tracking. È spazio personale.

---

## Modalità CUSTOM TAG — `/journal <tag>`

Per tag liberi (es. `travel`, `work`, `gym`, `food`, `gratitude`).

### 1. Chiedi

```
📔 JOURNAL — TAG: [tag] — [data]

Cosa vuoi scrivere su [tag] oggi?
```

### 2. Salva entry

In `journal/<tag>/YYYY-MM-DD.md`:

```markdown
---
tags: [journal, <tag>]
date: YYYY-MM-DD
type: <tag>
---

# 📔 [Tag-Capitalized] — YYYY-MM-DD

[Testo Dan]
```

### 3. Conferma

```
✅ Entry salvata: journal/<tag>/[date].md
```

Nessun XP, nessun tracking automatico (può essere aggiunto in futuro per tag specifici).

---

## Modalità SENZA ARG — `/journal`

Se Dan lancia `/journal` senza argomento:

```
📔 Su cosa vuoi fare journaling oggi?

Opzioni:
- `en` → English learning (genera flashcards)
- `personal` → diario personale (privato, no analisi)
- `<tag-libero>` → journal su topic specifico (es. travel, work, gym)

Dimmi il tag.
```

Aspetta input → procedi con la modalità corrispondente.

---

## ⚠️ Regole

1. **Mai analizzare entry `personal`** — è spazio privato. Solo salvataggio.
2. **Solo `en` genera flashcards.** Mai per altri tag.
3. **Streak journaling** in `English/stats.md` si aggiorna SOLO per entry `en`.
4. **Cartelle:** crea `journal/<tag>/` automaticamente se non esiste (Bash `mkdir -p` o equivalente).
5. **File esistente stesso giorno:** usa suffissi `-2.md`, `-3.md` (mai sovrascrivere).
6. **Lingua entry:**
   - `en` → entry salvata in inglese (corretta da Dan se misto)
   - `personal` / custom → lingua di Dan (italiano default, libero)
7. **Privacy:** entry `personal` non vanno mai citate in altre conversazioni o usate come contesto, salvo richiesta esplicita di Dan.
