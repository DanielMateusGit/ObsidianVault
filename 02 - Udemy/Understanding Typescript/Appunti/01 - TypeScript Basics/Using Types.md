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
