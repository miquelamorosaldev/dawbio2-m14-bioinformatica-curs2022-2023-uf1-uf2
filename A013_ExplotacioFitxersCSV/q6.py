# Imports
import utils

# -----------------------------------------------------------------------------
# Q6. List all Categories (without repeats and merged quarters)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#def get_unique_categories(clean_entries: list[dict]) -> list[str]:
def get_unique_categories(clean_entries):    

    unique_categories_set: set[str] = set()

    for entry in clean_entries:
        categories_list = entry['Categories']

        for category in categories_list:
            unique_categories_set.add(category)

    result: list[str] = sorted(unique_categories_set)
    return result

# -----------------------------------------------------------------------------
def q6():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get unique categories
    unique_categories_list: list[str] = get_unique_categories(clean_entries)

    # Print categories
    print("Categories:")
    for category in unique_categories_list:
        print(category)

    # Print number of categories (287 Categories)
    num = len(unique_categories_list)
    print(f"Number of unique categories: {num}")

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q6()
# -----------------------------------------------------------------------------
