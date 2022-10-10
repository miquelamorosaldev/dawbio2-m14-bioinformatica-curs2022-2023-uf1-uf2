# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q4. What is the oldest publisher that is still active?
#     (Has some publication in 2021)
# -----------------------------------------------------------------------------

# Useful URLs
# - https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
# - https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
# - https://stackoverflow.com/questions/21415661/logical-operators-for-boolean-indexing-in-pandas


# v1. String hack. Easy version.
# -----------------------------------------------------------------------------
def q4_v1():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Get first and last years
    coverage:   pd.Series = entries.loc[:, 'Coverage']
    first_year: pd.Series = coverage.str[0:4].astype(int)
    last_year:  pd.Series = coverage.str[-4:].astype(int)

    # Filter
    current_year:       int       = 2021
    still_active_mask:  pd.Series = (last_year == current_year)

    earliest_year:      int       = first_year[still_active_mask].min()
    earliest_year_mask: pd.Series = (first_year == earliest_year)

    oldest_active_mask: pd.Series = still_active_mask & earliest_year_mask

    # Show result
    print("Oldest publisher that is still active:")
    print(entries.loc[oldest_active_mask, ["Rank", "Sourceid", "Title", "Publisher", "Coverage"]])


# v2. Expanding the coverage. Harder, more flexible version.
# -----------------------------------------------------------------------------
def q4_v2():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Get all expanded coverages
    coverages: pd.DataFrame = utils.get_coverages(entries)

    # Group. 'Rank' will become the index.
    grouped_coverages = coverages.groupby(by='Rank')

    # Get first and last years. Reset index to merge later with entries.
    first_year: pd.Series = (grouped_coverages.min()
                                             .reset_index(drop=True)
                                             .rename(columns={'Coverage': 'First Year'})
                                              .loc[:, 'First Year']
    )
    print('*****************')
    print(first_year)
    last_year: pd.Series = (grouped_coverages.max()
                                             .reset_index(drop=True)
                                             .rename(columns={'Coverage': 'Last Year'})
                                             .loc[:, 'Last Year']
    )

    # Filter
    current_year:       int       = 2021
    still_active_mask:  pd.Series = (last_year == current_year)

    earliest_year:      int       = first_year[still_active_mask].min()
    earliest_year_mask: pd.Series = (first_year == earliest_year)

    oldest_active_mask: pd.Series = still_active_mask & earliest_year_mask

    # Show result
    print("Oldest publisher that is still active:")
    print(entries.loc[oldest_active_mask, ["Rank", "Sourceid", "Title", "Region", "Publisher"]])


# Additional question: Find longest running journals
# -----------------------------------------------------------------------------
def print_longest_running_top10() -> None:

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file('scimago-medicine.csv')

    # Get all expanded coverages
    coverages: pd.DataFrame = utils.get_coverages(entries)

    # Group. 'Rank' will become the index.
    grouped_coverages = coverages.groupby(by='Rank')

    # Longest running journals
    longest_running_top10: pd.DataFrame = (grouped_coverages.count()
                                                            .reset_index()
                                                            .rename(columns={'Coverage': 'Running Years'})
                                                            .sort_values(by='Running Years', ascending=False)
                                                            .head(10)
    )

    # Merge back to get the whole entries
    longest_running_top10_entries: pd.DataFrame = pd.merge(longest_running_top10, entries, on='Rank')

    # Print
    print("Longest running top 10 entries:")
    print(longest_running_top10_entries)
    longest_running_top10_entries.to_html("scimago-longest-running-top10.html")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    #q4_v1()
    #print_longest_running_top10()
    q4_v2()
# -----------------------------------------------------------------------------
