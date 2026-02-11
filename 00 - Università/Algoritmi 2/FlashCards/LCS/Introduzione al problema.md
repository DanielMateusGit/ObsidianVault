---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - LCS
  - Programmazione_dinamica
  - Algoritmi/LCS_introduzione_problema
---
#Algoritmi/LCS/Introduzione_al_problema

Qual è l' istanza della LCS?
;
 ***L' istanza non è altro che l' INPUT consumato dall'algoritmo***.
***
Nel caso della LCS sono le sequenze da confrontare. Possiamo dire che l'istanza di una LCS è:
***
Almeno due sequenze: $X=<x_1,x_2, ... , x_m>$ e $Y=<y_1, y_2, ... , y_n>$

Qual è la soluzione della LCS?
;
La soluzione è $Z$ sotto-sequenza di $X$ ed $Y$ (sequenze) tale che:
***
$|Z| = max\{ |W| \text{ t.c W è sotto-sequenza di X ed Y } \}$
***
Ossia la sotto-sequenza comune di $X$ ed $Y$ con la lunghezza maggiore (tra tutte le possibili sotto-sequenze comuni).
<!--SR:!2024-08-04,4,272-->

Quale è il tempo di esecuzione della LCS e lo spazio occupato nella sua versione dinamica?
;
$O(n×m)$ per il tempo di esecuzione e $O(n×m)$ per lo spazio di memoria.
Nella versione ottimizzata, lo spazio si riduce a $O(min(n,m))$.
