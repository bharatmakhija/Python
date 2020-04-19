# say I have a file having list of numbers, i want to normalized output
# ex: file has [2
# 3,
# 4]
# sum = 2 + 3 + 4
# output should be [(2/sum)*100,(3/sum)*100,(4/sum)*100 ]


# a generator that will yeild ints from input file
def read_file(name):
    with open(name, 'r') as f:
        for line in f:
            yield int(line)

# As generators returns an iterator


def print_generator_values(numbers):
    flag = True
    for i in numbers:
        flag = False
        print(i)
    if flag:
        print("no numbers found, iterator is empty")

it = read_file("mynums.txt")
# it is a generator object , lets see what it contains
print_generator_values(it)
print("lets try one more time")
print_generator_values(it)

# As we can see second time iterator is already empty or exhausted.
# so basically a iterator can be executed only once.
# now lets come to the problem

def normalize(numbers):
    total = sum(numbers)
    print("sum is " + total.__str__())
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

# In normalize method once sum runs on numbers, numbers will be exhaused. then value in numbers will not work as expected.

it = read_file("mynums.txt")
res = normalize(it) # this res will be empty list
print(res)

# one thing that can be done is keeping a copy of it in normalize

def normalize_keep_copy(numbers):
    numbers = list(numbers) # here we are converting iterator to list so eventually again this code can fail coz of out of memory if numbers are so many
    total = sum(numbers)
    print("sum is " + total.__str__())
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_file("mynums.txt")
res = normalize_keep_copy(it) # this res will be empty list
print(res)


print("getting new interator can be an option: ...")
# what we can do is we can send read_file("mynums.txt") as input to normalize function and it will get new iterator
# while doing addition and while iterating

def normalize_passed_read_file(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_passed_read_file(lambda : read_file("mynums.txt"))
print(percentages)

