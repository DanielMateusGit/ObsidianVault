---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Algoritmi/LCS/Soluzione_bottom_up
  - LCS
---
- [[#Come passare dalla soluzione ricorsiva alla soluzione dinamica?|Come passare dalla soluzione ricorsiva alla soluzione dinamica?]]
- [[#Che forma ha la matrice di supporto della LCS?|Che forma ha la matrice di supporto della LCS?]]
- [[#Come si calcola il valore di ogni cella?|Come si calcola il valore di ogni cella?]]
- [[#Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?|Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?]]

# Soluzione Bottom-up per LCS

## Come passare dalla soluzione ricorsiva alla soluzione dinamica?

Alla terza delle [[Processo di sviluppo di un algoritmo dinamico | quattro fasi del processo di sviluppo]] di algoritmi dinamici:

- È stata trovata una soluzione ricorsiva per l' algoritmo.
- È stata trovata la "variabile" che descrive i dati importanti per il calcolo del problema.
- Sono nati eventuali problemi ausiliari.

Il passaggio successivo è quello di salvare i risultati parziali prodotti dalla soluzione ricorsiva in una struttura dati, in modo da ==riciclare tutte le informazioni già calcolate==.

Nella LCS, abbiamo trovato come variabile: 

$C_{i,j}$ come la "lunghezza della sotto-sequenza comune più lunga tra i prefissi $X_i$ di $X$ ed $Y_j$ di $Y$."

Che sposta il focus dal problema della LCS ad un suo sotto-problema ausiliare:

==Ora stiamo cercando e confrontando lunghezze di sequenze e sotto-sequenze.==

La struttura che useremo per la LCS, dato che dobbiamo salvare un dato bi-dimensionale ($C_{i,j}$) sarà una Matrice $m*n$.

> [!Summary] In breve:
> La risposta alla domanda originale sarebbe : introduciamo una struttura dati di supporto per salvare i risultati dei sotto-problemi dell' algoritmo.

---

## Che forma ha la matrice di supporto della LCS?

Date le sequenze $X$ ed $Y$, la matrice:

- Avrà come numero di righe la lunghezza di X.
- Avrà come numero di colonne la lunghezza di Y.
- Ogni riga/colonna rappresenterà un indice della sequenza a cui è associata.
- Ogni cella $C_{i,j}$ corrisponderà alla "Lunghezza della LCS più comune più lunga prendendo i primi $i$ simboli da $X$ ed i primi $j$ simboli da $Y$".
- Il valore di ogni cella $C_{i,j}$ sarà calcolato a partire da un caso base della formulazione ricorsiva, o dalle celle calcolate in precedenza.
- Il Calcolo delle celle procede in ordine di lettura della matrice.
---

## Come si calcola il valore di ogni cella?

Questo è un esempio di matrice della LCS (già computata), con $X = <A, B, C, B, D, A , B>$ ed $Y =<B, D, C, A, B, A>$:

![[Pasted image 20240804095254.png | 350]]

> [!Hint] 
> I simboli $\epsilon$ corrispondono al simbolo nullo.
> 
>  Tutti i numeri in rosso sono stati calcolati con il "caso passo" in versione dinamica. 
>  
>  I numeri in blu, sono calcolati invece con il caso base in cui trovo due simboli uguali. 
>  
>  I numeri in verde sono calcolati con il caso base in cui una delle due sotto-sequenze è vuota.
>  

==Come utilizzare la struttura?==

> Una volta definita la struttura di supporto, dobbiamo riuscire ad utilizzare  i casi della ricorsione per calcolare ogni elemento della struttura dati.

In questo caso gli elementi son le celle $C_{i,j}$.

Ogni cella contiene il valore della Lunghezza della più lunga sotto-sequenza comune ad $X$ ed $Y$, considerato solo i primi $i$ e $j$ simboli.

> [!Example] Ad esempio $C_{3,3}$
> Contiene la lunghezza della più lunga sotto-sequenza comune ai due prefissi $X_3=<A, B, C>$ ed $Y_3=<B,D,C>$.

I casi della ricorsione sono quindi:

- Caso Base: $0 \text{ se } i = 0 \text{ o } j = 0$ 
  
>   Corrisponde a tutte le celle della matrice che hanno $i=0$ oppure $j=0$. In questo caso sto prendendo i simboli solo da una delle due sequenze (quindi la sotto-sequenza ==comune sarà vuota==).
  
- Il Caso Base: $c[i-1,j-1] + 1 \text{ se } i,j > 0 \text{ e } x_i = y_j$ 
  
>   Se trovo un simbolo in posizione $i$ (che risulta uguale al simbolo in posizione $j$), ***allora prendo la LCS più lunga fino a $i-1$ e $j-1$ ed aggiungo + 1 nella posizione corrente.*** 
>   
>   Nella matrice, $C_{i,j}$ = $C_{i-1, j-1}$ + 1.
  
- Il Caso Passo: $\max(c[i,j-1], c[i-1,j]) \text{ se } i,j > 0 \text{ e } x_i \neq y_j$
  
>   Se invece, trovandomi in posizione $C_{i,j} i simboli corrispondenti agli indici risultano diversi, allora devo portare avanti la soluzione migliore tra:
>   
>   - LCS non considerando 1 simbolo di $X$, che si traduce in $C_{i-1,j}$
>   - LCS non considerando 1 simbolo di Y, che si traduce in $C_{i,j-1}$
>     
>     Nella matrice, $C_{i,j}$ = $\max\{C_{i-1,j},C_{i,j-1}\}$

> [!Tip] In Sostanza:
> Quella che viene fatta, è una traduzione da formula ricorsiva a operazioni su matrice.
> 
> Tutto ciò che è una sotto-chiamata ricorsiva nella formulazione, corrisponde ad un accesso a cella in matrice. 
> 
> Questo avviene perchè quello che devo "calcolare ancora tramite la ricorsione", con la matrice di supporto lo ho già precedentemente calcolato e salvato.

Il seguente, è un disegno esplicativo del calcolo della singola cella:

![[Pasted image 20240804105550.png | 400]]

----

## Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?

**Tempo di esecuzione**: $O(n×m)$
    - Per ogni coppia di indici $(i,j)$, l'algoritmo esegue un'operazione costante (confronto e assegnazione).
    - Ci sono $(n+1)*(m+1)$ coppie di indici.

**Spazio di memoria**: $O(n×m)$
    - La tabella richiede spazio $(n+1)×(m+1)$

L' algoritmo è il seguente: 

```
LCS(C[m,n], i, j){

	#Caso base i = 0 or j = 0
	for(j=0 to n):
		C[0,j] = 0;
		
	for(i=0 to n):
		C[i,0] = 0;

	for(i = 1 to n):
		for(j=1 to n):
		
			#Caso base in cui ho simboli uguali
			if(X[i] = Y[j]) 
				then C[i,j] = C[i-1,j-1] + 1;
				
			#Caso passo in cui ho simboli diversi
			else
				C[i,j] = max{C[i-1,j], C[i,j-1]};
}
```

---
