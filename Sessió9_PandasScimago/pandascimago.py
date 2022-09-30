import numpy as np
import pandas as pd

# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("./Sessió9_PandasScimago/scimagomedicine.csv", sep=";")
print(entries)