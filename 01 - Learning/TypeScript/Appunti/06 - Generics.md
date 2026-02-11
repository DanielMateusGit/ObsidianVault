- [[#Funzioni Generiche|Funzioni Generiche]]
- [[#Constraints per i tipi generici|Constraints per i tipi generici]]
- [[#KeyOf Constraint|KeyOf Constraint]]
- [[#Classi template|Classi template]]

***
## Funzioni Generiche 

Funziona come nel C++.

Posso definire un tipo templato, che verrà concretizzato al momento della chiamata della funzione.

```typescript
function merge<T, U>(objA : T, objB : U){
	// Questa è una funzione built-in di JS
	// Ritorna un oggetto di tipo typeof objA & typeof objB
	return Object.Assign(objA, objB);
}

// TypeScript deduce il tipo degli argomenti passati
// (non devo esplicitarlo con in C++)
const mergedObj = merge({name : 'Max'}, {age : 30});
```

> [!Warning] Non potevamo usare object?
> Sì, ma in questo modo, con T ed U, stiamo anche specificando che i tipi sono diversi.
> 
> Inoltre, stiamo dicendo che qualsiasi tipo qui va bene, e la funzione godrà delle caratteristiche del codice generico.
> 
> Come in Java ad esempio, se passiamo Object => l'oggetto perde di identità, si sta facendo un UpCasting e vengono nascosti i suoi attributi etc...
> 
> Molto diverso invece è usare tipi templati. Sto semplicemente lasciando l' interpretazione dei tipi al momento della chiamata. Senza perdere alcuna informazione o fare Casting Impliciti di alcun tipo.

***
## Constraints per i tipi generici

Possiamo definire dei Contraint per i tipi generici.
Per farlo, ci basta definire dei tipi base per i nostri oggetti generici.

Ad esempio: un tipo T può estendere il tipo Object => in questo caso il tipo T sarà per forza un oggetto, ma della forma T.

Oppure vogliamo un tipo di base e poi vogliamo "aggiungerci qualsiasi altra cosa"? Allora la base di partenza sarà il constraint ed il resto invece rimarrà generica.

```typescript
// Ecco, in questo caso abbiamo inserito un constraint
// Ma il tipo rimane generico. Lo stiamo solo " stringendo un po' "
function merge<T extends object, U extends object>(objA : T, objB: U)
```

Altro esempio (bruttino, ma si capisce)

```typescript
interface Enumerable {
	length : number;
}

function CountLength<T extends Enumberable>(element : T) : [T, string];

// In questo caso ho un qualsiasi oggetto, ma che ha la proprietà length.
// Parto da un oggetto generico T => gli applico un contraint e lo rendo
// un pochino più specifico.
```

***
## KeyOf Constraint

Alcuni oggetti possono fare da chiave per altri oggetti.
Se vogliamo come input per una funzione un oggetto generico, ed un oggetto che fa da key per questo oggetto, possiamo utilizzare la keyword KeyOf.

```typescript
// In questo modo sto dicendo che il tipo T
// è un tipo generico, ma è comunque un oggetto (constraint)
// Ed il tipo U invece è una chiave del primo oggetto

function Extract<T extends object, U extends keyof T>(
	obj : T,
	key : U
){
	return obj[key]
};

// La chiamata ha la seguente forma:
Extract({name : 'John', lastName: 'Doe'}, 'name');
```


Esempio più complesso su cui riflettere:

```typescript
// A type that defines a validation function. 
// It receives a value and returns a boolean indicating if it's valid.
type ValidatorFunction<T> = (value: T) => boolean;

// A generic type that maps the keys of an object to their corresponding ValidatorFunction.
type Validator<T> = {
  [K in keyof T]: ValidatorFunction<T[K]>;
};

// Let's define an example object type
type User = {
  name: string;
  age: number;
  email: string;
};

// Now, we can create a specific validator object that adheres to the User type.
const userValidator: Validator<User> = {
  name: (value: string) => value.length > 0,
  age: (value: number) => value > 18,
  email: (value: string) => value.includes('@')
};

// A function that takes a Validator and an object, and validates it dynamically
function validateObject<T>(obj: T, validator: Validator<T>): boolean {
  for (const key in obj) {
    if (validator[key] && !validator[key](obj[key])) {
      return false; // Validation failed
    }
  }
  return true; // All validations passed
}

// Example usage
const user = {
  name: 'Alice',
  age: 25,
  email: 'alice@example.com'
};

const isValidUser = validateObject(user, userValidator);
console.log(isValidUser); // true

```

***

## Classi template

Abbiamo la seguente classe: 

```typescript
class DataStorage {
	private data = [];

	addItem(item) {
		this.data.push(item);
	}

	removeItem(item) {
		this.data.splice(this.data.indexOf(item), 1);
	}

	getItems() {
		return [...this.data];
	}
}
```

A cui vogliamo aggiungere "generalità". Possiamo introdurre un tipo templato di classe.

```typescript
class DataStorage<T> {
	private data : T[] = [];

	addItem(item : T) {
		this.data.push(item);
	}

	// etc...
}
```

Aggiungendo questo tipo generico, stiamo dicendo che i metodi in input accettano lo stesso tipo con cui abbiamo definito la classe.

Passando un generico item invece avremmo avuto un warning (e possibilità di fare errori).

```typescript
const textStorage = new DataStorage<string>();

// Siamo sicuri di avere un giusto controllo per chiamate del tipo:
textStorage.addItem("Eliot");

const objectStorage = new DataStorage<object>();
objectStorage.addItem({name : 'Max'});
```

Occhio! Gli oggetti complessi vengono passati per reference.
Bisogna gestire bene queste cose.

Possiamo specializzare il tipo template della classe (stringere):

```typescript
class DataStorage<T extends string | number | boolean> {
	// ... etc ...
}
```

> [!Warning]
> Conviene leggersi il passaggio per reference e copia in JS => e sugli oggetti.