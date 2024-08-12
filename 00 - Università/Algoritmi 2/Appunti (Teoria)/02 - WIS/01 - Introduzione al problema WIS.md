---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - WIS
  - Programmazione_dinamica
  - Algoritmi/Programmazione_dinamica
---
- [[#Perchè parliamo di WIS?|Perchè parliamo di WIS?]]
- [[#Esempio di soluzione del problema|Esempio di soluzione del problema]]
- [[#Quale è l' istanza del problema?|Quale è l' istanza del problema?]]
- [[#Qual è la soluzione del problema?|Qual è la soluzione del problema?]]

# Introduzione al problema WIS

## Perché parliamo di WIS?

WIS sta per ==Weightened Interval Scheduling==, ed è un algoritmo simile ad[[06 - Algoritmo LCS | LCS]].

È un buon esercizio per continuare ad esplorare il [[Processo di sviluppo di un algoritmo dinamico]].

Il problema è definito come segue:

> Dato un insieme di attività, ordinate temporalmente, vogliamo trovare un sotto-insieme di attività mutualmente compatibili di valore massimo. 


> [!Note] In breve 
> Il concetto di attività lo abbiamo già approfondito in [[00 - Università/Algoritmi 2/Appunti (Teoria)/02 - WIS/00 - Concetti propedeutici|00 - Concetti propedeutici]].
> 
> Un' attività corrisponde all' esecuzione di un "job" o "processo", che porta con sè un determinato "valore". 
> 
> Ogni attività è collocata in un intervallo temporale. 
> 
> Noi stiamo schedulando le migliori attività da portare a termine per ottenere il miglior "valore" prodotto dallo svolgimenti di esse.

***

## Esempio di soluzione del problema

![[Pasted image 20240812134117.png | 500]]

Questo è un esempio in cui ho 7 attività, ognuna con il suo peso e che vive in un' intervallo di tempo espresso in secondi.

La soluzione a questo esempio sarebbe l' insieme $S=\{1, 7\}$ che hanno un valore complessivo di 28.

***

## Quale è l' istanza del problema?

L' istanza del problema WIS è data dal numero $n$ di attività (che individua l' insieme $\{1,2...n\}$ delle attività) e dalle triple associate ad ognuna delle $n$ attività.

La tripla associata ad ogni attività $i$ corrisponde con la precedente definizione di [[00 - Università/Algoritmi 2/FlashCards/WIS/Concetti propedeutici|intervallo pesato]] dato in precedenza.

***

## Qual è la soluzione del problema? 

La soluzione del sotto-problema è il sotto-insieme di attività con valore complessivo massimo.

$S \subseteq \{1, \dots, n\}$ t.c: $V(S) = \underset{\text{Comp}(A) = \text{true}}{\overset{\text{max}}{A \subseteq \{1, \dots, n\}}}$ $\{A\}$

***
