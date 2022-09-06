# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q9. All regions covered by all entries
# -----------------------------------------------------------------------------

# This was too easy...

# -----------------------------------------------------------------------------
def q9():
    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # Get list of regions
    region_set:  set[str]  = {entry["Region"] for entry in clean_entries}
    region_list: list[str] = sorted(region_set)

    # Print
    pprint.pp(region_list)

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q9()
# -----------------------------------------------------------------------------
