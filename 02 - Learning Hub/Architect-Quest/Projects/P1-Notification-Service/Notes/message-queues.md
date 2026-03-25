---
tags:
  - p1
  - architecture
  - messaging
  - event-driven
  - from/week-05
  - status/learning
aliases:
  - Message Queue
  - Event-Driven Architecture
  - RabbitMQ
  - Azure Service Bus
created: 2026-03-25
source: "Sessione Week 5 - Message Queue"
---

# Message Queue — Architettura Event-Driven

> **One-liner:** Una Message Queue e un intermediario asincrono che disaccoppia chi produce messaggi da chi li processa, garantendo consegna affidabile, gestione del carico e retry automatici.

---

## Il Problema: Perche serve una Message Queue?

Nel nostro Notification Service, il `ScheduleNotificationHandler` salva la notifica nel DB con status `Pending`. Ma chi la invia davvero? Chi prende quella notifica e la spedisce via email/SMS/push?

### Approccio Sincrono (quello che NON vogliamo)

```
API Request → Handler → Salva in DB → Invia Email → Rispondi al client
```

**Problemi concreti:**
1. **Latenza** — Se l'invio email impiega 5 secondi, il client aspetta 5 secondi
2. **Fragilita** — Se il server SMTP e giu, la richiesta fallisce e la notifica e persa
3. **Congestione** — Se arrivano 10.000 richieste insieme, il sistema crolla tentando di inviare tutto contemporaneamente
4. **Accoppiamento** — L'API deve conoscere i dettagli dell'invio (SMTP, provider SMS, ecc.)

### Approccio Asincrono con Message Queue (quello che vogliamo)

```
API Request → Handler → Salva in DB → Pubblica messaggio in coda → Rispondi subito

[Separatamente, in background]
Worker → Legge dalla coda → Invia Email → Conferma
```

Il client riceve risposta immediata ("la tua notifica e stata schedulata"), il lavoro pesante avviene dopo, in background.

---

## I 3 Attori: DB, Queue, Worker

### Il Database (La Fonte di Verita)

Il DB e il **registro ufficiale** di tutto cio che esiste nel sistema:
- **Tiene traccia dello stato** di ogni notifica (Pending, Sent, Failed)
- **Contiene tutti i dettagli** (destinatario, template, body, canale, retry count)
- E **permanente** — i dati restano anche se tutto il resto crasha

### La Queue (La Lista di Lavoro)

La Queue e un **servizio separato** che gira indipendentemente dall'applicazione (RabbitMQ in Docker, o Azure Service Bus nel cloud).

**Cosa fa:**
- Riceve messaggi leggeri ("c'e lavoro da fare")
- Li conserva finche qualcuno non li processa
- Gestisce l'ordine (FIFO — First In, First Out)
- Garantisce che nessun messaggio si perda

**Cosa contiene un messaggio?** Solo le informazioni minime — un puntatore al lavoro da fare:

```json
{
  "notificationId": "abc-123",
  "event": "NotificationScheduled",
  "timestamp": "2026-03-25T10:30:00Z"
}
```

**Perche solo l'ID e non tutti i dettagli?**
1. La queue e **agnostica** al dominio — trasporta compiti, non conosce le notifiche
2. Se i dettagli cambiano nel DB dopo la pubblicazione, il worker legge sempre la **versione aggiornata**
3. Messaggi leggeri = queue piu veloce e meno memoria

> **Analogia:** La queue e come la cassetta delle lettere dell'ufficio postale. Tu (produttore) imbuchi la lettera e te ne vai. L'ufficio (queue) la conserva. Il postino (worker) la ritira quando puo. Se il postino e malato, la lettera resta al sicuro.

### Il Worker (Chi Fa il Lavoro)

Il Worker e un **programma che gira in background**, separato dall'API. In .NET e un `BackgroundService`.

**Analogia:** L'API e il **cameriere** (prende l'ordine). Il Worker e il **cuoco** (prepara il piatto in cucina, senza che il cliente lo veda).

```
┌─────────────────────┐     ┌──────────────────────┐
│    API (Cameriere)   │     │   Worker (Cuoco)      │
│                      │     │                       │
│  Riceve richiesta    │     │  Gira in background   │
│  Salva nel DB        │     │  Ascolta la queue     │
│  Pubblica in queue   │     │  Quando arriva msg:   │
│  Risponde al client  │     │    → legge dal DB     │
│                      │     │    → invia email/SMS   │
│  NON invia nulla     │     │    → aggiorna status   │
└─────────────────────┘     └──────────────────────┘
       ↓                              ↑
       └──── QUEUE (Collegamento) ────┘
```

Il Worker:
- **Non riceve richieste HTTP** — non e un'API
- **Ascolta la queue** in continuazione (loop infinito)
- **Processa un messaggio alla volta** (o N in parallelo, configurabile)
- Se crasha, viene riavviato e riprende dalla queue

**Chi fa cosa — Riepilogo:**

```
┌─────────────┐    ┌──────────────┐    ┌───────────────┐
│     DB       │    │    QUEUE     │    │    WORKER     │
│              │    │              │    │               │
│ E la VERITA  │    │ E il POSTINO │    │ E il CUOCO    │
│              │    │              │    │               │
│ Salva lo     │    │ Trasporta    │    │ Fa il lavoro  │
│ stato della  │    │ messaggi     │    │ vero: invia   │
│ notifica     │    │ leggeri      │    │ email/SMS     │
│ (Pending,    │    │ (solo ID +   │    │               │
│  Sent,       │    │  evento)     │    │ Legge dal DB  │
│  Failed)     │    │              │    │ il dettaglio  │
│              │    │ NON contiene │    │               │
│ Il DB e      │    │ la notifica  │    │ Conferma o    │
│ permanente   │    │ intera!      │    │ rifiuta (ACK/ │
│              │    │              │    │ NACK)         │
└─────────────┘    └──────────────┘    └───────────────┘
```

---

## Il Ciclo Completo: Flusso Normale

### Fase A: L'utente schedula una notifica

```
  Client                API Handler              DB                 Queue
    │                      │                     │                    │
    │── POST /notify ─────→│                     │                    │
    │                      │── Save(Pending) ───→│                    │
    │                      │                     │ ✅ Notifica        │
    │                      │                     │    salvata         │
    │                      │── Publish(msg) ─────│───────────────────→│
    │                      │                     │                    │ ✅ Messaggio
    │                      │                     │                    │    in coda
    │←── 202 Accepted ─────│                     │                    │
    │                      │                     │                    │
  FINE. Il client ha la risposta. Non aspetta l'invio.
```

### Fase B: Il Worker processa (in background)

```
  Queue                Worker                  DB              Email Server
    │                    │                     │                    │
    │── Messaggio ──────→│                     │                    │
    │   (invisibile*)    │                     │                    │
    │                    │── GetById(abc-123)─→│                    │
    │                    │←── Notification ────│                    │
    │                    │   (status: Pending) │                    │
    │                    │                     │                    │
    │                    │── SendEmail ────────│───────────────────→│
    │                    │                     │                    │── ✅ Inviata
    │                    │                     │                    │
    │                    │── Update(Sent) ────→│                    │
    │                    │                     │ ✅ Status: Sent    │
    │                    │                     │                    │
    │←── ACK (conferma) ─│                     │                    │
    │                    │                     │                    │
    │ ✅ Messaggio       │                     │                    │
    │    rimosso         │                     │                    │
```

**(*) Invisibile:** Quando il Worker legge il messaggio, la queue NON lo cancella. Lo rende **invisibile** agli altri worker (cosi nessun altro lo prende). Solo dopo l'ACK viene rimosso.

---

## ACK e NACK: Il Protocollo di Conferma

Come nelle reti (TCP), la queue usa un sistema di conferma:

| Segnale | Significato | Cosa succede al messaggio |
|---------|-------------|---------------------------|
| **ACK** (Acknowledge) | "Ho finito con successo" | Rimosso dalla queue definitivamente |
| **NACK** (Not Acknowledge) | "Non ce l'ho fatta" | Torna in coda per retry |
| **Nessun segnale** (timeout) | Worker crashato | Dopo timeout, torna visibile in coda |

**Regola:** Il messaggio resta nella queue finche non riceve un ACK esplicito. Questo e il meccanismo che garantisce **zero perdite**.

---

## Scenari di Fallimento e Retry

### Scenario 1: Email server giu

```
  Queue              Worker                    DB              Email Server
    │── Messaggio ──→│                         │                    │
    │                │── GetById ─────────────→│                    │
    │                │←── Notification ────────│                    │
    │                │── SendEmail ────────────│───────────────────→│
    │                │                         │                    │── ❌ TIMEOUT
    │                │                         │                    │
    │                │── Update(Failed) ──────→│                    │
    │                │                         │ Status: Failed     │
    │                │                         │ RetryCount: 1      │
    │←── NACK ───────│  (Non ce l'ho fatta)    │                    │
    │                │                         │                    │
    │ Il messaggio   │                         │                    │
    │ TORNA IN CODA  │                         │                    │
    │ (retry dopo    │                         │                    │
    │  30 secondi)   │                         │                    │
```

Il Worker sa che non ce l'ha fatta → manda NACK → la queue ripropone il messaggio dopo un intervallo. Il DB tiene traccia del numero di retry.

### Scenario 2: Worker crasha

```
  Queue              Worker                    DB
    │── Messaggio ──→│                         │
    │ (invisibile)   │── GetById ─────────────→│
    │                │←── Notification ────────│
    │                │                         │
    │                │── 💥 CRASH              │
    │                │                         │
    │  ...timeout... │                         │
    │  (es. 5 min)   │                         │
    │                │                         │
    │ Nessun ACK     │                         │
    │ ricevuto!      │                         │
    │                │                         │
    │ Il messaggio   │                         │
    │ TORNA VISIBILE │                         │
    │ in coda        │         Worker 2 (o restart)
    │── Messaggio ──→│────────────→│           │
    │                              │           │
    │               Riprocessa da capo         │
```

Nessuno manda ACK → dopo il timeout, la queue rende il messaggio nuovamente visibile → un altro worker (o lo stesso dopo restart) lo riprende.

### Scenario 3: Troppi retry → Dead Letter Queue (DLQ)

```
  Queue                                    Dead Letter Queue
    │                                          │
    │ Retry 1: ❌ fallito                      │
    │ Retry 2: ❌ fallito                      │
    │ Retry 3: ❌ fallito                      │
    │                                          │
    │── Messaggio spostato ───────────────────→│
    │   (dopo N retry)                         │ ⚠️ Qui resta per
    │                                          │    analisi manuale
    │ La queue principale                      │    (logging, alert)
    │ e libera per altri msg                   │
```

La **Dead Letter Queue (DLQ)** e una coda speciale dove finiscono i messaggi "impossibili" — quelli che dopo N tentativi non si riesce a processare. Servono per debugging: un operatore le analizza e capisce il problema (email invalida? servizio giu da ore? bug nel worker?). Approfondiremo la DLQ nella Week 8.

---

## At-Least-Once Delivery e Idempotenza

### Il Problema

La queue garantisce **at-least-once delivery**: ogni messaggio viene consegnato **almeno una volta**. Ma potrebbe essere consegnato **piu di una volta** — ad esempio nello Scenario 2: il worker ha gia inviato l'email, crasha prima dell'ACK, il messaggio viene riconsegnato.

Risultato senza protezione: **l'email viene inviata due volte**.

### La Soluzione: Idempotenza

Il worker deve essere **idempotente** — processare lo stesso messaggio due volte non deve creare problemi.

Come? Il DB e la fonte di verita. Prima di agire, il worker chiede "e gia stato fatto?":

```csharp
var notification = await _repository.GetByIdAsync(message.NotificationId);

// GUARD: se gia inviata, non fare nulla
if (notification.Status == NotificationStatus.Sent)
{
    await acknowledgeMessage(); // ACK e via
    return;
}

// Altrimenti processa normalmente
await _emailSender.SendAsync(notification);
notification.MarkAsSent();
await _unitOfWork.SaveChangesAsync();
await acknowledgeMessage();
```

**Perche controlliamo `Status == Sent` e non `== Pending`?**
Perche `Sent` e l'unico stato che ci dice "il lavoro e gia completato con successo". Un messaggio in `Pending` o `Failed` deve ancora essere processato (o riprocessato).

---

## Azure Service Bus vs RabbitMQ

| | Azure Service Bus | RabbitMQ |
|---|---|---|
| **Tipo** | Cloud managed (PaaS) | Self-hosted (o managed) |
| **Setup** | Zero infra, pay-per-use | Container Docker locale |
| **Quando** | Produzione Azure, zero ops | Dev locale, controllo totale |
| **Costo** | Pay-per-use (~€0.05/milione msg) | Gratis (self-hosted) |
| **DLQ** | Built-in, automatica | Configurabile manualmente |
| **Feature extra** | Sessions, Scheduling, Topics | Exchanges, routing flessibile |
| **Scaling** | Automatico | Manuale (cluster) |

**La nostra strategia:** creiamo un'interfaccia `IMessagePublisher` nell'Application Layer, con due implementazioni in Infrastructure:
- `RabbitMqMessagePublisher` → per dev/test (Docker locale)
- `AzureServiceBusMessagePublisher` → per produzione

Questo e **Ports & Adapters** applicato alla message queue. Il codice dell'Application non sa (e non deve sapere) quale queue sta usando.

---

## Nel Nostro Notification Service

```
ScheduleNotificationCommand
  → Handler salva Notification (Pending) nel DB
  → Pubblica "NotificationScheduled" nella queue
        ↓
    { notificationId: "abc-123", event: "NotificationScheduled" }
        ↓
NotificationWorker (BackgroundService)
  → Riceve messaggio dalla queue
  → Carica la Notification dal DB (con tutti i dettagli)
  → Controlla status (idempotenza)
  → Chiama il canale giusto (Email/SMS/Push)
  → Aggiorna status nel DB (Sent/Failed)
  → ACK o NACK alla queue
```

---

## Concetti Chiave da Ricordare

| Concetto | Significato |
|----------|-------------|
| **FIFO** | First In, First Out — i messaggi escono nell'ordine in cui entrano |
| **ACK/NACK** | Conferma/rifiuto del messaggio — come in TCP |
| **At-least-once** | Il messaggio arriva almeno 1 volta, forse piu |
| **Idempotenza** | Processare 2 volte = stesso risultato di 1 volta |
| **Dead Letter Queue** | Coda per messaggi impossibili dopo N retry |
| **Invisibility timeout** | Tempo in cui il messaggio e nascosto dopo la lettura |
| **BackgroundService** | Classe .NET per worker in background |

---

## Quiz

### Q1: Perche asincrono? (MQ-01)
Il `ScheduleNotificationHandler` salva la notifica nel DB. Se aggiungessi l'invio email direttamente nello stesso handler (sincrono), quali sono almeno 3 problemi concreti?

**Mia risposta:**

---

### Q2: Cosa contiene il messaggio? (MQ-02)
Il messaggio nella queue contiene solo `notificationId` e `event`. Perche non mettiamo tutti i dettagli della notifica (destinatario, template, body) direttamente nel messaggio?

**Mia risposta:**

---

### Q3: ACK vs NACK (MQ-03)
Qual e la differenza tra ACK e NACK? Per ciascuno, descrivi cosa succede al messaggio nella queue dopo che il worker lo invia.

**Mia risposta:**

---

### Q4: Worker crash (MQ-04)
Il worker legge un messaggio dalla queue, inizia a processarlo, e poi crasha (out of memory). Cosa succede al messaggio? Chi garantisce che non si perda?

**Mia risposta:**

---

### Q5: Idempotenza (MQ-05)
Il worker ha inviato l'email con successo ma crasha prima di mandare l'ACK alla queue. Il messaggio viene riconsegnato. Come impedisci che l'email venga inviata due volte?

**Mia risposta:**

---

### Q6: Perche Sent e non Pending? (MQ-06)
Nel check di idempotenza, controlliamo `notification.Status == Sent`. Perche NON controlliamo `== Pending`? Cosa succederebbe se usassimo Pending come guardia?

**Mia risposta:**

---

### Q7: DB vs Queue — Chi fa cosa? (MQ-07)
Completa la frase: "Il DB e ______, la Queue e ______". Spiega il ruolo di ciascuno nel sistema e perche sono separati.

**Mia risposta:**

---

### Q8: Dead Letter Queue (MQ-08)
Un messaggio fallisce 3 volte consecutive. Cosa succede? Dove finisce? A cosa serve questo meccanismo?

**Mia risposta:**

---

### Q9: Ports & Adapters nella Queue (MQ-09)
Perche creiamo un'interfaccia `IMessagePublisher` nell'Application Layer invece di usare direttamente il client RabbitMQ? Fai un esempio pratico di quando questo ci salva.

**Mia risposta:**

---

### Q10: Invisibility Timeout (MQ-10)
Quando il worker legge un messaggio, la queue lo rende "invisibile". Cosa significa? Cosa succede se il timeout scade senza ACK?

**Mia risposta:**

---

### Q11: At-Least-Once vs Exactly-Once (MQ-11)
La nostra queue garantisce "at-least-once delivery". Perche non "exactly-once"? Qual e il trade-off e come lo gestiamo?

**Mia risposta:**

---

### Q12: Ordine di Esecuzione (MQ-12)
Il worker riceve il messaggio. In quale ordine esegue queste operazioni e perche?
- A) Invia email
- B) Legge notifica dal DB
- C) Aggiorna status a Sent
- D) Manda ACK alla queue
- E) Controlla se status == Sent

**Mia risposta:**

---

### Q13: Scenario Completo (MQ-13)
Descrivi il flusso completo dal momento in cui il client chiama `POST /notify` fino a quando l'email arriva nella inbox del destinatario. Includi tutti e 3 gli attori (DB, Queue, Worker).

**Mia risposta:**

---

## Risorse

- [Azure Service Bus Documentation](https://learn.microsoft.com/en-us/azure/service-bus-messaging/) - Documentazione ufficiale
- [RabbitMQ Tutorials](https://www.rabbitmq.com/tutorials) - Getting started con RabbitMQ
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) - Pattern di messaging (Gregor Hohpe)
- [Cloud Design Patterns - Queue-Based Load Leveling](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling) - Pattern Microsoft per gestione carico con queue
