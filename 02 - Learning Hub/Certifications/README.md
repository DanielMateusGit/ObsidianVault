---
tags: [certifications, index]
created: 2026-04-28
updated: 2026-04-28
---

# 🏆 Certifications

> Hub centralizzato di tutte le certificazioni: tracker progresso, esercizi, retro.
> Le **note atomiche** delle lezioni vivono in `Knowledge/[categoria]/` per riusabilità cross-cert.

---

## 📋 Pipeline

| Cert | Provider | Status | Score | Cluster Target | Folder |
|------|----------|--------|-------|----------------|--------|
| Claude Code in Action | Anthropic | ✅ Completata (2026-03-13) | 8/8 Perfect | AI #4 (AI-Augmented SWE) | [`claude-code-in-action/`](claude-code-in-action/) |
| Claude Code 101 | Anthropic | 🚧 In corso | — | AI #4 | [`claude-code-101/`](claude-code-101/) |
| AZ-204 Azure Developer Associate | Microsoft | 📅 Tier 1 planned (Year 1) | — | SE #1, SE #5, AI deployment | [`az-204/`](az-204/) |
| Terraform Associate (003) | HashiCorp | 📅 Tier 1 planned (Year 1) | — | SE #3, SE #5, transversal | [`terraform-associate/`](terraform-associate/) |

---

## 🗂️ Struttura per Cert

Ogni cert ha la propria sotto-cartella con:

```
[cert-slug]/
├── tracker.md          # progress overview, lezioni, XP, achievement
├── lessons/            # appunti grezzi durante le lezioni (opzionale)
├── exercises/          # esercizi pratici svolti (opzionale)
├── final-exam.md       # risultato test finale
└── retrospective.md    # cosa ho imparato + cosa userò + 3 takeaway (post-completion)
```

**Regola d'oro:** le **note atomiche riusabili** vanno in `Knowledge/ai/claude/` (o categoria appropriata) — taggate `from/[cert-slug]` per tracciare la sorgente. Una nota su "MCP Server" vale per più cert e per i progetti.

---

## 🎮 Gamification

> Sistema XP cert: vedi `claude/context/gamification.md`. Schema XP per lezione/test/achievement è documentato nel `tracker.md` di ogni cert.

**Regola feedback (memoria persistente):** le certificazioni sono gamificate con **spaced repetition prioritaria** — almeno 1 quiz al giorno dal pool CLCODE/CL101 etc. Vedi `claude/context/quiz-tracker.md`.

---

## 🧠 Quiz Naming Convention

Ogni cert ha un prefisso quiz dedicato in `claude/context/quiz-tracker.md`:

| Cert | Prefisso |
|------|----------|
| Claude Code in Action | `CLCODE-NN` |
| Claude Code 101 | `CL101-NN` |
| AZ-204 Azure Developer Associate | `AZ204-NN` |
| Terraform Associate | `TFA-NN` |
| AZ-400 DevOps Engineer Expert (Tier 2) | `AZ400-NN` |
| CKAD Kubernetes Application Developer (Tier 2) | `CKAD-NN` |
| AWS Developer Associate (Tier 3) | `AWS-NN` |
| GCP Professional Cloud Developer (Tier 3) | `GCP-NN` |

I quiz entrano nel sistema Leitner globale (Box 1→5) come gli altri.

---

## 🆕 Aggiungere una nuova cert

1. Crea sotto-cartella `Certifications/[cert-slug]/` con `tracker.md` (copia template da una cert esistente)
2. Aggiungi riga nella tabella **Pipeline** sopra
3. Definisci prefisso quiz e aggiungilo alla tabella **Quiz Naming Convention**
4. Aggiungi la cert in `claude/current-state.md` > Progress > Certificazioni (se completata) o "Certificazioni in corso"
5. Se rilevante per cluster CV: aggiorna `claude/career-strategy.md` > Cluster Positioning Matrix

---

*Ultimo aggiornamento: 2026-05-07 (Tier 1 cert pipeline definita: AZ-204 + Terraform Associate skeletons creati; quiz prefixes pre-allocati per Tier 2/3)*

*Versione precedente: 2026-04-28 (creata struttura Certifications/ + migrazione Claude Code in Action + scaffold Claude Code 101)*
