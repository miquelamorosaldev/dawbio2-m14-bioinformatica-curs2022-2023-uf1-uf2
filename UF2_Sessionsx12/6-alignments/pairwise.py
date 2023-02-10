
"""
BioPython Tutorial: 6.6.2 PairwiseAligner
"""

from Bio            import SeqIO
from Bio.Seq        import Seq
from Bio.SeqRecord  import SeqRecord
from Bio.SeqFeature import SeqFeature
from Bio.Align      import PairwiseAligner, PairwiseAlignments, PairwiseAlignment, substitution_matrices

from Bio.Align.substitution_matrices import Array

# Aligner object
# ---------------------------------------------------------------------
def check_aligner_parameters():

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Print its parameters.
    print(aligner)

    # The algorithm is chosen automatically depending on the mode and gap scores. It's read-only.
    print(f"Algorithm: {aligner.algorithm}")


# Global alignment. It's the default.
# ---------------------------------------------------------------------
def align_globally(seq1: Seq, seq2: Seq):

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Get score only
    score: float = aligner.score(seq1, seq2)
    print(f"Global alignment score: {score}")

    # Get global alignments. Global is the default.
    alignments: PairwiseAlignments = aligner.align(seq1, seq2)

    # Alignments looks like an iterator, but it is not.
    # We can ask the length and has some extra methods. See dir().
    print(f"Number of alignments: {len(alignments)}")

    # Each alignment is a PairwiseAlignment object. It has additional methods.
    alignment: PairwiseAlignment
    for alignment in alignments:
        print(alignment)


# Local alignment. Score and number of alignments differ from global alignment.
# ---------------------------------------------------------------------
def align_locally(seq1: Seq, seq2: Seq):

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()
    aligner.mode = 'local'

    # Get score only
    score: float = aligner.score(seq1, seq2)
    print(f"Local alignment score: {score}")

    # Get global alignments. Global is the default.
    alignments: PairwiseAlignments = aligner.align(seq1, seq2)

    # Alignments looks like an iterator, but it is not.
    print(f"Number of alignments: {len(alignments)}")

    # Each alignment is a PairwiseAlignment object. It has additional methods.
    alignment: PairwiseAlignment
    for alignment in alignments:
        print(alignment)


# Aligner parameters
# ---------------------------------------------------------------------
def change_aligner_parameters():

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Print its default parameters.
    print(aligner)

    # Calculate alignment score
    score: float = aligner.score("ACGT","ACAT")
    print(f"Score with default parameters: {score}")
    
    # We can change the parameters
    aligner.match_score = 1.0
    aligner.mismatch_score = -2.0
    print(aligner)

    # Calculate alignment score
    score: float = aligner.score("ACGT","ACAT")
    print(f"Score with changed parameters: {score}")
    
    # gap_score changes automatically all gap scores!
    aligner.gap_score = -2.5
    print(aligner)


# Substitution Matrix (BLOSUM62, etc.) for aligning proteins.
# BLAST uses BLOSUM62 in blastp.
# ---------------------------------------------------------------------
def use_substitution_matrix():

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Print available matrices.
    print(substitution_matrices.load())

    # Get one of the matrices
    blosum62_matrix: Array = substitution_matrices.load('BLOSUM62')
    print(blosum62_matrix)

    # Put the matrix in the aligner.
    # This invalidates the match, mismatch and gap scores.
    aligner.substitution_matrix = blosum62_matrix

    # Align using the matrix
    score: float = aligner.score("ACDQ","ACDQ")
    print(f"Score with BLOSUM62 matrix: {score}")


# ---------------------------------------------------------------------
def inspect_global_alignment():

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Seqs
    seq1: Seq = 'GAACT'
    seq2: Seq = 'GAT'

    # Get global alignments.
    alignments: PairwiseAlignments = aligner.align(seq1, seq2)

    # Get first alignment
    alignment: PairwiseAlignment = alignments[0]

    # Alignment attributes
    print(f"Score: {alignment.score}")
    print(f"Target seq: {alignment.target}")
    print(f"Query seq:  {alignment.query}")
    print(f"Num of aligned seqs:  {len(alignment)}")
    print()

    # Print alignment
    print(alignment)

    # Shape
    print(f"Alignment shape:       {alignment.shape}")
    print(f"Num of aligned seqs:    {alignment.shape[0]}")
    print(f"Num of aligned letters: {alignment.shape[1]}")
    print()

    # Aligned
    print(f"Aligned attribute:      {alignment.aligned}")
    print(f"Matched indexes in target seq:  {alignment.aligned[0]}")
    print(f"Matched indexes in query seq:   {alignment.aligned[1]}")

# ---------------------------------------------------------------------
def inspect_local_alignment():

    # Create Aligner
    aligner: PairwiseAligner = PairwiseAligner()
    aligner.mode = 'local'

    # Seqs
    seq1: Seq = 'TGAACT'
    seq2: Seq = 'GAC'

    # Get global alignments.
    alignments: PairwiseAlignments = aligner.align(seq1, seq2)

    # Get first alignment
    alignment: PairwiseAlignment = alignments[0]

    # Alignment attributes
    print(f"Score: {alignment.score}")
    print(f"Target seq: {alignment.target}")
    print(f"Query seq:  {alignment.query}")
    print(f"Num of aligned seqs:  {len(alignment)}")
    print()

    # Print alignment
    print(alignment)

    # Shape
    print(f"Alignment shape:       {alignment.shape}")
    print(f"Num of aligned seqs:    {alignment.shape[0]}")
    print(f"Num of aligned letters: {alignment.shape[1]}")
    print()

    # Aligned
    print(f"Aligned attribute:      {alignment.aligned}")
    print(f"Matched indexes in target seq:  {alignment.aligned[0]}")
    print(f"Matched indexes in query seq:   {alignment.aligned[1]}")


# Coronavirus ARN sequence is TOO LONG. Always choose some small gene!
# Always try to align proteins!
# Traverse alignments one by one, not all at the same time!
# ---------------------------------------------------------------------
def align_coronavirus():

    # Read sequences
    record_list: list[SeqRecord] = list(SeqIO.parse('cov2.gb', 'gb'))
    seq_list:    list[Seq]       = [ record.seq for record in record_list ]

    # Get SeqRecords
    r1: SeqRecord = record_list[0]
    r2: SeqRecord = record_list[1]

    # Get CDS
    r1_cds_feature:    SeqFeature = r1.features[2]
    r1_cds_feature_tr: str        = r1_cds_feature.qualifiers['translation'][0]

    r2_cds_feature:    SeqFeature = r2.features[2]
    r2_cds_feature_tr: str        = r2_cds_feature.qualifiers['translation'][0]

    # Create Global Aligner
    aligner: PairwiseAligner = PairwiseAligner()

    # Get BLOSUM62 matrix
    blosum62_matrix: Array = substitution_matrices.load('BLOSUM62')

    # Put the matrix in the aligner.
    aligner.substitution_matrix = blosum62_matrix
    
    # Get first global alignment
    alignments: PairwiseAlignments = aligner.align(r1_cds_feature_tr, r2_cds_feature_tr)
    alignment = alignments[0]

    # Print it, its score, etc.
    print(alignment)
    print(f"Score: {alignment.score}")

    print(f"Matched indexes in target seq:  {alignment.aligned[0]}")
    print(f"Matched indexes in query seq:   {alignment.aligned[1]}")



# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    check_aligner_parameters()
    align_globally('GAACT',   'GAT')
    align_locally( 'AGAACTC', 'GAACT')
    change_aligner_parameters()
    use_substitution_matrix()
    inspect_global_alignment()
    inspect_local_alignment()
    align_coronavirus()

# ---------------------------------------------------------------------
