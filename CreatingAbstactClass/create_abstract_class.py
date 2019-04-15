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


class user2(MyAbstractClass):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_me(self):
        super().print_me() # Yes we can call abstract class printme method here to do whats default




k = user('bharat', 23)
z = user2('bharat',23)
z.print_me()