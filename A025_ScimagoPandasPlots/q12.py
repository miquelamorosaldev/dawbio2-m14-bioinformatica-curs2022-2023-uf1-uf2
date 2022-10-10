# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q12. List rows with NAs
# -----------------------------------------------------------------------------


# Pandas read_csv() converts empty strings to np.nan by default. Read docs.
# -----------------------------------------------------------------------------
def q12():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Are there empty strings? No.
    empty_strings_mask:             pd.DataFrame = (entries.loc[:, :] == '')
    rows_with_empty_strings_mask:   pd.Series    = empty_strings_mask.any(axis='columns')
    num_rows_with_empty_strings:    int          = rows_with_empty_strings_mask.sum()

    print("Number of rows with empty strings:", num_rows_with_empty_strings)


    # Are there np.nan? Yes!
    #mask with na's true/false
    na_mask:            pd.DataFrame = entries.loc[:, :].isna()
    #rows mask if it have na's values
    rows_with_na_mask:  pd.Series    = na_mask.any(axis='columns')
    #cols mask if it have na's values
    cols_with_na_mask:  pd.Series    = na_mask.any(axis='index')
    #count rows with na'
    num_rows_with_na:   int          = rows_with_na_mask.sum()


    # Print and save to disk
    print("Number of rows with NAs:", num_rows_with_na)
    print(entries.loc[rows_with_na_mask, cols_with_na_mask])
    entries.loc[rows_with_na_mask, :].to_html("scimago-medicine-nas.html")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q12()
# -----------------------------------------------------------------------------
