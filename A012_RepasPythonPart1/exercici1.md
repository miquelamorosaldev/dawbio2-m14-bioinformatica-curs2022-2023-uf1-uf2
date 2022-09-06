##### *Exercici* Crear un nou diccionari on les claus del primer siguin els valors del segon i els valors, passin a ser les claus.


```python
# Solution "for" 1

dict_reverse = {}

for key, value in d.items():
    name = key
    tel  = value
    dict_reverse[tel] = name
dict_reverse
```

Una segona solució, seria... 

```python
#Solution 2 items() example
d.items()
dict_reverse2 = {}
for key, item in d.items():
    dict_reverse2[item] = key
    print(key, item)
dict_reverse2
```
```python
#Solution 3 with only keys
# keys() example

dict_reverse3 = {}
for key in d.keys():
    tel = d[key]
    dict_reverse2[tel] = key
dict_reverse3
```


Per una de les possibles solucions al exercici s'introdueix un nou concepte el de comprenhension

<a name="comprenhension"></a>
**Comprenhension**
·Hi ha "Dict Comprenhensions" y "List Comprenhensions"
·Per a llegir o escriure una comprenhension, es comença pel mig (pel "for")
·Dict comprenhension

    ```d2 = {key:value for key,value in dictionary_source.items()```

·List comprenhension

    ```d2 = {elem for elem in List_source```

```python
# Solution 4 Comprenhemsion 
#Como crear una nueva coleccion a partir de otra en una linea
#Existe Dict Comprenhensio y List Comprenhension

dict_reverse_oneline = {tel:name for name, tel in d.items()}
dict_reverse_oneline
```

> {111: 'Roger', 234: 'Dani', 342: 'Mar', 567: 'Albert', 478: 'Carlos'}
