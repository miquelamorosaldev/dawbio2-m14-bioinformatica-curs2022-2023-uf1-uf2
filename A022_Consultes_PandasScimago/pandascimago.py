import numpy as np
import pandas as pd
import copy


# Seleccionar i mostrar les entries amb H index superior
def q1_hindex_gt_450(entries):
    entries_high = entries.loc[:,"H index"] >= 450
    entries_ok = entries.loc[entries_high,:]

    #Provem que ha funcionat
    print(entries_ok.loc[:,["Title","H index"]])


# Amb el loc també podem editar files del dataframe.

#canviar totes les entrades menors de 750 a h_index negatiu
def q2_hindex_lesser_750(entries):
    entries2 = copy.deepcopy(entries)

    # Màscara per a seleccionar només els que tenen menys de 750
    bad_entries_mask = (entries2.loc[:,"H index"] < 750)

    # Aquesta és la lína que edita els H Index, els posa un 0. 
    entries2.loc[bad_entries_mask,"H index"] = 0;

    # Ordena els valors i mostra els 10 primers.
    entries2 = entries2.sort_values(by=["H index"], 
                            axis=0, 
                            ascending=False).head(10)

    print("Canvi valors.")
    #Provem que ha funcionat
    print(entries2.loc[:,["Title","H index"]])


# Canviem el tipus de publicació, de Journal a Diari.

# Opcions de mask.
# Amb el loc, indiquem clarament quina fila i columna volem seleccionar.
def q3_pub_journal_to_diari(entries):
    entries2 = copy.deepcopy(entries)
    journals = entries2.loc[:,"Type"] == 'journal'
    #journals = entries2.loc[:,"Type"].str.contains('journal')
    print(journals.head(100))

    # Aquesta és la lína que edita els H Index, els posa un 0. 
    entries2.loc[journals,"Type"] = 'Diari';
    print(entries2.loc[:,["Title","Type"]])


# També ho podem fer amb el replace.

# entries3 = entries2.replace('journal','diari')
# print(entries3.loc[:,["Title","Type"]])

# Modificar el valor de tots els Publisher, que actualment esta informat a null, passar-los a np.nan.
# Clean NAs

def q4_publisher_nan(entries):
    entries4 = copy.deepcopy(entries)

    # Pas 1. Cercar valors nuls amb la màscara.
    print("Valors Publisher nuls o buits ??")

    entries4.loc[:,"Publisher"].isnull().value_counts()
    null_publisher_mask = entries4.loc[:,"Publisher"].isnull()

    # Pas 2. Comprovem el resultat de la màscara. 
    # En general: df.loc(MASK,FIELD)
    #print(entries4.loc[null_publisher_mask,"Publisher"] )

    # Pas 3. Substituïr els nulls per np.nan, aplicant la màscara.
    # En general: df.loc(MASK,FIELD) = VALUE.
    entries4.loc[null_publisher_mask,"Publisher"] = np.nan

    # Pas 4. Mostrem un resultat per a provar.
    print(entries4.iloc[62,:])



# Actualitzar tots els registres que es troben a nulls, o a nan, 
# amb un valor fixe de String="Unkown Publisher".
def q5_unknown_publishers(entries):
    entries5 = copy.deepcopy(entries)
    #2 opcions , aquestes dues linees, fan el mateix que utilitzant el parametre inplace
    update_publisher = entries5.loc[:,"Publisher"].fillna(value="Unkown Publisher")
    entries5.loc[:,"Publisher"] = update_publisher
    #segona opcio amb inplace, ho canvia a la mateixa linea (abans no)
    #entries5.loc[:,"Publisher"].fillna(value="Unkown Publisher",inplace=True)

    print(entries5.iloc[485,:])


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    csv_file_path = "./Sessió9_PandasScimago/scimago-medicine.csv"

    # Read scimago ranking
    entries: pd.DataFrame = pd.read_csv(csv_file_path, sep=";")
    print(entries)

    q1_hindex_gt_450(entries)
    q2_hindex_lesser_750(entries)
    q3_pub_journal_to_diari(entries)
    q4_publisher_nan(entries)
    q5_unknown_publishers(entries)

# -----------------------------------------------------------------------------
