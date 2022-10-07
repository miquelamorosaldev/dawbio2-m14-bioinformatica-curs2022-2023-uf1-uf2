# Imports
import file_utils
import re
import pprint

# * [Q1. How many entries are in scimago-medicine.csv?](#ex1)
# * [Q2. Show the first 25 entries.](#ex2)
# * [Q3 - How many entries are from Spain? (Country = Spain)](#ex3)
# * [Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) with an H-Index greater than 200.](#ex4)
# * [Q5 - What types of scientific publications are in the file ?](#ex5)
# * [Q52 - What types of scientific publications are in the file ?](#ex52)
# * [Q6 - List all the avaliable categories. Each entry can have more than one category.](#ex6)
# * [Q7 - Show all data from the category with most entries."](#ex7)
# * [Q8 - Show all data from entries of categories: "Sports Medicine" or "Sports science"](#ex8)
# * [Q9 - All regions covered by all entries.](#ex9)
# * [Q10 - Mean of H-index by region.](#ex10)
# * [Q11 - What is the oldest publisher that is still active?](#ex11)

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------
def q1(entries: list[dict]) -> int:
    num:     int        = len(entries)
    print("First entry:")
    pprint.pp(entries[0])
    return num

# -----------------------------------------------------------------------------
# Q2. Show the first 25 entries.
# -----------------------------------------------------------------------------
def q2(entries: list[dict]):
    print(entries[0:25])

# -----------------------------------------------------------------------------
# Q3 - How many entries are from Spain?
# Expected result = 135.
# -----------------------------------------------------------------------------

def is_spain_entry (entry:dict) -> bool:
    return entry['Country'] == 'Spain'

def q3(entries: list[dict]) -> int:
    entries_spain = list(filter(is_spain_entry,entries))
    return entries_spain


# -----------------------------------------------------------------------------
# Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) 
# with an H-Index greater than 200.](#ex4)
# -----------------------------------------------------------------------------
def filterUKJournalHIndex300 (entry:dict) -> bool:
    return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200

def q4(entries: list[dict]) -> int:
    entriesUKJournalHIndex300 = list(filter(filterUKJournalHIndex300,entries))
    return entriesUKJournalHIndex300


# -----------------------------------------------------------------------------
# Question 5 What types of scientific publications are in the file ?
# -----------------------------------------------------------------------------
def q5(entries: list[dict]) -> set:
    types_set: set = set()
    for entry in entries:
        types_set.add(entry['Type'])

    return types_set

#  -----------------------------------------------------------------------------
# QUESTION 5.2 How many publications are from each Type ???? 
# ------------------------------------------------------------------------------
# Expected result:
# {'journal': 7082, 'book series': 27, 'conference and proceedings': 5, 'trade journal': 4}
def q52(entries: list[dict]) -> dict:
    dict_entries_each_type = {}
    for entry in entries:
        # if Type don't exist, we add it in the dict.
        if (not (entry['Type'] in dict_entries_each_type)):
            dict_entries_each_type[entry['Type']]=1
        # if Type exist, we sum 1 more publication.
        else:
            dict_entries_each_type[entry['Type']] = dict_entries_each_type[entry['Type']] + 1
    return dict_entries_each_type

#  -----------------------------------------------------------------------------
# Exercici6 List all the avaliable categories. Each entry can have more 
# than one category.
# ------------------------------------------------------------------------------
# One entry can belong to one or more categories. These are separated by semicolon (;) 
# You should remove the quarter characters (Q1),(Q2)... between categories.

def q6(entries: list[dict]) -> list[str]:
    categories_set: set = set() #Millor així. Desambigua
    for entry in entries:
        #Separa, en función de los delimitadores que le pongas
        # entryCategories = entry.split(';')
        entry_categories: list[str] = entry['Categories'].split(';')
        for category in entry_categories:
            clean_category: str = file_utils.simple_clean_entries(category)
            categories_set.add(clean_category)

    categories_list: list[str] = sorted(categories_set)
    return categories_list

# -----------------------------------------------------------------------------
# Question 7 - Sort categories by number of publications.
# -----------------------------------------------------------------------------

def q7(entries: list[dict]):
    categories_num_dict = {}
    for entry in entries:
        # if Category don't exist, we add it in the dict.
        list_categories_entry = re.split(';', entry['Categories'])
        for category_entry in list_categories_entry:
            clean_category_entry = file_utils.simple_clean_entries(category_entry)
            if clean_category_entry in categories_num_dict:
                categories_num_dict[clean_category_entry]+=1
            else:
                categories_num_dict[clean_category_entry]=1

    categories_num_dict=dict(sorted(categories_num_dict.items(), key=lambda item: item[1] , reverse=True))
    # Debug
    # print(categories_num_dict)

    # We show the 20 entries with most publications.
    # We can't slice a dict, only their items as a list.
    # print(categories_num_dict[:20])
    first_twenty_pub = list(categories_num_dict.items())[:20]
    return first_twenty_pub

# -----------------------------------------------------------------------------
# Question 8. Show all data from entries of categories: 
# "Sports Medicine" or "Sports science"
# -----------------------------------------------------------------------------

def q8(entries: list[dict]) -> list[str]:
    list_sports_science_entries = [entry for entry in entries if 'sports' in entry['Categories'].lower()]
    return list_sports_science_entries

# -----------------------------------------------------------------------------
# Question 9. All regions covered by all entries.
# -----------------------------------------------------------------------------
# Expected Result: {'Africa/Middle East', 'Asiatic Region', ... }

def q9(entries: list[dict]) -> list[str]:
    regions_list: dict = set() #Mejor así. Desambigua
    for entrada in entries:
        regions_list.add(entrada['Region'])
    return regions_list


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
# Q10 - Mean of H-index by region.
# -----------------------------------------------------------------------------
def q10(entries: list[dict]) -> list[str]:
    # Get clean entries
    clean_entries: list[dict] = file_utils.clean_entries(entries)

   # Get list of regions
    region_set:  set[str]  = {entry["Region"] for entry in clean_entries}
    region_list: list[str] = sorted(region_set)

    # Calculate H-index average for each region
    h_index_avg_list: list[float] = [get_h_index_avg('Region', region, clean_entries) for region in region_list]

    # Create ranking
    country_ranking: dict[str, float] = dict(zip(region_list, h_index_avg_list))

    # Sort ranking
    sorted_region_ranking: list[tuple[str, float]] = file_utils.sort_ranking(country_ranking)

    # Print ranking.
    # pprint -> pretty data printer.
    # pprint.pp(sorted_region_ranking)
    return sorted_region_ranking


# -----------------------------------------------------------------------------
# Question 11 - What is the oldest publisher that is still active?
#     (Has some publication in 2021)
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
def q11(entries: list[dict]) -> dict[str]:
    
    # Get clean entries
    clean_entries: list[dict] = file_utils.clean_entries(entries)

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
    # pprint.pp(oldest_entry)
    # pprint.pp(oldest_entry['Publisher'])
    return oldest_entry


# -----------------------------------------------------------------------------
# Exercise 1 - Show the number of publications of each Region and each Country.
# -----------------------------------------------------------------------------

def ex1(entries: list[dict]):
    # 1. Get regions name.
    # region_set:  set[str]  = {entry['Region'] for entry in entries}
    # print('Regions list ', region_list)
    num_pubs_region_dict = {}
    for entry in entries:
        region = entry['Region']
        if region in num_pubs_region_dict:
            num_pubs_region_dict[region]+=1
        else:
            num_pubs_region_dict[region]=1

    print("Regions List")
    print(num_pubs_region_dict)

    num_pubs_coutries_dict = {}
    for entry in entries:
        country = entry['Country']
        if region in num_pubs_coutries_dict:
            num_pubs_coutries_dict[country]+=1
        else:
            num_pubs_region_dict[country]=1

    print("Countries List")
    print(num_pubs_coutries_dict)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # First of all, we load the Scimago-Medicine file, 2021 version.
    file_path: str = 'A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv'
    entries: list[dict] = file_utils.read_csv_file(file_path)

    # Now, we call each query, wich are pure functions, and we print the answers.
    # Comment the functions you don't want to call.

    # num:int = q1(entries)
    # print(f"There are {num} entries.")

    # q2(entries)

    # num_entries_spain: int = q3(entries)
    # print('There are ',len(num_entries_spain),' entries from Spain.')

    # entriesUKJournalHIndex300: int = q4(entries)
    # print('There are ', len(entriesUKJournalHIndex300), " results of Q4 query.")
    
    # types_set = q5(entries)
    # print('Q5 -Types of scientific publications.')
    # print(types_set)

    # dict_entries_each_type = q52(entries)
    # print('Q52 - Number of scientific publications of each type.')
    # print(dict_entries_each_type)

    # categories_list = q6(entries)
    # print('Q6 - List all the avaliable categories:')
    # print(categories_list)

    # print('Q7 - Sort 20 first categories by number of publications.:')
    # print(q7(entries))

    # print('Q8 - Show all data from entries of categories: "Sports Medicine" or "Sports science"')
    # print('Sports',len(q8(entries)))

    # print("Q9 - List of all regions from scientific publications.")
    # print(q9(entries))

    print("Q10 - Mean of H-index by region.")
    sorted_region_ranking = q10(entries)
    pprint.pp(sorted_region_ranking)

    print("Q11 - What is the oldest publisher that is still active?")
    pprint.pp(q11(entries))

    # Another exercise.
    #ex1(entries)
# -----------------------------------------------------------------------------