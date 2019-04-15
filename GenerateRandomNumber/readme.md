# Generate random numbers

For this:

```python
import random
```

- Generate random number between 1 to 100

```python
import random
for x in range(10):
  print(random.randint(1,101)) # here 101 is not included, its [) range type!!
```

- Generate random number between 1 to 100 which is multiple of 3.

```python
import random
for x in range(10):
  print(random.randint(1,34)*3) #33*3 WILL GO MAX UP TO 99, so numbers btw 3 to 99 will come
```

