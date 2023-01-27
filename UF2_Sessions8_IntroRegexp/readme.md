# Sessió 8 - Més Biopython i expressions regulars (2022-01-27)

### Repàs sessions 6 i 7.

SeqIO, devuelve SeqRecors, que se leen de ficheros fasta o genbank. 

SeqRecord
    locus           dict, key/value
    annotations     dict, key/value
    features        SeqFeature 
                    -> contains several SeqLocation
    seq             Seq (és un String)

El disseny de Prog.Or.Objectes no és òptim, conté massa classes i amb noms similars.

# Introduccó sessions regulars.

Imaginem que volem cercar si hi ha un tros de cadena en una seqüència molt llarga.

Podem usar mètodes de Python (in), però ens ofereixen molta més flexibilitat **les expressions regulars.**

Les expressions regulars són un llenguatge per expressar patrons. És a dir, una estructura que es repeteix entre 0 i n vegades.

### Recursos practicar regexp.

- Reptes per aprendre expressions regulars (teoria). 
  https://regexone.com/
- Validador d'expressions regulars (debug)
  https://regex101.com/

## Tipus patrons regexp.

Els patrons s'escriuen usant els següents caràcters.

**1. Literals (una lletra)**
 a L, Z, J, 9, 2, #, % => Qualsevol caràcter no especial

Per exemple, quantes vegades apareix un patró 'A' a la cadena 'GATAGATA'
Resultat: Apareix 4 vegades.

**2. Caràcters especials.** 

**2.1. Backslash "\"**

Fa que el següent càracter és especial (si no ho és).
Fa que el següent càracter no sigui especial (si ho és).

**Exemples** 
```python
    \n (newline)
    \t (tab)
    \s (whitespace)
    \b (boundary, un link)
    \. (punt normal, colon, dot)
    \w (carácter de palabra)
    \d dígito de un número
    \D Un caracter que no és un dígit.Una majúscula significa negació.
    \W Tots menys els alfanumèrics: És a dir, símbols (inclou espais)
```

Per a fer la \ com a literal, hem de fer '\\'

<em>En otras palabras; es como la varita de Harry Potter, le da poderes al literal del lado, convierte un literal a carácter especial y al revés.</em>

### Exemple:
Patró:      \d
Text:       hola123
Resultat:   3 coincidencies

**2.2. Dot "."**
El punt és un comodí, significa qualsevol caràcter, però només un.
Excepció: No coincideix amb el '\n', el salt de linea (a no ser que activis la opció single-line)

**Exemple: Agafa 3 caracters qualsevol** 

![[dotexemple1.png]](./img/dotexemple1.png "dotexemple1.png")

Amb el backslash interpreta un punt com a literal

![[dotexemple2.png]](./img/dotexemple2.png "dotexemple2.png")

