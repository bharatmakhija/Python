
class BinaryTree:

    def __init__(self,value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



tree = BinaryTree(10,left=BinaryTree(7,left=3, right=8), right=BinaryTree(15,left=11,right=17))
print(tree.__dict__)

print("So as we can see only the outer binaryTree class got converted into dictionary, it doesn't go into heirarchy")
print("So can we do something here")

res = tree.__dict__
for key, value in res.items():
    if hasattr(value, '__dict__'): # This basically checks if object is something on which __dict__ can be called, for ex for value = 10, __dict__ can't be called.
        res[key] = value.__dict__

print(res)

