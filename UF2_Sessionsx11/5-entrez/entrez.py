# Biopython Tutorial: "Chapter 9  Accessing NCBI’s Entrez databases"
# ---------------------------------------------------------------------
# Url: http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc111


# - Entrez = The old name of the NCBI Search Engine.
#   The old link now redirects to the current search page.
#   Old link:     http://www.ncbi.nlm.nih.gov/Entrez/
#   Current link: https://www.ncbi.nlm.nih.gov/search/
#   Entrez help:  https://www.ncbi.nlm.nih.gov/books/NBK3837/

# - ETools = Web API for accessing NCBI's online databases. (PubMed, GenBank, GEO, etc.)
# - Biopython has a module to use this API comfortably at Bio.Entrez.
#   You can find it in https://biopython.org/DIST/docs/api/

# - Usage levels:
#   IMPORTANT: **Be sensible in your usage levels**
#   All the functions that send requests to the NCBI Entrez API
#   will automatically respect the NCBI rate limit:
#   - 3 requests per second without an API key.
#   - 10 requests per second with an API key.
#   In case of network failure, 
#   - Biopython does a maximum of three tries before giving up.
#   - Sleeps for 15 seconds between tries.
#   You can tweak these params with:
#  - Bio.Entrez.max_tries
#  - Bio.Entrez.sleep_between_tries

# - There are 8 tools, and Bio.Entrez has functions for each.
#   1. Entrez.einfo
#   2. Entrez.esearch
#   3. Entrez.epost
#   4. Entrez.esummary
#   5. Entrez.efetch
#   6. Entrez.elink
#   7. Entrez.egquery
#   8. Entrez.espell
# - This document covers: einfo, esearch, epost, efetch.

# - Handles:
#   - All functions make extensive use of handles.
#     - They handle the http requests and responses.
#     - Their type is _io.TextIOWrapper.
#   - They must all be closed to free the resource with handle.close(), like files.
#     You can use standard Python idioms => with open(...) as xxx:
#   - https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python

# - XML:
#   - Some Entrez responses come in XML, JSON and text.
#     - Check the API for retmode='xml', retmode='json', retmode='text'
#     - Entrez.parse() does not support json. You must use python's parser.
#   - Entrez has functions to parse the XML automatically:
#     - Entrez.read(): Requests all the records (one or more) in one go.
#       You need enough memory (RAM + swap) in your pc.
#     - Entrez.parse(): Requests the records one by one. It's a generator.
#       Only useful with multiple records (not a big single record).
#       Can use a 'for' or next(handle) to advance.


# Preliminaries
# ---------------------------------------------------------------------

# Imports
import json
from   pprint   import pp
from   pathlib  import Path
from   Bio      import Entrez

# Before using any function, fill in your REAL e-mail
Entrez.email = "xxx@yyy.zzz"

# Path constants
CACHE_DIR = Path('/bio/data/entrez-cache')


# 9.2 EInfo + writing to disk
# ---------------------------------------------------------------------
def einfo():

    # EInfo: Get the list of Entrez databases in XML format (manual way)
    handle = Entrez.einfo()
    res = handle.read()
    handle.close()


    # Handles are _io.TextIOWrapper, exactly like files.
    print(type(handle))
    file_handle = open("entrez.py", "r")
    print(type(file_handle))
    file_handle.close()


    # EInfo: Get the list of Entrez databases in XML format (automatic way)
    with Entrez.einfo() as response:
        dbs_xml_bin_str = response.read()
    print(dbs_xml_bin_str)


    # EInfo: Get the list of Entrez databases in a dictionary 
    with Entrez.einfo() as response:
        dbs_dict = Entrez.read(response)

    print(dbs_dict)
    print(dbs_dict.keys())    # Only one key: DbList
    print(dbs_dict['DbList']) # Array of strings


    # The XML or JSON formats can be stored to a file in disk for later processing:
    # JSON:
    with Entrez.einfo(retmode='json') as response:
        dbs_json_str = response.read().decode("utf-8") 

    with open(CACHE_DIR/'dbs.json', 'w') as json_file:
        json_file.write(dbs_json_str)

    with open(CACHE_DIR/'dbs.json', 'r') as json_file:
        dbs_dict_from_json = json.load(json_file)


    # XML:
    with Entrez.einfo(retmode='xml') as response:
        dbs_xml_bin_str = response.read()

    with open(CACHE_DIR/'dbs.xml', 'wb') as xml_file:
        xml_file.write(dbs_xml_bin_str)

    with open(CACHE_DIR/'dbs.xml', 'rb') as xml_file:
        dbs_dict_from_xml = Entrez.read(xml_file)


    # Not exactly the same structure!
    print(dbs_dict_from_json == dbs_dict_from_xml)
    print(dbs_dict_from_json['einforesult']['dblist'])
    print(dbs_dict_from_xml['DbList'])

    # But have the same results
    print(dbs_dict_from_json['einforesult']['dblist'] == dbs_dict_from_xml['DbList'])



    # Parameters of einfo:
    # - https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EInfo
    # - db="database_name"
    # - retmode="xml" or retmode="json"
    # - Beware: There are dicts and lists!
    # - Biopython types inherit from std ones: type(nuc_db['DbInfo']['LinkList'])

    with Entrez.einfo(db="nucleotide") as response:
        nuc_db_xml_str = response.read()
        with open(CACHE_DIR/'nuc_db.xml', 'wb') as xml_file:
            xml_file.write(nuc_db_xml_str)

    with open(CACHE_DIR/'nuc_db.xml', 'rb') as xml_file:
        nuc_db = Entrez.read(xml_file)


    # Detailed info
    print(type(nuc_db))
    print(len(nuc_db))
    print(nuc_db.keys())
    print(nuc_db['DbInfo'].keys())
    print(nuc_db['DbInfo']['Description'])
    print(nuc_db['DbInfo']['Count'])
    print(nuc_db['DbInfo']['LastUpdate'])

    # Pretty printing
    print(nuc_db['DbInfo']['FieldList'])
    print(nuc_db['DbInfo']['FieldList'][0])

    for field in nuc_db['DbInfo']['FieldList']:
        pp(field, indent=4)
        print()

    # Compare with the web search: https://www.ncbi.nlm.nih.gov/



# 9.3 ESearch
# ---------------------------------------------------------------------
def esearch():

    # Searches any database. Returns IDs only!
    # The API has a link to the params page:
    # https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch

    # Opuntia = Cactus; accD = gene
    # idtype="acc": Accession number. By default it uses GI, but they are obsolete identifiers.
    with Entrez.esearch(db="nucleotide",
                        term="opuntia[ORGN] accD",
                        idtype="acc",
                        retmax=10) as response:
        res = Entrez.read(response)

    # Examining the results
    # RetStart: The first index of the results
    print(type(res))
    print(res.keys())
    pp(res, indent=4)

    # The results are all strings!!
    print(int(res["Count"]) >= 2)

    # Accession numbers to use with EFetch
    print(res["IdList"])


    # Compare with the web search: https://www.ncbi.nlm.nih.gov/
    # Database: "Nucleotide", search query: "Opuntia"[Organism] AND accD[All Fields]

    # Bigger example: Anything about Opuntia
    # Count and RetMax are different
    # Retmax is 20 by default.
    with Entrez.esearch(db="nucleotide", term="opuntia[ORGN]", idtype="acc") as response:
        res = Entrez.read(response)

    pp(res, indent=4)
    print(int(res["Count"]))
    print(len(res["IdList"]))
    print(int(res["RetMax"]))


    # Return ONLY the count (nothing else) with rettype="count".
    with Entrez.esearch(db="nucleotide", term="opuntia[ORGN]", rettype="count") as response:
        count_res = Entrez.read(response)
    pp(count_res, indent=4)


    # esearch() has a special parameter: usehistory="y"
    # This returns a webenv and a query_key in the response, like epost().
    # Section "9.16.1  Searching for and downloading sequences using the history".
    # But we'll use epost(), as it is more explicit and flexible.



# 9.4 EPost   and   9.6 EFetch
# ---------------------------------------------------------------------
def epost_and_efetch():

    # - Allows to upload a list of identifiers.
    # - Useful when there are > 200 UIDs.
    # - Useful for using with EFetch.

    # Get Accession numbers
    with Entrez.esearch(db="nucleotide",
                    term="opuntia[ORGN] accD",
                    idtype="acc",
                    retmax=10) as response:
        res = Entrez.read(response)

    # The XML response after posting the identifiers
    with Entrez.epost("nucleotide", id=",".join(res["IdList"])) as response:
        epost_xml_str = response.read()
    print(epost_xml_str)

    # The WebEnv and QueryKey we need for EFetch:
    with Entrez.epost("nucleotide", id=",".join(res["IdList"])) as response:
        epost = Entrez.read(response)

    pp(epost, indent=4)
    query_key = epost['QueryKey']
    webenv    = epost['WebEnv']


    # EFetch()
    # - The query must be less than 200 UIDs.
    # - For longer queries, use a webenv and a query_key.
    # - https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch
    # - Notes:
    #   - If only one id, no need for commas in the string.
    #   - Genbank type is "gb", NOT "genbank"!!
    #   - Use retstart and retmax to download in batches (recommended).
    #   - Entrez does not read nor parse text files. Use SeqIO for that.

    # Fetching by ID directly (less than 200 UIDs):
    id_list = res["IdList"][:3]
    ids_str  = ",".join(id_list)
    with Entrez.efetch( db="nucleotide",
                        retmode="text", rettype="fasta",
                        idtype="acc", id=ids_str) as response:
        fasta_txt = response.read()

    print(fasta_txt)
    with open(CACHE_DIR/'opuntia.fasta', 'w') as fasta_file:
        fasta_file.write(fasta_txt)


    # Fetching by webenv and a query_key (more than 200 UIDs):
    with Entrez.efetch( db="nucleotide",
                        retmode="text", rettype="gb",
                        retstart=0, retmax=3,
                        webenv=webenv, query_key=query_key,
                        idtype="acc") as response:
        gb_txt = response.read()

    print(gb_txt)
    with open(CACHE_DIR/'opuntia.gb', 'w') as gb_file:
        gb_file.write(gb_txt)



# 9.10 ESummary
# ---------------------------------------------------------------------
def esummary():

    # Entrez.parse allows to parse big responses record by record.
    # Consumes less RAM (only one record).
    # Do not close the handle before processing all records!
    # WRONG:
    # with Entrez.esummary(db="pubmed", id="19304878,14630660", retmode="xml") as response:
    #     recs_iter = Entrez.parse(response)
    # for rec in recs_iter:
    #     print(rec['Title'])
    # RIGHT:
    with Entrez.esummary(db="pubmed", id="19304878,14630660", retmode="xml") as response:
        recs_iter = Entrez.parse(response)
        for rec in recs_iter:
            print(rec['Title'])



# Other examples: Homologene
# https://www.biostars.org/p/345510/
# ---------------------------------------------------------------------
def other():

    with Entrez.esearch(db="homologene", term="Homo sapiens HBB", idtype="acc") as response: 
        res = Entrez.read(response) 

    res_str = ",".join(res['IdList']) 

    with Entrez.efetch( db="homologene",
                        retmode="text", rettype="fasta",
                        idtype="acc", id=res_str) as response:
        fasta_txt = response.read()

    with open(CACHE_DIR/"hbb.fasta", "w") as fasta_file:
        fasta_file.write(fasta_txt)


# -----------------------------------------------------------------------------
def main():

    einfo()
    esearch()
    epost_and_efetch()
    esummary()
    other()


# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
