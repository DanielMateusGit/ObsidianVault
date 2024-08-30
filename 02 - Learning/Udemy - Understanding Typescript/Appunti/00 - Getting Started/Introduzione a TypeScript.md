---
tags:
  - TypeScript/Intro
  - TypeScript
  - WebDev
---

# Introduzione a TypeScript

- [[#Cosa è TypeScript?|Cosa è TypeScript?]]
- [[#Perchè si utilizza? Semplice esempio.|Perchè si utilizza? Semplice esempio.]]
- [[#Come si installa Typescript?|Come si installa Typescript?]]
 
***

## Cosa è TypeScript?

TypeScript è un **==_superset_==** di JavaScript che aggiunge tipizzazione statica e caratteristiche avanzate come classi e interfacce, migliorando la manutenzione del codice Javascript.

> [!Hint] In breve
> È un' estensione del linguaggio Javascript.
> 
> ![[Pasted image 20240826094715.png | 500]]

> [!Warning] TypeScript non è un linguaggio di programmazione
> TypeScript da solo non può essere eseguito dal Browser (o da NodeJS). 
> TypeScript è un "tool che aggiunge po' di sintassi e feature a Javascript". 
> 
> Un documento TypeScript dovrà sempre essere compilato in un file finale Javascript, che sarà invece utilizzabile.
> 

***

## Perchè si utilizza? Semplice esempio.

Permette di prevenire tutti i comportamenti indesiderati generati dalla mancanza di tipizzazione in Javascript.

Aggiunge altre features che portano Javascript ad essere più simile ai linguaggi di alto livello tradizionali. Le principali funzionalità che aggiunge a Javascript sono:

- Tipizzazione,
- Interfacce e Codice generico
- Meta-programmazione (come i decoratori)
- Tooling 

```typescript
function addIntegers(a, b) {
	return a + b;
}

// Senza una tipizzazione dei dati, questo comportamento:
console.log(addIntegers('2', '3'));

// Questo non lancia alcuna eccezione da Javascript perchè tecnicamente è giusta.
// È il programmatore che ha compiuto (senza accorgersene) un errore PURAMENTE LOGICO.
// Con Vanilla JS si potrebbe fare un type check dentro la funzione, lanciare un' 
// eccezione in caso di tipo errato etc...
// MA TYPESCRIPT permette di rilevare questo errore in maniera più intelligente 

// IL codice TypeScript corrispondente alla funzione sopra sarebbe il seguente:
function addInteger( a : number, b : number ) : number {
	return a + b;
}

// In questo modo, quando si compilerà il codice da ts => js
console.log(addIntegers('2', '3'));  // => questo lancerà un errore 

```

*** 

## Come si installa Typescript?

Per installare e compilare TypeScript:

```bash
npm install -g typescript
tsc helloworld.tsc
```

Il codice TypeScript vive in file con estenzione .ts

***
