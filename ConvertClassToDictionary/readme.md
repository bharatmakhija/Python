# Convert a class to Json

```python

class Hello:

    def __init__(self):
        self.name = 'Bharat'
        self.age = '12'


k = Hello()
print(k.__dict__)

print("This dictionary can be directly converted to Json object for serialization")

import  json
k_json = json.dumps(k.__dict__)
print(k_json)
print("This json can be directly used to send in api calls")
```

Output:

```
{'name': 'Bharat', 'age': '12'}
This dictionary can be directly converted to Json object for serialization
{"name": "Bharat", "age": "12"}
This json can be directly used to send in api calls
```

- default scope of __dict __ is only one layer, so if class is nested __dict will convert only the outer class to dictionary.

- however we can achieve this using mixins.
