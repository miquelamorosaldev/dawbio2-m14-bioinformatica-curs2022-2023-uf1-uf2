# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q3. How many types of journal has each publisher?
#     (Group publisher by number of types)
# -----------------------------------------------------------------------------


# In the csv file some Publishers are an empty string ''.
# These are converted to np.nan automatically by Pandas when reading the file.
# -----------------------------------------------------------------------------
def q3():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Group by Publisher, calculate number of uniques Types
    publisher_numtypes: pd.DataFrame = (entries.loc[:, ["Publisher", "Type"]]
                                        .groupby("Publisher")
                                        .nunique()
                                        .rename(columns={"Type": "NumTypes"})
                                        .sort_values(by="NumTypes", ascending=False)
    )
    print(publisher_numtypes)
    # Group by NumTypes, calculate number of unique Publishers
    numtypes_numpublishers: pd.DataFrame = (publisher_numtypes
                                            .reset_index()
                                            .groupby("NumTypes")
                                            .nunique()
                                            .rename(columns={"Publisher": "NumPublishers"})
    )

    # Print results
    print("Number of different types and number of different publishers:")
    print(numtypes_numpublishers)
    print()

    # print("Publishers with two different types of journals:")
    two_types_mask:       pd.Series    = (publisher_numtypes.loc[:, "NumTypes"] == 2)
    two_types_publishers: pd.DataFrame = publisher_numtypes.loc[two_types_mask, :]
    print(two_types_publishers)


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q3()
# -----------------------------------------------------------------------------
