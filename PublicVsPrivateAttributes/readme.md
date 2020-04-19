# Public Vs Private Attributes

- prefer public more that private attributes.
- Private attributes are not harshly enforced by python compiler.

```python
class MyObj(object):
    
    def __init__(self):
        self.public_var = 4
        self.__private_var = 10
        self._protected_var = 12

```

- Private variables are declared with double underscore at the starting of variable name while protected variables are created
with single underscore at start.

- Directly accessing private variable outside the class raises an exception --> "Class__name__ object has no attribute ..."
- Private variables can be accessed by methods inside the class.

- Private variables can't be accessed by the child class.

#### But...

- We can access private variables of parent class.

```python
class CheckPrivateVarsParent(object):

    def __init__(self):
        self.__private_field = 12
        self.public_var = 10
        self._protected_var = 13




class CheckPrivateVarsChild(CheckPrivateVarsParent):

    def __init__(self):
        super().__init__()
        self.child_public =12
        self._child_protected = 13
        self.__child_private = 50

    def get_private_var(self):
        return self.__private_field


    def get_private_var_modified(self):
        return self._CheckPrivateVarsParent__private_field # we can access private variable of parent class
```

- All private variable names are modified as --> undescore + ClassName + private_variable_name.
- so basically parent class has its classname attached to it so while accessing from child class compiler attaches childclass name to the private variable being accessed and thus no matching attribute is found.
- If we explicitly mention the parent class name then we can access the parent classes private variables in current class.

### Note

- Only use private variables when you are in doubt that in future someone might come and use the same name as your variable to create conflicts. Otherwise as such there is no use of private variables.

- In Python community, protected variable are something which are supposed to be handled with caution. Always use protected variables to indicate that this variable is critical. If you
are tweaking it, things might fail.
- Infact its advised to keep documentation of protected variables to guide subclasses instead of trying to force access control via private variables.

