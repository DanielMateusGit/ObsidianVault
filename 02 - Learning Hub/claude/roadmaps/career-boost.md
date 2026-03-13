# Career Boost Module

> Modulo trasversale per passare da "bravo developer" a "hired senior"
> Parallelo ai progetti, Mesi 3-18+

---

## System Design Practice

**Obiettivo:** Saper spiegare e progettare sistemi "on the whiteboard"

**Cadenza:** 1 system design / settimana (30-45 min)

### System Design Topics

| # | Topic | Progetto Collegato | Quando |
|---|-------|-------------------|--------|
| 1 | URL Shortener | Senior P5 | Mese 3 |
| 2 | Rate Limiter | Senior P1.5 | Mese 3 |
| 3 | Chat System | Senior P2 | Mese 4 |
| 4 | Notification System | Architect P1 | Mese 5 |
| 5 | E-commerce Cart | Senior P3 | Mese 6 |
| 6 | Booking System | Architect P3 | Mese 7 |
| 7 | Social Feed | Standalone | Mese 8 |
| 8 | Search Autocomplete | Standalone | Mese 9 |
| 9 | Distributed Cache | Senior P5 (Redis) | Mese 10 |
| 10 | Video Streaming | Standalone | Mese 11 |
| 11 | Payment System | Senior P3 | Mese 12 |
| 12 | Ride Sharing (Uber) | Standalone | Mese 12 |

### System Design Template

Per ogni design, documenta:
```markdown
# System Design: [Nome]

## 1. Requirements (5 min)
### Functional
- User can...
- System should...

### Non-Functional
- Scale: X users, Y requests/sec
- Latency: < X ms
- Availability: 99.X%

## 2. Capacity Estimation (5 min)
- Storage: X GB/year
- Bandwidth: X MB/s
- Servers: ~X instances

## 3. High-Level Design (10 min)
[Diagramma ASCII o draw.io]

## 4. Deep Dive (15 min)
- Database schema
- API design
- Key algorithms

## 5. Trade-offs Discussed
- SQL vs NoSQL: chose X because...
- Caching strategy: X because...

## 6. Bottlenecks & Solutions
- Bottleneck: X → Solution: Y
```

### XP System Design
| Attivita | XP |
|----------|-----|
| Design documentato | +25 |
| Mock interview (con peer/Claude) | +50 |
| Design presentato in < 45 min | +30 |

---

## Communication Skills (Ongoing)

**Obiettivo:** Comunicare efficacemente in team remoti internazionali

### Code Review Best Practices

```markdown
## Quando fai review:
- "Consider using X because Y" (suggerimento con motivo)
- "I don't understand this part, could you explain?" (chiedere)
- "Nice approach! I learned something" (positivo)

## Quando ricevi review:
- "Good point, I'll change it"
- "I chose this because X, but your suggestion is better"
- Chiedere chiarimenti se non capisci
```

### Technical Writing Templates

| Documento | Quando | Template |
|-----------|--------|----------|
| **RFC** | Proporre cambio significativo | Problem → Proposal → Alternatives → Decision |
| **ADR** | Decisione architetturale | Gia coperto in Architect |
| **Post-mortem** | Dopo incident | What happened → Impact → Root cause → Action items |
| **Tech Spec** | Prima di feature grande | Context → Goals → Design → Milestones |

### English Technical Vocabulary

Flashcard per questi termini:
```
Scalability, Throughput, Latency, Availability
Trade-off, Bottleneck, Single point of failure
Eventual consistency, Strong consistency
Sharding, Replication, Partitioning
Circuit breaker, Bulkhead, Retry
Idempotent, Stateless, Immutable
```

### Async Communication Best Practices

```markdown
## Slack/Teams Messages
- Fornisci contesto completo (non "hi, can I ask you something?")
- Includi: What I tried → What happened → What I need
- Usa thread per discussioni
- Rispetta timezone (no urgenza finta)

## Written Updates
- Bullet points > wall of text
- Lead with conclusion
- Link a docs/PRs rilevanti
```

---

## API Mastery

**Obiettivo:** Progettare API che altri developer amano usare

### OpenAPI Spec Practice

Ogni progetto deve avere OpenAPI spec completa:
```yaml
openapi: 3.0.0
info:
  title: Task Manager API
  version: 1.0.0
paths:
  /tasks:
    get:
      summary: List all tasks
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, completed, all]
      responses:
        '200':
          description: List of tasks
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'
```

### API Versioning Strategy

```
Option A: URL versioning     → /api/v1/tasks, /api/v2/tasks
Option B: Header versioning  → Accept: application/vnd.api+json;version=1
Option C: Query param        → /api/tasks?version=1

Raccomandato per REST: URL versioning (piu esplicito)
```

### API Design Checklist

- [ ] Nomi risorse plurali (`/tasks`, non `/task`)
- [ ] HTTP verbs corretti (GET=read, POST=create, PUT=replace, PATCH=update, DELETE=remove)
- [ ] Status codes appropriati (201 Created, 204 No Content, 404 Not Found, 422 Unprocessable)
- [ ] Pagination per liste (`?page=1&limit=20`)
- [ ] Filtering/Sorting (`?status=pending&sort=-createdAt`)
- [ ] Error response consistente (`{ "error": { "code": "...", "message": "..." } }`)
- [ ] Versioning strategy definita
- [ ] Rate limiting headers (`X-RateLimit-Remaining`)

---

## Interview Prep (Mesi 15-18+)

**Obiettivo:** Passare interview per ruoli remote €90k-130k

### Behavioral Questions (STAR Method)

Prepara 5+ storie con questo formato:
```
Situation: Descrivi il contesto
Task: Qual era il tuo compito/obiettivo
Action: Cosa HAI FATTO tu specificamente
Result: Qual e stato il risultato (numeri se possibile)
```

**Domande comuni:**
1. "Tell me about a challenging technical problem you solved"
2. "Describe a time you disagreed with a teammate"
3. "Tell me about a project you're proud of"
4. "Describe a time you had to learn something quickly"
5. "Tell me about a failure and what you learned"

### Technical Questions Bank

**Domande frequenti senior .NET:**
- Explain dependency injection and its benefits
- What's the difference between IEnumerable and IQueryable?
- How does async/await work under the hood?
- Explain the difference between SQL and NoSQL databases
- What is CQRS and when would you use it?
- Explain the CAP theorem
- How would you handle distributed transactions?
- What's the difference between optimistic and pessimistic locking?

### "Walk Me Through Your Project" Template

```markdown
1. **Context** (30 sec)
   "I built a [type] system that [does what] for [who]"

2. **Architecture** (1 min)
   "It uses [stack]. Here's the high-level design..."
   [Disegna diagramma semplice]

3. **Interesting Challenge** (2 min)
   "The most interesting problem was [X]. I solved it by [Y]"

4. **Results** (30 sec)
   "It handles [X] requests/sec with [Y] latency"

5. **What I'd Do Differently** (30 sec)
   "If I rebuilt it, I'd [improvement]"
```

### Salary Negotiation Basics

```markdown
## Research
- Glassdoor, Levels.fyi, Blind per range
- Considera: base + bonus + equity + benefits

## Quando chiedono "What's your expected salary?"
- "Based on my research, roles like this in [location] range X-Y.
   I'm flexible depending on the total package."
- Mai dire il primo numero se possibile
- Mai dire il tuo stipendio attuale

## Dopo l'offerta
- "Thank you! I'm excited about this opportunity.
   I was hoping for something closer to X. Is there flexibility?"
- Sempre chiedere (gentilmente). Il peggio e "no".
```

### Portfolio Presentation

- [ ] GitHub profile curato (README, pinned repos)
- [ ] Ogni progetto ha README con: What, Why, How, Demo
- [ ] LinkedIn aggiornato (headline: "Senior .NET Engineer | ...")
- [ ] 1-page resume (no more!)
- [ ] Personal website/blog (opzionale ma utile)

---

## Career Boost XP

| Attivita | XP |
|----------|-----|
| System design documentato | +25 |
| Mock interview completata | +50 |
| Behavioral story scritta (STAR) | +15 |
| API spec OpenAPI completa | +30 |
| Code review su OSS project | +40 |
| Tech blog post pubblicato | +75 |
| Conference talk (anche meetup locale) | +150 |

### Achievements

| Badge | Nome | Requisito | XP |
|-------|------|-----------|-----|
| 🎤 | **Interview Ready** | 10 system designs + 5 mock interviews | +200 |
| 📝 | **Technical Writer** | 3 blog posts pubblicati | +150 |
| 🌍 | **Open Source Contributor** | 3 PR merged su progetti OSS | +200 |
| 💼 | **Offer Accepted** | Ricevi offerta €90k+ | +500 |

---

*Ultimo aggiornamento: 2026-03-13*
