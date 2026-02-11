---
tags:
  - Algoritmi
  - Algoritmi/FW
  - Algoritmi/FW/Introduzione
---

# Introduzione a Floyd Warshall

- [[#Qual è l' istanza?|Qual è l' istanza?]]
- [[#Qual è la soluzione?|Qual è la soluzione?]]
- [[#Quali sono le prestazioni dell' algoritmo?|Quali sono le prestazioni dell' algoritmo?]]
- [[#Esempio di calcolo|Esempio di calcolo]]
***

## Spiegazione in breve

Dato un grafo:

- Orientato
- Pesato
- Senza cicli negativi

L' algoritmo Floyd-Warshall calcola tutti i cammini minimi tra ogni coppia di vertici.

***

## Qual è l' istanza?

Il grafo: $G = (V, E)$

E la funzione peso associata ad ogni arco così definita:

$$
\begin{equation}
\quad \omega : E \rightarrow \mathbb{R}^{+} \quad \text{t.c.} \quad 
\omega_{ij} =
\begin{cases}
    0 & \text{se } i = j \\
    \omega(i,j) & \text{se } i \neq j \text{  and  } (i,j) \in E \\
    \infty & \text{se } i \neq j, \text{  and  } (i,j) \notin E
\end{cases}
\end{equation}
$$

***

## Qual è la soluzione? 

Definizione delle variabili:

$\pi_{i,j}$ = cammino minimo da i a j, se esiste
$C_{i,j}$ = costo del cammino minimo da i a j

***

## Quali sono le prestazioni dell' algoritmo?

***

## Esempio di calcolo

***
