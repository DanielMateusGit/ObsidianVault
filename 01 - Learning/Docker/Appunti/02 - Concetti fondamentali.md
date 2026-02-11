
- [[#Immagini Docker e Container|Immagini Docker e Container]]
- [[#Come costruire una Docker img base?|Come costruire una Docker img base?]]
- [[#Come avviare il container?|Come avviare il container?]]
- [[#Come funziona la Build?|Come funziona la Build?]]
- [[#Come far Partire i container?|Come far Partire i container?]]
- [[#Come Eliminare le immagini/container?|Come Eliminare le immagini/container?]]
- [[#Come importare/esportare file da un container?|Come importare/esportare file da un container?]]
- [[#Come organizzare i container? Naming e Tagging|Come organizzare i container? Naming e Tagging]]

## Immagini Docker e Container

Le immagini sono le "ricette" contenenti:

- Le istruzioni necessarie per creare il container.
- Il codice da caricare/eseguire all'interno del container.
- Quali sono i tools necessari per eseguire il codice caricato.

Un Container invece è l' istanza di un'immagine (posso generare più container da una sola immagine).


> [!Hint] Curiosità
> Ci sono delle immagini pre-impostate. Basta scaricarle e farle partire, sono "plug and play" e non hanno bisogno di ulteriori configurazioni. 
> 
> Sono disponibili nel sito dockerhub:
> 
>  ```bash
> 	# -it sta per "versione interattiva" : fornisce un
> 	# terminale dentro il container con cui interagire
> 	docker run -it rust
> ```

***

## Come costruire una Docker img base?

Immaginiamo di voler dockerizzare la seguente applicazione:

![[nodejs-app-starting-setup.zip]]

Per Dockerizzarla abbiamo bisogno di creare un Dockerfile (immagine docker) nel file system di applicazione.

Questo Dockerfile, conterrà le istruzioni base:

- FROM
- WORKDIR
- COPY
- RUN
- EXPOSE
- CMD

L' immagine sarà la seguente:

```dockerfile
# Questa serve per selezionare un' immagine Docker di partenza
# In questo caso partiamo dall' immagine officiale Docker
FROM node

# Questo dice a Docker che tutti i comandi da ora in avanti saranno eseguiti
# dentro questa cartella (nel container)
WORKDIR /app

# Il primo punto -> specifica l' inidirizzo dell' host
# Il secondo indirizzo -> specifica un indirizzo dentro il container
# In questo caso stiamo dicendo "copia tutto il contenuto" del primo indirizzo (host)
# Dentro il percorso del secondo indirizzo (che sta nel container)

# Occhio! Se ho settato prima una WORKDIR -> tutti gli indirizzi che andrò a 
# specificare saranno relativi alla WORKDIR (qui quindi in realtà gli sto
# dicendo di copiare dentro /app )
COPY . /

# Come step successivo dobbiamo eseguire "npm install" per installare le dipendenze
# del progetto NodeJS (come faremmo nella nostra macchina normale)
RUN npm install

# Questo comando espone una porta del container all' host
# Questo lo stiamo facendo perchè questa applicazione ascolta richiesta 
# su questa porta
EXPOSE 80

# Una volta preparato tutto l' ambiente
# facciamo partire l' applicazione
# ATTENZIONE! cmd è diverso da RUN perchè esegue un comando alla fine
# della creazione del container. Quindi -> con il container già in esecuzione
# RUN invece, durante la creazione del container.

CMD ["node", "server.js"]
```

> [!Hint] Le immagini sono read-only
> 
> Nel momento in cui creiamo il Container, tramite il comando COPY, copiamo il codice dentro il container.
> 
> Per aggiornare il codice del container, bisogna fare NUOVAMENTE LA BUILD e creare un nuovo container per avere la nuova versione di codice aggiornata.

***

## Come avviare il container?

1. Dentro la cartella dove risiede il Dockerfile:
   
```bash
docker run build .
```

2. Il precedente comando produrrà in output un codice, che servirà per lanciare il container:
   
```bash
docker run -p 3000:80 b123043c35a6
```   
   

> [!Warning] Attenzione!
> Il container va lanciato mappando la porta 80 del container con una porta della macchina host. 
> 
> Questo deve avvenire perchè l' applicazione server che stiamo dockerizzando ascolta richieste sulla porta 80 (del container), con cui dobbiamo interagire per mezzo dell' host sulla porta 3000.

***

## Come funziona la Build? 

Ogni comando in una docker image è uno "step" nella build.
Il risultato di ogni step, viene cachato.

Ogni step cachato, prende il nome di "layer di compilazione".
Quando viene buildata nuovamente l'immagine, a meno di modifiche delle istruzioni, vengono utilizzati i layer cachati.

> [!Warning] Quando invece modifico un comando?
>Viene ri-compilato il layer completamente (cache ignorata).
>Questo, a cascata, causa la re-build dei layer successivi (in ordine di comparsa nell' immagine).

Questo significa, ad esempio, che questa img:

```typescript
FROM node
WORKDIR /app
COPY . /app
RUN npm install
```

è meno performante di :

```typescript
FROM node
WORKDIR /app
COPY package.json
RUN npm install
COPY . /app
```


COPY cambia ogni volta che io voglio aggiornare il codice dell' applicazione e scatena la re-build della npm install. 

Questo è un errore: npm install deve partire solo in seguito ad un cambiamento delle dipendenze (package.json).

Facendo COPY alla fine e tenendo le installazioni dei pacchetti NPM all' inizio, la npm install causa una re-build del layer corrispondent, solo se cambia il package.json (non se cambia il codice applicativo).

***
## Come far Partire i container?

Esistono diversi comandi docker "fondamentali" per la gestione delle immagini.
Sono consultabili digitando il comando : 

```bash
docker --help
```

I comandi fondamentali per far partire i container sono:

```bash
# mostra tutti i container creati
docker ps -a 

# fa partire un container, ma senza terminale 
# (niente log o iterazioni con il container)
docker start @id_container

# fa partire il container con interazione da terminale
docker run @id_container
```


> [!Hint] Docker run vs start
> Run => funziona in modalità attached (occupa il terminale)
> Start => funziona in modalità detached (lascia il terminale libero) 
> 
> Scegliere d' accordo alla necessità: se devo vedere dei log di applicazione, sceglierò la modalità attached.

> [!Warning] Attivare le diverse modalità
> Attach e Detached sono modalità di default per run e start, ma possiamo comunque specificare la modalità con cui vogliamo che parta il container con:
> 
> docker run -d ...etc...
> docker run -a ...etc...
> 
> È anche possibile utilizzare docker logs => per vedere i precedenti log del container.
> 
> Flaggando logs con -f (follow) ho praticamente la modalità attached.
> 
> Se invece vogliamo rendere attached un container già in esecuzione, possiamo usare: docker attach CONTAINER.

> [!Warning] Una terza modalità: quella interattiva
> 
> La modalità -d ed -a servono solo per poter visualizzare il terminale di applicazione (l'output).
> 
> Alcune applicazioni (CLI) necessitano anche di interazione utente in input.
> Per questo, hanno bisogno di un terminale che ascolti.
> 
> La modalità docker per abilitare l' input utente da terminale è la modalità interattiva. Per abilitare la modalità interattiva si usa -it.
> 
> Quindi questo aggiunge un terzo caso: quando dobbiamo interagire con il programma, e non solo vedere l' output.

***
## Come Eliminare le immagini/container? 

I fondamentali per eliminale le immagini/container, invece:

```bash
# vedere i container creati
docker ps -a 

#rimuove i container (devono essere in stato di stop)
docker rm @container_name 

# vedere tutte le immagini create
docker images

# rimuovere un' immagine
docker rmi @image_id

# rimuovere tutte le immagini
docker rmi 

# attenzione! se voglio eliminare un' immagine, devo aver
# eliminato prima i container su cui si basa quell'immagine
# il seguente comando elimina solo quelle eliminabili
docker image prune 

#rimuovere tutti i container non startati
docker container prune

## metadai di un' immagine
docker image inspect @image_id
```

Un comando molto utile invece è --rm :
Questo flag permette di rimuovere un container automaticamente, una volta stoppato.

```bash
docker run --rm @container_name
```

***

## Come importare/esportare file da un container?

Per copiare un file dentro un container già avviato:

```bash
docker cp cartella_src/. @nome_container:/cartella_dest
```

Se cartella_dest non esiste, verrà creata.

Invertendo gli indirizzi, otteniamo il comportamento contrario:

```bash
docker cp @nome_container:/cartella_dest cartella_src
```

***
## Come organizzare i container? Naming e Tagging

Quando viene salvata un' immagine e buildato un container vengono a loro assegnati dei nomi e dei tag (automaticamente).

Questi nomi/tag possono essere rinominati.

```bash
# Assegnare un nome ad un container
docker run -p 3000:80 -d -rm --name new_custom_name @container_id

# Assegnare un name + tag alle immagini
docker build -t img_name:latest_tag .

# In questo caso, la creazione del container diventa
docker run -p 3000:80 -d --rm --name cont_name img_name:latest_tag
```

Il senso di name e tag sono un po' simili a quelli di git.

Con il nome si setta un "nome generale del container", invece con il tag si può settare informazione aggiuntiva (una variante? un versionamento?)


> [!Warning] Tag
> L' utilizzo più utile dei tag è quello di versionare le dipendenze.
> 
> Un' applicazione può aggiornare la versione di nodeJS (ad esempio). 
> Magari vorremmo poter tenere sia la vecchia che la nuova versione. Per esprimere questo cambiamento ecco che entra in gioco il tag.
> 

***
