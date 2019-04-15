# Abstract Class

- Abstract class is one which can't be instantiated.
- whose subclasses have to implement the methods of base abtract class.

- For this we will use ABC Module.

```python
from abc import ABC, abstractmethod
```

If we want to make any class abstract it should extend ABC class.

```
class myAbstactClass(ABC):
```

- abstract methods in python can have default implementation.
- abstract methods can be called from thier implementations in sub classes using super() functionality.
- **@AbstractMethod** decorator can be used to make method abstract.
- if abstract method is not implemented in child class a type error like following is thrown:

"TypeError: Can't instantiate abstract class user with abstract methods print_me" 

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC): # extending ABC is important else nothing will work!!

    def __init__(self):
        super().__init__()

    @abstractmethod
    def print_me(self):
       print("abstract methods in python can have implementation that can act as default")


class user(MyAbstractClass):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_me(self):
        pass # if i don't give implementation of this method, user object creation will fail.

#TypeError: Can't instantiate abstract class user with abstract methods print_me, if print_me is not declared typeerror will come!!

```

