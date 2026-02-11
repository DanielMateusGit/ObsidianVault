
LEZIONE 1:

Differenza tra ambiente locale e production. Cosa cambia? 

* Non abbiamo in Bind-Mount (si usa COPY).
* Sarà necessario introdurre uno step di build dell'applicazione.
* Progetti multi-container dovranno essere hostati in macchine diverse.

***

ESEMPIO MOLTO SEMPLICE: NodeJS stand-alone application

Passaggi da seguire:

* Installare Docker su una macchina remota (ssh)
* Fare push e pull dell'immagine Docker
* Runnare il container sulla macchina remota

Per installare Docker su una macchina remota, bisogna usufruire di un hosting provider che lo supporti. I più famosi sono: AWS, Azure e Google Cloud.

***

ESEMPIO CONCRETO:

AWS EC2. Passaggi: 

1. Creare e lanciare un' istanza di EC2, VPC e security group
2. Configurare security group per esporre le porte necessarie a WWW
3. Connettersi all' istanza da remoto tramite SSH, installare docker e runnare i container

*** 

LEZIONE 2: 

INTRODUZIONE DI AWS ed EC2:

Iscriversi (serve una carta di pagamento).

1. Per lanciare l'istanza:
AWS Management Console => Cercare EC2 => Launch instance.

2. Successivamente, per capire quale tipo di istanza lanciare:

Choose AMI : Amazon Linux 2 AMI 
Instance Type: Quello contrassegnato come "free"
Configure instance details: controllare che ci siano i valori di default

Review and Launch con opzione "create a new key pair".
La KeyPair è da scaricare e tenere in un posto sicuro.

3. Utilizzare ssh per stabilire una connessione con EC2. Per fare questo è meglio utilizzare il WSL 2 (oppure direttamente Linux se si può).

	Cliccando su "CONNECT" nella dashboard che mostra l' istanza della nostra macchina EC2 -> abbiamo tutte le coordinate per vedere COME COLLEGARCI ALL'ISTANZA TRAMITE SSH.

	
****

COME INSTALLARE DOCKER? 

Con il terminal connesso tramite ssh: 

```bash
sudo amazon-linux-extras install docker

# una volta installato, per partire:
sudo service docker start (+ flags)
```

> [!Warning] Comando deprecato
> Il comando potrebbe essere cambiato, comunque sta tutto nella documentazione AWS/Docker

***

COME PUSHARE L' IMMAGINE NEL CLOUD?

Abbiamo due opzioni fondamentalmente: 
1. Fare il Deploy di progetto (della sorgente) e poi lanciare i comandi docker nel terminale connesso tramite ssh
2. Possiamo Deployare un'immagine già buildata

Il secondo metodo è abbastanza conviente. Una volta deployata l'immagine già buildata, basta lanciare nella macchina remota "docker run".

Bisogna semplicemente creare un repository con Docker Hub e seguire le istruzioni
(quelle che si trovano nella pagina del repository).

> [!Hint] Come fornire un'immagine buildata alla macchina AWS?
> Semplice! Con Docker Hub. Buildiamo l'immagine, la carichiamo su Docker Hub, e ne facciamo il pull dalla macchina remota con il terminale cc ssh.

***

RUN DI APPLICAZIONE E PUBBLICAZIONE DELL'APP

Una volta fatta la pull dell'immagine buildata, semplicemente si lancia come sempre da terminale (utilizzando sudo prima del comando docker, unica differenza).

Ora l' applicazione sta andando sulla macchina host remota,ma ci sono delle restrizioni. Esiste un security group -> che è una whitelist di IP che possono contattare la macchina da remoto (tra questi, ci siamo noi che usiamo ssh).

Andando nella pagine dell'istanza (macchina remota) in basso ci sono due informazioni fondamentali: 

* Outbound Rules (chi può contattare la macchina -> verso l' esterno)
* Inbound Rules (da chi può essere contattata la macchina <- verso l'interno)

Dobbiamo editare le InBound rules -> aggiungere HTTP (con porta) + Source Anywhere.
Salvando questa nuova info -> possiamo accedere alla macchina host TRAMITE IL SUO INDIRIZZO IP.

> [!Hint] SIAMO ONLINE
> SIIIIIIIUUUUUUUUUUUU

***

AGGIORNARE IL CONTAINER / L'IMMAGINE

Si deve: 

* Buildare nuovamente l'immagine 
* Pushare l'immagine buildata in DockerHub
* Stoppo il container in remoto con ssh
* Runno nuovamente il container in remoto con ssh
* Infine, con il container ottenuto faccio docker pull

L' ultima istruzione fa pull della versione più recente del container a sistema.

***

AUTOMATIZZARE L'APPROCCIO:

Con ssh è sicuramente comodo gestire un container su un host remoto,ma questo approccio funziona per progetti modesti. 

Gestire un grosso progetto (magari con microservizi ed altro) con solo ssh, diventa un po' complicato. Per questo, ci sono sistemi che possono automatizzare il processo di deploy sulla macchina remota.

Si utilizza AMAZON ELASTIC CONTAINER SERVICE (a pagamento).

***
Amazon ECS

La compilazione del container è "wizard", l' unica cosa a cui si deve "prestare attenzione" è quella di puntare al container buildato su DockerHUB.

Tutto ciò che era lanciabile da termina con Docker Run è configurabile (con un altro nome ed una UI).

***

COME AGGIORNARE IL CODICE 

* Modifichiamo il codice 
* buildiamo di nuovo 
* tagghiamo nuovamente 
* si pusha su docker hub
* Andare su AWS nei task Definitions => Create a new revision => si Crea un nuovo task 
* Si avvia il task

***