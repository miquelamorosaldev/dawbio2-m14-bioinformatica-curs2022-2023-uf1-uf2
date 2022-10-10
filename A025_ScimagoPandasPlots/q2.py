# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q2. What types of scientific publications are in the file?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q2():

    # Get regions
    entries:      pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")
    unique_types: pd.Series    = (entries.loc[:, "Type"]
                                         .drop_duplicates()
                                         .sort_values()
                                         .reset_index(drop=True)
    )

    # Prepare output
    num:              int          = len(unique_types)
    unique_types_str: str          = ", ".join(unique_types)

    # Print
    print(f"There are {num} different types of publications: {unique_types_str}")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q2()
# -----------------------------------------------------------------------------
