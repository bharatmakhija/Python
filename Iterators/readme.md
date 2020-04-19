# Iterators

<h4>Iterator protocol</h4>

- Iterator protocol is how python for loops and related expressions traverse the contents of a container type.

- what happens when Python sees an expression like 

```python
foo = [1,2,3]
for x in foo: # what is happening in this exact statement
    print(x)
```

1. for x in foo will actually call iter(foo)
2. iter built in function calls 
```
foo.__iter__ 
```
3. The __iter __ method must return an iterator object.
4. Iterator objects theirselves implement the __next __ special method.
5. Then for_loop repeatedly calls next built-in function on iterator object until its exhausted.
5. Once iterator is exhausted it raises **StopIteration** exception.