---
tags:
  - Algoritmi
  - Algoritmi/LIS
  - LIS
  - Algoritmi/Programmazione_dinamica
  - Programmazione_dinamica
  - Algoritmi/LIS_Caratterizzazione_soluzione_ottima
---

# Caratterizzazione della soluzione ottima

## Perchè LIS non è direttamente risolvibile?

Seguendo l' esempio della LCS, potremmo arrivare a dire che i sotto-problemi di LIS sono "una porzione più piccola del problema originale".

Sarebbero quindi, tutti i prefissi: 

$X_{m-1}$, $X_{m-2}$, $X_{m-3}$, $X_{m-4}$, ... $X_{0}$ 

Dove ogni $X_m$ sarebbe la "sotto-sequenza ==ordinata== più lunga possibile, presi i primi $m$ simboli. "

==Ma queste informazioni (i sotto-problemi), sono insufficienti:==

Non è vero infatti, che se mi trovo al problema $X_m$, posso esaurire con certezza i casi di risoluzione.

Nella LCS, ==supponendo di avere già la soluzione==, posso spiegare la logica con cui questa viene calcolata.

Questo avviene per il fatto che la logica di calcolo risiede nella definizione del problema (uguaglianza tra simboli).

> [!Sumamry] In Pratica
> In pratica, nella LCS basta guardare l'istanza, o una porzione di essa, per poter definire la soluzione di un sotto-problema (sempre facendo finta di aver già calcolato la soluzione). 

Per la LIS non è possibile:

> Bisogna ==computare== tutto il resto dell'  istanza per capire con "chi combinare" il sotto-problema corrente.

Infatti, dato $x_m$ numero dell' istanza, questo si combina con :

> ==La più lunga sottosequenza crescente e COMPATIBILE== con $x_m$.


> [!Summary] In Breve:
> Per spiegare come il sotto-problema corrente si combina con gli altri già risolti, devo prima spiegare il criterio di compatibilità che regola le combinazioni.
> 
> Questo criterio di compatibilità non è altro che una valutazione fatta su tutti i numeri precedenti a quello corrente.
> 
> Bisogna quindi, prima di capire come descrivere la combinazione dei sotto-problemi, risolvere il ==problema ausiliare di trovare l' ottimo COMPATIBILE==

> [!Hint] Non è la stessa cosa nella LCS? In cosa differisce?
> Anche nella LCS dovevamo prendere una decisione seguendo un criterio (uguaglianza tra simboli)
> 
> La differenza con LIS sta nel fatto che nel caso della LCS bastava confrontare i simboli in coda alla sequenza, invece nel nostro caso si deve proprio ==computare== tutto il prefisso, confrontandolo con il simbolo in coda alla sequenza.
> 
> ==Una computazione "a parte" implica la definizione di un problema ausiliario.== 
> Non basta "guardare" l' istanza per fare le opportune valutazioni.
> 

***

## Come si definisce il problema ausiliario di LIS?

Il generico sotto-problema ausiliario sarebbe:

Data una sequenza $X$ di $m$ numeri interi, determinare una tra le più lunghe sotto-sequenza crescenti di $X_i$ e che termini con $x_i$.

PER LA SOTTO_STRUTTURA OTTIMA NON USARE ANCORA IL MAS O FORM RICORSIVA 


PROPRIETÀ di SOTTO-STRUTTURA OPTTIMA SE COMPATIBILE 

***

