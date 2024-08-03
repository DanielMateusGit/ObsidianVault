---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Programmazione_dinamica
  - Algoritmi/LCS/Caratterizzazione_della_soluzione
---
#Algoritmi/LCS/Caratterizzazione_della_soluzione 

Perchè utilizziamo la programmazione dinamica per il problema LCS?
;
 Un primo approccio per risolvere il problema della LCS potrebbe essere:
- Trovare tutte le possibili sotto-sequenze di $X$
- Controllare che ogni sotto-sequenza di $X$ sia anche sotto-sequenza di $Y$ 
- Aggiornare ad ogni controllo la LCS con lunghezza massima
***
Ci sono $X^n$ possibili sotto-sequenze di . Questo approccio richiede un tempo esponenziale. Per sequenza troppo lunghe non è utilizzabile.

Quali sono i sotto-problemi della LCS?
;
"Lunghezza della più lunga sotto-sequenza ricorsiva", tra $X_{m-1}$ ed $Y_{n-1}$.
***
Ossia: LCS computata prendendo in input i [[Concetti propedeutici | prefissi]] delle sequenze iniziali.
