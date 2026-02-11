---
tags: [architect-quest, p1, week-01, sedimentazione]
status: in-progress
started: 2026-02-03
xp_available: 300
xp_earned: 0
---

# 🧠 Sedimentazione - Week 01

> **Obiettivo:** Consolidare i concetti appresi durante la Week 1 prima di procedere alla Week 2.
> **Durata:** Finché non ti senti soddisfatto dell'approfondimento.

---

## 📊 Progress

| Metrica | Valore |
|---------|--------|
| Risorse obbligatorie | 0/4 (Clean Architecture in corso: cap 6/14) |
| Video visti | 0/3 |
| Note create | 5 |
| Quiz superati | 0 |

---

## 🗺️ Argomenti Esplorati (Week 1)

Ecco cosa abbiamo fatto insieme durante la Week 1:

### Clean Architecture
- [x] I 4 layer (Domain, Application, Infrastructure, API)
- [x] Dependency Rule (le dipendenze puntano verso l'interno)
- [x] Perché le violazioni sono pericolose
- [x] Quiz superato (4/4)

### SOLID Principles (Overview)
- [x] **S**ingle Responsibility - Un solo attore/stakeholder
- [x] **O**pen/Closed - Aperto per estensione, chiuso per modifica
- [x] **L**iskov Substitution - Sottotipi sostituibili
- [x] **I**nterface Segregation - Interfacce piccole e specifiche
- [x] **D**ependency Inversion - Dipendi da astrazioni
- [x] Quiz superato (4/4)

### Design Principles (A Philosophy of Software Design)
- [x] Natura della complessità (Change Amplification, Cognitive Load, Unknown Unknowns)
- [x] Strategic vs Tactical Programming
- [x] Deep Modules (interfaccia piccola, implementazione grande)
- [x] Information Hiding
- [x] Quiz superato (4/4)

### C4 Model
- [x] I 4 livelli di zoom (Context, Container, Component, Code)
- [x] Quando usare ogni livello
- [x] PlantUML per diagrammi as code
- [x] Context Diagram creato per Notification Service

### ADR (Architecture Decision Records)
- [x] Cos'è e quando usarlo
- [x] Struttura di un ADR
- [x] ADR-001 creato (Clean Architecture)

### Documentazione
- [x] Struttura README professionale
- [x] .env.example per configurazione

---

## 📚 Risorse Obbligatorie

> Completa queste risorse PRIMA di passare alla Week 2.
> Quando completi una risorsa, raccontami cosa hai imparato e creeremo una nota!

### Libri

| # | Risorsa | Capitoli | XP | Status |
|---|---------|----------|-----|--------|
| 1 | **Clean Architecture** (Robert C. Martin) | Cap. 1-14 | +30 | 🟡 In corso (cap. 1-6 letti) |
| 2 | **A Philosophy of Software Design** (John Ousterhout) | Cap. 1-5 | +30 | ⬜ |

### Articoli

| # | Risorsa | Link | XP | Status |
|---|---------|------|-----|--------|
| 3 | **The Clean Architecture** (Uncle Bob blog) | [blog.cleancoder.com](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) | +30 | ⬜ |
| 4 | **C4 Model - Core Diagrams** | [c4model.com](https://c4model.com/#coreDiagrams) | +30 | ⬜ |

**XP Risorse Obbligatorie:** 120 XP

---

## 🎬 Video Consigliati

> Questi video aiutano a consolidare i concetti. Non obbligatori ma molto utili.

| # | Video | Durata | Link | XP | Status |
|---|-------|--------|------|-----|--------|
| 1 | **Clean Architecture - Uncle Bob** | ~1h | [YouTube](https://www.youtube.com/watch?v=o_TH-Y78tt4) | +15 | ⬜ |
| 2 | **SOLID Principles** (Tim Corey) | ~1h | [YouTube](https://www.youtube.com/watch?v=5hAZ4XHdMTQ) | +15 | ⬜ |
| 3 | **C4 Model - Simon Brown** | ~45m | [YouTube](https://www.youtube.com/watch?v=x2-rSnhpw0g) | +15 | ⬜ |

**XP Video:** 45 XP

---

## 🔭 Da Esplorare Oltre (Opzionale)

> Questi sono approfondimenti extra per chi vuole andare più in profondità.
> Guadagni +25 XP per ogni approfondimento completato.

### Clean Architecture - Oltre le basi
- [ ] Screaming Architecture - L'architettura dovrebbe "urlare" lo scopo
- [ ] Humble Object Pattern - Come testare cose difficili
- [ ] Boundaries - Dove tracciare i confini tra layer

### SOLID - Casi reali
- [ ] Come SRP si applica in un progetto .NET
- [ ] OCP con Strategy Pattern
- [ ] DIP in Dependency Injection container

### Design Principles - Deep Dive
- [ ] "Working Code Isn't Enough" - Tactical vs Strategic
- [ ] Quando "Deep Module" è troppo deep
- [ ] Red Flags nel design (shotgun surgery, pass-through methods)

### C4 in pratica
- [ ] Container Diagram per Notification Service
- [ ] Structurizr DSL vs PlantUML
- [ ] Automazione diagrammi in CI/CD

### 🤖 AI-Native Engineering (Futuro - P3+)
> Risorse per prepararti all'integrazione AI in BookingHub e oltre.

| # | Risorsa | Autore | Note | XP | Status |
|---|---------|--------|------|-----|--------|
| 1 | **AI Engineering** | Chip Huyen (O'Reilly, 2025) | Framework architetturale per LLM, deployment, monitoring. [GitHub](https://github.com/chiphuyen/aie-book) | +30 | ⬜ |
| 2 | **LLM Design Patterns** | Ken Huang | Pattern architetturali per sistemi AI | +30 | ⬜ |
| 3 | **Building LLMs for Production** | Bouchard & Peters | Cost optimization, latency, observability | +25 | ⬜ |

**XP Approfondimenti Extra:** +25 XP ciascuno

---

## 📝 Note da Creare

> Quando mi racconti cosa hai imparato, creerò queste note in `Knowledge/`

### Note previste (verranno create durante la Sedimentazione)

| Topic | Categoria | Status |
|-------|-----------|--------|
| Programming Paradigms | `architecture/` | ✅ Creata |
| Clean Architecture | `architecture/` | ⬜ Da creare |
| Dependency Rule | `architecture/` | ⬜ Da creare |
| Single Responsibility Principle | `solid/` | ✅ Creata |
| Open/Closed Principle | `solid/` | ✅ Creata |
| Liskov Substitution Principle | `solid/` | ⬜ Da creare |
| Interface Segregation Principle | `solid/` | ⬜ Da creare |
| Dependency Inversion Principle | `solid/` | ✅ Creata |
| Deep Modules | `design/` | ⬜ Da creare |
| Information Hiding | `design/` | ⬜ Da creare |
| C4 Model | `documentation/` | ⬜ Da creare |
| ADR | `documentation/` | ⬜ Da creare |

**XP Note:** +20 XP ciascuna = 220 XP potenziali

---

## ✅ Checklist Completamento

Prima di passare alla Week 2, verifica:

### Obbligatorio
- [ ] Letto almeno i capitoli indicati dei 2 libri (o equivalente)
- [ ] Letto i 2 articoli
- [ ] Creata almeno 1 nota in Knowledge/
- [ ] Superato almeno 1 quiz di una nota

### Consigliato
- [ ] Visto almeno 1 video
- [ ] Create almeno 5 note in Knowledge/
- [ ] Raccontato a Claude cosa ho imparato per ogni argomento principale

### Per dire "Sono soddisfatto"
- [ ] Mi sento sicuro sui concetti di Clean Architecture
- [ ] Posso spiegare SOLID a qualcuno
- [ ] Capisco quando usare C4 e a quale livello
- [ ] So cosa sono i Deep Modules e perché sono importanti

---

## 🎮 XP Disponibili

| Categoria | XP |
|-----------|-----|
| Risorse obbligatorie (4) | 120 |
| Video (3) | 45 |
| Note (11 potenziali) | 220 |
| Approfondimenti extra | variabile |
| Completamento Sedimentazione | 100 |
| **Achievement possibili** | |
| 🧠 Knowledge Seeker | +50 |
| 🎓 Sedimentazione Master | +100 |

**XP Totali potenziali:** ~635 XP

---

## 📖 Come Procedere

1. **Scegli una risorsa** dalla lista (libro, articolo, video)
2. **Leggila/guardala** con calma
3. **Torna da me** e dimmi: "Ho letto/visto X, ti racconto cosa ho capito..."
4. **Io creo la nota** con quello che mi dici + quiz
5. **Guadagni XP** per risorsa + nota
6. **Ripeti** finché non sei soddisfatto
7. **Dimmi "Sono pronto per Week 2"** quando vuoi procedere

---

## 💬 Frasi per iniziare sessione Sedimentazione

- "Ho letto il capitolo X di Clean Architecture, ti racconto..."
- "Ho visto il video su SOLID, ecco cosa ho capito..."
- "Sono sul treno, ti spiego cosa ho imparato su [topic]..."
- "Ho un dubbio su [concetto], puoi chiarire?"

---

*Creato: 2026-02-03*
*Ultimo aggiornamento: 2026-02-03*
