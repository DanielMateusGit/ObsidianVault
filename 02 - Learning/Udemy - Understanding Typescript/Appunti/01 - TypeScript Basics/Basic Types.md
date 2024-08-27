---
tags:
  - TypeScript
  - TypeScript/Types
  - WebDev
---

# Types

## Core Types 

I "Core Type" sono quelli supportati da Javascript e compatibili con TypeScript. 

Questi sono:

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

## Objects

Con TypeScript possiamo definire una "linea guida" custom che un oggetto deve seguire per passare un nostro type check.

Per definire "tipi diversi dai primitivi", i creatori di TypeScript hanno inventato un tipo specifico: ==object==.

Dichiarando un dato ==object==, stiamo dicendo che questo sarà un oggetto custom e non primitivo.

Non abbiamo però alcuna informazione sull'oggetto: 

 - Non abbiamo informazioni sui metodi che dovrebbe contenere
 - Non abbiamo informazioni sugli attributi che dovrebbe contenere

L' accesso a qualsiasi dato membro di questo oggetto genererà un errore TypeScript.

Il tutto però è risolvibile, specificando in maniera esplicita quali sono gli attributi di questo object:

```typescript
const person : object = {
	name: 'Maximilian',
	age: 30
}

// Questo genera un errore, perchè ci manca informazione sull' object correte
console.log(person.name);

const anotherPerson : {name: string; age :number;} = {
	name : 'Eliot',
	age : 30
}

// Qui invece abbiamo informazioni a sufficienza 
console.log(anotherPerson.name);
```

> [!Hint] In Breve
> Un dato diverso dai tipi primitivi, in TypeScript è un dato ==object==.
> 
> Se si vuole avere accesso al contenuto di oggetto custom, bisogna definirne la struttura.

***

## Arrays Types

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

## Tuples

Le tuple sono array con una dimensione e tipo fissati (durante la dichiarazione).


> [!Warning] Cosa si intende per tipo fissato
> In TypeScript si intende che ogni elemento dell' array ha un tipo specifico, deciso durante la dichiarazione della tupla.
> 
> Questo vuol dire che i tipi dei singoli dati possono anche non essere omogenei.
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

## Enum

Gli Enum, come le Tuple, non esistono in Javascript.

Possiamo utilizzarle solamente grazie a TypeScript ed il suo step di compilazione intermedio.

```typescript
 enum Role {ADMIN, READ_ONLY, AUTHOR};

 // Utilizzabile in qualsiasi altro punto del codice:
 if( person.role = Role.AUTHOR) {
	 console.log( 'is author');
 }
```
