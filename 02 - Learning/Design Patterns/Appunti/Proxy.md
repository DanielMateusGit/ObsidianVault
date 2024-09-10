
# Proxy
## Cosa fa?

Aggiunge un livello di astrazione tra CLIENT ed un Servizio Server

Praticamente è un wrapper di un servizio che il CLIENT vuole utilizzare.

***

## Quando si utilizza? 

Quando la classe wrapper (proxy) deve fare le STESSE COSE che fa il servizio, ma vuole aggiungere delle feature in più, come :

- controlli
- logging
- caching
- access control


> [!Warning] Attenzione!
> Ci sono altri pattern che fanno praticamente la stessa cosa, ma con una sottile differenza:
> 
> Aggiungono più metodi all' interfaccia wrappata.
> 
> Nel pattern proxy l' interfaccia implementata dalla classe proxy è la stessa implementata dal Servizio contenuto.
> 
> Sto solo separando le responsabilità: il servizio fa quello che deve fare, il proxy "aggiunge uno step prima".

> [!Hint] Importante
> Implementando la stessa interfaccia del servizio che sta wrappando. Questo rende le classi intercambiabili. 

> [!Warning] Differenze con altri pattern simili:
> - Adapter: wrappa un servizio e fornisce in uscita un' interfaccia DIVERSA da quella del servizio wrappato
> - Facade: implementa un' interfaccia diversa da quella del servizio wrappato
> - Decorator: prende l' interfaccia del servizio wrappato ed "aggiunge più features."
>   
>   Invece, ricordiamo, il proxy fa la STESSA COSA della classe wrappata, ma lascia al servizio fare "il lavoro bruto", e tutto ciò che sta attorno ed è di contorno se lo prende in carico lui.


## Esempio UML:

![[Pasted image 20240910100421.png | 400]]

Ad esempio CachedTubeClass implementa la stessa interfaccia del servizio che gestisce, fa dei controlli in più e basta (tipo "queste info sono presenti in cache?")

## Esempio in pseudo-codice:

```typescript
// 1. Definisco l'interfaccia del servizio
interface IService
    method GetData(param: String): String

// 2. Implementazione del servizio reale che fa la chiamata API
class RealService implements IService
    method GetData(param: String): String
        // Simula una chiamata API
        Print("Fetching data from API for: " + param)
        return "Data from API for " + param

// 3. Implementazione del Proxy con caching
class CachedServiceProxy implements IService
    private realService: IService
    private cache: Dictionary<String, String>

    // Costruttore che accetta il servizio reale
    constructor(realService: IService)
        this.realService = realService
        this.cache = new Dictionary<String, String>()

    // Metodo proxy che aggiunge il caching
    method GetData(param: String): String
        if cache.ContainsKey(param)
            Print("Returning cached data for: " + param)
            return cache[param]
        
        // Se non è in cache, chiama il servizio reale
        data = realService.GetData(param)

        // Memorizza la risposta nella cache
        cache[param] = data

        return data

// 4. Esempio di utilizzo
// Creo il servizio reale
realService = new RealService()

// Creo il proxy che avvolge il servizio reale
serviceProxy = new CachedServiceProxy(realService)

// Prima chiamata: si chiama l'API reale
Print(serviceProxy.GetData("example"))   // Output: Fetching data from API for: example
                                         //         Data from API for example

// Seconda chiamata con lo stesso parametro: si usa la cache
Print(serviceProxy.GetData("example"))   // Output: Returning cached data for: example
                                         //         Data from API for example

```

