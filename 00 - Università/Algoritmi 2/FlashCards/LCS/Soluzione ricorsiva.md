---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Algoritmi/LCS/Soluzione_ricorsiva
  - Programmazione_dinamica
---

#Algoritmi/LCS/Soluzione_ricorsiva 

Come passo dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?
;
 Per passare dalla sotto-struttura ottima ad una formulazione ricorsiva che effettivamente restituisca il risultato sperato, ==bisogna adoperare la ricorsività doppia==.

Quale è la soluzione ricorsiva della LCS?
;
$$
\begin{flalign*}
&c[i,j] = 
\begin{cases}
0 & \text{se } i = 0 \text{ o } j = 0 \\
c[i-1,j-1] + 1 & \text{se } i,j > 0 \text{ e } x_i = y_j \\
\max(c[i,j-1], c[i-1,j]) & \text{se } i,j > 0 \text{ e } x_i \neq y_j
\end{cases} &
\end{flalign*}
$$

Quali variabili si introducono per risolvere la LCS? Perchè?
;
La lunghezza della LCS è il dato che "da direzione" alla formulazione con ricorsione doppia. Nel caso passo della formulazione ricorsiva si sta utilizzando un confronto tra lunghezze.
***
In più le variabili dei problemi di programmazione dinamica, già definibili durante la ricerca della soluzione ricorsiva, ==determinano quale sarà la struttura dati da utilizzare nel momento dell'applicazione dell' algoritmo dinamico.==

Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)
;
**Tempo di esecuzione**: $O(2min⁡(n,m))$
***
```
LCS_R(X,Y,i,j)
	if( i = 0 or j = 0)
		return 0;
	else if( X_i = X_j )
		return LCS_R(X, Y, i-1, j-1) concat X_i;
	else
		L = LCS_R(X, Y, i-1, j);
		R = LCS_R(X, Y, i, j-1);
	if(|L| > |R|)
		return L;
	else
		return R;
```
