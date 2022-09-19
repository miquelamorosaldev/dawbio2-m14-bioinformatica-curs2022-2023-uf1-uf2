# Imports
import file_utils
import re
import pprint

# * [Q3 - How many entries are from Spain? (Country = Spain)](#ex3)
# * [Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) with an H-Index greater than 200.](#ex4)
# * [Q5 - What types of scientific publications are in the file ?](#ex5)
# * [Q52 - What types of scientific publications are in the file ?](#ex5)
# * [Q6 - List all the avaliable categories. Each entry can have more than one category.](#ex6)
# * [Q7 - Show all data from the category with most entries."](#ex7)
# * [Q8 - Show all data from entries of categories: "Sports Medicine" or "Sports science"](#ex8)
# * [Q9 - All regions covered by all entries.](#ex9)
# * [Q10 - Mean of H-index by region.](#ex10)
# * [Q11 - What is the oldest publisher that is still active?](#ex11)

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------
def q1(entries: list[dict]):
    num:     int        = len(entries)
    print("First entry:")
    pprint.pp(entries[0])

    print(f"There are {num} entries.")

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

def q3(entries: list[dict]):
    entries_spain = list(filter(is_spain_entry,entries))
    print('There are ',len(entries_spain),' entries from Spain.')


# -----------------------------------------------------------------------------
# Q4 - Show all the journals (Type = journal) published in UK (Country = United Kingdom) with an H-Index greater than 200.](#ex4)
# -----------------------------------------------------------------------------
def filterUKJournalHIndex300 (entry:dict) -> bool:
    return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' and int(entry['H index']) > 200

def q4(entries: list[dict]):
    entriesUKJournalHIndex300 = list(filter(filterUKJournalHIndex300,entries))
    print('There are ', len(entriesUKJournalHIndex300), " results of Q4 query.")

# -----------------------------------------------------------------------------
# Question 5 What types of scientific publications are in the file ?
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Question 7 Order (sort) categories by number of publications.
# -----------------------------------------------------------------------------

# def q7(entries: list[dict]):
#     categories_num_dict = {}
#     for entry in entries:
#         # if Category don't exist, we add it in the dict.
#         list_categories_entry = re.split(';', entry['Categories'])
#         for category_entry in list_categories_entry:
#             clean_category_entry = file_utils.clean_entries(category_entry)
#             if clean_category_entry in categories_num_dict:
#                 categories_num_dict[clean_category_entry]+=1
#             else:
#                 categories_num_dict[clean_category_entry]=1

#     categories_num_dict=dict(sorted(categories_num_dict.items(), key=lambda item: item[1] , reverse=True))
#     print(categories_num_dict)

#     # At last, we show the 20 entries with most publications.
#     # We can't slice a dict, only their items as a list.
#     # print(categories_num_dict[:20])
#     first_twenty_pub = list(categories_num_dict.items())[:20]
#     print(first_twenty_pub)

# regiones: dict = set() #Mejor así. Desambigua
# for entrada in entries:
#     regiones.add(entrada['Region'])

# print("Q9 - REGIONS.")
# print(regiones)


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

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    file_path: str = 'A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv'
    entries: list[dict] = file_utils.read_csv_file(file_path)
    q1(entries)
    q2(entries)
    q3(entries)
    q4(entries)
    #q7(entries)
    ex1(entries)
# -----------------------------------------------------------------------------