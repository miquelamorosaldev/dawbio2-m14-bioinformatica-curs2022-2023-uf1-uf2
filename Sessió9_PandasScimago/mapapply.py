import numpy as np
import pandas as pd
import copy

#1 Map: Numbers and Strings.
# https://www.w3resource.com/pandas/series/series-map.php

def mult5(num: int)-> int:
    return num * 5

def helloName(name: str)-> str:
    return "Hello " + name

ser3: pd.Series = pd.Series([2,4,6,8,10,12])
ser3 = ser3.map(mult5)
print(ser3)

ser4: pd.Series = pd.Series(["John","Lucy","Mary","Peter"])
ser4 = ser4.map(helloName)
print(ser4)

# DataFrame.mapaply(). Works elements wise for rows
data = {"A": [1,2,3,9,6],
       "B": [3,4,8,6,9]}
df3 = pd.DataFrame(data)

dfcopy = copy.deepcopy(df3)

df3 = df3.applymap(mult5)
#print(df3)

# Si només volem aplicar a una columna la funció.
dfcolA = dfcopy["B"].map(mult5)
print(dfcolA)


## Exemple funció Apply -> Suma columnes

print(dfcopy)
df4 = copy.deepcopy(dfcopy)
dfcopy = dfcopy.apply(lambda column:column.sum())
print(dfcopy)

# Crear columna C -> Mult B * 5 
df4.loc[:,"C"] = df3["B"].map(mult5)
print(df4)

# Canviar ordre aparició columnes
df5 = df4.loc[:,["C","A","B"]]
print(df5)