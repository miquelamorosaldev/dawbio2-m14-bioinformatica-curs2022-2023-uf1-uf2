# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q9. All regions covered by all entries
# -----------------------------------------------------------------------------

# .size() equals to (len) in Series. In DataFrames it is the total count.
# -----------------------------------------------------------------------------
def q9():

    # Get regions
    entries:          pd.DataFrame = utils.read_csv_file("./A025_ScimagoPandasPlots/scimago-medicine.csv")
    unique_regions:   pd.Series    = (entries.loc[:, "Region"]
                                             .drop_duplicates()
                                             .sort_values()
                                             .reset_index(drop=True)
    )

    # Print
    print(unique_regions)
    print(f"There are {unique_regions.size} regions.")

    #Other Solutions, it's worse, but it's ok
    unique_regions2:   pd.Series    = (entries.loc[:, ["Region", "H index"]]
                                            .groupby(["Region"])
                                            .count()
                                            .rename(columns={"H index":"Veces"})
                                            .reset_index()
                                            .assign(mon=lambda df: df.index + 1)
                                            .set_index("mon")
    )
    print(unique_regions2)

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q9()
# -----------------------------------------------------------------------------
