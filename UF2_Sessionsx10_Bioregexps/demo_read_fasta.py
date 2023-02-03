import re
from pathlib import Path

"""
Read fasta files without using BioPython.
"""

# -----------------------------------------------------------------------------
def read_fasta_v1(filename: str) -> str:
    """Reads a .fasta file with a single sequence.
       Uses a regexp with a single match.
       Removes whitespace using string .replace()"""

    # Regex setup  
    
    # txt, read fasta file.  
    txt: str = Path(filename).read_text()
    # reg, regexp.
    reg: str = r'(>[^\n]{1,})(.{0,})'
    # flag re.DOTALL -> el punt coincideix amb salts de línia
    pat: re.Pattern = re.compile(reg, re.DOTALL)

    # Get matches
    match_list: list[re.Match] = list(pat.finditer(txt))

    # If there is a sequence, there is a match
    assert len(match_list) == 1
    match: re.Match = match_list[0]
    lines: str      = match.group(2)

    # Remove newlines
    seq: str = lines.replace('\n', '')

    return seq

# Main
# -----------------------------------------------------------------------------
# print(read_fasta_v1('coronavirus2.fasta'))
print(read_fasta_v1('test1.fasta'))