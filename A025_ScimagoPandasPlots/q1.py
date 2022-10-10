# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------

# In DataFrames .size is the total count. len() returns the number of rows.
# -----------------------------------------------------------------------------
def q1():
    
    entries: pd.DataFrame = utils.read_csv_file("./A025_ScimagoPandasPlots/scimago-medicine.csv")
    num:     int          = len(entries)
    
    print("Exporting all entries to html...")
    entries.to_html("scimago-medicine.html")

    print("First entry:")
    print(entries.loc[0, :])

    print(f"There are {num} entries.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q1()
# -----------------------------------------------------------------------------
