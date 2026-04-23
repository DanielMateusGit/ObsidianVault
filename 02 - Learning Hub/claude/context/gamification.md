# Sistema Gamification

---

## XP - Attivita Quotidiane

| Attivita | XP |
|----------|-----|
| Daily log | +10 |
| 30min studio | +20 |
| 1h studio | +40 |
| 2h+ studio | +60 |
| Commit con progressi | +15 |

## XP - Progetti

| Attivita | XP |
|----------|-----|
| Task completato | +50 |
| Deliverable completato | +100 |
| Modulo completato | +150 |
| Progetto completato | +500 |

## XP - Studio e Note

| Attivita | XP |
|----------|-----|
| Nota atomica creata | +20 |
| Capitolo libro letto | +30 |
| Capitolo + appunti | +45 |
| Articolo breve | +15 |
| Video | +15 |
| ADR scritto | +75 |
| Diagramma C4 | +60 |
| Approfondimento extra | +25 |

## XP - Spaced Repetition

| Risultato | XP |
|-----------|-----|
| Corretto | +10 |
| Parziale | +5 |
| Sbagliato | +2 |
| 5 corrette consecutive | +25 bonus |
| 10 corrette consecutive | +50 bonus |
| Quiz padroneggiato (Box 5) | +30 |

---

## Esami

### Quando Proporre (completion-based, NO date)

| Trigger | Tipo | Punti | Obbligatorio |
|---------|------|-------|--------------|
| Fine Modulo importante | Mini-verifica | 15 | Opzionale |
| Dopo 2-3 Moduli correlati (stesso topic) | Esame tematico | 30 | Opzionale-consigliato |
| Fine Progetto | Esame completo / Boss Battle | 30 | **OBBLIGATORIO** |
| Pre-Certificazione | Simulazione | 30+ | Su richiesta |

> **Principio:** nessun esame e legato a una data di calendario. Si fa quando i prerequisiti sono completi e Dan si sente pronto.

### Struttura Mini-verifica (15 punti, ~15 min)

| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 6 | 3 domande aperte |
| B | 4 | 4 multiple choice |
| C | 5 | 1-2 esercizi codice |

### Struttura Esame Completo (30 punti, ~30-45 min)

| Parte | Punti | Contenuto |
|-------|-------|-----------|
| A | 10 | 4-5 domande aperte |
| B | 6 | 6 multiple choice |
| C | 8 | 3+ esercizi codice |
| D | 6 | Design/Architettura |

### XP Esami

**Esami completi (30 punti):**

| Voto | XP |
|------|-----|
| >=27/30 | +200 (Lode) |
| >=24/30 | +150 (Merito) |
| >=18/30 | +100 (Superato) |
| <18/30 | +30 (Tentativo + ripasso) |

**Mini-verifiche (15 punti):**

| Voto | XP |
|------|-----|
| >=13/15 | +75 |
| >=11/15 | +50 |
| >=9/15 | +30 |
| <9/15 | +15 |

### Achievement Esami

| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| First Exam | Primo esame completato | +50 |
| Dean's List | 3 esami >=27/30 | +150 |
| Exam Veteran | 10 esami completati | +200 |
| Certification Ready | Esame certificazione >=24/30 | +300 |

---

## Boss Battle

Verifica autonoma alla fine di ogni progetto.

| Path | Focus |
|------|-------|
| Architect Quest | 70% Design, 30% Code |
| Senior Engineer | 30% Design, 70% Code |

| Risultato | XP |
|-----------|-----|
| >=24/30 | +300 |
| >=28/30 | +500 |

**Achievement finali:** Architect Champion (4/4) +1000 | Senior Champion (6/6) +1500

---

## Achievement Trasversali Roadmap v6 ⭐ (NUOVO 2026-04-23)

> Achievement aggiunti con job-postings-driven enrichment delle roadmap (`ai-skills.md` v3.1, `senior-frontend.md` v2.0, `senior-engineer.md` v6.0).
> Single source of truth — referenziati dalle roadmap (non duplicati).

### Senior Engineer (M-T moduli trasversali)

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 🌐 **Polyglot** | Porting di 1 modulo SE in 2nd linguaggio (Java/Node) + ADR — *opzionale on-the-job* | +400 |
| 📊 **Observability Master** | OpenTelemetry + Prometheus + Grafana + Jaeger in 1 progetto | +350 |
| ☁️ **Cloud Native Deployer** | 1 progetto SE deployato su AWS/GCP managed (production-grade) | +400 |
| 🔧 **IaC Practitioner** | Terraform completo per 1 progetto (VPC + compute + DB + secrets) | +300 |
| 🚀 **CI/CD Builder** | GitHub Actions su tutti i progetti core (lint + test + build + deploy) | +250 |
| 🆔 **Identity Federator** | OAuth2/OIDC + Auth0/Keycloak + SCIM endpoint integrati | +350 |
| 🤖 **AI-Native Backend** | LangGraph agent + MCP server + RAG production-grade + AI cert | +500 |

### Senior Frontend (P6 + moduli trasversali)

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 🤖 **AI-Native Frontend** | P6 completato + demo deployata (Vercel AI SDK + streaming UI) | +400 |
| 🛡️ **Security Aware** | Frontend security audit + 0 vuln su dependency | +200 |
| 🎯 **TypeScript Craftsman** | Branded types + Zod inferenza in 3+ progetti | +300 |
| 🧪 **Testing Champion** | Vitest + Playwright + MSW in 3+ progetti | +200 |

### Mini-Projects Portfolio (cross-roadmap, vedi `context/mini-projects-index.md`)

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 📦 **Mini Builder** | 5 mini-projects pubblicati GitHub (qualsiasi categoria AI/SE/FE) | +500 |
| 🚀 **Portfolio Pro** | 10 mini-projects + repo pinned curato | +750 |
| 🌍 **Cluster Ready** | Tutti i mini-projects per 1 cluster completati | +1000 |
| 🔥 **Triple Threat** | 1 mini-project che serve 3+ cluster con 3+ portfolio | +500 |

### XP per mini-project (singoli)

| Attivita | XP |
|----------|-----|
| Mini-project completato + GitHub README pro | +150 |
| Demo live deployata Vercel/Railway | +50 |
| Demo live deployata cloud managed (AWS/GCP) | +75 |
| README con AI tools workflow doc | +30 |
| Mini-project pubblicato come library/package (npm/NuGet) | +200 |
| Engagement reale (stars/issues/fork) | +100 |

### AI Skills Roadmap (Boss Battle nuovi)

| Achievement | Requisito | XP |
|-------------|-----------|-----|
| 🐍 **Python AI Bridge Built** | Python AI Bridge Project completato (FastAPI + LangGraph + pgvector + Ragas + Langfuse) | +500 |
| 🎯 **AI-Augmented SWE Ready** | Cluster #4 portfolio raggiunto (5 mini-projects AI-built) | +500 |

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

---

## Streak

**Per mantenere:** uno di questi ogni giorno:
- 30+ min di studio
- 1 commit con progressi
- 1 task completato

**Bonus:**

| Streak | Bonus |
|--------|-------|
| 7 giorni | +100 |
| 14 giorni | +200 |
| 30 giorni | +500 |
| 60 giorni | +1000 |

---

## Sedimentazione XP

| Attivita | XP |
|----------|-----|
| Nota atomica creata | +20 |
| Risorsa obbligatoria completata | +30 |
| Video visto | +15 |
| Approfondimento extra | +25 |
| Fase Sedimentazione completata | +100 |

---

## Certificazioni & Corsi

### XP Corsi

| Attivita | XP |
|----------|-----|
| Lezione completata | +15 |
| Nota/cheatsheet creata | +20 |
| Test finale superato | +50 |
| Perfect Score (100%) | +200 |
| Corso completato (100%) | +500 |
| Quiz estesi (oltre quelli base) | +50 |

### Achievement Corsi

| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| First Lesson | Prima lezione completata | 1 lezione | +50 |
| Course Master | Corso completato 100% | 100% | +500 |
| Perfect Score | Test finale perfetto | 100% test | +200 |
| Lifelong Learner | 3 corsi completati | 3 corsi | +300 |
| Certification Hunter | 5 certificazioni | 5 cert | +500 |

### Registro Certificazioni

| Data | Corso | Provider | Score | XP | Note |
|------|-------|----------|-------|-----|------|
| 2026-03-13 | Claude Code in Action | Anthropic | 8/8 (100%) | +980 | 25 quiz, cheatsheet completa |

### Regole Spaced Repetition Certificazioni

- Ogni certificazione genera quiz nel tracker
- **Minimo 1 quiz/giorno** dalla certificazione piu recente
- I quiz certificazione hanno **priorita alta** nella coda review
- Obiettivo: portare tutti i quiz a Box 3+ entro 30 giorni dal corso

---

## n8n Prototype Practice

| Attivita | XP |
|----------|-----|
| Prototipo n8n pre-progetto (kickoff) | +15 |
| Confronto n8n post-progetto (closeout) | +20 |

---

## Coach CLI

```bash
python3 coach.py briefing|status|suggest|quiz|add-xp|streak|motivation
```

---

*Aggiornato: 2026-04-23 (v2.0 — aggiunti Achievement Trasversali Roadmap v6: SE M-T moduli (Polyglot, Observability Master, Cloud Native Deployer, IaC Practitioner, CI/CD Builder, Identity Federator, AI-Native Backend), FE achievement (AI-Native Frontend, Security Aware, TypeScript Craftsman, Testing Champion), Mini-Projects Portfolio achievement (Mini Builder, Portfolio Pro, Cluster Ready, Triple Threat), AI Skills (Python AI Bridge Built, AI-Augmented SWE Ready). Cross-reference: `context/cluster-taxonomy.md`, `context/mini-projects-index.md`)*

*Versione precedente: 2026-04-17 (refactor self-paced — Week→Modulo, esami completion-based)*
