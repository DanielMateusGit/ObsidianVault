---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Algoritmi/Programmazione_dinamica
  - Programmazione_dinamica
  - LCS
  - Algoritmi/LCS/Soluzione_ricorsiva
---
- [[#Soluzione ricorsiva|Soluzione ricorsiva]]
- [[#Come passo dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?|Come passo dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?]]
- [[#Quali variabili si introducono per risolvere la LCS? Perchè?|Quali variabili si introducono per risolvere la LCS? Perchè?]]
- [[#Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)|Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)]]

## Soluzione ricorsiva

## Come passare dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?

La [[Sotto-struttura ottima]] della LCS funziona **==supponendo di aver già trovato la soluzione==**.

Tolta questa premessa, la sotto-struttura ottima risulta insufficiente per trovare la soluzione della LCS:

> [!Missing] Assenza della soluzione $Z$
> Quando il calcolo del sotto-problema non soddisfa le condizioni per il punto (1)  della sotto-struttura, come procede la regola?
> 
> Controlla se $Z_k$ è diverso da $X_m$ oppure $Y_n$, e continua a risolvere i sotto-problemi prodotti da uno di questi due casi (il caso 2 e 3).
> 
> Ma attenzione! Senza $Z_k$ (che non è stata calcolata veramente) ==questa operazione risulta impossibile.==
> 

> In questo caso, per passare dalla sotto-struttura ottima ad una formulazione ricorsiva che effettivamente restituisca il risultato sperato, ==bisogna adoperare la ricorsività doppia==.

Una volta stabilito che $X_n$ $\neq$ da $Y_m$ e che quindi il simbolo $S = X_n = Y_m$ non farà parte della soluzione, quale sarà la soluzione del sotto-problema tra le due scelte rimanenti?

> [!Hint] Soluzione
> Facile! Quella che restituisce la Lunghezza più lunga tra le due opzioni: $S^{i,j} = max \{S^{i-1,j}, S^{i, j-1} \}$


> [!Question] A cosa serve allora la sotto-struttura ottima?
> La sotto-struttura ottima è un "passaggio" che porta chi progetta un algoritmo a capire che la programmazione dinamica è applicabile su un dato problema.
> 

 ==Non vuole risolvere il problema==, ma bensì dimostrare che questo gode di una proprietà sfruttabile per arrivare al risultato in un certo modo (tramite programmazione dinamica).

---

# Quale è la soluzione ricorsiva della LCS?

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

con $c$ lunghezza della LCS considerando $i$ simboli di $X$ e $j$ simboli di $Y$

> [!Warning] Problema ausiliario delle lunghezze
> Stiamo introducendo la variabile c del sotto-problema "Trova la LUNGHEZZA della più lunga sotto-sequenza comune tra X ed Y"

---

## Quali variabili si introducono per risolvere la LCS? Perchè?

Nella soluzione ricorsiva delle LCS si introduce la variabile c, che non rappresenta direttamente la soluzione della LCS, ma la ==*lunghezza della soluzione della LCS.*== 

Perchè si introduce questa variabile? 

Semplicemente perchè la lunghezza della LCS è il dato che "da direzione" alla ricorsione doppia. Nel caso passo della formulazione ricorsiva si sta utilizzando un confronto tra lunghezze.

I simboli della LCS sono invece secondari, perchè ricavabili a fine esecuzione ([[Processo di sviluppo di un algoritmo dinamico | durante la fase di ricostruzione della soluzione.]])

In più le variabili dei problemi di programmazione dinamica, già definibili durante la ricerca della soluzione ricorsiva, ==determinano quale sarà la struttura dati da utilizzare nel momento dell'applicazione dell' algoritmo dinamico.==

---

## Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)

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

**Tempo di esecuzione**: $O(2min⁡(n,m))$, dove n e m sono le lunghezze delle due stringhe. Il tempo è esponenziale. L' albero delle chiamate ricorsive risulta:

```
LCS_R(X, Y, 3, 2)     // 'C' != 'C'
   ├── LCS_R(X, Y, 2, 2)    // 'B' != 'C'
   |    ├── LCS_R(X, Y, 1, 2)  // 'A' == 'C'
   |    |    ├── LCS_R(X, Y, 0, 1) = 0
   |    |    └── LCS_R(X, Y, 1, 1)  // 'A' == 'A'
   |    |         └── LCS_R(X, Y, 0, 0) = 0
   |    └── LCS_R(X, Y, 2, 1)   // 'B' != 'A'
   |         ├── LCS_R(X, Y, 1, 1)  // già risolto sopra
   |         └── LCS_R(X, Y, 2, 0) = 0
   └── LCS_R(X, Y, 3, 1)    // 'C' != 'A'
        ├── LCS_R(X, Y, 2, 1)  // già risolto sopra
        └── LCS_R(X, Y, 3, 0) = 0
```
