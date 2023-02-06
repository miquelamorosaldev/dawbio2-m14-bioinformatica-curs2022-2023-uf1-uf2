
'''Entrez: Easy access to the NCBI API through BioPython.
   9.6 EFetch: Downloading full records from Entrez.
   9.16 Using the history and WebEnv.
'''

import utils

from Bio               import SeqIO
from Bio.SeqRecord     import SeqRecord

from Bio.Entrez.Parser import DictionaryElement, ListElement
from Bio.SeqIO.InsdcIO import GenBankIterator


# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    utils.request_search( db           = 'nucleotide',
                          term         = 'coronavirus',
                          retmax       = 3,
                          xml_filename = 'cache/cov2-search.xml' )

    search_content:      DictionaryElement = utils.read_xml('cache/cov2-search.xml')
    coronavirus_id_list: list              = list(search_content['IdList'])

    utils.request_multi_fetch(  db          = 'nucleotide',
                                id_list     = coronavirus_id_list,
                                batch_size  = 3,
                                file_format = 'gb',
                                filename    = 'cache/cov2.gb' )

    # Use iterators for big files (only one traversal) or list if it fits in RAM.
    record_iter: GenBankIterator = SeqIO.parse('cache/cov2.gb', 'gb')
    record_list: list[SeqRecord] = list(record_iter)

    for record in record_list:
        print(record)
        print()

# ---------------------------------------------------------------------
