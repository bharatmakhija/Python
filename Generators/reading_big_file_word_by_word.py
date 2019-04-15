from itertools import islice

FIRST_N_WORDS = 10
def index_file(f):
    offset = 0
    for line in f:
        if line:
            yield offset
            for letter in line:
                offset += 1
                if letter == ' ':
                    yield offset
def open_file():
    with open('hello.txt', 'r') as f:
        it = index_file(f)
        results = islice(it,0,FIRST_N_WORDS) # it will be called firstnwords time and that many times it has to yield
        print(list(results))

open_file()