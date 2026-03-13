---
tags: [architect-quest, project, ai-track, ai-1, rag, vector-db, embeddings]
status: locked
duration: 2 months
start: M7
end: M8
parallel-to: P2-NutriPlan
type: ai-first
---

# 🧠 AI-1: AI Second Brain

## 📋 Overview
Il tuo Obsidian vault diventa queryabile con AI. Semantic search sulle TUE note.

**Durata:** 2 mesi (Mesi 7-8) | **Focus:** RAG, Vector DB, Embeddings

**Tipo:** AI-First Project - Lo userai OGNI GIORNO!

**Parallelo a:** P2 NutriPlan

---

## 🎯 Obiettivo
Costruire un sistema che capisce e risponde su tutto quello che hai scritto nelle tue note Obsidian.

---

## 🛠️ Stack
- .NET 8 Minimal API (backend)
- Qdrant o ChromaDB (vector DB)
- Ollama embeddings (locale) + Claude per query complesse
- Obsidian plugin o CLI

---

## 📚 Cosa Imparerai

| Topic | Dettaglio |
|-------|-----------|
| RAG Completo | Chunking, embeddings, retrieval, generation |
| Vector Databases | Similarity search, indexing, filtering |
| Embedding Models | Sentence transformers, dimensionality |
| Prompt Engineering | Context injection, few-shot |
| Semantic Search | vs keyword search, quando usare quale |
| Chunking Strategies | Overlap, semantic boundaries |

---

## 🏗️ Come Funziona

```
┌─────────────────────────────────────────────────────────────┐
│                    TUO OBSIDIAN VAULT                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ CQRS.md │ │ DDD.md  │ │Redis.md │ │ ...     │           │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘           │
└───────┼───────────┼───────────┼───────────┼─────────────────┘
        │           │           │           │
        ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────┐
│                    CHUNKING + EMBEDDING                     │
│         Ogni nota → chunks → vectors (1536 dim)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    VECTOR DATABASE                          │
│                    (Qdrant/ChromaDB)                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  TUA QUERY: "Cosa ho imparato su Event Sourcing?"           │
│                              │                              │
│                              ▼                              │
│  1. Query → embedding                                       │
│  2. Similarity search → top 5 chunks                        │
│  3. Chunks + query → LLM                                    │
│  4. Risposta basata sulle TUE note!                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 📅 Piano Settimane

### Mese 7: RAG Foundation
- [ ] W1: Vector DB setup (Qdrant), embedding pipeline
- [ ] W2: Chunking strategies, Obsidian vault indexing
- [ ] W3: Retrieval + basic Q&A
- [ ] W4: Prompt optimization, context window management

### Mese 8: Features + Polish
- [ ] W5: Quiz generation dalle note
- [ ] W6: "Related notes" suggestions
- [ ] W7: CLI o Obsidian plugin
- [ ] W8: Boss Battle

---

## 📦 Deliverables

- [ ] Vector DB con tue note indicizzate
- [ ] Q&A funzionante sulle tue note
- [ ] Quiz auto-generation
- [ ] "Related notes" suggestions
- [ ] CLI o plugin Obsidian
- [ ] Response time < 3 sec

---

## ✅ Testing Checklist

- [ ] Unit tests - Chunking, embedding generation
- [ ] Integration tests - Vector DB operations
- [ ] Quality tests - Retrieval relevance
- [ ] Performance tests - Response time < 3 sec

---

## 🏆 Boss Battle: "Documentation Q&A"

**Scenario:** Estendi Second Brain per queryare documentazione tecnica esterna (Microsoft Docs, MDN, etc.)

| Parte | Deliverable |
|-------|-------------|
| **A. Design** | ADR-001 (chunking strategy per docs tecniche), C4 Container |
| **B. Domain Model** | Document, Chunk, QueryResult, Source tracking |
| **C. API Spec** | OpenAPI per index URL, query, list sources |
| **D. Implementazione** | Web scraper + indexer per docs esterne |

**Performance Goal:** Query con risposta in < 3 secondi su documento 50 pagine

**Reward:** ≥24/30 → +300 XP | ≥28/30 → +500 XP

---

## 💡 Uso Quotidiano

Questo progetto è speciale perché lo userai **ogni giorno** per:
- 🔍 Cercare nelle tue note: "Cosa avevo scritto su..."
- 📝 Generare quiz per spaced repetition
- 🔗 Trovare note correlate automaticamente
- 🧠 Consolidare la conoscenza

---

## 🔗 Integrazione con Learning Hub

```
Prima: "Dove avevo scritto sul Repository Pattern?"
       → Cerca manualmente tra 100+ note

Dopo:  "Cosa so del Repository Pattern?"
       → AI trova tutti i chunks rilevanti
       → Genera risposta basata sulle TUE parole
       → Cita le fonti (link alle note)
```

---

*Ultimo aggiornamento: 2026-03-04*
