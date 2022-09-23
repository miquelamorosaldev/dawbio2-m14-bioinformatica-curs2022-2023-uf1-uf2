import numpy as np
import pandas as pd

# Test dataframes
# Com en el cas de les series,.
dict_animals = {'num_legs': [2, 4, 0, 8, 6], 'num_wings': [2, 0, 0, 0, 4], 'can_fly': [True, False, False, False, True]}
name_animals = ['falcon', 'dog', 'snail', 'spider', 'butterfly']
df_animals = pd.DataFrame(data=dict_animals, index=name_animals)
print(df_animals)

#date_range = pd.date_range("20130101", periods=6)
dates = pd.date_range("20220101", periods=40, freq='M')
print(dates)

days = pd.date_range("20130101", periods=6, freq='D')
df_days = pd.DataFrame(np.random.randn(6, 4), index=days, columns=list("ABCD"))
print(df_days)

print(df_days.dtypes)

# rows x cols
print(df_days.shape)

# Statistics from each column
print(df_days.describe())


#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]

# Fusionem les 2 llistes en un dataframe per a que entrin com a valors del dataframe.
datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
print(students_frame)

# Càlculs estadístics.
print("Shape = ",students_frame.shape)

print(students_frame.describe())

#Ordenació per valors axis=0 columnes 
students_grade_sorted = students_frame.sort_values(by=['grade'], 
                                                   axis=0, 
                                                   ascending=False)
print(students_grade_sorted)


#Afegir files al Pandas, tenint en compte l'index.
students_frame.loc["Ann"]=[10,True]
print(students_frame)
print(students_frame.dtypes)
# row_student = {"index": "Ann", "grade": 10, "dual": True}
# students_frame.append(row_student, ignore_index=False)
