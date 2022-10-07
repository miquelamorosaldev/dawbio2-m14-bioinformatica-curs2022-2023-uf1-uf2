import numpy as np 
import pandas as pd
import copy

# Exercici per repassar el Join i altres comandes.

# Estudi d'un nou tractament per a pacients de Covid persitent.

# covidper_evolucio.csv conté la evolució del tractament.
# covidper_tractaments.csv té la dosi del medicament que s'aplica a cada pacient.

# Aquests 2 fitxers tenen un camp comú, l'id del pacient (1a fila)

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    csv_file_path = "./Sessió10_JoinPandas/covidper_evolucio.csv"
    # Read Evolution File.
    entries: pd.DataFrame = pd.read_csv(csv_file_path, sep=";")
    print(entries)