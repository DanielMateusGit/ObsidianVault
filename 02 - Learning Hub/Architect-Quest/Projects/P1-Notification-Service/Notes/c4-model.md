---
tags:
  - architect-quest
  - p1
  - week-01
  - documentation
  - c4-model
aliases:
  - C4
  - C4 Diagrams
  - Context Diagram
created: 2026-02-03
updated: 2026-02-03
source: "Sessione Week 1 - 2026-02-03"
---

# C4 Model

> **One-liner:** Un modello per visualizzare l'architettura software a 4 livelli di zoom, come Google Maps per il codice.

## Cos'è

Il C4 Model, creato da **Simon Brown**, è un approccio alla documentazione dell'architettura software che usa **4 livelli di astrazione** (zoom), permettendo di comunicare con audience diverse usando il livello appropriato.

### L'Analogia Google Maps

```
🗺️ Google Maps          →    🏗️ C4 Model

Vista satellitare       →    Level 1: CONTEXT
(Europa)                     (Sistema + utenti + esterni)

Vista città             →    Level 2: CONTAINER
(Roma)                       (Applicazioni, DB, servizi)

Vista quartiere         →    Level 3: COMPONENT
(Trastevere)                 (Componenti interni)

Vista strada            →    Level 4: CODE
(Via del Moro)               (Classi, interfacce)
```

## I 4 Livelli

### Level 1: Context Diagram
**Per chi:** Tutti (anche non-tecnici, CEO, stakeholder)
**Cosa mostra:**
- Il TUO sistema al centro
- Chi lo usa (Person)
- Con quali sistemi esterni comunica

**Frequenza d'uso:** 95% dei progetti

```
┌─────────────┐     ┌─────────────────┐     ┌─────────────┐
│   User      │────▶│  YOUR SYSTEM    │────▶│  External   │
│  [Person]   │     │  [Software      │     │   System    │
└─────────────┘     │   System]       │     │  [Ext Sys]  │
                    └─────────────────┘     └─────────────┘
```

### Level 2: Container Diagram
**Per chi:** Dev team, architects
**Cosa mostra:**
- Le "scatole" deployabili (API, Web App, DB, Message Queue)
- Come comunicano tra loro
- Tecnologie usate

**Frequenza d'uso:** 80% dei progetti

### Level 3: Component Diagram
**Per chi:** Dev che lavorano su quel container specifico
**Cosa mostra:**
- I componenti interni di UN container
- Pattern usati (Repository, Service, Controller)

**Frequenza d'uso:** 30% dei progetti (solo sistemi complessi)

### Level 4: Code Diagram
**Per chi:** Dev specifici (raramente utile)
**Cosa mostra:** Classi, interfacce, relazioni UML

**Frequenza d'uso:** 5% dei progetti - L'IDE fa meglio!

## Quando Usare C4

### ✅ USA C4 quando:
- Inizi un nuovo progetto
- Fai onboarding di nuovi dev
- Comunichi con stakeholder non-tecnici
- Vuoi ADR visivi
- Code review architetturali

### ❌ NON usare C4 quando:
- Hai bisogno di UML dettagliato (sequence, state)
- Documenti algoritmi specifici
- Il progetto è un semplice script
- Fai design UI/UX

## La Regola d'Oro

> **Ogni diagramma deve essere comprensibile in 5 secondi.**
> Se devi spiegare il diagramma, il diagramma è sbagliato.

## Tool per C4

### Tool Principali

| Tool | Tipo | Pro | Contro |
|------|------|-----|--------|
| **Structurizr** | DSL as Code | Gold standard, di Simon Brown | Learning curve |
| **PlantUML + C4** | Code → Diagram | Gratuito, CI/CD friendly | Sintassi verbose |
| **Mermaid** | Code → Diagram | Nativo GitHub/GitLab | C4 support basico |
| **Draw.io** | Drag & drop | Gratuito, flessibile | Manuale, no Git |
| **Lucidchart** | Drag & drop | Collaborativo | Pagamento |

### AI + C4: Stato Attuale (2026)

**Non esiste ancora un tool "AI-native" dedicato a C4.**

Però si può usare AI per generare il codice del diagramma:

```
Tu: "Genera un C4 Context diagram in PlantUML per un notification service..."
Claude/GPT: [genera codice PlantUML]
Tu: [copi in PlantUML editor → diagram fatto]
```

**Approcci:**
1. **AI genera PlantUML** → renderizzi su plantuml.com
2. **AI genera Structurizr DSL** → usi Structurizr
3. **AI genera Mermaid** → nativo in GitHub/Claude

### Raccomandazione

Per progetti enterprise/portfolio: **PlantUML + C4-PlantUML** perché:
- Gratuito e open source
- Versionabile in Git (diagramma = codice)
- CI/CD ready
- AI-friendly

## Esempio Pratico

### Context Diagram - Notification Service

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(clientApps, "Client Applications", "Apps that send notifications")
System(notificationService, "Notification Service", "Multi-channel notifications")
System_Ext(sendgrid, "SendGrid", "Email delivery")
System_Ext(twilio, "Twilio", "SMS delivery")

Rel(clientApps, notificationService, "Sends requests", "REST")
Rel(notificationService, sendgrid, "Sends emails", "HTTPS")
Rel(notificationService, twilio, "Sends SMS", "HTTPS")

LAYOUT_WITH_LEGEND()
@enduml
```

## Collegamenti

- [[clean-architecture|Clean Architecture]] - C4 documenta architetture Clean
- [[adr|ADR]] - C4 + ADR = documentazione completa

## Quiz

**Q1:** Hai 3 minuti per spiegare l'architettura al CEO. Quale livello C4 usi?

- A) C4 - Code
- B) C2 - Container
- C) C1 - Context
- D) C3 - Component

<details>
<summary>Risposta</summary>

**C) C1 - Context**

Il CEO non è tecnico e ha poco tempo. Il Context Diagram mostra il sistema, chi lo usa, e con cosa comunica - tutto comprensibile in 5 secondi.

</details>

---

**Q2:** Nel C1 Context Diagram, dove posizioni il TUO sistema?

- A) In un angolo, piccolo
- B) Al centro, evidenziato
- C) Non presente (mostra solo esterni)
- D) Diviso nei suoi componenti

<details>
<summary>Risposta</summary>

**B) Al centro, evidenziato**

Il Context Diagram ha il TUO sistema come protagonista al centro. Gli utenti e sistemi esterni sono attorno.

</details>

---

**Q3:** Qual è il livello C4 che si usa MENO nella pratica?

- A) Context
- B) Container
- C) Component
- D) Code

<details>
<summary>Risposta</summary>

**D) Code**

Il livello Code (~5% dei progetti) è quasi mai utile perché:
1. Il codice cambia troppo spesso
2. L'IDE mostra già classi e relazioni
3. Mantenere sincronizzato è impossibile

</details>

---

**Q4:** Vuoi che i diagrammi siano versionati in Git insieme al codice. Quale tool scegli?

- A) Lucidchart
- B) Draw.io
- C) PlantUML / Structurizr
- D) PowerPoint

<details>
<summary>Risposta</summary>

**C) PlantUML / Structurizr**

Entrambi sono "diagrams as code" - il diagramma È un file di testo che puoi committare, diffanziare, e revieware come codice.

</details>

---

*Nota creata durante Week 1 - P1 Notification Service*
