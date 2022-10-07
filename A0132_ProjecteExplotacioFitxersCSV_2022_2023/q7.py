# Imports
import utils

# -----------------------------------------------------------------------------
# Q7. Top 20 categories with most entries
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def get_num_entries(category: str, clean_entries: list[dict]) -> int:

    num_entries = 0

    for entry in clean_entries:
        categories_list: list[str] = entry['Categories']
        
        if category in categories_list:
            num_entries += 1

    return num_entries

# -----------------------------------------------------------------------------
def q7():
    
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get unique categories
    unique_categories_list: list[str] = utils.get_unique_categories(clean_entries)

    # Make ranking
    category_ranking: dict[str, int] = {category: get_num_entries(category, clean_entries) for category in unique_categories_list}

    # Sort ranking
    sorted_category_ranking: list[tuple[str, int]] = utils.sort_ranking(category_ranking)

    # Get Top 20
    top20_list: list[tuple[str, int]] = sorted_category_ranking[0:20]

    # Print top 20
    print("Top 20 Categories:")
    for item in top20_list:
        category:    str = item[0]
        num_entries: int = item[1]
        print(f"{category}: {num_entries}")

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q7()
# -----------------------------------------------------------------------------
