
- [[#Cosa è Docker?|Cosa è Docker?]]
- [[#Docker Setup|Docker Setup]]
- [[#Eseguire un primo Container Docker|Eseguire un primo Container Docker]]
- [[#Stoppare un Container|Stoppare un Container]]
## Cosa è Docker? 

Container: 

"Unità di codice standardizzata", ossia del codice + tutte le dipendenze per eseguire tale codice, impacchettate in un "ambiente di sviluppo eseguibile". 

> [!Hint] Esempio
> Docker è un tool per creare questi ambienti di sviluppo. 
> 
> Un Container docker potrebbe essere (ad esempio) un' applicazione .NET (il codice) + tutto il necessario per eseguirla (.NET Core, C#, Sql Server etc...). 
> 
> Il Container fornisce un ambiente di sviluppo "runnabile", nel quale possiamo eseguire la nostra applicazione.

> [!Polemichina] Perchè usiamo Docker e non le macchine virtuali?
> 
> Le macchine virtuali:
> 
> - Sono dei calcolatori "veri e propri" emulati su un calcolatore host.
> - Hanno bisogno di configurazioni abbastanza complesse.
> - Non è sempre garantito che possano essere riprodotte su un altro calcolatore (non facilmente).
>   
> I Container Docker: 
> 
> - Sono solo pacchetti/dipendenze/moduli necessari ad eseguire un codice (non calcolatori emulati per intero).
> - La configurazione richiede solo un file (scritto dal programmatore).
> - Per poter riprodurre un Container su un altro calcolatore basta che questo disponga del Docker Engine (che fa da middleware) + file di configurazione Docker per far partire il container.

***

## Docker Setup

L' installazione Docker dipende dal SO della macchina ospitante.

Sempre su sistemi diversi da Linux, è consigliato installare Docker Desktop + Docker Tools.

Invece, su Linux, basta installare il Docker da linea di comando (perchè supportato nativamente.

Link utili:

https://labs.play-with-docker.com/
https://docs.docker.com/desktop/setup/install

È utile anche installare (se si usa Visual Studio Code) l' estensione Docker ufficiale di Microsoft: https://code.visualstudio.com/docs/containers/overview


> [!Curiosità] Cosa abbiamo installato?
> Su sistemi operativi che non sono Linux, viene installato il Docker Engine.
> 
> Il Docker Engine è una macchina virtuale su cui poi verrà eseguito Docker. 
> Linux non ne ha bisogno perchè lo supporta nativamente. 
> 
> Gli altri sistemi operativi lavoreranno comunque con Docker (eseguito su questa singola macchina virtuale).
> 
> In più abbiamo:
> - Docker Desktop : un CLI + Interfaccia per l' utilizzo di Docker.
> - Docker Hub : tool per la distribuzione e condivisione Container.
> - Docker Compose : un tool per "scrivere container più complessi".

***

## Eseguire un primo Container Docker 

Questo è il "Hello, world!" della Dockerizzazione. Per eseguire un primo Container (e runnare un' applicazione di esempio):


Scaricare ed aprire il seguente progetto NodeJS (molto semplice) con Visual Studio Code:

![[01 - Learning/Docker/Resources/first-demo-starting-setup.zip]]

Aggiungere alla cartella di progetto il seguente file: 

![[02 - Learning/Udemy - Learn Docker, Docker Compose, Multi-Container Projects, Deployment and all about Kubernetes from the ground up!/Resources/Dockerfile]]

Ed eseguire il file di configurazione in console con il comando:

```bash
docker build . 
```

Questo comando andrà a buildare l' immagine Docker (scaricando i pacchetti necessari per runnare l' applicazione NodeJS).

La build produrrà un messaggio finale del tipo:

```bash
Successfully built moby-201408b2821828df1f61e0
```

Ed infine, per avviare il Container, basta copiare il codice risultante dalla build: 

```bash
docker run -p 3000:3000 moby-201408b2821828df1f61e0
```

Questo comando è composto da due parti: 

* docker run (comando per runnare un Container).
* -p 3000:3000 è un mapping tra una porta del nostro calcolatore ed una porta del container.
* moby-201408b2821828df1f61e0 è l'identificativo del container (prodotto dalla build).

***

## Stoppare un Container

Una volta runnato il container, la console su cui è in esecuzione rimane "bloccata".

Per fermare il container 

```bash
# Questo comando permette di vedere tutte le informazioni dei container
# attualmente in esecuzione tra cui, molto importante, l' identificativo
# di ognuno
dockes ps 

# Una volta preso l' id del container che si vuole stoppare, basta
# invocare questo comando puntando al container tramite il suo id
docker stop @Id_container
```

***

