# 🎮 Gamification

## XP - Attività Quotidiane
| Attività | XP |
|----------|-----|
| Daily log | +10 |
| 30min studio | +20 |
| 1h studio | +40 |
| Commit con progressi | +15 |

## XP - Progressi Progetti
| Attività | XP |
|----------|-----|
| Task completato | +50 |
| Deliverable completato | +100 |
| Settimana completata | +150 |
| Progetto completato | +500 |
| Boss Battle superata (≥24/30) | +300 |
| Boss Battle con lode (≥28/30) | +500 |

## 🏆 BOSS BATTLE SYSTEM (NUOVO!)

> Verifica autonoma alla fine di ogni progetto

### Struttura
| Path | Focus |
|------|-------|
| **Architect Quest** | 70% Design, 30% Code |
| **Senior Engineer** | 30% Design, 70% Code |

### XP Boss Battle
| Risultato | XP |
|-----------|-----|
| ≥24/30 (Superata) | +300 |
| ≥28/30 (Con lode) | +500 |

### Achievement Boss Battle - Architect
| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 🎖️ | **Battle Won** | Boss Battle ≥24/30 | +300 |
| 👑 | **Battle Master** | Boss Battle ≥28/30 | +500 |
| 🏆 | **Architect Champion** | 4/4 Boss Battle superate | +1000 |

### Achievement Boss Battle - Senior
| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| ⚔️ | **Code Warrior** | Boss Battle ≥24/30 | +300 |
| 🗡️ | **Code Master** | Boss Battle ≥28/30 | +500 |
| 🏆 | **Senior Champion** | 6/6 Boss Battle superate | +1500 |

## XP - Studio e Documentazione
| Attività | XP |
|----------|-----|
| Capitolo libro letto | +30 |
| Articolo completato | +15 |
| Video visto | +15 |
| Nota creata | +20 |
| ADR scritto | +75 |
| Diagramma C4 | +60 |

## 🧠 Challenge del Giorno (Spaced Repetition)
| Attività | XP |
|----------|-----|
| Challenge completata | +5 |
| Risposta corretta | +10 |
| Risposta sbagliata | +2 (per aver provato!) |
| 5 challenge streak | +25 bonus |
| 10 challenge streak | +50 bonus |
| Quiz padroneggiato (Box 5) | +30 |

**Tracker:** `context/quiz-tracker.md`

---

## 🎓 ESAMI (NUOVO!)

> Sistema di verifica conoscenze stile universitario

### Quando Fare Esami
| Momento | Tipo | Punti | Obbligatorio |
|---------|------|-------|--------------|
| **Fine Week importante** | Mini-verifica | 15 | ⬜ Opzionale |
| **Fine Mese** | Esame medio | 30 | ✅ Sì |
| **Fine Progetto** | Esame completo | 30 | ✅ **OBBLIGATORIO** |
| **Pre-Certificazione** | Simulazione | 30+ | Su richiesta |

### Calendario Esami P1
```
Mese 1: Mini-verifica W2 + Esame Mese 1
Mese 2: Mini-verifica W6 + Esame Mese 2
Mese 3: Mini-verifica W10 + Esame Mese 3
Mese 4: ESAME FINALE PROGETTO
```

### XP per Voto - Esami Completi (30 punti)
| Voto | XP | Descrizione |
|------|-----|-------------|
| ≥27/30 | +200 | Superato con lode |
| ≥24/30 | +150 | Superato con merito |
| ≥18/30 | +100 | Superato |
| <18/30 | +30 | Tentativo + ripasso |

### XP per Voto - Mini-verifiche (15 punti)
| Voto | XP | Descrizione |
|------|-----|-------------|
| ≥13/15 | +75 | Eccellente |
| ≥11/15 | +50 | Buono |
| ≥9/15 | +30 | Sufficiente |
| <9/15 | +15 | Ripasso consigliato |

### Struttura per Tipo di Esame

**Mini-verifica (15 punti)** - ~15 min
| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 6 | 3 domande aperte |
| B | 4 | 4 multiple choice |
| C | 5 | 1-2 esercizi codice |

**Esame Mensile/Progetto (30 punti)** - ~30-45 min
| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 10 | 4-5 domande aperte |
| B | 6 | 6 multiple choice |
| C | 8 | 3+ esercizi codice |
| D | 6 | Design/Architettura |

### Achievement Esami
| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 📝 | First Exam | Primo esame completato | +50 |
| 🎯 | Dean's List | 3 esami ≥27/30 | +150 |
| 📚 | Exam Veteran | 10 esami completati | +200 |
| 🏅 | Certification Ready | Esame certificazione ≥24/30 | +300 |

**Cartella esami:** `Exams/esame_YYYY-MM-DD.md`

---

## 📚 LETTURE (NUOVO!)

> Claude aggiorna `context/reading-list.md` ogni volta che consiglia una lettura

### XP Letture
| Tipo | XP |
|------|-----|
| Articolo breve | +15 |
| Articolo lungo / Capitolo | +30 |
| Video | +15 |

**Tracker:** `context/reading-list.md`

---

## Livelli
| Lv | XP | Titolo |
|----|-----|--------|
| 1 | 0 | Apprentice Developer |
| 2 | 500 | Code Crafter |
| 3 | 1,200 | Pattern Seeker |
| 4 | 2,000 | Module Builder |
| 5 | 3,000 | Service Architect |
| 6 | 4,200 | Domain Master |
| 7 | 5,600 | System Designer |
| 8 | 7,200 | Cloud Engineer |
| 9 | 9,000 | Principal Developer |
| 10 | 11,000 | Staff Engineer |
| 11 | 15,000 | Senior Architect |
| 12 | 20,000 | AI-Native Architect |

## Streak
- **Mantenimento:** 30+ min/giorno
- **Bonus:** 7d = +100, 14d = +200, 30d = +500, 60d = +1000

## Coach CLI
```bash
python3 coach.py briefing|status|suggest|quiz|add-xp|streak|motivation
```

---

*Aggiornato: 2026-02-12*
