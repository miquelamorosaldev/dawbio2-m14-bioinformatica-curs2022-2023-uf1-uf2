# PANDAS - Ús de màscares i funcions de selecció i edició dades. 

1. Ordenació dataframes
2. Coordenades, cercar per files.
3. Coordenades, cercar per columnes.
4. Coordenades, cercar valors.

**Referències:**

1. [https://pandas.pydata.org/docs/user_guide/10min.html#selection](Doc.Pandas-10min-Selection)


<a name="sort"></a>

## Ordenació dataframes.

#### Ordenació per índex.

```python
#Ordenació per index axis=0 el index de la primera columna, axis=1 ordena els index de la primera columna.
dataframe_sorted = students_frame.sort_index(axis=1, ascending=True)
```
Si l'índex és un text l'ordenarà alfabèticament, si és un número de major a menor (o la inversa si ascending=False)...

#### Ordenació per valors de columnes.

```python
#Ordenació per valors axis=0 columnes i pel camp indicat dins del by.
students_grade_sorted = students_frame.sort_values(by=['grade'], axis=0, ascending=False)
#També és vàlida aquesta instrucció
students_grade_sorted = students_frame.sort_values(['grade'],ascending=False)
```

<a name="coordenades"></a>

## Sistema coordenades.

Amb un daframe, el sistema de coordenades, comença per 0, i la coordenada s'indica primera la fila i després la columna.

**Regla nemotècnica (enfonsar-se i nedar)** 
1. Primer et tires de cap a la fila.
2. Llavors vas nedant fins la columna.

<center>
 <img src="dive-jump.gif" alt="drawing" width="200"/>
</center>

Per a treballar aquests exemples usarem [un fitxer CSV de Pokemons que he descarregat.](./pokedex.csv)

[Font original CSV Pokemons](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)

```python
# Read Pokedex.
pokedex: pd.DataFrame = pd.read_csv("./pokemon.csv", sep=",")
print(pokedex)
```
Si tot ha anat bé se'ns ha creat un dataframe amb un index autonumèric (del 0 al número de files del fitxer). 
Per a cada camp, Pandas intenta adivinar el tipus que té cada camp (inferència).

<a name="loc"></a>

### Guardar tots els valors d'una columna en una Sèrie.

```python
pokemonNames: pd.Series = pokedex['Name']
print(pokemonNames)
```

0                  Bulbasaur
1                    Ivysaur
2                   Venusaur
...
798       HoopaHoopa Unbound
799                Volcanion

### Per a seleccionar alguns camps de cada fila (SELECT <camps>).

```python
print(pokedex.loc[:,['Name','HP']])
```
                    Name   HP
0              Bulbasaur   45
1                Ivysaur   60
...
799            Volcanion   80

 
## Seleccionar diverses files.

 
El requisit es que en los valors de les files cal indicar les de l'index.

```python
print(pokedex.loc[ [152,153] , : ] )
```

 <em> Ampliant </em>
 
<a name="mask"></a>

## Màscares

### Màscares de selecció

```python
# Mask = Objecte que amaga tota la informació que no volem
```

### Màscares de substitució de valors.
```python
# Mask = Objecte que reemplaça els valors dels registres que hem filtrat amb una màscara de selecció.
```

### Màscares per a reemplaçar els valors nulls (np.nan)
```python
# Mask = Objecte que amaga tota la informació que no volem
```

Les practicarem totes en aquest quadern.

<a href="./pandaspokemons.ipynb">pandaspokemons.ipynb</a>

Posteriorment, ho aplicarem al fitxer de Scimago.