#  Exercici explotació fitxers CSV (2022 - 2023)
## <center>Pablo Garcia, Miquel Angel Amoros, Miquel Angel Bardají</center>

[Font de dades: Web Scimago ](https://www.scimagojr.com/journalrank.php?area=2700 "Web font de dades ")

> The SCImago Journal & Country Rank is a publicly available portal that includes the journals and country scientific indicators developed from the information contained in the Scopus® database. These indicators can be used to assess and analyze scientific domains. Journals can be compared or analysed separately. Country rankings may also be compared or analysed separately.


###  **Practica explotar un fitxer** i resoldre diferents consultes.

Fitxer de dades : [aqui](./scimago-medicine.csv "aqui")

#### Entries from SciMago

Per llegir un fitxer a python, utilitzarem una funció que li passarem la ruta i retornarà una llista amb totes les línies del fitxer.

```python
# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result
```

D'aquesta manera anomenem la funció que ens tornarà el contingut.



```python
# Import notebook
# How to import a notebook a file

import csv
csv_file_path = "scimago-medicine.csv"
entries = read_csv_file(csv_file_path)
entries[0]       
```

>    {'Rank': '1',
>    'Sourceid': '28773',
>    'Title': 'Ca-A Cancer Journal for Clinicians',
>    'Type': 'journal',
>    'Issn': '15424863, 00079235',
>    'SJR': '62,937',
>    'SJR Best Quartile': 'Q1',
>    ...
>    'Categories': 'Hematology (Q1); Oncology (Q1)'}


## Exercicis

**Es publicaran les solucions obtingudes al final de la sessió.**
També s'enviarà codi intermig per a donar-vos pistes durant la sessió a:
[https://etherpad.wikimedia.org/p/m14-uf1-uf2](Wiki Etherpad M14)


* [Ex1 - How many entries are in scimago-medicine.csv?](#ex1)
* [Ex2 - Show the first 25 entries.](#ex2)
* [Ex3 - Compta el número d'entrades publicades a Espanya en una llista (Country = Spain)](#ex3)
* [Ex4 - Mostra les revistes (Type = journal) publicades a UK (Country = United Kingdom) i que tinguin un H index superior a 200.](#ex4)
* [Ex5 - What types of scientific publications are in the file ?](#ex5)
* [Ex6 - List all the avaliable categories. Each entry can have more than one category.](#ex6)
* [Ex7 - Show all data from entries of categories: "Sports Medicine" or "Sports science"](#ex7)


# Read Entries from SciMago CSV file.

```python
# How to define a function in python with the word key
# the type date after the : is only documentation for Python
def read_csv_file(csv_file_path: str) -> list:
    
    with open(csv_file_path, newline='') as csvfile:
        csv_reader=csv.DictReader(csvfile, delimiter=";")
        result = [row_dict for row_dict in csv_reader]
        
    return result
```


```python
# Import notebook
# How to import a notebook a file

import csv
import re
csv_file_path = "scimago-medicine.csv"
entries = read_csv_file(csv_file_path)
# entries = entries[0:10] opció per a quedar-se sol amb els 10 primers , per poder fer proves.
entries[0]
```

```python
>    {'Rank': '1',
>     'Sourceid': '28773',
>     'Title': 'Ca-A Cancer Journal for Clinicians',
>     'Type': 'journal',
>     'Issn': '15424863, 00079235',
>     'SJR': '62,937',
>     'SJR Best Quartile': 'Q1',
>     'H index': '168',
>     'Total Docs. (2020)': '47',
>     'Total Docs. (3years)': '119',
>     'Total Refs.': '3452',
>     'Total Cites (3years)': '15499',
>     'Citable Docs. (3years)': '80',
>     'Cites / Doc. (2years)': '126,34',
>     'Ref. / Doc.': '73,45',
>     'Country': 'United States',
>     'Region': 'Northern America',
>     'Publisher': 'Wiley-Blackwell',
>     'Coverage': '1950-2020',
>     'Categories': 'Hematology (Q1); Oncology (Q1)'}
>     
```


<a name="ex1"></a>
**Exercici 1** How many entries are in scimago-medicine.csv?




<a name="ex2"></a>

**Exercici2** Show the first 25 entries.




<a name="ex3"></a>

**Exercici3**
Compta el número d'entrades publicades a Espanya en una llista (Country = Spain)



<a name="ex4"></a>

**Exercici4** Show the first 25 entries.



<a name="ex5"></a>

**Exercici 5** What types of scientific publications are in the file ?



<a name="ex6"></a>

**Exercici 6**  List all the avaliable categories. Each entry can have more than one category.



<a name="ex7"></a>

**Exercici 7** Show all data from entries of categories: "Sports Medicine" or "Sports science"



