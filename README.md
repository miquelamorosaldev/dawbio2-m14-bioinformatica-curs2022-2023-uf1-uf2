# M14 - Bioinformàtica.

* Pablo García.
* Miquel Àngel Amorós

[Professorat de l'Institut Provençana.](https://www.proven.cat/intraweb/index.php)

<br/>
<hr/>

# 🧬 UF2 - Ciències Òmniques. 🧬


## 🖧 Preparació d'un entorn amb Docker 🖧

1. [Sessió 1 - Conceptes previs, instal·lació de Docker i el nostre primer contenidor](./UF2_Sessions1+2_Docker)
2. [Sessió 2 - Creem més contenidors de Docker](./UF2_Sessions2+3_Docker)
3. [Sessió 3 - Part 1. Com treballem i debuguem amb Docker](./UF2_Sessions2%2B3_Docker/readme.md#sessi%C3%B3-3-part-1-com-treballem-amb-docker-)


<br/>
<hr/>

## UF2_A01 - Biopython, per a tractar informació de gens.

#### Introducció ciències Òmniques
3. [Sessió 3 - Part 2. Dogma central de la Biologia Molecular. Investigacions genòmiques del SARSCov2.](./UF2_Sessió3_IntroCiènciesÒmniques1)
4. [Sessió 4 - Part 1. Crispr.](./UF2_Sessió3_IntroCiènciesÒmniques1/readme.md#S4_Part1_Crispr)

### Introducció a BioPython.
1. [Sessió 4 - Part 2. Primers passos amb BioPython](./UF2_Sessions4+5_IntroBioPython/readme.md)


#### Expressions regulars:
* Validador d'expressions regulars https://regex101.com/ 
* Reptes per aprendre expressions regulars. https://regexone.com/

<br/>
<hr/>

## UF2_A02 - Alineament de diversos gens i bases de dades de gens.

<br/>
<hr/>
<hr/>
<br/>

# UF1 - Informàtica mèdica.

## 🐍 A01 - Introducció a Python. 🐍

⌚ Temps previst. 12 hores.

### A011 - Preparació entorn: SO Linux, Python, Anaconda i editors de codi.

⌚ Temps previst: Entre el primer i segon dia.

1. [Sessió 1](./Sessi%C3%B31_PreparacioEntorn "Sessió 1")
	- Important! Com actualitzar de PopOS 20.04 a PopOS 22.04 LTS
	- Creació usb bootable amb iso de PopOS o Ubuntu 22.04 LTS
	- Instal·lació de noves versions de python diferent al de PopOs o Ubuntu
	- Instal·lació Anaconda i comandes bàsiques (cheatsheet)
	- Instal·lació i proves amb JupyterLab (**.ipynb** )
	- Integració IDE VSCode.

### A012 - Repàs funcionalitats bàsiques de Python.

⌚ Temps previst. (2 hores) amb el més important.
La resta de recursos queden com a referència. 
Pressuposem que ja s'han treballat les funcions, bones pràctiques i estructures bàsiques de Python, i aquí en fem un repàs.

1. [Repàs Python, part 1](./A012_RepasPythonPart1 "Repàs Python, part 1")
	- Introducció Bàsica a Python 
		- print
		- bucles
		- llistes, list comprension
		- diccionaris
		- Tuples
		- Slices
		- Conjunts (Sets)
		- Ajuda
3. [Txuletari Python](./A012_Cheatsheet "Txuletari Python")
	- Txuletari propi de comandes bàsiques python per Llistes i Diccionaris.
4. [ExercicisBasicsPython](./A012_ExercicisBasicsPython "ExercicisBasicsPython")
	- Exercicis programació amb python (bucles, llistes, set, etc)
5. [Repàs Python, part 2](./A012_RepasPythonPart2 "Repàs Python, part 2")
	- Llegir fitxers CSV amb iteradors
	- Instrucció Yields
	- Prog. Funcional : Map i filter
6. [Com fer còpia seguratat amb RSYNC](./A012_ConsellsGit "ConsellsGit 5")

#### Activitat A012 - Repassem Python amb Jupyter Notebook.

**[A012-Exercicis-JupyterNb-Sessio1](./A012_ExercicisBasicsPython/a012_exercicis_1asessio.md "A012-Exercicis-JupyterNb-Sessio1")**

**[A012-SolucionsExercicis-JupyterNb-Sessio1](./A012_ExercicisBasicsPython/A012_SolucionsExercicisBasicsPython.ipynb)**

<hr/>

### A013 - Exercicis explotació de dades amb Python.


**[A013-Exercicis Fitxes CSV Scymago (2022-2023)](./A013_ExplotacioFitxersCSV_2022_2023/readme.md)**
	- Llegir nou fitxer CSV i exercicis d'explotació de dades.
  
[Fitxes CSV Scymago (2021-2022)](https://github.com/mikibardaji/M15UF2_2021-22/blob/main/Sessi%C3%B35_ExplotacioFitxersCSV/readme.md)
	- Llegir fitxers CSV i exercicis d'explotació de dades fets, anys anteriors.
  
<hr/>
<hr/>

## 🐼 A02 - Tractament de dades biomèdiques amb Python i Pandas. 🐼
	
⌚ Temps previst. 21 hores.

### A021 - Introducció a les estructures de la libreria Pandas.

#### Introducció a Pandas. Sessions 4 i 5.
1. [Estructures Pandas : Series , Dataframes](./A021_EstructuresPandas "EstructuresPandas:Series,Dataframes")
	- Estructures bàsiques pandas.
		* Sèries
		* Dataframe
		* DTYPES
	- Funcions bàsiques pandas.
		* HEAD, TAIL
		* SORT_INDEX
		* SORT_VALUES
		* LOC, ILOC
		* MASKS
2. **[Solució Exercicis Sessió 5, introducció als Dataframes.](./A021_EstructuresPandas/exercicisSessio5dataframes.py)**
	
3. [Com importar un fitxer de dades a un Dataframe de Pandas.](./A0212_ImportacioDadesPandas/readme.md)

### A022 - Ús de màscares i funcions de selecció i edició dades. 

4. [Repàs ús de màscares, selecció i edició de màscares.](./A021_EstructuresPandas/mascares_readme.md)

**[Exercicis solucionats Pokemons](./A021_EstructuresPandas/pandaspokemons.ipynb)**

#### Apliquem Pandas a la BBDD de Scimago. Sessions 6 i 7
5. [Apliquem Pandas a la BBDD de Scimago.](./A022_Consultes_PandasScimago "Sessió 9")
	- Inici explotació fitxer Scimago amb Pandas (es fà a la sessió 12)
	- Seleccionar diferents registres a partir d'una condició d'un camp
	- Detecció Valors na, eliminació de registres amb valors incoherents.
  
**Dins del mateix fitxer, introduïm aquests conceptes:**
	
	- Funcions aply, map, mapapply
	
	- Afegir noves columnes **(columnes calculades)**
	- Canvi d'ordre dels camps. 

### A023 - Funcions d'agrupació i fusió de dades. Sessió 8.

5. [Teoria i exemples. Merge and Join Pandas](./A023_FuncionsAgrupacio "Sessió 8")

6. [Practiquem funcions d'agrupació, fitxers evolució i tractament pacients CSV](./A023_FuncionsAgrupacio/joindf_tractaments.py)

7. [Practiquem funcions d'agrupació, gràfiques i columnes calculades, fitxer pacients random](./A023_FuncionsAgrupacio/pd_grups_pacients_random.ipynb)


### A024 - Creació de gràfics amb Matplotlib i Pandas. Sessió 9.

8. [Exemples de Gràfiques amb Matplotlib i Pandas](./A024_Grafiques "Sessió 9")

9. [Exercicis de SCImago amb Pandas i gràfics Matplotlib](./A025_ScimagoPandasPlots/ "Sessió 10")

## Sessions 10 - 14. Pràctica, simulacre i prova de Pandas.

### A025 - Recursos per a realitzar una pràctica Pt1.

**[Exemple codi de la pràctica Pt1, fet pels professors.](./A026_PracticaExemple_Covid19Variants/ "Sessió 12")**

### Recull de bancs de dades mèdiques obertes per a fer pràctiques.

* [HealthData, EEUU](https://healthdata.gov/browse?tags=hhs+covid-19)
* [Casos SIDA EEUU.](https://wonder.cdc.gov/controller/datarequest/D14)
* [NCBI, USA](https://www.ncbi.nlm.nih.gov/datasets/)
* [World Health Organization/OMS](https://www.who.int/data/collections)
* [Dades obertes organitzacions mundials com la UNESCO](https://data.un.org/)
* [Unicef](https://data.unicef.org/dv_index/?q=)
* [Dades de salut i altres, Govern Espanya](https://datos.gob.es/en/catalogo?theme_id=salud)
* [Nou portal dades malalties víriques Catalunya](https://sivic.salut.gencat.cat/dades_obertes)
* [Portal dades Covid19 a Catalunya, inactiu des del juliol del 2022](https://dadescovid.cat/descarregues)
* [Dades obertes Institut Estadística Catalunya](https://www.idescat.cat/dades/)
* [Cens persones desaparegudes durant la Guerra Civil, Gencat](https://analisi.transparenciacatalunya.cat/Legislaci-just-cia/Cens-de-persones-desaparegudes-durant-la-Guerra-Ci/u2ix-2jr6)

#### Com transformar bancs de dades en format Tidy.

    1. Cada fila és una observació.
    2. Cada columna és una variable.
    3. Cada cel·la conté només una dada.
       
- [Tutorial de com convertir datasets a format Tidy en Pandas](https://www.jeannicholashould.com/tidy-data-in-python.html)

- [Codi dels exemples usats](https://github.com/nickhould/tidy-data-python)

#### Altres tutorials amb exemples resolts.
- [Kaggle, molt ben resumit tot el que hem vist](https://www.kaggle.com/learn/pandas)
- [AprendeconAlf, exercicis 7 i 8 molt interessants](https://aprendeconalf.es/docencia/python/ejercicios/pandas/)

### Simulacre Pandas amb solucions, any 2021-2022
- [Solucions Prova Pandas 2021-2022](https://github.com/mikibardaji/M15UF2_2021-22)

## Solucions del Simulacre de prova de Pandas, any 2022-2023.

- [Carpeta Codis Solucions, revisats el 04/11/2022](https://github.com/miquelamorosaldev/pandas-sim-solutions)

## Solucions de la prova (Pròximament) 

<hr/>
<hr/>

## 📈 A03 - Estadística 📈
 
⌚ Temps previst. 18 hores.

### Sessió 15. [Repàs estadística](./Sessió15_Estadistica)	

### Sessió 16. [Exercicis estadística Dades Covid](./Sessió16_EstadisticaDadesCovid)	

Amb dades de dadescovid.cat, veurem les diferents variables descriptores Estadístiques.

	- Mitjana
	- Moda
	- Mediana
	- Quartils
	- Desviació típica.
	- Gràfics Plotbox

### Sessió 17. Nous gràfics i exercicis. 

[Recta de regressió, augment temperatures a Londres i Barcelona](https://github.com/miquelamorosaldev/dawbio2-m14-bioinformatica-uf1-uf2/blob/main/Sessi%C3%B315_Estadistica/Estadistica_Rectes_Regressi%C3%B3/exercicis-metereologia.ipynb)	

#### [Actualització apunts estadística](./Sessió15_Estadistica)	

Nous conceptes introduïts.

	- Diagrames de punts (scatter) i rectes de regressió (comparar 2 variables).
	- Gràfic distribució normal
	- Mapes de calor (heatmap).
	
Creació de mapes del món (per a què investigueu):
* https://www.python-graph-gallery.com/map-read-geojson-with-python-geopandas
* https://plotly.com/python/mapbox-county-choropleth/
	     

<em>No són la única opció, també es poden fer gràfics interactius amb [3dJS](https://d3js.org) </em>

### Sessió 18. [Jornades IA a la FP, 2020. Video i Codi font](https://github.com/miquelamorosaldev/dawbio2-m14-bioinformatica-uf1-uf2/blob/main/A01_JornadesIAXFP_WineQuality/Wine_Quality_Amor%C3%B3s_2022.ipynb)

#### Recursos per entendre millor com usar rectes de regressió aplicades a fer prediccions i a Machine Learning.

**Gràcies a aquests recursos podem fer prediccions. (estadistica inferencial).** 

- https://naps.com.mx/blog/3-ejemplos-explicados-de-machine-learning-en-python/
- https://www.iartificial.net/arboles-de-decision-con-ejemplos-en-python/

### Sessions 19-22. Pràctica d'estadística, simulacre i prova final.

Punts a tractar.

	- Revisem un exemple de pràctica (sobretot els gràfics)
	- Enumero els recursos vistos i organitzats d'estadística.
	- Recursos rectes de regressió i ML.
	- Introducció a com insta·lar les llibreries de mapes del món.
	- Consells per resoldre la pràctica.
	- Com tractar els outliers.

Recursos útils:

[Valors outliers temperatures a Barcelona i Londres](./Sessió15_Estadistica/Estadistica_Rectes_Regressió/exercicis-metereologia.ipynb)
[Codi font mapa atur als EEUU](./Sessió15_Estadistica/Estadistica_Rectes_Regressió/exercicis-metereologia.ipynb)

<br/>
<hr/>
<br/>

### Agraïments.

Gràcies a tot el professorat de l'institut que ha fet possible tirar endavant el cicle de DAW, perfil especialitzat en Bioinformàtica. 

En aquest mòdul concret, agraeixo al Pablo Garcia i el Miquel Àngel Bardají, que han publicat de forma resumida projectes de programació en Python aplicats a la bioinformàtica.

Per últim, i el més important, als i les alumnes de l'institut per demostrar cada dia la seva iniciativa, saber fer i esperit crític. 
