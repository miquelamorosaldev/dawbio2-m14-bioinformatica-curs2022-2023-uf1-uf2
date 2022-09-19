# Imports
import utils
import pprint


# * [Q1 - How many entries are in scimago-medicine.csv?](#ex1)
# * [Q2 - Show the first 25 entries.](#ex2)
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

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    file_path: str = 'A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv'
    entries: list[dict] = utils.read_csv_file(file_path)
    q1(entries)
    q2(entries)
# -----------------------------------------------------------------------------