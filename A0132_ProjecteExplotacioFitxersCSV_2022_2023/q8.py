# Imports
import utils

# -----------------------------------------------------------------------------
# Q8. All entries in sport-related categories
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def is_sport_entry(clean_entry: dict, sport_categories: list[str]) -> bool:

    result:           bool      = False
    entry_categories: list[str] = clean_entry['Categories']

    for category in entry_categories:
        if category in sport_categories:
            result = True

    # return set(entry_categories) & set(sport_categories)
    return result

# -----------------------------------------------------------------------------
def q8():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get unique categories
    unique_categories_list: list[str] = utils.get_unique_categories(clean_entries)

    # Get sport categories
    sport_categories: list[str] = [category for category in unique_categories_list if ('Sports' in category)]

    # Get sport entries
    sport_entries: list[dict] = [entry for entry in clean_entries if is_sport_entry(entry, sport_categories)]
    
    # Print number of sport entries (355)
    num: int = len(sport_entries)
    print(f"There are {num} sport entries")

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q8()
# -----------------------------------------------------------------------------
