# Any class which will extend this class can be converted to dictionary directly
# This is a generic mixin class that will convert any class to dictionary!!
class MyDictMixin(object):

    def convert_to_dict(self):
        return self._traverse_dict(self.__dict__) # top layer class is converted to dict and forwarderd
        print(self.__dict__) # so what comes here as self is tree object which is converted to __dict__


    def _traverse_dict(self, current_dict_instance):
        output = {}
        for key, value in current_dict_instance.items():
            output[key] = self._traverse(value)
        return output



    def _traverse(self, value):
        if isinstance(value, MyDictMixin):
            return value.convert_to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value




class BinaryTree(MyDictMixin):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(1,left=BinaryTree(2,left=BinaryTree(1,2,3),right=BinaryTree(4,5,6)), right=BinaryTree(4,5,6))
print(tree.convert_to_dict())


