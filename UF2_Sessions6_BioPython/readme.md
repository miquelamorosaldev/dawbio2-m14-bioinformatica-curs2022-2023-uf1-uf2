# Ciències Òmniques amb BioPython (2022-01-20)

Ens vam quedar consultant la fitxa (SeqRecord) del virus Sars-Cov-2.

Aquest SeqRecord (sars-cov-2.genbank) l'hem extret de Genbank, la BBDD del NCBI.

### També ens descarreguem dades de Nucleotids del Sars-Cov-2 
BBDD del Genbank que ens permet obtenir informació d'aquestes macromolècules, com la seva seqüència.

## Codi font de la sessió

En aquesta sessió seguirem el codi i dades que ens ha facilitat el Pablo Garcia.

- intro.py
- utils.py
- intro.ipynb

Les dades són 6 fitxers, de 3 organismes amb format fasta (seqüència/es ADN) i genbank (fitxa amb seqüència/es ADN formatades i moltes altres dades)
- **example** i **orchid-list** els hem tret
- **sars-cov-2**, com ja recordareu, de l'NCBI 


## Pas 1. Adaptem la ruta on tenim els fitxers de la carpeta data.

intro.py, linia 13:

En el meu cas la ruta del meu contenidor és:

```python
from pathlib import Path
DATA_DIR = Path('/bio/2023-01-20-code/3-seqrecord/data')
```

## Comentem el codi del Chapter 3.

No confonguem la notació de la taula de traducció de Codom dels:

- Aminoàcids
Amb 
- Nucleòtids

#### Recordemos que: 3 nucleótidos = 1 aminoácido
En el código genético, **cada tres nucleótidos consecutivos actúa como un triplete que codifica un aminoácido. De este modo cada tres nucleótidos codifican para un aminoácido.** Las proteínas se componen a veces de cientos de aminoácidos. Así que el código de una proteína podría contener cientos, a veces incluso miles, de tripletes. 

Ref:
https://www.genome.gov/es/genetics-glossary/Codigo-genetico


#### Què podem fer amb Python amb seqüències ADN ? 

Recordem els selectors de llista:

Aquesta línia ens permet seleccionar els números parells, del index 0 al 5.

```python
In [1]: seq = [0,1,2,3,4,5,6,7,8]

In [2]: print(seq[0:6:2])
[0, 2, 4]
```

Tinguem en compte com funcionen els índex negatius, si posem -1 accedim a l'última posició.

```python
In [7]: print(seq[-1])
8
```

Un altre exemple, podem usar el paràmetre step (-2) per mostrar números parells des del final fins al principi.
```python
In [12]:  print(seq[-1::-2])
[8, 6, 4, 2, 0]
In [14]: print(seq[-1:2:-2])
[8, 6, 4]
```

Recordem el constructor de tuples, enumerate.

Fixem-nos què fa la linia 59.

```python
base numbers:  { list(enumerate(Seq("GATA"))) }
```
Si compilem el resultat és:

```python
base numbers:  [(0, 'G'), (1, 'A'), (2, 'T'), (3, 'A')]
```

Tenim indexada en una llista de tuples la seqüència d'ADN: id, lletraADN; que serà útil per tractar l'ORIGIN del Genbank.

### Enumerate, ens serveix per tractar cadenes d'ADN, Genbank vs Fasta

A Genbank, per facilitar lectura representa la cadena en 6 blocs de 10 lletres:
```sh
1 attaaaggtt tataccttcc caggtaacaa accaaccaac tttcgatctc ttgtagatct
61 gttctctaaa cgaactttaa aatctgtgtg gctgtcactc ggctgcatgc ttagtgcact
```

A fasta ens surt tot seguit:
```sh
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
```

### En resum, mireu bé els useful methods:

```python
    useful_methods_text = f'''
    complement():  { atg_seq.complement()         }
    concatenation: { Seq("GATA") + Seq("GATA")    }
    reverse (1):   { Seq(''.join(list(reversed("GATAGATA")))) }
    reverse (2):   { Seq("GATAGATA"[::-1])        }
    base numbers:  { list(enumerate(Seq("GATA"))) }
    slices:        { Seq("GATAGATA")[2:6]         }
    seq to str     { str(Seq("GATAGATA"))         }
    Seq objects are immutable. MutableSeq objects can mutate.
    '''
```

Multiple Strings (''') són Herdocs.

## Comentem el codi del Chapter 5.

El capítol 4 ja el vam treballar a la anterior sessió.

A partir d'aquí hi haurà uns quants imports més. Per no liarn-nos amb els imports i els submòduls, podem consultar la API de Biopython:

https://biopython.org/docs/latest/api/Bio.Seq.html

## La última part de la sessió la dediquem a trobar diversos organismes que vulguem estudiar per a la pràctica.

Idees, comparar el genoma de: 
- diverses plantes.
- estudiar els virus, i com s'infiltren a éssers vius
- diversos fongs: rovellons vs bolets verinosos vs altres plantes
- d'essers humans i altres mamífers: rates, gats, gossos.
