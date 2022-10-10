# Imports
import pandas as pd
from   pandas.api.types import CategoricalDtype

# -----------------------------------------------------------------------------
# Read CSV File
# -----------------------------------------------------------------------------

# See 'open' docs to understand the newline parameter
# DictReader converts each row in csv_file in a dictionary.
# The dictionary keys are the column names.
# -----------------------------------------------------------------------------
def read_csv_file(csv_file_path: str) -> pd.DataFrame:
    
    entries: pd.DataFrame = pd.read_csv(csv_file_path, sep=";")
    return entries



# -----------------------------------------------------------------------------
# Clean entries
# -----------------------------------------------------------------------------
# - In raw Python we had to fix Categories, H-Index and NAs.
# - With Pandas we only need to fix Categories. H-Index and NAs are correct.


# replace() returns a new copy each time.
# Instead of replace() you can use a regexp.
# -----------------------------------------------------------------------------
def remove_quarter(category: str) -> str:
    "Returns the category string without the quarter id: (Q1), (Q2), (Q3) or (Q4)"

    result = (category.replace("(Q1)", "")
                      .replace("(Q2)", "")
                      .replace("(Q3)", "")
                      .replace("(Q4)", "")
    )

    return result


# -----------------------------------------------------------------------------
def get_clean_categories(categories_str: str) -> list[str]:
    "Returns a clean list of the categories in categories_str."

    # Split categories
    categories_list: list[str] = categories_str.split(';')

    # Remove quarter ids
    categories_merged_list: list[str] = [remove_quarter(category) for category in categories_list]

    # Trim whitespaces
    categories_clean_list: list[str] = [category.strip() for category in categories_merged_list]

    return categories_clean_list


# Sorting: .unique() is a numpy method. Use .drop_duplicates() to obtain a Series.
# Categories: .astype() can be used on a df and you can change some columns only.
# Pandas con calculate categories itself, but not the order. Did it manually to show.
# -----------------------------------------------------------------------------
def get_categories(entries: pd.DataFrame) -> pd.DataFrame:
    """Returns a DataFrame containing the expanded categories of the Scimago entries.
       The index is the default numerical index.
       Rank:     Journal rank. It is the primary key.
       Category: A fixed Category. A single category. The quarters are deleted.
                 It has Pandas 'category' type, and we order them alphabetically."""

    # Select only Rank and Coverage columns
    rank_category_df: pd.DataFrame       = entries.loc[:, ['Rank', 'Categories']]
    categories_list:  list[pd.DataFrame] = []

    # Expand all coverages into a list of dataframes
    for rank, categories_str in rank_category_df.itertuples(index=False):

        df: pd.DataFrame = pd.DataFrame({'Rank':     rank,
                                         'Category': get_clean_categories(categories_str)})
        categories_list.append(df)

    # Concatenate all dataframes. This is faster than doing it iteratively. Use default index.
    untyped_categories: pd.DataFrame = pd.concat(categories_list, ignore_index=True)

    # Remove duplicates, sort and reset index of series
    sorted_categories: pd.Series = (untyped_categories.loc[:, 'Category']
                                                      .drop_duplicates()
                                                      .sort_values()
                                                      .reset_index(drop=True)
    )

    # Create Category
    category_type: CategoricalDtype = CategoricalDtype(categories=sorted_categories, ordered=True)

    # Set type as Panda's category
    categories: pd.DataFrame = untyped_categories.astype({'Category': category_type})

    return categories



# -----------------------------------------------------------------------------
# Coverage functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def expand(register: str) -> list[int]:
    """Input:
        - A string with two possible formats:
          1. YYYY:      A single year with four digits.
          2. YYYY-YYYY: A range of years separated by a dash (start-end).
       Output:
        - A list of years, as integers.
        - If the input is a range, the list includes all years. End year is included."""

    result: list[int]

    is_range:       bool = ('-' in register)
    is_single_year: bool = not is_range

    if is_single_year:
        result = [int(register)]

    elif is_range:
        first_year: int = int(register[0:4])
        last_year:  int = int(register[-4:])
        result = list(range(first_year, last_year+1))

    return result


# -----------------------------------------------------------------------------
def get_years(coverage_str: str) -> list[int]:
    """Get the expanded list of years from a coverage string.
       A coverage string can contain multiple coverage registers."""

    # Split by commas. Strip whitespace. Store into a list of registers.
    register_list: list[str] = [register.strip() for register in coverage_str.split(',')]

    # Expand each register into its years
    year_nested_list:   list[list[int]] = [expand(register) for register in register_list]
    year_list:          list[int]       = flatten(year_nested_list)

    return year_list


# 'Rank' and 'Sourceid' could be both primary keys, but we use the rank for simplicity.
# - https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
# -----------------------------------------------------------------------------
def get_coverages(entries: pd.DataFrame) -> pd.DataFrame:
    """Returns a DataFrame containing the expanded coverages of the Scimago entries.
       The index is the default numerical index.
       Rank:     Journal rank. It is the primary key.
       Coverage: Covered year."""

    # Select only Rank and Coverage columns
    rank_coverage_df: pd.DataFrame       = entries.loc[:, ['Rank', 'Coverage']]
    coverages_list:   list[pd.DataFrame] = []

    # Expand all coverages into a list of dataframes
    for rank, coverage in rank_coverage_df.itertuples(index=False):

        df: pd.DataFrame = pd.DataFrame({'Rank':     rank,
                                         'Coverage': get_years(coverage)})
        coverages_list.append(df)

    # Concatenate all dataframes. This is faster than doing it iteratively.
    coverages: pd.DataFrame = pd.concat(coverages_list, ignore_index=True)

    return coverages


# -----------------------------------------------------------------------------
# Collection functions
# -----------------------------------------------------------------------------


# https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
# -----------------------------------------------------------------------------
def is_iterable(something) -> bool:
    """Returns True if the input is a collection. False otherwise.
       Strings are not considered collections."""

    result: bool

    try:
        iter(something)
    except TypeError:
        result = False
    else:
        result = True

    return result


# This is a more general alternative to itertools.chain.from_iterable():
# - https://docs.python.org/3/library/itertools.html
# Beware of recursion limit (1000):
# - https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
# -----------------------------------------------------------------------------
def flatten(something) -> list:
    """Can flatten any nested iterable. Does not flatten strings. Result is always a single list."""

    result: list = []

    has_iter:       bool = is_iterable(something)
    is_string:      bool = isinstance(something, str)
    is_collection:  bool = (has_iter and not is_string)

    if is_collection:
        for element in something:
            flattened_list: list = flatten(element)
            result.extend(flattened_list)
    else:
        result = [something]
    
    return result


# -----------------------------------------------------------------------------
