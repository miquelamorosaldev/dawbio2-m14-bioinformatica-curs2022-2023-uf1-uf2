# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q5. Ranking of countries according to H index
# -----------------------------------------------------------------------------

# assign() is not necessary. set_index() can do it.
# assign() is very flexible, as it receives the whole dataframe in the lambda.
# -----------------------------------------------------------------------------
def q5():

    # Read entries
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Select columns, group, calculate mean
    country_means: pd.DataFrame = ( entries.loc[:, ["Country", "H index"]]
                                    .groupby("Country")
                                    .mean()
                                    .sort_values(by="H index", ascending=False)
    )

    # Add Ranking numbers
    country_ranking: pd.DataFrame = (country_means
                                    .reset_index() #drop index and country isn't index
                                    .assign(Ranking=lambda df: df.index + 1) #new Column Ranking df.index +1
                                    .set_index("Ranking") #new column is index
    )

    # Print result
    print(country_ranking.head(50))

    # Plot result
    country_means.head(40).plot(kind="bar").get_figure().savefig("s5.pdf")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q5()
# -----------------------------------------------------------------------------
