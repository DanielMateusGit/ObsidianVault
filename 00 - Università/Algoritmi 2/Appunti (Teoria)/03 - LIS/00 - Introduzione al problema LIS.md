---
tags:
  - Algoritmi
  - Algoritmi/LIS
  - LIS
  - Programmazione_dinamica
  - Algoritmi/Programmazione_dinamica
  - Algoritmi/LIS_Introduzione_problema
---
- [[#Qual è l' istanza della LCS?|Qual è l' istanza della LCS?]]
- [[#Qual è la soluzione della LCS?|Qual è la soluzione della LCS?]]
- [[#Esempio di calcolo|Esempio di calcolo]]

# Introduzione al problema LIS

## Descrizione in breve:

LIS sta per Longest Increasing Subsequence. 

Serve per trovata una (tra le tante) sotto-sequenze tale che:

- La sotto-sequenza contiene elementi ordinati in ordine crescente
- La sotto-sequenza ha lunghezza massima 

Anche questo è un algoritmo simil-LCS.

***

## Qual è il tempo di esecuzione della LIS e lo spazio occupato, nella sua versione dinamica? 

$O(m^2)$ è il tempo di esecuzione e $\Theta(m)$ lo spazio di memoria.

***

## Esempio di calcolo

$X = <6,4,7,3,5,9,11,8>$ è la sequenza iniziale,  e le sue LIS :

$S_1 = <6,7,9,11>$

$S_2 = <3,5,9,11>$

$etc...$

***

## Qual è l' istanza della LIS?

L' istanza dell' algoritmo LIS è una sequenza $X$ di $m$ numeri interi.

***

## Qual è la soluzione della LIS?

La soluzione è ==una tra le più lunghe sotto-sequenze crescenti== della sequenza data come istanza del problema.

> [!NOTE] Ho molteplici soluzioni!
> Rispetto ad altri problemi in cui la soluzione è univoca, in questo caso l' unica cosa che mi importa è che la sotto-sequenza trovata rispetti una certa policy (che i numeri in essa siano crescenti) e che sia di lunghezza massima.

***
