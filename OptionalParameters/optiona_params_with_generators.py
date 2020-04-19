

def my_gen():
    for i in range(10):
        yield i


def my_print(*values):
    print(values)

it = my_gen()
my_print(*it) # its output will be tuple from 0 to 9. If in future generator yields millions of values, this will fail
# as it will try to create tuple of those million of values


