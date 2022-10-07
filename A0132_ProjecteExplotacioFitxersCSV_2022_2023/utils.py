# Imports
import csv
import copy
import re
from numbers import Number


# -----------------------------------------------------------------------------
# Read CSV File
# -----------------------------------------------------------------------------

# See 'open' docs to understand the newline parameter
# DictReader converts each row in csv_file in a dictionary.
# The dictionary keys are the column names.
# -----------------------------------------------------------------------------
def read_csv_file(csv_file_path: str) -> list[dict]:
    
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        result     = [row_dict for row_dict in csv_reader]

    return result


# Uses unnecessary copy(). replace() returns a new copy each time.
# Instead of replace() you can use a regexp.
# -----------------------------------------------------------------------------
def remove_quarter(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"

    result = copy.copy(category)

    result = result.replace("(Q1)", "")
    result = result.replace("(Q2)", "")
    result = result.replace("(Q3)", "")
    result = result.replace("(Q4)", "")

    return result


# -----------------------------------------------------------------------------
def get_clean_categories(categories_str: str) -> list[str]:
    "Returns a clean list of the categories in categories_str."

    # Split categories
    categories_list: list[str] = categories_str.split(';')

    # Remove quarter ids
    categories_merged_list: list[str] = [remove_quarter(category) for category in categories_list]

    # Trim whitespaces
    categories_clean_list: list[str] = [category.strip() for category in categories_merged_list]

    return categories_clean_list

# -----------------------------------------------------------------------------
def clean_entry(entry: dict) -> dict:
    "Returns a copy of the original entry with several fixed values."

    # Make a copy of the entry.
    result: dict = copy.deepcopy(entry)

    # Get values to be fixed
    categories_str: str = result['Categories']
    h_index_str:    str = result['H index']

    # Fix values
    result['Categories'] = get_clean_categories(categories_str)
    result['H index']    = int(h_index_str)

    # Return the result with Categories as a list of clean strings
    return result


# -----------------------------------------------------------------------------
def clean_entries(raw_entries: list[dict]) -> list[dict]:
    "Returns a copy of the entries with cleanup values: Categories, H-Index"
    clean_entries: list[dict] = [clean_entry(entry) for entry in raw_entries]
    return clean_entries


# -----------------------------------------------------------------------------
# Get unique categories
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def get_unique_categories(clean_entries: list[dict]) -> list[str]:

    unique_categories_set: set[str] = set()

    for entry in clean_entries:
        categories_list = entry['Categories']

        for category in categories_list:
            unique_categories_set.add(category)

    result: list[str] = sorted(unique_categories_set)
    return result



# -----------------------------------------------------------------------------
# Dict-related functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def reverse_dict(d: dict[object, object]) -> dict[object, list[object]]:
    """Reverses keys and values. Works for any dict.
       Allows duplicate values in d.
       The result has all values in lists."""

    result: dict = {}

    for key, value in d.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)

    return result

# Sort dict by values: https://docs.python.org/es/3/howto/sorting.html
# -----------------------------------------------------------------------------
def sort_ranking(ranking: dict[str, Number]) -> list[tuple[str, Number]]:
    """Sorts dictionary. Expects keys to be strings and values to be numbers.
       Returns a list of tuples."""

    ranking_items:  list[tuple[str, Number]] = list(ranking.items())
    get_num:        function                 = lambda item: item[1]
    sorted_ranking: list[tuple[str, Number]] = sorted(ranking_items, key=get_num, reverse=True)

    return sorted_ranking

# -----------------------------------------------------------------------------
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
