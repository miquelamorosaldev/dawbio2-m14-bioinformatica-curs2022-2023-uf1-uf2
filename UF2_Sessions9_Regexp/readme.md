# Sessió 9 - Expressions regulars (2022-01-30)

Començarem fent alguns exercicis de tipus joc per repassar la teoria de regex.

## Regex Crossword.

Fem el Beginner.

https://regexcrossword.com/challenges/beginner/puzzles/1

#### Pista 1: Llegim les regex.

Aquesta què vol dir ? 

EP|IP|EF 

Que les 2 caselles ha de ser EP, IP o EF.

[?,E]
[?,P]

Ara, hem de verificar que la E i la P compleixen les altres 
expressions regulars ? 

A la fila 1, podem afirmar que serà la H.

[H,E]
[?,P]

#### Pista 2: Llegim les regex.

.*M?O.*

Pot haver una M o no.
La O és la única lletra que hi ha d'estar; pot ser la primera lletra o la segona.

(A|B|C)\1

Significa que hi ha d'haver 2 A, 2 B o 2 C.; el \1 significa que el 
patró del parèntesi s'ha de repetir.

#### Pista 5: Llegim les regex.

Cal entendre aquest:

\d[2480]

El primer caràcter, \d; significa qualsevol xifra.
El segon caràcter és un número que pot ser qualsevol dels 4 que surt a [2480], un 2 o un 4 o un 0 o un 8.


### SOLUCIONS.
<details>
  <summary>Si teniu dubtes, cliqueu per veure les solucions</summary
  
  #### SOLUCIÓ 1. Cançó Help dels Beatles.
    [H,E]
    [L,P]

  #### SOLUCIÓ 2. 
    [B,O]
    [B,E]

  #### SOLUCIÓ 5. 
    [1,9]
    [8,4]

</details>

<hr/>
<hr/>

## Sketch Engine.

http://regex.sketchengine.eu/cgi/ex1.cgi

### Possibles solucions 

<details>
<summary>Si teniu dubtes, cliqueu per veure les solucions</summary
  

Ex1.
![[regex-ex1-g2.png]](./img/regex-ex1-g2.png "regex-ex1-g2.png")

### (pi|sp|sl)

### .p.+|pit

La millor solució no és la més curta sinó la més clara; en aquest cas seria:
### (pi|sp|sl)

Possibles solucions Ex2:

http://regex.sketchengine.eu/cgi/ex2.cgi

### [arts7]ap|ap[ot]

Però encara millor:

### ap.[th]

Primeres lletres ap, tercera lletra pot ser qualsevol, 4a lletra la t o la h. 

#### Ex3, solucions.

### af..[fak ]

#### Ex4.

[^\w] = \W

</details>


## Regex Play.

Aquest és el més bo, perquè t'ajuda a resoldre problemes de la vida real: filtrar MAC's, adreces ftp, etc...

Abans de jugar et fa resoldre una petita enquesta.

![[regular_expressions.png]](./img/regular_expressions.png "regular_expressions.png")
Source: [xkcd](https://xkcd.com/208/)

http://play.inginf.units.it/#/level/1


<details>
<summary>Si teniu dubtes, cliqueu per veure les solucions</summary
  
Ex2.

### ([0-9a-f][0-9a-f]:?){6}

Per seleccionar les adreces MAC, optem per seleccionar 2 digits hexadecimals.
[0-9a-f]{2}

La MAC consta de 5 grups de 2 hexadecimals separats


Ex3.

### [a-z].*(FreeBSD.org/pub/FreeBSD/)

### ftp://[^ ]{1,}
### ftp://[\S]{1,}

ftp seguit de 1 o més caràcters que no siguin un espai [^ ]

</details>