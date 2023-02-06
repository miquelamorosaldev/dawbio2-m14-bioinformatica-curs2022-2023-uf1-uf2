'''Entrez: Easy access to the NCBI API through BioPython.'''

import sys
import json
from pathlib     import Path
from http.client import HTTPResponse

from Bio               import Entrez
from Bio.Entrez.Parser import DictionaryElement, ListElement

import pygments
from   pygments.lexers.web             import JsonLexer
from   pygments.formatters.terminal256 import Terminal256Formatter


# Entrez Global Config
Entrez.email = ""
assert Entrez.email != "", "Write your email address before using Entrez."


# Get DB list v1
# - HTTPResponse's .read() always returns bytes.
# - It's your job to convert them to a utf-8 string using .decode('utf-8').
# - Make sure first that the server returns utf-8 (It's the usual nowadays).
# - Always call .close() on any file, connection, database, etc.
# - The content_xml line can be after the close() line. It does not need response.
# - We must parse the XML ourselves: https://realpython.com/python-xml-parser/
# - This is very similar to using the Requests library.
# ---------------------------------------------------------------------
def get_info_xml_v1() -> str:

    response:      HTTPResponse = Entrez.einfo()
    content_bytes: bytes        = response.read()
    content_xml:   str          = content_bytes.decode('utf-8')
    response.close()

    return content_xml


# Get DB list v2
# - The idiom 'with ... as ...' calls .close() automatically.
# - It's the preferred way to open files, connections, databases, etc.
# - The type of the 'response' variable must be written beforehand.
#   Can't be written in the 'with...' expression.
# - The content_xml line can be outside the 'with' block. It does not need response.
# ---------------------------------------------------------------------
def get_info_xml_v2() -> str:

    response: HTTPResponse

    with Entrez.einfo() as response:
        content_bytes: bytes = response.read()
        content_xml:   str   = content_bytes.decode('utf-8')

    return content_xml


# Write DB list to disk v1
# - In order to not overload the NCBI, we can write the response to disk once first.
# - Later, we can read it from disk as many times as we want, without accessing the NCBI.
# ---------------------------------------------------------------------
def write_info_xml_to_disk_v1():

    response: HTTPResponse

    with Entrez.einfo() as response:
        content_bytes: bytes = response.read()

    Path('dblist.xml').write_bytes(content_bytes)


# Write DB list to disk v2
# - A more general version than v1.
# - Accepts a filename.
# - Makes the parent dirs, if they don't exist.
# ---------------------------------------------------------------------
def write_info_xml_to_disk_v2(filename: str):

    response: HTTPResponse

    with Entrez.einfo() as response:
        content_bytes: bytes = response.read()

    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    Path(filename).write_bytes(content_bytes)


# Read DB list from disk v1
# - Read xml file from disk using old method open().
# - By default open() opens the file in text mode.
# ---------------------------------------------------------------------
def read_info_xml_from_disk_v1() -> str:

    with open('cache/dblist.xml', 'r') as xml_file:
        content_xml: str = xml_file.read()

    return content_xml


# Read DB list from disk v2
# - Read xml file from disk using Path's open() method.
# - By default Path's .open() method opens file in text mode.
# - Equivalent to v1, but accepts a filename argument.
# ---------------------------------------------------------------------
def read_info_xml_from_disk_v2(filename: str) -> str:

    with Path(filename).open() as xml_file:
        content_xml: str = xml_file.read()

    return content_xml


# Read DB list as a dict v1.
# - BioPython's Entrez module can parse the XML for us.
# - Entrez.read() can parse any object that 
#   - Supports .read() (files, connections, etc.)
#   - Returns bytes (not utf-8 strings!)
# - Entrez.read() returns an object made of lists and dicts.
#   - The objects are ListElement and DictionaryElement.
#   - Those are not standard dicts and lists, but Entrez subclasses.
#   - They have all standard list and dict methods.
#   - You can print them using the json.dumps().
# - As usual, Entrez has .read() and .parse() methods.
#   - Use .read() when you expect a single dict as a response.
#   - Use .parse() when you expect a list of dicts as a response.
#     (Cannot use .parse() with the examples in this file)
# ---------------------------------------------------------------------
def get_info_dict_v1() -> str:

    response: HTTPResponse

    with Entrez.einfo() as response:
        content_dict: DictionaryElement = Entrez.read(response)

    return content_dict


# Read DB list as a dict v2.
# - Same as v1, but read the xml from disk.
# - Entrez expects an object with a .read() method that returns bytes.
# - We must open the file in binary mode with 'rb' (Read Binary).
# ---------------------------------------------------------------------
def get_info_dict_v2(filename: str) -> str:

    with Path(filename).open('rb') as xml_file:
        content_dict: DictionaryElement = Entrez.read(xml_file)

    return content_dict


# Prettify v1
# - Entrez's DictionaryElement and ListElement do not print well, even with pprint.
# - For printing in the terminal, better use json.dumps().
# ---------------------------------------------------------------------
def prettify(something) -> str:

    pretty_str: str = json.dumps(something,
                                 sort_keys=True,
                                 indent=4)

    return pretty_str


# Prettify v2
# - Same as v1, but adding colors to be displayed in the terminal.
# - Pygments adds escape sequences to the pretty string.
# - This function prints it directly to the terminal.
# - List of all supported styles:  print(list(pygments.styles.get_all_styles()))
# - Interesting styles: default, solarized-dark, solarized-light, zenburn
# ---------------------------------------------------------------------
def print_pretty(something, style: str):

    pretty_str: str = json.dumps(something,
                                 sort_keys=True,
                                 indent=4)

    lexer     = JsonLexer()
    formatter = Terminal256Formatter(style=style)

    colored_str: str = pygments.highlight( pretty_str,
                                           lexer=lexer,
                                           formatter=formatter )

    print(colored_str)


# Main
# ---------------------------------------------------------------------
this_module: str = __name__
main_module: str = "__main__"

if this_module == main_module:

    # write_info_xml_to_disk_v2('cache/dblist.xml')
    content = get_info_dict_v2('cache/dblist.xml')

    style: str = 'default'
    print_pretty(content, style)

# ---------------------------------------------------------------------
