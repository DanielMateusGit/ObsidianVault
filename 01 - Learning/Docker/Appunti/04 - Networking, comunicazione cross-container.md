- [[#Con chi comunica un Container?|Con chi comunica un Container?]]
- [[#Come fare comunicare il container con il web? (API Calls)|Come fare comunicare il container con il web? (API Calls)]]
- [[#Come fare comunicare il container con l' host?|Come fare comunicare il container con l' host?]]
- [[#Come far comunicare il container con un altro container?|Come far comunicare il container con un altro container?]]
- [[#Docker Networks (maniera più elegante di gestire la comunicazione)|Docker Networks (maniera più elegante di gestire la comunicazione)]]

## Con chi comunica un Container?

Un Docker container ha bisogno di : 
 * Comunicare con API esterne
 * Comunicare con la macchina host (db in locale ad esempio)
 * Comunicare con un altro container 

***
## Come fare comunicare il container con il web? (API Calls)

I Container possono mandare richieste al web (API Calls) "out of the box" senza alcuna configurazione particolare.

***
## Come fare comunicare il container con l' host?

Il Container, può interpellare l'host tramite l' indirizzo:

```bash
host.docker.internal
```

Questo è un percorso riconosciuto da docker per riferirsi a localhost.
Si può utilizzare OVUNQUE NEL CODICE: 

```bash
# URL per fare una richiesta a un db mongo nella macchina locale
'mongodb://host.docker.internal:27017/favorites' 
```

La chiamata la gestisco DENTRO IL CODICE APPLICATIVO.

***
## Come far comunicare il container con un altro container?

Ad ogni container corrisponde un indirizzo IP, per mezzo del quale questo può essere interpellato. Per conoscerlo:

```bash
# Ispezioniamo il container contenente mongo
docker inspect docker_container
```

Del Json risultante, ci interessa il valore "NetworkSettings/IPAddress".
Per comunicare con il Container, basta fare una chiamata con questo IPAddress come base. La chiamata la gestisco DENTRO IL CODICE APPLICATIVO.
***

## Docker Networks (maniera più elegante di gestire la comunicazione)

Se due Container comunicano e l'IP di uno dei due per qualsiasi motivo cambia, rompiamo la comunicazione. L'approccio con IP funziona, ma è "hard-coded".


Possiamo creare una network ed aggiungere Container. Tutti i container dentro la network potranno comunicare tramite il naming.

```bash
# creiamo un network
docker network create appNet

# primo container (aggiungiamo la rete)
docker run -d --name mongodb --network appNet mongo

# secondo container (aggiungiamo la rete)
docker run --name application --network appNet -d --rm -p 3000:3000 appImg
```

Dentro il codice dei container possiamo usufruire della rete. 
INVECE DELL' INDIRIZZO IP DEGLI ALTRI CONTAINER, possiamo usare direttamente il NOME:

```typescript
server.listen(mongo);
```

> [!Hint] Chi risolve l'IP? 
> E la risoluzione dell' IP sarà automatica, ed affidata a Docker.
Container nella stessa rete potranno "chiamarsi" in questo modo.

> [!Warning] Network sono un' altra entità a sè stante
> E giustamente come tutte le altre entità Docker ha i suoi comandi (visualizzabili con --help).

***
