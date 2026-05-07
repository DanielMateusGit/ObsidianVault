---
tags: [english, language-learning, flashcards, spaced-repetition]
created: 2026-05-05
level: B2.3
target: C1+
---

# 🇬🇧 English Track — Comprehension & Production (UK)

> Percorso parallelo per migliorare comprensione/produzione inglese UK.
> Parte della formazione professionale di Dan (mercato UK, candidature internazionali).
> **Livello attuale:** B2.3 → target C1+

---

## 🎯 Obiettivo

Comprendere/parlare inglese UK fluentemente per:
- Letteratura (libri UK, podcast, lezioni)
- Lavoro (interview, daily standup, pair programming, code review)
- Vita quotidiana a Londra

**Non è un corso strutturato** — è un sistema di **memorizzazione attiva** di parole, frasi, espressioni, pronuncia che Dan incontra leggendo/ascoltando/parlando.

---

## 🗂️ Struttura cartelle

```
English/
├── CLAUDE.md                      ← SEI QUI (regole agente quiz + schema)
├── stats.md                       ← XP, streak, livello, accuracy
├── decks/
│   ├── vocab/                     ← parole/espressioni dai libri/podcast
│   │   └── <book-or-source>.md   ← es. thursday-murder-club.md
│   ├── pronunciation/             ← parole con guida pronuncia
│   │   └── <topic>.md            ← es. tricky-uk-sounds.md
│   └── journaling/                ← card generate da journal entries
│       └── <topic>.md            ← es. phrasal-verbs.md
└── journal/
    └── YYYY-MM-DD.md              ← entry diario in English
```

**Regola:** ogni file deck ha frontmatter completo + sezioni card uniformi (vedi schema sotto).

---

## 🃏 Schema card (formato unico per tutti i deck)

```markdown
## Card N

**Front:** [parola/frase/espressione]

**Back:**
- **🇮🇹 Translation:** [traduzione italiana]
- **📖 Explanation:** [spiegazione uso, sfumature, registro, falsi amici]
- **🔊 Pronunciation:** /[IPA]/ → **[ITALIANIZZAZIONE]** ([note opzionali sui suoni difficili])
- **🤡 Example:** *[frase d'esempio in inglese, possibilmente memorabile]*

**Meta:** source:[ch:6 / podcast / lesson] · last_reviewed: [date|—] · next_review: [date] · box: [1-6]
```

### Regole del Back

- **Translation** sempre in italiano
- **Explanation** in italiano (registro, falsi amici, contesto, etimologia se utile)
- **Pronunciation** OBBLIGATORIA per deck `pronunciation/`, OPZIONALE per `vocab/` e `journaling/` se la parola è facile
  - Formato: `/IPA standard/` → **ITALIANIZZAZIONE FONETICA UK**
  - Esempio: `Like` → `/laɪk/` → **LÀIC** (la L meno netta dell'italiano)
  - Esempio: `Through` → `/θruː/` → **THRU** (TH = lingua tra i denti, non "tru")
- **Example** in inglese, possibilmente divertente o memorabile

---

## 📐 Spaced Repetition System (Box 1-6, incrementale + decrementale)

Sistema custom **completion-based** (non solo data-based) ma con intervalli giorni per dare "respiro" alla memoria.

| Box | Significato | Prossima review |
|-----|-------------|-----------------|
| 📦 Box 1 | Nuova / sbagliata di recente | Prossima sessione (no attesa) |
| 📦 Box 2 | Passata 1x | +2 giorni |
| 📦 Box 3 | Passata 2x consecutive | +5 giorni |
| 📦 Box 4 | Passata 3x consecutive | +10 giorni |
| 📦 Box 5 | Passata 4x consecutive | +20 giorni |
| 📦 Box 6 | Padroneggiata (5x consecutive) | +40 giorni |

### Regole transizione

| Esito | Effetto |
|-------|---------|
| ✅ Pass | `box += 1` (max Box 6) → `next_review = today + interval[new_box]` |
| ❌ Fail | `box -= 2` (min Box 1) → `next_review = today + interval[new_box]` |

> **Esempio decremento:** card a Box 5 (intervallo +20g) → fail → Box 3 (intervallo +5g). NON resetta a Box 1: l'errore può essere distrazione, non oblio totale.

> **Esempio extra:** card a Box 2 → fail → Box 1 (next session, immediato).

### Aggiornamento meta dopo ogni card

```
last_reviewed: 2026-05-05  (data sessione)
next_review:   2026-05-07  (calcolata da box nuovo)
box:           2            (aggiornato)
```

---

## 🎮 Skill `/english`

Vedi `.claude/skills/english/SKILL.md`. Comportamenti:

| Comando | Effetto |
|---------|---------|
| `/english` | 10 card miste in scadenza (next_review ≤ oggi) o nuove |
| `/english N` | N card invece di 10 |
| `/english vocab` | solo vocabolario |
| `/english pronunciation` | solo pronuncia |
| `/english journaling` | solo card da journal |
| `/english <deck-slug>` | solo da quel deck |
| `/english add <deck-name>` | modalità aggiunta: Dan incolla parole, agente formatta card |
| `/english stats` | mostra stats da `stats.md` |

### Priorità selezione card

1. **Card in scadenza** (next_review ≤ oggi, Box 2+)
2. **Card Box 1** (nuove o appena sbagliate)
3. Mix dei 3 tipi (vocab + pronunciation + journaling) per varietà
4. Mix dei deck (max 3 card consecutive dallo stesso deck)

---

## 📔 Journal entries (via `/journal en`)

Vedi `.claude/skills/journal/SKILL.md`.

Workflow `/journal en`:
1. Agente chiede: "Cosa hai imparato oggi in inglese?"
2. Dan scrive (anche in italiano misto inglese)
3. Agente:
   - Salva entry in `English/journal/YYYY-MM-DD.md` (in inglese, corretto se serve)
   - Estrae 3-5 concetti chiave
   - Genera flashcards in `English/decks/journaling/<topic>.md` con domande **in inglese** (es. "What is a phrasal verb? Give 3 examples.")
4. Le journaling cards entrano nel pool `/english`

Ogni entry diario riceve +20 EXP. Streak journaling tracciato in `stats.md`.

---

## 🏆 XP system (separato da percorso AI Engineer)

Tracciato in `English/stats.md`.

| Attività | EXP |
|----------|-----|
| Card pass | +5 |
| Card fail (per aver provato) | +2 |
| Card → Box 6 (mastered) | +30 |
| Journal entry (`/journal en`) | +20 |
| Streak journaling 7gg | +50 |
| Streak journaling 30gg | +200 |
| Deck creato (≥10 card) | +50 |
| Sessione `/english` ≥10 card | +15 |

### Livelli English (completion-based, NO date)

| Livello | Trigger |
|---------|---------|
| **B2.3** | Stato attuale (2026-05-05) |
| **B2.4** | 100 card → Box 6 + 10 journal entries |
| **B2.5** | 250 card → Box 6 + 25 journal entries |
| **C1.1** | 500 card → Box 6 + 50 journal entries + 1 libro UK letto end-to-end |
| **C1.2** | 750 card → Box 6 + 100 journal entries + 2 libri UK + 1 podcast settimana |
| **C1.3** | 1000 card → Box 6 + 150 journal entries + 3 libri UK |
| **C2** | 1500 card → Box 6 + 200 journal entries + 5 libri UK + capacità mock interview tecnica |

> Trigger sono indicativi: il vero livello è la **capacità reale** (test ufficiali, conversazioni con native, performance interview). I numeri servono come milestone gamificate.

> ⚠️ **Auto-promotion DISABLED.** Il livello English (B2.3 → C1+) lo aggiorna **solo Dan** quando si sente effettivamente al livello successivo. L'agente NON promuove automaticamente al raggiungimento dei trigger — al massimo segnala "trigger raggiunto, vuoi promuovere a [livello]?".

---

## 🤖 Istruzioni agente quiz (`/english` workflow)

### 1. Selezione card

```
1. Scansiona tutti i deck in English/decks/**/*.md
2. Estrai card con next_review ≤ oggi OR box=1
3. Ordina per: priorità (Box 2+ in scadenza > Box 1) → next_review crescente
4. Seleziona top N (default 10)
5. Mescola per varietà (no 3+ stessa deck consecutivi)
```

### 2. Presentazione

Per ogni card:

```
### Card N/totale — [deck-name]

**Front:** [contenuto front]

[Se deck=pronunciation O field pronunciation presente:]
🔊 Pronuncia ad alta voce, poi rispondi.
```

Mostra TUTTE le card, poi attendi le risposte di Dan.

### 3. Valutazione

Per ogni risposta di Dan:
- **Pass (✅):** ha ricordato significato + (se richiesto) pronunciato correttamente
- **Partial (🟡):** parziale → conta come **fail** (box -2) ma EXP intermedi (+3)
- **Fail (❌):** non ricordata o sbagliata

Se Dan dice "non so" → fail.
Se Dan dà risposta vaga ma corretta → pass.
Se per pronuncia: Dan riporta la sua pronuncia, agente confronta con italianizzazione attesa.

### 4. Aggiornamento meta

Per ogni card valutata, aggiorna in-place nel file deck:
- `box` → nuovo valore
- `last_reviewed` → data oggi (YYYY-MM-DD)
- `next_review` → calcolato da `today + interval[new_box]`

Aggiorna `last_revision` nel frontmatter del deck.

### 5. Aggiornamento stats.md

```
- Sessioni totali +1
- Card riviste += N
- Pass count += N_pass
- Fail count += N_fail
- EXP totali += sum
- Aggiorna distribuzione box (count per box)
- Aggiorna ultima sessione (data, deck toccati)
```

### 6. Riepilogo a Dan

```
RIEPILOGO ENGLISH

| Card | Front | Esito | Box | EXP |
|------|-------|-------|-----|-----|
| #1 [deck] | [front] | ✅/🟡/❌ | [old]→[new] | +N |
| ...

EXP guadagnati: +N (totale: M)
Card in scadenza prossima sessione: N
Streak journaling: N giorni
```

---

## ⚠️ Regole IMPORTANTI per agente

1. **NON modificare** mai card senza chiedere (escluso meta dopo quiz)
2. **NON ripetere** una card che Dan ha appena visto in questa sessione
3. **Se Dan ha pronunciato** male una parola, mostra la pronuncia corretta ITALIANIZZATA + IPA, non lunghe spiegazioni
4. **Se non ci sono card in scadenza:** proponi card Box 1 nuove. Se nessuna, suggerisci `/english add` o `/journal en`
5. **Lingua agente:**
   - Italiano per spiegazioni di sistema, struttura, errori
   - Inglese per le card stesse (front/example)
   - Italiano per back (translation/explanation)
   - Inglese o italiano per il dialogo durante quiz (Dan può scegliere)
6. **Mai** aggiungere campi non previsti nello schema card (es. emoji, varianti) senza consultare CLAUDE.md prima

---

## 📚 Deck attivi (aggiornare quando creati)

| Deck | Path | Card | Box 6 | Ultimo update |
|------|------|------|-------|---------------|
| Thursday Murder Club (Osman) — capitoli 6-9 | `decks/vocab/thursday-murder-club.md` | 49 | 0 | 2026-05-05 |
| Grammar Corrections — Personal anti-mistakes | `decks/journaling/grammar-corrections.md` | 10 | 0 | 2026-05-07 |

> Quando crei un nuovo deck, aggiungere riga qui con count card e last_revision.

---

*Created: 2026-05-05 (English track v1.0 — sistema flashcards UK con spaced repetition Box 1-6 incrementale/decrementale)*
