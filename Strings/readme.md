# String Formatting

To create string with multiple variables coming at runtime use format function

````python
message = "formatting can take number: {} decimal: {} string: {} ".format(89898989, 2.3, "testme")
````
Output:

```
formatting can take number: 89898989 decimal: 2.3 string: testme
```

Another way to do the same

```python
first_name = "a"
middle_name = "b"
last_name = "c"
message = "My name is %s %s %s" % (first_name,middle_name,last_name)
```

Output:

```
My name is a b c
```


For numbers and decimails give %d and %f.

```python
message = "formatting can take number: %d decimal: %f string: %s " % (89898989, 2.3, "testme")
```

Output:

```
formatting can take number: 89898989 decimal: 2.300000 string: testme
```

<h4>Enumerate method</h4>

If we want to break a string into (index, character) tuple then use enumerate method

```python
text = "hi this is your friend"
for item in enumerate(text):
    print(item)
```

Output:

```
(0, 'h') # indexing starts with index 0
(1, 'i')
(2, ' ')
(3, 't')
(4, 'h')
(5, 'i')
(6, 's')
(7, ' ')
(8, 'i')
(9, 's')
(10, ' ')
(11, 'y')
(12, 'o')
(13, 'u')
(14, 'r')
(15, ' ')
(16, 'f')
(17, 'r')
(18, 'i')
(19, 'e')
(20, 'n')
(21, 'd')
```

