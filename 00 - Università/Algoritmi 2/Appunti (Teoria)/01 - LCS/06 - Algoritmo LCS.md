---
tags:
  - Algoritmi
  - Algoritmi/LCS
  - Programmazione_dinamica
  - LCS
  - Resume
---

- [[#Cosa si intende per sequenza?|Cosa si intende per sequenza?]]
- [[#Cosa si intende per sotto sequenza?|Cosa si intende per sotto sequenza?]]
- [[#Cosa si intende per prefisso?|Cosa si intende per prefisso?]]
- [[#Motivazione dell' algoritmo LCS|Motivazione dell' algoritmo LCS]]
- [[#Quale è il tempo di esecuzione della LCS e lo spazio occupato nella sua versione dinamica?|Quale è il tempo di esecuzione della LCS e lo spazio occupato nella sua versione dinamica?]]
- [[#Esempio di calcolo della LCS tra due sequenze|Esempio di calcolo della LCS tra due sequenze]]
- [[#Qual è l' istanza della LCS?|Qual è l' istanza della LCS?]]
- [[#Qual è la soluzione della LCS?|Qual è la soluzione della LCS?]]
- [[#Cosa si intende per caratterizzazione della soluzione ottima?|Cosa si intende per caratterizzazione della soluzione ottima?]]
- [[#Perchè utilizziamo la programmazione dinamica per il problema LCS?|Perchè utilizziamo la programmazione dinamica per il problema LCS?]]
- [[#Quali sono i sotto-problemi della LCS?|Quali sono i sotto-problemi della LCS?]]
- [[#Che forma ha la proprietà della sotto-struttura ottima di una LCS?|Che forma ha la proprietà della sotto-struttura ottima di una LCS?]]
- [[#Come si dimostra la proprietà di sotto-struttura ottima di una LCS?|Come si dimostra la proprietà di sotto-struttura ottima di una LCS?]]
- [[#Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?|Come si caratterizza la soluzione della LCS in relazione ai suoi sotto problemi?]]
- [[#Soluzione ricorsiva|Soluzione ricorsiva]]
- [[#Come passare dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?|Come passare dalla proprietà di sotto-struttura ottima alla definizione ricorsiva?]]
- [[#Quali variabili si introducono per risolvere la LCS? Perchè?|Quali variabili si introducono per risolvere la LCS? Perchè?]]
- [[#Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)|Qual è l' algoritmo ricorsivo? (con calcolo tempi ed albero ricorsivo)]]
- [[#Come passare dalla soluzione ricorsiva alla soluzione dinamica?|Come passare dalla soluzione ricorsiva alla soluzione dinamica?]]
- [[#Che forma ha la matrice di supporto della LCS?|Che forma ha la matrice di supporto della LCS?]]
- [[#Come si calcola il valore di ogni cella?|Come si calcola il valore di ogni cella?]]
- [[#Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termini di tempo e spazio?|Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termini di tempo e spazio?]]
- [[#Cosa si intende per costruzione della soluzione LCS?|Cosa si intende per costruzione della soluzione LCS?]]
- [[#Come costruire la soluzione LCS data la matrice?|Come costruire la soluzione LCS data la matrice?]]

# Concetti propedeutici

## Cosa si intende per sequenza?

Dato un alfabeto $\Sigma$, una **sequenza su $\Sigma$** è una tupla di simboli $X = \langle x_1, x_2, \ldots, x_n \rangle$ dove per ogni $\forall i \in[1,n]$ si ha che $x_i$ appartiene a $\Sigma$.

Esempio: $\Sigma$ = "Lettere dell' alfabeto" e $X = \{c, i ,a, o\}$

***

## Cosa si intende per sotto sequenza?

Data una sequenza $X=<x_1,x_2, ... X_m>$, la tupla $Z=<z_1,z_2,...z_k>$ è sotto-sequenza di $X$ sse:

$\exists$ **==una sequenza strettamente crescente di indici di X==** $I = <i_1, i_2, ..., i_k>$ tale che $\forall j \in [1,k]$ $Z_j=X_{ij}$

> [!Important] Attenzione agli indici!
> Ricorda: gli indici devono essere strettamente crescenti


> [!Example] Esempio di sotto-sequenza
> $X=<a, b, c, b, d, a, b>$ e $Z=<b, c, b, d>$. Esiste una sequenza di indici $I=<2,3,5,7>$.
> 
> $J=<c, c>$ invece non è una sotto-sequenza
>  
> $K=<d, c>$ nemmeno è una sotto-sequenza
> 
> In entrambe i casi non abbiamo una sequenza di indici  strettamente crescente.

***

## Cosa si intende per prefisso?

Data una sequenza $X = <x_1, x_2, ... x_n>$ ed un indice $i\in[1,n]$, viene chiamata prefisso di $X$, la ==sotto-sequenza fatta dai primi i simboli di X==. 

> [!Example] Esempio di prefisso
> Il Prefisso $X_4$ della sequenza $X=<a,b,c,b,d,a,b>$ è la sotto-sequenza: $X_4=<a,b,c,b>$

***

# Introduzione al problema LCS

## Motivazione dell' algoritmo LCS

LCS sta per Longest-Common-SubSequence. Serve per trovare le sotto-sequenze comuni (a n sequenze) più lunga possibile.

Si applica (per esempio) per confrontare sequenze di DNA.

Trovando la sotto-sequenza comune a due sequenze di DNA posso determinare quanto due organismi siano simili o meno.

---

## Quale è il tempo di esecuzione della LCS e lo spazio occupato nella sua versione dinamica?

$O(n×m)$ per il tempo di esecuzione e $O(n×m)$ per lo spazio di memoria.

Nella versione ottimizzata, lo spazio si riduce a $O(min(n,m))$.

---

## Esempio di calcolo della LCS tra due sequenze

$X =<a, b, c, b, d, a ,b>$ di lunghezza 7.

$Y=<b,d,c,a,b,a>$ di lunghezza 6

$<b,c,a,b>$ è sotto-sequenza di X ed Y ed ha lunghezza 4. È una soluzione della LCS.

$<b,d,a,b>$ è sotto-sequenza di X ed Y ed ha lunghezza 4. È una soluzione della LCS.

<b,c,a> è sotto-sequenza di X ed Y, ma non avendo la lunghezza massima possibile, non è una soluzione della LCS.

***

## Qual è l' istanza della LCS?

> ***L' istanza non è altro che l' INPUT consumato dall'algoritmo***.

Nel caso della LCS sono le sequenze da confrontare. Possiamo dire che l'istanza di una LCS è:

> [!Summary] In Breve:
> Almeno due sequenze: $X=<x_1,x_2, ... , x_m>$ e $Y=<y_1, y_2, ... , y_n>$

***

## Qual è la soluzione della LCS?

La soluzione (o le soluzioni) è ogni $Z$, sotto-sequenza di $X$ ed $Y$, (sequenze) tale che:

> [!Summary] In Breve:
> $|Z| = max\{ |W| \text{ t.c W è sotto-sequenza di X ed Y } \}$

***

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

> "Lunghezza della più lunga sotto-sequenza ricorsiva", tra $X_{m-1}$ ed $Y_{n-1}$.
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

# Soluzione Bottom-up per LCS

## Come passare dalla soluzione ricorsiva alla soluzione dinamica?

Alla terza delle [[Processo di sviluppo di un algoritmo dinamico | quattro fasi del processo di sviluppo]] di algoritmi dinamici:

- È stata trovata una soluzione ricorsiva per l' algoritmo.
- È stata trovata la "variabile" che descrive i dati importanti per il calcolo del problema.
- Sono nati eventuali problemi ausiliari.

Il passaggio successivo è quello di salvare i risultati parziali prodotti dalla [[Soluzione ricorsiva]] in una struttura dati, in modo da ==riciclare tutte le informazioni già calcolate==.

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

## Come risulta l'algoritmo della LCS dinamico? Quali sono i suoi consumi in termini di tempo e spazio?

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

*** 

# Links

## Teoria

 [[00 - Università/Algoritmi 2/Appunti (Teoria)/01 - LCS/00 - Concetti propedeutici]]

 [[01 - Introduzione al problema LCS]]

 [[00 - Università/Algoritmi 2/Appunti (Teoria)/01 - LCS/02 - Caratterizzazione della soluzione ottima]]

 [[00 - Università/Algoritmi 2/Appunti (Teoria)/01 - LCS/03 - Soluzione ricorsiva]]

 [[04 - Soluzione bottom-up (top - down)]]

 [[00 - Università/Algoritmi 2/Appunti (Teoria)/01 - LCS/05 - Costruzione della soluzione]]

***

## Flash Cards

[[00 - Università/Algoritmi 2/FlashCards/LCS/Concetti propedeutici]]

[[Introduzione al problema]]

[[Caratterizzazione della soluzione]]

[[Soluzione ricorsiva]]

[[Soluzione bottom-up]]

[[Costruzione_Soluzione]]
