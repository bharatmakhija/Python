
class MyBaseClass:

    def __init__(self, value):
        self.value = value

class AddTwo(MyBaseClass):

    def __init__(self, value):
        MyBaseClass.__init__(self,value=value)
        self.value += 2


class MultiplyFive(MyBaseClass):

    def __init__(self, value):
        MyBaseClass.__init__(self, value=value)
        self.value *= 5


class MyCustomClass(MultiplyFive, AddTwo):

    def __init__(self, value):
        MultiplyFive.__init__(self, value=value)
        AddTwo.__init__(self, value=value)

# So this is a diamond where a class Mycustom class inherits from 2 classes (MultiplyFive and AddTwo) which inherit from same class (MyBaseclass)

k = MyCustomClass(5) # by this way it should be 5*5 + 2 which is 27 however the result is 7
print(k.value)
print("This happens because myBase class constructor got called twice")
print("Python 3 solved this problem by using super keyword")
print("Another problem with this approach was if class name changes at latr stage, we need to change it everywhere")


