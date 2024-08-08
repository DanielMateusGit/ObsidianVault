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
Ossia: LCS computata prendendo in input i [[00 - Università/Algoritmi 2/FlashCards/LCS/Concetti propedeutici| prefissi]] delle sequenze iniziali.

Che forma ha la proprietà della sotto-struttura ottima di una LCS?
;
Siano $X = <x_1, x_2, ... x_m>$ e $Y=<y_1, y_2, ... y_n>$ due sequenze.
Sia $Z= <z_1, z_2 ... z_k>$ una qualsiasi LCS tra $X$ ed $Y$.
***
1. Se $X_m$ = $Y_n$, allora $Z_k$ = $X_m$ = $Y_n$  e $Z_{k-1}$ è una LCS di $X_{m-1}$ e $Y_{n-1}$.
2. Se $X_m$ $\neq$ $Y_n$, allora $Z_k$ ${\neq}$ $X_m$  implica che $Z$ è una LCS di $X_{m-1}$ e $Y$.
3. Se $X_m$ $\neq$ $Y_n$, allora $Z_k$ ${\neq}$ $Y_n$  implica che $Z$ è una LCS di $X$ e $Y_{n-1}$.
***

Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?
;
$S^{m, n}$ è la soluzione del problema iniziale.
***
$S^{m-h, n-k}$ è la soluzione del generico sotto-problema.
***
Il problema iniziale è "Trovare la sotto-sequenza comune più lunga tra le sequenze $X$ ed $Y$".
***
Il generico sotto-problema è "Trovare la sotto-sequenza comune più lunga tra i prefissi $X_{m-h}$ ed $Y_{n-k}$ di $X$ ed $Y$, con $h\in[0,m]$ e $k\in[0,n]$".
***
E la soluzione si ottiene combinando i sotto-problemi:
***
$S^{m, n}$ = $\{ S^{m-1, n-1}, ... , S^{m, n-k}, ... S^{m-h, n-k}, ... , S^{0, n-1}, ...,   S^{m-h, 0}, ... , S^{0, 0}\}$