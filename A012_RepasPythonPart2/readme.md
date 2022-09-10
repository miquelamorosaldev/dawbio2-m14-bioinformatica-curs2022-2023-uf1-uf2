## Lectura de fitxers amb iteradors

|  Python v3.9 |
| :------------ |
|  cheatsheets|
|   Anaconda > Environments (Jupyter Lab)|
|   python > list,dict,set|

* * *

|  Iteradors |
| :------------ |
|  **Pros:** |
|  Ocupa molt poca memòria|
|  **Contres:** |
|  Sol es pot recorrer un sol cop|
|  No admet acces directe|
|  No puc donar marxa endarrera|

* * *

|  Implementació |
| :------------ |
|  Un iterador es qualsevol objecte que te dues funcions sempre |
|  **__iter__()** > Retorna un iterador |
|  **__next__()** retorna el següent element del iterador, en funció de la iteraciò anterior|

* * *

|  Utilització |
| :------------ |
|  Per fitxers molts grans, es recomable, al utilitzar menys memòria file.readLine()|
|  Concatena càlculs (*programació funcional*) |

```python
#obrim el fitxer amb mode lectura i ho retorna a un iterador (file)
file = open('scimago-medicine.csv',"r")
for i in range(5):
    print(file.readline())

```

  >  Rank;Sourceid;Title;Type;Issn;SJR;SJR Best Quartile;H index;Total Docs. (2020);Total Docs. (3years);Total Refs.;Total Cites (3years);Citable Docs. (3years);Cites / Doc. (2years);Ref. / Doc.;Country;Region;Publisher;Coverage;Categories
  >  
  >  1;28773;"Ca-A Cancer Journal for Clinicians";journal;"15424863, 00079235";62,937;Q1;168;47;119;3452;15499;80;126,34;73,45;United States;Northern America;"Wiley-Blackwell";"1950-2020";"Hematology (Q1); Oncology (Q1)"
  >  
  >  2;19434;"MMWR Recommendations and Reports";journal;"10575987, 15458601";40,949;Q1;143;10;9;1292;492;9;50,00;129,20;United States;Northern America;"Centers for Disease Control and Prevention (CDC)";"1990-2020";"Epidemiology (Q1); Health Information Management (Q1); Health (social science) (Q1); Health, Toxicology and Mutagenesis (Q1); Medicine (miscellaneous) (Q1)"
  >  
  > 3;18991;"Nature Reviews Genetics";journal;"14710056, 14710064";26,214;Q1;365;106;325;7332;6348;149;21,22;69,17;United Kingdom;Western Europe;"Nature Publishing Group";"2000-2020";"Genetics (Q1); Genetics (clinical) (Q1); Molecular Biology (Q1)"
  > 
  > 4;21318;"Nature Reviews Immunology";journal;"14741741, 14741733";20,529;Q1;390;230;436;9421;8200;202;17,33;40,96;United Kingdom;Western Europe;"Nature Publishing Group";"2001-2020";"Immunology (Q1); Immunology and Allergy (Q1); Medicine (miscellaneous) (Q1)"
  > 
    

```python
#Si no esta tancat el iterador, es troba al punt ultim que ha llegit a l'instrucció
#anterior, no pot tirar endarrera.
for i in file:
    print(i)
#recordar tancar
file.close()
```

## Paradigmes de la programació amb Python.

|  Paradigmes de la programació |
| :------------ |
|  *Procedural* utilitzen funcions impures |
|  *OOP* tenen totes funcions impures |
|  *Funcional* emprar el màxim possible de funcions pures(almenys una segur que hi ha) |


## Funcions pures: 
>  ·Sol llegeix dels seus paràmetres d'entrada
>  ·Sol escriu desde els seus paràmetres de sortida
>  ·Si pels mateixos paràmetres d'entrada sempre retorna els mateixos paràmetres d'entrada
 
> **Pros** 
> Són les més reutilitzables.
> Les més testejables
> Amb general, son les que tenen menys bugs

<hr/>
|  Yield  |
| :------------ |
|  Substitueix al return amb la diferencia que el yield , no fa acabar la funció guarda l'estat intern de la funció recorda el punt on s'estava executant, i quant la tornes a  crida comença a partir del yield, no del inici. |


|  Generator  |
| :------------ |
|  Un iterador creat per la paraula clau "yield" |
| Es comporta igual que un iterador creat a mà (té la funció __next__()) |

```python
def get_nums():
    for num in range(5):
        yield num 
                
```


```python
type(get_nums)
```


> function


```python
n = get_nums()
n
```


 >   <generator object get_nums at 0x7f044a85c5f0>


```python
n.__next__()
```

>    0


```python
n.__next__()
```

>    1


```python
n.__next__()
```

>  2


```python
n.__next__()
```

> 3


```python
n.__next__()
```

> 4

```python
n.__next__()
```

Quan arriba al final, de la iteració dona un error i una excepció.

>    ---------------------------------------------------------------------------
>    
>     StopIteration                             Traceback (most recent call last)
>     
>   <ipython-input-24-8d5cb7b534a9> in <module> ----> 1 n.__next__()
>
>  StopIteration: 

## Programació funcional
    

Per concatenar operacions fent 3 funcions bàsiques (sol treballar amb iteracions) |
1. **map**, alternativa a les list/dict comprensions.
2. **filter**, força interessant i més net que l'ús de condicionals dintre de bucles.
3. **reduce**, va bé per agrupar valors, però s'utilitza menys.
4. **zip**, s'utilitza si volem treballar amb tuples.

### Exemple Map.    
    
```python
    #funció que qualsevol número que li passes, multiplicarà per 2
def mult2(i: int) -> int:
    return i*2
```


```python
n = get_nums()
n2 = map(mult2,n) 
```


```python
n2.__next__()
```

>  0


```python
#el 1 multiplicat per 2
n2.__next__()
```

>  2

```python
#el 2 que dona la iteració n es multiplicat per 2
n2.__next__()
```

> 4

### Exercici 4 - Map. 

Crea una llista de números i una funció per multiplicar per 3 un número, i fes que es mostrin per pantalla tots els números de la llista multiplicats per 3.

```python
def mult3 (num: float) -> float:
    return num * 3

# range genera sequències de números
# range (num_ini, num_fin, step)
llistaNums: float = list(range(10,40,2))

print("Llista números original.")
print(llistaNums)

print("Llista números multiplicats per 3.")
llistaNumsPer3 = list(map(mult3,llistaNums))

print(llistaNumsPer3)
```
Llista números original.
    
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
    
Llista números multiplicats per 3.
    
[30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114]


### Exemple Filter.

```python
def is_even(i: int) -> bool:
    return True if i % 2 == 0 else False

n = get_nums()
    #filtra la sortida si compleix la condició de la funció booleana, si el número és parell.
n3 = filter(is_even, n)
list(n3)
```

> [0, 2, 4]

```python
#creo un generador amb el for
iterador_meu = (i for i in range(4))
type(iterador_meu)
```

    >  generator


```python
iterador_meu.__next__()
```

> 0


```python
iterador_meu.__next__()
```
> 1

### Exercici 5 - Filter. 

Crea una llista de números (pex de notes d'alumnat) i una funció per a comprovar si el número és major o igual a 5, i fes que es mostrin per pantalla únicament els números de la llista majors o iguals que 5. Finalment, calcula el percentatge de números filtrats (els >=5) arrodonit a 2 decimals.

```python
def greaterOrEqual5 (num: float) -> bool:
    return num >= 5

llistaNotes: float = [8,5,6.2,4.2,10,6.8,3.4,7.9,9.3,8,2.4,9.7,7.6]

print("Llista notes original.")
print(llistaNotes)

print("Llista notes majors o iguals a 5.")
llistaNotesMajorsIguals5 = list(filter(greaterOrEqual5,llistaNotes))

print(llistaNotesMajorsIguals5)

print("Percentatge aprovats.")
# Dividim la longitud de les notes >5 respecte el total de notes 
# La funció len ens permet veure el número d'elements de les llistes. 
percAprov: int = len(llistaNotesMajorsIguals5) / len(llistaNotes)

## Per arrodonir a 2 decimals usem funció round.
print( str( round(percAprov,4)*100) + ' %') 
```

Llista notes original.
[8, 5, 6.2, 4.2, 10, 6.8, 3.4, 7.9, 9.3, 8, 2.4, 9.7, 7.6]
Llista notes majors o iguals a 5.
[8, 5, 6.2, 10, 6.8, 7.9, 9.3, 8, 9.7, 7.6]
Percentatge aprovats.
76.92 %

Més exemples de Programació Funcional:
https://pythondiario.com/2018/07/ejercicios-en-python-con-funciones.html
