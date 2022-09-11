#  Exercici explotació fitxers CSV (2021 - 2022)
## <center>Pablo Garcia, Miquel Angel Bardají</center>

[Font de dades: Web Scimago ](https://www.scimagojr.com/journalrank.php?area=2700 "Web font de dades ")

> The SCImago Journal & Country Rank is a publicly available portal that includes the journals and country scientific indicators developed from the information contained in the Scopus® database. These indicators can be used to assess and analyze scientific domains. Journals can be compared or analysed separately. Country rankings may also be compared or analysed separately.


###  **Practica explotar un fitxer** i resoldre diferents consultes.

Fitxer de dades : [scimago-medicine.csv](../A013_ExplotacioFitxersCSV_2021_2022/scimago-medicine.csv "aqui")

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


### Exercicis

**A cada exercici, en alguns casos hi haurà dues solucions:

  · Una la proposada per Pablo Garcia (en un fitxer apart), aprofitant totes les funcionalitats de Python. Per les solucions suggerides per Pablo, serà necessari que tingueu també el fitxer [utils.py](utils.py "Utils.py") , que es troba dins la mateixa carpeta de github, com així mateix les solucions de Pablo.  
  
  · Una segona suggerida per Miquel Angel Bardají, més a l'estil de programació Java, realitzat al curs anterior. 
  


* [Ex1 - How many entries are in scimago-medicine.csv?](#ex1)
* [Ex2 - What types of scientific publications are in the file?](#ex2)
* [Ex3 - Agrupar publisher por numero de tipo de publicaciones](#ex3)
* [Ex4 - Cual es publisher más antiguo que aún publica (tiene publicación el último año)](#ex4)
* [Ex5 - Ranking de paises por H-Index](#ex5)
* [Ex6 - Llistar totes les categories](#ex6)
* [Ex7 - Categoría con más entradas](#ex7)
* [Ex8 - Todas las entradas de "Sports Medicine" o "Sports science"](#ex8)
* [Ex9 - Todas las regiones cubiertas por todas las entries](#ex9)
* [Ex10 - Exercici 10 Media del H-Index por region](#ex10)



# Entries from SciMago



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

<a name="ex1"></a>
**Exercici 1** How many entries are in scimago-medicine.csv?

```python
# 1. How many entries are in {csv_file_path}?
num = len(entries)
print(f"There are {num} entries.")
```

<a name="ex2"></a>

**Exercici 2** Detectar tots els valors diferents de la columna Type.



```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def get_unique_type(entries:list) -> list:
    unique = []
    for entrada in entries:
        # print(entrada['Type'])
        if (not (entrada['Type'] in unique)):
            unique.append(entrada['Type'])
            
    return unique
```


```python
# Buscar cuantos tipos de entradas hay diferentes
unicos = get_unique_type(entries)
print(unicos)
```

    ['journal', 'book series', 'conference and proceedings', 'trade journal']



```python
# Función que devuelve diccionario con los diferentes tipos y el numero de veces que aparece
def get_num_type(lista:list) -> dict:
    num_type = {}
    for entrada in lista:
        # print(entrada['Type'])
        if (not (entrada['Type'] in num_type)):
            num_type[entrada['Type']]=1
        else:
            num_type[entrada['Type']] = num_type[entrada['Type']] + 1
            
    return num_type
```


```python
diccionario = get_num_type(entries)
print(diccionario)
```

    {'journal': 6823, 'book series': 35, 'conference and proceedings': 262, 'trade journal': 5}



```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def get_unique_type2(entries:list) -> list:
    unique = []
    for entrada in entries:
        # print(entrada['Type'])
        if (not (entrada in unique)):
            unique.append(entrada)
            
    return unique
```


```python
#type(entries)
#type(entries[0])

listaTipos = [d["Type"] for d in entries]
l = get_unique_type2(listaTipos)
print(l)
```

    ['journal', 'book series', 'conference and proceedings', 'trade journal']



```python
#Buscar cuantas publicaciones de españa hay
#buscar cuabntas superan una tasa
#buscar cuantas publicaciones de cada tipo hay

import re

text = "python is, an easy;language; to, learn."
print(re.split('; |, ', text))

```

    ['python is', 'an easy;language', 'to', 'learn.']

<a name="ex6"></a>
### Exercici 6: Llistar totes les categories

--> [Solució Pablo exercici6 FER CLICK AQUI](q6.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA a continuació --> 

```python
categorias: set = set() #Mejor así. Desambigua
for entrada in entries:
    lista = re.split(';', entrada['Categories']) #Separa, en función de los delimitadores que le pongas
    for cate in lista:
        posicion=cate.find(" (Q")
        if (posicion!=-1):
            cate = cate[:posicion]
        categorias.add(cate.strip())
        
#print(categorias)
#mylist = [x for x in iterable]
mylist = list(categorias)
mylist.sort()
i=1
for item in mylist:
    print(i,item,)
    i=i+1
```

   > 1 Acoustics and Ultrasonics
   > 2 Advanced and Specialized Nursing
   > ..
   > 286 Waste Management and Disposal
   > 287 Water Science and Technology

<a name="ex7"></a>
### Exercici 7: Categoría con más entradas

--> [Solució Pablo exercici7 CLICK AQUI](q7.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python
categorias: dict = set() #Mejor así. Desambigua
dictionary = {}
for entrada in entries:
    lista = re.split(';', entrada['Categories']) #Separa, en función de los delimitadores que le pongas
    for cate in lista:
        posicion=cate.find(" (Q") # Elimino el texto trimestre
        if (posicion!=-1):
            cate = cate[:posicion]
        cate = cate.strip() #Elimino espacios por delante
        if cate in dictionary:
            dictionary[cate]+=1
        else:
            dictionary[cate]=1
dictionary2=dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))
dictionary2
i=0
for key in dictionary2:
    i = i + 1
    if (i<=20):
        print((i),'-', key,':',dictionary2[key])
    else:
        break;
```


> 1 - Medicine (miscellaneous) : 2447
> 2 - Public Health, Environmental and Occupational Health : 560
> 3 - Psychiatry and Mental Health : 537
>  ...
>  19 - Health (social science) : 195
>  20 - Clinical Psychology : 195

<a name="ex8"></a>
### Exercici 8 Todas las entradas de "Sports Medicine" o "Sports science"

--> [Solució Pablo exercici8 CLICK AQUI](q8.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python
i=0
for entrada in entries:
    #if entrada['Categories'].find("Sports")!=-1:
    if "Sports" in entrada['Categories']:
        i=i+1
        print(entrada)
        
```

>    {'Rank': '121', 'Sourceid': '19817', 'Title': 'British Journal of Sports Medicine', 'Type': 'journal', 'Issn': '03063674, 14730480', 'SJR': '4,329', 
>    'SJR  Best Quartile': 'Q1', 'H index': '171', 'Total Docs. (2020)': '394', 'Total Docs. (3years)': '1156', 'Total Refs.': '11234', 'Total Cites (3years)': 
>    '7715', >'Citable Docs. (3years)': '668', 'Cites / Doc. (2years)': '5,97', 'Ref. / Doc.': '28,51', 'Country': 'United Kingdom', 'Region': 'Western Europe', 
>    'Publisher': >'BMJ Publishing Group', 'Coverage': '1964, 1974-2020', 'Categories': 'Medicine (miscellaneous) (Q1); Orthopedics and Sports Medicine (Q1); 
>    Physical Therapy, Sports Therapy and Rehabilitation (Q1); Sports Science (Q1)'}
>    ...

> {'Rank': '7091', 'Sourceid': '21101013588', 'Title': 'Journal of Spine Surgery', 'Type': 'journal', 'Issn': '2414469X, 24144630', 'SJR': '', 
> 'SJR Best Quartile': '-', 'H index': '4', 'Total Docs. (2020)': '127', 'Total Docs. (3years)': '0', 'Total Refs.': '4501', 'Total Cites (3years)': '0',
>  'Citable Docs. (3years)': '0', 'Cites / Doc. (2years)': '0,00', 'Ref. / Doc.': '35,44', 'Country': 'China', 'Region': 'Asiatic Region', 'Publisher': 
>  'AME Publishing Company', 'Coverage': '2020', 'Categories': 'Orthopedics and Sports Medicine; Surgery'}


<a name="ex9"></a>
### Exercici 9 Totes les regions cobertes per totes les entrades

--> [Solució Pablo exercici9_CLICK AQUI](q9.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python
regiones: dict = set() #Mejor así. Desambigua
for entrada in entries:
    regiones.add(entrada['Region'])
regiones
```



 >   {'Africa',
 >    'Africa/Middle East',
 >    'Asiatic Region',
 >    'Eastern Europe',
 >    'Latin America',
 >    'Middle East',
 >    'Northern America',
 >    'Pacific Region',
 >    'Western Europe'}


<a name="ex10"></a>
### Exercici 10 Media del H-Index por region

--> [Solució Pablo exercici10_CLICK AQUI](q10.py "Solucion Pablo")


##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python
# Función que devuelve una lista de valores unicos de una lista con valores repetidos
def actualizar_lista(entrada:list, valor:int) -> list:
    entrada[0] = entrada[0] + 1
    entrada[1] = entrada[1] + valor
    
            
    return entrada

def media(entrada:list) -> float:        
    return entrada[1]/entrada[0]


dictionary = {}
for entrada in entries:
    region = entrada['Region']
    if region in dictionary:
        dictionary[region] = actualizar_lista(dictionary[region], int(entrada['H index']))
    else:
        dictionary[region]=[1]
        dictionary[region].append(int(entrada['H index']))

for entrada_diccionario in dictionary:
    print(entrada_diccionario,'-', media(dictionary[entrada_diccionario]))

```

>    Northern America - 65.21652816251154
>    Western Europe - 54.08188428706924
>    Asiatic Region - 21.913719943422915
>    Pacific Region - 28.87704918032787
>    Eastern Europe - 12.408415841584159
>    Middle East - 19.862962962962964
>    Africa/Middle East - 26.017241379310345
>    Latin America - 18.331550802139038
>    Africa - 17.75

<a name="ex5"></a>
### Exercici 5 -  Ranking de paises por H-Index

--> [Solució Pablo exercici5 CLICK AQUI](q5.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python

```
<a name="ex4"></a>
### Exercici 4.- Cual es publisher más antiguo que aún publica (tiene publicación el último año)

--> [Solució Pablo exercici4 CLICK AQUI](q4.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 
```python
# 'Publisher': 'Wiley-Blackwell',
  #'Coverage': '1950-2020',
import datetime

#Obtains the current year of execution
def current_year() -> int:  
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = int(date.strftime("%Y"))      
    return year


categorias: dict = set() #Mejor así. Desambigua
dictionary = {}
year_min = current_year()
year = year_min
name = [] 

for entrada in entries:
    anyos = re.split('-|,', entrada['Coverage']) #Separa
    anyos = [int(i) for i in anyos]
    if (year_min > anyos[0] and anyos[-1]==(year-1)):
        name.append(entrada['Publisher'])
        year_min = anyos[0]
    elif (year_min== anyos[0] and anyos[-1]==(year-1)):

        name.append(entrada['Publisher'])

print('The publishers -> ' ,name, ' first publish in ', year_min)


```

  
 >   The publishers ->  ['Wiley-Blackwell', 'Massachussetts Medical Society', 'American Physiological Society', 'Elsevier Ltd.']  first publish in  1823

<a name="ex3"></a>
### Exercici 3 Agrupar publisher por numero de tipo de publicaciones

--> [Solució Pablo exercici3 CLICK AQUI](q3.py "Solucion Pablo")

##### Segona solució PROPOSADA MÉS ESTIL JAVA--> 

```python
# Imports

import utils
import pprint


# ---3. Group publisher by number of publications----
# -----------------------------------------------------------------------------
def q3():
    
    publisher_dict:dict[str,set()]={} #dictionari clave publicador, valor conjunto de type de publicacionse
    publisher_dict_num:dict[str,int]={} 
    raw_entries: list[dict] = utils.read_csv_file("scimago-medicine.csv")
    lista_tupla:list[tuple[str, int]]

    for publicacio in raw_entries:

            if publicacio['Publisher'] in publisher_dict: 
                publisher_dict[publicacio['Publisher']].add(publicacio['Type']) #afegeixo al ser
            else:
                publisher_dict[publicacio['Publisher']] = {publicacio['Type']} #afegeixo primer al dictionari

    #print(publisher_dict);

    for clave in publisher_dict:
    # conto el numero de elements de cadascun dels conjunts
        publisher_dict_num[clave] = len(publisher_dict[clave])
    
    publisher_num_type:dict[int,int]={} 
    for clave in publisher_dict_num:
        #aqui la clave la utilitzo per trobar el numero de types que te aquest publisher
        #aquest valor sera la clau del nou diccionari, si existeix augmento en 1 i sino la 
        #inicialitzo a 1
        clau = publisher_dict_num[clave]
        if clau in publisher_num_type:
            publisher_num_type[clau] += 1
        else:
            publisher_num_type[clau] = 1
    
    
    #lista_tupla = sort_ranking(publisher_dict_num)
    #print(lista_tupla)
    print(publisher_num_type)
    
    
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    q3()
# -----------------------------------------------------------------------------

```

>    {1: 1884, 2: 20}




