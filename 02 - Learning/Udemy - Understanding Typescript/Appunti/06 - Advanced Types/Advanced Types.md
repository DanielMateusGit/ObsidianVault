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
