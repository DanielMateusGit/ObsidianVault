---
tags: [certifications, terraform, hashicorp, iac, planned]
created: 2026-05-07
updated: 2026-05-07
status: not-started
provider: HashiCorp
exam_code: "TF-Associate-003"
exam_name: "HashiCorp Certified: Terraform Associate"
cluster_target: "SE #3 Infrastructure/SRE, SE #5 Modern Full-Stack, all clusters (IaC = transversal)"
priority: tier-1
estimated_prep: "3-4 weeks"
exam_cost_usd: 70
---

# 🏆 Terraform Associate (003) — HashiCorp Certified

> **Status:** not-started · scheduled in **Tier 1 cert pipeline** (Year 1, dopo AZ-204 o in parallelo)
>
> **Why this cert:** IaC è transversale a TUTTI i cluster cloud. Cert relativamente economica ($70) e veloce (~3-4 settimane prep). Riconosciuta cross-cloud (AWS, Azure, GCP). Ottimo complemento ad AZ-204 (Microsoft preferisce Bicep ma Terraform è multi-cloud standard).

---

## 📋 Pipeline

| Step | Status | Note |
|------|--------|------|
| Acquisto voucher esame | ⬜ | $70.50 USD |
| Microsoft Learn / HashiCorp Learn paths completati | ⬜ | HashiCorp Learn ha tutorial gratuiti |
| Hands-on lab su 2+ cloud (AWS + Azure) | ⬜ | Sandbox locale + free tier cloud |
| Practice tests (>=85%) | ⬜ | Bryan Krausen (Udemy) — gold standard |
| Esame finale | ⬜ | Target: **>=85%** (passing 70%) |

---

## 🎯 Exam Objectives

Ufficiali da [hashicorp.com/certification/terraform-associate](https://www.hashicorp.com/certification/terraform-associate):

| Area | Topics chiave |
|------|---------------|
| Understand IaC concepts | Why IaC, Terraform vs others (Pulumi, ARM, Bicep, CFN) |
| Understand Terraform's purpose | Stato, providers, workflow init/plan/apply |
| Understand Terraform basics | Variables, outputs, expressions, functions |
| Use the Terraform CLI | init, plan, apply, destroy, fmt, validate, workspace |
| Interact with Terraform modules | Module sources, versions, inputs/outputs |
| Use the core workflow | write → plan → apply, idempotency |
| Implement and maintain state | Local vs remote state, state locking, backends |
| Read, generate, and modify configuration | HCL syntax, resources, data sources |

---

## 📚 Risorse consigliate

### Tier 1 (must-have)
- **HashiCorp Learn — Terraform tutorials**: gratis, ufficiali ([link](https://developer.hashicorp.com/terraform/tutorials))
- **Bryan Krausen — HashiCorp Certified: Terraform Associate** (Udemy): IL corso di riferimento per la cert
- **Terraform: Up & Running** (Yevgeniy Brikman, O'Reilly): libro completo

### Tier 2 (deep-dive)
- "Infrastructure as Code" (Kief Morris, O'Reilly) — IaC theory broader
- Pratica: replicare infra di un progetto Senior Engineer (es. P1 Task Manager) con Terraform invece di setup manuale

---

## 🧠 Quiz Tracker Integration

**Quiz prefix:** `TFA-NN`

I quiz entrano nel sistema Leitner globale in `claude/context/quiz-tracker.md` con prefisso `TFA-`.

---

## 🎮 XP per completion

| Milestone | XP |
|-----------|-----|
| HashiCorp Learn tutorial completato | +30 each |
| Hands-on Terraform deploy completo (1 progetto) | +100 |
| Practice test >=85% | +75 |
| **Esame superato** | +300 |
| **Esame >=90%** | +400 (Lode bonus) |

---

## 📓 Note Atomiche correlate

> Tag: `from/terraform-associate`. Le note IaC sono utili anche per AZ-400 e CKAD (overlap).

- *(none yet — to be created during prep)*

---

## 🔗 Linked Knowledge

Knowledge notes esistenti rilevanti:
- [[Knowledge/architecture/clean-architecture-principles|Clean Architecture]] — Terraform come "Infrastructure layer" del deploy

Knowledge notes da creare durante prep:
- `Knowledge/devops/iac-fundamentals.md`
- `Knowledge/devops/terraform-state-management.md`
- `Knowledge/devops/terraform-modules.md`

---

*Created: 2026-05-07 (skeleton pre-creato nell'/end della sessione, partenza prep TBD — possibilmente in parallelo o subito dopo AZ-204)*
