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

### IDEA-004: AI Ecosystem Awareness Sessions

**Data:** 2026-03-25
**Status:** 🟢 Parcheggiata → Sessioni da 30-45 min durante deload o fine sessione

**Descrizione:**
Sessioni di awareness (no implementazione) sull'ecosistema AI che un AI Engineer deve conoscere per colloqui e per riconoscere tool/framework in progetti reali. L'obiettivo è saper dire "lo conosco, nel mio caso ho scelto X perché Y".

**Formato:** Conversazione strutturata per ogni topic — cos'è, quando si usa, pro/contro, come si confronta con quello che costruisci tu in P2.5.

#### Classifica per importanza (studia in quest'ordine)

> Se finisci i progetti prima del previsto, attacca questa lista dall'alto.
> A-tier = quasi sicuramente ti servirà, D-tier = nice to have.

**A-tier — Quasi sicuramente ti servirà**

1. **Semantic Kernel (Microsoft)** — Equivalente .NET di LangChain. NEL TUO STACK — se cerchi ruoli AI in aziende Microsoft-stack, te lo chiedono
2. **LangChain / LangGraph** — Lo standard de facto (Python). Il 70% dei progetti AI lo usa. Devi sapere parlarne fluentemente
3. **Prompt Management & Versioning** — Come gestire prompt in produzione: versioning, A/B deploy, rollback. Ogni azienda che fa AI in prod ha questo problema
4. **OpenTelemetry GenAI Semantic Conventions** — Nuove convenzioni OTEL specifiche per LLM (gen_ai.* attributes). Tu hai già OTEL, questo è l'upgrade naturale

**B-tier — Ti dà un vantaggio concreto**

5. **Hugging Face** — Hub modelli, Transformers library, Inference API. Ecosistema onnipresente, se ti danno un modello custom passa da qui
6. **Vector DB landscape** — Pinecone, Weaviate, Qdrant, ChromaDB vs il tuo pgvector. Domanda da colloquio classica: "quando serve un DB dedicato?"
7. **LangSmith / LangFuse / Braintrust** — Observability & eval platforms per LLM. Tu costruisci eval custom, sapere quando preferire piattaforme pronte
8. **AI Cost Management a scala** — Budget alerts, cost allocation per feature/team, token budgeting a livello org. Ogni CTO vuole sapere "quanto ci costa l'AI"

**C-tier — Buono da sapere, non bloccante**

9. **LlamaIndex** — Framework focalizzato su RAG. Più di nicchia rispetto a LangChain ma utile in progetti RAG-heavy
10. **AI Orchestration durabile (Temporal.io / Inngest / Hatchet)** — Workflow AI long-running (ore, non secondi). Importante in sistemi complessi, ma non dal giorno 1
11. **CrewAI / AutoGen** — Framework multi-agent alternativi. Multi-agent è hot ma ancora early
12. **GGUF / GGML / Quantization** — Come funzionano i modelli locali di Ollama. Q4 vs Q8. Ti distingue tecnicamente
13. **LoRA / QLoRA** — Fine-tuning efficiente. Completa il tuo decision framework con il "come si fa" pratico
14. **OpenAI Assistants API / GPTs** — Modello "managed agent" di OpenAI. Sta perdendo rilevanza vs approcci custom

**D-tier — Nice to have**

15. **Guardrails AI / NeMo Guardrails (NVIDIA)** — Framework dedicati a safety. Tu costruisci custom, sapere che esistono basta
16. **DSPy** — Framework per "programmare" prompt in modo strutturato (Stanford). Affascinante ma di nicchia
17. **Tokenization (BPE, SentencePiece)** — Perché "token" ≠ "parola", impatto su costi e context window. Cultura generale
18. **vLLM / TensorRT-LLM** — Inference optimization per modelli locali. Troppo infra per AI Engineer generalista
19. **ONNX Runtime** — Inference cross-platform, rilevante per .NET ma di nicchia nel mercato AI
20. **Weights & Biases (W&B)** — Experiment tracking. Più per ML Engineer che AI Engineer
21. **AI Gateway products (Portkey, LiteLLM, Helicone)** — Prodotti che fanno quello che costruisci in P2.5. Sapere i competitor basta

#### Quando farle

- Sessioni deload (solo quiz + lettura + awareness)
- Fine sessione quando avanza tempo (ultimi 30 min)
- Prima di iniziare job search (refresh generale)
- **NON** durante sessioni di coding/progetto attive

#### Decisione (2026-03-25)

**→ PARCHEGGIATA** come sessioni opzionali ricorrenti. Nessuna priorità sopra i progetti, ma da integrare nei tempi morti.

---

### IDEA-005: n8n Prototype vs Engineered — Il Confronto

**Data:** 2026-03-26
**Status:** ✅ INTEGRATA → Pratica standard in ogni progetto (vedi `claude/CLAUDE.md` sezione "n8n Prototype Practice")

**Descrizione:**
Costruire un workflow con n8n (1-2 ore) che replica il risultato finale di un progetto del percorso, poi confrontarlo con la versione engineered quando il progetto è completato. L'obiettivo è duplice:
1. **Vedere subito il "traguardo"** — motivazione tangibile
2. **Capire i limiti** — quando n8n crolla e perché serve engineering vero

**Prototipo suggerito: Notification Pipeline**
```
n8n workflow (1-2 ore):
Webhook (POST /notify) → IF email/sms → Send Email (Gmail node) → On Error → Retry 3x → Log to Sheet

Equivalente engineered (AQ P1):
API → Command Handler → Domain Validation → RabbitMQ → Worker → Retry/DLQ → Idempotency → Multi-channel
```

**Confronto da fare a fine P1:**

| Aspetto | n8n | Tuo codice |
|---------|-----|-----------|
| Tempo di setup | 1-2 ore | 5 settimane |
| 10k notifiche | Crolla | Gestisce |
| Retry granulare | Generico | Per canale con backoff |
| Test automatici | Zero | 268+ |
| Costo a scala | $50-200/mese | $5-10/mese |
| Modificabilità | Drag & drop | PR + review + test |

**Uso futuro di n8n nel percorso:**
- Prototyping rapido prima di ogni progetto ("ecco cosa costruiremo")
- Automazioni interne reali (sync vault, reminder, CI notifications)
- Portfolio piece: "Ho prototipato con n8n in 2h, poi engineered per produzione — ecco perché"

#### Valutazione

| Domanda | Risposta |
|---------|----------|
| **Cosa imparo?** | Low-code awareness, confronto architetturale, saper valutare build vs buy |
| **Lo userei davvero?** | ✅ SÌ - sia come prototipo che per automazioni personali |
| **Quanto è grande?** | Side activity (2-4 ore per il prototipo, poi confronti durante il percorso) |

#### Decisione (2026-03-26)

**→ INTEGRATA** come pratica standard per ogni progetto (sandwich PRIMA + DOPO).
- Per AQ P1 e SE P1 (già in corso): solo confronto DOPO a fine progetto
- Da P2 in poi: sandwich completo
- Regole e XP in `claude/CLAUDE.md` sezione "n8n Prototype Practice"

---

## 📊 Statistiche

| Metrica | Valore |
|---------|--------|
| Idee totali | 5 |
| Integrate in roadmap | 3 |
| Parcheggiate | 2 |
| Scartate | 0 |

---

*Ultimo aggiornamento: 2026-03-26*
