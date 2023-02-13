# Sessió 12. Biopython. Capítol 9, lectura de fitxers de l'NCBI Entrez des de la API i alineament de seqüències (2023-02-10)

## Els codis que vam seguir ahir:

[Entrez Intro PY](./5-entrez/1-intro/entrez.py)

### Resum funcions:

**EInfo (9.2 EInfo + writing to disk)** Mètode tipus GET. Conté informació d'ORGANISMES =ORGN

- [Prova 1 einfo IPYNB](./entrez1.ipynb "entrez1.ipynb")

**ESearch (9.3 ESearch)** és un mètode tipus (GET)

Entrez retorna XML.

Amb la funció read d'Entrez es parseja l'XML i retorna un diccionari {}.

Aquest conté llista d'Accession Numbers (idList) en comptes de retornar les cadenes dirèctament.

### 9.4 EPost and 9.6 EFetch

**EPost** és un mètode tipus (POST)

Ens permet pujar a l'NCBI la nstta idList (Accession Numbers)

Es important que la llista sigui de menys de 200 id; per no estressar serveis NCBI.

Ens retorna un Id de Sessió.


**EFetch** recull les dades usant l' idSessió.

Baixar els fitxers fasta demanats anteriorment a l'EPost.


## Els codis que seguirem avui:

[Entrez Functions folder](./5-entrez/2-functions/)

Tenim diversos exemples de:

- EInfo
- ESearch
- EFetch
  
A l'EFetch hi ha uns fitxers d'Utils que llegeixen directament els fitxers del disc.

L'utils de l'Efetch 3 és el més complet i interessant per a fer pràctiques. 
Per exemple; només fa la petició a NCBI si no existeix el fitxer XML al disc.

## I per a què ens serveix ?

La genòmica ha pogut aplicar-se gràcies al projecte del Gènoma Humà (2001), als repositoris accessibles 
mundialment com l'NCBI i les dades obertes de llocs com la WHO i a les tècniques d'**alineament de seqüències.**

A biologia s'han vist els alineaments per parelles de seq. = **PAIRWISE**

Exemple seqA.   GAT
Exemple seqB.   GATA

Normalment la longitud és diferent (habitual) i necessitem algoritmes avançats.
Si fos igual seria més fàcil (comparem lletra a lletra).

* Global Alignement
  * Va bé per a cadenes de longitud similar (no igual).
* Local Alignement
  * S'usa molt quan només disposem un tros petit de seqüència,
  * com ho pot fer la policía científica.

Com traiem l'score (la puntuació) de la diferència de les 2 seqüència.

## Com més baix sigui l'score més semblants seran.

També podem fer alineament de moltes parelles de seqüències (clustal):

Exemple seqA.   GAT
Exemple seqB.   GATA
Exemple seqC.   ATGC

Un cop tenim aquesta taula podem crear arbres filogenètics per a comparar espècies.
És una pena que no hem arribat a temps per abordar la creació d'aquests arbres.

## Alineament de proteïnes.

Sempre que poguem, fem alineació de proteïnes. 
Perquè tenen més lletres, i llavors les diferències són molt més marcades.

Matriu BLOSUM62.

![[Blosum62-dayhoff-ordering.svg]](./Blosum62-dayhoff-ordering.svg)

Sempre usar aquesta matriu per a l'alineament de proteines.

## Alineament d'ADN.

Tenim una matriu d'scores de les 4 lletres.

![[dna_align_mat.jpg]](./dna_align_mat.jpg)

## Pendent:

Provar el codi pairwise.py i aprendre més sobre l'alineament de seqüències.

<hr/>