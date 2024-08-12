---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - LCS
  - Programmazione_dinamica
  - Algoritmi/LCS_Caratterizzazione_soluzione_ottima
---
- [[#Cosa si intende per caratterizzazione della soluzione ottima?|Cosa si intende per caratterizzazione della soluzione ottima?]]
- [[#Verso la programmazione dinamica (ragionamento)|Verso la programmazione dinamica (ragionamento)]]
- [[#Quali sono i sotto-problemi della LCS?|Quali sono i sotto-problemi della LCS?]]
- [[#Che forma ha la proprietà della sotto-struttura ottima di una LCS?|Che forma ha la proprietà della sotto-struttura ottima di una LCS?]]
- [[#Come si dimostra la proprietà di sotto-struttura ottima di una LCS?|Come si dimostra la proprietà di sotto-struttura ottima di una LCS?]]
- [[#Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?|Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?]]

# Caratterizzazione della soluzione ottima

## Cosa si intende per caratterizzazione della soluzione ottima?

Questa è la prima delle 4 fasi del processo di sviluppo di algoritmi di programmazione dinamica.

> [!Note] Le 4 fasi:
> [[01 - Processo di sviluppo di un algoritmo dinamico]]

---

## Perchè utilizziamo la programmazione dinamica per il problema LCS?

Un primo approccio per risolvere il problema della LCS potrebbe essere:

- Trovare tutte le possibili sotto-sequenze di $X$
- Controllare che ogni sotto-sequenza di $X$ sia anche sotto-sequenza di $Y$ 
- Aggiornare ad ogni controllo la LCS con lunghezza massima

> [!Warning] Perchè questo approccio non funziona?
> Ci sono $2^m$ possibili sotto-sequenze di $X$. Questo approccio richiede un tempo esponenziale. Per sequenza troppo lunghe non è utilizzabile.

Proviamo quindi a seguire gli step necessari per [[00 - Sotto-struttura ottima | trovare una sotto-struttura ottima nel problema]].

---

## Quali sono i sotto-problemi della LCS?

Considerando quali sono le [[01 - Introduzione al problema LCS | istanze della LCS]], un sotto-problema è definibile come:

> "Più lunga sotto-sequenza", tra $X_{m-1}$ ed $Y_{n-1}$.
> Ossia: LCS computata prendendo in input i[[00 - Università/Algoritmi 2/FlashCards/LCS/Concetti propedeutici| prefissi]] delle sequenze iniziali.

Date $X$ ed $Y$, i sotto-problemi sono:

$X_{m-1}$, $X_{m-2}$, $X_{m-3}$, $X_{m-4}$, ... $X_{0}$  
$Y$, $Y_{m-2}$, $Y_{m-3}$, $Y_{m-4}$, ... $Y_{0}$  

> [!Summary] In Breve:
> Il [[00 - Sotto-struttura ottima | sotto-problema]] per la LCS, non è altro che
> la LCS stessa, calcolata con istanze più piccole (ridotte dal problema originale).

---

## Che forma ha la proprietà della sotto-struttura ottima di una LCS?

Seguendo gli step [[00 - Sotto-struttura ottima | trovare una sotto-struttura ottima nel problema]] :

Siano $X = <x_1, x_2, ... x_m>$ e $Y=<y_1, y_2, ... y_n>$ due sequenze.

Sia $Z= <z_1, z_2 ... z_k>$ una qualsiasi LCS tra $X$ ed $Y$.

1. Se $X_m$ = $Y_n$, allora $Z_k$ = $X_m$ = $Y_n$  e $Z_{k-1}$ è una LCS di $X_{m-1}$ e $Y_{n-1}$.
2. Se $X_m$ $\neq$ $Y_n$, allora $Z_k$ ${\neq}$ $X_m$  implica che $Z$ è una LCS di $X_{m-1}$ e $Y$.
3. Se $X_m$ $\neq$ $Y_n$, allora $Z_k$ ${\neq}$ $Y_n$  implica che $Z$ è una LCS di $X$ e $Y_{n-1}$.

Questa definizione segue esattamente gli step, dato che :

- Il sotto-problema in cui ci troviamo si risolve tramite una scelta.
- Stiamo generando dei sotto-problemi ad ogni scelta
- Stiamo supponendo di conoscere già la soluzione $Z$ (dato che confrontiamo con il valore $Z_{k}$ ).
- Le soluzioni dei sotto-problemi sono ottime (questo lo dimostreremo).

> [!Important] Stiamo confrontando X, Y e Z
> Un punto importantissimo di questa "ricerca della sotto-struttura" è quella di supporre di avere già la soluzione. Inizialmente è un pensiero innaturale, ma prenderà senso quando verrà stesa la soluzione ricorsiva del problema.

==*Spiegazione primo punto:*==

In questo punto stiamo confrontando il carattere finale delle sequenze (più precisamente del [[00 - Università/Algoritmi 2/FlashCards/LCS/Concetti propedeutici| prefisso]] delle sotto-sequenze, dato che siamo in un sotto-problema). 

> Se il carattere finale di $X$ ed $Y$ è uguale, giustamente lo sarà anche in $Z$ (che, ricordiamo, sto supponendo di avere già).

Il mio simbolo sta nella soluzione, quindi il prossimo simbolo $Z_{k-1}$ da trovare, sarà la soluzione di tutte le sequenze meno il simbolo appena trovato.

==*Spiegazione del secondo e terzo punto:*==

Se invece, confrontando il carattere finale delle sequenze:

- Mi accorgo che non sono uguali (non vale $Z_k$ = $X_m$ = $Y_n$ ) 
- Il simbolo corrente di $X_{m}$ non è presente nella soluzione $Z$ (che, ripetiamo, sto supponendo di avere già trovato)

> Allora il calcolo della soluzione corrente sarà il risultato della "LCS tra la sequenza Y ed X senza questo simbolo, che so già non essere nella soluzione (perchè ho Z)".

La spiegazione è simmetrica per il terzo punto.

--- 

## Come si dimostra la proprietà di sotto-struttura ottima di una LCS?

Le soluzioni dei sotto-problemi sono ottime. Dimostrazione per assurdo.

Premessa : $Z_{k - 1}$ è LCS di lunghezza $k-1$ tra $X_{m-1}$ ed $Y_{n-1}$.

Assurdo  : Esiste $W$, sotto-sequenza di $X_{m-1}$ ed $Y_{n-1}$ , di lunghezza $k$ > $k-1$.

Seguendo le regole della sotto-struttura ottima della LCS, trovando $X_{m}$ = $Y_{n}$ posso accodare a $W$ l' ultimo simbolo di entrambe le sequenze.

Così facendo la lunghezza di $W$ sarebbe maggiore di $k$. Contraddizione con la premessa! 

(complicata, guarda lezione!)

---

## Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?

$S^{m, n}$ è la soluzione del problema iniziale.

$S^{m-h, n-k}$ è la soluzione del generico sotto-problema.

Il problema iniziale è "Trovare la sotto-sequenza comune più lunga tra le sequenze $X$ ed $Y$".

Il generico sotto-problema è "Trovare la sotto-sequenza comune più lunga tra i prefissi $X_{m-h}$ ed $Y_{n-k}$ di $X$ ed $Y$, con $h\in[0,m]$ e $k\in[0,n]$".

E la soluzione si ottiene combinando i sotto-problemi:

$S^{m, n}$ = $\{ S^{m-1, n-1}, ... , S^{m, n-k}, ... S^{m-h, n-k}, ... , S^{0, n-1}, ...,   S^{m-h, 0}, ... , S^{0, 0}\}$

---
