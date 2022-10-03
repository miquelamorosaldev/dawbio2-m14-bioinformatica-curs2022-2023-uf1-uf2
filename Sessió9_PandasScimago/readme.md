# Fitxer Scimago amb Pandas

### Exercicis

* [Read - Llegir fitxer Scimago](#scimagoexample)
* [Seleccionar registres amb h index superior a 450](#hindex450)
* [Canviar valors - Canviar el h_index de tots els registres que el tenen inferior a 750](#hindex750)
* [Canviar els valors a h_index negatiu sempre i quant el h_index sigui inferior a 750](#hindex750negatius)
* [Posar tots els Publisher, que actualment es troben a null, ficar-los a np.nan.](#publishernan1)
* [NAN - Tots els registres que tenen publisher a null, pasar-los a Nan](#publishernan)
* [Series - Canviar el valor als objectes d'una serie que conté nan](#seriesvalor)
* [Les instruccions MAP, APPLY, APPLYMAP](#map)
* [Afegir columnes a un dataframe existent](#novacolumna)
* [Canviar el ordre de les columnes d'un dataframe](#orden)




<a name="scimagoexample"></a>

Partirem del fitxer descarregat [scimago-medicine.csv](scimago-medicine.csv "Fitxer Scimago")

```python
# Read scimago ranking
entries: pd.DataFrame = pd.read_csv("scimagomedicine.csv", sep=";")
entries
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>28773</td>
      <td>Ca-A Cancer Journal for Clinicians</td>
      <td>journal</td>
      <td>15424863, 00079235</td>
      <td>62,937</td>
      <td>Q1</td>
      <td>168</td>
      <td>47</td>
      <td>119</td>
      <td>3452</td>
      <td>15499</td>
      <td>80</td>
      <td>126,34</td>
      <td>73,45</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Wiley-Blackwell</td>
      <td>1950-2020</td>
      <td>Hematology (Q1); Oncology (Q1)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>19434</td>
      <td>MMWR Recommendations and Reports</td>
      <td>journal</td>
      <td>10575987, 15458601</td>
      <td>40,949</td>
      <td>Q1</td>
      <td>143</td>
      <td>10</td>
      <td>9</td>
      <td>1292</td>
      <td>492</td>
      <td>9</td>
      <td>50,00</td>
      <td>129,20</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>1990-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>18991</td>
      <td>Nature Reviews Genetics</td>
      <td>journal</td>
      <td>14710056, 14710064</td>
      <td>26,214</td>
      <td>Q1</td>
      <td>365</td>
      <td>106</td>
      <td>325</td>
      <td>7332</td>
      <td>6348</td>
      <td>149</td>
      <td>21,22</td>
      <td>69,17</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2000-2020</td>
      <td>Genetics (Q1); Genetics (clinical) (Q1); Molec...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>21318</td>
      <td>Nature Reviews Immunology</td>
      <td>journal</td>
      <td>14741741, 14741733</td>
      <td>20,529</td>
      <td>Q1</td>
      <td>390</td>
      <td>230</td>
      <td>436</td>
      <td>9421</td>
      <td>8200</td>
      <td>202</td>
      <td>17,33</td>
      <td>40,96</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2001-2020</td>
      <td>Immunology (Q1); Immunology and Allergy (Q1); ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>71056</td>
      <td>MMWR. Surveillance summaries : Morbidity and m...</td>
      <td>journal</td>
      <td>15458636, 15460738</td>
      <td>19,961</td>
      <td>Q1</td>
      <td>100</td>
      <td>32</td>
      <td>48</td>
      <td>499</td>
      <td>2235</td>
      <td>48</td>
      <td>57,77</td>
      <td>15,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>2002-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>7120</th>
      <td>7121</td>
      <td>25412</td>
      <td>Zhonghua kou qiang yi xue za zhi = Zhonghua ko...</td>
      <td>journal</td>
      <td>10020098</td>
      <td>NaN</td>
      <td>-</td>
      <td>14</td>
      <td>150</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1987-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7121</th>
      <td>7122</td>
      <td>21485</td>
      <td>Zhonghua liu xing bing xue za zhi = Zhonghua l...</td>
      <td>journal</td>
      <td>02546450</td>
      <td>NaN</td>
      <td>-</td>
      <td>31</td>
      <td>292</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1982-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7122</th>
      <td>7123</td>
      <td>26726</td>
      <td>Zhonghua nei ke za zhi [Chinese journal of int...</td>
      <td>journal</td>
      <td>05781426</td>
      <td>NaN</td>
      <td>-</td>
      <td>18</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1957-1959, 1979-1997, 1999-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7123</th>
      <td>7124</td>
      <td>19324</td>
      <td>Zhonghua wai ke za zhi [Chinese journal of sur...</td>
      <td>journal</td>
      <td>05295815</td>
      <td>NaN</td>
      <td>-</td>
      <td>16</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>0,00</td>
      <td>China</td>
      <td>Asiatic Region</td>
      <td>Zhonghua Yixuehui Zazhishe</td>
      <td>1957, 1959-1964, 1979-2016, 2020</td>
      <td>Medicine (miscellaneous)</td>
    </tr>
    <tr>
      <th>7124</th>
      <td>7125</td>
      <td>20906</td>
      <td>Zhurnal Mikrobiologii Epidemiologii i Immunobi...</td>
      <td>journal</td>
      <td>03729311</td>
      <td>NaN</td>
      <td>-</td>
      <td>12</td>
      <td>53</td>
      <td>0</td>
      <td>1264</td>
      <td>0</td>
      <td>0</td>
      <td>0,00</td>
      <td>23,85</td>
      <td>Russian Federation</td>
      <td>Eastern Europe</td>
      <td>Izdatel'stvo S-Info</td>
      <td>1945-1947, 1954-2016</td>
      <td>Immunology; Medicine (miscellaneous); Microbio...</td>
    </tr>
  </tbody>
</table>
<p>7125 rows × 20 columns</p>
</div>



*Mostra totes les files, però sol la seva columna Rank*

```python
entries.loc[:,"Rank"]
```




  >  0          1
  >
  >  1          2
  >
  >  2          3
  >
  >  3          4
  >
  > 4          5
  >
  >           ... 
  >
  > 7120    7121
  >
  > 7121    7122
  >
  > 7122    7123
  > 
  > 7123    7124
  >
  > 7124    7125
  >
  > Name: Rank, Length: 7125, dtype: int64


*Mostra el tipus de dades de totes les files, però sol la seva columna Rank*

```python
entries.loc[:,"Rank"].dtype
```



>
>    dtype('int64')
>




```python
entries.dtypes
```




 >   Rank                       int64
 >   
 >  Sourceid                   int64
 >  
 >  Title                     object
 >  
 >  Type                      object
 >  
 >  Issn                      object
 >  
 >  SJR                       object
 >  
 >  SJR Best Quartile         object
 >  
 >  H index                    int64
 >  
 >  Total Docs. (2020)         int64
 >  
 >  Total Docs. (3years)       int64
 >  
 >  Total Refs.                int64
 >  
 >  Total Cites (3years)       int64
 >  
 >  Citable Docs. (3years)     int64
 >  
 >  Cites / Doc. (2years)     object
 >  
 >  Ref. / Doc.               object
 >  
 >  Country                   object
 >  
 >  Region                    object
 >  
 >  Publisher                 object
 >  
 >  Coverage                  object
 >  
 >  Categories                object
 >  
 >  dtype: object




```python
#Mostra els index de cada fila
entries.index
```




 >   RangeIndex(start=0, stop=7125, step=1)
 >


<a name="hindex450"></a>

Podem fer filtres de files a partir del contingut d'alguna columna.
*Exemple:* Mostrar totes les entries, el qual el seu **H index** es superior a 450

```python
#seleccionar i mostrar les entries amb H index superior
entries_high = entries.loc[:,"H index"] >= 450
entries_ok = entries.loc[entries_high,:]
entries_ok
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>15847</td>
      <td>New England Journal of Medicine</td>
      <td>journal</td>
      <td>00284793, 15334406</td>
      <td>19,889</td>
      <td>Q1</td>
      <td>1030</td>
      <td>1671</td>
      <td>4312</td>
      <td>15715</td>
      <td>82469</td>
      <td>1842</td>
      <td>19,08</td>
      <td>9,40</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Massachussetts Medical Society</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>15819</td>
      <td>Nature Medicine</td>
      <td>journal</td>
      <td>1546170X, 10788956</td>
      <td>19,536</td>
      <td>Q1</td>
      <td>547</td>
      <td>452</td>
      <td>953</td>
      <td>10601</td>
      <td>22548</td>
      <td>664</td>
      <td>23,52</td>
      <td>23,45</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>1995-2020</td>
      <td>Biochemistry, Genetics and Molecular Biology (...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>16590</td>
      <td>Lancet, The</td>
      <td>journal</td>
      <td>01406736, 1474547X</td>
      <td>13,103</td>
      <td>Q1</td>
      <td>762</td>
      <td>1488</td>
      <td>4593</td>
      <td>16580</td>
      <td>45581</td>
      <td>1227</td>
      <td>9,45</td>
      <td>11,14</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Elsevier Ltd.</td>
      <td>1823-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>29949</td>
      <td>Journal of Clinical Oncology</td>
      <td>journal</td>
      <td>15277755, 0732183X</td>
      <td>10,482</td>
      <td>Q1</td>
      <td>548</td>
      <td>583</td>
      <td>1890</td>
      <td>17448</td>
      <td>23642</td>
      <td>1221</td>
      <td>12,29</td>
      <td>29,93</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Clinical Oncology</td>
      <td>1983-2020</td>
      <td>Cancer Research (Q1); Medicine (miscellaneous)...</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>22581</td>
      <td>Circulation</td>
      <td>journal</td>
      <td>00097322, 15244539</td>
      <td>7,795</td>
      <td>Q1</td>
      <td>607</td>
      <td>778</td>
      <td>2685</td>
      <td>22242</td>
      <td>26532</td>
      <td>1702</td>
      <td>9,48</td>
      <td>28,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Lippincott Williams and Wilkins Ltd.</td>
      <td>1950-2020</td>
      <td>Cardiology and Cardiovascular Medicine (Q1); P...</td>
    </tr>
    <tr>
      <th>69</th>
      <td>70</td>
      <td>15870</td>
      <td>Journal of Clinical Investigation</td>
      <td>journal</td>
      <td>00219738, 15588238</td>
      <td>6,278</td>
      <td>Q1</td>
      <td>488</td>
      <td>611</td>
      <td>1446</td>
      <td>32961</td>
      <td>16569</td>
      <td>1418</td>
      <td>10,27</td>
      <td>53,95</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>The American Society for Clinical Investigation</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>89</th>
      <td>90</td>
      <td>25454</td>
      <td>Blood</td>
      <td>journal</td>
      <td>15280020, 00064971</td>
      <td>5,515</td>
      <td>Q1</td>
      <td>465</td>
      <td>853</td>
      <td>2755</td>
      <td>26498</td>
      <td>22558</td>
      <td>2041</td>
      <td>7,41</td>
      <td>31,06</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Hematology</td>
      <td>1946-2020</td>
      <td>Biochemistry (Q1); Cell Biology (Q1); Hematolo...</td>
    </tr>
    <tr>
      <th>113</th>
      <td>114</td>
      <td>85291</td>
      <td>JAMA - Journal of the American Medical Associa...</td>
      <td>journal</td>
      <td>15383598, 00987484, 00029955</td>
      <td>4,688</td>
      <td>Q1</td>
      <td>680</td>
      <td>1793</td>
      <td>5000</td>
      <td>14369</td>
      <td>30016</td>
      <td>2627</td>
      <td>5,46</td>
      <td>8,01</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Medical Association</td>
      <td>1883-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
  </tbody>
</table>
</div>




```python
#ensenyar les 5 primeres
#Ordenació per valors axis=0 columnes 
entries_top = entries_ok.sort_values(by=['H index'], 
                                    axis=0, 
                                    ascending=False)
entries_top.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>15847</td>
      <td>New England Journal of Medicine</td>
      <td>journal</td>
      <td>00284793, 15334406</td>
      <td>19,889</td>
      <td>Q1</td>
      <td>1030</td>
      <td>1671</td>
      <td>4312</td>
      <td>15715</td>
      <td>82469</td>
      <td>1842</td>
      <td>19,08</td>
      <td>9,40</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Massachussetts Medical Society</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>16590</td>
      <td>Lancet, The</td>
      <td>journal</td>
      <td>01406736, 1474547X</td>
      <td>13,103</td>
      <td>Q1</td>
      <td>762</td>
      <td>1488</td>
      <td>4593</td>
      <td>16580</td>
      <td>45581</td>
      <td>1227</td>
      <td>9,45</td>
      <td>11,14</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Elsevier Ltd.</td>
      <td>1823-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>113</th>
      <td>114</td>
      <td>85291</td>
      <td>JAMA - Journal of the American Medical Associa...</td>
      <td>journal</td>
      <td>15383598, 00987484, 00029955</td>
      <td>4,688</td>
      <td>Q1</td>
      <td>680</td>
      <td>1793</td>
      <td>5000</td>
      <td>14369</td>
      <td>30016</td>
      <td>2627</td>
      <td>5,46</td>
      <td>8,01</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Medical Association</td>
      <td>1883-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>22581</td>
      <td>Circulation</td>
      <td>journal</td>
      <td>00097322, 15244539</td>
      <td>7,795</td>
      <td>Q1</td>
      <td>607</td>
      <td>778</td>
      <td>2685</td>
      <td>22242</td>
      <td>26532</td>
      <td>1702</td>
      <td>9,48</td>
      <td>28,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Lippincott Williams and Wilkins Ltd.</td>
      <td>1950-2020</td>
      <td>Cardiology and Cardiovascular Medicine (Q1); P...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>29949</td>
      <td>Journal of Clinical Oncology</td>
      <td>journal</td>
      <td>15277755, 0732183X</td>
      <td>10,482</td>
      <td>Q1</td>
      <td>548</td>
      <td>583</td>
      <td>1890</td>
      <td>17448</td>
      <td>23642</td>
      <td>1221</td>
      <td>12,29</td>
      <td>29,93</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>American Society of Clinical Oncology</td>
      <td>1983-2020</td>
      <td>Cancer Research (Q1); Medicine (miscellaneous)...</td>
    </tr>
  </tbody>
</table>
</div>


<a name="hindex750"></a>

Canviar totes les entrades inferiors a 750 a h_index igual a 0.

```python
import copy
#canviar totes les entrades menors de 750 a h_index negatiu
entries2 = copy.deepcopy(entries)


bad_entries_mask = (entries2.loc[:,"H index"] < 750)
entries2.loc[bad_entries_mask,"H index"] = 0;
entries2.sort_values(by=["H index"], 
                          axis=0, 
                          ascending=False).head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>15847</td>
      <td>New England Journal of Medicine</td>
      <td>journal</td>
      <td>00284793, 15334406</td>
      <td>19,889</td>
      <td>Q1</td>
      <td>1030</td>
      <td>1671</td>
      <td>4312</td>
      <td>15715</td>
      <td>82469</td>
      <td>1842</td>
      <td>19,08</td>
      <td>9,40</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Massachussetts Medical Society</td>
      <td>1945-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>16590</td>
      <td>Lancet, The</td>
      <td>journal</td>
      <td>01406736, 1474547X</td>
      <td>13,103</td>
      <td>Q1</td>
      <td>762</td>
      <td>1488</td>
      <td>4593</td>
      <td>16580</td>
      <td>45581</td>
      <td>1227</td>
      <td>9,45</td>
      <td>11,14</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Elsevier Ltd.</td>
      <td>1823-2020</td>
      <td>Medicine (miscellaneous) (Q1)</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>28773</td>
      <td>Ca-A Cancer Journal for Clinicians</td>
      <td>journal</td>
      <td>15424863, 00079235</td>
      <td>62,937</td>
      <td>Q1</td>
      <td>0</td>
      <td>47</td>
      <td>119</td>
      <td>3452</td>
      <td>15499</td>
      <td>80</td>
      <td>126,34</td>
      <td>73,45</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Wiley-Blackwell</td>
      <td>1950-2020</td>
      <td>Hematology (Q1); Oncology (Q1)</td>
    </tr>
    <tr>
      <th>4747</th>
      <td>4748</td>
      <td>21100896985</td>
      <td>2018 IEEE Biomedical Circuits and Systems Conf...</td>
      <td>conference and proceedings</td>
      <td>-</td>
      <td>0,266</td>
      <td>-</td>
      <td>0</td>
      <td>0</td>
      <td>178</td>
      <td>0</td>
      <td>216</td>
      <td>177</td>
      <td>1,21</td>
      <td>0,00</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>NaN</td>
      <td>2018</td>
      <td>Biomedical Engineering; Electrical and Electro...</td>
    </tr>
    <tr>
      <th>4758</th>
      <td>4759</td>
      <td>21100901159</td>
      <td>International Journal of Child Care and Educat...</td>
      <td>journal</td>
      <td>19765681, 22886729</td>
      <td>0,265</td>
      <td>Q3</td>
      <td>0</td>
      <td>11</td>
      <td>40</td>
      <td>419</td>
      <td>42</td>
      <td>40</td>
      <td>0,77</td>
      <td>38,09</td>
      <td>Singapore</td>
      <td>Asiatic Region</td>
      <td>Springer Open</td>
      <td>2007-2020</td>
      <td>Sociology and Political Science (Q2); Communit...</td>
    </tr>
  </tbody>
</table>
</div>

<a name="hindex750negatius"></a>

Ficar el valor de les les entrades a h_index negatiu, si son menors de 750...


```python
#canviar el valor de les entrades amb el **H index** menor a 750,  al seu valor amb negatiu.
entries3 = copy.deepcopy(entries)

bad_entries_mask = (entries3.loc[:,"H index"] < 350)
entries3.loc[bad_entries_mask,"H index"] = entries3.loc[bad_entries_mask,"H index"]*(-1);
entries3.sort_values(by=["H index"], 
                                                   axis=0, 
                                                   ascending=False)
entries3.head(5)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
      <th>Sourceid</th>
      <th>Title</th>
      <th>Type</th>
      <th>Issn</th>
      <th>SJR</th>
      <th>SJR Best Quartile</th>
      <th>H index</th>
      <th>Total Docs. (2020)</th>
      <th>Total Docs. (3years)</th>
      <th>Total Refs.</th>
      <th>Total Cites (3years)</th>
      <th>Citable Docs. (3years)</th>
      <th>Cites / Doc. (2years)</th>
      <th>Ref. / Doc.</th>
      <th>Country</th>
      <th>Region</th>
      <th>Publisher</th>
      <th>Coverage</th>
      <th>Categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>28773</td>
      <td>Ca-A Cancer Journal for Clinicians</td>
      <td>journal</td>
      <td>15424863, 00079235</td>
      <td>62,937</td>
      <td>Q1</td>
      <td>-168</td>
      <td>47</td>
      <td>119</td>
      <td>3452</td>
      <td>15499</td>
      <td>80</td>
      <td>126,34</td>
      <td>73,45</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Wiley-Blackwell</td>
      <td>1950-2020</td>
      <td>Hematology (Q1); Oncology (Q1)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>19434</td>
      <td>MMWR Recommendations and Reports</td>
      <td>journal</td>
      <td>10575987, 15458601</td>
      <td>40,949</td>
      <td>Q1</td>
      <td>-143</td>
      <td>10</td>
      <td>9</td>
      <td>1292</td>
      <td>492</td>
      <td>9</td>
      <td>50,00</td>
      <td>129,20</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>1990-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>18991</td>
      <td>Nature Reviews Genetics</td>
      <td>journal</td>
      <td>14710056, 14710064</td>
      <td>26,214</td>
      <td>Q1</td>
      <td>365</td>
      <td>106</td>
      <td>325</td>
      <td>7332</td>
      <td>6348</td>
      <td>149</td>
      <td>21,22</td>
      <td>69,17</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2000-2020</td>
      <td>Genetics (Q1); Genetics (clinical) (Q1); Molec...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>21318</td>
      <td>Nature Reviews Immunology</td>
      <td>journal</td>
      <td>14741741, 14741733</td>
      <td>20,529</td>
      <td>Q1</td>
      <td>390</td>
      <td>230</td>
      <td>436</td>
      <td>9421</td>
      <td>8200</td>
      <td>202</td>
      <td>17,33</td>
      <td>40,96</td>
      <td>United Kingdom</td>
      <td>Western Europe</td>
      <td>Nature Publishing Group</td>
      <td>2001-2020</td>
      <td>Immunology (Q1); Immunology and Allergy (Q1); ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>71056</td>
      <td>MMWR. Surveillance summaries : Morbidity and m...</td>
      <td>journal</td>
      <td>15458636, 15460738</td>
      <td>19,961</td>
      <td>Q1</td>
      <td>-100</td>
      <td>32</td>
      <td>48</td>
      <td>499</td>
      <td>2235</td>
      <td>48</td>
      <td>57,77</td>
      <td>15,59</td>
      <td>United States</td>
      <td>Northern America</td>
      <td>Centers for Disease Control and Prevention (CDC)</td>
      <td>2002-2020</td>
      <td>Epidemiology (Q1); Health Information Manageme...</td>
    </tr>
  </tbody>
</table>
</div>


<a name="publishernan1"></a>

Modificar el valor de tots els Publisher, que actualment esta informat a null, passar-los a np.nan.

```python
# Modificar el valor de tots els Publisher, que actualment esta informat a null, passar-los a np.nan.
# Clean NAs

entries4 = copy.deepcopy(entries)

# Pas 1. Cercar valors nuls amb la màscara.
print("Valors Publisher nuls o buits ??")

entries4.loc[:,"Publisher"].isnull().value_counts()
null_publisher_mask = entries4.loc[:,"Publisher"].isnull()

# Pas 2. Comprovem el resultat de la màscara. 
# En general: df.loc(MASK,FIELD)
print(entries4.loc[null_publisher_mask,"Publisher"] )
```

Valors Publisher nuls o buits ??
62      NaN
485     NaN
662     NaN
1481    NaN
1545    NaN

...


```python
# Pas 3. Substituïr els nulls per np.nan, aplicant la màscara.
# En general: df.loc(MASK,FIELD) = VALUE.
entries4.loc[null_publisher_mask,"Publisher"] = np.nan

# Pas 4. Mostrem un resultat per a provar.
print(entries4.iloc[62,:])
```




>   Rank                                                                    645
>   
>   Sourceid                                                              22549
>   
>   Title                                                 Public Health Reviews
>   
>   Type                                                                journal
>       Issn                                                     21076952, 03010422
>   
>       SJR                                                                   1,692
>   
>       SJR Best Quartile                                                        Q1
>
>       H index                                                                  34
>   
>   Total Docs. (2020)                                                       31
>   
>       Total Docs. (3years)                                                     68
>   
>       Total Refs.                                                            1891
>   
>       Total Cites (3years)                                                    376
>   
>       Citable Docs. (3years)                                                   65
>   
>   Cites / Doc. (2years)                                                  5,76
>   
>   Ref. / Doc.                                                           61,00
>   
>   Country                                                      United Kingdom
>   
>   Region                                                       Western Europe
>   
>   Publisher                                                               NaN
>   
>       Coverage                                    1973-1980, 1982-2003, 2010-2020
>   
>   Categories                Community and Home Care (Q1); Public Health, E...
>   
>   Name: 644, dtype: object

<a name="cleannan"></a>

Marcar todos los publisher que se encuentran a Null, pasarlos a Nan


```python
# Clean NAs

entries4 = copy.deepcopy(entries)

entries4.loc[:,"Publisher"].isnull().value_counts()

null_publisher_mask = entries4.loc[:,"Publisher"].isnull()

entries4.loc[null_publisher_mask,"Publisher"] = np.nan
entries4.iloc[644,:]
```




    Rank                                                                    645
    Sourceid                                                              22549
    Title                                                 Public Health Reviews
    Type                                                                journal
    Issn                                                     21076952, 03010422
    SJR                                                                   1,692
    SJR Best Quartile                                                        Q1
    H index                                                                  34
    Total Docs. (2020)                                                       31
    Total Docs. (3years)                                                     68
    Total Refs.                                                            1891
    Total Cites (3years)                                                    376
    Citable Docs. (3years)                                                   65
    Cites / Doc. (2years)                                                  5,76
    Ref. / Doc.                                                           61,00
    Country                                                      United Kingdom
    Region                                                       Western Europe
    Publisher                                                               NaN
    Coverage                                    1973-1980, 1982-2003, 2010-2020
    Categories                Community and Home Care (Q1); Public Health, E...
    Name: 644, dtype: object


<a name="updatepublisher"></a>

Actualitzar tots els registres que es troben a nulls, o a nan, amb un valor fixe de  String=**"Unkown Publisher"**

```python
# Manage NA's

entries5 = copy.deepcopy(entries4)
#2 opcions , aquestes dues linees, fan el mateix que utilitzant el parametre inplace
update_publisher = entries5.loc[:,"Publisher"].fillna(value="Unkown Publisher")
entries5.loc[:,"Publisher"] = update_publisher
#segona opcio amb inplace, ho canvia a la mateixa linea (abans no)
entries5.loc[:,"Publisher"].fillna(value="Unkown Publisher",inplace=True)
entries5.iloc[644,:]
```




>    Rank                                                                    645
>    
>    Sourceid                                                              22549
>    
>    Title                                                 Public Health Reviews
>    
>    Type                                                                journal
>    Issn                                                     21076952, 03010422
>    
>        SJR                                                                   1,692
>    
>        SJR Best Quartile                                                        Q1
>    
>        H index                                                                  34
>    
>        Total Docs. (2020)                                                       31
>    
>        Total Docs. (3years)                                                     68
>    
>        Total Refs.                                                            1891
>    
>        Total Cites (3years)                                                    376
>    
>        Citable Docs. (3years)                                                   65
>    
>        Cites / Doc. (2years)                                                  5,76
>    
>        Ref. / Doc.                                                           61,00
>    
>        Country                                                      United Kingdom
>    
>        Region                                                       Western Europe
>    
>        Publisher                                                  Unkown Publisher
>    
>        Coverage                                    1973-1980, 1982-2003, 2010-2020
>    
>        Categories                Community and Home Care (Q1); Public Health, E...
>    
>        Name: 644, dtype: object
>    


<a name="seriesvalor"></a>

Canviar valors na a 0, o eliminant registres que tenen el valor na en una columna especial.

```python
ser1: pd.Series = pd.Series([0,1,2,3,np.nan,5.6])
ser1.fillna(value=0,inplace=True)
ser1
```




    0    0.0
    1    1.0
    2    2.0
    3    3.0
    4    0.0
    5    5.6
    dtype: float64




```python
#esborrar registres amb valors na
ser2: pd.Series = pd.Series([0,1,2,3,np.nan,5.6])
ser2=ser2.dropna()
ser2
```




    0    0.0
    1    1.0
    2    2.0
    3    3.0
    5    5.6
    dtype: float64


<a name="map"></a>

### MAP,MAPAPPLY, APPLY

#### Instrucció MAP

Aplicar una transformació(en aquest cas, doblar el valor) a tota la fila

```python
#1 Map
ser3: pd.Series = pd.Series([0,1,2,3])
ser3.map(lambda x:x*2)
```

>    0    0
>
>    1    2
>
>    2    4
>
>    3    6
>
>    dtype: int64

**Optimització**

No es recomana usar funcions lambda en series o dataframes molt grans, perquè el temps que es triga creant la 
funció anònima és alt i això fa que el rendiment sigui més dolent que creant la funció apart.

Per tant, aquest codi tindria més bon rendiment.


```python
#1 Map
def mult5(num: int)-> int:
    return num * 5

ser3: pd.Series = pd.Series([2,4,6,8,10,12])
ser3 = ser3.map(mult5)

print(ser3)
```


```python
ser4: pd.Series = pd.Series(["John","Lucy","Mary","Peter"])
ser4.map(lambda x: "Hello " + x)
```

```python
def helloName(name: str)-> str:
    return "Hello " + name

ser4: pd.Series = pd.Series(["John","Lucy","Mary","Peter"])
ser4 = ser4.map(helloName)
print(ser4)
```



>    0     Hello John
>
>    1     Hello Lucy
>
>    2     Hello Mary
>
>    3    Hello Peter
>
>    dtype: object
>

<a name="mapaply"></a>

###### applymap 

```python
# DataFrame.mapaply(). Works elements wise for rows
data = {"A": [1,2],
       "B": [3,4]}
df3 = pd.DataFrame(data)
df3.applymap(lambda x:x*2)
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>


<a name="apply"></a>
###### Funció apply

En aquest cas sumarem valors

```python
#Works column wise
df3.apply(lambda column:column.sum())
```




>    A    3
>
>    B    7
>
>    dtype: int64

<a name="novacolumna"></a>

###### Crear una nova columna, dins el teu dataframe.

```python
df4 = copy.deepcopy(df3)
df4.loc[:,"C"] = df3.B.map(lambda x:x*2)
df4
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>

<a name="orden"></a>

###### Canviar el ordre dins un dataframe

```python
df5 = df4.loc[:,["C","A","B"]]
df5
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>


