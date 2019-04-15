
def outer():
    a = 12
    def inner(a):
        a = a + 2 # this a has different scope, by default this a will not make any changes in outer a
        print("modified in inner " + a.__str__())
    inner(a)
    return a

print(outer())

# SO basically scope traversal doesn't happen in closures, however there is a way to do so using "nonlocal" before variable a


def outer2():
    a = 12
    def inner():
        nonlocal a
        a = a + 2 # this a has different scope, by default this a will not make any changes in outer a
        print("modified in inner " + a.__str__())
    inner() # makesure we are not passing a otherwise it will create discrepency
    return a

print("Using nonlocal for a allowed scope traversal " + outer2().__str__())


# Another normal way is to explicitly pass the modified value to outer function
def outer3():
    a = 12
    def inner(a):
        a = a + 2 # this a has different scope
        print("modified in inner " + a.__str__())
        return a
    a = inner(a) # Now we have modified the outer function variable so it will work
    return a

print(outer3())