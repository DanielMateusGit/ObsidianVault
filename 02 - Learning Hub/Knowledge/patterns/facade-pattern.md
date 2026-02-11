---
tags:
  - patterns
  - structural-pattern
  - from/book
  - status/learned
aliases:
  - Facade
  - Facciata
created: 2026-02-06
updated: 2026-02-06
source: "Dive into Design Patterns - Alexander Shvets"
---

# Facade Pattern

> **One-liner:** Un entry point semplificato che nasconde la complessità di un sistema o libreria, esponendo solo le funzionalità necessarie.

## Cos'è

Il Facade è un **pattern strutturale** che fornisce un'interfaccia semplificata verso un sistema complesso, una libreria, o un insieme di classi strettamente accoppiate.

**Responsabilità della Facade:**
- Fare da **entry point** per il sistema complesso
- **Inizializzare e gestire** il sottosistema
- **Nascondere la complessità** implementativa
- Esporre solo le funzionalità necessarie al client

## Analogia: Il Call Center

Un call center è la Facade di un'azienda:
- Il cliente chiama **un solo numero** (la Facade)
- L'operatore ha la responsabilità di **reperire informazioni** dal sistema complesso (HR, Team Sviluppo, Team Commerciale, etc.)
- Il cliente ottiene una **risposta semplice** senza conoscere la struttura interna dell'azienda

## Quando usarlo

**Domanda chiave:** *"Ho bisogno di un'interfaccia più semplice per un sistema complesso che è difficile da gestire?"*

Usa Facade quando:
1. Vuoi un **entry point semplificato** per un sistema complesso
2. Vuoi **nascondere i dettagli implementativi** di una libreria
3. Vuoi **stratificare** un sistema complesso già esistente (es. AudioConverter, VideoConverter)
4. Hai bisogno di **riassumere tanti passaggi difficili** in una sola chiamata

## Quando NON usarlo

**Attenzione alla confusione con Factory!**

Se la Facade si occupa **solamente di inizializzare** il sistema complesso, ma NON di "riassumere tanti passaggi in una funzione chiamabile" → probabilmente stai sbagliando pattern.

| Facade | Factory |
|--------|---------|
| Semplifica l'**uso** di un sistema | Semplifica la **creazione** di oggetti |
| Nasconde complessità operativa | Nasconde complessità di costruzione |
| Entry point per operazioni | Entry point per istanziazione |

## Esempio Pratico

```csharp
// Sistema complesso di conversione video
public class VideoFile { /* ... */ }
public class CodecFactory { /* ... */ }
public class BitrateReader { /* ... */ }
public class AudioMixer { /* ... */ }

// FACADE: semplifica tutto in una chiamata
public class VideoConverterFacade
{
    public void ConvertVideo(string filename, string format)
    {
        // Inizializza e gestisce il sistema complesso
        var file = new VideoFile(filename);
        var codec = CodecFactory.Extract(file);
        var bitrate = BitrateReader.Read(filename, codec);
        var audio = AudioMixer.Fix(/* ... */);

        // Il client non vede nulla di tutto questo
        // Chiama solo: facade.ConvertVideo("video.mp4", "avi")
    }
}
```

## Pro e Contro

| Pro | Contro |
|-----|--------|
| Isola il codice dalla complessità | Può diventare una **God Object** |
| Interfaccia semplice per il client | Può nascondere troppo (debugging difficile) |
| Facilita i test (mock della facade) | |

**Se la Facade diventa troppo grande:** spezzala in più Facade specializzate (es. `AudioConverter`, `VideoConverter`, `ImageConverter`).

## Collegamenti

- [[solid/single-responsibility-principle|SRP]] - Facade permette di raggruppare per dominio mantenendo SRP nei servizi interni
- [[architecture/information-hiding|Information Hiding]] - La Facade nasconde i dettagli implementativi
- Factory Pattern (da creare) - Pattern spesso confuso con Facade

---

## Quiz

### Q1: Facade vs Factory

Stai lavorando con una libreria di pagamenti complessa (Stripe). Devi:
- Inizializzare il client con API key
- Creare un PaymentIntent
- Gestire la conferma
- Loggare il risultato

Creeresti una Facade o un Factory? Perché?

**Mia risposta:** Facade, perché non sto solo inizializzando la libreria per il pagamento, ma sto effettivamente pagando ed inviando conferma. Il metodo si chiamerebbe `Pay()` - gestisce tante classi della libreria Stripe e fa cose. Non ottengo un StripePaymentObject, sto proprio pagando.

✅ **Corretto** - La chiave è "sto FACENDO qualcosa, non sto CREANDO un oggetto".

---

### Q2: God Object Alert

La tua `PaymentFacade` ora gestisce: pagamenti, rimborsi, subscription, invoices, webhook, fraud detection. Cosa faresti?

**Mia risposta:** Sta facendo troppe cose, è un God Object. Obbligatorio spezzare perché infrange SRP - sta "servendo più attori": fraud detection serve al sistema legale, webhook al team dev, pagamenti/rimborsi alla contabilità.

✅ **Corretto** - Ottimo collegamento con SRP e gli attori! Soluzione: `PaymentFacade`, `SubscriptionFacade`, `FraudFacade`.

---

### Q3: Scenario pratico

Hai un sistema legacy con 15 classi interconnesse per generare report PDF. I developer si lamentano che è impossibile da usare. Quale pattern applicheresti e come?

**Mia risposta:** Dipende da cosa rende "impossibile da usare": se sono tecnologie incompatibili con il nostro stack → Adapter. Se invece è proprio difficile venirne a capo → Facade. Implementerei un metodo `ReportPdf()` nascondendo la complessità dietro la Facade.

✅ **Corretto + Bonus** - Distinzione precisa tra Adapter (incompatibilità) e Facade (complessità d'uso).

---

*Nota creata durante Sedimentazione W01*
