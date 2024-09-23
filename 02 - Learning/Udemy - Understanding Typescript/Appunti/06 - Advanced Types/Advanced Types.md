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


