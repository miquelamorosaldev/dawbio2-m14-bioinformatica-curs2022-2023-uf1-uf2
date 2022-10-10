# Imports
import utils

import pandas as pd

# -----------------------------------------------------------------------------
# Q13. Are entry titles unique?
#      Are ranks unique?
#      What columns can be used as a primary key?
# -----------------------------------------------------------------------------


# Using .unique(). Long method.
# -----------------------------------------------------------------------------
def are_titles_unique_v1():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Are titles unique?
    all_titles:     pd.Series = entries.loc[:, 'Title']
    unique_titles:  pd.Series = entries.loc[:, 'Title'].drop_duplicates()

    all_titles_size:    int = len(all_titles)
    unique_titles_size: int = len(unique_titles)

    are_all_titles_unique: bool = (all_titles_size == unique_titles_size)

    print(f"Are titles unique identifiers? {are_all_titles_unique}.")
    print(f"Number of titles: {all_titles_size}")
    print(f"Number of unique titles: {unique_titles_size}")


    # Show repeated titles
    title_appearances:    pd.Series = entries.groupby(by='Title').size()
    repeated_titles_mask: pd.Series = (title_appearances > 1)
    repeated_titles_num:  pd.Series = title_appearances[repeated_titles_mask]
    repeated_titles:      pd.Index  = repeated_titles_num.index
    print(repeated_titles_num)


    # Write entries to disk
    repeated_entries_mask: pd.Series    = entries.loc[:, 'Title'].isin(repeated_titles)
    repeated_entries     : pd.DataFrame = entries.loc[repeated_entries_mask, :]
    repeated_entries.to_html("scimago-repeated-entries.html")
    print("Look at scimago-repeated-entries.html")


# Using .nunique(). Very similar to v1.
# -----------------------------------------------------------------------------
def are_titles_unique_v2():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Are titles unique?
    all_titles_size:    int = len(entries.loc[:, 'Title'])
    unique_titles_size: int = entries.loc[:, 'Title'].nunique()

    # The rest is the same as v1...


# Using .duplicated(). Much shorter.
# -----------------------------------------------------------------------------
def are_titles_unique_v3():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Are titles unique?
    repeated_titles_mask:  pd.Series = entries.loc[:, 'Title'].duplicated(keep=False)
    are_all_titles_unique: bool      = not repeated_titles_mask.any()
    print(f"Are titles unique identifiers? {are_all_titles_unique}.")

    # Write entries to disk
    repeated_entries: pd.DataFrame = entries.loc[repeated_titles_mask, :]
    repeated_entries.to_html("scimago-repeated-entries.html")
    print("Look at scimago-repeated-entries.html")

    # Show repeated titles
    print(repeated_entries.groupby(by='Title').size())
    print()


# Using .unique(). Verbose method.
# -----------------------------------------------------------------------------
def are_ranks_unique_v1():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Are Ranks unique?
    all_ranks:     pd.Series = entries.loc[:, 'Rank']
    unique_ranks:  pd.Series = entries.loc[:, 'Rank'].unique()

    all_ranks_size:    int = len(all_ranks)
    unique_ranks_size: int = len(unique_ranks)

    are_all_ranks_unique: bool = (all_ranks_size == unique_ranks_size)

    print(f"Are ranks unique identifiers? {are_all_ranks_unique}.")
    print(f"Number of ranks: {all_ranks_size}")
    print(f"Number of unique ranks: {unique_ranks_size}")


# Using duplicated(). Short method
# -----------------------------------------------------------------------------
def are_ranks_unique_v2():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Show result
    print("Are ranks unique identifiers?")
    print(not entries.loc[:, 'Rank'].duplicated(keep=False).any())
    print()


# What columns can be used as unique idientifiers? (primary keys)
# -----------------------------------------------------------------------------
def find_primary_keys():

    # Read entries (7125 entries)
    entries: pd.DataFrame = utils.read_csv_file("scimago-medicine.csv")

    # Show result
    print("What columns are primary keys?")
    print(entries.apply(lambda column: not column.duplicated().any()))


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    are_titles_unique_v3()
    are_ranks_unique_v2()
    find_primary_keys()
# -----------------------------------------------------------------------------
