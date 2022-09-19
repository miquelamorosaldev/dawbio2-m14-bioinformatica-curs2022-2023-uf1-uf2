# ______ UTILS ______ #
# How to import a notebook a file
import csv
from pathlib import Path

# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result

# Llegir el mateix fitxer amb la llibreria Pathlib.
# No aconsegueixo que em posi les entries en un diccionar.
def read_csv_file_pathlib(csv_file_path: str) -> list:
    '''Input:  The file contents as a single string.
      Output: A list of strings where each string is a row of the csv file.'''
   
    raw_text:      str = Path(csv_file_path).read_text()
    stripped_text: str = raw_text.strip()
    rows: list[str] = stripped_text.split("\n")
    result = [row_dict for row_dict in rows]

    return result


csv_file_path = "scimago-medicine.csv"
entries = read_csv_file(csv_file_path)
print(entries[0])

# Exercici1 How many entries are in scimago-medicine.csv?
print(len(entries))

# Exercici2 Show the first 25 entries.
print(entries[0:25])

# Exercici3 Compta el número d'entrades publicades a Espanya en una llista (Country = Spain)
num_entries_spain: int = 0
for entry in entries:
    if(entry['Country'] == 'Spain'):
        num_entries_spain+=1
#print(num_entries_spain)


# Possible solució amb filter.
def is_spain_entry (entry:dict) -> bool:
    return entry['Country'] == 'Spain'

entries_spain = list(filter(is_spain_entry,entries))
print(len(entries_spain))

# Sol 3. List Comp.
# https://riptutorial.com/python/example/767/conditional-list-comprehensions
result = [entry for entry in entries if entry['Country'] == 'Spain' ]
print('There are ',len(result),' entries.')

# Expected result = 135.

# Exercici4 - Mostra les revistes (Type = journal) publicades 
# a UK (Country = United Kingdom) 
# i que tinguin un H index superior a 200.

# Expected result = 62.

num_entries_filtered: int = 0
for entry in entries:
    if(entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200):
        num_entries_filtered+=1


def filterUKJournalHIndex300 (entry:dict) -> bool:
    return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200

entriesUKJournalHIndex300 = list(filter(filterUKJournalHIndex300,entries))
print(entriesUKJournalHIndex300)

expected_result_q4 = 62

if(len(entriesUKJournalHIndex300) == 62):
    print("Query OK!") 

# Question 5 What types of scientific publications are in the file ? Show the name of all types.

# Expected Result:
# ['journal', 'book series', 'conference and proceedings', 'trade journal']

types_set: set = set()
for entry in entries:
    types_set.add(entry['Type'])

print('Types of scientific publications.')
print(types_set)

# QUESTION 5.2 How many publications are from each Type ???? 

# Expected result:
# {'journal': 7082, 'book series': 27, 'conference and proceedings': 5, 'trade journal': 4}

num_entries_type = {}
for entry in entries:
    # if Type don't exist, we add it in the dict.
    if (not (entry['Type'] in num_entries_type)):
        num_entries_type[entry['Type']]=1
    # if Type exist, we sum 1 more publication.
    else:
        num_entries_type[entry['Type']] = num_entries_type[entry['Type']] + 1

print(num_entries_type)



# Exercici6 List all the avaliable categories. Each entry can have more than one category.
# One entry can belong to one or more categories. These are separated by semicolon (;) 
# You should remove the quarter characters (Q1),(Q2)... between categories.


# ** Hint **
# import re
# text = "python is, an easy;language; to, learn."
# print(re.split('; |, ', text))
# ['python is', 'an easy;language', 'to', 'learn.']

import re

def remove_quarter(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"
    " Pending apply regex. Q(*) "
    result = category
    result = re.sub(" ?\(Q\d\)", "", result)
    result = result.strip()
    return result


categories_set: set = set() #Millor així. Desambigua
for entry in entries:
    #Separa, en función de los delimitadores que le pongas
    ## entryCategories = entry.split(';')
    entry_categories: list[str] = entry['Categories'].split(';')
    for category in entry_categories:
        clean_category: str = remove_quarter(category)
        categories_set.add(clean_category)

categories_list: list[str] = sorted(categories_set)

#print(len(categories_set))
#print(categories_list)

# Solution from students :)
def q6(data: list[dict[str, str]]) -> list[str]:
    return sorted(list( set( sum([remove_quarter(dictionary['Categories']).split(';') for dictionary in data], []))))

q6_result = q6(entries)
#print(q6_result)


# Question 7. Order categories by num of publications.

# We get the clean categories, from question 6.

# NOT TODAY.


# Question 8. Show all data from entries of categories: "Sports Medicine" or "Sports science"

# Pending: Remove quarters.

# Expected Result (aprox.) 355. 
# Expected Result without removing Quarters (aprox.) 369. 

list_sports_science_entries = [entry for entry in entries if 'sports' in entry['Categories'].lower()]

#print('Sports',len(list_sports_science_entries))

# list_result = (set(list_sports_science_entries), set(list_sports_medicine_entries) )


# Question 9. All regions covered by all entries.
# EXP. RESULT 
# {'Africa/Middle East', 'Asiatic Region', 'Latin America', 'Western Europe', 'Pacific Region', 'Middle East', 'Northern America', 'Africa', 'Eastern Europe'}

regiones: dict = set() #Mejor así. Desambigua
for entrada in entries:
    regiones.add(entrada['Region'])


print("Q9 - REGIONS.")
print(regiones)