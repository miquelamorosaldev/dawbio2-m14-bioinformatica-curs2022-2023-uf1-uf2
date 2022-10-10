# M14 - Bioinformàtica.

* Pablo García.
* Miquel Àngel Amorós

[Professorat de l'Institut Provençana.](https://www.proven.cat/intraweb/index.php)

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
	- **[Solució Exercicis Sessió 5, introducció als Dataframes.](./A021_EstructuresPandas/exercicisSessio5dataframes.py)**

### A022 - Ús de màscares i funcions de selecció i edició dades. 

2. [Com importar un fitxer de dades a un Dataframe de Pandas.](./A0212_ImportacioDadesPandas/readme.md)

3. [Repàs ús de màscares, selecció i edició de màscares.](./A021_EstructuresPandas/mascares_readme.md)

#### Apliquem Pandas a la BBDD de Scimago. Sessions 6 i 7
4. [Apliquem Pandas a la BBDD de Scimago.](./A022_Consultes_PandasScimago "Sessió 9")
	- Inici explotació fitxer Scimago amb Pandas (es fà a la sessió 12)
	- Seleccionar diferents registres a partir d'una condició d'un camp
	- Detecció Valors na, eliminació de registres amb valors incoherents.
  
**Dins del mateix fitxer, introduïm aquests conceptes:**
	- Funcions aply, map, mapapply
	- Afegir noves columnes, canvi d'ordre 

### A023 - Funcions d'agrupació i fusió de dades. Sessió 8.

5. [Merge and Join Pandas](./A023_FuncionsAgrupacio "Sessió 8")

Practiquem funcions d'agrupació.


### A024 - Creació de gràfics amb Matplotlib i Pandas. Sessió 9.

6. [Gràfiques amb Matplotlib i Pandas](./A024_Grafiques "Sessió 9")

<em> 🚧 Actualitzant 🚧 </em>

Pendent mirar aquest banc de dades, casos SIDA EEUU.
https://wonder.cdc.gov/controller/datarequest/D14

Organització de què és cada dada.
https://wonder.cdc.gov/wonder/help/aids.html

<hr/>
<hr/>

## 📈 A03 - Estadística 📈
 
⌚ Temps previst. 18 hores.

15. [Repàs estadística](./Sessió15_Estadistica)	

<em> 🚧 Actualitzant 🚧 </em>

16. [Exercicis estadística Dades Covid](./Sessió16_EstadisticaDadesCovid)	

Amb dades de dadescovid.cat, veurem les diferents variables descriptores Estadístiques	
	- Mitjana
	- Moda
	- Mediana
	- Quartils 
	- 
<em> 🚧 Actualitzant 🚧 </em>

<hr/>


# 🧬 UF2 - Ciències Òmniques. 🧬

<em> 🚧 Pròximament 🚧 </em>


<hr/>
<hr/>

### Agraïments.

Gràcies a tot el professorat de l'institut que ha fet possible tirar endavant el cicle de DAW, perfil especialitzat en Bioinformàtica. 

En aquest mòdul concret, agraeixo al Pablo Garcia i el Miquel Àngel Bardají, que han publicat de forma resumida projectes de programació en Python aplicats a la bioinformàtica.

Per últim, i el més important, als i les alumnes de l'institut per demostrar cada dia la seva iniciativa, saber fer i esperit crític. 
