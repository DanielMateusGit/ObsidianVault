---
tags:
  - Algoritmi
  - Algoritmi/Programmazione_dinamica
  - Programmazione_dinamica
---

- [[#Quando un problema soddisfa la proprietà di sotto-struttura ottima?|Quando un problema soddisfa la proprietà di sotto-struttura ottima?]]
- [[#La soluzione finale di un problema contiene al suo interno le soluzioni dei sotto problemi.|La soluzione finale di un problema contiene al suo interno le soluzioni dei sotto problemi.]]
- [[#Come trovare la proprietà di sotto struttura ottima di un problema?|Come trovare la proprietà di sotto struttura ottima di un problema?]]
- [[#Esempi|Esempi]]

# Sotto-struttura ottima

## Quando un problema soddisfa la proprietà di sotto-struttura ottima?

Un problema soddisfa la proprietà di sotto-struttura ottima se una sua soluzione ottimale può essere ottenuta combinando soluzioni ottimali dei suoi sotto-problemi.

> La soluzione ottima del problema contiene al suo interno le soluzione ottime dei sotto problemi.

> [!Hint] Cosa si intende per sotto problemi?
> Un sotto problema si ottiene riducendo l' input e considerando tutte le condizioni che portano un problema complesso a diventare il più semplice possibile.
> 
> Ad esempio: 
> I sotto problemi di un calcolo su n matrici mxm, potrebbero essere:
> 
> - Lo stesso problema di calcolo considerando solo due matrici alla volta.
> - Lo stesso problema di calcolo considerando una  porzione ridotta (m-k x m-k) di tutte le matrici.
> - Un mix tra i due.

---

## Come trovare la proprietà di sotto struttura ottima di un problema?

La proprietà di sotto-struttura ottima sarà un insieme "di regoline" che descriveranno come, dato un sotto-problema del problema originale, risolvere tale sotto-problema e generare l' insieme di sotto-problemi successivi.

Per trovarla, bisogna seguire uno schema:

- Dimostrare che una soluzione del problema consiste nel fare una scelta. Questa scelta genera porta ad uno o più sotto-problemi da risolvere.
- Per un dato problema, supporre di conoscere la scelta che porta alla soluzione ottima.
- Fatta la scelta, determinare quali sono i sotto problemi che ne derivano e caratterizzare lo spazio dei sotto problemi risultante dall'effettuare tale scelta.
- Dimostrare che le soluzioni dei sotto-problemi devono essere necessariamente soluzioni ottime. In genere si fa per assurdo.

La soluzione ottima sarà una composizione di tutti questi sotto problemi.

---

## Esempi:

[[00 - Università/Algoritmi 2/Appunti (Teoria)/01 - LCS/02 - Caratterizzazione della soluzione ottima]]
