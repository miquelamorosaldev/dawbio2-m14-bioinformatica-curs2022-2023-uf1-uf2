# Imports
import utils

# -----------------------------------------------------------------------------
# Q6. List all Categories (without repeats and merged quarters)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q6():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get unique categories
    unique_categories_list: list[str] = utils.get_unique_categories(clean_entries)

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
