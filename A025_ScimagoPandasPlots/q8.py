# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q8. All entries in sports-related categories
# -----------------------------------------------------------------------------


# Warning: str.cotains() uses regexps by default. (!)
# -----------------------------------------------------------------------------
def q8():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Get all expanded categories and corresponding journals
    categories: pd.DataFrame = utils.get_categories(entries)

    # Get unique categories
    unique_categories: pd.Series = (categories.loc[:, 'Category']
                                              .cat
                                              .categories
                                              .to_series()
                                              .reset_index(drop=True)
    )

    # Get sport categories (3 categories)
    sport_mask:       pd.Series = unique_categories.str.contains('Sport')
    sport_categories: pd.Series = unique_categories[sport_mask]
    print("sport categories")
    print(sport_categories)
    
    # Get ids (ranks) in sport-related categories and remove duplicates.
    sport_ids_mask: pd.Series =  categories.loc[:, 'Category'].isin(sport_categories)

    print("sport sport_ids_mask")
    print(sport_ids_mask)
    sport_ids:      pd.Series = (categories.loc[sport_ids_mask, 'Rank']
                                           .drop_duplicates()
                                           .reset_index(drop=True)
    )
    print("sport_ids")
    print(sport_ids)
    # Merge back to get the whole entries
    sport_entries: pd.DataFrame = pd.merge(sport_ids, entries, on='Rank')

    # Print
    print(sport_entries.loc[:, ['Rank', 'Title', 'Publisher', 'Categories']])


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q8()
# -----------------------------------------------------------------------------
