# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q11. Transpose the entries
# -----------------------------------------------------------------------------


# Certain operations are easier to understand if you transpose the dataframe.
# But in the case of the Scimago entries it does not help much.
# -----------------------------------------------------------------------------
def q11():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Print transposed entries
    print(entries.T)

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q11()
# -----------------------------------------------------------------------------
