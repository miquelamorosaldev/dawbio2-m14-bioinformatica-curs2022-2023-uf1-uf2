# _____________ fileUtils ________________ #

# Mètode vell per llegir el CSV i portar-lo a un diccionari.
# Aquest també va bé.
import csv 

# Funció que llegeix un fitxer CSV i el posa en una llista.
# Algoritme versions antigues.
def read_csv_file_old(csv_file_path: str) -> list:
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result

# Mètode nou, usar la lliberia nativa.
from pathlib import Path

# Algoritme més eficient, llibreria Pathlib.
# Per ara no m'ha sortit aquest mètode, pot llegir el fitxer però no en el format
# exacte per tal d'aprofitar les respostes dels exercicis.

def read_csv_file(csv_file_path: str) -> list:
    '''Input:  The file contents as a single string.
      Output: A list of strings where each string is a row of the csv file.'''
   
    raw_text:      str = Path(csv_file_path).read_text()
    stripped_text: str = raw_text.strip()
    rows: list[str] = stripped_text.split("\n")
    result = [row_dict for row_dict in rows]

    return result


# _____________ main ________________ #
 
csv_file_path = "scimago-medicine.csv"

# Old way.
#entries = read_csv_file(csv_file_path)

entries = read_csv_file_old(csv_file_path)

print(entries[0:1])

#Fixeu-vos que cada element d'entries és un diccionari, i cada camp ('Rank' : '1') és una línia del diccionari.
dict = {} 

## Q1. Num of entries.
num = len(entries)
# Restem la capçalera.
print(f"There are {num-1} entries.")

## Q2. Mostra les primeres 15 entrades.
print(entries[1:15])

## Q3. Compta el número d'entrades publicades a Espanya en una llista (Country = Spain).
def isSpainEntry (entry:dict) -> bool:
    return entry['Country'] == 'Spain'

entriesSpain = list(filter(isSpainEntry,entries))
print(len(entriesSpain))

## Q4. Mostra les revistes (Type = journal) publicades a UK (Country = United Kingdom) i que tinguin un H index superior a 200.

def filterUKJournalHIndex300 (entry:dict) -> bool:
    return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200

entriesUKJournalHIndex300 = list(filter(filterUKJournalHIndex300,entries))
print(len(entriesUKJournalHIndex300))

## Q5. Detectar tots els valors de la columna Type: journal, book series, ...

# La estructura set només afegeix valors si no s'han inserit abans.
TypeValuesSet: set = set()
NumTypeValuesDict: dict = {}

for entry in entries:
    TypeValuesSet.add(entry['Type'])

print(TypeValuesSet)

# Si volem comptar quants n'hi ha posem els resultats en un dictionari.
for entry in entries:
    TypeValuesSet.add(entry['Type'])
    if( not (entry['Type']) in NumTypeValuesDict):
        NumTypeValuesDict[entry['Type']] = 1
    else:
        NumTypeValuesDict[entry['Type']] = NumTypeValuesDict[entry['Type']] + 1

print(NumTypeValuesDict)


#q8 i q9

# Q6. Guardar quines categories (Categories) existeixen.
# Fixeu-vos que una entrada pot pertanyer a més d'una categoria, i estan seperades per ;
# També hem d'esborrar els paràmetres que hi diu (Q1),(Q2)... que hi ha entremig.

def remove_quarter(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"
    result = category
    result = result.replace("(Q1)", "")
    result = result.replace("(Q2)", "")
    result = result.replace("(Q3)", "")
    result = result.replace("(Q4)", "")
    return result


categoriesSet: set = set() #Millor així. Desambigua
for entry in entries:
    #Separa, en función de los delimitadores que le pongas
    ## entryCategories = entry.split(';')
    entryCategories: list[str] = entry['Categories'].split(';')
    for category in entryCategories:
        cleanCategory: str = remove_quarter(category)
        categoriesSet.add(cleanCategory)

categoriesList: list[str] = sorted(categoriesSet)

print(len(categoriesSet))
print(categoriesList)

#    for category in entryCategories:
#        position=category.find(" (Q")
#        if (position!=-1):
#            cate = cate[:posicion] 