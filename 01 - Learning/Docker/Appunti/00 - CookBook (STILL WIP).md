
***
## 5 semplici passaggi per containerizzare uno stack:

> [!Warning] 
> Questa è una roadmap di "cosa fare". Il riassunto di "come farlo" sarà descritto in seguito. Per capire nel dettaglio ogni passaggio, bisogna leggere il relativo capitolo.

Vogliamo utilizzare Docker per creare un ambiente di sviluppo in locale.
Per farlo, basta seguire dei semplici passaggi:

1. Scrivere un' immagine, ossia una "ricetta" di quello che ci serve per il nostro ambiente.
   
2. Una volta creata l'immagine, abbiamo bisogno di persistere dei dati: quelli GENERATI saranno salvati in volumi di memoria, E QUELLI CONSUMATI verranno condivisi con la macchina host (tramite una tecnica, chiamata bind-mount).
   
3. Per far comunicare più container, o semplicemente un Container con la macchina host, abbiamo bisogno di creare una RETE DI COMUNICAZIONE.
   
4. Infine, se avessimo bisogno di più servizi nel nostro stack dovremmo configurare PIÙ CONTAINER E FARLI PARTIRE INSIEME grazie a Docker compose.
   
5. Una volta svolti gestiti questi 4 aspetti (ricetta del container, persistenza dei dati, comunicazione di rete ed esecuzione multipla), non ci resta che buildare le varie immagini e fare partire i servizi.

****
## Immagini e Container

Un'immagine non è altro che una serie di istruzioni. Ogni tecnologia ha il suo "set" di istruzioni fondamentali (cercare online).

```bash
# Usa un'immagine base di Node.js
FROM node:18-alpine  

# Imposta la directory di lavoro nel container
WORKDIR /app  

# Copia i file package.json e package-lock.json
COPY package*.json ./  

# Installa le dipendenze
RUN npm install  

# Copia il resto del codice dell'applicazione
COPY . .  

# Espone la porta 3000 per l'app
EXPOSE 3000  

# Comando di avvio del container
CMD ["node", "server.js"]  

```

Questo file si salve come .dockerfile nel file system di progetto.
Per gestire l'immagine ed i container invece esistono i seguenti comandi: 

```bash
# Scarica un'immagine da Docker Hub  
docker pull ubuntu  

# Mostra le immagini disponibili localmente  
docker images  

# Costruisce un'immagine da una Dockerfile nella directory corrente  
docker build -t my_image .  

# Tagga un'immagine con un nuovo nome e tag  
docker tag my_image myrepo/my_image:latest  

# Carica un'immagine su Docker Hub  
docker push myrepo/my_image:latest  

# Avvia un container in modalità interattiva  
docker run -it --name my_container ubuntu /bin/bash  

# Esegue un container in background  
docker run -d --name my_daemon_container ubuntu  

# Elenca i container attivi  
docker ps  

# Elenca tutti i container (anche quelli spenti)  
docker ps -a  

# Ferma un container  
docker stop my_container  

# Riavvia un container  
docker restart my_container  

# Rimuove un container  
docker rm my_container  

# Rimuove un'immagine  
docker rmi ubuntu  

# Mostra i log di un container  
docker logs my_daemon_container  

# Accede a un container in esecuzione  
docker exec -it my_daemon_container /bin/bash  

```

Quindi per far partire un Container per l'applicazione (sempre quella NodeJS di esempio), basta salvare il file nel fs di progetto e poi: 

```bash
docker build -t my-node-app .
docker run -d -p 3000:3000 --name my-running-app my-node-app`
```

***

## Persistenza (volumi)

I volumi di un container sono come quelli fisici. Ne esitono di due tipi:

* Anonimi
* Con naming

Sono indipendenti dal Container, e persistono anche dopo la sua chiusura e rimozione. Stanno da qualche parte nella macchina host.

I Bind-Mount invece sono cartelle (memoria) della macchina host, condivisa con il Container. Si utilizza per l'aggiornamento di codice.

I comandi principali per la gestione di volumi e bind-mounts sono:

```bash
# Crea un container con un volume anonimo per la cartella /data
docker run -d --name my_container -v /data ubuntu

# Elenca i volumi Docker (compresi quelli anonimi)
docker volume ls

# Ispeziona un volume (scopre il path effettivo)
docker inspect my_container

# Rimuove un container, eliminando anche il volume anonimo
docker rm -v my_container
```

```bash
# Crea un volume nominato
docker volume create my_volume

# Usa un volume nominato con un container
docker run -d --name my_container -v my_volume:/app ubuntu

# Ispeziona un volume per vedere il percorso fisico
docker volume inspect my_volume

# Elimina un volume (deve essere inutilizzato)
docker volume rm my_volume

# Elimina tutti i volumi inutilizzati
docker volume prune
```

```bash
# Avvia un container e collega una cartella locale (/home/user/data) al container (/app/data)
docker run -d --name my_container -v /home/user/data:/app/data ubuntu

# Avvia un container con un bind mount in sola lettura
docker run -d --name my_container -v /home/user/data:/app/data:ro ubuntu
```

Facendo un esempio, sempre con la nostra applicazione NodeJS:

```bash
# STO CREANDO UN VOLUME CON NOME PER SALVARE I NODE_MODULES
docker run -d -p 3000:3000 \
  -v $(pwd):/app \
  -v my_node_modules:/app/node_modules \
  -w /app \
  node:18-alpine npm start
```

```bash
# In questo caso invece sto aggiungendo anche un bind-mount per il codice
# applicativo
docker run -it --rm -p 3000:3000 \ -v $(pwd):/usr/src/app \ -v node_modules:/usr/src/app/node_modules \ -w /usr/src/app \ node:18-alpine sh
```

***
## Concetto Chiave 4: Comunicazione tra container (Networking)

***
## Concetti Chiave 5: applicazioni multi-container (Docker compose).
***
