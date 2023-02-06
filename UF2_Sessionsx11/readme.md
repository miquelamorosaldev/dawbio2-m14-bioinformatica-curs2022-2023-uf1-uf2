
# Sessió 11, part 2. Biopython. Capítol 9, lectura de fitxers de l'NCBI Entrez des de la API. (2023-02-06)

Recordem els 2 principals tipus de BioPython:
* SeqRecord
* SeqIO

Gràcies a expressions regulars podem filtrar millor aquests objectes.

Recordem que els nucleòtids ens els podem baixar d'NCBI.

### API de NCBI per a llegir genbanks

No només ens podem baixar els genbank des de la web; sinó que podem baixar-nos massivament des de la API (App.Prog.Interface)

També és important tenir la API si necessitem crear una web que consulti en temps real les dades (fitxers que canvia molt sovint, per exemple, la metereologia)

Les API ens permeten, mitjançant crides HTTP; consultar i enviar dades a un servidor web.

![[API.jpg]](./API.jpg "API.jpg")

#### Els mètodes HTTP més comuns són: 

- GET (consulta)
- HEAD(consulta metadades)
- POST (enviament de dades des d'un formulari).

Des de fa 10 anys s'utilitzen cada cop més les API Restful; les que permete associar operacions CRUD a un servidor mitjançant HTTP.
* **GET** = READ
* **POST** = UPDATE
* **PUT** = CREATE
* **DELETE** = DELETE.


#### Referència:
[https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto#GET]

Tots els que no hem mencionat han caigut en desús.

<hr/>

# Biopython, capítol 9. Com llegir des de la API d'NCBI.

Seguirem el tutorial de biopython, al capítol 9:

1. [Biopython Tutorial oficial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec143 "biopython")

⚠ Avís important abans d'executar el codi ⚠
Es recomana només fer una lectura a la API de l'NCBI i baixar-nos al disc dur, en fitxers XML (o JSON si és possible) les dades que necessitem.
També, al fer cada consulta, hem d'omplir un camp amb el nostre email.

Primer exemple:

```python
from unittest import result
from Bio import Entrez
from pathlib import Path
import pprint 

# Entrez Config
# No abuseu de les peticions a NCBI.
Entrez.email = "mamoro10@xtec.cat"

handle = Entrez.einfo()
result_bytes:   bytes   = handle.read()
# Cal decodificar a text utf-8 perquè ncbi guarda 
# les dades del fitxer en format binari (per protecció) 
result_str:     str     = result_bytes.decode('utf-8')
## Ja tenim guardat el fitxer.
Path('result.xml').write_text(result_str)
handle.close()

# Ja podem llegir el fitxer.
with open('result.xml','rb') as xml_file:
    record = Entrez.read(xml_file) # Handle punter a un fitxe
#Realitza el close, automaticament

# Ja podem consultar les dades des del disc.
print(type(record)) #Similar a dict
print(record)
```

## Les instruccions que veurem seran:

**EInfo** Les instruccions que hem fet avui.

- [Prova 1 einfo IPYNB](./entrez1.ipynb "entrez1.ipynb")

**ESearch** és un mètode tipus (GET)
   
**EPost** és un mètode tipus (POST)
   
**EFetch** recull les dades

</hr>
</hr>
