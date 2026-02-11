# Decorators

***
## Cosa sono?

I decoratori sono dei modi compatti per definire funzioni.

Per definire un decoratore:
- Creare una funzione che prenda in input un argomento di tipo Function.
- Alla funzione corrisponderà un simbolo @nome_funzione riutilizzabile.
- Ponendo questo simbolo prima di una classe (o dato membro di una classe), questa verrà passata automaticamente come argomento al decoratore.
- Il Decoratore verrà eseguito durante il processo di Compilazione da TS => JS. 

> [!NOTE] Come configurare TypeScript
> Vengono attivati ponendo a true la voce "experimentalDecorators del file tsconfig.json. La versione di Js deve essere es6 o superiore.

*** 
## Quando utilizzarlo?

Quando voglio creare delle funzionalità "attacca-stacca" per classi eterogenee.
Ad esempio: 
- Funtore per fare il Log di classi diverse
- Funtore per validare l' input di un metodo di classe
- Funtore per rendere readonly una proprietà 

***

## Esempio

```typescript

const Logger = (contructor : Function) => {
    console.log("INSIDE LOGGER DECORATOR");
    console.log(contructor);
}

@Logger
class Person {

    constructor (private name : string, private lastName : string) {}

    @Logger
    public greeting(){
        console.log(`Hello! I am ${this.name} ${this.lastName}`);
    }
}
```

Avrà come risultato: 

```bash
[LOG]: "INSIDE LOGGER DECORATOR"  

---

[LOG]: greeting() { console.log(`Hello! I am ${this.name} ${this.lastName}`); }  

---

[LOG]: "INSIDE LOGGER DECORATOR"  

---

[LOG]: class { constructor(name, lastName) { this.name = (__runInitializers(this, _instanceExtraInitializers), name); this.lastName = lastName; } greeting() { console.log(`Hello! I am ${this.name} ${this.lastName}`); } }
```

*** 

## Decorator Factory

Il Decorator Factory è una funzione che: 
 * È in grado di impostare un decoratore tramite un input
 * È in grado di restituire il decoratore previamente impostato

Il Decorator Factory è rende configurabile e riutilizzabile il decoratore.

***

## Esempio

```typescript
// Decorator Factory ()
function Logger(logString : string){
    return function(constructor : Function){
        console.log(logString);
        console.log(constructor);
    }
}

@Logger('LOGGING - PERSON CLASS:')
class Person {
    constructor (private name : string, private lastName : string) {}
    
    @Logger('LOGGING - PERSON GREETING METHOD:')
    public greeting(){
        console.log(`Hello! I am ${this.name} ${this.lastName}`);
    }
}
```

 Avrà come risultato:

```bash
[LOG]: "LOGGING - PERSON GREETING METHOD:"  

---

[LOG]: greeting() { console.log(`Hello! I am ${this.name} ${this.lastName}`); }  

---

[LOG]: "LOGGING - PERSON CLASS:"  

---

[LOG]: class { constructor(name, lastName) { this.name = (__runInitializers(this, _instanceExtraInitializers), name); this.lastName = lastName; } greeting() { console.log(`Hello! I am ${this.name} ${this.lastName}`); } }
```

*** 

## Esempio di utilizzo più avanzato

Stiamo progettando un videogioco. 
Nel videogioco possiamo avere diversi item: Cibo, Armi, Vestiti.

Tutte queste classi hanno un type. Vogliamo stampare a video tutti i tipi di item esistenti.

```typescript
// Decorator Factory

function print_info_with_template(template: string, id: string) {

    // Decorator
    return function (constructor: any) {
        const anchorHTML = document.getElementById(id);
        const item = new constructor();

        if (anchorHTML) {
            anchorHTML.innerHTML = template;
            const paragraph = anchorHTML.querySelector('p');
            paragraph
                ? (paragraph.textContent = item.type)
                : (anchorHTML.innerHTML += `<p>you should define a <p> in 
                template</p>`);
        }
    };
}

  

// Applicazione del decoratore a una classe

@print_info_with_template('<p>Type is:</p>', 'app')
class Product {
    type: string = 'Electronics';
}
```


Questo andrà ad aggiungere, sotto l' elemento HTML con id 'app' il template specificato. Successivamente andrà a rimpiazzare il testo del template con l' informazione data dentro il corpo del decoratore.


> [!Hint] Dove potrebbe risultare utile? 
> Esempio di utilizzo? Una classe "Editor"


****

## Applicare più decoratori

Se applico più decoratori ad una classe, l' esecuzione avverrà in modalità bottom-up.

Prima verrà applicato il decoratore più vicino alla dichiarazione di classe (o metodo) e successivamente quelli man mano più lontani.

***

## Property Decorators

Sono dei decorators applicabili alle proprietà di una classe.

```typescript
function Log(target : any, propertyName : string | Symbol){
	console.log('PropertyDecorator');
	console.log(target, propertyName);
}

class Product {
	@Log
	title : string;
}
```

Questo stampa: 

* Il prototipo della classe
* La stringa "title"

***
## Parameter decorator

Posso creare dei decoratori per parametri di funzione:

```typescript
getPriceWithTax( @Log tax : number ){
 return ....
}

// Voglio stampare tax :
function Log(target: any, name : string | Symbol, position : number){
	console.log('Parameter decorator!');
	console.log(target); //parameter name
	console.log(name); // method name
	console.log(position); // position of the argument
}
```

***

## Ritornare una classe con i decoratori

È possibile ritornare una classe in un decoratore.
Ricordiamo ancora una volta, i decoratori non sono altro che funzioni.

Quello che un decoratore è ritornare una classe costruita a partire da quella recepita come input.

```typescript
function WithTemplate (template : string, hookId : string) {
	// stiamo dicendo che il ritorno sarà un oggetto invocabile con new!
	// che prende un numero di parametri di tipo qualsiasi, ma di cui 
	// almeno uno deve essere chiamato name e deve essere di tipo string
	return function<T extends { new(..args: any[]) : {name : string} }>
	(
		originalConstructor : T
	){
		// Nuova classe costruita (a partire da quella in input)
		return  class extends originalConstructor {
			constructor(..._: any[]){ 
			
				// stiamo chiamando originalConstructor (come in Java)
				super(); 
				
				// Comportamento della nuova classe :D 
				console.log('rendering template');
				const hookElement = document.getElementById(hookId);
				const p = new constructor();
				
				if(hookElement){
					hookElement.innerHTML = template;
					hookElement.querySelector('h1').textContent = p.name;
				}
			}
		}
	};
}

// lo utilizzo
@WithTemplate('<h1> My person Object </h1>', 'app')
class Person { 
	name = 'Max';
	
	constructor() {
		console.log('creating person object...');
	}
}

// istanzio oggetto
const p = new Person();

// Tutta la logica viene aggiunta solo quando 
// la classe viene istanziata (non solo in dichiarazione)
```

In questo modo posso impacchettare in un decorator dei comportamenti che vanno a specializzare le classi vicino a cui verrà posto.


> [!Warning] Bisogna istanziare oggetti!
> In questo caso, dato che il decoratore ritorna una funzione di costruzione, per essere "invocato" bisogna per forza istanziare un oggetto del tipo di classe in input.
> 
> Ora il decoratore non è più legato alla definizione della classe, ma all' istanziazione di oggetti di tale classe!

***

## Esempio avanzato di uso dei docorator per validazione:

```typescript
interface ValidatorConfig {

  [property: string]: {

    [validatableProp: string]: string[]; // ['required', 'positive']

  };

}

  

const registeredValidators: ValidatorConfig = {};

  

function Required(target: any, propName: string) {

  registeredValidators[target.constructor.name] = {

    ...registeredValidators[target.constructor.name],

    [propName]: ['required']

  };

}

  

function PositiveNumber(target: any, propName: string) {

  registeredValidators[target.constructor.name] = {

    ...registeredValidators[target.constructor.name],

    [propName]: ['positive']

  };

}

  

function validate(obj: any) {

  const objValidatorConfig = registeredValidators[obj.constructor.name];

  if (!objValidatorConfig) return true;

  let isValid = true;

  for (const prop in objValidatorConfig) {

    for (const validator of objValidatorConfig[prop]) {

      switch (validator) {

        case 'required':

          isValid = isValid && !!obj[prop];

          break;

        case 'positive':

          isValid = isValid && obj[prop] > 0;

          break;

      }

    }

  }

  return isValid;

}

  

class Course {

  @Required

  title: string;

  @PositiveNumber

  price: number;

  

  constructor(t: string, p: number) {

    this.title = t;

    this.price = p;

  }

}
```

