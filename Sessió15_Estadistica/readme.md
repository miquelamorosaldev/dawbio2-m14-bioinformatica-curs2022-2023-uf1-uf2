
# Teoria i explicació classe

- La teoria realitzada, la farem amb les instruccion al fitxer --> [Stats and theory.ipynb](stats-theory.ipynb "stats-theory")
- La pràctica la realitzarem amb:
* [Funcions agrupació, estadística i gràfiques.](https://github.com/miquelamorosaldev/dawbio2-m14-bioinformatica-uf1-uf2/blob/main/Sessi%C3%B315_Estadistica/pd_grups_pacients_random.ipynb)
* [Sessió 16 - estadística dades Covid19](https://github.com/miquelamorosaldev/dawbio2-m14-bioinformatica-uf1-uf2/tree/main/Sessi%C3%B316_EstadisticaDadesCovid)

## Installation Packages.
```sh
conda activate bio
conda list

conda install -n bio -c anaconda numpy
conda install -n bio -c anaconda scipy
conda install -n bio -c anaconda matplotlib  # Comandos básicos de R
conda install -n bio -c anaconda pandas
conda install -n bio -c anaconda seaborn        # Equivalente a ggplot2

## Installation Optional Packages.

conda install -n bio -c anaconda statsmodels
conda install -n bio -c conda-forge pymc3

cd workspace
jupyter lab
```

## Boxplots
- https://www.youtube.com/watch?v=09Cx7xuIXig
- https://www.phoronix.com/scan.php?page=article&item=vulkan-rt-aug21&num=4

## Python visualization
- https://realpython.com/pandas-plot-python/
- https://realpython.com/python-data-visualization-bokeh/


## Dades.

### Fins el juliol del 2022:
- https://dadescovid.cat/descarregues
- POBLACIÓ RESIDÈNCIES/GENERAL -> DIVISIÓ TERRITORIAL (AGA) -> DADES DIÀRIES

### A partir d'agost del 2022:

Les dades les publiquen al portal Sivic a partir d'aquesta dada, juntament amb les de la grip.

- https://sivic.salut.gencat.cat/covid

<em>Nota: Encara que des del juliol del 2022 no s'actualitza dadescovid.cat, l'estudi fet segueix sent vàlid i útil.</em>

Exercicis interessants:

- <a href="Sessió15_Estadistica/Estadistica_Rectes_Regressió/exercici-tempbcn.ipynb">Possible Solució. Gràfic Scatter Plot del Co·lapse Climàtic a Barcelona</a>


## Charset conversion:
- From Windows encoding to UTF-8:
  - iconv -f ISO-8859-1 -t UTF-8 aga_diari.csv > covid_dades.csv
