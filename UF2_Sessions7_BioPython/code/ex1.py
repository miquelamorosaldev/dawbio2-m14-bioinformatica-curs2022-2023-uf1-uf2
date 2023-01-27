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
# - Biopython Exercises
# #############################################################################

# -----------------------------------------------------------------------------
def q1():

    # 1. Read the .genbank file and write it as a .fasta file
    sars_cov_2_record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')
    SeqIO.write(sars_cov_2_record, EXAMPLE_FASTA, 'fasta')

    # 2. Show how many annotations, features are in the genbank file
    pp( {key:len(value) for key,value in explore(sars_cov_2_record).items()} )
    print()

# -----------------------------------------------------------------------------
def q2():

    # 1. Show what information you have in the first part of the genbank
    sars_cov_2_record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Keys in the annotations section
    pp(sars_cov_2_record.annotations.keys())

    # Show all annotations
    pp(sars_cov_2_record.annotations)

    # Show main reference
    print(sars_cov_2_record.annotations['references'][0])

# -----------------------------------------------------------------------------
def q3():

    # 1. Show what information you have in the second part of the genbank
    sars_cov_2_record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Show how many features are in the genbank file
    print(f"Number of features: {len(sars_cov_2_record.features)}")

    # Show type and location of each feature
    feature_info_list: list[SeqFeature] = [ (feature.type, str(feature.location))
                                            for feature
                                            in sars_cov_2_record.features ]

    pp(feature_info_list, width=200)


# -----------------------------------------------------------------------------
def q4():

    # 1. Get the last CDS, translate it manually and compare it to the genbank translation
    sars_cov_2_record: SeqRecord = SeqIO.read(SARS_COV_2_GENBANK, 'genbank')

    # Get list of CDS features
    cds_list: list[SeqFeature] = [  feature
                                    for feature
                                    in sars_cov_2_record.features
                                    if feature.type == 'CDS']

    # Get last cds
    cds_feature: SeqFeature = cds_list[-1]

    # Explore the CDS SeqFeature
    # pp(explore(cds_feature))

    # Get start and end
    cds_start: int = int(cds_feature.location.start)
    cds_end:   int = int(cds_feature.location.end)

    # Get my translation
    cds_seq = sars_cov_2_record.seq[cds_start:cds_end]
    my_translation: Seq = cds_seq.translate()

    # Get genbank translation
    genbank_translation: Seq = Seq(cds_feature.qualifiers['translation'][0])

    # Checks
    print(my_translation)
    print(genbank_translation)

    # Genbank translation with stop
    genbank_translation_with_stop: Seq = genbank_translation + '*'

    # Same translation?
    same_translation = (my_translation == genbank_translation_with_stop)
    print(f"Same translation? {same_translation}")


# -----------------------------------------------------------------------------
def main():

    q1()
    q2()
    q3()
    q4()


# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
