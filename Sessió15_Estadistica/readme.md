
# Teoria i explicació classe

- La teoria realitzada, la farem amb les instruccion al fitxer --> [Stats and theory.ipynb](stats-theory.ipynb "stats-theory")

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


## Charset conversion:
- From Windows encoding to UTF-8:
  - iconv -f ISO-8859-1 -t UTF-8 aga_diari.csv > covid_dades.csv
