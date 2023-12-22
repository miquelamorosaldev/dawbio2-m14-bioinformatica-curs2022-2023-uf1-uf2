# Ciències Òmniques amb BioPython. Sessions 4 i 5.

Omicas , es un sufix grec que significa molts, en aquest cas moltes opcions per treballar sobre les lleis de la genètica.


### Recordem el DOGMA CENTRAL DE LA BIOLOGIA MOLECULAR.

La transcripció es ADN(**ATCG**) que dona pas a les cadenes ARN(**UTCG**) (doble sentit), més la traducció que és la creació de proteïnes a partir de les cadenes d'ARN.

![[Dogma]](dogma.png "Dogma")

<hr/>

# BioPython, aplicat la bioinformàtica.

La llibreria que utilitzarem es la [biopython](https://biopython.org/ "biopython"). Podem partir de la seva documentació que esta plantejada com un [Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html "Tutorial")


## Proves amb Mòdul Biopython.

En aquesta sessió usarem el:

 -->[./biopython-v1.ipynb](biopython-v1.ipynb "biopython-v1.ipynb")

 Haurem de recordar la nomenclatura de -->[./biopython-v1.ipynb](https://iupac.org/ "biopython-v1.ipynb")

 Per alguns dels exercicis, hem de tenir present la **traducció** [aminoacids_table](https://upload.wikimedia.org/wikipedia/commons/7/70/Aminoacids_table.svg"biopython.ipynb")

 Treballarem també amb el GENBANK de coronavirus.



### Dins d'aquest projecte s'utilizen dos tipus de fitxers

1.-*BioPython.*
		- .fasta
		- .gb (gen bank)
	
2.- *Busqueda de secuencias.* Expressiones regulares (Regexp)

3.- *Alineamiento de secuencias.* 3 algoritmos principales

		- **Lineal**

		- **Global**

		- ** [BLAST](https://es.wikipedia.org/wiki/BLAST "BLAST") 
- <em>Utilitza una matriu de substitució d'aminoàcids o nucleòtids per qualificar els seus alineaments. Aquesta matriu conté la puntuació (també anomenada score) que se li dóna en alinear un nucleòtid o un aminoàcid X de la seqüència A amb un altre aminoàcid I de la seqüència B.</em>


### Fitxers fasta

- Conté una(*archivo fasta*) o més(*archivo multifasta*) seqüències.

- Escritas como secuencias de ADN
  
| bases nitrogenades  |  Combinacions de totes  |
| ------------  | ------------ |
|  A T C G      |  N· K · I |

### Extreurem fitxers FASTA de la web [NCBI](https://www.ncbi.nlm.nih.gov/ "NCBI"). National Center for Biotechnology Information.

Totes les bases de dades del NCBI, de les quals la que ara ens interessa més és la [Genbank](https://www.ncbi.nlm.nih.gov/genbank/), estan disponibles en línia de manera gratuïta, i són accessibles usant el cercador [Entrez](https://www.ncbi.nlm.nih.gov/search/).


## FI SESSIÓ 4, DIA 12/01/2023. INICI SESSIÓ 5.

<hr/>
<hr/>
<hr/>

<a name="s5-genbank"></a>

### Estructura bàsica de Biopython

Quan fem 
```python
from Bio.Seq import Seq
```

És estrany perquè:
Bio = Mòdul
1r Seq = Submòdul
2n Seq = Classe

L'habitual és que el nom de la classe i el nom del submòdul siguin diferents.

També hi ha classes que no estan dins de cap submòdul:

```python
from Bio import SeqIO
```

## Com funcionen les capçaleres dels fasta ?

SeqRecord és una fitxa de la seqüència.
- sequence
- id
- name
- description

Estan trets del Genbank.

### Trobar FASTA de Genbank des del buscador 

Buscar al cercador de nucleòtids, la paraula COVID, per exemple:

- **ORF** Open Reading Frame. ORFx , el numero x indica per quina base, tinc que començar per llegir una seqüència.

Cadena (Orf1)**G**(Orf2)**A**(Orf3)**TAGATA**

Per cada seqüència, hi ha dos coses:
1. Un comentari/descripció que comença per > i es una sola linea
2. La seqüència de bases dividides per línies de ...[70] caràcters pot variar.

Si es un fitxer MULTI-FASTA, és separa seqüència amb seqüència amb una linea de capçalera ( > ), 

### Trobar FASTA de Genbank des de la pàgina principal.

Ens baixem un fitxer del Genbank, de la web d'NCBI.

Estem a gener del 2023 i encara hi ha un accés directe a tots els recursos del Sars-Cov-2:

https://www.ncbi.nlm.nih.gov/sars-cov-2/

Coses interessants:
PMC -> Papers lliures. 
PubMed -> Papers de pagament.
 
Anem baixant i ara trobem el més important:

SARS-CoV-2 Sequence Resources.

Cliquem el botó de la segona fila:

NCBI RefSeq SARS-CoV-2 genome sequence record 

I quan ![[Dogma]](dogma.png "Dogma")ens trobem a la següent pàgina podem descarregar el fitxer.

![[sars-cov-2-genbank]](sars-cov-2-genbank.png "sars-cov-2-genbank")

 ## Estructura del fitxer GENBANK del coronavirus.

 Explicació de la fitxa general del fitxer de coronavirus, extreta de ... 
 [ncbi coronavirus, NC_045512](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512 "ncbi coronavirus")


Observació: S'utilitzen fitxers Genbank per retrocompatibilitat, ja que quan es va inventar, a inicis dels 80; no existia ni el JSON ni l'XML.

 
### CAPÇALERA DEL GENBANK

 Els genbank sempre comencen per la paraula LOCUS i haurien de tenir informats tots els camps.

 . **Locus** identificació del lloc. 

 . **Definition** Descripció textual

 . **Accession** És l'ID de la fitxa.

 . **Version** Notació general: ID + NumVersion

 · **DBLINK** projecte d'on ha sortit aquesta seqüència.

 · **KEYWORDS** paraules claus al buscador.

 · **SOURCE** Descripció més científica, amb taxonomies.

 · **REFERENCE** de otras personas (i les seves publicacions) que han estat treballant sobre el tema.

 · **COMMENTS** Calaix desastre, qualsevol text.


### SEGONA PART DEL GENBANK

 · **FEATURES** les diferents anotacions que tenen el fitxer. Per exemple: des de la base 7 a la 20 d'un ADN té una anotació especial.

#### Aclaracions de la part de Features concreta

 *5'UTR           1..265* no ho ha codificat
 *gene*                   
 *CDS*            Cadena codificant
 */translation*    Cadena proteïna

   ![[anotacions]](anotacions.png "anotacions")

 · **ORIGIN** On comença la seqüencia, la conté tota.

 · **ORGANISM** Diferents classificacions del coronavirus.

 · **Reference Authors** tots els que l'han seqüenciat

 · **Title** Títol del article on han publicat.

 · **JOURNAL** Mitjà on ho han publicat 

 · **PUBMED** link del article (si el volem llegir podem intentar buscar a SCI HUB)

El fitxer // es el final d'un fitxer genbank

## Link següent sessió

[Sessió 6 - Biopython. Tractament del fitxer Genbank del Sars-Cov-2](./UF2_Sessions6_BioPython/readme.md)
