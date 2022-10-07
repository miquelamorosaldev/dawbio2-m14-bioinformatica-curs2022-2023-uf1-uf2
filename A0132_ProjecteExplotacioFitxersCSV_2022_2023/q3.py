# Imports
import utils
import pprint

# -----------------------------------------------------------------------------
# Q3. How many types of journal has each publisher?
#     (Group publisher by number of types)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
def get_types(publisher: str, entries: list[dict]) -> list[str]:

    # Get all unique types, filtered by Publisher
    unique_types_set: set[str] = {entry['Type']
                                  for entry in entries
                                  if entry['Publisher'] == publisher}

    # Sorted unique types
    unique_types_list: list[str] = sorted(unique_types_set)

    return unique_types_list

# One of the publishers is ''. Should be deleted in a real report.
# -----------------------------------------------------------------------------
def q3():

    # Get clean entries
    raw_entries:   list[dict] = utils.read_csv_file("A0132_ProjecteExplotacioFitxersCSV_2022_2023/scimago-medicine.csv")
    clean_entries: list[dict] = utils.clean_entries(raw_entries)

    # List of unique publishers: 1904. One of them is '' (unknown)
    publishers_set:   set[str] = {entry['Publisher'] for entry in clean_entries}
    publishers_list: list[str] = sorted(publishers_set)

    # List of unique types of publisher
    types_of_publisher_list: list[list[str]] = [get_types(publisher, clean_entries)
                                                for publisher in publishers_list]

    # List of numtypes of publisher
    numtypes_of_publisher_list: list[int] = [len(types_list)
                                             for types_list in types_of_publisher_list]

    # Make dictionary: publisher -> number of types
    publisher_numtypes_dict: dict[str,int] = dict(zip(publishers_list,
                                                      numtypes_of_publisher_list))

    # Reverse dictionary
    numtypes_publishers_dict: dict[int,list[str]] = utils.reverse_dict(publisher_numtypes_dict)

    # Make dictionary: number of types -> number of publishers
    numtypes_numpublishers_dict: dict[int,int] = {  numtypes: len(publishers_list)
                                                    for numtypes, publishers_list
                                                    in numtypes_publishers_dict.items()}

    # Sort. Just for printing.
    numtypes_numpublishers_sorted_dict: dict[int,int] = \
                                        dict(sorted(numtypes_numpublishers_dict.items()))

    # Print
    pprint.pp(numtypes_numpublishers_sorted_dict)


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q3()
# -----------------------------------------------------------------------------
