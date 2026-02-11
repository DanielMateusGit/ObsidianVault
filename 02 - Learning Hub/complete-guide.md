**# 📖 Guida Completa: Learning Hub + AI Coach

## 🎯 Panoramica del Sistema

Hai costruito un **sistema di apprendimento gamificato** con:

| Componente | Cosa fa |
|------------|---------|
| **Obsidian Vault** | Organizza tutto: roadmap, task, note, progress |
| **AI Coach (Python)** | Ti guida, motiva, traccia XP, fa quiz |
| **Gamification** | XP, livelli, achievement, streak per motivarti |

---

## 🗓️ Workflow Giornaliero

### 🌅 Mattina (2 min)

```bash
python3 coach.py briefing
```

Il coach ti dice:
- Come sta andando il tuo streak
- Cosa dovresti fare oggi
- Quanto tempo dedicare (weekday vs weekend)
- Motivazione personalizzata

### 🌙 Sera - Sessione di Studio

#### 1. Apri Obsidian
Vai al task della settimana corrente:
- `Architect-Quest/Projects/P1-.../Tasks/Week-01.md`
- oppure `Senior-Engineer/Projects/P1-.../Tasks/Week-01.md`

#### 2. Scegli UN task dalla lista
Ogni task ha checkbox:
```markdown
- [ ] Crea repo GitHub `notification-service`
- [ ] Solution .NET 8 con struttura Clean Architecture
```

#### 3. Lavora sul task
Mentre lavori, prendi note nella sezione `Notes/` del progetto.

#### 4. Completa e segna
```markdown
- [x] Crea repo GitHub `notification-service`  ✅
```

#### 5. Crea/aggiorna Daily Log
Crea file `Daily/2025-01-29.md` (usa il template):
```markdown
---
completed: true    # <-- IMPORTANTE per lo streak!
hours: 1
minutes: 30
xp_earned: 50
---

## ✅ Completato
- [x] Creato repo notification-service
- [x] Setup struttura Clean Architecture

## 📖 Imparato
> La direzione delle dipendenze in Clean Architecture...
```

#### 6. Aggiungi XP

```bash
python3 coach.py add-xp 50 "Setup repo notification-service"
```

#### 7. Verifica streak

```bash
python3 coach.py streak
```

---

## 🤖 Comandi del Coach

### Comandi Quotidiani

| Comando | Quando usarlo |
|---------|---------------|
| `python3 coach.py briefing` | Mattina, per sapere cosa fare |
| `python3 coach.py status` | Vedere XP, level, streak |
| `python3 coach.py suggest` | Non sai cosa studiare? |
| `python3 coach.py streak` | Verificare se streak è ok |

### Gestione XP

```bash
# Aggiungi XP dopo aver completato qualcosa
python3 coach.py add-xp 50 "Completato task X"
python3 coach.py add-xp 75 "Scritto ADR-001"
python3 coach.py add-xp 30 "Letto capitolo 3 Clean Architecture"
```

### Quiz (Spaced Repetition)

```bash
python3 coach.py quiz
```

Ti fa una domanda su un concetto che hai studiato. Ottimo per consolidare!

---

## ⭐ Sistema XP

### Come Guadagni XP

| Attività | XP | Note |
|----------|-----|------|
| Daily log completato | +10 | Automatico se `completed: true` |
| 30 min studio | +20 | |
| 1+ ora studio | +40 | |
| Task completato | +50 | Varia per task |
| Deliverable | +100 | Fine settimana |
| Capitolo libro | +30 | +10 extra con note |
| ADR scritto | +75 | |
| Diagramma C4 | +60 | |
| Week completata | +150 | Tutti i task della settimana |
| Progetto completato | +500 | Boss battle! |

### Streak Bonus

| Streak | Bonus |
|--------|-------|
| 7 giorni | +100 XP |
| 14 giorni | +200 XP |
| 30 giorni | +500 XP |

### Livelli

| Level | XP | Titolo |
|-------|-----|--------|
| 1 | 0 | Apprentice Developer |
| 2 | 500 | Code Crafter |
| 3 | 1,200 | Pattern Seeker |
| 4 | 2,000 | Module Builder |
| 5 | 3,000 | Service Architect |
| ... | ... | ... |
| 12 | 20,000 | AI-Native Architect 👑 |

---

## 🔥 Mantenere lo Streak

Lo streak è il motore della consistenza. Per mantenerlo serve **UNO** di questi ogni giorno:

- ✅ 30+ minuti di studio
- ✅ 1 commit con progressi reali
- ✅ 1 task completato

**Nel Daily Log**, metti `completed: true` nel frontmatter:

```yaml
---
completed: true   # <-- Questo mantiene lo streak!
---
```

**Se salti un giorno?** Lo streak riparte da 0, ma gli XP restano. Non demotivarti, ricomincia!

---

## 📅 Workflow Settimanale

### Durante la Settimana
- Lavora sui task della Week corrente
- Crea Daily Log ogni giorno che studi
- Aggiungi XP man mano

### Domenica Sera (15 min)

1. **Crea Weekly Review** (`Weekly/2025-W05.md`)
2. **Calcola XP totali della settimana**
3. **Retrospettiva:** cosa è andato bene? Cosa migliorare?
4. **Pianifica:** quali task per la prossima settimana?

```bash
python3 coach.py status  # Vedi il riepilogo
```

---

## 🏆 Achievement

Gli achievement si sbloccano automaticamente facendo cose. Vai in `achievements.md` e quando ne completi uno:

1. Cambia 🔒 → 🔓
2. Aggiungi la data
3. Aggiungi XP: `python3 coach.py add-xp 50 "Achievement: First Commit"`

### Achievement Facili per Iniziare
- 🌱 **First Commit** — Fai il primo commit
- 📝 **Daily Writer** — Primo daily log
- 🔥 **Spark** — 3 giorni di streak

---

## 📁 Navigare il Vault

### Struttura Mentale

```
Learning Hub
├── Dashboard      → Vista generale
├── Progress       → XP e livelli
├── achievements   → Badge
│
├── Architect-Quest/           → Percorso Architettura
│   └── Projects/P1-.../
│       └── Tasks/Week-01      → Cosa fare questa settimana
│
├── Senior-Engineer/           → Percorso Coding
│   └── Projects/P1-.../
│       └── Tasks/Week-01      → Cosa fare questa settimana
│
├── Daily/         → Log giornalieri
├── Weekly/        → Review settimanali
└── Books/         → Note sui libri
```

### Link Utili in Obsidian

Dalla Dashboard puoi raggiungere tutto. Usa `[[link]]` per navigare.

---

## 🎯 I Due Percorsi

### 🏛️ Architect Quest
**Focus:** Progettare sistemi, documentazione, cloud
**Per chi:** Chi vuole diventare architect / dirigere AI per implementare
**Progetti:** Notification Service → NutriPlan → BookingHub → FamilyBudget

### 💻 Senior Engineer
**Focus:** Coding hands-on, TDD, patterns, Redis
**Per chi:** Chi vuole diventare senior developer
**Progetti:** Task Manager → Chat → E-commerce → ... → Capstone

### Quale seguire?

**Opzione A:** Uno alla volta (focus totale)
- Pro: Meno context switching
- Contro: 18 mesi su un percorso solo

**Opzione B:** Alternati (es. una settimana ciascuno)
- Pro: Varietà, le competenze si rinforzano
- Contro: Più lento su ciascuno

**Opzione C:** Paralleli (un po' di entrambi ogni settimana)
- Pro: Progressi su entrambi
- Contro: Richiede più tempo settimanale

**Consiglio:** Inizia con UNO per le prime 2-4 settimane, poi decidi.

---

## 🚀 Inizia Ora!

### Primo Giorno

1. **Decidi quale percorso iniziare:**
   - `Architect-Quest/Projects/P1-Notification-Service/Tasks/Week-01.md`
   - oppure `Senior-Engineer/Projects/P1-Task-Manager/Tasks/Week-01.md`

2. **Leggi la Week-01** e scegli il primo task

3. **Fallo!** (anche solo 30 min)

4. **Crea il Daily Log** con `completed: true`

5. **Aggiungi XP:**
   ```bash
   python3 coach.py add-xp 50 "Primo task completato"
   python3 coach.py add-xp 30 "Achievement: First Commit"
   ```

6. **Celebra!** 🎉

---

## ❓ FAQ

**Q: Devo fare entrambi i percorsi?**
A: No, scegli quello che ti serve di più. Oppure fai entrambi se hai tempo.

**Q: Quanto tempo serve al giorno?**
A: Minimo 30 min per mantenere streak. Ideale: 1-2h weekday, 3-4h weekend.

**Q: Se salto un giorno?**
A: Streak riparte da 0, ma XP restano. Non è la fine del mondo!

**Q: Il coach non risponde?**
A: Verifica che Ollama sia attivo: `ollama serve`

**Q: Posso modificare i task/XP?**
A: Certo! È il TUO sistema. Adattalo come vuoi.

---

## 🔧 Troubleshooting

```bash
# Coach non risponde
ollama serve  # In un altro terminale

# Verifica setup
python3 coach.py check

# Ollama lento la prima volta
# È normale! Sta caricando il modello in RAM (~30 sec)
```

---

*Buon apprendimento! 🚀*
