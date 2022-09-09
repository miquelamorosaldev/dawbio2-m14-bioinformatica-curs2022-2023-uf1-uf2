## A012 - Exercicis repàs Pyhton. Primera Sessió

Realitza aquests exercicis en un quadern de Jupyter Notebook (ipynb).
Apart d'aquests exercicis t'anirà bé per a provar els exemples que hem posat en aquesta wiki, i exemples propis :) 

### EXA1. A partir d'una llista, que va del 0 al 20, crea, usant només una nova llista, la seva potència de base 2 elevat al número.
#### El resultats haurien de ser: 1, 2, 4, 8, 16, ...

**Pista:**

llistaNums = range(1,21)

List Comprension. 
myNewList = [elem for elem in list_source]

### EXA2. Crear un diccionari on les claus seran números autoincrementals a partir de l'1, i els valors una llista d'estudiants. 

**Pista:**

Dict. Comprension.
d2 = {key:value for key,value in dictionary_source.items()


### EXA3. A partir d'una llista en la qual els seus valors hi ha el grup sanguini i RH d'alguns donants de sang, crea un conjunt on es vegin els valors no repetits. (grup sanguini i RH; pex A+)

**Pista:**
llistaDonants = ["A+","O+","O-","A+", "AB+", "A+", "AB+", "B-", "O+"]


### EXA4. Crea una llista de números de l'1 al 100 i una funció per multiplicar per 5 un número, i fes que només es mostrin per pantalla els múltiples de 5.

**Pista:**
Operador divisió entera: %.
Exemples d'ús: 10 % 5 = 0. 2 % 5 = 2.


### Indicacions de FAQs Sessió 1.

Eliminar aquestes linies, que no calen mai:


conda install -n BIO anaconda python

o bé

conda install -c anaconda python

----

Afegir aquestes linies:

conda update -n base -c defaults conda

conda create -n bio

conda install -n bio -c conda-forge jupyterlab


Els entorns son molt lleugers.

Per veure'ls

conda env list

I borrar l'entorn vell:

conda env remove -n BIO
