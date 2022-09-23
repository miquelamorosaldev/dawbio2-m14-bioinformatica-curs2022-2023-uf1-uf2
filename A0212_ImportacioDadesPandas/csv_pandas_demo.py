import numpy as np
import pandas as pd
import pathlib as Pathlib

pokemon_entries: pd.DataFrame = pd.read_csv("./A0212_ImportacioDadesPandas/pokemon.csv", sep=",")
#print(pokemon_entries)

print(pokemon_entries.dtypes)