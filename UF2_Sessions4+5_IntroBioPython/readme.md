# Ciències Òmniques amb BioPython.

Omicas , es un sufix grec que significa molts, en aquest cas moltes opcions per treballar sobre les lleis de la genètica.


### Recordem el DOGMA CENTRAL DE LA BIOLOGIA MOLECULAR.

La transcripció es ADN(**ATCG**) que dona pas a les cadenes ARN(**UTCG**) (doble sentit), més la traducció que és la creació de proteïnes a partir de les cadenes d'ARN.

![[Dogma]](dogma.png "Dogma")

<hr/>

## BioPython, aplicat la bioinformàtica.

La llibreria que utilitzarem es la [biopython](https://biopython.org/ "biopython"). Podem partir de la seva documentació que esta plantejada com un [Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html "Tutorial")


### El fitxer que integra totes les proves que hem fet és biopython-v1.ipynb

 -->[./biopython-v1.ipynb](biopython-v1.ipynb "biopython-v1.ipynb")

S'utilizen dos tipus de fitxers

	1.- *BioPython.*
		- .fasta
		- .gb (gen bank)
	
	2.- *Busqueda de secuencias.* Expressiones regulares (Regexp)

	3.- *Alineamiento de secuencias.* 3 algoritmos principales

		- **Lineal**

		- **Global**

		- ** [BLAST](https://es.wikipedia.org/wiki/BLAST "BLAST") ** utilitza una matriu de substitució d'aminoàcids o nucleòtids per qualificar els seus alineaments. Aquesta matriu conté la puntuació (també anomenada score) que se li dóna en alinear un nucleòtid o un aminoàcid X de la seqüència A amb un altre aminoàcid I de la seqüència B.


### Fitxers fasta

- Conté una(*archivo fasta*) o més(*archivo multifasta*) seqüències.

- Escritas como secuencias de ADN
  
| bases nitrogenades  |  Combinacions de totes  |
| ------------  | ------------ |
|  A T C G      |  N· K · I |


### Extreurem fitxers FASTA de la web [NCBI](https://www.ncbi.nlm.nih.gov/ "NCBI"). National Center for Biotechnology Information.

Totes les bases de dades del NCBI, de les quals la que ara ens interessa més és la [Genbank](https://www.ncbi.nlm.nih.gov/genbank/), estan disponibles en línia de manera gratuïta, i són accessibles usant el cercador [Entrez](https://www.ncbi.nlm.nih.gov/search/).

Buscar al cercador de nucleòtids, la paraula COVID, per exemple

- **ORF** Open Reading Frame. ORFx , el numero x indica per quina base, tinc que començar per llegir una seqüència.

Cadena (Orf1)**G**(Orf2)**A**(Orf3)**TAGATA**

Per cada seqüència, hi ha dos coses:
1. Un comentari/descripció que comença per > i es una sola linea
2. La seqüència de bases dividides per línies de ...[70] caràcters pot variar.

Si es un fitxer MULTI-FASTA, és separa seqüència amb seqüència amb una linea de capçalera ( > ), 


#### Proves amb Mòdul Biopython 

 -->[./biopython-v1.ipynb](biopython-v1.ipynb "biopython-v1.ipynb")

 Tindrem que recordar la nomenclatura de -->[./biopython-v1.ipynb](https://iupac.org/ "biopython-v1.ipynb")

 Per alguns dels exercicis, tindrem que tenir present la **traducció** [aminoacids_table](https://upload.wikimedia.org/wikipedia/commons/7/70/Aminoacids_table.svg"biopython.ipynb")

 Treballarem també amb el GENBANK de coronavirus.

# FI SESSIÓ 4, DIA 12/01/2023

<hr/>
<hr/>
<hr/>


 ### Fitxer GENBANK del coronaviurs

 Explicació de la fitxa general del fitxer de coronavirus, extret de ... [ncbi coronavirus](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512 "ncbi coronavirus")

 ![[severeacute]](severeacute.png "severeacute")
 
 **Locus** identificació

 · **29903** posició de la seqüencia en la que acaba la seqüència.
 · **DBLINK** projecte d'on ha sortit aquesta seqüència.
 · **ORGANISM** Diferents classificacions del coronavirus.
 · **Reference Authors** tots els que l'han seqüenciat
 · **Title** Títol del article on han publicat.
 · **JOURNAL** Mitjà on ho han publicat 
 · **PUBMED** link del article (si el volem llegir podem intentar buscar a SCI HUB)
 · **REFERENCE** de otras personas que han estat treballant sobre el tema.
 · **FEATURES** les diferents anotacions que tenen el fitxer.
  ![[anotacions]](anotacions.png "anotacions")
 · **ORIGIN** On comença la seqüencia

El fitxer // es el final d'un fitxer genbank

#### Aclaracions de la part de Features concret

 *5'UTR           1..265* no ho ha codificat
 *gene*                   
 *CDS*            Cadena codificant
 */translation*    Cadena proteïna