# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q6. List all Categories (without repeats and merged quarters)
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q6():
    
    # Read entries
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Get all expanded categories and corresponding journals
    categories: pd.DataFrame = utils.get_categories(entries)

    # Get unique categories
    category_series:    pd.Series = categories.loc[:, 'Category']
    unique_categories:  pd.Index  = category_series.cat.categories

    # Print
    print(unique_categories)

    # Save to disk
    (unique_categories
    .to_frame()
    .reset_index(drop=True)
    .to_html('scimago-categories.html')
    )


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q6()
# -----------------------------------------------------------------------------
