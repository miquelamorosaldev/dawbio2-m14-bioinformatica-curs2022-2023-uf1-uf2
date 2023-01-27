# Sessió 8 - Expressions regulars (2022-01-27)

### Repàs sessions 6 i 7.

SeqIO, devuelve SeqRecors, que se leen de ficheros fasta o genbank. 

SeqRecord
    locus           dict, key/value
    annotations     dict, key/value
    features        SeqFeature 
                    -> contains several SeqLocation
    seq             Seq (és un String)

El disseny de Prog.Or.Objectes no és òptim, conté massa classes i amb noms similars.

# Introducció expressions regulars.

Imaginem que volem cercar si hi ha un tros de cadena en una seqüència molt llarga.

Podem usar mètodes de Python (in), però ens ofereixen molta més flexibilitat **les expressions regulars.**

Les expressions regulars són un llenguatge per expressar patrons. És a dir, una estructura que es repeteix entre 0 i n vegades.

En altres paraules, serveixen per buscar coincidències (matches) en un text.

Per exemple, si un text té format de DNI/NIE, email, etc...

Per raons d'eficiència es prefereix usar regexp que programar-les nosaltres, és un llenguatge de baix nivell que s'ha de compilar, com el C. 

### Recursos practicar regexp.

- Reptes per aprendre expressions regulars (teoria). 
  https://regexone.com/
- Validador d'expressions regulars (debug)
  https://regex101.com/


## ExercicisPython Regexp.

Si ja heu llegit tota aquesta pàgina accediu al codi:


## Teoria Tipus patrons regexp.

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

**Exemple:**

Si el fessim en Python, usariem aquestes variables:

txt = "G**AT****AG****AT****AA**CCGG**AT****AG**"
rgx = "A."

matches = ["AT","AG","AT","AA","AT","AG"]
Descartem la G, la T

**2.3.Character classes**

Una "char class" ens permet dir que un caràcter és una de les opcions que hi ha dins.

**Exemples** 

1. Rex. "Hola guap[ao]"
Txt. "Hola guapa"      ✅ MATCH 
Txt. "Hola guapo"      ✅ MATCH 
Txt. "Hola guapi"      ❌ NOT MATCH 
· Els [] són caràcters especials.

1. Hola a tod[ao]s <= Una clase de 2 lletres hi haurà coincidència tant amb la 'a' i la 'o'

2. Parsejar capçaleres d'un fitxer html (h1,h2,h3,h4,h5,h6)
      <h\d> => tots els numeros inclosos el 0
      <h[123456]> => tots excepte el 7,8,9,0.

[exemple1exp]

**2.4. guió - (DASH)** Altre caràcter que es torna especial es el guió - (DASH)

  1. Quant esta entre dos caràcters, crea un rang.
    *exemple* [0-9] => Tots els dígits entre 0 i 9
              [a-z] => El alfabet amb minúscules, anglès (ASCII,UTF-8)
              [a-zA-Z0-9] => Qualsevol caràcter alfanumèric (\w)
  2. Quan es troba al principi o al final de la classe, és un literal normal.

Aquest algoritme només aplica als caràcters ASCII, 127 primers caràcters (les ñ i altres símbols no).

**Exemples**

Rex: [-ab] 
Txt: 18 year-old

![[express2minus.png]](./img/express2minus.png "express2minus.png")
Busca totes les lletres.

![[express2majus.png]](./img/express2majus.png "express2majus.png")
Busca els espais.

![[exemple1exp.png]](./img/exemple1exp.png "exemple1exp.png")

**2.4.caràcter ^ (CARET o NEGACIÓ)** 

Dins d'una clase hi ha un caràcter que es torna especial segons la seva posició dins la clase. Es el caràcter ^ (CARET)

1. Quan és el primer caràcter dins de la classe, nega tota la classe. 
      *exemple* [^S] => Busca paraules amb singular  Qualsevol caràcter que no sigui S, [^aeiou] => Buscaria consonants

2. Quan no és el primer dins la clase, és un literal:
     [a^eiou] => Busca totes les paraules y el caret

**Exemples**

![[rgxcaret1.png]](./img/rgxcaret1.png "rgxcaret1.png")

Retorna tot el que no són lletres. 

![[exemple1exp.png]](./img/exemple1exp.png "exemple1exp.png")

Troba les consonants i altres caràcters que no són vocals (els espais)

**2.5.Cuantificadors** 

Amb aquestex expressions podem detectar moltes vegades un mateix caràcter.

Si s'escriu entre {} indica quantes repeticions hi ha del caràcter anterior.

A nivell de rendiment, tenir en compte que són GREEDY (el contrari de LAZY); per això millor definir bé l'intèrval. 

Sintaxis:
{ num_min , (opt)num_max }

**Exemples**

Rgx:    "a{5}"
Txt:    "aaaaa"

![[rgx_quant1.png]](./img/rgx_quant1.png "rgx_quant1.png")

Cerca una cadena d'ADN que contingui exactament el patró AAA.
- Si té AAAA selecciona les 3 primeres
- Si té menys de 3 A seguides no compta.


{n,m} entre n i m repeticions. Per defecte és GREEDY(ambiciós). Intenta sempre agafar el màxim (consumeix el màxim de l'entrada).

![[cuantificadorsexample1.png]](./img/cuantificadorsexample1.png "cuantificadorsexample1.png")

{n,} entre n i "infinit" repeticions. {,m} com a mínim 0 i màxim m.

![[cuantificadorsexample2.png]](./img/cuantificadorsexample2.png "cuantificadorsexample2.png")

![[cuantificadorsexample3.png]](./img/cuantificadorsexample3.png "cuantificadorsexample3.png")

Tenen dos abreviacions comuns:

- * = {0,} (asterisc)

- + = {1,} (plus) exigeix que almenys hi hagi 1


<em>La abreviatura de l'asterisc és la més coneguda amb diferència; sobretot a l'hora de cercar noms de fitxers.
```bash
*.png
Pt[1-9]*
```
</em>




