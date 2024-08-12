---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - Algoritmi/WIS/Soluzione_ricorsiva
---

# Soluzione ricorsiva

***
- [[#Introduzione di OPT e p(i)|Introduzione di OPT e p(i)]]
- [[#Quale è la soluzione ricorsiva di WIS?|Quale è la soluzione ricorsiva di WIS?]]
- [[#Vengono introdotte nuove variabili per la soluzione ricorsiva di WIS? Perchè?|Vengono introdotte nuove variabili per la soluzione ricorsiva di WIS? Perchè?]]
- [[#Qual è l' algoritmo ricorsivo? Come si comporta in termini di tempi?|Qual è l' algoritmo ricorsivo? Come si comporta in termini di tempi?]]
***

## Introduzione di OPT e p(i)

==OPT==

Per parlare della soluzione ricorsiva di WIS, dobbiamo prima definire una variabile-soluzione $OPT$ associata ad ogni soluzione $S_i$.

Dato un qualsiasi problema di WIS, la sua soluzione sarà un sotto-insieme di intervalli $S_i$ ed $OPT(S_i)$ sarà il valore associato a tale insieme. 

$OPT$ è fondamentale perchè sposta il focus del problema al confronto di valori numerici, anche se la soluzione finale sarà un sotto-insieme di tutti gli intervalli iniziali.

==p(i)==

$p(i)$ è invece un' abbreviazione per qualcosa che abbiamo già definito. Dato il sotto-problema $S_i$, definiamo $p(i)$ come l' attività di indice minore ad $i$, compatibile a quella corrente e di peso maggiore.

> [!Hint] In breve:
> $OPT_i = V(S_i)$
> $p_i$ = {max j | j < i è compatibile con i}

***

## Quale è la soluzione ricorsiva di WIS?

==Caso base:==

$OPT_0 = 0$

==Caso passo:==

$$
S_i = 
\begin{cases} 
S_{i-1} & \text{se } OPT_{i-1} \geq OPT_{p_i} + v_i \\
S_{p_i} \cup \{i\} & \text{altrimenti}
\end{cases}
$$

***

## Qual è l' algoritmo ricorsivo? Come si comporta in termini di tempi?

```
procedure WISRIC(i)
    if i = 0 then
        return (0, ∅)
    else
        (V1, S1) ← WISRIC(i - 1)
        (V2, S2) ← WISRIC(p(i))
        V2 ← V2 + vi
        if V1 ≥ V2 then
            return (V1, S1)
        else
            return (V2, S2 ∪ {i})
```

Tempo esponenziale: $O(2^n)$

***
