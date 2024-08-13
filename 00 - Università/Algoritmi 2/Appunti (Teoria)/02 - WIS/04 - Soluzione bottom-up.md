***
- [[#Quale struttura dati viene utilizzata?|Quale struttura dati viene utilizzata?]]
- [[#Come viene calcolato il valore di ogni cella?|Come viene calcolato il valore di ogni cella?]]
- [[#Come risulta l' algoritmo bottom-up? Quali sono i suoi consumi in termini di tempo e spazio?|Come risulta l' algoritmo bottom-up? Quali sono i suoi consumi in termini di tempo e spazio?]]
***

## Quale struttura dati viene utilizzata?

***

Abbiamo visto nella[[03 - Soluzione ricorsiva | soluzione ricorsiva]]  che per "decidere quale intervallo prendere" nel caso passo, dobbiamo fare un confronto ==tra i valori complessivi associati a due sotto-insiemi.==

La soluzione del problema invece è un sotto-insieme dell' insieme iniziale.

Abbiamo quindi due elementi in gioco: valori associati ai sotto-insiemi, ed i sotto-insiemi stessi.

Per trasformare la soluzione ricorsiva in "programmazione dinamica" ci affidiamo allora al vettore V che riguarda i valori. 

Come in LCS, è più importante definire una struttura dati che possa contenere il valore che serve per "prendere le decisioni nella ricorsione".

La combinazione degli intervalli (che è la soluzione effettiva_ , potrà essere ricostruita a partire da questo vettore.

> [!Hint] In breve:
> Utilizzo un vettore V per memorizzare il valore associato alla soluzione di ogni sotto-problema.

***

## Come viene calcolato il valore di ogni cella?

Il corrispettivo delle [[Soluzione ricorsiva | equazioni ricorsive]] trovate in precedenza:

$$
S_i = 
\begin{cases} 
S_{i-1} & \text{se } V(S_{i-1}) \geq V(S{p_i}) + v_i \\
S_{p_i} \cup \{i\} & \text{altrimenti}
\end{cases}
$$

All' interno di un vettore non è altro che:

- M[i-1] è l' ottimo trovato fino ad ora senza la soluzione corrente
- M[p(i)] + v(i) è il valore della possibile soluzione che include l' intervallo che si sta valutando attualmente.

Ed il massimo valore tra questi due sarà il nuovo valore della cella.

***

## Come risulta l' algoritmo bottom-up? Quali sono i suoi consumi in termini di tempo e spazio?

```
WIS() {
    M[0] = 0
    for i = 1 to n do
        M[i] = max(M[p[i]] + v[i], M[i-1])
    return M
}
```

Tempo computazionale: $O(n)$

Spazio occupato: $O(n)$

***
