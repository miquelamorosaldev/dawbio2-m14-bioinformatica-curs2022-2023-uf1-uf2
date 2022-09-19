import numpy as np
import pandas as pd

# Test dataframes
# Com en el cas de les series,.
dict_animals = {'num_legs': [2, 4, 0, 8], 'num_wings': [2, 0, 0, 0]}
name_animals = ['falcon', 'dog', 'snail', 'spider']
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
datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
print(students_frame)

# Càlculs estadístics.
print(students_frame.describe())

# Us convido a que editeu els 2 Dataframes anteriors.
