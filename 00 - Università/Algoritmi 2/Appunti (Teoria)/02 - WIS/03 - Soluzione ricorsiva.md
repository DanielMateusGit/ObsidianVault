---
tags:
  - Algoritmi
  - Algoritmi/WIS
  - Algoritmi/WIS/Soluzione_ricorsiva
---
# Soluzione ricorsiva

***
- [[#Introduzione di p(i)|Introduzione di p(i)]]
- [[#Quale è la soluzione ricorsiva di WIS?|Quale è la soluzione ricorsiva di WIS?]]
- [[#Qual è l' algoritmo ricorsivo? Come si comporta in termini di tempi?|Qual è l' algoritmo ricorsivo? Come si comporta in termini di tempi?]]
***

## Introduzione di p(i)

==p(i)==

$p(i)$ è un' abbreviazione per qualcosa che abbiamo già definito.

Dato il sotto-problema $S_i$, definiamo $p(i)$ come l' attività di indice minore ad $i$, compatibile e di peso maggiore.

> [!Hint] In breve:
> $p_i$ = {max j | j < i è compatibile con i}

***

## Quale è la soluzione ricorsiva di WIS?

==Caso base:==

$S_0 = \emptyset$

==Caso passo:==

$$
S_i = 
\begin{cases} 
S_{i-1} & \text{se } V(S_{i-1}) \geq V(S{p_i}) + v_i \\
S_{p_i} \cup \{i\} & \text{altrimenti}
\end{cases}
$$

Spiegazione:

Sto valutando se inserire oppure meno l' intervallo di indice $i$ all'interno della mia soluzione.

Se sono nel caso passo possono avvenire solo due cose:

- La soluzione trovata fino ad ora (insieme di intervalli) è migliore della nuova soluzione che l' intervallo in analisi costituisce (intervallo corrente + sotto-insieme di intervalli compatibile).
- La nuova soluzione è migliore di qualsiasi trovata fino ad ora.

Nel primo caso sto "portando avanti" un ottimo trovato in precedenza e migliore di quello realizzabile attualmente.

Nel secondo caso invece ho trovato un intervallo migliore di quello trovato fino ad ora e che costituirà il nuovo ottimo.

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
