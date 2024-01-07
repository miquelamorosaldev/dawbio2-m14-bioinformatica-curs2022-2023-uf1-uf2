from Bio                import SeqIO            # SeqIO is a module
from Bio.SeqIO.FastaIO  import FastaIterator    # FastaIterator is a class
from Bio.Seq            import Seq              # Seq is a class
from Bio.SeqRecord      import SeqRecord        # SeqRecord is a class
from Bio.SeqFeature     import SeqFeature, FeatureLocation

from pathlib import Path
from pprint  import pp
from utils   import explore


# Constants
DATA_DIR = Path('/bio/data')

EXAMPLE_FASTA       = DATA_DIR/'example.fasta'
EXAMPLE_GENBANK     = DATA_DIR/'example.genbank'

ORCHID_FASTA        = DATA_DIR/'orchid-list.fasta'
ORCHID_GENBANK      = DATA_DIR/'orchid-list.genbank'

SARS_COV_2_FASTA    = DATA_DIR/'sars-cov-2.fasta'
SARS_COV_2_GENBANK  = DATA_DIR/'sars-cov-2.genbank'



# #############################################################################
# - Biopython Tutorial and Cookbook
# - https://biopython.org/DIST/docs/tutorial/Tutorial.html
# 
# - Chapter 3 Seqs
# - Chapter 5 I/O
# - Chapter 4 SeqRecords
# 
# #############################################################################


# Biopython Chapter 3: Seqs
# - [Codon tables](https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables)
# - [IUPAC codes](https://www.bioinformatics.org/sms/iupac.html)
# -----------------------------------------------------------------------------
def chapter_3_seq():

    # Methionine Example
    atg_seq: Seq = Seq("ATG")
    aug_seq: Seq = atg_seq.transcribe()
    met_seq: Seq = aug_seq.translate()

    translation_text = f'''
    transcribe() + translate():    {atg_seq} -> {aug_seq} -> {met_seq}
    translate() directly from DNA: {atg_seq} -> {atg_seq.translate()}
    Biological databases store sequences in DNA, not RNA.
    '''

    useful_methods_text = f'''
    complement():  { atg_seq.complement()         }
    concatenation: { Seq("GATA") + Seq("GATA")    }
    reverse (1):   { Seq(''.join(list(reversed("GATAGATA")))) }
    reverse (2):   { Seq("GATAGATA"[::-1])        }
    base numbers:  { list(enumerate(Seq("GATA"))) }
    slices:        { Seq("GATAGATA")[2:6]         }
    seq to str     { str(Seq("GATAGATA"))         }
    Seq objects are immutable. MutableSeq objects can mutate.
    '''

    print(translation_text)
    print(useful_methods_text)


# Biopython Chapter 5: Input/Output
# - Input/Output is done using SeqRecords:
#   - SeqRecords resemble .genbank files.
#     See SARS-CoV-2 genbank file on NCBI: https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
#   - Genbanks and SeqRecords can have many optional fields. See Biopython Chapter 4 later.
#     All SeqRecords have at least a .seq attribute storing a Seq object.
# - SeqIO.read():
#   - Reads files with only ONE datum (sequence, record, etc.)
#   - Returns a SeqRecord object, even when reading fasta files.
# - SeqIO.parse():
#   - Reads files with multiple data (sequence, record, etc.)
#   - Returns an Iterator of SeqRecord objects.
#   - Iterators allow us to process big files, but can traverse them only once.
#   - If you have enough RAM, it's easier to convert to lists. Easier to debug and manipulate.
# -----------------------------------------------------------------------------
def chapter_5_io():

    # Example of a SeqRecord. Inspect them with our own explore() function
    print('SeqRecord of SARS-CoV-2 from fasta file:')
    record: SeqRecord = SeqIO.read(SARS_COV_2_FASTA, 'fasta')
    pp(explore(record))
    print()

    # Use SeqIO.read() to read a fasta or genbank file with only one sequence/record
    record: SeqRecord = SeqIO.read(SARS_COV_2_FASTA, 'fasta')
    record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Use SeqIO.parse() to read multi-fasta or multi-genbank files
    record_list: list[SeqRecord] = list(SeqIO.parse(ORCHID_FASTA, 'fasta'))
    record_list: list[SeqRecord] = list(SeqIO.parse(ORCHID_GENBANK, 'genbank'))

    # When not enough RAM, use iterators to read one SeqRecord at a time (memory-efficient)
    record_iterator: FastaIterator = SeqIO.parse(ORCHID_FASTA, 'fasta')

    # Iterators can be traversed only once.
    # All SeqRecords have at least the .seq attribute (Seq object)
    print('Lengths of all orchids:')
    for record in record_iterator:
        print( len(record.seq), end=', ' )

    # Fasta files cointain much less information than genbanks
    fasta_record:   SeqRecord = SeqIO.read(SARS_COV_2_FASTA,   'fasta')
    genbank_record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    print(); print()

    print('SeqRecord from fasta file:')
    pp( {key:len(value) for key,value in explore(fasta_record).items()} )

    print()

    print('SeqRecord from genbank file:')
    pp( {key:len(value) for key,value in explore(genbank_record).items()} )

    print()

    # We can create SeqRecords, modify them and write them to disk.
    # Minimum requirements:
    # 1. seq must be of class Seq
    # 2. annotations must have a key 'molecule_type'
    seq:         Seq        = Seq('GATAGATA')
    annotations: dict       = { 'molecule_type' : 'DNA' }
    record:      SeqRecord  = SeqRecord( seq = seq,
                                         id  = '12345',
                                         description = 'GATA seq',
                                         annotations = annotations )

    # Inspect Python objects with our own explore() function
    print('SeqRecord to be written to disk:')
    pp(explore(record))
    print()

    # SeqRecords can be written to .fasta or .genbank files
    SeqIO.write(record, EXAMPLE_FASTA, 'fasta')
    SeqIO.write(record, EXAMPLE_GENBANK, 'genbank')


# Biopython Chapter 4: SeqRecords
# SeqRecords are similar to Genbank files.
# Genbank files have three parts:
# 1. Annotations:     From LOCUS until FEATURES. Also called Header or Context.
# 2. Features:        From FEATURES until ORIGIN.
# 3. Sequence:        From ORIGIN until the end of file or the next LOCUS.
# -----------------------------------------------------------------------------
def chapter_4_seq_record():

    # Read Sars-Cov-2 genbank
    record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Show types of SeqRecord attributes
    pp( {key:type(value) for key,value in explore(record).items()} )

    # SeqRecord main attributes and their types
    record.annotations        # dict        (Context: Genbank 1st part)
    record.description        # str         (...)
    record.dbxrefs            # list[str]   (In genbanks it's in the Context)
    record.id                 # str
    record.name               # str
    record.seq                # Bio.Seq.Seq (Sequence: Genbank 3rd part)
    record.letter_annotations # dict
    record.features           # list[SeqFeature]

    # A SeqFeature is an annotation inside the FEATURES section of genbank files.
    source_feature: SeqFeature = record.features[0]

    pp(explore(source_feature))
    source_feature.type       # str
    source_feature.id         # str
    source_feature.location   # FeatureLocation
    source_feature.strand     # int (hebra directa o indirecta)
    source_feature.ref        # str
    source_feature.ref_db     # str
    source_feature.qualifiers # dict[str, list[str]] => dict(source_feature.qualifiers)

    # Locations
    source_location: FeatureLocation = source_feature.location

    pp(explore(source_location))
    source_location.strand         # int. 1 = Hebra directa. -1 = Hebra indirecta
    source_location.start          # Position
    source_location.end            # Position
    source_location.nofuzzy_start  # Position (int)
    source_location.nofuzzy_end    # Position (int)
    source_location.parts          # Para joins
    source_location.ref            # str
    source_location.ref_db         # str

    # Las posiciones están explicadas en 4.3.2.3 Fuzzy Positions
    # - ExactPosition
    # - BeforePosition
    # - AfterPosition
    # - WithinPosition
    # - OneOfPosition
    # - UnknownPosition


# -----------------------------------------------------------------------------
def main():

    chapter_3_seq()
    chapter_5_io()
    chapter_4_seq_record()


# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
