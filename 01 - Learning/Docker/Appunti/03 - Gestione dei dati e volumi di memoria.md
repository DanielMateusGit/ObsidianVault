- [[#Quali dati vivono all'interno di un Container?|Quali dati vivono all'interno di un Container?]]
- [[#Come condivido da Container->Host?|Come condivido da Container->Host?]]
- [[#Come si creano/gestiscono i Volumi?|Come si creano/gestiscono i Volumi?]]
- [[#Come condivido da Host->Container?|Come condivido da Host->Container?]]
- [[#Quando scelgo tra volumi, volumi anonimi e bound mounts?|Quando scelgo tra volumi, volumi anonimi e bound mounts?]]
- [[#Come ignorare un file durante la condivisione?|Come ignorare un file durante la condivisione?]]
- [[#Cosa sono le variabili di ambiente? Come si usano?|Cosa sono le variabili di ambiente? Come si usano?]]
- [[#Mettere variabili sotto sicurezza: i file .env|Mettere variabili sotto sicurezza: i file .env]]
- [[#Cosa sono i build arguments e come si utilizzano?|Cosa sono i build arguments e come si utilizzano?]]

## Quali dati vivono all'interno di un Container?

I Dati dentro un container sono: 

- Codice applicativo: salvato nella compilazione d' immagine.
- Dati temporanei di applicazione: salvato nella memoria interna del container.
- Dati permanenti: salvato con container o volumi.


> [!Warning] Ma attenzione!
> Il container è isolato dalla macchina host: ha una sua memoria ed un suo file system. Nemmeno altri container hanno visibilità della memoria del Container.

> [!Hint] La memoria del container non persiste
> Tutti dati che fanno parte della memoria del Container, una volta morto questo, VENGONO PERSI. Sono isolati e non persistono nella macchina host.

***
## Come condivido da Container->Host?

Tramite i volumi: cartelle nella MACCHINA HOST, che sono MONTATE COME VOLUMI dentro i container (esattamente, come su linux). 

Anche se muore il container, il VOLUME PERSISTE NELLA MACCHINA HOST.

> [!Hint] Cosa cambia rispetto a COPY
> Con COPY viene creato uno "snapshot del codice".
> Invece un VOLUME è un ponte tra la macchina host ed il container ospitato.

> [!Hint] E dove sta la condivisione?
> Posso associare ad un Container Docker un volume. 
> 
> Il Container Docker può anche essere rimosso totalmente, ma i dati salvati da esso rimarranno in questa cartella nell'host.
> 
> Poi? Ne faccio quello che voglio, posso ad esempio associare più container allo stesso volume.

***
## Come si creano/gestiscono i Volumi? 

Posso farlo nell'immagine Docker:

```bash
# Specifico una cartella destinazione (dentro il container)
# Specico una certella sorgente (macchina host)
VOLUME["/app/feedback",""]
```

Oppure durante l' avvio del Container:

```bash
# volume anonimo
docker run -v /app/data

# named volume
docker run -v /nome/volume:/app/data
```


> [!Hint] Volumi con nome vs anonimi
> I Volumi anonimi vengono eliminati con il Container (se questo ha il flag --rm).
> I Volumi con nome invece sono indipendenti dal Container (non soffrono --rm).

> [!Hint] Dove vivono "in memoria" i volumi?
> Sono cartelle nella macchina HOST, mappati dentro il FS del Container.
> Dove sono salvati (la posizione nella macchina HOST) è sconosciuto al programmatore.

Per gestire i volumi invece, esistono come per tutte le altre entità Docker:

```bash
# tutte le istruzioni disponibili
docker volume --help

# Vedere quali sono i volumi creati
docker volume ls

# creazione di volumi (con options etc)
docker volume create 

 # informazioni del volume
docker volume inspect

 # rimuovere il volume
docker volum rm nome_volume

```

> [!Warning] Inspect
> L'Inspect del volume è fondamentale per il debbugging. Generalmente quando non si riesce a collegare bene un Container con un Volume la spiegazione risidere in un' errata configurazione.

*** 

## Come condivido da Host->Container? 

Se volessi (ad esempio) condividere il codice applicativo tra Host e Container, dovrei affidarmi al BOUND MOUNTING:

Ossia un volume che ha come nome un INDIRIZZO SORGENTE DEL FS HOST e come destinazione L'INDIRIZZO DESTINAZIONE DEL FS DENTRO IL CONTAINER. 

```bash
docker run .... -v /host/path/codice:/destinazione/container
```

> [!Warning] 
> Su Windows / MacOS il bound mounting richiede un minimo di configurazione lato Docker Desktop. Leggere le pagine di Trouble shooting

> [!Warning] Cosa succede al COPY?
> Se ci fosse un'istruzione di COPY, ed il suo risultato fosse salvata in /folder, con il successivo BIND MOUNT si andrebbe a sovrascrivere il contenuto del /folder con il codice sorgente.
> 
> Il COPY quindi è inutile? Assolutamente no, in genere il COPY si fa durante i Deploy di applicazione ed il BOUND-MOUNT invece per lo sviluppo.

> [!Hint] E dove sta la condivisione?
> Modificare nella nostra macchina host la cartella sorgente, si riflette in una modifica nel container (perchè la cartella è effetivamente la stessa).
> 
> Se questa cartella fosse del codice applicativo, potremmo MODIFICARE IL CODICE DIRETTAMENTE NELLA MACCHINA HOST PER VEDERE LA MODIFICA NEL CONTAINER

> [!Hint] E gli aggiornamenti live?
> Ogni tecnologia ha il suo modo per aggiornare live il codice applicativo. Ad esempio NodeJS ha Nodemon, ma ognuno ha il suo (configurabile come dipendenza dentro l' immagine Docker)

***

## Quando scelgo tra volumi, volumi anonimi e bound mounts? 

In Docker abbiamo una regola molto importante, parlando di percorsi del file system: "IL PATH PIÙ SPECIFICO SOPRAVVIVE". 

Questo significa che ogni volume, può corrispondere ad una cartella specifica del FS Docker, e COESISTERE CON ALTRI VOLUMI E BIND-MOUNTS.

Per questo motivo:

* I volumi anonimi possono servire per ospitare dati temporanei essenziali per il funzionamento dell' applicativo, che NON DEVONO MAI ESSERE SOVRASCRITTI.
* I dati prodotti dal Container IN OUTPUT, che devono essere riutilizzati e magari condivisi invece devono essere salvati in un volume con nome
* I dati inseriti nel Container dalla macchina HOST invece devono essere condivisi tramite un BOUND MOUNT.
  
```bash
# volume anonimo
docker run -v /app/data

# named volume
docker run -v /nome/volume:/app/data

# bind mount 
docker run -v path/to/code:/app/code
```

Esempio?

Se volessi Dockerizzare un' applicazione NodeJS, utilizzerei:

* Un volume anonimo per salvare i node_modules (sono file essenziali per funzionamente che non cambiano mai).
* Un volume con nome per salvare l' output del container (magari file di log, o qualsiasi cosa)
* Un Bound Mount per collegare il codice applicativo al container.


```bash
docker run ... -v host_path/src:/app ... -v /app/node_modules ... -v
app_out:/app/feedback
```


In questo caso, per la regola d'oro di Docker, /app sarà del BindMount, ma non andrà ad eliminare o sovrascrivere le cartelle innestate, quindi /app/node_modules sarà del volume anonimo e /app/feedback del volume chiamato app_out. 

***
## Come ignorare un file durante la condivisione?


Utilizziamo il file .dockerignore:

Funziona esattamente come per git il .gitignore: i file specificati dentro il DockerIgnore vengono ignorati dai comandi Docker (come COPY):

```bash
#questo file si chiama proprio .dockerignore
node_modules
```

***

## Cosa sono le variabili di ambiente? Come si usano?


Le variabili di ambiente sono esattamente come quelle che si passano da console ad un qualsiasi programma.

Sono consumabili sia dal Container Docker che dall' applicazione che ospita. 
Si dichiarano nel docker file e valorizzano via docker run.

```bash
ENV PORT 80
EXPOSE $PORT
```

In questo modo, posso avere 80 come valore di default per "PORT", ma settarlo durante la fase di lancio del container:

```bash
docker run .... --env PORT=8080
```

Questo giustamente funziona perchè un' applicazione NodeJS (ad esempio), supporta il comando:

```typescript
app.listen(process.env.PORT)
```

Ogni framework ha il suo modo di recepire variabili di ambiente.

*** 

## Mettere variabili sotto sicurezza: i file .env

Si può creare un file .env:

``` bash
#questo è il contenuto del file .env
PORT=8080
```


Ed usarlo come configuratore durante la build: 

```bash
docker run ... etc ... --env-file ./.env
```


> [!Warning] Sicurezza
> Il file .env  si utilizza per ragioni di sicurezza.
> Quando viene letto le variabili di ambiente vengono caricate (on-demand, quind) dentro il Container, ma NON VENGONO SALVATE NELLA SUA MEMORIA.
> 
 Quando invece si passano con la docker run, le variabili di ambiente vengono salvate nella memoria del Container. 
> 
> Per dati sensibili è meglio che vengano caricato "on demand", invece di far parte del Container. NON BISOGNA MAI DISTRIBUIRE UN CONTAINER CHE HA IN MEMORIA SALVATE INFORMAZIONI SENSIBILI.

*** 
## Cosa sono i build arguments e come si utilizzano?

Non fa parte del codice. Non è una variabile di ambiente dell' applicazione.
Sono invece delle variabili utilizzabili dentro l' immagine Docker, e quindi configurabili sono durante la build di immagine.

```bash
#dentro il Dockerfile
ARG DEFAULT_PORT=80
```


Posso utilizzare questa variabile dentro il Dockerfile:

```bash
ENV PORT DEFAULT_PORT
EXPOSE $DEFAULT_PORT
```

E valorizzarla in fase di build: 

```bash
docker build ... --build-arg DEFAULT_PORT=8000
```


> [!Warning] Ogni build argument è un Layer
> Bisogna valutare questo aspetto. Una volta modificata una variabile di build, i layer successivi vengono buildati nuovamente.

> [!Warning] Differenza tra env e build args?
> Le build args interessano il build del Container. Possono modificare il contenuto del Container.
> 
> Le variabiili env invece si settano durante il lancio di un' applicazione già buildata dentro un Cotainer già esistente. Servono al codice in esecuzione per poter gestire dei flussi di esecuzione alternativi.
> 
> Vivono due fasi di vita del container diversi, configurano cose diverse.

***
