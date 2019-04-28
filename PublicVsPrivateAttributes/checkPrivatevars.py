
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



k = CheckPrivateVarsChild()
print("k.get_private_var()")
print("If we run above line we will get: AttributeError: 'CheckPrivateVarsChild' object has no attribute '_CheckPrivateVarsChild__private_field")

print("Lets print its dict object")
print(k.__dict__)
print("current class and parent class public and private variables are kept with original names")
print("All private variable names are modified as --> undescore + ClassName + private_variable_name")
print("so when in child class when we try to access parent private variable __private_filed then what compiler does is it modifies the name as")
print("_CheckPrivateVarsChild__private_filed but since var is in parent class its names is _CheckPrivateVarsChild__private_filed so they don't match")
print("so the result is : AttributeError: 'CheckPrivateVarsChild' object has no attribute '_CheckPrivateVarsChild__private_field")

print("But since we know how the names are tweaked we can access private variables by giving parent class name")

print(k.get_private_var_modified())
