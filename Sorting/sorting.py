nums = [3,4,51,2,3]
nums.sort()
print(nums)

# to sort in desc order

nums.sort(reverse=True)
print(nums)

# sorting using specific condition like all even numbers should come first
# for this we can use helper function
def sorting_helper(x):
    if x % 2 == 0:
        return (0,x)
    return (1,x)

nums.sort(key=sorting_helper)
print(nums)

# We can also pass a class to do so

nums = [3,4,51,2,3]

class Sorter:

    def __init__(self):
        pass

    def __call__(self, x):
        if x % 2 == 0:
            return (0, x)
        return (1, x)

sorter = Sorter()
nums.sort(key=sorter)
print(nums)