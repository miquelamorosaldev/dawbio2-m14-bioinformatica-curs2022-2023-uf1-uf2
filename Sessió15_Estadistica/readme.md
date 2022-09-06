
# Teoria i explicació classe

- La teoria realitzada, la farem amb les instruccion al fitxer --> [Stats and theory.ipynb](stats-theory.ipynb "stats-theory")

## Installation
```sh
conda activate bio
conda list

conda install -n bio -c anaconda numpy
conda install -n bio -c anaconda scipy
conda install -n bio -c conda-forge matplotlib  # Comandos básicos de R
conda install -n bio -c anaconda pandas
conda install -n bio -c anaconda seaborn        # Equivalente a ggplot2

conda install -n bio -c anaconda statsmodels
conda install -n bio -c conda-forge pymc3

cd workspace
jupyter lab
```

## Boxplots
- https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
- https://www.phoronix.com/scan.php?page=article&item=vulkan-rt-aug21&num=4

## Python visualization
- https://realpython.com/pandas-plot-python/
- https://realpython.com/python-data-visualization-bokeh/


## Data
- https://dadescovid.cat/descarregues
- POBLACIÓ RESIDÈNCIES/GENERAL -> DIVISIÓ TERRITORIAL (AGA) -> DADES DIÀRIES


## Charset conversion:
- From Windows encoding to UTF-8:
  - iconv -f ISO-8859-1 -t UTF-8 aga_diari.csv > covid_dades.csv
