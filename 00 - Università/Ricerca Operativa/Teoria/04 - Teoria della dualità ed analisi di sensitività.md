
* Introduzione alla teoria della dualità
	* [ ] Associato ad ogni PPL => Problema duale
	* [ ] ==I Prezzi ombra sono la soluzione del problema duale==
	* [ ] Analisi di sensitività: studio della soluzione ottimale su condizioni differenti da quelle ipotizzate inizialmente.
	* [ ] Problema primale e problema duale.
	* [ ] Relazioni tra il primale ed il duale: 
		* [ ] Parallelismo in forma standard
		* [ ] Parallelismo in forma matriciale => fa vedere meglio come i termini del primale si trasformano per formare il problema duale
		* [ ] primale max => duale min 
	* [ ] Forma tabellare => ancora più chiaro :D
	* [ ] Ultima tabellina riassuntiva => da tenere per gli esercizi 

* Metodo del simplesso (parallelismo tra primale e duale)
	* [ ] Occhio alle relazioni tra W e le bi e yi => FONDAMENTALE (slide, lez 2). Spiega la funzione obiettivo del duale.
	* [ ] Occhio alla relazione zj => questa spiega come ricavare i termini noti a sinistra del problema duale.
	* [ ] Posso trovare le variabili di surplus dei vincoli funzionali (altra formula, guarda sul pdf)
	* [ ] Esempio WYNDORGLASS => penso spieghi "la ciccia". Partire da quello e poi capire le formule.


> [!Warning] 
> Bisogna saper descrivere bene il primale con le variabili giuste.
> Bisogna saper arrivare al duale con le variabili del primale + formule.
> 
> Forse può essere meccanizzato ogni esercizio, ma livello di ragionamento aiuta molto conoscere la "FORMA DEI PROBLEMI".

* Proprietà di dualità debole e forte. Teorema di dualità.
	* [ ] Enunciato delle prime due proprietà. Relazione esistente tra le due soluzione (quella del primale e quella del duale).
	* [ ] Proprietà delle soluzioni complementari. (ad ogni passo ho una soluzione primale ed una complementare duale).
	* [ ] Proprietà di simmetria
	* [ ] Teorema di dualità => riassume un po' tutte le precedenti
	* [ ] Spiega la correlazione tra soluzione del primale e duale.
	* [ ] Posso risolvere il duale per trovare una soluzione per il primale (con il metodo del simplesso). sotto certe condizioni (slide). A volte il duale può avere meno vincoli funzionali del primale. In questo caso riduco il costo computazionale per risolvere il primale.

* Interpretazione del problema duale:
	* Questa lezione (anche se è facoltativa), fa capire il senso del duale in maniera più pratica.

	- [ ] C'è una buona scomposizioni in "variabili" del primale (come intro).
	- [ ] Le variabili $y_i$ sono i contributi al profitto di ogni attività nel duale => (quelli che compaiono di fianco alle variabili in funzione obiettivo del duale). => corrispondono ai prezzi ombra del primale.
	- [ ] Ogni coefficente risultante dalla risoluzione del duale => è un prezzo ombra.
	- [ ] Ogni prezzo ombra, $y_i$ ottenuto => mi dice che aumentando nel primale la risorsa corrispondente $b_i$ => ottengo un aumento dell' ottimo corrispondente a $+y_i$ per ogni unità aggiunta.
	- [ ] Occhio! Guardare bene il concetto di CONTRIBUTO CORRENTE AL PROFITTO del primale
	- [ ] Ì vincoli del duale sono i contributi correnti al profitto del primale (wow).

* Proprietà della teoria della dualità: complementary slackness
	* [ ] Ogni soluzione di base nel problema primale => ha una corrispondente soluzione di base nel problema duale.
	* [ ] Proprietà di complementary Slackness : esiste una relazione di complementarietà tra le variabili di primale e duale => guarda tabella nelle slide.
	* [ ] Questa tabellina (e proprietà) è FONDAMENTALE e riassume il "calcolo da fare" per passare da un problema all' altro.

* Soluzione primale ammissibile e soluzione duale ammissibile
	* [ ] La soluzione Z del primale deve avere lo stesso valore della soluzione W del duale.
	* [ ] È possibile, avendo la soluzione del primale, ricavare tramite formule (guarda tabella pdf) la soluzione del duale. Esiste quindi una corrispondenza anche in questo.
	* [ ] Classificazione delle soluzioni d' accordo alla combinazione sol. primale e sol. duale (d' accordo all' ammissibilità).

* PPL Non in forma standard? Possiamo usare la teoria della dualità per risolvere! No problem!
	- [ ] Metodo SOB => Sensible-odd-bizarre => metodo per trasformare primale in duale e vice versa.
	- [ ] Esempio di utilizzo del metodo SOB => utilizzarlo quando si vuole passare da primale a duale.
