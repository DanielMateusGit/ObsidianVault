# Modelli nella ricerca operativa

## Che cosa è un problema di ottimizzazione?

È un problema che cerca di trovare => la massima o ( minima ) resa di una funzione.

> [!Esempio stupido:]
> Luca deve decidere quante casse di mele e di arance acquistare per massimizzare il profitto. Il profitto per cassa di mele è 5 euro e per cassa di arance è 7 euro. Ha un budget di 300 euro e può immagazzinare al massimo 15 casse. Ogni cassa di mele costa 20 euro e ogni cassa di arance costa 30 euro.

Questa parte del corso si occupa di modellare matematicamente situazioni di questo tipo (ovviamente più complesse).

***

## Quali sono le parti importanti di un problema di ottimizzazione? 

Sono solo 3 "ingredienti":

- Una funzione obiettivo: $opt f(x)$ 
- Una regione ammissibile di soluzioni: $X \subseteq R^n$
- Delle variabili decisionali:  $x \in X$

La definizione risulta: $opt(f(x))$ $\text{"soggetto a": } x \in X$, con $X \subseteq R^n$

> [!Summary] Cosa significa?
> $opt(f(x))$ $\text{"soggetto a": } x \in X$, con $X \subseteq R^n$ si traduce in :
> 
> "Ottimizzazione del problema descritto dalla funzione $f(x)$, il cui valore (e miglioramento) dipendono dalle variabili decisionali $x$, prese da una regione di ammissibilità $X \subseteq R^n$."

> [!Hint] Spiegazione delle singole parti
> - La funzione obiettivo rappresenta il problema. Siamo interessati ad ottimizzarla (opt).
>   
> - La funzione migliora d'accordo all'input che le viene dato in pasto. Questi input prendono il nome di variabili decisionali. 
> 
> - L' insieme da cui posso pescare queste variabili decisionali si chiama regione ammissibile.

***

## Quale è la soluzione di un problema di ottimizzazione?

## Che corrispondenza esiste tra un problema di massimo e di minimo?

## In quanti modi posso categorizzare un problema di ottimo?

## Cosa è un problema di programmazione matematica?

***
- [ ] Obiettivi del corso: ottimizzazione. 
- [x] Come si definisce un problema di ottimizzazione?
	- [x] Funzione OB
	- [x] Regione ammissible
	- [x] Variabili decisionali
- [ ] Quale è la soluzione di un problema di ottimizzazione? 
- [ ] max f(x) = -min - f(x):
	- [ ] Trova un esempio nelle slide ( due coniche una simmetrica all' altra)
	- [ ] Ha un nome questa proprietà? Nel caso, sarebbe da definire
- [ ] Categorizzazione di un problema? 
	- [ ] minimo/massimo
	- [ ] ottimizzazione vincolata / ottimizzazione non vincolata
	- [ ] ottimizzazione intera / binaria / mista 
	- [ ] Cosa è un problema di Programmazione matematica?  => specializzazione di un problema di ottimizzazione
		- [ ] Vincoli ?
		- [ ] Regione ammissibile? = insieme dei vincoli del problema
		- [ ] Ammissibilità della soluzione? 

LEZIONE: 

https://elearning.unimib.it/mod/book/view.php?id=738961

MINUTO 27:00
***\
*** 

- [ ] Primo esempio di programmazione matematica (riportarlo)
- [ ] Possibili esiti
	- [ ] Problema non ammissibile. La regione ammissibile = insieme vuoto
	- [ ] Problema illimitato (non ho un minimo/massimo)
	- [ ] Esempi di programmazione matematica (riportare)
- [ ] Ottimo globale vs ottimo Locale (ricordiamo le osservazioni)
	- [ ] Esempio (riportare, fob convessa)
- [ ] Categorizzazione dei problemi di programmazione matematica
	- [ ] Programmazione lineare 
	- [ ] Programmazione lineare intera
	- [ ] Programmazione non lineare 
	- [ ] Alcuni esempi (riportarli => caso particolare di $x^2 -1$)
- [ ] Esempio "Cuba Libre" => molto importante, sicuramente da riportare.
- [ ] Esempio "Videogiochi" con variabili decisionali binarie
- [ ] Esempio "Problema dello zaino" => variabili intere 
- [ ] Esempio FantaCalcio

***

- [ ] Esempio "valore di un' abitazione"
- [ ] Esempio "Pokemon go"
- [ ] Attenzione => forse è meglio non spiegare tutti gli esempi, ma lasciarli in allegato "sintetizzati"

La lezione finisce con l' introduzione alla programmazione lineare intera => lasciata in un pdf a parte.
