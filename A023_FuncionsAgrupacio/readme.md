# Joins utilitzants Pandas

Per aquesta part on farem diferents exercicis, utilitzarem la taula d'alumnes-dual, ja treballada a classe anteriorment


### Datasets per a practicar.
https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/g62h-syeh/data


### Exemples.

* [Desglossar el dataframe amb dos dataframes, un amb els grades i el altre amb el dual](#dividir)
* [Realitzar un join amb els dos dataframes anteriors](#joins)

### Exercicis fets a classe (2022).

* [Merge i altres funcions d'agrupament](joindframes.ipynb)
* [Fitxers CSV Tractaments](joindf_tractaments.py)

### Teoria

* [Agrupacions per valors de columnes](#grouping)
* [TimeSeries](#timeseries)
* [Categoricals](#categoricals)

<a name="dividir"></a>

```python
import numpy as np 
import pandas as pd
import copy
#np --> numerical panda, es una llibreria per a realitzar càlcul numèric
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
datos: dict[list] = {"grade": grades_list,
                   "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
students_frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_grades: pd.DataFrame = copy.deepcopy(students_frame)
#al index li fiquem un nom
students_grades.index.name = "name"
students_grades
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#inplace matxaca el mateix dataFrame
#reset_index passa el index com columna
students_grades.reset_index(inplace=True)
students_grades
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#borrem la columna
students_grades.drop(columns="dual", inplace=True)
students_grades
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_grades.rename(columns={"name":"names"},inplace=True)
students_grades
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>names</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Per ordenar les columnes com vols
students_grades = students_grades.loc[:, ["names","grade"]]
students_grades
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>names</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# SQL Like Joins
# Let's split the dataframe
students_grades: pd.DataFrame = (copy.deepcopy(students_frame)
                                    .reset_index()
                                    .rename(columns={"index":"name"})
                                    .drop(columns="dual")
                                    .loc[:,["name","grade"]]
                                    )
students_grades
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_duals: pd.DataFrame = (copy.deepcopy(students_frame)
                                    .reset_index()
                                    .rename(columns={"index":"name"})
                                    .drop(columns="grade")
                                    .loc[:,["name","dual"]]
                                        )
students_duals
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="joins"></a>


```python
#join with the 2 dataFrame
#how = inner fa intersecció, outer fa union. 
join: pd.DataFrame = pd.merge(students_grades,students_duals, on="name", how="outer")
join
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mary</td>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lucy</td>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Peter</td>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
join.index = join.loc[:,"name"]
join.drop(columns=["name"], inplace=True)
join.index.name = ""
join
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


<a name="grouping"></a>

## Grouping - Agrupacions

Per realitzar el que amb sql coneixem amb la comanda **Group by**. [grouping documentació oficial](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#grouping "grouping documentacion oficial")

```python
import numpy as np 
import pandas as pd
import copy
df3 = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df3
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>0.072135</td>
      <td>-1.829523</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>one</td>
      <td>1.642161</td>
      <td>-0.564049</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>-1.619752</td>
      <td>-0.505827</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>three</td>
      <td>0.134393</td>
      <td>1.396961</td>
    </tr>
    <tr>
      <th>4</th>
      <td>foo</td>
      <td>two</td>
      <td>-0.062482</td>
      <td>1.082786</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>two</td>
      <td>0.365225</td>
      <td>0.687873</td>
    </tr>
    <tr>
      <th>6</th>
      <td>foo</td>
      <td>one</td>
      <td>0.161747</td>
      <td>0.055421</td>
    </tr>
    <tr>
      <th>7</th>
      <td>foo</td>
      <td>three</td>
      <td>-0.180678</td>
      <td>0.533017</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_grouped = df3.groupby("A") #group by a colum(or more)
df3_grouped.groups #mostra les columnes que compleixien per cada valor de l'agrupació
```




>  {'bar': [1, 3, 5], 'foo': [0, 2, 4, 6, 7]}




```python
df3_sum = df3_grouped.sum()
df3_sum #only numeric's columns
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>2.141779</td>
      <td>1.520785</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.629029</td>
      <td>-0.664126</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_groups = df3_grouped.groups

foo_rows = df3_groups['foo']
bar_roows = df3_groups['bar']

df3.loc[foo_rows, "C"]
```




>   0    0.072135
>
>   2   -1.619752
>
>   4   -0.062482
>
>   6    0.161747
>
>   7   -0.180678
>
>   Name: C, dtype: float64




```python
df3.loc[foo_rows, "C"].sum()
```




>  -1.6290291261449736




```python
df3.loc[bar_roows,"D"].sum()
```




>  1.5207848046995553




```python
df3.loc[bar_roows,"D"].max()
```




>   1.3969613630859894




```python
df3_grouped.cumcount()
```




  >  0    0
  >
  >  1    0
  >
  >  2    1
  >
  > 3    1
  >
  > 4    2
  >
  > 5    2
  >
  > 6    3
  >
  > 7    4
  >
  > dtype: int64




<a name="timeseries"></a>

## Time Series

[Consultar la documentació oficial de time series](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#time-series "time series documentacion oficial")



<a name="category"></a>

## Categoricals


Es pot marcar els diferents valors d'una de les columnes, del tipus *Categories*, marcant-la com categories dins la columna, no com a valors.
[categories documentació oficial](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#categoricals "categoricals  documentacion oficial")

*Exemple*

```python
import numpy as np 
import pandas as pd
import copy
#np --> numerical panda, es una llibreria per a realitzar càlcul numèric
#les notes de dawbio amb series
student_list=["John","Mary","Lucy","Peter"]
grades_list = [7,9,8,4]
wants_dual_list = [False,True,False,True]
datos: dict[list] = {"grade": grades_list,
                   "dual": wants_dual_list}
students_frame = pd.DataFrame(
    index=student_list,
    data = datos
)
students_frame
```



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create a new column
students_frame.loc[:,"cat_grade"] = ["Not","Exc","Not","Insuf."]
students_frame.dtypes
```




>    grade         int64
>
>    dual           bool
>
>    cat_grade    object
>
>    dtype: object
>




```python
students_frame.loc[:,"cat_grade"]= students_frame.loc[:,"cat_grade"].astype("category")
students_frame.dtypes
```




>    grade           int64
>
>    dual             bool
>
>    cat_grade    category
>
>    dtype: object
>



```python
students_frame.loc[:,"cat_grade"]
```




>    John        Not
>
>    Mary        Exc
>
>    Lucy        Not
>
>    Peter    Insuf.
>
>    Name: cat_grade, dtype: category
>
>    Categories (3, object): ['Exc', 'Insuf.', 'Not']
>




```python
#reasignar totes les categories 
cat_grades: list[str] = reversed(["Exc","Not","Bien","Sufi","Insuf."])
students_frame.loc[:,"cat_grade"]= students_frame.loc[:,"cat_grade"].cat.set_categories(cat_grades)
#Order by cat_grade and grade
students_frame.sort_values(by=["cat_grade","grade"],ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>grade</th>
      <th>dual</th>
      <th>cat_grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Mary</th>
      <td>9</td>
      <td>True</td>
      <td>Exc</td>
    </tr>
    <tr>
      <th>Lucy</th>
      <td>8</td>
      <td>False</td>
      <td>Not</td>
    </tr>
    <tr>
      <th>John</th>
      <td>7</td>
      <td>False</td>
      <td>Not</td>
    </tr>
    <tr>
      <th>Peter</th>
      <td>4</td>
      <td>True</td>
      <td>Insuf.</td>
    </tr>
  </tbody>
</table>
</div>
