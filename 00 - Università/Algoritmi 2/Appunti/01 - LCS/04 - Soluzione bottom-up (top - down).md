---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Algoritmi/LCS/Soluzione_bottom_up
  - LCS
---

- [[#Come passo dalla soluzione ricorsiva alla soluzione dinamica?|Come passo dalla soluzione ricorsiva alla soluzione dinamica?]]
- [[#Come si calcola il valore di una cella della matrice?|Come si calcola il valore di una cella della matrice?]]
- [[#Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?|Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?]]
- [[#Esempio di calcolo della lunghezza di una LCS (con matrice)|Esempio di calcolo della lunghezza di una LCS (con matrice)]]

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
## Come si calcola il valore di ogni cella?


![[Pasted image 20240804095254.png | 350]]

Questo è un esempio di matrice della LCS (già riempita e vedremo come), con $X = <A, B, C, B, D, A , B>$ ed $Y =<B, D, C, A, B, A>$.

I simbolo $\epsilon$ corrispondono al simbolo nullo.

---

## Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termine di tempo e spazio?

---

## Esempio di calcolo della lunghezza di una LCS (con matrice)

---
