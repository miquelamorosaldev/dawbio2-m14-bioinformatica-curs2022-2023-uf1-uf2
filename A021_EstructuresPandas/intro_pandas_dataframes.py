#Codi de prova fet durant la sessió del 18/09/2022, introducció als dataframes.
import numpy as np
import pandas as pd

dict_animals = {'num_legs': [2, 4, 0, 8, 6, 2], 'num_wings': [2, 0, 0, 0, 4, 2], 'can_fly': [True, False, False, False, True, True]}
name_animals = ['falcon', 'dog', 'snail', 'spider', 'butterfly', 'duck']
df_animals = pd.DataFrame(data=dict_animals, index=name_animals)
print(df_animals)


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)


animals_df = pd.Series(data=['falcon', 'dog', 'snail', 'spider'], dtype="string")

df3 = pd.DataFrame(
    {
        "A": [1.0] + [np.nan] * 2 + [3.0],
        "B": pd.date_range("20220101", periods=4, freq='D'),
        "C": animals_df,
        "D": pd.Categorical(["Male", "Female", "NS/NC", "Female"]),
        "E": "foo",
    }
)
print(df3)

#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter","Ann","Tom"]
grades_list = [7,9,8,4,10,6]
wants_dual_list = [False,True,False,True,True,True]
wants_dualipa_list = [True]
start_date = pd.date_range("20210101", periods=6)

datos: dict[list] = {"grade": grades_list,
      "dual": wants_dual_list, "student_list" : student_list}

students_frame = pd.DataFrame(
    index=student_list,
    data=datos
)
#print(students_frame)

# Ordenar numèric
students_frame_sorted = students_frame.sort_values(by=["grade"],axis=0,ascending=False)
print(students_frame_sorted)

# Ordenar alfabètic.
students_frame_sorted = students_frame.sort_values(by=["student_list"],ascending=True)
print(students_frame_sorted)

# Les 2 consultes retornen el mateix resultat.
# at = loc opt.
print(students_frame.at["Lucy","grade"])
# iat = loc opt.
print(students_frame.iat[2,0])


#Podemos devolver una lista de varias filas, devuelve una lista
students_frame.loc[["Mary","Lucy"],"grade"]
print(students_frame)

#Podem retornar una llista de varies files, i retorna una llista
students_frame2 = students_frame.loc[["Mary","Lucy"],
                   ["grade","dual"]]
print("llista varies files")

print(students_frame)

# https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
print("students_pass")
students_pass1 = students_frame.loc[students_frame['grade'] > 6]
print(students_pass1)

print("students_pass")
students_pass2 = students_frame.loc[students_frame['dual'] == True]
print(students_pass2)

# EXERCICIS

# 1 i 2. Crea un nou dataframe similar als dels alumnes, que tingui 4 - 6 files més (10 està bé)
# i 1 o 2 columnes més (per exemple: gènere, població)
# L'index ha de ser el nom de l'alumne. Apart de ser índex també ha de ser un camp.

#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter","Ann","Tom", "Pablo", "Miquel", "Roser"]
grades_list = [7,9,8,4,10,6] 
wants_dual_list = [False,True,False,True,True,True]
wants_dualipa_list = [True]
start_date = pd.date_range("20210101", periods=9)

genders = pd.Categorical(["Male", "Female", "Non-Binary", "Male", "Female", "I prefer not to say", "Male", "I prefer not to say", "Female"])

datos: dict[list] = {
      "grade": grades_list + 3 * [0],
      "dual": wants_dual_list + 3 * [True], 
      "student_list" : student_list,
      "start_date" : start_date,
      "gender" : genders}

exercicis_frame = pd.DataFrame(
    index=student_list,
    data=datos
)
print(exercicis_frame)

#     3. Mostra la mitjana de notes de tots els alumnes.
print(exercicis_frame["grade"].describe())

#     4. Ordena els alumnes alfabèticament.
exercicis_frame4 = exercicis_frame.sort_values(by=["student_list"],ascending=True)
print(exercicis_frame4)

#     5. Mostra tota la info d'un alumne, a partir del seu nom.
print("EX5 - Info d'una alumne")
print(exercicis_frame.loc["Mary"])

# Si volguessim info sobre només un atribut d'un alumne.
# students_frame.loc[["Mary"],"grade"]

#     6. Mostra les notes dels 3 alumnes que tenen una nota més alta.
#Possible solució - ordenar els alumnes per nota i mostrar els 3 primers.
exercicis_frame6 = exercicis_frame.sort_values(by=["grade"],axis=0,ascending=False)
print(exercicis_frame6[0:3])

#     7. Usant una màscara, mostra els noms dels alumnes que volen fer Dual.
exercicis_frame7 = exercicis_frame.loc[exercicis_frame['dual'] == True]
print(exercicis_frame7)

#     8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.
exercicis_frame8 = exercicis_frame.loc[exercicis_frame['grade'] >= 7]
print("8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.")
print(exercicis_frame8)

# 9 i 10. Espai per a que creis 2 consultes i les seves solucions, a partir de les noves consultes que has creat.
# El pròxim dia veurem com tractar dataframes més grans, importats de fitxers CSV o altres formats.


# 9. Consulta tota la info dels alumnes Ann, Lucy i John.

# 10. 
