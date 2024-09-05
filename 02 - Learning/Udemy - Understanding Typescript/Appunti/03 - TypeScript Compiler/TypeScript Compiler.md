---
tags:
  - TypeScript
---
# Typescript Compiler

## Usare watch mode 

Per ascoltare i cambiamenti in un file, invece di ricompilare ogni volta:

```
tsc nomefile.tsx --watch
```

***

## Inserire TypeScript in un progetto

==tsc --init== configura un progetto TypeScript.
Lanciando il comando, verrà creato il file tsconfig.json

Aggiungendo questo file ad una cartella principale di progetto:

```
tsc
```

Il comando tsc andrà a compilare tutti i file TypeScript della cartella di progetto.

Usando tsc con --watch invece, abiliteremo la compilazione automatica di tutti i file TypeScript.

***
## Includere ed Escludere file

Dentro il file json tsconfig.json, possiamo aggiungere:

```json
"exclude" : [
	"*.dev.ts",
	"node_modules"
],

"include" : [

]
```

Questo escluderà i file specificati, dalla compilazione.
Una decisione sensata (e molto comune) è quella di non compilare i node_modules.

Include è simmetrico.

***

## Compilation Target

L' opzione target serve per specificare "per quale versione di Javascript" deve essere compilato il codice.

```json
"target" : "es5"
```

Possiamo decidere quale è "il nostro target" cambiando questa opzione, valutando "quando retro-compatibile" vogliamo rendere il risultato della compilazione del nostro codice.

***

## TypeScript core libs 

L' opzione lib permette di specificare quali feature JavaScript (librerie) utilizzeremo nel progetto corrente.

Se non è specificato alcun valore, verranno attivate tutte le librerie della versione JavaScript specificata in "target" e "modules".

```json
"target" : "es6",
"module" : "commonjs",
"lib" : [
	"dom"
]
```

Per esempio in questo caso, si prende solo la libreria per la manipolazione del dom della versione es6 di javascript.

***

## SourceMap (debugging)

Settando source map a true, dopo la compilazione verranno creati dei file con esetension js.map 

Questi file servono al browser per poter vedere da console (in sources) anche i file typescript.

In questo modo è possibile debuggare direttamente i file typescript e non solo i js compilati.

***

## outDir e rootDir

Opzioni che servono per organizzare il fs di progetto.

Con OutDir possiamo specificare la posizione in cui vogliamo trovare i nostri compilati.

Con src invece possiamo specificare la cartella sorgente da cui prendere i file da compilare.


```json
"outDir" : "./dist"
"rootDir" : "./src"
```

***


## Strict compilation e Code Quality Options

Sono opzioni per il type-checking. (leggere doc, sono tanti).
Ci sono anche "Additional Check" che controllano la qualità del codice.


***

## Debugging with Visual Studio Code 

ESLint => aggiunge un controllo sintattico
Pretties => aggiunge formattazione
Debugger for Chrome => Permette di debuggare codice anche internamente a VSCode

Si può mettere un breakpoint dentro il codice vs code => attivare sourceMap: truee successivamente andae in debug / Chrome (con ctrl + p).

In questo modo può essere lanciato tutto il codice in una cartella specificata,in locale.

***


