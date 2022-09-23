# Importar fitxers CSV amb Pandas

### Índex

* [Read - Llegir fitxer CSV](#csvexample)
* [Read - Llegir fitxer CSV Scimago](#scimagoexample)


<a name="csvexample"></a>

### Llegir fitxers CSV.

Podem cercar un dataset en format CSV on fer consultes de prova de les funcions apreses.

Exemple: (CSV Pokemons)[https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6]
Exemple: (CSV pacients Oestoporosi)[http://www3.uah.es/marcos_marva/CursoSanitaria/practicas/datos/osteoporosis.csv]

```python
# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("scimagomedicine.csv", sep=";")
print(entries)
```

### Llegir altres fitxers, iris.data

Ho podem provar en el DataSet de la planta Iris.
És coneguda com a lliri blau a Catalunya.
És una de les plantes que té més tipus d'espècies.

* [https://archive.ics.uci.edu/ml/datasets/Iris] (Descripció del dataset Iris)
* [https://archive.ics.uci.edu/ml/machine-learning-databases/iris/] (Descarrega iris.data)
* [https://www.youtube.com/watch?v=PvNKKrPE0AI] (Video de l'exemple)


<a name="scimagoexample"></a>

### Llegir fitxers CSV, Scimago Medicine.

Partirem del fitxer de Scimago que vam descarregar: [scimago-medicine.csv](./../A013_ExplotacioFitxersCSV_2022_2023/scimago-medicine.csv "Fitxer Scimago")

```python
# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("scimagomedicine.csv", sep=";")
print(entries)
```


