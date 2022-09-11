# Imports
import utils
import pprint
import os

print(f"El nombre del modulo utils.py es ",(__name__))
# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------
# El nombre de un módulo es igual al nombre de un fichero
# Excepción cuand es el script principal que se llama __main__
# Mirando el nombre del mòdulo puedes saber si esto modulos son importados
# -----------------------------------------------------------------------------
def q1():


    entries: list[dict] = utils.read_csv_file("scimago-medicine.csv")
    num:     int        = len(entries)
    
    print("First entry:")
    pprint.pp(entries[0])

    print(f"There are {num} entries.")


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q1()
# -----------------------------------------------------------------------------
