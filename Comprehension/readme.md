# List Comprehensions
- Python privides ways to convert one list to another which are called list comprehensions.

Approach 1:
````python
a = [1,2,3,4,5]
squares = [x ** 2 for x in a]
print(squares)
````

Approach 2:

````python
squares_using_map = map(lambda x:x **2, a)
print(list(squares_using_map))
````

- Approach 1 looks pretty straight forward and visually less noisy.

<h4> Say we want to filter all even numbers from squares above: </h4>

Approach 1:
````python
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)
````

Apporach 2:
```python
even_squares_using_map = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(even_squares_using_map))
```

- As we can see again approach 2 is difficult to understand.

# Dictionary Comprehensions

````python
d = { 'hello': 1, 'hi': 2, 'namaste': 3}
d_inverse = {b:a for a, b in d.items()}
````

- when we iterate over a dictionary like this

```python
for item in d.items():
    print(item)
```

Output:

```
('namaste', 3)
('hi', 2)
('hello', 1)
```

- every item is nothing but a tuple.

- we can extract tuple to different values like this:
 
 ```python
a,b,c = ("hello",1,2)
 ```
 
 - here a will get hello, b will get 1 and c will get 2.
 
 - so if we go this way
 
 ```
for key, value id dict.items():
    print(key + " " + value)
 ```
 - we can get key, value seperately like above. 
 
 - we can do multiple things with that like say i want all keys to become value and viceversa in new dictionary
 
 ```
 new_dic = {b:a for a,b in dic.items()}
 ```
 
 - this new_dic so created will be inverse of dic
 
 - One thing to note, If we are doing some mathamatical operation of finding length of values in dic and we want them in same order as the key-value pairs exist
 in dictionary then store them in list. 
 
 ````
 k =  [ len(a) for a,b in d.items()] # it will be of same order as items are in dictionary
print(k)

````

- However if order doesn't matter we can store the same in another dictionary object as well. here length will always come in increasing order.

```
# we can store above in dictionary as well

k = { len(a) for a,b in d.items()} # here no matter what it will always be sorted
print(k)
'''
