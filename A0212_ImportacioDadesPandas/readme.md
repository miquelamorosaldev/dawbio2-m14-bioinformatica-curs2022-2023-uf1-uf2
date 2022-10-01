# Importar fitxers CSV amb Pandas

### Índex

* [Read - Llegir fitxer CSV](#csvexample)
* [Read - Llegir fitxer CSV Scimago](#scimagoexample)

Podem llegir i escriure diversos tipus de fitxers amb Pandas.
Exemple: [IO tools (text, CSV, HDF5, …)](https://pandas.pydata.org/docs/user_guide/io.html)

Per ara, ens centrarem en la importació del contingut de fitxers CSV a Pandas dataframe.

<a name="csvexample"></a>

### Llegir fitxers CSV.

Podem cercar un dataset en format CSV on fer consultes de prova de les funcions apreses.

- Exemple: [CSV Pokemons](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)
- Exemple: [CSV pacients Oestoporosi](http://www3.uah.es/marcos_marva/CursoSanitaria/practicas/datos/osteoporosis.csv)

```python
# Read Pokedex.
pokedex: pd.DataFrame = pd.read_csv("./pokemon.csv", sep=",")
print(pokedex)
```

Si tot ha anat bé se'ns ha creat un dataframe amb un index autonumèric (del 0 al número de files del fitxer). 
Per a cada camp, Pandas intenta adivinar el tipus que té cada camp (inferència).


### Llegir altres fitxers, iris.data

Ho podem provar en el DataSet de la planta Iris.
És coneguda com a lliri blau a Catalunya.
És una de les plantes que té més tipus d'espècies.

* [Descripció del dataset Iris](https://archive.ics.uci.edu/ml/datasets/Iris)
* [Descarrega iris.data](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/)
* [Video de l'exemple](https://www.youtube.com/watch?v=PvNKKrPE0AI)
* [Exemples Iris documentació Pandas](https://pandas.pydata.org/docs/user_guide/dsintro.html#assigning-new-columns-in-method-chains)



```python
# Read Pokedex.
iris_dataframe: pd.DataFrame = pd.read_csv("./iris.data")
print(iris_dataframe)
```

<a name="scimagoexample"></a>

### Llegir fitxers CSV, Scimago Medicine.

Partirem del fitxer de Scimago que vam descarregar: [scimago-medicine.csv](../A013_ExplotacioFitxersCSV_2022_2023/scimago-medicine.csv "Fitxer Scimago")

```python
# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("../A013_ExplotacioFitxersCSV_2022_2023/scimago-medicine.csv", sep=";")
print(entries)
```


