---
tags:
  - TypeScript
  - TypeScript/Types
  - WebDev
---

# Types

***

## Quali sono i tipi primitivi?

I tipi primitivi sono:

- number
- string
- boolean


> [!Warning] TypeScript funziona solo in fase di compilazione
> Essendoci una fase intermedia che compila TS => JS, gli errori vengono notificati solamente durante la compilazione. 
> 
> A Run-Time TypeScript, è inutile. Ad essere eseguito è solo ed esclusivamente codice Javascript. 
> 
> Possiamo eseguire un file JavaScript generato da un file TypeScript solo in seguito ad una precedente compilazione.

> [!Hint]
> Per avere un check degli errori durante la scrittura del codice, si possono estendere gli editor con dei tools appositi.
> 
> Non sarà necessario compilare esplicitamente da terminale ogni volta prima di vedere dove abbiamo sbagliato.
> 

***

## Come definisco oggetti?

I creatori di TypeScript hanno inventato un tipo specifico: ==object==.

Il solo tipo object non è però sufficiente! Non abbiamo le seguenti informazioni:

 - Non abbiamo informazioni sui metodi che dovrebbe contenere
 - Non abbiamo informazioni sugli attributi che dovrebbe contenere

L' accesso a qualsiasi dato membro di un oggetto di tipo ==object== genererà un errore TypeScript.

È possibile specificare la "forma" del tipo di dato, per poter specializzare un tipo object generico in un oggetto più specifico:

```typescript
const person : object = {
	name: 'Maximilian',
	age: 30
}

// Questo genera un errore, perchè ci manca informazione sull' object correte
console.log(person.name);

// Notare che stiamo specializzando il tipo object con informazioni sui suoi 
// dati membro
const anotherPerson : {name: string; age :number;} = {
	name : 'Eliot',
	age : 30
}

// Qui invece abbiamo informazioni a sufficienza 
console.log(anotherPerson.name);
```

> [!Hint] In Breve
> Il tipo di dato per oggetti, in TypeScript è ==object==.
> 
> Se si vuole avere accesso al contenuto di oggetti custom, bisogna specificarne la struttura.

***

## Come definisco un array?

Quando vogliamo specificare un array di dati primitivi in TypeScript, basta utilizzare la sintassi:

```typescript
 let hobbies : string[] = [ 'Sports', 'Cooking' ];

 for( const hobby of hobbies ){
	 console.log(hobby.toUpperCase());
 }
```

Oltre ad avere un controllo sul tipo, quando ==itero sugli array tipizzati== ho un check automatico sui metodi che posso oppure non posso utilizzare.

Ad esempio, se ho un array di string => ogni oggetto potrà invocare il metodo toUpperCase().

Invece avendo un array di interi, la chiamata .toUpperCase() genererà un errore.

***

## Come definisco delle Tuple?

Le tuple sono array con una dimensione e tipo fissati (durante la dichiarazione).

> [!Warning] Cosa si intende per tipo fissato
> Ogni elemento dell' array ha un tipo specifico, deciso durante la dichiarazione della tupla.
> 
> Però => i tipi dei singoli dati possono anche non essere omogenei.
> 
> Posso decidere di creare una tupla di 3 stringhe, così come una tupla di un booleano, una stringa ed un intero.
> 

Javascript non supporta nativamente le Tuple, sono consentiti da TypeScript.

```typescript
	const role : [number, string] = [1, 'Captain'];

	// Questo genera un errore in compilazione
	role[0] = 'AnotherRole';
	// Questo invece è corretto
	role[0] = 1;
	
```

*** 

## Come definisco degli enum?

Gli Enum, come le Tuple, non esistono in Javascript.

Possiamo utilizzarle solamente grazie a TypeScript ed il suo step di compilazione intermedio.

```typescript
 enum Role {ADMIN, READ_ONLY, AUTHOR};

 // Utilizzabile in qualsiasi altro punto del codice:
 if( person.role = Role.AUTHOR) {
	 console.log( 'is author');
 }
```

***

## Come attivo il comportamento di default? 

È possibile "disattivare" il type check di Typescript, per alcuni dati.

Per poterlo fare, basta utilizzare il data type "any".

Questo data type, riattiva il comportamento di default di Javascript.

Un dato può quindi contenere qualsiasi cosa, senza produrre errori in compilazione.

È solamente possibile specificare se un dato conterrà un dato singolo (any) oppure un array (any[])

```
const arrayWithoutTypeCheck = ["Hello", 10, true];
```

***

## Union Types

Possiamo dare ad un dato più di un tipo alla volta.

```typescript

function combine ( a : number | string, b : number | string ) {
	return a + b;
}

```

***

## Literal Types 

In questo caso non si deve dare il tipo => ma proprio il valore esatto che un dato deve contenere.

Ad esempio:

```typescript
const tempMeasure : 'fahrenheit' | 'celsius' = 'celsius';

// In questo caso stiamo dicendo che la variabile tempMeasure deve contener uno
// tra i valori specificati
```

I literals sono particolarmente utili quando ci si aspetta un determinato input a funzione. Ad esempio: 

```typescript
function printTemperature
(
	value : number,
	conversionFactor : 'celsius' | 'fahrenheit'
) 
{
	// Qui dentro sono sicuro che il fattore di conversione passato
	// che è una stringa, conterrà o il valore celsius, o il valore fahrenheit
	// qualsiasi altro valore passato erroneamente, genererà un errore 
}
```

***

## Aliases 

Possiamo creare un type alias, così come possiamo farlo in C++.

Basta utilizzare la keyword ==type== .

```typescript
type conversionFactor = 'celsius' | 'fahrenheit';

// ora, la funzione di prima diventa: 
function printTemperatur (value: number, conversionFactor : conversionFactor ) {} 

```

Ancora più utile per creare Alias di tipi complessi.

```typescript
1. type User = { name: string; age: number };
2. const u1: User = { name: 'Max', age: 30 }; // Funziona!
```

***

## Return delle funzioni

(:type) occhio a void => non ritorna nulla.

*** 

## Funzioni e Callbacks

Possso specificare che una variabile conterrà una funzione nel seguente modo:

```typescript
let variableContainingFunction : () => void ;
let variableContainingFunction : (input : string) => boolean ;
```

Possiamo passare una funzione come argomento, seguendo questa stessa logica:

```typescript
function AddAndHandler (n1: number, n2: number, cb : (num : number) => void);
```

***

## Unknown Type

È un segnaposto. Possiamo inserire qualsiasi valore dentro una variabile dichiarata unknown.

È più restrittivo di any. Per andare a riassegnare un valore unknow con un' altra variabile, siamo forzati a fare un controllo sul tipo.

```typescript
let userInput : unknown;
let userName : string;

if(typeof userInput === 'string') {
	userName = userInput;
}
```

È preferibile ad any perchè forza il type check.

***

## Never 

```typescript
function infiniteLoop(): never {
    while (true) {
        // Loop infinito
    }
}

function throwError(message: string): never {
    throw new Error(message);
}
```

Viene utilizzato in situazioni specifiche:

- loop infiniti
- eccezioni
- casi "trappola" negli switch

I dati o le funzioni dichiarate con never non vengono mai raggiunte (o non dovrebbero mai essere raggiunte).

```typescript
type Animal = 
    | { type: 'dog'; bark: () => void }
    | { type: 'cat'; meow: () => void };

function handleAnimal(animal: Animal) {
    switch (animal.type) {
        case 'dog':
            animal.bark();
            break;
        case 'cat':
            animal.meow();
            break;
        default:
            // Qui il tipo di animal dovrebbe essere never
            // poiché abbiamo già coperto tutti i casi
            const _exhaustiveCheck: never = animal;
            throw new Error(`Tipo non supportato: ${_exhaustiveCheck}`);
    }
}
```

***
