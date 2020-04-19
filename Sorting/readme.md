
# Sorting

- use sort function on list to sort in asc order by default 

```python
nums = [3,4,51,2,3]
nums.sort()
print(nums)
```
Output:

```
[2, 3, 3, 4, 51]
```

- sorting in reverse order 

```
nums.sort(reverse=True)
```
<h4>Using a helper function to sort:</h4>
- Using function helper to sort such that all even numbers will come first

```python
nums = [3,4,51,2,3]
def sorting_helper(x):
    if x % 2 == 0:
        return (0,x)
    return (1,x)

nums.sort(key=sorting_helper)
print(nums)
```

Output:

```
[2, 4, 3, 3, 51]
```

<h4>Using a helper class to sort</h4>
- Using seperate class to define sorting behavior:

```python
nums = [3,4,51,2,3]

class Sorter:

    def __init__(self):
        pass

    def __call__(self, x):
        if x % 2 == 0:
            return (0, x)
        return (1, x)

sorter = Sorter()
nums.sort(key=sorter)
print(nums)
```

Output:

````
[2, 4, 3, 3, 51]
````

