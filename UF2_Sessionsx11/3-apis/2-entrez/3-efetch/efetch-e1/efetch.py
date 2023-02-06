
'''Entrez: Easy access to the NCBI API through BioPython.
   9.6 EFetch: Downloading full records from Entrez.
'''

import utils

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    utils.request_fetch(  db='nucleotide',
                          id='EU490707',
                          file_format='gb',
                          filename='cache/chloroplast.gb' )

    record: SeqRecord = SeqIO.read('cache/chloroplast.gb', 'gb')

    print(record)

# ---------------------------------------------------------------------
