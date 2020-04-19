# class inheritance

- if your base class is user and you want to extend it i.e. say you want to create another class named 'prime_user', this is how we will do it.

```
class prime_user(user): # this is how we extend
    .
    .
```
- calling constructor of parent class

```
class prime_user(user): # this is how we extend

    def __init__(self, name, age):
        # here first we call the constructor of a super class
        super().__init__(name,age) # This is how super-object is called.
        self.prime = True
        self.plan = None

```

