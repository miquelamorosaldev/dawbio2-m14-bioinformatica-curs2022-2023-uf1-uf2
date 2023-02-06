import re
from   pathlib import Path



# #############################################################################
# Read a file with a fasta file with a single seq. Very simple code.
# #############################################################################

# -----------------------------------------------------------------------------
def read_single_fasta_file(filename: str):

    txt: str        = Path(filename).read_text()
    reg: str        = r'.{0,}'
    pat: re.Pattern = re.compile(reg)

    match_list: list[re.Match] = list(pat.finditer(txt))

    # Remove header
    match_list.pop(0)

    # Get list of all lines
    line_list: list[str] = [match.group(0)
                            for match
                            in match_list]

    # Sequence
    seq: str = ''.join(line_list)
    return seq



# #############################################################################
# Read a file with a fasta file with a multiple seqs. Robust code.
# #############################################################################

# -----------------------------------------------------------------------------
def remove_whitespace(txt: str) -> str:
    """Removes whitespace everywhere using a regex."""

    # Regex setup
    reg: str = r'\s'
    pat: re.Pattern = re.compile(reg)

    # Remove whitespaces
    result: str = pat.sub('', txt)

    return result


# -----------------------------------------------------------------------------
def parse_fasta(fasta: str) -> str:
    """Reads a .fasta string with a single sequence.
       Uses a regexp with a single match.
       Removes whitespace using another regex."""

    # Regex setup
    reg: str = r'(>[^\n]{1,})(.{0,})'
    pat: re.Pattern = re.compile(reg, re.DOTALL)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(fasta))

    # If there is a sequence, there is a match
    assert len(match_list) == 1
    match: re.Match = match_list[0]
    lines: str      = match.group(2)

    # Remove newlines
    seq: str = remove_whitespace(lines)

    return seq


# -----------------------------------------------------------------------------
def split_multi_fasta(txt: str) -> list[str]:
    """Input: A multifasta text. Can be single fasta, too."""

    # Regex setup
    reg: str = r'>[^>]{0,}'
    pat: re.Pattern = re.compile(reg)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(txt))

    # Return list of matches (fastas) as strings
    fasta_list: list[str] = [match.group(0) for match in match_list]

    return fasta_list


# -----------------------------------------------------------------------------
def read_fasta_file(filename: str) -> list[str]:
    """Input: A filename of a fasta file.
       It can be multifasta or single fasta."""

    txt:        str       = Path(filename).read_text()
    fasta_list: list[str] = split_multi_fasta(txt)
    seq_list:   list[str] = [parse_fasta(fasta)
                             for fasta
                             in fasta_list]

    return seq_list



# -----------------------------------------------------------------------------
def main():

    print(read_single_fasta_file('/bio/data/regex-1.fasta'))
    print(read_fasta_file('/bio/data/regex-2.fasta'))


# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
