
## Cosa è una CTE ricorsiva: 

Una CTE ricorsiva ha due componenti principali:

1. ***Caso base (anchoring member)*:** La parte non ricorsiva della query che rappresenta il punto di partenza.
   
2. ***Parte ricorsiva*:** La query che si richiama ricorsivamente, utilizzando il risultato intermedio fino a quando una condizione di termine viene raggiunta.

## Pseudocodice 

```sql
WITH RECURSIVE cte_name (column1, column2, ...) AS (
    -- Caso base: selezione iniziale
    SELECT initial_column1, initial_column2, ...
    FROM base_table
    WHERE initial_condition
    
    UNION ALL
    
    -- Parte ricorsiva: selezione ricorsiva
    SELECT recursive_column1, recursive_column2, ...
    FROM cte_name -- Qui si richiama la CTE stessa
    JOIN related_table
    ON cte_name.some_column = related_table.some_column
    WHERE recursive_condition
)
SELECT * FROM cte_name;
```

## Esempio 

### **Problema**

Hai un sistema di gestione delle cartelle in cui:

- Ogni cartella è rappresentata da un identificativo (`folder_id`), un nome (`folder_name`), un riferimento al genitore (`parent_id`), e un'indicazione se la cartella è salvata su un file system (`is_in_filesystem`).
- Una cartella può avere sottocartelle, formando una struttura ad albero.
- Le cartelle senza un valore `parent_id` sono considerate **radici** della struttura.
- Se una cartella non è salvata su un file system (`is_in_filesystem = FALSE`), è considerata **orfana**, e tutte le sue sottocartelle sono anch'esse orfane.

#### **Obiettivo**

Scrivere una query ricorsiva che:

1. Permetta di risalire la gerarchia delle cartelle partendo da una qualsiasi cartella figlia fino alla radice.
2. Tracci ogni percorso dalla cartella di partenza fino al suo antenato più alto.
3. Permetta di determinare se una cartella, insieme alla sua catena di antenati, è connessa a un file system o è orfana.

#### **Output desiderato**

La query deve restituire:

- L'identificativo di ciascuna cartella (`folder_id`).
- Il nome della cartella (`folder_name`).
- L'identificativo del genitore (`parent_id`).
- L'indicatore se la cartella è nel file system (`is_in_filesystem`).
- L'identificativo della cartella radice associata al percorso (`root_folder_id`).

#### Soluzione: 

```sql
WITH RECURSIVE FolderHierarchy AS (
    -- Caso base: inizia con tutte le cartelle
    SELECT folder_id, folder_name, parent_id, is_in_filesystem, folder_id AS root_folder_id
    FROM folders

    UNION ALL

    -- Parte ricorsiva: risale alla cartella genitore
    SELECT f.folder_id, f.folder_name, f.parent_id, f.is_in_filesystem, fh.root_folder_id
    FROM folders f
    JOIN FolderHierarchy fh ON f.folder_id = fh.parent_id
)
```


## Come funziona? 

### **Tabella `folders`**

|folder_id|folder_name|parent_id|is_in_filesystem|
|---|---|---|---|
|1|root|NULL|TRUE|
|2|subfolder1|1|TRUE|
|3|subfolder2|2|TRUE|
|4|orphan1|NULL|FALSE|
|5|orphan2|4|FALSE|
|6|orphan3|5|FALSE|

Questa struttura ha un percorso radicato che parte da `root` e termina in `subfolder2`, e un percorso orfano che parte da `orphan3` e risale fino a `orphan1`.

---

### **Caso Base: Iterazione 0**

La query comincia selezionando tutte le cartelle per iniziare il processo.

#### Risultato iniziale (caso base)

|folder_id|folder_name|parent_id|is_in_filesystem|root_folder_id|
|---|---|---|---|---|
|1|root|NULL|TRUE|1|
|2|subfolder1|1|TRUE|2|
|3|subfolder2|2|TRUE|3|
|4|orphan1|NULL|FALSE|4|
|5|orphan2|4|FALSE|5|
|6|orphan3|5|FALSE|6|

---

### **Iterazione 1: Risalita al primo genitore**

Il primo passo ricorsivo unisce ogni cartella con il suo genitore.
Questo lo si fa tramite la JOIN del caso passo. 

Rimangono solamente le righe in grado di trovare una corrispondenza con la tabella prodotta dal caso base.
#### Unione con i genitori

- `folder_id = 2` ha come genitore `folder_id = 1`
- `folder_id = 3` ha come genitore `folder_id = 2`
- `folder_id = 5` ha come genitore `folder_id = 4`
- `folder_id = 6` ha come genitore `folder_id = 5`

|folder_id|folder_name|parent_id|is_in_filesystem|root_folder_id|
|---|---|---|---|---|
|1|root|NULL|TRUE|2|
|2|subfolder1|1|TRUE|3|
|4|orphan1|NULL|FALSE|5|
|5|orphan2|4|FALSE|6|

---

### **Iterazione 2: Risalita al secondo genitore**

Il secondo passo ricorsivo continua la risalita per le cartelle che hanno ancora un genitore.

Si fa di nuovo la JOIN tra le righe iniziali della tabella ed il risultato prodotto all'interazione 2.

Naturalmente rimangono solo quelle che riescono a soddisfare la JOIN.

- `folder_id = 2` risale fino a `folder_id = 1`
- `folder_id = 5` risale fino a `folder_id = 4` (e termina qui perché `parent_id = NULL`)

|folder_id|folder_name|parent_id|is_in_filesystem|root_folder_id|
|---|---|---|---|---|
|1|root|NULL|TRUE|3|
|4|orphan1|NULL|FALSE|6|

---

### **Iterazione 3: Risalita finale**

L'ultima risalita verifica i genitori rimanenti:

- `folder_id = 1` termina perché `parent_id = NULL`
- `folder_id = 4` termina perché `parent_id = NULL`

---

