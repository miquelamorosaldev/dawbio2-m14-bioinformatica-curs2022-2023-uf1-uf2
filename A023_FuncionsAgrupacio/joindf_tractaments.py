import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import copy

# Exercici per repassar el Join i altres comandes.

# Estudi d'un nou tractament per a pacients de Covid persitent.

# covidper_evolucio.csv conté la evolució del tractament.
# covidper_tractaments.csv té la dosi del medicament que s'aplica a cada pacient.

# Aquests 2 fitxers tenen un camp comú, l'id del pacient (1a fila)

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Exercici 0. 
    csv_file_path1 = "./A023_FuncionsAgrupacio/covidper_evolucio.csv"
    # Read Evolution File.
    df_evolucio: pd.DataFrame = pd.read_csv(csv_file_path1, sep=";")
    print(df_evolucio)

    csv_file_path2 = "./A023_FuncionsAgrupacio/covidper_tractaments.csv"
    # Read Evolution File.
    df_tractament: pd.DataFrame = pd.read_csv(csv_file_path2, sep=",")
    print(df_tractament)

    # Exercici 1. Fer una outer join dels 2 dataframes.
    joinDfs: pd.DataFrame = pd.merge(df_evolucio,df_tractament, how="outer", on="id")
    print(joinDfs)

    joinDfsCopy = copy.deepcopy(joinDfs)

    # Exercici 2. Substituïr els valors ?? de la columna evolució pel valor desconeguda.
    # https://kanoki.org/2019/07/17/pandas-how-to-replace-values-based-on-conditions/
    joinDfs['evolució'].mask(joinDfs['evolució'] 
        == '???', 'desconeguda', inplace=True)
    print(joinDfs)

    # Exercici 3. Substituïr els valors NaN de la columna 
    # dosis per placebo.
    joinDfs['dosis'] = joinDfs['dosis'].fillna("placebo")
    print(joinDfs)

    # Exercici 4. Compta quants pacients s'han aplicat cada dosi
    # (columna 'dosis').
    grouped_df = joinDfs.groupby('dosis')['id'].count()
    print(grouped_df)

    # Exercici 5. En català, es diu dosi, no dosis. Canvia el nom de la columna.
    joinDfs.rename({'dosis': 'dosi'}, axis=1, inplace=True)
    #print(joinDfs)

    # Exercici 6. Fes una còpia de seguretat del dataframe en un fitxer anomenat
    # covidper_fusio.csv
    joinDfs.to_csv("./A023_FuncionsAgrupacio/covidper_fusio.csv")

    # Exercici 7. A partir de l'agrupació de l'exercici 4, 
    # fes un gràfic de barres de les dosis aplicades de cada tractament.
    # https://www.statology.org/pandas-groupby-plot/

    joinDfs.groupby('dosi')['id'].count().plot(kind="bar", bottom=0.155, title="Dosis aplicades de cada tractament.", legend= True)
    plt.show()
    # Reset previous plot
    plt.clf()

    #print(joinDfs.groupby('dosis')['id'].count())

    # Exercici 8. Fes una agrupació del camp evolució, i compta quants pacients tenen 
    # cada tipus d'evolució.

    # Un cop fet, crea un gràfic circular.
    joinDfs.groupby('evolució')['id'].count().plot(kind="pie", legend=False, autopct="%1.1f%%")
    plt.show()




    