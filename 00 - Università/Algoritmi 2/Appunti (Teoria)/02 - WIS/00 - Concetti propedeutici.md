---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - Algoritmi/WIS/Concetti_propedeutici
  - Programmazione_dinamica
  - Algoritmi/Programmazione_dinamica
---
- [[#Cosa si intende per intervallo pesato ai fini dell' algoritmo WIS?|Cosa si intende per intervallo pesato ai fini dell' algoritmo WIS?]]
- [[#Come è definita la funzione COMP ai fini dell' algoritmo WIS?|Come è definita la funzione COMP ai fini dell' algoritmo WIS?]]
- [[#Come è definita la funzione VAL ai fini dell' algoritmo WIS?|Come è definita la funzione VAL ai fini dell' algoritmo WIS?]]

# Concetti propedeutici

## Cosa si intende per intervallo pesato ai fini dell' algoritmo WIS?

Un "intervallo pesato" è: 

- Un intervallo di tempo associato all'esecuzione di un' attività.
  
- Più il "peso" o "valore" associato all'esecuzione di tale attività.

Quindi, ad intervallo $i$ è associato:

- $s_i$ => Istante di tempo in cui inizia l' attività 
- $e_i$ => Istante di tempo in cui termina l'attività 
- $v_i$ => Valore associato all' attività 

> [!Example] Esempio di pratico di intervallo
> Vogliamo realizzare uno schedulatore per processi in C. Questo schedulatore tiene conto del tempo di inizio e fine esecuzione di ogni singolo processo. Ogni processo inoltre, ha associato un valore di consumo della CPU.

***

## Come è definita la funzione COMP ai fini dell' algoritmo WIS?

È una funzione che controlla che tutte le attività contenute in un insieme siano compatibili temporalmente tra di loro. 

Valuta l' insieme della parti dell' insieme iniziali.

Dato un insieme di attività $X = \{ 1 ... n \}$, si definisce funzione COMP:

$COMP$: $\rho(X)\longrightarrow \{true, false\}$

$$
\begin{align*}
\text{COMP}(\rho(X)) = 
\begin{cases} 
\text{True} & \text{se } \forall i,j \in \rho(X) \text{ con } i \ne j, \, [s_i, e_i] \cap [s_j, e_j] = \emptyset \\ 
\text{False} & \text{altrimenti} 
\end{cases}
\end{align*}
$$

Esempio:

***

## Come è definita la funzione VAL ai fini dell' algoritmo WIS?

È una funzione che calcola il valore complessivo di un insieme di Attività.

Dato un insieme di attività $X = \{ 1 ... n \}$, si definisce funzione VAL:

$VAL$: $\rho(X)\longrightarrow R_+$

$$
v(A) = \begin{cases} \sum_{i \in A} v_i & \quad \text{se } A \ne \emptyset \\ 0 & \quad \text{se } A = \emptyset \end{cases}
$$

Esempio:

***
