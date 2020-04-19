# Continuing from normalize a file

#Even better way to achieve the same result is using a class that implements iterator protocol.
# read iterators readme.md to understand better

# Basically when we try to run over a iterator ,__iter__ method is called.
def normalize(numbers):
    total = sum(numbers)
    print("sum is " + total.__str__())
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

print("created a new container class, where __iter__ itself yields data")
class ReadFileGenerator(object):

    def __init__(self, file_name):
        self.file_name = file_name
    def __iter__(self):
        with open(self.file_name) as f:
            for line in f:
                yield int(line)
it = ReadFileGenerator("mynums.txt")
percentages = normalize(it)
print(percentages)

# So what ever we send list, array etc are all containers which python knows how to traverse.
# what we did above is defined one of our own container and used __iter method to tell it to yield results one after another.
# In this case at the time of sum __iter__ method will be called at it will yield line by line, and sum method will keep using it and doing sum.
# once its yielded it will be consumed then only next yield will happen.
# next while accessing each number in for loop, again second item iter method will get called and all are yielded again , and for loop will keep using that yielded value one by one.
# to generate results. Remeber this yielding and consumption are sequential.

# However we need to make sure that only the container type is passed to normalize function, because normalize will work fine
# with containers implementing iterator protocol. But it should throw error if the input is iterable but not a container type.

# how do we check in input to a function is iterable and container type.

# Iterator protocol states that when a iterator is passed to a built-in iter function, it returns the same iterator itself.
# however when a container type is passed to iter function, a newly created iterator will be returned each time.

def check_if_container_iterator(numbers):
    if iter(numbers) is iter(numbers):
        return False
    return True


it = ReadFileGenerator("mynums.txt")
print(check_if_container_iterator(it)) # as you can see it will print true

test_list = [1,2,3,4]
print(check_if_container_iterator(test_list)) # so even a normal list is a container iterator


it = iter(test_list) # calling iter on container type will return normal iterator which is no more container type
print(check_if_container_iterator(it))


k = ReadFileGenerator("mynums.txt")
k = iter(k)  #calling iter on container type will return normal iterator which is no more container type
print(check_if_container_iterator(k)) # as you can see it will print true
