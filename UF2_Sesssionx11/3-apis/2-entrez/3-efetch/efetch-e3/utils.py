'''Utils to be used along BioPython's Entrez.'''

import json

from pathlib import Path
from typing  import Union

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement

import pygments
from   pygments.lexers.web             import JsonLexer
from   pygments.formatters.terminal256 import Terminal256Formatter


# Entrez Global Config
# ---------------------------------------------------------------------
Entrez.email = "mabardajiprofe@gmail.com"
assert Entrez.email != "", "Write your email address before using Entrez."
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# NCBI Functions
# ---------------------------------------------------------------------
# Functions won't make the request if xml_filename exists.


# ---------------------------------------------------------------------
def request_db_info(db: str, xml_filename: str):

    if Path(xml_filename).exists(): return

    with Entrez.einfo(db=db) as response:
        xml_bytes: bytes = response.read()

    write_xml(xml_bytes, xml_filename)


# ---------------------------------------------------------------------
def request_search(db: str, term: str, retmax: int, xml_filename: str):

    if Path(xml_filename).exists(): return

    with Entrez.esearch( db     = db,
                         term   = term,
                         retmax = retmax,
                         idtype = "acc"  ) as response:

        xml_bytes: bytes = response.read()

    write_xml(xml_bytes, xml_filename)


# ---------------------------------------------------------------------
def request_fetch(  db:          str,
                    id:          Union[str, list[str], set[str]],
                    file_format: str,
                    filename:    str  ):
    """ This function writes plain text in the type you specify.
        Typical types: 'fasta', 'gb', etc.
        SHOULD BE USED TO DOWNLOAD ONLY ONE OR A FEW FILES.
    """

    if Path(filename).exists(): return

    with Entrez.efetch( db      = db,
                        id      = id,
                        rettype = file_format,
                        retmode = "text",
                        idtype  = "acc"        ) as response:

        content: str = response.read()

    write_text(content, filename)


# ---------------------------------------------------------------------
def _request_batch( db:          str,
                    webenv:      str,
                    query_key:   str,
                    start:       int,
                    batch_size:  int,
                    file_format: str,
                    filename:    str  ):
    """ Internal function used by request_multi_fetch().
        Do not call it directly.
        This function writes plain text in the type you specify.
        Typical types: 'fasta', 'gb', etc. 
        Should be used to download only a few files.
    """

    with Entrez.efetch( db        = db,
                        webenv    = webenv,
                        query_key = query_key,
                        idtype    = "acc",
                        retstart  = start,
                        retmax    = batch_size,
                        rettype   = file_format,
                        retmode   = "text"       ) as response:

        content: str = response.read()

    with Path(filename).open('a') as output_file:
        output_file.write(content)


# ---------------------------------------------------------------------
def request_multi_fetch( db:           str,
                         id_list:      Union[list[str], set[str]],
                         batch_size:   int,
                         file_format:  str,
                         filename:     str                        ):
    """ Downloads files in batches from NCBI.
        Use it to download large quantities of files or very big files.
        Adjust batch_size to something reasonable.
        id_list must be a list or a set. A single id string won't work!
    """

    if Path(filename).exists(): return


    # Post IDs
    id_list_str: str = ','.join(id_list)

    with Entrez.epost(  db=db,
                        id=id_list_str ) as response:
        
        post_id: DictionaryElement = Entrez.read(response)
        webenv:                str = post_id['WebEnv']
        query_key:             str = post_id['QueryKey']


    # Retrieve contents
    start: int = 0
    stop:  int = len(id_list)
    step:  int = batch_size  

    start_list: list[int] = list(range(start, stop, step))

    for start in start_list:
        _request_batch( db          = db,
                        webenv      = webenv,
                        query_key   = query_key,
                        start       = start,
                        batch_size  = batch_size,
                        file_format = file_format,
                        filename    = filename    )



# ---------------------------------------------------------------------
# File Functions
# ---------------------------------------------------------------------
# These functions are meant to be used with Entrez's responses.
# Writing functions behave as follows:
# - Make the parent dirs, if they don't exist.
# - Overwrite existing files.


# Write a string of text to a disk file. Read it later using SeqIO.
# ---------------------------------------------------------------------
def write_text(txt: str, filename: str):

    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    Path(filename).write_text(txt)


# Write xml as a bytes string to a disk file.
# ---------------------------------------------------------------------
def write_xml(xml_bytes: bytes, filename: str):

    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    Path(filename).write_bytes(xml_bytes)


# Read xml from a file in disk.
# ---------------------------------------------------------------------
def read_xml(xml_filename: str) -> Union[DictionaryElement, ListElement]:

    with Path(xml_filename).open('rb') as xml_file:
        content = Entrez.read(xml_file)

    return content



# ---------------------------------------------------------------------
# Pretty Printing Functions
# ---------------------------------------------------------------------


# Prettifies an object and returns its pretty representation as a string.
# It expects a json-able object.
# ---------------------------------------------------------------------
def get_pretty_str(something) -> str:

    pretty_str: str = json.dumps(something,
                                 sort_keys=True,
                                 indent=4)

    return pretty_str


# Print in color
# - Adds colors and prints directly to the terminal.
# By default it expects a Json, but you can provide another lexer.
# - Available lexers: https://pygments.org/docs/lexers/
# It will use the 'default' theme, but you can choose a different one:
# - List of all supported styles:  print(list(pygments.styles.get_all_styles()))
# - Interesting styles: default, solarized-dark, solarized-light, zenburn
# ---------------------------------------------------------------------
def print_in_color(text: str, lexer = JsonLexer(), style: str = 'default'):

    formatter = Terminal256Formatter(style=style)

    colored_str: str = pygments.highlight( text,
                                           lexer=lexer,
                                           formatter=formatter )

    print(colored_str)

# ---------------------------------------------------------------------

