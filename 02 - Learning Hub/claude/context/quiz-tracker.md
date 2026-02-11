---
tags: [context, quiz, spaced-repetition]
created: 2026-02-05
updated: 2026-02-05
---

# 🧠 Quiz Tracker - Spaced Repetition

> Claude usa questo file per tracciare tutti i quiz e gestire la spaced repetition.

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| **Quiz totali** | 22 |
| **Risposte corrette** | 10 |
| **Risposte sbagliate** | 0 |
| **Non risposti** | 12 |
| **Challenge completate** | 5 |
| **Streak challenge** | 5 |

---

## 🎯 Sistema Spaced Repetition

### Intervalli (Leitner System semplificato)
| Box | Intervallo | Significato |
|-----|------------|-------------|
| 📦 Box 1 | Ogni sessione | Nuovo o sbagliato di recente |
| 📦 Box 2 | 3 giorni | Risposto correttamente 1 volta |
| 📦 Box 3 | 7 giorni | Risposto correttamente 2 volte |
| 📦 Box 4 | 14 giorni | Risposto correttamente 3 volte |
| 📦 Box 5 | 30 giorni | Padroneggiato |

### Regole
- ✅ Risposta corretta → passa al box successivo
- ❌ Risposta sbagliata → torna a Box 1
- Quiz in Box 5 da 60+ giorni → `status/mastered`

---

## 🎮 Gamification Challenge

| Attività | XP |
|----------|-----|
| Challenge del giorno completata | +5 |
| Risposta corretta | +10 |
| Risposta sbagliata | +2 (per aver provato!) |
| 5 challenge streak | +25 bonus |
| 10 challenge streak | +50 bonus |
| Quiz → Box 5 (padroneggiato) | +30 |

---

## 📚 Quiz per Argomento

### Architecture

#### Programming Paradigms
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| PARA-01 | Secondo Dijkstra, la programmazione è più simile a... | 📦1 | - | Ora | ⬜ Non risposto |
| PARA-02 | Un collega dice "OOP ha inventato l'encapsulation". Come rispondi? | 📦1 | - | Ora | ⬜ Non risposto |
| PARA-03 | Cosa hanno dimostrato Böhm e Jacopini nel 1966? | 📦1 | - | Ora | ⬜ Non risposto |

---

### SOLID

#### Open/Closed Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| OCP-01 | PaymentService usa StripeClient, CEO vuole PayPal - cosa c'è di sbagliato? | 📦3 | 2026-02-10 | 2026-02-17 | ✅ Corretto |
| OCP-02 | OrderProcessor protetto da DatabaseRepository - chi dipende da chi? | 📦3 | 2026-02-11 | 2026-02-18 | ✅ Corretto |
| OCP-03 | Perché Plugin Architecture è conseguenza di OCP? | 📦3 | 2026-02-11 | 2026-02-18 | ✅ Corretto |

#### Single Responsibility Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| SRP-01 | Qual è la VERA definizione di SRP? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-02 | ReportGenerator con metodi per Sales, HR, Finance - viola SRP? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-03 | Un collega dice che EmployeeFacade viola SRP. Come rispondi? | 📦1 | - | Ora | ⬜ Non risposto |
| SRP-04 | CalculateDiscount() per Sales e Finance - duplicazione vera o accidentale? | 📦1 | - | Ora | ⬜ Non risposto |

#### Dependency Inversion Principle
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| DIP-01 | OrderService usa direttamente SqlServerRepository. Cosa c'è di sbagliato? | 📦1 | - | Ora | ⬜ Non risposto |
| DIP-02 | Differenza tra Dependency Inversion e Dependency Injection? | 📦1 | - | Ora | ⬜ Non risposto |
| DIP-03 | Dove deve stare l'interfaccia IOrderRepository? | 📦3 | 2026-02-09 | 2026-02-16 | ✅ Corretto |

---

### Patterns

#### Facade Pattern
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| FAC-01 | Stripe payment: Facade o Factory? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |
| FAC-02 | PaymentFacade God Object - cosa faresti? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |
| FAC-03 | Sistema legacy 15 classi PDF - quale pattern? | 📦2 | 2026-02-06 | 2026-02-09 | ✅ Corretto |

---

### Domain Events
| ID | Domanda | Box | Ultima risposta | Prossima review | Status |
|----|---------|-----|-----------------|-----------------|--------|
| EVT-01 | Perché dispatchiamo eventi DOPO SaveChanges? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-02 | L'Entity può avere dipendenze come IStatsService? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-03 | Quanti handler possono ascoltare lo stesso evento? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-04 | L'entity può dispatchare direttamente l'evento? Perché? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-05 | Cos'è MediatR in relazione ai Domain Events? | 📦1 | - | Ora | ⬜ Non risposto |
| EVT-06 | Validazione email: evento o eccezione? Perché? | 📦1 | - | Ora | ⬜ Non risposto |

---

### Design
_Nessun quiz ancora_

---

### Documentation
_Nessun quiz ancora (quiz ADR sono nelle Notes del progetto, non in Knowledge)_

---

## 📅 Storico Challenge

> Aggiornato automaticamente da Claude dopo ogni challenge

| Data | Quiz ID | Risultato | XP | Note |
|------|---------|-----------|-----|------|
| 2026-02-06 | DIP-03 | ✅ | +15 | Prima challenge! |
| 2026-02-09 | DIP-03 | ✅ | +15 | Streak 2! Box 2→3 |
| 2026-02-10 | OCP-01 | ✅ | +15 | Streak 3! Box 2→3 |
| 2026-02-11 | OCP-02 | ✅ | +15 | Streak 4! Box 2→3 |
| 2026-02-11 | OCP-03 | ✅ | +40 | Streak 5! Box 2→3, +25 bonus! |

---

## 🔮 Coda Review (Quiz da ripassare oggi)

> Claude aggiorna questa lista all'inizio di ogni sessione

**Prossimi quiz da ripassare:**
1. Tutti i 6 quiz sono nuovi (Box 1) - pronti per la prima risposta!

---

## 📝 Note per Claude

### All'inizio di ogni sessione:
1. Leggi questo file
2. Controlla "Coda Review" per quiz in scadenza
3. Proponi "Challenge del giorno!" con UN quiz:
   - Priorità 1: Quiz in scadenza (spaced repetition)
   - Priorità 2: Quiz non ancora risposti
4. Dopo la risposta di Dan:
   - Aggiorna Box, data, status
   - Assegna XP
   - Se corretto: "Esatto! Infatti: {riassunto dalla nota}"
   - Se sbagliato: "Non preoccuparti! Ripasso veloce: {riassunto dalla nota}"

### Quando creo nuovi quiz:
1. Aggiungi alla tabella dell'argomento corretto
2. Assegna ID univoco (TOPIC-XX)
3. Inizia in Box 1
4. Aggiorna contatore "Quiz totali"

### Formato ID Quiz:
- `PARA-XX` = Programming Paradigms
- `DIP-XX` = Dependency Inversion Principle
- `SRP-XX` = Single Responsibility Principle
- `OCP-XX` = Open/Closed Principle
- `LSP-XX` = Liskov Substitution Principle
- `ISP-XX` = Interface Segregation Principle
- `CLEAN-XX` = Clean Architecture
- `C4-XX` = C4 Model
- `ADR-XX` = Architecture Decision Records
- `DEEP-XX` = Deep Modules
- ... (aggiungi altri man mano)

---

*Ultimo aggiornamento: 2026-02-11*
