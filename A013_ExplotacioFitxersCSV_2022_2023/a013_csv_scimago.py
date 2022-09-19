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


#csv_file_path = "scimago-medicine.csv"
csv_file_path = "./A013_ExplotacioFitxersCSV_2022_2023/scimago-medicine.csv"

print('Path = ',Path().absolute())

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

def clean_entries(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"
    " and without spaces."
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
        clean_category: str = clean_entries(category)
        categories_set.add(clean_category)

categories_list: list[str] = sorted(categories_set)

#print(len(categories_set))
#print(categories_list)

# Solution from students :)
def q6(data: list[dict[str, str]]) -> list[str]:
    return sorted(list( set( sum([clean_entries(dictionary['Categories']).split(';') for dictionary in data], []))))

q6_result = q6(entries)
#print(q6_result)


# Question 7. Order categories by num of publications.

# Solucion 71. New query. 2021-2022.

categories_num_dict = {}
for entry in entries:
    # if Category don't exist, we add it in the dict.
    list_categories_entry = re.split(';', entry['Categories'])
    for category_entry in list_categories_entry:
        clean_category_entry = clean_entries(category_entry)
        if clean_category_entry in categories_num_dict:
            categories_num_dict[clean_category_entry]+=1
        else:
            categories_num_dict[clean_category_entry]=1

categories_num_dict=dict(sorted(categories_num_dict.items(), key=lambda item: item[1] , reverse=True))
print(categories_num_dict)

# We show the 20 entries with most publications.
# We can't slice a dict, only their items as a list.
# print(categories_num_dict[:20])
first_twenty_pub = list(categories_num_dict.items())[:20]
print(first_twenty_pub)


# Question 8. Show all data from entries of categories: "Sports Medicine" or "Sports science"

# Expected Result (aprox.) 355. 
# Expected Result without removing Quarters (aprox.) 369. 

list_sports_science_entries = [entry for entry in entries if 'sports' in entry['Categories'].lower()]
print('Sports',len(list_sports_science_entries))

# list_result = (set(list_sports_science_entries), set(list_sports_medicine_entries) )


# Question 9. All regions covered by all entries.
# EXP. RESULT 
# {'Africa/Middle East', 'Asiatic Region', 'Latin America', 'Western Europe', 'Pacific Region', 'Middle East', 'Northern America', 'Africa', 'Eastern Europe'}

regiones: dict = set() #Mejor así. Desambigua
for entrada in entries:
    regiones.add(entrada['Region'])

print("Q9 - REGIONS.")
print(regiones)


# Question 10. Mean of H-index by region.
# Pablo Solution.

# Expected Result. (moreless)
# Northern America - 65.21652816251154, Western Europe - 54.08188428706924 ...
# Africa - 17.75

import utils
import pprint

def get_h_index_avg(filter_key: object, filter_value: object, clean_entries: list[dict]) -> float:
    "Filters entries and returns their H-Index average."

    # Filter entries
    filtered_entries: list[dict] = [entry for entry in clean_entries if entry[filter_key] == filter_value]

    # Get all H-Indexes of filtered entries
    h_index_list: list[int] = [entry['H index'] for entry in filtered_entries]

    # Calcualte H-Index average
    h_index_avg: float = sum(h_index_list) / len(h_index_list)

    return h_index_avg

# -----------------------------------------------------------------------------
def q10():
    # Get clean entries
    clean_entries: list[dict] = utils.clean_entries(entries)

   # Get list of regions
    region_set:  set[str]  = {entry["Region"] for entry in clean_entries}
    region_list: list[str] = sorted(region_set)

    # Calculate H-index average for each region
    h_index_avg_list: list[float] = [get_h_index_avg('Region', region, clean_entries) for region in region_list]

    # Create ranking
    country_ranking: dict[str, float] = dict(zip(region_list, h_index_avg_list))

    # Sort ranking
    sorted_region_ranking: list[tuple[str, float]] = utils.sort_ranking(country_ranking)

    # Print ranking.
    # pprint -> pretty data printer.
    pprint.pp(sorted_region_ranking)

print("Q10 - Mean of H-index by region.")
q10()

# Question 11 - What is the oldest publisher that is still active?
#     (Has some publication in 2021)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def get_first_year(entry: dict) -> int:

    coverage_str:   str = entry['Coverage']
    first_year_str: str = coverage_str[0:4]
    first_year_int: int = int(first_year_str)

    return first_year_int

# -----------------------------------------------------------------------------
def get_last_year(entry: dict) -> int:

    coverage_str:  str = entry['Coverage']
    last_year_str: str = coverage_str[-4:]
    last_year_int: int = int(last_year_str)

    return last_year_int

# -----------------------------------------------------------------------------
def q11():
    
    # Get clean entries
    clean_entries: list[dict] = utils.clean_entries(entries)

    # Constants
    CURRENT_YEAR: int = 2021

    # Filter entries: Only those who are still publishing
    filtered_entries: list[dict] = [entry for entry in clean_entries
                                    if get_last_year(entry) == CURRENT_YEAR]

    # Get oldest entry
    first_year_list:    list[int] = [get_first_year(entry) for entry in filtered_entries]
    oldest_year:        int       = min(first_year_list)
    oldest_entry_index: int       = first_year_list.index(oldest_year)
    oldest_entry:       dict      = filtered_entries[oldest_entry_index]

    # Print
    pprint.pp(oldest_entry)
    pprint.pp(oldest_entry['Publisher'])

print("11 - What is the oldest publisher that is still active?")
q11()