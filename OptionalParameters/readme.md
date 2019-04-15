# Optional Parameters

In python we can give optional parameters that we can decide if we
want to pass or not.

- we use * to indicate if parameter is optional or not
```python
def log(message, *values):
    pass
```
- here first param message is required.
- after first message parameter, any number of subsequent parameters are optional.
- function's body doesn't need to change, only callers will change
in different scenarios.

```python
import datetime

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print("%s: %s" % (message, values_str))

log("helo")
log("my numbers are ",1,2,3)
log("current date is ", datetime.datetime.now())
```

-  if we want to pass some list values as optional arguments we can directly do so using * operator

```python
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print("%s: %s" % (message, values_str))
        
l = [1,12.3,'hello']
log()
```

- Issue: variable arguments are always turned into tuple before they are passed to function(here log function)
so if we use * operator on a generator, it will try to create a tuple of all values generator will yield. 
if tuple grows so much in size, program may fail.

- Another usability issue with optional parameters is if my function structure is func(a,b, *args) and function is being used at multiple places where different optional params were
set to it from time to time.
Now if i want to add a positional argument then I have to add it before *args and that means whereever I have passed optional params till now, i have to go and change the definition there.

