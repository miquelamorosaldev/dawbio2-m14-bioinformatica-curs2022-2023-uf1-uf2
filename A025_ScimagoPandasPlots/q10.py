# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q10. Mean of H index by region
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def q10():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Select columns, group, calculate mean
    region_means: pd.DataFrame = (  entries.loc[:, ["Region", "H index"]]
                                    .groupby("Region")
                                    .mean()
                                    .sort_values(by="H index", ascending=False)
    )

    # Print result
    print(region_means)

    # Plot result
    region_means.plot(kind="bar").get_figure().savefig("s10.pdf")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q10()
# -----------------------------------------------------------------------------
