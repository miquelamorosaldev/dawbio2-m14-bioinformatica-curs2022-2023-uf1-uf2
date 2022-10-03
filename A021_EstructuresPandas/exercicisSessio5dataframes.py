import numpy as np
import pandas as pd
from IPython.display import display

### Exercicis.

# 1. Crea un nou dataframe similar als dels alumnes, que tingui 4 - 6 files més (10 està bé) i 1 o 2 columnes més (per exemple: gènere, població)
# 2. L'index ha de ser el nom de l'alumne. Apart de ser índex també ha de ser un camp.
# 3. Mostra la mitjana de notes de tots els alumnes.
# 4. Ordena els alumnes alfabèticament.
# 5. Mostra tota la info d'un alumne, a partir del seu nom.
# 6. Mostra les notes dels 3 alumnes que tenen una nota més alta.
# 7. Mostra els noms dels alumnes que volen fer Dual.
# 8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.

# 9 i 10.
# Espai per a que creis 2 consultes i les seves solucions, a partir de les noves consultes que has creat.



# Solució primers exercicis Dataframes

# 1 i 2. Crea un nou dataframe similar als dels alumnes, que tingui 4 - 6 files més (10 està bé)
# i 1 o 2 columnes més (per exemple: gènere, població)
# L'index ha de ser el nom de l'alumne. Apart de ser índex també ha de ser un camp.

#les notes de dawbio amb dataframe
student_list=["John","Mary","Lucy","Peter","Ann","Tom", "Oliver", "Luna", "Aria"]
grades_list = [7,9,8,4,10,6,np.nan,np.nan,np.nan] 
wants_dual_list = [False,True,False,True,True,True]
wants_dualipa_list = [True]
start_date = pd.date_range("20210101", periods=9)

genders = pd.Categorical(["Male", "Female", "Non-Binary", "Male", "Female", "I prefer not to say", "Male", "I prefer not to say", "Female"])

datos: dict[list] = {
      "grade": grades_list,
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

# Tots els càlculs.print(exercicis_frame["grade"].describe())
print("Ex3 ", exercicis_frame["grade"].mean())

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
print("7. Usant una màscara, mostra els noms dels alumnes que volen fer Dual.")
exercicis_frame7 = exercicis_frame.loc[exercicis_frame['dual'] == True]
#print(exercicis_frame7.loc['student_list'])

#     8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.
exercicis_frame8 = exercicis_frame.loc[exercicis_frame['grade'] >= 7]
print("8. Usant una màscara, mostra els alumnes que tenen una nota superior o igual a 7.")
print(exercicis_frame8)

# 9 i 10. Espai per a que creis 2 consultes i les seves solucions, a partir de les noves consultes que has creat.
# El pròxim dia veurem com tractar dataframes més grans, importats de fitxers CSV o altres formats.


# 9. Consulta tota la info dels alumnes Ann, Lucy i John.
print("9. Consulta tota la info dels alumnes Ann, Lucy i John.")
print(exercicis_frame.loc[["Ann","Lucy","John"]])

# 10. Consulta les notes de la Mary.
print(exercicis_frame.loc["Mary","grade"])

# 11. Mostra el camp index i la nota dels alumnes, ordenats alfabèticament.
print("11. Mostra el camp index i la nota dels alumnes que tenen nota.")
exercicis_frame11 = exercicis_frame.loc[exercicis_frame['grade'] > 0]
print(exercicis_frame.loc[exercicis_frame11.index,'grade'])


# Més exemples de consultes, interessants.

## Mostrar només les ciutats dels estudiants que volen dual:
        
# dual_students_df: pd.DataFrame = students_df[students_df['dual'] == True]
# dual_students_city_df: pd.DataFrame = dual_students_df.filter(items=['city'])
# print(dual_students_city_df)

# #Ejemplo ejercio 9 solo me devuelve al estudiante que su nombre
# termine en ia y tenga mas de 7
# print(df.loc[df['student_list'].str.endswith('ia') & (df['grade'] >= 7), ['student_list']])


# Ordenar per index y mostra els camps que volem en una sola línia.
print(exercicis_frame.sort_index(ascending=True).loc[:, ['grade','dual']]) 

# Ideal pera a Jupyter Notebook.
display(exercicis_frame)


## Exercice 10:
    ## Insertar dues columnes:
    ##   - Columna1: columna que mostri l'edat. La columna ha
    ##     d'aparèixer al final:
    ##   - Columna2: si han aprovat o no FOL. La columna ha
    ##     d'apareixer en segona posició després de la nota.
    ##   - Trobar els alumnes que volen fer dual i tenen suspès
    ##     FOL. 
    ##   - Mostrar només les columnes de nota i de si han aprovat FOL.

students_age: list          = [27, 21, 30, 36, 30, 39, 47, 26, 23]
fol_success:  list[bool]    = [True, True, True, True, True, True, False, False, False]

# Podem inserir automàticament 2 noves columnes sense refer el df.

exercicis_frame.insert(len(exercicis_frame.keys()), 'age', students_age)
exercicis_frame.insert(1, 'fol_succ', fol_success)
print(exercicis_frame)
dual_students_df3:          pd.DataFrame = exercicis_frame[exercicis_frame['dual'] == True]
no_fol_dual_students:       pd.DataFrame = dual_students_df3[dual_students_df3['fol_succ'] == False] 
no_fol_dual_stud_filtered:  pd.DataFrame = no_fol_dual_students.filter(items=['grade', 'fol_succ'])
print(no_fol_dual_stud_filtered)