
# Return Exception than None

- If you return None from a function which can return 0 as a valid return value then following expression will be true for both 0 and None.

```
res = someFunc()
if not res:
    print("Invalid inputs")
```

- not res will evaluate to true for both None and 0.
- This can be error prone. 

- Instead do a proper None check to avoid issues or return multiple values like:

```python
def divide_returns_tuple(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None
```

