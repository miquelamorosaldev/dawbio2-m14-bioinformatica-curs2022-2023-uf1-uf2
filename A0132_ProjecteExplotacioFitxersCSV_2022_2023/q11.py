# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q11. Convert entries from list[dict] to dict[str, list] (one list for each key)
# -----------------------------------------------------------------------------


# Convert the list of dicts to a dict of lists (DataFrame-like format)
# -----------------------------------------------------------------------------
def convert_format_v1(entries: list[dict]) -> dict[str,list]:
    
    # Get list of keys. All dicts have the same keys
    entry: dict           = entries[0]
    keys:  list[str]      = list(entry.keys())

    # Empty result. df = DataFrame.
    df: dict[str,list] = {}

    # Get all values for each key
    for key in keys:
        df[key] = [entry[key] for entry in entries]

    return df

# Same as v1, but using a lambda. Slightly shorter and clearer.
# -----------------------------------------------------------------------------
def convert_format_v2(entries: list[dict]) -> dict[str,list]:
    
    # Get list of entry keys. All dicts have the same keys.
    first_entry: dict  = entries[0]
    keys: list[str]    = list(first_entry.keys())
    
    # Get all values for each key
    get_all_values     = lambda key, entries: [entry[key] for entry in entries]
    df: dict[str,list] = {key: get_all_values(key, entries) for key in keys}

    return df

# -----------------------------------------------------------------------------
def q11():

    raw_entries: list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    df:          dict[list] = convert_format_v2(raw_entries)

    print("List of keys:")
    pprint.pp(list(df.keys()))

    print("List of top ten Journals:")
    pprint.pp(df["Title"][0:10])

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q11()
# -----------------------------------------------------------------------------
