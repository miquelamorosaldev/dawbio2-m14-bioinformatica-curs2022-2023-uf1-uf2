#### *Exercici* A partir d'una llista, del 1 al 10, crear una nova llista, amb els valors al quadrat.

Solució usant List Comprension.

```python
numbers = range(1,11)
llista2 = [ num**2 for num in numbers]
llista2
```

> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Solució sense List Comprension.

```python
numbers = range(1,11)
i: int = 0
while i < len(numbers):
    numbers[i]=numbers[i]**2
    i+=1
```

