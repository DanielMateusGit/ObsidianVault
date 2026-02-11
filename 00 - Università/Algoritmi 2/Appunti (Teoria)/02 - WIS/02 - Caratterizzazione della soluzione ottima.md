---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - WIS
  - Programmazione_dinamica
  - Algoritmi/WIS/Caratterizzazione_soluzione_ottima
---

- [[#Quali sono i sotto-problemi dell' algoritmo WIS?|Quali sono i sotto-problemi dell' algoritmo WIS?]]
- [[#Che forma ha la proprietà della sotto-struttura ottima di WIS?|Che forma ha la proprietà della sotto-struttura ottima di WIS?]]
- [[#Come si dimostra la proprietà di sotto-struttura ottima di WIS?|Come si dimostra la proprietà di sotto-struttura ottima di WIS?]]

# Caratterizzazione della soluzione ottima

## Quali sono i sotto-problemi dell' algoritmo WIS?

Essendo in un problema simile alla [[06 - Algoritmo LCS| LCS]], i sotto-problemi si trovano in maniera praticamente identica: riducendo l' istanza.

Considerando l' insieme $X_n = \{1, \dots, n\}$ di attività iniziali, ed $S \subseteq \{1, \dots, n\}$, allora i sotto-problemi sono:

$S_i \subseteq X_i$ tale che: $V(S_i) = \underset{\text{Comp}(A) = \text{true}}{\overset{\text{max}}{A \subseteq X_n}}$ $\{A\}$

> [!Summary] In breve
> Come in LCS, i sotto-problemi sono tutte le riduzioni possibili dell' istanza.

*** 

## Che forma ha la proprietà della sotto-struttura ottima di WIS?

Assumendo di conoscere già le soluzioni di WIS $S_0, S_1 \dots S_n$:

$$
\begin{aligned}
&  \text{ Se } i \in S_i \rightarrow  Si = S_{p(i)} \cup \{i\} \\
&  \text{ Se } i \not\in S_i \rightarrow Si = S_{i-1}
\end{aligned}
$$

> [!Hint] Cosa è $p(i)$?
> $p(i)$ è un' abbreviazione che sta per "Attività compatibile con la corrente, di peso maggiore".

Ricordiamo dal [[Processo di sviluppo di un algoritmo dinamico]] che stiamo supponendo già risolti i sotto-problemi, e stiamo semplicemente spiegando come è stata calcolata una soluzione ==già trovata==.

Spiegazione:

Quando prendo in considerazione il problema $S_i$ sto in realtà:

Considerando la migliore soluzioni presi i primi $i$ intervalli.

Dato che io conosco già la soluzione, guardandola e guardando il mio $i$-esimo intervallo mi posso trovare solo in due situazioni:

- L' intervallo che sto valutando si trova nella soluzione
- L' intervallo che sto valutano non si trova nella soluzione

E posso anche dire come è stato trovato, rispetto alle altra soluzioni di indice $j<i$ .

***

## Come si dimostra la proprietà di sotto-struttura ottima di WIS? 

***

// PDF di john ha una buona spiegazione 
