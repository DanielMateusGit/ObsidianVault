---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - "#Algoritmi/LCS_introduzione_problema"
  - Programmazione_dinamica
  - LCS
---
- [[#Motivazione dell' algoritmo LCS|Motivazione dell' algoritmo LCS]]
- [[#Esempio di calcolo della LCS tra due sequenze|Esempio di calcolo della LCS tra due sequenze]]
- [[#Qual è l' istanza della LCS?|Qual è l' istanza della LCS?]]
- [[#Qual è la soluzione della LCS?|Qual è la soluzione della LCS?]]
# Introduzione al problema LCS

## Motivazione dell' algoritmo LCS

LCS sta per Longest-Common-SubSequence. Serve per trovare la sotto-sequenza comune (a n sequenze) più lunga possibile.

Si applica (per esempio) per confrontare sequenze di DNA.

Trovando la sotto-sequenza comune a due sequenze di DNA posso determinare quanto due organismi siano simili o meno.

---
## Quale è il tempo di esecuzione della LCS e lo spazio occupato nella sua versione dinamica?

$O(n×m)$ per il tempo di esecuzione e $O(n×m)$ per lo spazio di memoria.
Nella versione ottimizzata, lo spazio si riduce a $O(min(n,m))$.

---

## Esempio di calcolo della LCS tra due sequenze

$X =<a, b, c, b, d, a ,b>$ di lunghezza 7.

$Y=<b,d,c,a,b,a>$ di lunghezza 6

$<b,c,a,b>$ è sotto-sequenza di X ed Y ed ha lunghezza 4. È una soluzione della LCS.

$<b,d,a,b>$ è sotto-sequenza di X ed Y ed ha lunghezza 4. È una soluzione della LCS.

<b,c,a> è sotto-sequenza di X ed Y, ma non avendo la lunghezza massima possibile, non è una soluzione della LCS.

***

## Qual è l' istanza della LCS?

> ***L' istanza non è altro che l' INPUT consumato dall'algoritmo***.

Nel caso della LCS sono le sequenze da confrontare. Possiamo dire che l'istanza di una LCS è:

> [!Summary] In Breve:
> Almeno due sequenze: $X=<x_1,x_2, ... , x_m>$ e $Y=<y_1, y_2, ... , y_n>$

***

## Qual è la soluzione della LCS?

La soluzione (o le soluzioni) è ogni $Z$, sotto-sequenza di $X$ ed $Y$, (sequenze) tale che:

> [!Summary] In Breve:
> $|Z| = max\{ |W| \text{ t.c W è sotto-sequenza di X ed Y } \}$

***
