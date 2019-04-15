
class hello:

    count = None # this is a class variable, this can be modified by both class and instance of the class

    def __init__(self):
        self.name = None # this is an instance variable, this can be modified by instance i.e. object of class
         # This is the constructor

    def __call__(self, *args, **kwargs):
        pass # this is the method which is called when this class object is executed.

    def __str__(self):
        pass
        # This method can be overridden, here when you try to print object of this class
        # whatever string we return from this class will get printed


    def method1(self,a ,b, *args):
        pass # this is a instance method i.e. this method can be called by object of this class only
        # this method takes argument self i.e. the instance of the class. a and b are positional parameters, *args are optional.


    @classmethod
    def method2(cls,a,b, *args):
        pass # this is a class method. It can be accessed by class or instance both. This takes class as input instead of instance.(will se later how it works)

    @staticmethod
    def method3(a,b,*args):
        pass # this is static method, its basically like an independent function defined inside the class. it can be accessed by both instance and class.
        # it doesn't depend on either the instance or class variables. it can work independently thats why static method.
        # this is kept in the class only because it has some relation with the class.

k = hello() # this is how we create instance of a class.