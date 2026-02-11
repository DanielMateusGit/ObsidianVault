---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - LCS
  - Algoritmi/LCS/Soluzione_bottom_up
  - Programmazione_dinamica
  - Algoritmi/Programmazione_dinamica
---

#Algoritmi/LCS/Soluzione_bottom_up

Come passare dalla soluzione ricorsiva alla soluzione dinamica LCS?
;
 Introduciamo una struttura dati di supporto per salvare i risultati dei sotto-problemi dell' algoritmo. 
 ***
 Nel caso specifico una matrice che ha come dimensione le lunghezze delle sequenze di partenza, e dove la cella $C_{i,j}$ contiene la lunghezza della più lunga sotto-sequenza comune, considerando i primi simboli i della prima sequenza ed i primi j simboli della seconda.
***

Che forma ha la matrice di supporto della LCS?
;
- Avrà come numero di righe la lunghezza di X.
- Avrà come numero di colonne la lunghezza di Y.
- Ogni riga/colonna rappresenterà un indice della sequenza a cui è associata.
- Ogni cella $C_{i,j}$ corrisponderà alla "Lunghezza della LCS più comune più lunga prendendo i primi $i$ simboli da $X$ ed i primi $j$ simboli da $Y$".
- Il valore di ogni cella $C_{i,j}$ sarà calcolato a partire da un caso base della formulazione ricorsiva, o dalle celle calcolate in precedenza.
- Il Calcolo delle celle procede in ordine di lettura della matrice.

Come si calcola il valore di ogni cella?
;
![[Pasted image 20240804105550.png | 400]]

Come risulta l' algoritmo della LCS dinamico? Quali sono i suoi consumi in termini di tempo e spazio?
;
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
***
**Tempo di esecuzione**: $O(n×m)$
    - Per ogni coppia di indici $(i,j)$, l'algoritmo esegue un'operazione costante (confronto e assegnazione).
    - Ci sono $(n+1)*(m+1)$ coppie di indici.
***
**Spazio di memoria**: $O(n×m)$
    - La tabella richiede spazio $(n+1)×(m+1)$