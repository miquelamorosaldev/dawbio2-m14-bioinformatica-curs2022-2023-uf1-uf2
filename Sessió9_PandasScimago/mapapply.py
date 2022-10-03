import numpy as np
import pandas as pd
import copy

#1 Map
def mult5(num: int)-> int:
    return num * 5

ser3: pd.Series = pd.Series([2,4,6,8,10,12])
ser3.map(mult5)

print(ser3)