---
tags: [context, ai-skills, job-market, gap-analysis]
created: 2026-04-23
status: batch-1-complete
---

# Job Postings Analysis — AI Skills Enrichment

> Accumulo annunci rilevanti per il ruolo AI Engineer / AI Tech Lead. Ogni 3-5 annunci → gap analysis contro `roadmaps/ai-skills.md` → update roadmap.

---

## Batch 1 (COMPLETO — 8/8) — IT + UK mix

### #1 — Open Reply — AI Tech Lead

**Meta:**
- Azienda: Open Reply (gruppo Reply, system integrator enterprise)
- Settori clienti: Finance, Telco, Automotive, Oil&Gas, Retail, Public Sector
- Sede: Milano (ibrida)
- Seniority: Tech Lead — 3+ anni AI/ML enterprise
- Leadership: SI (coordinamento team, roadmap tech, stakeholder)

**GenAI Frameworks (deep):**
- LangChain
- LangGraph
- Langfuse (observability LLM)
- LlamaIndex

**LLM Skills:**
- Conoscenza dei principali LLM
- Selezione/valutazione LLM per use case specifico
- **Fine-tuning** LLM
- Valutazione consumi runtime (token, costi, latenza)
- Dimensionamento macchine (fisiche/virtuali) per esecuzione modelli **on-premises**

**Classical ML / DL:**
- Framework: TensorFlow, PyTorch, scikit-learn, Keras (almeno uno approfondito)
- Domini: NLP, Computer Vision, Recommendation Systems, GenAI
- Training, validation, ottimizzazione modelli
- Deep Learning fondamentali

**MLOps:**
- Docker, Kubernetes
- MLflow (model registry, tracking)
- Airflow (orchestrazione)
- CI/CD per AI
- Pipeline ciclo vita modello: data ingestion → training → deployment → monitoring → retraining

**Cloud AI:**
- AWS / Azure / GCP — servizi AI managed

**Software Engineering fundamentals:**
- Python (primario)
- Java (secondario)
- OOP + design patterns solidi
- Protocolli di rete
- Crittografia + security best practice

**Architecture:**
- Progettazione architetture AI **scalabili**
- Soluzioni ML end-to-end (data → prod)

**Leadership / Soft skills (Tech Lead markers):**
- Traduzione business requirements → soluzioni AI misurabili
- Gestione progetti end-to-end
- Coordinamento team multidisciplinari (DE, DS, SW Architect)
- Definizione roadmap tecnologiche
- Mentorship / promozione cultura AI
- Sperimentazione nuove tech

**Nota particolare:** molto peso su **on-premises** (dimensionamento macchine fisiche per modelli) — segnale di cliente enterprise con constraint di data residency/compliance. Non è il tipico "tutto su API OpenAI".

---

### #2 — Reply — AI Engineer

**Meta:**
- Azienda: Reply (gruppo, IC role — non Tech Lead)
- Sede: ibrida, EN richiesto
- Seniority: IC mid/senior (non specificato anni, ma "hands-on" + portfolio)
- Leadership: NO (collaborazione, code review, knowledge sharing)

**GenAI Frameworks:**
- LangChain
- LangGraph
- **LiteLLM** ← nuovo (proxy multi-provider LLM)
- **Hugging Face Transformers** ← nuovo esplicito

**Vector & Data:**
- **Vector databases** ← esplicito (mancava in #1)

**LLM Skills:**
- LLM training + fine-tuning
- **Evaluation / benchmarking modelli AI** (esplicito)
- Tool: **Ragas, DeepEval** ← nuovo, evals dedicati
- Nice-to-have: **small high-performance models** (SLM, distillation, quantization)
- Nice-to-have: **ottimizzazione inference latency + costi**

**MLOps / Infra:**
- Docker, Kubernetes
- Cloud AI: AWS, GCP, Azure
- Nice-to-have: **Infrastructure as Code (Terraform)** ← nuovo
- Nice-to-have: **Claude Code** ← interessante (Dan ha già la cert!)

**Software Engineering:**
- Python (essential, deep)
- Software engineering best practices

**Soft skills:**
- Curiosità + proattività
- Critical thinking, adaptability
- **English fluente** (esplicito)
- Attention to detail
- Open-source contribution / public portfolio (signal di crescita)

**Differenze vs #1:** no Java, no on-premises, no leadership, ma compaiono **vector DB**, **evaluation tools dedicati** (Ragas/DeepEval), **IaC**, **SLM/inference optimization**. Più "modern AI engineer" puro vs "tech lead enterprise".

---

### #3 — hlpy — AI Engineer (LLMOps + Agents)

**Meta:**
- Azienda: hlpy (scale-up, roadside assistance, IT/FR/ES/DE)
- Sede: remote
- Seniority: senior IC ("several years professional experience", hands-on, ownership)
- Leadership: NO (co-own backlog, share ownership con altro AI Engineer)
- Tipo: product company AI-first

**Agent / GenAI:**
- **AI agent frameworks in production** (generico, non vincola tool)
- **Agentic architecture, patterns, trade-offs** ← primo annuncio esplicito
- Agent development end-to-end (scoping → prod)
- Co-ownership backlog agenti

**LLMOps (focus PRINCIPALE):**
- **LLMOps** come termine esplicito (vs MLOps generico)
- **Evaluation pipelines** + **prompt testing** + **observability** + **continuous monitoring**
- Define metrics agent accuracy + degradation detection
- **Automated monitoring pipelines** che triggerano su accuracy degradation
- **Large-scale evaluation datasets** costruiti da real production cases (data flywheel)
- Evaluation harness + dataset-driven testing at scale (nice-to-have)

**Tooling & Integrations (focus PRINCIPALE):**
- **MCP servers** ← primo annuncio esplicito (Dan ha cert Claude Code → MCP coperto)
- **API design** REST + MCP (build, consume, test)
- Third-party integrations
- Product-level connections
- Valutazione tools/lib emergenti (speed vs reliability trade-off)

**DevOps:**
- Docker, CI/CD, infrastructure automation
- IaaS practices

**Software Engineering:**
- **Full-stack software engineering background** (esplicito — SE è prerequisito, AI è layer sopra)
- Hands-on, delivery-oriented, ownership

**Differenze vs #1 e #2:**
- **NON cita** fine-tuning, TF/PyTorch, MLflow, Airflow, Langfuse, LiteLLM, vector DB
- Probabilmente usano LLM via API + RAG, focus tutto su **orchestrazione agenti + ops**
- Mindset "product engineering" non "ML research"
- **MCP** + **agentic patterns** + **eval harness from prod data** = profilo molto contemporaneo

---

### #4 — Jet HR — Software Engineer Growth (AI-augmented) ⭐ HIGH WEIGHT

**Meta:**
- Azienda: Jet HR (startup IT, well-funded — 25M€ Serie A da Base10, Marco Ogliengo & Francesco Scalambrino founders)
- **Dan flag:** azienda all'avanguardia, molto seguita in Italia → **peso maggiore**
- Sede: full remote (timezone IT-compatible)
- RAL: €40-65k
- Seniority: ≥1 anno SE, ownership totale (no PM, no spec dettagliate)
- Tipo: **NON è AI Engineer puro** → è **Growth Engineer AI-augmented**

**Categoria emergente di ruolo (NUOVA vs #1-3):**
- AI come **leva di business**, non come prodotto finale
- Costruisce **agenti interni** che muovono revenue (sales, marketing, GTM, growth)
- Profilo ibrido: SWE backend + AI usage + business mindset + product sense

**Use case agenti (concreti):**
- **Sales agents**: valutazione qualità lead, routing, x10 team Sales
- **Marketing agents**: gestione milioni € campagne ads (creative + ottimizzazione)
- **GTM**: pipeline enrichment, data tooling
- **Growth**: referral, esperimenti pricing, feature virality

**Stack tecnico (implicito — non vincolano):**
- Backend + infrastruttura solidi (≥1 anno SE)
- AI integrata in prodotti già costruiti
- Nessun framework/linguaggio specifico richiesto → il valore è **come usi l'AI**

**"AI-pilled" definition:**
- "Non sei un vibe coder, ma sai come usare l'AI per andare veloce"
- Hai già spedito prodotti con AI dentro
- → Coding-with-AI mastery (Claude Code, Cursor, Aider) come skill di prima classe

**Soft skills (PESO ALTO):**
- **Ownership totale** senza PM né spec
- **Pragmatismo radicale**: prototipo in 2 giorni > soluzione perfetta in 2 settimane
- **Business mindset**: misurato in revenue/ore risparmiate, non OKR generici
- **UX awareness** anche su tool interni
- Proattività + spirito sperimentale (testing, iterazione)

**Differenze sostanziali vs #1-3:**
- Zero menzione di: LangChain/LangGraph, fine-tuning, MLOps tools, vector DB, evaluation pipelines, MCP
- Zero menzione di domini AI classici (NLP, CV, RecSys)
- L'azienda **non vende AI**, **usa AI internamente** per crescere
- Profilo "Forward-Deployed Engineer" / "AI-Native Software Engineer"

**Insight chiave per Dan:**
Questo annuncio rappresenta un **pattern di mercato in forte crescita**: aziende che cercano SWE che sappiano **costruire agenti interni per amplificare il business**. È un ruolo accessibile prima di diventare AI Engineer "puro" — leva su skill SWE solide + uso intelligente di LLM API.

---

### #5 — Homey (London, UK) — AI-Native Engineer (Early Career)

**Meta:**
- Azienda: Homey (PropTech UK, established + scale-up)
- Sede: London (UK)
- Seniority: **Early career esplicito** (graduate, school leaver, junior dev)
- Tipo: AI-Native software engineer (categoria #4 confermata + estesa)

**"AI-Native" engineer — definition esplicita:**
- LLM (Claude Code, Grok, GitHub Copilot, **Cursor**) come "superpower"
- Ship high-quality code at speed
- "Build things fast" > "memorize syntax"
- Già attivamente usa AI per scrivere/raffinare progetti

**Tools menzionati (espliciti):**
- **Claude Code** ← Dan ha cert
- **Grok**
- **GitHub Copilot**
- **Cursor**

**Stack tecnico:** ZERO menzionato. Il valore è nel **come usi l'AI per shippare**, non in quale stack.

**Soft skills:**
- Can-do attitude
- Ownership day one
- Curiosità (interesse a disrupt real estate)
- Mentorship-receptive

**Application requirement (segnale forte):**
- Apply con **GitHub link** + **progetto AI-built**
- → Portfolio AI-augmented è ora un prerequisito di candidatura

**Conferma vs #4 Jet HR:**
Questo annuncio **conferma e rafforza** il profilo #4 (AI-Native SWE). È diventata una **categoria di ruolo di mercato consolidata**, non una stranezza italiana:
- Tutti i tool AI di coding nominati esplicitamente
- Stack tecnico irrilevante vs mindset
- Portfolio AI-built come asset principale
- Accessibile da early career (non serve seniority)

**Implicazione strategica per Dan:**
Dan ha già il vantaggio competitivo per questa categoria:
- ✅ Claude Code cert (8/8 Perfect Score)
- ✅ 3 anni SE
- ✅ Mindset di studio strutturato (Learning Hub)
- ❌ MANCA: portfolio pubblico GitHub di progetti **AI-augmented** (non solo "studied AI", ma "built X with AI")

---

### #6 — Euphoric (London, UK) — Software Engineer Full-Stack AI-First

**Meta:**
- Azienda: Euphoric (HR-tech / benefits admin AI-first, spin-out di Peppy Health Series B, seed Ott 2025)
- Sede: Remote-first, London hub (UK/EU candidates, preferenza vicino Londra)
- RAL: **£90k-110k** (~€105-128k) ← primo annuncio con range salariale UK alto
- Seniority: **2+ anni industry experience**
- Tipo: **Full-stack SWE AI-first** (mix tra #2 e #4)

**Stack tecnico (PRIMO annuncio esplicito full-stack):**
- **Frontend**: React + JavaScript/TypeScript
- **Backend**: Python + **FastAPI** + **SQLAlchemy** ← nuovo (FastAPI primo annuncio)
- **Cloud**: **GCP preferred** (AWS/Azure ok) ← primo annuncio con preferenza cloud
- **Data pipelines** + **RESTful API**
- CI/CD + peer review

**AI/ML methods (variety wide):**
- Agents / LLMs
- **Recommender systems** (#1 generico, qui esplicito core)
- **Reinforcement learning** ← primo annuncio esplicito RL
- **Personalization + experimentation** (A/B tests AI-driven)

**AI coding tools:**
- **Cursor** ← conferma #5
- **Windsurf** ← nuovo (Codeium)
- "Push the boundary of AI-powered software dev tools"

**Soft skills:**
- Cross-functional (design + product + ML + frontend)
- Comunicazione tecnica/non-tecnica
- Pragmatic best practices (tech debt vs delivery speed)
- "Do whatever it takes"
- Curiosità + tenere il passo con AI advances

**Insight:**
Profilo **ibrido full-stack + AI-first** — non è AI Engineer puro né SWE puro. Sta in mezzo. Devi:
- Saper buildare features end-to-end (FE + BE + ML)
- Switch contesto da "fix bug frontend" a "iterate ML pipeline" senza problemi
- Usare AI tools per amplificare velocity

**Profilo "T-shaped":** ampio su FE/BE/ML, profondo su Python+AI.

---

### #7 — AI Engineer (London, recruiter-posted) — Generalist End-to-End

**Meta:**
- Azienda: non specificata (recruiter-posted, City London)
- Sede: London hybrid (no sponsorship)
- RAL: **£90k-120k** + bonus (~€105-140k) — coerente con #6
- Seniority: "engineers at all levels"
- Tipo: AI Engineer generalist end-to-end

**Skill richiesti (concisi, conferme solo):**
- **Python** + dati + **LLM tooling** moderno
- **Unstructured data** handling ← nuovo termine esplicito
- **Pipelines** robuste data → produzione
- **API** reliable in production
- Software dev skills forti
- **Model deployment** + **DevOps** + **MLOps**
- Containerization + CI/CD
- Comunicazione + ownership + problem solving

**Insight:**
Conferma il **core comune** del mercato AI Engineer London. Niente di nuovo rispetto al batch — utile come **baseline minimo richiesto** per fascia £90-120k a Londra:
- Python + LLM tooling (qualsiasi, non vincolato)
- Pipeline data + API production
- DevOps/MLOps + CI/CD + container
- End-to-end ownership

**Nuovo termine:** **unstructured data** (PDF, immagini, audio, testo libero) → skill rilevante per RAG, document processing, multimodal.

---

### #8 — AI-Native Fintech (London, Series A) — Senior AI Engineer Multi-Agent ⭐ HIGH-END

**Meta:**
- Azienda: AI-native fintech (investment/financial services), Series A appena chiuso
- Sede: **London in office full time** (no remote)
- RAL: **£100k-200k base** + ~$160k equity 4 anni (top tier UK)
- Seniority: **4+ anni AI/ML eng** OR strong SWE + AI exposure
- Tipo: Senior AI Engineer multi-agent, founder-adjacent

**Core technical responsibilities:**
- **Architecting + deploying multi-agent systems** ← esplicito multi-agent (vs single agent #3)
- **Scalable RAG pipelines** + retrieval systems
- **Evaluation frameworks**: performance + **safety** + reliability ← safety nuovo (regulatory)
- AI-driven products in real-world enterprise

**Stack tecnico esplicito:**
- Python backend (**FastAPI / Django**) ← Django nuovo
- Infrastructure + production deployment
- **PyTorch / TensorFlow** (conferma #1)
- **RAG architectures** (esplicito)
- **Vector databases** (esplicito)
- Modern cloud infra

**Patterns / Frameworks (espliciti per nome):**
- **LangGraph** (3a citazione: #1, #2, #8)
- **ReAct** pattern ← nuovo
- **Chain-of-Thought (CoT)** pattern ← nuovo
- "...or building similar systems **from scratch**" ← segnale: capire i pattern, non solo usare framework

**System design AI (esplicito):**
- Orchestration
- **Memory** (per agenti — short/long term)
- Deployment
- Monitoring

**Soft skills:**
- Autonomia in ambienti ambigui
- Decision-making veloce
- Founder-adjacent comfort

**Insight:**
- Profilo top-tier London fintech: stack ampio (RAG + agents + classical ML) + system design AI + safety/evaluation rigorose.
- "Build from scratch" è un segnale potente: non basta saper usare LangGraph, devi sapere **come funziona dentro** (graph state machines, message passing, tool calling, memory architectures).
- **Safety in evaluation** è un nuovo asse (compliance fintech) — guardrails, alignment, hallucination detection.

---

## Pattern emergenti (8/8 annunci — finale)

**Stack ricorrente in 3/3:**
- **Python** (100%)
- **Docker / containerization** (100%)
- **CI/CD + cloud** (100%)
- **Evaluation / benchmarking** (100% — #1 generico, #2 Ragas/DeepEval, #3 eval harness from prod)
- Software engineering fundamentals solidi (100%)

**Citato in 2/3:**
- **LangChain + LangGraph** (#1, #2 espliciti — #3 generico "agent frameworks")
- **Fine-tuning LLM** (#1, #2 — manca in #3 product company)
- **Cloud AI managed** AWS/GCP/Azure (#1, #2)
- **Kubernetes** (#1, #2)
- Agentic patterns / multi-agent (#1 implicito via LangGraph, #3 esplicito)

**Citato in 1/3 (da monitorare nel batch successivo):**
- **MCP servers** (#3) ← contemporaneo, Dan ha già cert
- **Vector DB** esplicito (#2)
- **LlamaIndex, Langfuse, LiteLLM, HF Transformers** (#1 o #2)
- **Ragas, DeepEval** (#2) — evals dedicati
- **MLflow, Airflow** (#1) — ML classico
- **TF/PyTorch/sklearn/Keras** (#1) — ML classico
- **Terraform IaC** (#2)
- **Inference optimization** SLM/latency/costi (#2)
- **On-premises** / HW sizing (#1)
- **Java** (#1)
- **Computer Vision, RecSys** (#1)
- **Production data → eval dataset** flywheel (#3)
- **Agentic architecture/patterns** esplicito (#3)
- **Leadership** (#1 only — Tech Lead role)

**Insight (4 annunci → 4 profili distinti):**
- #1 = **Tech Lead enterprise** system integrator (broad, leadership, on-prem, Java)
- #2 = **AI Engineer GenAI puro** IC (eval con tool, IaC, SLM)
- #3 = **AI Engineer product company** (LLMOps + agents + MCP, no ML classico)
- #4 = **Growth Engineer AI-augmented** (uses AI for business leverage, no AI stack vincolato)

**Il core comune (3-4 annunci):**
Python + Docker + cloud + agenti/LLM API + evaluation/iteration loop + business pragmatism.

**Skill traversali emergenti (NON puramente tech):**
- **Ownership / autonomia** (#3, #4 espliciti)
- **Pragmatismo / prototyping** (#4 esplicito)
- **Business mindset** (#1 traduzione req, #4 revenue-driven)
- **UX awareness** (#4 esplicito)

**Tassonomia di mercato che si sta delineando:**

| Categoria | Stack | Mindset | Esempi |
|-----------|-------|---------|--------|
| AI Tech Lead Enterprise | Broad + leadership + on-prem + ML classico | Architettura + team | #1 Open Reply |
| AI Engineer GenAI puro | LangChain + Ragas + IaC + SLM | Modern IC research-leaning | #2 Reply |
| AI Engineer Product/LLMOps | LLMOps + agents + MCP + eval harness | Ship-and-iterate | #3 hlpy |
| AI-Augmented SWE / Growth | Backend + AI API + business sense | Business leverage | #4 Jet HR |

**Implicazione per Dan:**
Il profilo #4/#5 è **immediatamente raggiungibile** con SE skills + Claude Code cert + portfolio GitHub di progetti AI-augmented. I profili #2/#3 richiedono più tempo (eval pipelines, MCP, agentic patterns). #1 è il long-game (3+ anni AI + leadership).

**Conferma cross-mercato (IT vs UK):**
- #4 (Jet HR, IT) e #5 (Homey, UK) confermano che "AI-Native SWE" è una categoria **internazionale consolidata**, non una bolla italiana.
- Tool AI coding (Claude Code, Cursor, Copilot, Windsurf) ora sono **prerequisiti espliciti** di candidatura, non nice-to-have.
- Portfolio AI-built su GitHub è chiesto **direttamente** in fase application.

---

## SINTESI FINALE BATCH 1 (8/8)

### Frequency table tecnologie/skill

**Citato in 8/8 (CORE INEVITABILE):**
- Python
- LLM / GenAI usage
- Software engineering fundamentals + ownership

**Citato in 6-7/8 (HIGH PRIORITY):**
- Docker / containerization (#1, #2, #3, #6, #7)
- Cloud (AWS/GCP/Azure) (#1, #2, #3, #6, #7, #8)
- CI/CD + DevOps (#1, #2, #3, #6, #7)
- Evaluation / benchmarking (#1, #2, #3, #7, #8) — sempre più strutturato
- Production deployment + API (#1, #2, #3, #6, #7, #8)

**Citato in 4-5/8 (MEDIUM PRIORITY — differenzianti):**
- LangChain / LangGraph (#1, #2, #8 espliciti, #3 generic)
- Agent frameworks / agentic patterns (#1, #3, #4, #5, #6, #8)
- AI coding tools (Claude Code, Cursor, Copilot, Windsurf) (#2, #4, #5, #6)
- Vector databases (#2, #8 espliciti, #1 implicito via LlamaIndex)
- RAG architectures (#2 implicito, #8 esplicito)
- Pythonic backend (FastAPI/Django) (#6, #8)
- TypeScript/React frontend (#6 + soft requirement #4)
- Fine-tuning LLM (#1, #2)
- Kubernetes (#1, #2)
- PyTorch / TensorFlow (#1, #6 generic, #8)
- MLOps stack (MLflow, Airflow) (#1)

**Citato in 1-3/8 (NICHE / SPECIALIZED):**
- MCP servers (#3) ⭐ Dan ha cert
- Multi-agent systems (#8 esplicito)
- ReAct + CoT patterns (#8)
- Memory architectures per agenti (#8)
- Safety evaluation / guardrails (#8) ← regulatory pressure
- Recommender systems (#1, #6)
- Reinforcement Learning (#6)
- Computer Vision (#1)
- NLP classico (#1)
- LiteLLM, Langfuse, LlamaIndex, HF Transformers (#1, #2)
- Ragas, DeepEval (#2)
- Terraform IaC (#2)
- SLM / inference optimization (#2)
- On-premises / HW sizing (#1)
- Java (#1)
- Unstructured data (#7)
- Multi-modal / document AI (implicito #7)

### Salary anchors emersi

| Mercato | Profilo | Range |
|---------|---------|-------|
| IT (Jet HR) | Growth Eng AI-augmented | €40-65k |
| UK London (Homey) | AI-Native junior | non specificato |
| UK London (Euphoric) | Full-stack AI-first 2+yr | £90-110k (~€105-128k) |
| UK London (recruiter generico) | AI Eng generalist | £90-120k + bonus |
| UK London (fintech Series A) | Senior AI Eng multi-agent 4+yr | £100-200k + ~$160k equity |

**Insight:** Mercato UK paga 2-3x rispetto IT per stesso seniority. Senior multi-agent fintech London = top tier (£200k+).

### Categorie di ruolo confermate (4 cluster distinti)

| # | Categoria | Esempi | Stack tipico | Salary EU range |
|---|-----------|--------|--------------|-----------------|
| 1 | **AI Tech Lead Enterprise** | #1 Open Reply | Broad + leadership + on-prem + Java + ML classico | €70-100k IT |
| 2 | **AI Engineer GenAI / LLMOps** | #2 Reply, #3 hlpy, #7 recruiter, #8 fintech | LangChain/LangGraph + RAG + eval + agents + MCP | €80-180k+ |
| 3 | **Full-Stack AI-First Engineer** | #6 Euphoric | React/TS + Python/FastAPI + AI methods | €90-130k |
| 4 | **AI-Augmented SWE / Growth Engineer** | #4 Jet HR, #5 Homey | SWE backend + AI tools mastery + business sense | €40-80k IT (UK più alto) |

### Profili strategici per Dan (ordine di accessibilità)

1. **Immediato (3-6 mesi):** Cluster #4 (AI-Augmented SWE) → ha già SE + Claude Code cert. Manca: portfolio GitHub di 2-3 progetti AI-built business-oriented.
2. **Mid-term (6-12 mesi):** Cluster #3 (Full-Stack AI-First) → richiede React/TS + Python/FastAPI + AI methods applicati. Dan ha React side-track.
3. **Mid-term (12-18 mesi):** Cluster #2 (AI Engineer GenAI/LLMOps) → richiede LangChain/LangGraph + RAG + eval pipelines + agents + MCP. Path di studio strutturato necessario.
4. **Long-term (18-30+ mesi):** Cluster #1 (AI Tech Lead Enterprise) → richiede 3+ anni AI esperienza + leadership track + ML classico (PyTorch/TF). Solo dopo aver consolidato il cluster #2.

---

## Gap identificati vs `roadmaps/ai-skills.md`

*Da compilare a fine batch.*
