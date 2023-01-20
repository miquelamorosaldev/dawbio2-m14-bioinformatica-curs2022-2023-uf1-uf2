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
DATA_DIR = Path('/bio/2023-01-20-code/3-seqrecord/data')
```
