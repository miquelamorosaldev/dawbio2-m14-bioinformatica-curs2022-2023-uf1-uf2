import re
from pathlib import Path


# #############################################################################
# Python Regexps: 
# 
# - [Standard Library](https://docs.python.org/3/library/re.html)
# - [Official Tutorial](https://docs.python.org/3/howto/regex.html)
# 
# #############################################################################


# -----------------------------------------------------------------------------
def finditer_example():

    txt: str        = 'Hola\nAdiós\nHola2\nAdiós2'
    reg: str        = r'(\w+)\n(\w+)'
    pat: re.Pattern = re.compile(reg)

    match_list: list[re.Match] = list(pat.finditer(txt))

    # match: re.Match = match_list[1]

    for match in match_list:
        print(f"Start:        {match.start()}")
        print(f"End:          {match.end()}")
        print(f"Whole match:  {match.group(0)}")
        print(f"First group:  {match.group(1)}")
        print(f"Second group: {match.group(2)}")
        print("--------------")



# -----------------------------------------------------------------------------
def sub_example():

    txt: str        = 'Hola\nAdiós\nHola2\nAdiós2'
    reg: str        = r'Hola'
    pat: re.Pattern = re.compile(reg)

    new_txt: str    = pat.sub('Buenasss!!!', txt)
    print(new_txt)


# -----------------------------------------------------------------------------
def main():

    finditer_example()
    sub_example()


# Main
# -----------------------------------------------------------------------------
this_module = __name__
main_module = '__main__'

if (this_module == main_module): main()
# -----------------------------------------------------------------------------
