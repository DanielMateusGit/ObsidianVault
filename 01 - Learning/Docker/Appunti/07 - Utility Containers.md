- [[#Cosa sono gli utility container?|Cosa sono gli utility container?]]
- [[#Come creo un utility container?|Come creo un utility container?]]
- [[#Come lancio comandi in un utility container?|Come lancio comandi in un utility container?]]
## Cosa sono gli utility container? 

Sono dei container che non detengono un codice, ma fanno da "ambiente di esecuzione di comodo".
***
## Come creo un utility container?

Il modo più semplice è quello di utilizzare le immagini ufficiali docker:

```
docker run -it -d node
```

Ma si può anche creare un'immagine con ENTRYPOINT:

```bash
FROM node:14
WORKDIR /app
ENTRYPOINT ["npm"]
```

Lanciando qualsiasi istruzione nel container, questa sarà preceduta da quanto specificato come entry-point. Nell'esempio soprà interperllerò sempre NPM.

****
## Come lancio comandi in un utility container?

Si fa un run del container specificando l'istruzione da eseguire, nel seguente modo:

```bash
docker run -it node-util npm init
```

Con entry point invece:

```bash
docker run -it node-util init
# non devo metter npm perchè ho già messo l' entry-point
```

Altro esempio:
```bash 
docker run -it -v /path/to/code:/app node-util install
```

Questo fa un bind-mount tra host e container. Installa i pacchetti nodeJs dentro il file system di progetto e poi si chiude. Per utilizzare questa feature con docker compose: 

```bash
docker compose run COMANDO
```
***