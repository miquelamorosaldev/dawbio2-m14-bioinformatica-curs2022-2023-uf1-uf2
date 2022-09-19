import numpy as np
import pandas as pd

# Demo series.
# np.nan es equivalente a not avaliable, más eficiente.
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Serie amb index predeterminat (0,1,2,...)
list_temp = [12.5,17.3,20.5,np.nan]
serie_temp = pd.Series(data=list_temp, dtype=float )
print(serie_temp)

# Serie amb index personalitzat.
index_temp = ['jan','feb','mar','apr']
serie_temp_mensuals = pd.Series(data=list_temp, dtype=float, index=index_temp)
print(serie_temp_mensuals)

# Serie, valors String
#index_series = ['jan','feb','mar','apr']
list_bestseries = ['Casa Papel', 'Casa Dragon', 'Merli', 'Plats Bruts']
serie_bestseries = pd.Series(data=list_bestseries, dtype="string")
print(serie_bestseries)

student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
grades_serie = pd.Series(data=grades_list, index = student_list, dtype=int, name="student_grades")
print(grades_serie)

# Consultem dtypes
print(grades_serie.dtypes)

# Serie autogenerada.
list_numbers = range(1,11)
serie_numbers = pd.Series(data=list_numbers, index =list_numbers, dtype=int)

# Serie dates
list_numbers = range(1,11)
serie_numbers = pd.Series(data=list_numbers, index =list_numbers, dtype=int)
print(serie_numbers)

#or21 .. o28 
# id_classrooms = list(range(21,29))
# list_classrooms = ['or'+str(room) for room in id_classrooms]
# serie_classrooms = pd.Series(data=list_classrooms, index=id_classrooms, dtype="string")

# Solució Dani, més eficient
id_classrooms = list(range(21,31))
list_classrooms = [f'or{room}' for room in id_classrooms]
serie_classrooms = pd.Series(data=list_classrooms, index=id_classrooms, dtype="string")
print(serie_classrooms)

# Print dtypes
print(serie_numbers.dtypes)