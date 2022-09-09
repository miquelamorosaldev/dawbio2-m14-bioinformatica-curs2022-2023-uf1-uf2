## A0121 - Exercicis repàs Pyhton. Primeres Sessions.

Realitza aquests exercicis en un quadern de Jupyter Notebook (ipynb).
Apart d'aquests exercicis t'anirà bé per a provar els exemples que hem posat en aquesta wiki, i exemples propis :) 

### EXA1. A partir d'una llista, que va del 0 al 20, crea, usant només una nova llista, la seva potència de base 2 elevat al número.
#### El resultats haurien de ser: 1, 2, 4, 8, 16, ...

**Pista:**

llistaNums = range(1,21)

L'operació per a fer la potència 2 ^ num és: 2 ** num

List Comprension. 

myNewList = [elem for elem in list_source]

### EXA2. Crear un diccionari on les claus seran números autoincrementals a partir de l'1, i els valors una llista d'estudiants. 

**Pista:**

Dict. Comprension.
d2 = {key:value for key,value in dictionary_source.items()}


### EXA3. A partir d'una llista en la qual els seus valors hi ha el grup sanguini i RH d'alguns donants de sang, crea un conjunt on es vegin els valors no repetits. (grup sanguini i RH; pex A+)

**Pista:**

llistaDonants = ["A+","O+","O-","A+", "AB+", "A+", "AB+", "B-", "O+"]


### EXA4. Crea una llista de números de l'1 al 100 i una funció per multiplicar per 5 un número, i fes que només es mostrin per pantalla els múltiples de 5.

**Pista:**

Operador divisió entera: %.

Exemples d'ús: 10 % 5 = 0. 2 % 5 = 2.


### EXA5. Tenim un llistat de pluges mensuals. Mostra els següents resultats.
llistaPluges21 = [16.5, 0.0, 32.7, 6.5, 24.6, 15.7, 2.6, 0.0, 94.2, 65.5, 25.5, 9.2]
1. Calcula el total.
2. Ordena la llista de valors grans a petits.
3. Mostra els 3 valors més grans.
4. Obtén el valor màxim i el mínim.
5. Calcula la mitjana aritmètica.

