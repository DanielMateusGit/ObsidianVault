---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - LCS
  - Programmazione_dinamica
  - Algoritmi/Programmazione_dinamica
  - Costruzione_soluzione
  - LCS/Costruzione_soluzione
---

# Costruzione della soluzione LCS

## Cosa si intende per costruzione della soluzione LCS?

Per trovare una soluzione al problema della LCS abbiamo risolto un sotto-problema di lunghezze.

Una volta trovata la soluzione a questo problema di lunghezze, bisogna ricostruire una soluzione per il problema originale.

Alla fine del calcolo della lunghezza della LCS tra due sequenze $X$ ed $Y$, è possibile ricostruire la sequenza dei simboli ripercorrendo "al contrario" la matrice.

## Come costruire la soluzione LCS data la matrice?

Durante la risoluzione della LCS, oltre a calcolare la lunghezza, bisogna salvare (sempre nella matrice) la direzione (il caso ricorsivo) utilizzato per avanzare di uno step risolutivo.

Successivamente, basta prendere la matrice e "ripercorrerla":

````
# b è la matrice "computata" 
# X è una delle sequenze originali
# i e j sono indici di supporto

PRINT_LCS (b, X, i, j) 
	if( i == 0 OR j ==0 )
		return
	if b[i, j] == "↖"
		PRINT_LCS( b, X, i-1, j-1)
		print X[j]
	elseif b[i,j] == "↑" 
		PRINT_LCS( b, X, i-1, j)
	else PRINT_LCS(b, X, i, j-1)
````

Questa soluzione impiega $O(m+n)$.