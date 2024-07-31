---
tags:
  - "#Algoritmi"
  - LCS
  - Algoritmi/LCS
  - Programmazione_dinamica
aliases: []
---

#Algoritmi/LCS_Concetti_propedeutici

Cosa si intende per sequenza? Fai un esempio semplice
;
Dato un alfabeto $\Sigma$, una **sequenza su $\Sigma$** è una tupla di simboli $X = \langle x_1, x_2, \ldots, x_n \rangle$ dove per ogni $\forall i \in[1,n]$ si ha che $x_i$ appartiene a $\Sigma$.
***
Esempio: $\Sigma$ = "Lettere dell' alfabeto" e $X = \{c, i ,a, o\}$

Cosa si intende per sotto-sequenza? Fai un esempio ed un esempio "sbagliato" di sotto-sequenza.
;
Data una sequenza $X=<x_1,x_2, ... X_m>$, la tupla $Z=<z_1,z_2,...z_k>$ è sotto-sequenza di $X$ sse:
***
$\exists$ **==una sequenza strettamente crescente di indici di X==** $I = <i_1, i_2, ..., i_k>$ tale che $\forall j \in [1,k]$ $Z_j=X_{ij}$
***
Esempio:
$X=<a, b, c, b, d, a, b>$ e $Z=<b, c, b, d>$.
Esiste una sequenza di indici $I=<2,3,5,7>$.
***
$J=<c, c>$ invece non è una sotto-sequenza
$K=<d, c>$ nemmeno è una sotto-sequenza
In entrambe i casi non abbiamo una sequenza di indici  strettamente crescente.

Cosa si intende per prefisso di una sequenza? Fare un esempio.
;
Data una sequenza $X = <x_1, x_2, ... x_n>$ ed un indice $i\in[1,n]$, viene chiamata prefisso di $X$, la ==sotto-sequenza fatta dai primi i simboli di X==. 
***
Esempio:
Il Prefisso $X_4$ della sequenza $X=<a,b,c,b,d,a,b>$ è la sotto-sequenza: $X_4=<a,b,c,b>$


