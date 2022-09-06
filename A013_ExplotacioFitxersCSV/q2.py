# Imports
import utils

# -----------------------------------------------------------------------------
# Q2. What types of scientific publications are in the file?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def get_unique_types(entries):

    unique_types_set:  set[str]  = {entry['Type'] for entry in entries}
    unique_types_list: list[str] = sorted(unique_types_set)

    return unique_types_list

# -----------------------------------------------------------------------------
def q2():
    
    entries: list[dict] = utils.read_csv_file("scimago-medicine.csv")

    unique_types_list: list[str] = get_unique_types(entries)
    num:               int       = len(unique_types_list)
    unique_types_str:  str       = ", ".join(unique_types_list)

    print(f"There are {num} different types of publications: {unique_types_str}")

# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q2()
# -----------------------------------------------------------------------------
