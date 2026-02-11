---
tags:
  - Algoritmi
  - Programmazione_dinamica
---
#Algoritmi/Programmazione_dinamica/sotto_stuttura_ottima

Quando un problema soddisfa la proprietà di sotto-struttura ottima?
;
Un problema soddisfa la proprietà di sotto-struttura ottima se una sua soluzione ottimale può essere ottenuta combinando soluzioni ottimali dei suoi sotto-problemi.

Come trovare la proprietà di sotto struttura ottima di un problema?
;
La proprietà di sotto-struttura ottima sarà un insieme "di regoline" che descriveranno come, dato un sotto-problema del problema originale, risolvere tale sotto-problema e generare l' insieme di sotto-problemi successivi.
***
Per trovarla, bisogna seguire uno schema:
- Dimostrare che una soluzione del problema consiste nel fare una scelta. Questa scelta genera porta ad uno o più sotto-problemi da risolvere.
- Per un dato problema, supporre di conoscere la scelta che porta alla soluzione ottima.
- Fatta la scelta, determinare quali sono i sotto problemi che ne derivano e caratterizzare lo spazio dei sotto problemi risultante dall'effettuare tale scelta.
- Dimostrare che le soluzioni dei sotto-problemi devono essere necessariamente soluzioni ottime. In genere si fa per assurdo.



