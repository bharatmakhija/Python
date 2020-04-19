
class MyBaseClass:

    def __init__(self, value):
        self.value = value

class AddTwo(MyBaseClass):

    def __init__(self, value):
        super().__init__(value=value)
        self.value += 2


class MultiplyFive(MyBaseClass):

    def __init__(self, value):
        super().__init__(value=value)
        self.value *= 5


class MyCustomClass(MultiplyFive, AddTwo):

    def __init__(self, value):
        super().__init__(value=value)

# So this is a diamond where a class Mycustom class inherits from 2 classes (MultiplyFive and AddTwo) which inherit from same class (MyBaseclass)

k = MyCustomClass(5) # by this way it should be 5*5 + 2 which is 27 however the result is 7
print(k.value)

print("so ordering is depth first search left to right so multiply five should come first which will make 5_5 and then +2 should come which should make it 27")
print("but what we are getting is 35")
print("lets print its mro and find out why?")

from pprint import pprint
pprint(MyCustomClass.mro())
print("init is called in the order mycustomclass -> multiplyfive -> plus2 -> MyBaseClass")
print("then execution actually happens in reverse order, i.e. starting from MyBaseClass to MyCustomClass")
print("so first 5 is set as value then call comes back to AddTwo and 2 is added and then call comes back to Multiply5 and 5 is multiplied and then call Comes back to MyCustomClass")
print("printing mro if order is changed to AddTwo and then MultiplyFive")
class MyCustomClassModified(AddTwo, MultiplyFive):

    def __init__(self, value):
        super().__init__(value=value)

pprint(MyCustomClassModified.mro())
print(MyCustomClassModified(5).value)
print("See here value came as 27")