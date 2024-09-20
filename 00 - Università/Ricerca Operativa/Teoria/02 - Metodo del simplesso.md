
* Introduzione
	- [ ] Cosa è il metodo del simplesso? (1 dei 10 migliori algoritmi del 900).

* Rappresentazione grafica del metodo:
	- [ ] Frontiera del vincolo 
	- [ ] Concetto di vertice
		- [ ] Vertici Adiacenti 
	- [ ] Spigolo
	- [ ] Test di ottimalità di una soluzione

* Step dell' algoritmo:
	 - [ ] Inizializzazione.
	 - [ ] Test di ottimalità per ottenere lo spostamento al vertice successivo.
	 - [ ] Sposarsi fino a quando il test di ottimalità non consente più spostamenti.
	 - [ ] Il vertice corrente alla fine dell' algoritmo, sarà quello ottimale.

- Concetti Chiave:
	- [ ] Guardarli sulle slide, puramente teorici

* Interpretazione algebrica del metodo del simplesso
	- [ ] Bisogna tradurre la procedura grafica => geometrica 
	- [ ] Risoluzione di un sistema di equazioni lineare.
	- [ ] Convertire i vincoli di disuguaglianza in uguaglianza ed ottenere la forma aumentata del problema 
		- [ ] Variabili Slack 
	- [ ] Forma standard e forma aumentata di un problema 
	- [ ] Soluzione aumentata di un problema
	
	- [ ] Variabile di base e non di base:
		- [ ] durante l'inizializzazione del simplesso (e ad ogni step):
			- [ ] n variabili (d' accordo al numero di gradi di decisione) vengono poste a 0 => diventando variabili non di base
			- [ ] le altre sono tutte variabili di base
		- [ ]  Quantità delle variabili di base / non di base (slide, importante).

	- [ ] Modello in forma aumentata + Equazione di ottimo 

* Due passi del metodo del simplesso in forma algebrica 
	- [ ] Inizializzazione: si seleziona l' origine (variabili non di slack) e si settano a 0. Si ottiene una soluzione di base ammissibile.
	- [ ] Test di ottimalità:
	- [ ] Determinare la direzione di spostamento: Scelgo tra le variabili correnti, quella che mi porta un maggiore incremento.
		- [ ] Si scambia una variabile non di base => diventa di base
		- [ ] Con una di base => non di base 
		- [ ] Queste due prendono il nome di variabile entrante ed uscente
	- [ ] Determinazione dell' incremento:
		- [ ] Si ricalcolano tutte le variabili (dopo la modifica del cambio direzione).
		- [ ] Bisogna risolvere il sistema per capire quale sia il massimo valore assegnabile alla variabile entrante (senza infrangere i vincoli di non negatività).
		- [ ] Si utilizza il TEST DEL RAPPORTO MINIMO DEI VINCOLI
		- [ ] Questo determina la nuova variabile uscente.
	- [ ] Determinazione della nuova soluzione di base 

* Forma tabellare del metodo del simplesso:
	- [ ] Versione "in tabella" in cui il simplesso è più semplice da svolgere 
	- [ ] > Buona spiegazione sulle slide ( abbastanza visibile )


> [!Warning] Occhio
> Il simplesso in forma tabellare è estremamente più sintetico (anche da spiegare). Forse è meglio partire da quello?

* Tie Breaking
	- [ ] Sono situazioni particolari in cui la soluzione può non risultara "chiara" di primo impatto, oppure situazioni in cui non si sa bene come procedere con l' algoritmo
	- [ ] Situazione 1: Come decidere la variabile entrante quando i coefficienti sono uguali?
	- [ ] Concetto di variabile degenere 
	- [ ] Situazione 2: Nessuna variabile uscente 
	- [ ] Situazione 3: Multiple soluzioni ottimali al problema
	

* Forme alternative del metodo del simplesso 
	* [ ] Portate un problema da qualsiasi forma => alla forma standard.
	* [ ] Slack e Surplus 

* Analisi di post ottimalità e prezzo ombra
	* [ ] Diversi Task
	* [ ] Task 1: Debugging
	* [ ] Task 2: Validazione
	* [ ] Task 3: Decisione manageriale finale
	* [ ] Task 4: Valutazione stima parametri 
	* [ ] Task 5: Valutazione trade off tra parametri del modello
	* [ ] Prezzo ombra 

* Parametri sensibili, terminare nel pome:

https://elearning.unimib.it/mod/book/view.php?id=952591&chapterid=5478
