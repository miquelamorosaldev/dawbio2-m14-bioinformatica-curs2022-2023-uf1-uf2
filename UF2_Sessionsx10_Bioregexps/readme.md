# Sessió 10 - Aplicació Expressions regulars amb Biopython (2022-02-03)

Hem resolt les expressions del regexplay que quedaven:

[Sessió 9, juguem amb regexs](../UF2_Sessions9_RegexpGames/readme.md)

## Com posar les expressions regulars a Python ? 

Pàgina oficial llibreria de regex Pyhton **re**

https://docs.python.org/3/library/re.html

És molt llarga, i bona part del que hem fet ja ho hem resumit a les anteriors sessions.

Per tant, proposem una sintaxi general per aplicar exp. regulars a Python per tots els casos.

```python
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
```

</hr>

## Exemples de la sessió d'avui.

### Primers exemples.

[demo_regexps.py](./demo_regexps.py)

### Primer exemple lectura .fasta.
 
[demo_read_fasta.py](./demo_read_fasta.py)

[test1.fasta](./test1.fasta)

</hr>

## Utilitats regexp amb Python.

1. Parseig de fitxers fasta, CSV i parts concretes de genbank.
2. Info de pàgines que no sigui HTML (pex abstracts, imatges)
3. Secuenciar l'ADN.


### Altres tècniques: WebScrapping. 

#### Webscrapping: Serveix per agafar informació online que no et facilita descarregar (per exemple taules HTML)

   2.1. Pandas. Ideal per agafar taules HTML

   2.2. BeautifulSoup. Ideal per agafar taules HTML

Cal vigilar, ja que si la web té (C) Copyright podem infringir drets d'autor.

</hr>


