# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q4. What is the oldest publisher that is still active?
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
def q4():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

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


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q4()
# -----------------------------------------------------------------------------
