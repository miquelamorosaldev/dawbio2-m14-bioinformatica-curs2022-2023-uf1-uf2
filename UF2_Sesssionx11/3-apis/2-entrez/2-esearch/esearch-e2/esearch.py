
'''Entrez: Easy access to the NCBI API through BioPython.
   9.3 ESearch: Searching the Entrez databases.
'''

import utils

from Bio.Entrez.Parser import DictionaryElement, ListElement


# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    utils.request_search( db='pubmed',
                          term='biopython[title]',
                          retmax=40,
                          xml_filename='cache/pubmed-search.xml' )

    content: DictionaryElement = utils.read_xml('cache/pubmed-search.xml')

    utils.print_in_color(utils.get_pretty_str(content))

# ---------------------------------------------------------------------
