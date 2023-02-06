# Sessió 11 - Biopython (2022-02-06)

El repte que vam proposar a la sessió anterior és aconseguir com llegir un fitxer multifasta 
mitjançant Pyhton i regexps.

## Solució parseig multifasta Python.
 
[questions.py](./questions.py)

### Fitxers de prova

[regex-1.fasta](./regex-1.fasta)
[regex-2.fasta](./regex-2.fasta)

### Provem expressió a regex101

La estratègia que segueix el codi és:

1. Separar el fitxer multifasta en blocs amb cada una de les cadenes fasta; mètode **split_multi_fasta**

La expressió que ens permet seleccionar cada un dels blocs fasta del fitxer multifasta és aquesta:

```python
>[^>]{0,}
```

"Primer caràcter >, els següents poden ser qualsevol menys >; anem llegint infinitament fins a trobar un altre >"


2. Ara, apliquem la expressió regular per a filtrar el tros de cadena dins de cada un dels fasta. **parse_fasta**

```python
>[^\n]{1,})(.{0,})
```

"Primer caràcter >, els següents poden ser qualsevol menys >; anem llegint infinitament fins a trobar un altre >"

3. Apart d'això, hem de tenir en compte que moltes vegades els fasta tenen la cadena separada per espais. 
Els hem d'eliminar amb compte; amb la funció **remove_whitespaces**

I la expressió:
```python
\s
```

</hr>
</hr>


## Biopython. Alineament seqüències.

Recordem els 2 principals tipus de BioPython:
* SeqRecord
* SeqIO

Gràcies a expressions regulars podem filtrar millor aquests objectes.

Recordem que els nucleòtids ens els podem baixar d'NCBI.

### API de NCBI per a llegir genbanks

No només ens podem baixar els genbank des de la web; sinó que podem baixar-nos massivament des de la API (App.Prog.Interface)

També és important tenir la API si necessitem crear una web que consulti en temps real les dades (fitxers que canvia molt sovint, per exemple, la metereologia)

Les API ens permeten, mitjançant crides HTTP; consultar i enviar dades a un servidor web.

#### Els mètodes HTTP més comuns són: 

- GET (consulta)
- HEAD(consulta metadades)
- POST (enviament de dades des d'un formulari).

Des de fa 10 anys s'utilitzen cada cop més les API Restful; les que permete associar operacions CRUD a un servidor mitjançant HTTP.
* GET = READ
* POST = UPDATE
* PUT = CREATE
* DELETE = DELETE.

#### Referència:
[https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto#GET]

Tots els que no hem mencionat han caigut en desús.

Llibreria python request.


## Biopython, capítol 9. Com llegir des de la API d'NCBI.

Seguirem el tutorial de biopython, al capítol 9:

1. [Biopython Tutorial oficial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec143 "biopython")

Les instruccions que veurem seran

**EInfo** Les instruccions 
      
- [Prova 1 einfo](./3-apis/2-entrez/1-einfo/einfo-e1/einfo.py "einfo-e1")

- [Prova 2 einfo](./3-apis/2-entrez/1-einfo/einfo-e2/einfo.py "einfo-e1")
    
**ESearch** és un mètode tipus (GET)
   
- [Prova 1 esearch](./3-apis/2-entrez/2-esearch/esearch-e1/esearch.py "esearch-e1")
   
- [Prova 2 esearch](./3-apis/2-entrez/2-esearch/esearch-e2/esearch.py "esearch-e2")
   
**EPost** és un mètode tipus (POST)
   
**EFetch** recull les dades

- [Prova 1 efetch](./3-apis/2-entrez/3-efetch/efetch-e1/efetch.py "efetch-e1")

- [Prova 2 efetch](./3-apis/2-entrez/3-efetch/efetch-e2/efetch.py "efetch-e2")

- [Prova 3 efetch](./3-apis/2-entrez/3-efetch/efetch-e3/efetch.py "efetch-e3")


</hr>
</hr>

## Link següent sessió

[Sessió 12 - Regexp](./UF2_Sessionsx12/readme.md)