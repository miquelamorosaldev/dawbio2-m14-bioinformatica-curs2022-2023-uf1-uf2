# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def q1():
    
    entries: list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    num:     int        = len(entries)
    
    print("First entry:")
    pprint.pp(entries[0])

    print(f"There are {num} entries.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q1()
# -----------------------------------------------------------------------------