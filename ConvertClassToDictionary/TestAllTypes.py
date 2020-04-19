

class TestAllTypes:

    def __init__(self):
        self.str_var = "asdf"
        self.int_var = 12
        self.float_Var = 12.3
        self.list_Var = ['1','2']
        self.dic_var = {'2':'hello'}



k = TestAllTypes()
print(k.__dict__)

print('"Yes it converts all types to dict')
print("what if one of the variable is another python object")

class Crap:

    def __init__(self):
        self.test_Var = "kv"

class MyNewClass:

    def __init__(self):
        self.crap = Crap()
        self.name = 'name'


t = MyNewClass()
print(t.__dict__) # {'name': 'name', 'crap': <__main__.Crap object at 0x7ff8ec1b2cc0>}

# As we can see its printing python object, so we want that all classes should automatically get converted to dict object

print("We can create a generic mixin class to do this for us")