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

