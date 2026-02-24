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

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| Idee totali | 2 |
| Integrate in roadmap | 1 |
| Parcheggiate | 1 |
| Scartate | 0 |

---

*Ultimo aggiornamento: 2026-02-24*
