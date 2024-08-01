---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - "#Algoritmi/LCS_introduzione_problema"
  - Programmazione_dinamica
  - LCS
---
- [[#Motivazione dell' algoritmo LCS]]
- [[#Qual è l' istanza della LCS?]]
- [[#Qual è la soluzione della LCS?]]

# Motivazione dell' algoritmo LCS

LCS sta per Longest-Common-SubSequence. Serve per trovare le sotto-sequenze comuni (a n sequenze) più lunga possibile.

Si applica (per esempio) per confrontare sequenze di DNA.

Trovando la sotto-sequenza comune a due sequenze di DNA posso determinare quanto due organismi siano simili o meno.

***

# Qual è l' istanza della LCS?

> ***L' istanza non è altro che l' INPUT consumato dall'algoritmo***.

Nel caso della LCS sono le sequenze da confrontare. Possiamo dire che l'istanza di una LCS è:

> [!Summary] In Breve:
> Almeno due sequenze: $X=<x_1,x_2, ... , x_m>$ e $Y=<y_1, y_2, ... , y_n>$

***

# Qual è la soluzione della LCS?

La soluzione è $Z$ sotto-sequenza di $X$ ed $Y$ (sequenze) tale che:

> [!Summary] In Breve:
> $|Z| = max\{ |W| \text{ t.c W è sotto-sequenza di X ed Y } \}$

***
