# 💡 Idea Backlog

> Raccolta delle idee che vengono durante il percorso di apprendimento.
> Ogni idea viene valutata per decidere se/come integrarla.

---

## 📋 Processo di Valutazione

Quando arriva un'idea:

### 1. Cattura immediata
Scrivi l'idea appena arriva (anche 2 righe).

### 2. Valutazione (3 domande)

| Domanda | Risposta |
|---------|----------|
| **Cosa imparo?** | Quali skill/tecnologie? Si allinea con roadmap? |
| **Lo userei davvero?** | Motivazione personale? Risolve un mio problema? |
| **Quanto è grande?** | Side project (1-2 sett) / Progetto medio / Progetto grande |

### 3. Decisione

| Risultato | Azione |
|-----------|--------|
| Fit perfetto | Sostituisce/integra progetto esistente |
| Buona idea, timing sbagliato | Parcheggiata per dopo |
| Side project veloce | Settimana "libera" tra progetti |
| Non allineata | Backlog personale (post-percorso) |

---

## 💡 Idee

### IDEA-001: AI Teaching Platform (E-Learning con Ollama)

**Data:** 2026-02-17
**Status:** 🟢 Parcheggiata → Rivalutare dopo P5 (Mese 7-8)

**Descrizione:**
Webapp di e-learning con AI locale (Ollama) che usa la knowledge base creata durante il percorso. Un "insegnante AI" basato sugli appunti di Dan. Quello che ora fa con Claude/Obsidian diventa una piattaforma web accessibile.

**Stack ipotizzato:**
- Frontend: React/Next.js
- Backend: .NET 8 API
- AI: Ollama (locale) o Claude API
- Knowledge: RAG sulla Knowledge Base esistente
- Vector DB: per semantic search sulle note

#### Valutazione

| Domanda | Risposta |
|---------|----------|
| **Cosa imparo?** | RAG, Embeddings, Vector DB, Full-stack, AI integration |
| **Lo userei davvero?** | ✅ SÌ - risolve un problema reale (studiare con AI sui MIEI appunti) |
| **Quanto è grande?** | Progetto grande (2-3 mesi per MVP) |

#### Allineamento Roadmap

| Progetto Esistente | Overlap | Note |
|--------------------|---------|------|
| **P5 AI Second Brain** | 🔴 90% | RAG sul vault, query note con AI |
| **P6 Capstone** | 🟡 60% | Piattaforma educativa con AI |
| **P6 Interview Coach** | 🟢 30% | AI evaluation, structured output |

#### Decisione

**Verdict:** 🎯 **QUESTA IDEA È GIÀ NELLA ROADMAP!**

È essenzialmente la combinazione di:
- **P5 AI Second Brain** (RAG sulle tue note)
- **P6 Capstone Academic Knowledge Hub** (piattaforma educativa)

**Opzioni:**
1. **Merge P5 + Capstone** → Il tuo "AI Teaching Platform" diventa il progetto principale
2. **Aspetta P5** → Quando ci arrivi, lo personalizzi così
3. **Side project ora** → MVP minimale per validare l'idea (rischioso: distrae)

**Potenziale monetizzazione:** ⭐⭐⭐⭐⭐
- SaaS per studenti/professionisti
- White-label per aziende (formazione interna)
- Marketplace di "knowledge base" curate

#### Decisione Finale (2026-02-17)
**→ PARCHEGGIATA** - Rivalutare dopo P5 AI Second Brain (Mese 7-8).
Motivo: L'idea ha overlap alto con P5+P6. Meglio arrivarci con skill solide.

---

### IDEA-002: Focus Tube (YouTube Learning Client)

**Data:** 2026-02-24
**Status:** ✅ INTEGRATA → Senior Frontend P1

**Descrizione:**
Client alternativo per YouTube che elimina distrazioni (Shorts, raccomandazioni algoritmiche, infinite scroll) e trasforma la piattaforma in uno strumento di apprendimento. Community-driven curation: utenti valutano contenuti, creano playlist curate, si iscrivono a playlist altrui.

**Il problema:**
YouTube è progettato per massimizzare tempo speso, non valore ottenuto. Dan (e molti altri) perdono ore in scrolling invece di apprendimento mirato.

#### Decisione (2026-02-24)

**→ INTEGRATA** in nuovo percorso **Senior Frontend** come P1.

Vedi: `roadmaps/senior-frontend.md`

**Potenziale monetizzazione:** ⭐⭐⭐⭐⭐

---

---

### IDEA-003: FitHub (App Fitness Multi-tenant con AI)

**Data:** 2026-02-24
**Status:** ✅ INTEGRATA → Architect Quest P5 + Senior Frontend PX

**Descrizione:**
Applicazione fitness multi-versione (Stretching/Yoga, CrossFit, Palestra) con AI per assistenza allenamento. Supporta:
- **B2B:** Palestre/box come clienti (gestione turni allenatori, abbonamenti, programmazione)
- **B2C:** Utenti singoli (allenamento a casa, tracking progressi)
- **White-label:** Stessa codebase, diverse skin per mercati verticali

**Il problema:**
Le app fitness esistenti sono o troppo generiche o troppo costose per piccole palestre. L'AI può personalizzare gli allenamenti ma poche app lo fanno bene.

**Use case reale:**
Dan può proporlo alla palestra dove lavora come servizio extra a pagamento.

#### Valutazione

| Domanda | Risposta |
|---------|----------|
| **Cosa imparo?** | Multi-tenant architecture, AI workout planning, Flutter (rispolverare), White-label patterns, Subscription billing |
| **Lo userei davvero?** | ✅ SÌ - Lavoro in palestra, posso proporlo come servizio! |
| **Quanto è grande?** | Progetto GRANDE (4-6 mesi backend + 2-3 mesi Flutter) |

#### Allineamento Roadmap

| Progetto Esistente | Overlap | Come si Integra |
|--------------------|---------|-----------------|
| **P2 NutriPlan** | 🟡 40% | Nutrition AI → riutilizzabile in FitHub |
| **P3 BookingHub** | 🔴 70% | Multi-tenant, scheduling, subscriptions → base per FitHub |
| **P2.5 AI Gateway** | 🟢 30% | AI provider abstraction → usato in FitHub |
| **P4 FamilyBudget** | 🟡 50% | Flutter, offline-first → competenze per FitHub mobile |

#### Architettura Cross-Progetto

```
P1 Notification  →→→→→→→→→→→→→→→→→→→→┐
P2 NutriPlan (patterns AI nutrition) →→→┼→→→ P5 FitHub (REALE)
P2.5 AI Gateway →→→→→→→→→→→→→→→→→→→→┤
P3 BookingHub (multi-tenant, subs) →→→→→┤
P4 FamilyBudget (Flutter intro) →→→→→→→┘
                                         ↓
                               Senior Frontend PX: FitHub Mobile
```

#### Decisione (2026-02-24)

**→ INTEGRATA** come:
1. **Architect Quest P5** - Backend multi-tenant + AI (dopo P4)
2. **Senior Frontend PX** - App Flutter (dopo P5 backend completato)

**Potenziale monetizzazione:** ⭐⭐⭐⭐⭐
- SaaS per palestre (€50-200/mese)
- Commissione su abbonamenti gestiti
- White-label licensing
- **Già un cliente potenziale: la palestra dove lavora Dan!**

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| Idee totali | 3 |
| Integrate in roadmap | 2 |
| Parcheggiate | 1 |
| Scartate | 0 |

---

*Ultimo aggiornamento: 2026-02-24*
