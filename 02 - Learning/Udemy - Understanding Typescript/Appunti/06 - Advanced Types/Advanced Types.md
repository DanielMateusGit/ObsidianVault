# Advanded Types

## Inersection Type

Posso Unire più tipi in uno solo. Si chiama intersezione ma corrisponde all'unione.

```typescript
type Admin = {
	name : string;
	privileges : string[]; 
};
```

```typescript
type Employee = {
	name : string;
	startDate : string;
}
```

```typescript
type ElevatedEmployee = Admin & Employee;

// In questo momento ElevatedEmployee:

type ELevatedEmployee = {
	name : string; 
	privileges: string[];
	startDate : string;
}
```

Ha lo stesso comportamento di un' interfaccia che ne estende altre due preesistenti.

***

## Type Guards 

Abbiamo già visto le type guards. Sono dei controlli preliminari ci che assicurano che sia possibile eseguire un' operazione su un dato di un certo tipo. Ad esempio:

```typescript
function add ( a : CompType , b : CompType ) {
	if(typeof a == 'string' && typeof b == string){
		return a.toString()  + b.toString();
	}

	return a + b
}
```

Se volessimo fare la stessa cosa con un tipo Typescript?

Non potremmo, dato che typeof funziona solo con i tipi nativi di Javascript.

Abbiamo però una "soluzione":

```typescript
// Questo nuovo tipo può essere di due tipi: Employee oppure Admin
type UnknownEmployee = Employee | Admin;

function printEmployeeInformation(emp : UnknownEmployee ){
	// Questa istruzione sappiamo che possiamo sicuramente farla
	// perchè sia in Employee che Admin abbiamo un attributo Name
	console.log('Name' + emp.name);
	
	//Invece, un attributo può esistere in un tipo o nell' altro.
	// E visto che noi possiamo avere "o un tipo o l' altro", non è
	// garantito che un attributo esista.
	console.log(emp.privileges); // QUESTO MAGARI NON ESISTE

	// Dobbiamo fare il seguente controllo:
	if( 'privileges' in emp ){
		// Qui siamo sicuri che esiste l' attributo privileges
		console.log(emp.privileges);
	}
}
```

Un esempio con le classi potrebbe essere il seguente:

```typescript
class Car {
	drive() {
		console.log("I am driving a car");
	}
}

class Truck {
	drive() {
		console.log("I am driving a Truck");
	}

	loadCargo(weight : number) {
		console.log("Loading a cargo");
	}
}

// A questo punto devo definire un tipo 
type Vehicle = Car | Truck;

// Se voglio definire un metodo che sia sicuro per il tipo veicolo
// Allora devo mettere delle guardie sulle informazioni non comuni
function useVehicle( Vehicle : Vehicle ){
	vehicle.drive();

	if(loadCargo in Vehicle) {
		vehicle.loadCargo(100);
	}
}
```

L' ultimo metodo, dato il type Checking che sta facendo, è sicuro per l' utilizzo di un tipo di dato Vehicle.

*** 

## Discriminated Unions 

Se invece volessimo discriminare il tipo in una maniera più precisa, potremmo creare un dato type:

```typescript
interface Bird = {
	type : 'bird';
	flyingSeed : number;
}

interface Horse = {
	type : 'horse';
	runningSpeed : number;
}

type Animal = Bird | Horse;

// Nel momento in cui vogliamo eseguire un' operazione sul tipo
// Animal, ci basta controllare il type (che esiste per tutti)

function moveAnimal(animal : Animal) {
	let speed;
	switch(animal.type){
	
		case 'bird':
			console.log(animal.flyingSpeed);
		break;
		
		case 'horse':
			console.log(animal.runningSpeed);
		break;
	}
}
```

Questo lo abbiamo già visto in C#. Magari in un' ottica più da Dependency Injection. Tante classi che implementano la stessa interfaccia, discriminate grazie ad un type. 

Non è proprio la stessa cosa, ma è un rimando.

***

## Type Casting

Esiste il type casting esplicito in TypeScript.

Caso d' uso: 

```html
<input type="text" id="user-input"/> 
```

```typescript
const userInputElement = document.getElementById('user-input');
// La seguente linea di codice produrrà un warning di typescript:
userInputElement.value = 'Hello, friend!'; 
```

Il warning verrà prodotto perchè TypeScript non conosce esattamente il tipo di elemento che si sta cercando di reperire dal DOM.

Lui sa solo che è un elemento di tipo html. Nient' altro.

Non sa se questo elemento html ha dentro un value. 

Non sa nemmeno se è possibile reperire correttamente questo elemento (protrebbe essere null).

Come faccio a dire a typescript che questo elemento esiste e che ha un valore (dato che è un input text)?

```typescript
// Con il punto esclamativo ne correggo l'esistenza!
// In questo modo sto dicendo a typescript che questo elemento
// sicuramente esiste e non è null.
const userInputElement = document.getElementById('user-input')!;

// Questa riga mi genera ancora un warning però
// E questo accade perchè comunque io non so di che tipo di 
// elemento html stiamo parlando (non so se ha un value).
userInputElement.value = 'Hello, friend!'; 
```

Ora, per riuscire a far capire a TypeScript che tipo di elemento stiamo selezionando dal DOM, posso fare un casting.

Il casting mi permette di trasformare l' oggetto generico del DOM in un oggetto specializzato HTMLInputElement.

```typescript
const userInputElement = <HTMLInputElement>document.getElementById('user-input')!;
```

Possiamo utilizzare anche un sintactic sugar: 

```typescript
const userInputElement = document.getElementById('user-input')! as HTMLInputElement;
```

Questa scritta è equivalente, e forse un po' più parlante.

> [!Warning] Potrebbe non bastare!
> 	Nel caso ci fossero ancora errori da parte di TypeScript => bisogna inserire in tsconfig.json in lib => la libreria dom

> [!Warning] Attenzione!
> Ovviamente noi stiamo forzando un casting, essendo certi del tipo che sta dietro a questa variabile. Bisogna essere assolutamente sicuri e certi che si stiano facendo le cose correttamente. Altrimenti potremmo avere degli errori indesiderati.

***

## Index Properties (utile per dizionari)

Le proprietà indicizzate sono degli attributi "speciali".

Queste proprietà possono avere un qualsiasi nome (o chiave).

L' importante è che seguano la "forma" specificata dall' interfaccia in cui vivono.

In genere possono essere utilizzati per creare delle interfacce per Dizionari.

In ESGeo ad esempio sono utilizzate nei Bundle (quelli con più istruzioni per creare una lista di operazioni CRUD per il server).

```typescript

// interfaccia con index property
interface ErrorContainer {

    // Qui io sto dicendo che voglio una prop generica, di cui non conosco il nome.
    // Il property name è associato al concetto di chiave (come nei dictionary).
    // Posso specificare il data type della chiave, ed il data type del value
    // Inoltre, sto anche dicendo che voglio "molti di questi dati".

    [prop : number] : string;

	// Posso anche specificare un attributo in particolare, e l' oggetto
	// che implementa questa interfaccia sarà forzato a contenerlo
    email : string;
	
	// Ma tutto il resto, che non è contemplato in questa interfaccia 
	// Ed è "Extra" sarà visto dal compilatore come un errore
}

const errorBar : ErrorContainer = {

    email: "prova proprietà",

    1 : "hello",

    2: "hello",

    ciao : "hola" // Questo da errore perchè nell' interfaccia non è previsto!
}
```

***

## Overload di funzioni 

Altra feature OOP arricchita da TypeScript è l' overload di funzioni:

```typescript

type Combinable = string & number;

function add(a : Combinable, b : Combinable) {
	if(typeof a === 'string' && typeof b === 'string') {
		return a.toString() + b.toString() ; 
	}
	
	return a + b;
}

const result = add('Hello, ', 'Friend'); 
console.log(result.toString()); // Ho un errore!

// result è di tipo Combinable ... che accetta sia numeri che stringhe
// io a questo punto del codice non so se ho un numero o una stringa.
// Posso quindi chiamare toString su result? Non lo so per certo.
```

Il problema di questo codice è che ritornerà un tipo Combinable, anche se riesce effettivamente, tramite le guardie, a gestire diversi tipi di dato in input.

Per ovviare al problema possiamo fare un overload del metodo, specificando come cambia il tipo dell' output, al variare dell'input.

> [!Warning] Attenzione
> Se l' overload di una funzione non ha un corpo, allora verrà trovato dal compilatore, il primo corpo (o definizione) compatibile. 
> 
> In questo caso posso definire più firme di una funzione con un solo corpo, basta che siano compatibili. Voglio solo specificare quale output ho con determinati input in entrata, ma tutto deve essere compatibile con la definizione piu "generica".

Esempio di quanto detto: 

```typescript

type Combinable = string & number;

// Ecco, grazie a questo overloading di funzione 
// Compatibile con Combinable, io posso fare in modo di
// ottenere un determinato output al variare dell' input.
function add(a: number, b: number) : number;
function add(a : string, b: string) : string;
function add(a : Combinable, b : Combinable) {
	if(typeof a === 'string' && typeof b === 'string') {
		return a.toString() + b.toString() ; 
	}
	
	return a + b;
}

// In questo caso:
const result = add('Hello, ', 'Friend'); 
console.log(result.toString()); // funziona!

// Perchè grazie all' overloading di funzione con un solo corpo 
// Data la compatibilità di input tra Combinable e string, io sto 
// chiamando la funzione che prende delle stringhe come input 
// e mi restituisce una stringa come ouput.
// Ma sto andando ad eseguire la stessa definizione di funzione di Combinable.
```

In Typescript si può "cammuffare" la definizione di funzione per castare implicitamente l' output tra tipi compatibili.

=> Altrimenti, se non si vuole fare tutto questo, basta utilizzare un cast dell'output, come abbiamo visto in precedenza. 

***

## Optional Chaining

In TypeScript abbiamo una shorcut per l' optional Chaining di JS:

```javascript

// Se abbiamo un oggetto che dovrebbe avere la seguente forma:
const Person = { 
	name : 'John',
	lastName : 'Doe',
	//job : { title: 'Developer', Description: 'FullStack Dev' } 
}

// Immaginiamo che l' ultimo non esista per un qualunque motivo
// O sia null per qualunque motivo.
// (magari arriva dal server e J.D Ancora non ha un lavoro).

// Per evitare di accedere ad un dato inesistente, in js:

console.log( Person.job && Person.job.title);

// Se non esiste Person.job, allora non accederò al title
```

Invece in TS abbiamo una shortcut:

```javascript
const Person = { 
	name : 'John',
	lastName : 'Doe',
	//job : { title: 'Developer', Description: 'FullStack Dev' } 
}

// Con TS la stessa cosa si fa così: 
console.log( Person.job?.title);

// Mi sto chiedendo: esiste Person.job? Ok, allora accedi al title
// Uguale, ma più bello
```

***

## Null Coalescing

```typescript
// Posso specificare un valore di default per quelle situazioni in cui ho un dato
// NULL, dopo un controllo:

const storedDate = dataFromServer ?? 'DEFAULT_VALUE';
```

***
