import numpy as np 
import pandas as pd
import copy

#np --> numerical panda, es una llibreria per a realitzar càlcul numèric
#les notes de dawbio amb series
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

# EXERCICI. Transformar el Dataframe en 2.

students_grades: pd.DataFrame = copy.deepcopy(students_frame)

# Pas 1
students_grades: pd.DataFrame = copy.deepcopy(students_frame)

# Pas 2. al index li fiquem un nom
students_grades.index.name = "name"
print(students_grades)

# Pas 3.
#inplace matxaca el mateix dataFrame
#reset_index passa el index com columna
students_grades.reset_index(inplace=True)
print(students_grades)

# Pas 4.
# Borrem columna dual.
students_grades.drop(columns="dual", inplace=True)

# Podem renombrarla si volem.
students_grades.rename(columns={"name":"names"},inplace=True)
print(students_grades)

# Ara, creem la segona taula.
students_duals: pd.DataFrame = (copy.deepcopy(students_frame)
                                    .reset_index()
                                    .rename(columns={"index":"name"})
                                    .drop(columns="grade")
                                    .loc[:,["name","dual"]]
                                        )
print(students_duals)

# El merge, el pròxim dia.
