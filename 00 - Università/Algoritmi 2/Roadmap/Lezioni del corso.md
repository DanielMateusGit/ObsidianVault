
- [ ] **Lezione 25/09**
  - Ripasso: notazioni asintotiche, tempi di calcolo di algoritmi iterativi, ricorsivi e divide et impera. 
  - Fibonacci: tempo di calcolo dell'algoritmo ricorsivo, verso la programmazione dinamica.

- [x] **Lezione 26/09**
  - Sequenze, sottosequenze, prefissi.
  - Il problema della LCS. Riformulazione in termini ricorsivi, sottoproblemi, algoritmo ricorsivo.
  - Proprietà della sottostruttura ottima della LCS.

- [x] **Lezione 27/09**
  - Calcolo della lunghezza di una LCS, algoritmo bottom-up.
  - Esercizio su LCS (riempimento matrice per il calcolo della lunghezza di una LCS).

- [x] **Lezione 2/10**
  - Il problema del Weighted Interval Scheduling (WIS). Risoluzione mediante programmazione dinamica inclusa la ricostruzione di una soluzione mediante stampa.
  - Dimostrazione della proprietà della sottostruttura ottima.

- [x] **Lezione 3/10**
  - Ricostruzione di una LCS mediante algoritmo ricorsivo di stampa.

- [x] **Lezione 4/10**
  - Dimostrazione della proprietà della sottostruttura ottima della LCS.
  - Esercizi proposti: Heaviest Common Subsequence (HCS) tra due sequenze e LCS tra tre sequenze.
  - Il problema della Longest Increasing Subsequence (LIS). Risoluzione mediante programmazione dinamica attraverso l'introduzione di un problema ausiliario/vincolato.

- [x] **Lezione 9/10**
  - Il problema "Hateville". Risoluzione mediante programmazione dinamica inclusa la ricostruzione di una soluzione mediante stampa. 
  - Dimostrazione della proprietà della sottostruttura ottima.
  - Il problema "Interleaving". Risoluzione mediante programmazione dinamica.
  - Problema del calcolo del numero minimo di caratteri da aggiungere ad una stringa per renderla palindroma. Risoluzione mediante programmazione dinamica (parte 1).

- [x] **Lezione 10/10**
  - Proprietà della sottostruttura ottima del problema vincolato di LIS.
  - Calcolo della lunghezza di una LIS. Algoritmo bottom-up.
  - Ricostruzione di una soluzione mediante stampa. Esempio.
  - Dimostrazione della proprietà della sottostruttura ottima della LIS (nel problema vincolato).

- [x] **Lezione 11/10**
  - Il problema della Longest Increasing Common Subsequence (LICS). Risoluzione mediante programmazione dinamica attraverso l'introduzione di un problema ausiliario/vincolato.
  - Proprietà della sottostruttura ottima della LICS (nel problema vincolato).
  - Calcolo della lunghezza di una LICS. Algoritmo bottom-up.
  - Varianti di LICS: decrescente, alternanza pari-dispari, nessun numero consecutivo pari.
  - Esercizio: determinare una più lunga sottosequenza comune di X e Y con simboli rossi <= R.
  - Calcolo della distanza di EDIT tra due sequenze.

- [x] **Lezione 16/10**
  - Problema del calcolo del numero minimo di caratteri da aggiungere ad una stringa per renderla palindroma. Risoluzione mediante programmazione dinamica (parte 2).
  - Problema del calcolo di un sottovettore di valore massimo di un vettore con componenti intere. Risoluzione mediante programmazione dinamica. Ricostruzione di un sottovettore di valore massimo lasciata come esercizio.
  - Problema del calcolo del costo di un percorso di costo minimo dalla posizione (1,1) alla posizione (m,n) in una griglia di m righe e n colonne con 3 possibili spostamenti da una cella alla successiva.
  - Esercizio (solo impostato): calcolo del numero dei percorsi possibili dalla posizione (1,1) alla posizione (m,n) in una griglia di m righe e n colonne con 3 possibili spostamenti da una cella alla successiva.

- [x] **Lezione 17/10**
  - ==Il problema dello Zaino (Knapsack 0-1)==. Risoluzione completa mediante programmazione dinamica.

- [x] **Lezione 18/10**
  - Esercizio: determinare se la lunghezza di una LCS di X e Y è >= L.
  - Problema di decisione del Subsetsum. Risoluzione mediante programmazione dinamica.
  - Esercizio: Knapsack 0-1 con oggetti colorati.

- [x] **Lezione 23/10**
  - Esercizio (risoluzione): calcolo del numero di tutti percorsi possibili dalla posizione (1,1) alla posizione (m,n) in una griglia di m righe e n colonne con 3 possibili spostamenti da una cella alla successiva.
  - Knapsack a coppie: dato un numero naturale C>0 e dati due insiemi disgiunti X e Y rispettivamente di m e n oggetti, a ciascuno dei quali è associato un valore ed un ingombro, si vuole calcolare un sottoinsieme di XxY di valore massimo composto da coppie di oggetti di ingombro complessivo <= C.
  - LCS pesata [esercizio assegnato nella prima prova parziale A.A. 22/23]: dato un numero naturale C>0 e date due sequenze X e Y rispettivamente di lunghezza m e n  di simboli a ciascuno dei quali è associato un ingombro, si vuole calcolare una più lunga sottosequenza comune a X e Y di ingombro complessivo <= C.
  - Variante di WIS (weighed interval scheduling) con ingombri: dato un numero naturale C>0 e dato un insieme X di n attività, a ciascuna delle quali è associato un tempo di inizio, un tempo di fine, un valore ed un ingombro, si vuole calcolare un sottoinsieme di X di valore massimo composto da attività mutualmente compatibili e di ingombro complessivo <= C.

- [x] **Lezione 24/10**
  - Calcolo dei cammini minimi tra tutte le coppie di vertici di un grafo orientato e pesato. ==Algoritmo di Floyd-Warshall.==
***
==Questa è la metà del corso
***

- [ ] **Lezione 25/10**
  - ==Algoritmo di Floyd-Warshall== (continuazione). Calcolo dei predecessori e ricostruzione di un cammino minimo.
  - Esercizi su varianti di Floyd-Warshall.

- [ ] **Lezione 30/10**
  - ==Strutture Dati per Insiemi Disgiunti.== Definizioni. Calcolo delle componenti connesse di un grafo non orientato. Rappresentazione mediante liste concatenate e costi delle operazioni. Questioni inerenti la complessità di un algoritmo che sfrutta le Strutture Dati per Insiemi Disgiunti.
  - Esercizi di Programmazione Dinamica.

- [ ] **Lezione 31/10**
  - Esercizio: cammino minimo in un grafo con archi colorati.
  - Esercizio: cammino minimo con numero di archi rossi <= R.

- [ ] **Lezione 6/11**
  - Esercizio: cammino minimo in un grafo non pesato con archi colorati.
  - Esercizio: cammino minimo con numero pari di archi rossi.
  - Esercizio: Knapsack con oggetti colorati e numero pari di oggetti rossi.
  - Esercizio proposto: cammino minimo di lunghezza <= L.

- [ ] **Lezione 14/11**
  - Esercizio: cammino minimo con archi rossi e blu.
  - Esercizio proposto: calcolare la più lunga sottostringa comune di due sequenze X e Y.

- [ ] **Lezione 15/11**
  - ==Euristica dell'unione pesata.== Teorema (con dimostrazione): utilizzando l'euristica dell'unione pesata,  una sequenza di m operazioni di cui n sono make-set e al più n-1 delle quali sono union, per essere eseguita impiega un tempo O(m + n log n ).
  - ==Strutture dati per insiemi disgiunti: rappresentazione mediante foreste di alberi.== Unione per rango e compressione dei cammini. Relativa implementazione di make-set, find-set e union. Tempi di calcolo di una sequenza di m operazioni  (di cui n sono make-set e al più n-1 delle quali sono union) mediante unione per rango + compressione dei cammini (senza dimostrazione).
  - Esercizio. Dato un grafo pesato sugli archi e nel quale ad ogni arco, oltre al peso, è associato un numero naturale tramite una data funzione f, calcolare, per ogni coppia di vertici, il peso di un cammino minimo nel quale la sequenza dei valori associati agli archi tramite f è strettamente crescente.
  - Esercizio. Dato un naturale H e dato un grafo pesato sugli archi e nel quale ad ogni vertice è associato un numero naturale tramite una data funzione f, calcolare, per ogni coppia di vertici, il peso di un cammino minimo nel quale la somma dei valori associati ai vertici è minore o uguale ad H.
  - Esercizio proposto. Esercizio Hateville (con anche un numero di alberi associato ad ogni casa) con il vincolo che il numero totale di alberi è pari.

- [ ] **Lezione 20/11**
  - Esercizio. Dato un grafo nel quale ad ogni vertice è associato un colore (rosso o blu), stabilire, per ogni coppia di vertici, se esiste un cammino nel quale sono presenti due vertici consecutivi rossi.
  - Esercizio. Date due sequenze X e Y su un alfabeto di simboli a ciascuno dei quali è associato un colore (rosso o blu), calcolare una LCS nella quale vi sono due simboli consecutivi di rossi.
  - Esercizio. Dato un naturale H e dato un grafo pesato sugli archi e nel quale ad ogni arco, oltre al peso, è associato un numero naturale tramite una data funzione f, calcolare, per ogni coppia di vertici, il peso di un cammino di peso massimo nel quale la somma dei valori associati agli archi mediante f è minore o uguale ad H.
  - Risoluzione esercizio proposto. Esercizio Hateville (con anche un numero di alberi associato ad ogni casa) con il vincolo che il numero totale di alberi è pari.
  - Esercizio. Esercizio Hateville (con anche un colore associato ad ogni casa) con il vincolo che nell'insieme ricercato non vi siano due case consecutive rosse.

- [ ] **Lezione 5/12**
  - Perché ==greedy-min== risolve un problema di minimo associato ad un matroide pesato (trasformazione di un problema di minimo in un problema di massimo definendo una nuova opportuna funzione peso a partire da quella data + applicazione del teorema di Rado).
  - ==Nozione di arco sicuro e algoritmo Generic-MST== per il calcolo di un albero di copertura minimo. Rilettura dell'algoritmo di Kruskal come specializzazione di Generic-MST.
  - Nozioni di taglio, arco che attraversa un taglio, taglio che rispetta un sottoinsieme di archi e arco leggero.

- [ ] **Lezione 11/12**
  - Rappresentazione di una grafo tramite liste di adiacenza. ==Algoritmo di Prim come specializzazione di Generic-MST== e sua complessità.
  - Teorema dell'arco sicuro (con dimostrazione, illustrata il 12/12). Tale teorema assicura la correttezza dell'algoritmo di PRIM.
  - Corollario (con dimostrazione): se (u,v) è un arco di peso minimo che collega una componente connessa ad un'altra componente connessa in una foresta (V,S), allora (u,v) è un arco sicuro per S. Tale corollario assicura la correttezza dell'==algoritmo di Kruskal== come specializzazione Generic-MST. Nota bene: sappiamo già che l'algoritmo di Kruskal funziona correttamente indipendentemente da questo risultato. Infatti l'algoritmo di Kruskal è anche un'istanza di greedy-min associato ad un problema di minimo definito su un matroide (il matroide grafico) e quindi l'algoritmo di Kruskal funziona correttamente.
  - Cammini minimi da un'unica sorgente. ==Tecnica del rilassamento e algoritmo di Dijkstra.==
  - Visita in ampiezza di un grafo (BFS).

- [ ] **Lezione 12/12**
  - Dimostrazione del teorema dell'arco sicuro.
  - Dimostrazione della correttezza dell'algoritmo di Dijkstra.

- [ ] **Lezione 13/12**
  - Complessità della visita in ampiezza di un grafo (==BFS==).
  - Definizione di Albero BFS.
  - Esercizi: contare i vertici raggiungibili da un vertice dato, stampare i vertici che hanno distanza pari da un vertice dato, ricostruire il cammino tra due vertici, stabilire se un grafo non orientato è connesso, stabilire se un grafo non orientato è un albero.
  - Visita in profondità di un grafo (==DFS==) e relativa complessità.
  - Classificazione degli archi generata da DFS su un grafo orientato e classificazione degli archi generata da DFS su un grafo non orientato. Come individuare la presenza di un ciclo in grafi orientati ed in grafi non orientati (con relativa modifica dell'algoritmo DFS).
  - Modifica dell'algoritmo DFS per stampare per ogni arco la classe cui appartiene (in accordo con la classificazione degli archi).
  - Calcolo delle componenti connesse di un grafo non orientato mediante modifica dell'algoritmo DFS.
  - Definizione di Foresta DF.
  - Teorema delle parentesi in DFS (con dimostrazione).
  - Definizione di ordinamento topologico in un DAG (grafo orientato aciclico). Come si calcola un ordinamento topologico di un dato DAG. Un esempio di applicazione.



