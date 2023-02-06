
'''Entrez: Easy access to the NCBI API through BioPython.
   9.3 ESearch: Searching the Entrez databases.
'''

from pathlib import Path

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement

import utils


# Entrez Global Config
Entrez.email = ""
assert Entrez.email != "", "Write your email address before using Entrez."



# Search an NCBI database
# If xml_filename exists, it won't make the request to the NCBI.
# ---------------------------------------------------------------------
def request_search(db: str, term: str, retmax: int, xml_filename: str):

    if Path(xml_filename).exists(): return

    with Entrez.esearch( db=db,
                         term=term,
                         retmax=retmax ) as response:

        xml_bytes: bytes = response.read()

    utils.write_xml(xml_bytes, xml_filename)



# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    request_search(db='pubmed',
                   term='biopython[title]',
                   retmax=40,
                   xml_filename='cache/pubmed-search.xml' )

    content: DictionaryElement = utils.read_xml('cache/pubmed-search.xml')

    utils.print_in_color(utils.get_pretty_str(content))

# ---------------------------------------------------------------------
