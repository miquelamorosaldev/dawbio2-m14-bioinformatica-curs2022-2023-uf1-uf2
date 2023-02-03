import re

# Put a text (txt param) and the regular expression (reg param) 
# and you will obtain the number of matches and all subtexts 
# that matches the regexp in the text.
def regex_validator(txt: str, reg: str):
    pat: re.Pattern = re.compile(reg)
    matches: list[re.Match] = list(pat.finditer(txt))
    print("txt     =       ", txt)
    print("reg     =       ", reg)
    print("num matches ? = ",len(matches))
    print("txt matches ? = ",pat.findall(txt))
    print("-------------------------------------------")

# Substitute regex with another value.
def sub_example(text: str, reg: str, subtxt: str):
    pat: re.Pattern = re.compile(reg)
    print("txt     =       ", text)
    print("reg     =       ", reg)
    # repl=replacement.
    # new_txt: str = pat.sub(repl='Buenaas!!!', txt=text)
    # new_txt: str = pat.sub('Buenaas!!!', text)
    new_txt: str = pat.sub(subtxt, text)
    print("txt matches ? = ",new_txt)
    print("-------------------------------------------")


def exemple1():
     # Al fer regexp sempre s'ha de definir 4 variables
    # d'aquesta forma no ens equivocarem.
    txt: str = 'Hola\nAdiós'
    # Aquesta r significa raw (crudo)
    # Cal posar-la per a què funcionin els caràcters
    # especials amb barra: \n \t \d 
    # reg: str    =r'\n'
    reg: str    =r'(\w+)\n(\w+)'
    # El mètode per a fer match a Pyhton és compile
    # i passar-lo a un objecte Pattern.
    pat: re.Pattern = re.compile(reg)
    # L'objecte pat és una llista de coincidències
    # que podem iterar.
    match_list: list[re.Match] = list(pat.finditer(txt))
    match: re.Match = match_list[0]

    print("txt  =   ", txt)
    print("reg  =   ", reg)
    print(f"Start:    {match.start()}")
    print(f"End:    {match.end()}")
    print(f"Whole match:    {match.group()[0]}")
    print(f"Group 1:    {match.group()[1]}")
    print(f"Group 2:    {match.group()[2]}")
    print("-------------------------------------------")


# Another way to validate regexps.
def exemple2022():
    txt: str    ="Hola a todossssss"
    reg: str    =r"s{2,}"
    pat: re.Pattern = re.compile(reg)
    matches: list[re.Match] = list(pat.finditer(txt))
    print("txt     =       ", txt)
    print("reg     =       ", reg)
    print("num matches ? = ",len(matches))
    print("txt matches ? = ",pat.findall(txt))
    print("-------------------------------------------")


## -------------- MAIN --------------------------- 
print("Regex demo. 2023.")
print("-------------------------------------------")
exemple1()
#exemple2022()
#regex_validator("GATAGATAG",r"GATA")
regex_validator("GATAGATAG",r"(GATA)\1")
sub_example(r'Hola\nAdiós\nHola2\nAdios2')