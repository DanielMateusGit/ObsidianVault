- [[#Cosa è Docker Compose?|Cosa è Docker Compose?]]
- [[#Come funziona Docker Compose?|Come funziona Docker Compose?]]
- [[#Come scrivere il file di configurazione?|Come scrivere il file di configurazione?]]
- [[#Come abilitare l'interazione da terminale?|Come abilitare l'interazione da terminale?]]
## Cosa è Docker Compose?

Docker compose è una maniera elegante per comprimere tutte le impostazioni di start di un container: 

***Invece di inserire in input da terminale le configurazioni di start, si scrivono dentro un file yaml.***

> [!Warning] Caso d'uso
> Docker compose è adatto a gestire gli ambienti di sviluppo locali.
> Non utilizzarlo in produzione.

> [!Warning] Non rimpiazza i Dockerfile
> Non è un sostitutivo delle immagini Docker, bensì un "tool complementare".

***
## Come funziona Docker Compose? 

Docker compose è incluso con l'installazione di Docker (quindi lo abbiamo già pronto all'uso).

Per utilizzarlo, invece:
* Si deve creare un file di configurazione chiamato docker-compose.yaml
* Si deve configurare opportunamente il file in formalo YAML (vedremo come)
* Si lancia con il comando docker compose up

***

## Come scrivere il file di configurazione?

La struttura base dei file di configurazione è la seguente: 

```yaml
# Le versioni di docker compose si trovano sul sito Docker
version: "3.8" 

# I vari container della nostra applicazione, ora saranno considerati
# come dei servizi
services: 
  mongodb:
  backend:
  frontend:
```

Ed ogni singolo servizio è configurabile come abbiamo fatto tramite il terminale:

```yaml

services:
  
  # servizio di db 
  mongodb:
    image: 'mongo'
    volumes: 
      - data:/data/db:ro
    environment:
      MONGO_INITDB_ROOT_USERNAME: max
      MONGO_INITDB_ROOT_PASSWORD: secret
	#posso come sempre utilizzare un env file
	env_file:
	  - ./env/mongo.env
  
  # servizio del be
  # notare che è basato su un'immagine (a differenza del primo)
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - '80:80'
    volumes:
      - logs:/app/logs 
      - ./backend:/app
      - /app/node_modules
    env_file:
       - ./env/backend.env
    depends_on:
       - mongodb

# Se utilizzo dei named volumes devono essere specificati anche qui
volumes: 
  data: 
  logs:
```

> [!Warning] Automatismi di Docker Compose
> Tutti i servizi (quindi Container) avviati da Docker Compose, avranno implicitamente:
> - Un --rm
> - Saranno associati ad una network (stesso file = stessa network)
> - Si può comunque utilizzare una network pre-esistente (aggiungendo un campo network)

***

## Come abilitare l'interazione da terminale?

Se vogliamo avviare un servizio che ha bisogno di interazione da terminale: 

```yaml
stdin_open: true
tty: true
```

***
