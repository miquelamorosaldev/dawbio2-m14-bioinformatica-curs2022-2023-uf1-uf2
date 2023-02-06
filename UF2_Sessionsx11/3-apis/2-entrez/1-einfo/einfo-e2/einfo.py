'''Entrez: Easy access to the NCBI API through BioPython.'''

from pathlib import Path

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement

import utils

# Entrez Global Config
Entrez.email = ""
assert Entrez.email != "", "Write your email address before using Entrez."



# Request DB info
# If xml_filename exists, it won't make the request to the NCBI.
# ---------------------------------------------------------------------
def request_db_info(db: str, xml_filename: str):

    if Path(xml_filename).exists(): return

    with Entrez.einfo(db=db) as response:
        xml_bytes: bytes = response.read()

    utils.write_xml(xml_bytes, xml_filename)


# Print Nucleotide number of parameters
# ---------------------------------------------------------------------
def print_nucleotide_num_fields():

    content:    DictionaryElement = utils.read_xml('cache/nucleotide.xml')
    field_list: ListElement       = content['DbInfo']['FieldList']
    num_fields: int               = len(field_list)

    print(f"Number of query parameters for the Nucleotide DB: {num_fields}")


# Print PubMed number of parameters
# ---------------------------------------------------------------------
def print_pubmed_num_fields():

    content:    DictionaryElement = utils.read_xml('cache/pubmed.xml')
    field_list: ListElement       = content['DbInfo']['FieldList']
    num_fields: int               = len(field_list)

    print(f"Number of query parameters for the PubMed DB: {num_fields}")


# Print PubMed query parameters v1
# ---------------------------------------------------------------------
def print_pubmed_query_parameters_v1():

    content:           DictionaryElement       = utils.read_xml('cache/pubmed.xml')
    field_list:        ListElement             = content['DbInfo']['FieldList']
    sorted_field_list: list[DictionaryElement] = sorted(field_list, key=lambda field: field['Name'])

    for field in sorted_field_list:

        name:        str = field['Name']
        full_name:   str = field['FullName']
        description: str = field['Description']

        print(f"{name}, {full_name}, {description}")


# Print PubMed query parameters v2.
# Alternative version. Dict with only 3 fields = Easier to debug.
# ---------------------------------------------------------------------
def print_pubmed_query_parameters_v2():

    content:    DictionaryElement = utils.read_xml('cache/pubmed.xml')
    field_list: ListElement       = content['DbInfo']['FieldList']

    slim_field_list = [ {'Name':        field['Name'],
                         'FullName':    field['FullName'],
                         'Description': field['Description'] }
                        for field in field_list ]

    sorted_field_list: list[dict] = sorted(slim_field_list, key=lambda field: field['Name'])

    for field in sorted_field_list:

        name:        str = field['Name']
        full_name:   str = field['FullName']
        description: str = field['Description']

        print(f"{name}, {full_name}, {description}")


# Print PubMed query parameters v2.
# Same as v2 but using a dict comprehension inside the list comprehension (!)
# ---------------------------------------------------------------------
def print_pubmed_query_parameters_v3():

    content:    DictionaryElement = utils.read_xml('cache/pubmed.xml')
    field_list: ListElement       = content['DbInfo']['FieldList']

    clean_field: function = lambda field: { key: value
                                            for key, value
                                            in field.items()
                                            if key in ['Name', 'FullName', 'Description'] }

    clean_field_list = [ clean_field(field) for field in field_list ]

    sorted_field_list: list[dict] = sorted(clean_field_list, key=lambda field: field['Name'])

    for field in sorted_field_list:

        name:        str = field['Name']
        full_name:   str = field['FullName']
        description: str = field['Description']

        print(f"{name}, {full_name}, {description}")


# Print PubMed Author parameter info
# ---------------------------------------------------------------------
def print_pubmed_author_parameter_info():

    content:    DictionaryElement = utils.read_xml('cache/pubmed.xml')
    field_list: ListElement       = content['DbInfo']['FieldList']

    filtered_field_list = [ field
                            for field in field_list
                            if field["Description"] == "Author Identifier" ]

    assert len(filtered_field_list) == 1
    author_field: DictionaryElement = filtered_field_list[0]

    utils.print_in_color(utils.get_pretty_str(author_field))



# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    request_db_info('',           'cache/dblist.xml')
    request_db_info('nucleotide', 'cache/nucleotide.xml')
    request_db_info('pubmed',     'cache/pubmed.xml')

    print_nucleotide_num_fields()
    print_pubmed_num_fields()
    print_pubmed_query_parameters_v3()
    print_pubmed_author_parameter_info()

# ---------------------------------------------------------------------
