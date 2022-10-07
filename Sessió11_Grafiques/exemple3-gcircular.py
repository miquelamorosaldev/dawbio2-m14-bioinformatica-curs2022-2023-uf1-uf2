# Demo Matplotlib i lectura CSV
import csv
import matplotlib.pyplot as plt

# Read CSV file by file name, with delimiter ';' and utf-8 format.
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result


# Obtingudes de: https://www.naciodigital.cat/municipals2019/municipi/08101/hospitalet-llobregat
csv_file_path: str = "vots-lh-mun-2019.csv"
election19Results: dict = read_csv_file(csv_file_path)

print(election19Results[0])

# Obtenim els vots, regidors i el nom dels partits en 3 llistes separades.
votsPartits: int = []
nomPartits: str = []
regidors: int = []

for resultatPartit in election19Results:
    nomPartits.append(resultatPartit['Partit'])
    votsPartits.append(resultatPartit['NumVots'])
    regidors.append(resultatPartit['Regidors'])

print(nomPartits)
print(votsPartits)
print(regidors)


colorsPartits=["Red","Yellow","Orange","Purple","Blue","Pink"]

# Inicialitzem el gràfic de pastís amb les dades i config. adients
# El percentatge el calcula amb el paràmetre autopct="%1.1f%%".
# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.pie.html
plt.pie( votsPartits, labels=nomPartits, autopct="%1.1f%%", colors=colorsPartits, shadow=True)
plt.title("Resultats Eleccions Municipals 2019 en vots, L'Hospitalet de Llobregat")
plt.show()