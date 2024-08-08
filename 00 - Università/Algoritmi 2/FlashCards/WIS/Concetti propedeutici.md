---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - WIS
  - Algoritmi/WIS/Concetti_propedeutici
---
#Algoritmi/WIS/Concetti_propedeutici

Cosa si intende per intervallo pesato ai fini dell' algoritmo WIS?
;
Un "intervallo pesato" è: 
- Un intervallo di tempo associato all'esecuzione di un' attività
- Più il "peso" o "valore" associato all'esecuzione di tale attività
Quindi, ad intervallo $i$ è associato:
- $s_i$ => Istante di tempo in cui inizia l' attività 
- $e_i$ => Istante di tempo in cui termina l'attività 
- $v_i$ => Valore associato all' attività 

Come è definita la funzione COMP ai fini dell' algoritmo WIS?
;
È una funzione che controlla che tutte le attività contenute in un insieme siano compatibili temporalmente tra di loro .
***
Dato un insieme di attività $X = \{ 1 ... n \}$, si definisce funzione COMP:
***
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
***

Come è definita la funzione VAL ai fini dell' algoritmo WIS?
;
È una funzione che calcola il valore complessivo di un insieme di Attività.
***
Dato un insieme di attività $X = \{ 1 ... n \}$, si definisce funzione VAL:
***
$VAL$: $\rho(X)\longrightarrow R_+$
$$
v(A) = \begin{cases} \sum_{i \in A} v_i & \quad \text{se } A \ne \emptyset \\ 0 & \quad \text{se } A = \emptyset \end{cases}
$$