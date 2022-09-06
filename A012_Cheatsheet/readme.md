# CheatSheet List and Dictionary


## List cheatsheet list


```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)
```

 >[0, 1, [3]]
 >[0, 1, [3, 4]]
 >[0, 1, 2]



```python
sum([1, 2, 3])
```




 >6




```python
# list cheatsheet

# How to create an empty array?
l = [] #square brackets
l = list()
l
```




 >[]




```python
# How to create a literal array
l = [1,2,3]
```


```python
n = [int(num) for num in l]
n
```




 >[1, 2, 3]




```python
# how to find the number of elements in an array
len(l)
```




 >3




```python
# how to access elements in an array
l[0]
```




 >1




```python
# how to slice an array
l[0:2] #last index always excluded
```




 >[1, 2]




```python
#how to update the value at a given position
l[1] = 5
l
```




 >[1, 5, 3]




```python
#how to read and update the value at a given position
l[1] = l[1] + 2
l[1] += 2
l
```




 >[1, 9, 3]




```python
#How to list all the methods of an array
dir(l) #list of all methods, but the function with this '__' is only intern usage
```




 >['__add__',
 
 >'__class__',

 >'__contains__',
 
 > ..

> 'append',

> 'clear',

> ..

> 'reverse',
>  'sort']

```python
#How to the documentation of a method
help(l.remove)
```

>Help on built-in function remove:
>
>remove(value, /) method of builtins.list instance
>     Remove first occurrence of value.
>
>      Raises ValueError if the value is not present.
>


```python
#how to add new values at hen end of the array 
l.append(5)
```


```python
#how to insert new values at a given index
l.insert(3,7)
l
```




>[1, 9, 3, 7, 5]




```python
#How to remove the value at the end
l.pop()
l
```




>5






>[1, 9, 3, 7]




```python
# how to remove the value at a given index
l.remove(3)
l
```




>[1, 9, 7]




```python
l.pop(2)
```




>7




```python
l.append(22)
del l[1]
```


>1




>[1, 22]




```python
#How to remove all the elements in an array
l.clear()
del l[:]
```


```python
# how to find an element in an array
l = ["a","b","c","d"]
"c" in l #exists?
```




>True




```python
l.index("c")
```




>2




```python
l.reverse()
l
```




>['d', 'c', 'b', 'a']




```python
l[::-1]
l
```




>['a', 'b', 'c', 'd']






>['d', 'c', 'b', 'a']




```python
l.sort()
```


```python
sorted(l)
```




>['a', 'b', 'c', 'd']




```python
l1 = ["a","b","c"]
l2 = ["d","e","f"]
l3 = l1 + l2
l3
```




>['a', 'b', 'c', 'd', 'e', 'f']




```python
l3.extend(l2) #Modifies the original array
l=l1 + l2 #Returns a new list
```


```python
# How to copy an array
l4 = l1 #ERROR!!! NO COPY!!! It's a pointer
l4
l1.append('z')
l4
```




>['a', 'b', 'c']






>['a', 'b', 'c', 'z']




```python
#copy
l4 = l1.copy() #Shallow copy only objects without nested lists, nested lists point to original object
l1.append('w')
l1
```




>['a', 'b', 'c', 'z', 'w']




```python
l4 #its object different
```




>['a', 'b', 'c', 'z']




```python
import copy
l4=copy.deepcopy(l1) #Deep copy it's the best option.
```


```python
x1 = [{'a':1},{'b':2}]
x2 = x1.copy()
x2[0]["a"] = 3 #modificas también el x1
x1
```




>[{'a': 3}, {'b': 2}]




```python
x1 = [{'a':1},{'b':2}]
import copy
x2 = copy.deepcopy(x1)
x2[0]["a"] = 3 #no lo modificas
x1
```




>[{'a': 1}, {'b': 2}]




```python
#How to delete a slice
del l4[0:2]
```


```python
#How to delete an array
del l4
```

## Dictionari cheatsheet 


```python
# How to create an empty dict
dictionary = {}
```


```python
# How to create a populated literal dict
dictionary = {"name":"Miquel","surname":"Bardaji","age":30}
```


```python
# How to create a dict form a list of tuples
my_list = [('a', 1), ('b', 2)]
dict(my_list)
```




>{'a': 1, 'b': 2}




```python
# How to create a dict form two lists
keys_list = ["a","b","c"]
values_list = [1,2,3]
tuple_list=list(zip(keys_list, values_list))
d = dict(zip(keys_list,values_list))
print("tuple_list:", tuple_list)
d= dict(tuple_list)
```

>tuple_list: [('a', 1), ('b', 2), ('c', 3)]



```python
# How to find the number of items in a dict
len(d)
```



>3




```python
# How to list all the methods in a dict
dir(d)
```




>['__class__',

>'__contains__',

>'__delattr__',

>'__delitem__',

> .. 

> 'clear',

> 'copy',

> .. 

> 'update',

> 'values']




```python
# How to list items
list(d.items())
```




>[('a', 1), ('b', 2), ('c', 3)]




```python
# How to list keys
list(d.keys())
```




>['a', 'b', 'c']




```python
# How to list values
list(d.values())
```




>[1, 2, 3]




```python
# How to access an element in an dict
d["a"]
d.get("z","No encontrado")
```




>1






 >'No encontrado'




```python
# How to add a new element to a dict
d["d"] = 0
```


```python
# How to update a value in a dict
d["d"] = 10
d
```




>{'a': 1, 'b': 2, 'c': 3, 'd': 10}




```python
# How to read and update a value in a dict
d["d"] = d["d"]+3
d
```




>{'a': 1, 'b': 2, 'c': 3, 'd': 13}




```python
# How to add all items from one dict to another dict
d2 = {"d":4,"c":3,"f":5}
d.update(d2)
d
```




>{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}




```python
# How to remove a specific item and retrieve the value
"f" in d #Test if it exist
```




> True




```python
d.pop("f")
```




>5




```python
# How to sort a dict
d = {"c":3,"b":2,"d":4,"a":1}
sorted_keys = sorted(d.keys())
sorted_values = [d[k] for k in sorted_keys]
sorted_dict = dict(zip(sorted_keys,sorted_values))

print("sorted:", sorted_keys)
print("sorted_values",sorted_values)
print("sorted_dict",sorted_dict)
```

>sorted: ['a', 'b', 'c', 'd']

>sorted_values [1, 2, 3, 4]

>sorted_dict {'a': 1, 'b': 2, 'c': 3, 'd': 4}



```python
# How to delete one item in a dict
d["w"] = 4
d
```




>{'c': 3, 'b': 2, 'd': 4, 'a': 1, 'w': 4}




```python
del d["w"]
d
```




>{'c': 3, 'b': 2, 'd': 4, 'a': 1}




```python
# How to copy a dict
import copy
d4 = copy.deepcopy(d)
d4
```




>{'c': 3, 'b': 2, 'd': 4, 'a': 1}




```python
# How to delete a dict
del d4
```


```python
# How to delete a list of keys
keys_delete = ["b","d"]
for k in keys_delete:
    d.pop(k)
d
```




>2




>4


 >{'c': 3, 'a': 1}
