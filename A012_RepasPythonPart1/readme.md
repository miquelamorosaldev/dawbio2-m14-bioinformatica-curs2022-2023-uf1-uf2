# Repàs d'instruccions de Python.

##       <center>Pablo Garcia, Miquel Angel Bardají</center>
<p></p>

### Bibliografia Python

· [Tutorial pàgina oficial Python](https://docs.python.org/es/3/tutorial/)

· [Revolunet](https://pythonbooks.revolunet.com/)

· [Pildoras informaticas](https://www.youtube.com/watch?v=G2FCfQj-9ig)

· [Python cheatsheets](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

· [Python cheatsheets begginners](https://ehmatthes.github.io/pcc/cheatsheets/README.html)

· [10 must have python cheatsheets](https://betterprogramming.pub/10-must-have-python-cheatsheets-2b74e8097bc3)


## Tipus de dades.

- Python per defecte es **tipat implicit i dinàmic** (va bé per programes petits, de forma interactiva o exploratoria). 
- Vol dir, que no ens falta declarar el tipus de la variable, al utilitzar-la per primer cop(*implicit*), i a més, una variable, pot canviar de tipus durant el programa(*dinàmic*). 
- 
- **Exemple**

```python
    var1 = 1;
    print (var1);
```
 > 1

 Canviem posteriorment i li assignem el String "Hola"
 ```python
     var1 = "Hola";
    print(var1);
```
> Hola

 **Java** és explícit i estàtic, al definir la variable, tens que declarar quin tipus és, i no pot canviar el seu tipus durant el cicle de vida del programa.


## Comandes bàsiques

* [Imprimir Pantalla](#print)
* [Declaracions funcions](#funcions)
* [If](#if)
* [Bucles for/while](#bucles)
* [Funció range](#range)
* [Operadors lògics](#logics)
* [Instrucció pass](#pass)
* [Llistes](#llistes)
* [Tuples](#tuples)
* [Diccionari](#diccionari)
    * [Exercicis amb diccionaris](#exercici_diccionari)
    * [Comprenhension](#comprenhension)
    * [Exercici Llistes amb comprenhension](#exercici2_comprenhension)
* [Slices](#slices)
* [Conjunts (Sets)](#sets)
* [Bucles e indexs Avançats](#buclessup)
* [Utilitat Ajuda python](#ajuda)

<a name="print"></a>

#### Imprimir per pantalla, forma bàsica.

```python
print("Hello World!");
```
>Hello World!

```python
s = "Hola Mundo. \n ¿Que tal estas?"
print(s)
```
> Hola Mundo. 
> ¿Que tal estas?

#### Raw Strings No interpreta els càracters de ESCAPE.

```python
r = r"Hola Mundo.\n¿Que tal estàs?"
print(r)
```
> Hola Mundo.\n¿Que tal estàs?

#### Format Strings. Van be per imprimir variables

```python
name = "Bardaji"
name2 = "Pablo"
print("Hello " + name + " and hello " + name2)
frase_format = f"Hello {name} and hello {name2}"
print(frase_format)
```
> Hello Bardaji and hello Pablo
> Hello Bardaji and hello Pablo

<a name="funcions"></a>
Declaracions de funcions

```python
In [3]: def say_hello():
...:     print("Hello World!!!")
...:     print("Dawbio")
...: 
In [4]:  say_hello():
```

>Hello World!!!
>Dawbio

**Tabulacions obligatòries despres dels :** 
   Els claudàtors(corchetes) dels if's i del while, amb Java, es substitueix per un tabulador.

<a name="if"></a>

#### if

El tabulador s´utilitza al if i al else

```python
if (s=="HOLA"):
    print ("HOLA")
elif (s=="Adios"):
   print("Era adios")
else:
    print("No es hola")
```


<a name="bucles"></a>

#### bucles (while/for)

***while***
El while s'executa igual que Java.

```python
count = 1
while (count <= 10):
    print(count)
    count += 1
```

***for***
Es diferent a la forma vista amb Java, ja que necessita un array inicialitzat.


```python
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
```

Inicialitzem, el array amb la funció **range()**, ficant el punt d'inici(inclusiu) i el punt final(exclusiu).

```python
# Solution 3
numbers = range(1,11)
for number in numbers:
    print(number)
``` 
Segona forma d'inicialitzar la comanda for.

```python
for number in range(1,11):
    print(number)
``` 
<a name="range"></a>
**Range tiene tres formas:**
 1. Con 1 parámetro
 2. Con 2 parámetros
 3. Con 3 parámetros

Range devuelve un "Generador", no una lista. Si quiero una lista, tengo que convertirla, manualmente con list(...)

```python
list(range(10))

list(range(1, 11))

list(range(1, 11, 2))
``` 

<a name="logics"></a>
##### **Operadors lògics **
A diferencia de java, s'escriuen amb lletres (AND/OR/XOR/NOT)

```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
elif (n>5) OR (n<2):
   print("Fora de 2 y 5")
else:
    print("es un altre cas")
```
<a name="pass"></a>
##### **pass**
Es la paraula per no fer cap acció dintre de un if
```python
if (n>2) AND (n<5):
    print ("esta entre 2 y 5")
else:
    pass
```

<a name="llistes"></a>
##### **llistes**

Comencen per 0, com a molts llenguatges.

```python
l1 = [0,1,2,3]
lx = [0,1,True,"Hola"]
```
Per saber la longitud d´una llista
```python
len(lx)
```

Diferències amb Java, la comilla(") i la comilla simple(') és el mateix

```python
l=["a","b","c"]
```

però serveix per poder ficar cometes dobles dins de la simple

```python
msg ='Dijo "Vete de aqui!"'
msg
```

> msg ='Dijo "Vete de aqui!"'

amb python "a" == 'a' es TRUE

<a name="tuples"></a>
##### **Tuples**

Tupla és una llista de sol lectura, no és la opció mes recomanable..
```python
t = ("a","b","c")
t
```

> ('a', 'b', 'c')

<a name="diccionari"></a>
#### **Diccionari**

Diccionari, Hash, Tabla Hash, Has Map, Mapa son tots sinònims. És diferent d'Arrays...

**Arrays**
|Claus   | Valors   |
| :------------: | :------------: |
|0   | "Roger"  |
| 1  |  "Dani" |
| 2  |  "Mar" |
| 3  |  "Albert" |
| 4  |  "Carlos" |

- Amb un diccionari, les claus, poden ser del tipus que vulgui, no sol enters. *Exemple: Strings*
- Les claus tenen que ser úniques, no hi pot haver repetides.

**Diccionari**
|  Claus | Valors   |
| :------------: | :------------: |
|  "Roger" | 111  |
| "Dani"  |  222 |
| "Mar" |  223 |
| "Albert" | 342  |
| "Carlos" |  782 |

Nomenclatura per diccionaris
- () Brackets
- [] Square Brackets
- {} Curly Brackets
- <> Angle Brackets

```python
d = {"Roger": 111,
    "Dani":   234,
    "Mar":    342,
    "Albert": 567,
    "Carlos": 478 }
d["Roger"]
```
> 111

```python
for keys in d:
    print(keys)
```

>Roger

>Dani

>Mar

>Albert

>Carlos

<a name="exercici_diccionari"></a>
***Exercici 1*** Crear un nou diccionari on les claus del primer siguin els valors del segon i els valors, passin a ser les claus.

Per una de les possibles solucions al exercici s'introdueix un nou concepte el de comprenhension

<a name="comprenhension"></a>

##### Comprenhension Lists and Dicts

·Hi ha "Dict Comprenhensions" y "List Comprenhensions", serveixen per a inicialitzar i omplir de dades d'una llista (o diccionari) basant-nos en valors d'una llista (o dict.) existent. 

·Per a llegir o escriure una comprenhension, es comença per la comanda del mig (pel "for") de l'instrucció.

·**Dict comprenhension**

    ```d2 = {key:value for key,value in dictionary_source.items()```

·**List comprenhension**

    ```d2 = {elem for elem in List_source```

Crear un nou diccionari on les claus del primer siguin els valors del segon i els valors, passin a ser les claus.

[Solucions exercici1](exercici1.md "exercici1")

<a name="exercici2_comprenhension"></a>

***Exercici 2*** A partir d'una llista, que va del 1 al 10, crear amb una linea , una nova llista, amb els valors al quadrat de la primera.

[Solucions exercici2](exercici2.md "exercici2")


<a name="slices"></a>

##### Slices

Es una opció per retallar diferents llistes, de maneres diferents. 
S'utilitza sovint perquè és molt pràctic, i una funcionalitat inèdita.

```python
#Indexes = 0..7 (8 letters)
# len -1 = últim índex

slic = ["a","b","c","d","e","f","g","h"]
len(slic)

#del 2 al 7
slic[2:7]
```

> ['c', 'd', 'e', 'f', 'g']


```python
#del 2 al final
slic[2:len(slic)]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
#del 2 al final
slic[2:]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
# Del principi a la 5 lletra
slic[:5]
```

> ['a', 'b', 'c', 'd', 'e']

```python
#Tota la llista retornant una copia
slic[:]
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


```python
#Si fiques un index fora de límits del array, no dona error outofBounds del segon índex
slic[2:2000]
```

> ['c', 'd', 'e', 'f', 'g', 'h']

```python
#Llegir tota una llista saltant de X en X, es un tercer parametre "step"
slic[0:8:2]
```

> ['a', 'c', 'e', 'g']

```python
#Índex negatius, comencen pel final de la llista. El -1 és el final de la llista.
slic[-1]
```

> 'h'

```python
#Puc fer rangs amb índexs negatius
slic[-8:-1]
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

```python
slic[-8:] #fins la h. No puc ficar el índex final
```

> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

```python
#Exemple avançat. Invertir una secuencia
slic[::-1]
```

> ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

```python
"Hola Mundo"[::-2]
```

> 'onMao'
<a name="sets"></a>

#### Sets

Objecte creats que funcionen similar a la teoría de conjunts.
- S'utilitzen sobretot quant vols tenir elements que no es repeteixin. 
- Els elements no tenen ordre, (realment tenen ordre d'inserció), quant començes a utilitzarlos amb diferents operacions, aquest ordre es pot perdre.

```python
# num_set: set ={} #igual que un dict
num_set: set = set() #Mejor así. Desambigua

num_set.add(1)
num_set.add(1)
num_set.add(1)
num_set.add(2)
num_set.add(2)
num_set
```

>  {1, 2}



```python
len(num_set)
```

> 2


```python
num_set.pop()
```

> 1

```python
#Borra si existe, sin dar error , si no existe -> Remove si no existe , fallara
num_set.discard(2)
```


```python
seta:set = {1,2,3}
setb:set = {3,4,5}
seta
setb
```

> {1, 2, 3}

> {3, 4, 5}




```python
#unió tots els elements amb un eliminat duplicats
seta.union(setb)
seta | setb
```



> {1, 2, 3, 4, 5}

> {1, 2, 3, 4, 5}



```python
#elements que es troben als dos conjunts
seta.intersection(setb)
seta & setb
```
> {3}

> {3}


```python
#saber si un objecte es subconjunt d'un altre o sigui que tots els seus elements es
#troben al b.
seta.issubset(setb)
```

> False


```python
#saber si un objecte es superconjunt del altre ( o sigui que tots els elementos del altre)
seta.issuperset(setb)
```

> False



```python
#Poder eliminar duplicats d'una llista, la passo a un conjunt(set)
types_list = ["journal","journal","journal","journal","journal","others"]
types_set = set(types_list)
types_set
```


> {'journal', 'others'}



```python
# Set comrenhension
set2 = {elem*2 for elem in seta}
print(set2)
```

>   {2, 4, 6}


```python
#Dict comprenhensio
d1 = {"a": 1, "b":2}
d2 = {k: v for k, v in d1.items()}
print(d2)
```

>   {'a': 1, 'b': 2}

<a name="buclesup"></a>

##### Bucles avançats, recuperar el index i crear tuples.

Utilitzem normalment els índex, si vols o necessites els índexs, utilitzem el while.

Si no ens fa falta el index, utilitzem el for

Pero si volem saber els índexs, utilitzant la instrucció for podem utilitzar **enumerate**

```python
lista_index = ["a","b","c","d","e","f","g","h"]

for item in enumerate(lista_index):
    print(item)
```

> (0, 'a')
 
> (1, 'b')
 
> (2, 'c')
 
> (3, 'd')
 
> (4, 'e')
 
> (5, 'f')
 
> (6, 'g')
 
> (7, 'h')

Com ho fem si volem veure, per exemple el segon element de cadascuna de les tuples?.

```python
for item in enumerate(lista_index):
    print(item[1])
```

> a

> b

> ..

> h

Si volem crear una llista de tuples podem fer...

```python
el = list(enumerate(lista_index))
el
```

> [(0, 'a'),  (1, 'b'),  (2, 'c'),  (3, 'd'),  (4, 'e'),  (5, 'f'),  (6, 'g'),  (7, 'h')]

Per poder mostrar amb el for, el primer o el segon element de cadascuna de les tuples realitzem aquesta comanda

```python
for index, elem in enumerate(lista_index):
    print(elem)
```

> a

> b

> ..

> h


o si volem veure el índex

```python
for index, elem in enumerate(lista_index):
    print(index)
```
> 0

> 1

> ..

> 7

Altres utilitats, anomenar cada element d'un array amb una variable

```python
nombre, apellido1, apellido2 = ["Pablo","Garcia","Bardaji"]
print(nombre + "-" + apellido1 + "-" + apellido2)
```
> Pablo-Garcia-Bardaji

També si algunes posicions no ens interessen,  podem assignar aquelles posicions a _ .
```python
nombre, apellido1, _ ,_ = ["Pablo","Garcia","Bardaji","Dawbio"]
print(nombre + "-" + apellido1 )
```

> Pablo-Garcia

***Exercici 3*** 
Construir la llista de tuples amb un bucle while

[Solució exercici3](exercici3.md "Solució exercici3")


<a name="ajuda"></a>

### Documentació funcions

Per saber totes les funcions associades al objecte, es pot fer com realitzem amb Java...
```
 nom_objecte. <Tab> -> Autocomplete
 nom_objecte.nom_funcio <Tab>+<Shift> Documentació de la funció
```

### Type Hint -> Definir tipus a les variables.

Una opció molt útil, es comentar linees dins el codi, per indicar el tipus de les variables s'utilitza :
** Important ** Els dos ':' i el tipus de darrera. 
Per python és sol comentari, no fa cas, la variable prendrà el tipus de valor que se li asigni, en cada moment.

```python
a: int = 3
b: bool = True
myList: float = [4.0,5.0,6.0]
# Los dos : y el tipo, per python es sols un comentari, no ho té amb compte, la variable pendrà el tipus del valor que li assignis.
```
