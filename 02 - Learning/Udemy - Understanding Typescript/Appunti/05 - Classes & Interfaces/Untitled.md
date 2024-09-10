
## Classes and interfaces 

## Classi per OOP 

```javascript
class Department {
	name : string = ''; //posso dargli un valore iniziale

	 constructor (n : string) {
		 this.name = n;
	 }

}

const dep1 = new Department("Computer Science");
```

Come si può vedere, abbiamo una normale classe con metodo costruttore.

***
## Modificatori di accesso

In Javascript è tutto pubblico di default. 
Per rendere qualcosa private, si usa le keyword private.

```typescript
class Department {
	private name : string; 
	// questo rende l' attributo inaccessibile da fuori 
}
```

Anche il modificatore d' accesso public può essere specificato.

Javascript supporta i modificatori di accesso SOLO NELLE VERSIONI PIÙ RECENTI.

È sempre grazie a TypeScript che possiamo utilizzare e controllare i modificatori di accesso delle classi.

***

## Costruttore "slim"

Come in C#, possiamo usare una shorthand:

```typescript
// invece di creare un costruttore come questo:

private name : string = "example";
private id : number = 24030;

constructor ( name: string, id: number ){
	this.name = name;
	this.id = id
} 

// Possiamo SOLO PASSARE GLI ARGOMENTI AL COSTRUTTORE
// ED IL RESTO SARÀ AUTOMATICO

constructor (name : string, id : number) {}

// Basta questo. È equivalente.

```


*** 

## Proprietà readonly


Semplicemente, si usa la keyword readonly dopo la private.

*** 

## Esempio di quanto visto fino ad ora

```typescript
class Person {

  constructor
  (
	  private name : string,
	  private id : number,
	  private readonly password : string
  ){}

  public getName = () => this.name;
  public getId = () => this.id;
}

const person = new Person("Daniel", 24030);
console.log(person.getName());
console.log(person.getId());
```

Tutto questo funziona e poi viene compilato in JS.
Attenzione le classi sono supportate da es6 in avanti (JS 2015).


> [!Warning] Attenzione!
> Le classi in JS non sono davvero classi.
> Le classi in JS sono funzioni. Infatti, prima della version es6, esistevano solo le funzioni di costruzione.
> 
> TypeScript permette di scrivere delle classi arricchite, che vengono tradotto in classi Javascript.
> 
> Le classi Javascript a loro volta, vengono tradotte in funzioni di costruzione.
> 
> ci sono più dettagli sull' argomento:
> 
> https://www.digitalocean.com/community/tutorials/understanding-classes-in-javascript

> [!Warning] Funzioni costruttrici ed oggetti
> Le funzioni costruttrici erano le incaricate di andare a creare un oggetto.
> 
> Oltre agli attributi dell' oggetto, poteva, tramite i PROTOTIPI (definizione di cosa contiene la classe), definire i metodi dell' oggetto che andava a costruire.
> 
> Inoltre, l' utilizzo dei prototipi permetteva l' ereditarietà.
> Ancora oggi funziona così, ma è tutto camuffato in una sintassi più vicina alla tradizionale OOP


```typescript
function Persona(nome) {
  this.nome = nome; // Proprietà definita direttamente sull'oggetto
}

Persona.prototype.saluta = function() {
  console.log(`Ciao, mi chiamo ${this.nome}`);
};

// Creazione di due istanze
const mario = new Persona('Mario');
const luigi = new Persona('Luigi');

```

***
