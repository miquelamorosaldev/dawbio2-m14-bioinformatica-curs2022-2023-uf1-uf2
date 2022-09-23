import numpy as np
import pandas as pd

# Read pokemons ranking
pokemon_entries: pd.DataFrame = pd.read_csv("pokemon.csv", sep=";")
print(pokemon_entries)