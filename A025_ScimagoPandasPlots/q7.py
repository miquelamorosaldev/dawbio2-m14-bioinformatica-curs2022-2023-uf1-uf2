# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q7. Top 20 categories with most entries
# -----------------------------------------------------------------------------


# Stable sorting to keep alphabetical order on ties.
# -----------------------------------------------------------------------------
def q7():
    
    # Read entries
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Get all expanded categories and corresponding journals
    categories: pd.DataFrame = utils.get_categories(entries)

    # Group
    category_top20: pd.DataFrame = (categories
                                    .groupby(by='Category')
                                    .count()
                                    .rename(columns={'Rank': 'Number of Entries'})
                                    .sort_values(by='Number of Entries',
                                                 ascending=False,
                                                 kind='stable')
                                    .head(20)
    )

    print(category_top20)


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q7()
# -----------------------------------------------------------------------------
