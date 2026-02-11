
LEZIONE 1: 

Vogliamo dockerizzare un' applicazione multi-container:
* MongoDB 
* NodeJS Back-end
* ReactJS Front-end (SPA)

Esplorando tutti i concetti visti fino ad ora.

***
LEZIONE 2:

Dockerizzazione dell' applicazione mongoDB:

```bash
docker run --name mongodb --rm  -d -p 27017:27017 mongo
```

In questo caso la configurazione del Container mongo è abbastanza facile perchè dalla documentazione risulta che automaticamente mongo occupa la porta 27017.

Ci basta mappare la porta 27017 del container con la porta 27017 della macchina host per poter accedere al servizio mongoDB del container da host.

Nel codice non dobbiamo cambiare nulla, ma possiamo semplicemente riferirci alla "porta nota mongoDB" per utilizzare il servizio.

***

LEZIONE 3:

Dockerizzazione dell'applicazione NodeJS. Scriviamo il Dockerfile.

```bash
FROM node

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 80
CMD ["node", "app.js"]
```

Buildiamo l' immagine: 

```bash
docker build -t goals-node .
```

Runniamo: 

Attenzione! Dobbiamo ancora mappare la porta 80 esposta dal container Docker con la nostra porta in locale. 

```bash
docker run --name goals-backend --rm -d -p 80:80 goals-node
```

Per connetterci con mongoDB, all' interno del codice dobbiamo utilizzare: 

```bash
	host.docker.internal:27017/url
```

**** 

LEZIONE 4:

Applicazione SPA front-end.
Creiamo un altro Dockerfile dentro la cartella di progetto del front.

```bash
FROM node

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

È praticamente cambiato solo il comando alla fine perchè stiamo utilizzando ReactJS. Buildiamo:

```bash
docker build -t goals-react .
```


Runniamo:

```bash
docker run --name goals-frontend --rm -it -p 3000:3000 goals-react
```


Attenzione! Le applicazioni ReactJS devono per forza essere runnate in --it mode.

***

LEZIONE 5: 

Aggiungiamo una rete per la comunicazione tra questi container.
(Miglioramento prestazioni, migliore gestione).

DIFFERENZA DA ORA: 

Non abbiamo creato la rete, abbiamo mappa porta a porta sulla nostra macchina i diversi container + utilizzato il servizio host sulla nostra macchina (mongo).

Questo può funzionare se stiamo sviluppando una cosa sul nostro PC. Su un server invece? Se non possiamo mappare i container e l' host porta a porta? 3

SI FA COSÌ: 

Creiamo una rete 

```bash
docker network create goals-net
```

Ora possiamo far partire tutti i container, ma inserendoli dentro una network.
Basta scrivere tutti i comandi di run con --network goals-net.

Ora, dentro il codice, invece di utilizzare host.internal.docker, utilizziamo direttamente il nome del container.

Occhio! Togliamo anche la mappatura delle porte. Ora non ci servono più.
***
LEZIONE 6:

Persistiamo i dati di mongoDB con un volume. Per capire come configurarlo, basta guardare la documentazione. Si aggiunge data:/data/db .

Si devono aggiungere anche altri v. di ambiente (guarda doc).
z
***

