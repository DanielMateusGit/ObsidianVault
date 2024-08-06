---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - LCS
  - LCS/Costruzione_soluzione
  - Algoritmi/LCS/Costruzione_soluzione
---

#Algoritmi/LCS/Costruzione_soluzione 

Scrivi l' algoritmo per la costruzione della soluzione
;
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
