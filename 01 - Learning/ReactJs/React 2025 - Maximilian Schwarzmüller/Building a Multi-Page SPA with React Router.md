
- [[#Cosa è il routing?|Cosa è il routing?]]
- [[#Come funziona?|Come funziona?]]
- [[#Installazione|Installazione]]
- [[#Le API createBrowserRouter ed il RouterProvider|Le API createBrowserRouter ed il RouterProvider]]
- [[#La prima route!|La prima route!]]
- [[#Come navigare tra le pagine?|Come navigare tra le pagine?]]
- [[#Come utilizzare un RouteLayout?|Come utilizzare un RouteLayout?]]
- [[#E se si visita una route che non esiste?|E se si visita una route che non esiste?]]
- [[#Migliorare la navigazione con i NavLinks|Migliorare la navigazione con i NavLinks]]

---
## Cosa è il routing? 

In una **Single Page Application (SPA)** non ci sono ricaricamenti di pagine dal server: i contenuti vengono aggiornati dinamicamente all’interno della stessa pagina.

Il **Routing** serve a dare l’illusione della navigazione, permettendo di associare diverse sezioni dell’app a URL distinti. In pratica:

- Ogni URL mostra una parte diversa dell’applicazione.
    
- Consente la navigazione avanti/indietro con i pulsanti del browser.
    
- Permette di condividere link diretti a specifiche sezioni.
    
- Migliora l’organizzazione e la struttura dell’app.

***
## Come funziona?

Il **routing in una SPA** funziona così:

- Normalmente, quando scrivi un URL e premi invio, il browser manda una **richiesta HTTP al server**, che risponde con un nuovo file HTML.
    
- In una SPA invece non succede: c’è un solo file `index.html`.
    
- Il **router** intercetta il cambio di URL e dice al browser: _“Non chiedere niente al server. Carico io il componente giusto dentro la pagina”_.
    
- Quindi, a seconda dell’URL, vengono caricati **on demand** i componenti corretti (es. `/home` → componente Home, `/about` → componente About).
    

> [!Hint] 
> 👉 In pratica, il server invia l’app solo una volta. Dopo, è il **JavaScript della SPA** che gestisce tutta la “navigazione” localmente.

> [!Hint] 
> Quindi, vogliamo un comportamento tipico delle applicazioni multi-pagina, ma in una single-page, con il vantaggio di dover richiedere la SPA una sola volta.

---
## Installazione

Molto semplice:

```
npm install react-router-dom
```

Dentro il terminale dell' applicazione, ed abbiamo finito ;) 

---
## Le API createBrowserRouter ed il RouterProvider

Le API fondamentali per configurare le rotte dell' applicazioni sono `createBrowserRouter` e `RouterProvider`.

Quando usi `createBrowserRouter` e `RouterProvider` stai semplicemente dicendo a React Router **“questa è la mappa della mia applicazione, usala per gestire la navigazione”**.

`createBrowserRouter` è lo strumento con cui costruisci quella mappa: una lista ordinata di percorsi e componenti da mostrare.  

`RouterProvider`, invece, è il “motore” che prende quella mappa e la mette in funzione, collegandola al browser e permettendo all’utente di spostarsi tra le varie sezioni della tua app.

Lavorano sempre insieme: il primo descrive _cosa_ deve succedere, il secondo si assicura che accada davvero.

--- 
## La prima route!

Per prima cosa disegniamo la mappa di navigazione della nostra applicazione:

```jsx
// router.jsx
import { createBrowserRouter } from "react-router-dom";

// Qui stiamo dicendo: 
// "se visito https://localhost8080/path -> renderizza il componente <X />"

const router = createBrowserRouter([
  {
    path: "/",         // URL
    element: <Home />, // Componente da renderizzare
  },
  {
    path: "/about",
    element: <About />,
  },
  {
    path: "/contact",
    element: <Contact />,
  },
]);

export default router;

```

E poi, rendiamo nota questa informazione (la nostra mappatura) a tutto il resto dell' applicazione:

```jsx
// main.jsx o App.jsx
import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import router from "./router";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

```

Adesso è possibile "visitare" : 

locahost:8080, locahost:8080/about e locahost:8080/contact

> [!Hint] RouterProvider funziona come i Context!
> `<RouterProvider>` **funziona come un context** di React sotto il cofano. Quando lo usi, fornisce a tutti i componenti figli (e ai discendenti) **l’accesso allo stato del router**

> [!Hint] Cosa possiamo fare con RouterProvider
> Abbiamo accesso ad alcuni hook per la gestion del routing:
> 
> - `useNavigate()` → per navigare programmaticamente
> - `useLocation()` → per sapere l’URL corrente
> - `useParams()` → per leggere i parametri dinamici della route
> - `useMatches()` → per avere info sulle route correnti e sui dati caricati
> 

---
## Come navigare tra le pagine?

Finora hai impostato le route, ma muoverti tra di esse significa ancora cambiare manualmente l’URL.  

In una vera app web, vuoi **cliccare su link o pulsanti e spostarti subito da una pagina all’altra**, senza ricaricare tutto.

React Router ti semplifica la vita con componenti dedicati, tipo:

```jsx
<Link to="/products">Vai a Products</Link>
```

Così, clicchi e sei subito nella route desiderata, veloce e senza ricaricare la pagina. 🚀

*** 
## Come utilizzare un RouteLayout? 

Quando hai più pagine che condividono **parte della struttura**, conviene creare una **route madre** (layout) e delle **route figlie** per i contenuti specifici.

>[!success] Concetto chiave:
>1. La **route madre** (layout) si occupa **solo di presentare la struttura generale**
>   2. Le **route figlie** sono le pagine effettivamente navigabili
>   
    
Questa separazione è utile, ad esempio, quando vuoi creare un menu di navigazione con tante sezioni diverse.

1. Dichiara la route madre e le route figlie usando `createBrowserRouter`:

```jsx
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,  // layout madre (fa da layout)
    children: [
      { path: "/", element: <Home /> },     // route figlia
      { path: "about", element: <About /> }, // route figlia
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

```

> [!Hint] Che è successo fino ad ora?
> Così informiamo il `RouterProvider` che `<Layout />` è responsabile di ospitare le sue route figlie.

2. Definire il layout e dove renderizzare le route figlie

All’interno del componente layout, usa `<Outlet />` come **segnaposto** per le route figlie. Puoi posizionarlo dove vuoi: in alto, in basso, in un menu laterale, ecc.

```jsx
import { Outlet, Link } from "react-router-dom";

function Layout() {
  return (
    <div>
      <header>
        <h1>La mia App</h1>
        <nav>
          {/* Link per navigare tra le route figlie */}        
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
        </nav>
      </header>

      <main>
        {/* Qui verranno renderizzate le route figlie */}
        <Outlet />
      </main>

      <footer>© 2025</footer>
    </div>
  );
}

export default Layout;

```

> [!Hint] ⚡ Nota importante
> `<Outlet />` è **il punto dove React Router inserisce la route figlia attiva**.  
Quando cambi pagina, il layout resta fisso, mentre `<Outlet />` mostra il contenuto della route figlia corrente.

***
## E se si visita una route che non esiste?

Quando definisci le tue route, React Router permette di specificare un componente che viene renderizzato **in caso di errore**, ad esempio se la route non esiste o se un loader/action genera un errore.

Il componente di errore si dichiara usando la proprietà `errorElement` nella route.

```jsx
function ErrorPage({ error }) {
  return (
    <div>
      <h1>Oops! Qualcosa è andato storto.</h1>
      <p>{error?.statusText || error?.message || "Errore sconosciuto"}</p>
    </div>
  );
}

export default ErrorPage;

```

> [!Hint] 
> Il parametro `error` viene passato automaticamente da React Router quando qualcosa va storto nella route.

Per aggiungere questa pagina di errore ci basta:

```jsx
const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />, // qui dichiariamo la ErrorPage
    children: [
      { path: "/", element: <Home /> },
      { path: "about", element: <About /> },
    ],
  },
]);
```

Riassumendo: 

- Se accedi a una route inesistente (ad esempio `/contatto`) oppure un loader/action genera un errore, **React Router renderizza `<ErrorPage />` al posto della route figlia**.    
- Il layout madre rimane attivo, quindi header/footer/menu non spariscono.

***

## Migliorare la navigazione con i NavLinks

Fino ad ora hai utilizzati i Link per costruire dei collegamenti.
Ci sono dei collegamenti più adatti alle strutture Layout e di navigazione: i NavLinks

Che cosa cambia? Hanno delle direttive in più per facilitare la realizzazione di "stati della navigazione".

```jsx
	{\* Questo è il link classico usato fino ad ora :D *\}
  <Link to="/home">Home</Link> | <Link to="/about">About</Link>
  
  {\* invece con i NavLink, abbiamo delle funzioni, che prendono uno stato in entrata ( e react router capisce da solo come settarli), per poter resgire meglio a quello che succede:   *\}
  
  <NavLink
	to="/about"
	style={({ isActive }) => ({
	  color: isActive ? "green" : "blue",
	  fontWeight: isActive ? "bold" : "normal",
	})}
  >	
	About
  </NavLink>
```

**** 