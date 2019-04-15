# Class Methods in python

- class methods are ones which can be accessed by class or intance of class both.
- class methods take class as input rather than instance of a class.
- class methods can act as constructor as they can be accessed using class and using class methods we
can provide multiple constructors for a class. 
- class methods can be declared using a decorator **@classmethod**

Say we have a class named Employee where its constructor takes name, age and salary as input:

```python
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
```

However we are given employees as a string like
'JOHN-23-12000'

so to create an employee from this we need to parse it 

```python
s = 'JOHN-23-12000'
name, age, salary = s.split('-')
```
then use these variables to create employee.

Instead what we can do is we can move above logic to a method which is class method and that will create the employee for us.
Also it will be availabe to us throughout whereever employee is imported. 

```python
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def create_employee_from_str(cls, employee_str, split_param = '-'): 
        name, age, salary = employee_str.split(split_param)
        return cls(name,age,salary)

    def __str__(self):
        return "name: {}, age: {} , salary: {}".format(self.name,self.age,self.salary)
```

- In class method above, we have given default split param, we can give other as well.
- Similarly we can add multiple other implementations as well.
