
## Introduzione

Questa guida ✍️, scritta da me (@DanielMateusGit), vuole essere un aiuto semplice e pratico 💡 per chi vuole costruire interfacce in **ReactJS** ⚛️ senza perdersi nei dettagli. Non troverai regole rigide 🚫, ma piuttosto consigli e buone pratiche ✅ da tenere a mente quando scrivi codice.

---
## Separare presentazione e logica

Quando si progetta una UI è bene separare i componenti in due categorie:
1. I componenti dei presentazione, che si occupano solo della UI
2. I componenti contenitori, che gestiscono Stato e logiche complesse.

Ad esempio, se volessi comporre la seguente interfaccia: 

![[Pasted image 20250908100643.png]]

La separazione sarebbe la seguente: 

```jsx
// Presentazione 
const UserCard = ({ user }) => (
	<div className="card"> 
		<img src={`users/${user.image}`}/>
		<h3>{user.name}</h3>
	</div>
);
```

```jsx
// Contenitore logico
const UserListContainer = () => {
	const [users, setUsers] = useState([]);
	
	useEffect(() => {
		fetch('api/users/').then(res => res.json()).then(setUsers);
	}, []);
	
	return users.map(u => ); 
};
```


---
## Utilizzare la props children per comporre componenti riutilizzabili

In React, **`children` è una prop speciale** che contiene **quello che scrivi dentro un componente**.  

È come dire: _“tutto quello che metti tra `<Apertura>` e `</Chiusura>` lo passo al componente come `children`”_.

```jsx
const Box = ({ children }) => <div className="box">{children}</div>;

// Uso:
<Box>
  <h2>Ciao</h2>
  <p>Io sono dentro il box!</p>
</Box>

// In questo caso, il children di Box è:

<h2>Ciao</h2>
<p>Io sono dentro il box!</p>

```

Quindi, children risulta utile per scrivere componenti più generici, come ad esempio:

```jsx
const Card = ({ children }) => ( 
	<div className="card">{children}</div>
}
```

In questo modo, sto wrappando i figli di Card in un div, qualsiasi essi siano:

```jsx
<Card>
	{// Questi sono i figli!}
	<h3> Titolo </h3>
	<p>Contenuto</p>
</Card>

<Card>
	{// E posso passare qualsiasi cosa! }
	<div className="userContent"> 
		<img src={`users/${user.image}`}/>
		<h3>{user.name}</h3>
	</div>
</Card>


<Card>
	<MyComponent />
</Card>
```

---

## Utilizzo di List Rendering + Keys

Per renderizzare un insieme di componenti, bastano:
1. La funzione map() che applica una funzione in entrata ad ogni oggetto di una lista.
2. Una lista di oggetti contenenti le informazioni da presentare

Ad esempio: 

```jsx
const devs = ["Anna", "Flavio", "Davide", "Hasan", "Saimir", "Eugenio", "Luca", "Giacomo", "Daniel"];

// ... dentro la return del componente
<h1> Il nostro team dev! </h1> 
<ul>
	{devs.map((dev, index) => <li key={index}> {dev} </li> )}
</ul>
```

---

## Rendering su condizione 

Come suggerisce il nome, questa è una tecnica per mostrare/nascondere una parte di UI su condizione: 

```jsx
{loading ? <p> Users list is loading </p> : <UsersList data={data} />}
{error && <p> There was an error fetching data </p>}
```

In questo caso: 
1. Se il booleano loading è a true, allora faccio vedere un messaggio di caricamento
2. Altrimenti faccio vedere il componente Lista 
3. Se ho un errore (booleano settato da funzione esterna), invece faccio vedere un messaggio di errore 

---- 