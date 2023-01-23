from Bio                import SeqIO            # SeqIO is a module
from Bio.SeqIO.FastaIO  import FastaIterator    # FastaIterator is a class
from Bio.Seq            import Seq              # Seq is a class
from Bio.SeqRecord      import SeqRecord        # SeqRecord is a class
from Bio.SeqFeature     import SeqFeature, FeatureLocation

from pathlib import Path
## Pretty Print
from pprint  import pp
from utils   import explore


# Constants
DATA_DIR = Path('/bio/2023-01-23-code/3-seqrecord/data')

SARS_COV_2_FASTA    = DATA_DIR/'sars-cov-2.fasta'
SARS_COV_2_GENBANK  = DATA_DIR/'sars-cov-2.genbank'

CANNABIS_FASTA    = DATA_DIR/'cannabis.fasta'
CANNABIS_GENBANK  = DATA_DIR/'cannabis.genbank'


# Biopython Chapter 4: SeqRecords
# SeqRecords are similar to Genbank files.
# Genbank files have three parts:
# 1. Context:     From LOCUS until FEATURES.
# 2. Annotations: From FEATURES until ORIGIN.
# 3. Sequence:    From ORIGIN until the end of file or the next LOCUS.
# -----------------------------------------------------------------------------
def chapter_4_cannabis_genbank():

    # Read Sars-Cov-2 genbank
    #record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Read Cannabis genbank
    # Source:
    # https://www.ncbi.nlm.nih.gov/nuccore/JAATIP010000026.1?report=fasta
    record_cannabis: SeqRecord = SeqIO.read(CANNABIS_GENBANK, 'genbank')

###Mostrar quantes features y annotations hi ha.
###Quina longitud tiene la secuencia ?

    # Keys in Annotations section 
    print('==>SeqRecord: types of attributes:')
    pp(record_cannabis.annotations.keys())

    print("Num Annotations = ")
    print(len(record_cannabis.annotations.keys()))

    # Secuence length.
    print("==>Secuence length ")
    pp(len(record_cannabis.seq))

    # Compare sequence with fasta.
    print("==>FASTA description and length ")
    fasta_cannabis: SeqRecord = SeqIO.read(CANNABIS_FASTA, 'fasta')
    print(fasta_cannabis.description)
    pp(len(fasta_cannabis.seq))

    # Main reference
    print("==>Main reference ")
    print(record_cannabis.annotations['references'][0])


def chapter_4_cannabis_genbank_part2():

    record_cannabis: SeqRecord = SeqIO.read(CANNABIS_GENBANK, 'genbank')
    # Show how many features are in genbank.
    print("==>Number of features")
    #print(f'Number of features:' len(fasta_cannabis.features))
    print(len(record_cannabis.features))
    print("==>Show first feature")
    print(record_cannabis.features[0])


    ## Mostrem el tipus i la location.
    print("==>Show first 10 features type and location")
    for pos in range(0, 10):
        print("Info feature ",pos,",type",str(record_cannabis.features[pos].type))
        print(record_cannabis.features[pos].location)

    ## Mostrem el tipus i la location.
    features_list : list = record_cannabis.features

    ## *expression* for *item* in *iterable*
    # using the list comprehension method
    # [print(x) for x in countries]
    print("==>Show All locations")
    [pp(str(feature.location)) for feature in record_cannabis.features]

    # Las posiciones están explicadas en 4.3.2.3 Fuzzy Positions
    # - ExactPosition
    # - BeforePosition
    # - AfterPosition
    # - WithinPosition
    # - OneOfPosition
    # - UnknownPosition

    ## Comparar la traducción del CDS con la cadena del ADN traducida por ByoPython.

    ## Primer provarem la última cadena del sars-cov-2 que és la més fàcil.
    ## MGYINVFAFPFTIYSLLLCRMNSRNYIAQVDVVNFNLT

    record_sars_cov_2: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')
    print("==>Show Last Feature CDS")
    sars_cov_2_ft : list = record_sars_cov_2.features

    ## El last CDS es troba a aquesta posició.
    last_cds = sars_cov_2_ft[len(sars_cov_2_ft)-5]
    print(last_cds)
    adn_locations = last_cds.location
    print(adn_locations)
    adn_genbank_translation = last_cds.qualifiers['translation']
    print(adn_genbank_translation)

    print("==>Show FASTA last characters")
    fasta_sars_cov_2: SeqRecord = SeqIO.read(SARS_COV_2_FASTA, 'fasta')

    print("==>TRANSLATE FASTA ADN")
    # Convert to Seq object
    fasta_sars_cov_2_SEQ = Seq(fasta_sars_cov_2.seq[29557:29674])
    print(fasta_sars_cov_2_SEQ)
    fasta_sars_cov_2_translated = fasta_sars_cov_2_SEQ.translate()

    print("==>TRANSLATED ADN FASTA WITH BYOPYTHON")
    print(fasta_sars_cov_2_translated)
    print("==>GENBANK TRANSLATION")
    print(str(adn_genbank_translation[0]))
# -----------------------------------------------------------------------------
def main():

    chapter_4_cannabis_genbank()
    chapter_4_cannabis_genbank_part2()

# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
