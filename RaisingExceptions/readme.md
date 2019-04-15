# Raising Exceptions

- One should raise proper exceptions when provided with wrong inputs.

- we can forcefully raise exceptions using the keyword raise.

- say input value to a function is invalid, we can raise value error.

```python
def check(a):
    if a < 0:
        raise ValueError(str(a) + " is invalid")
```

- we can rais Memory Error like 

```python
raise MemoryError("This is an argument")
```


We can convert one of python errors and generate our own errors to handle specific use cases.
For example


```python
def divide(a,b):
    try:
        return True, a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs') from e
```

So now in any case of b == 0 python will give zero division error which we have caught and given our own error with message.

where ever we call this function, lets handle it

````python
def divide(a,b):
    try:
        return True, a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs') from e
        
try:
    result = divide(x,y)
except ValueError:
    print("Invalid Input")
else:
    print(result)
````

- so here if zerodivisionError occurs then we have handled it as it is due to b = 0 passed as input.
but if any other exception occurs due to any reason, we don't want to handle it but we will let it fail because if anyother exception is coming it means something has gone wrong in our divide function which should quickly be fixed.


if I would have written:

````
try:
    result = divide(x,y)
except Exception as e:
    print(e.__str()__)
else:
    print(result)

````

- here we have handled any exception and print it. Code will never fail but if anything goes
wrong in divide function now, it might go on now for few days impacting your business unleass you are strictly monitoring logs with any exception being printed.
- so basically big issues can go hidden with this which is not a good practice.
