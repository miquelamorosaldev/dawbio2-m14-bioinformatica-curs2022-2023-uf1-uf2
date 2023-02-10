
'''Entrez: Easy access to the NCBI API through BioPython.
   9.6 EFetch: Downloading full records from Entrez.
'''

import utils

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Entrez.Parser import DictionaryElement, ListElement
from Bio.SeqIO.InsdcIO import GenBankIterator


# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    utils.request_search( db='nucleotide',
                          term='coronavirus',
                          retmax=3,
                          xml_filename='cache/nucleotide-coronavirus-search.xml' )

    search_content: DictionaryElement = utils.read_xml('cache/nucleotide-coronavirus-search.xml')
    # utils.print_in_color(utils.get_pretty_str(content))

    coronavirus_id_list: list = list(search_content['IdList'])
    # print(coronavirus_id_list)

    utils.request_fetch(  db='nucleotide',
                          id=coronavirus_id_list,
                          file_format='gb',
                          filename='cache/coronavirus.gb' )

    # Iterators are ideal for big files, but you can traverse them only once!
    record_iter: GenBankIterator = SeqIO.parse('cache/coronavirus.gb', 'gb')

    for record in record_iter:
        print(record)
        print()

    # Convert to list if they fit in RAM for ease of use and debugging.
    record_list: list[SeqRecord] = list(SeqIO.parse('cache/coronavirus.gb', 'gb'))

    for record in record_list:
        print(record)
        print()


# ---------------------------------------------------------------------
