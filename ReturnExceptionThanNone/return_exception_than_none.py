def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

# Here function is returning None
#  Here None has a meaning that zeroDivisionError has occurred

res = divide(3,0)
if not res:
    print("invalid inputs")


res = divide(0,2)
if not res:
    print("invalid inputs")
    print("Even when numerator is 0, even then not res will evaluate to true")


# So when None is returned or When 0 is returned in both cases "not res" will evaluate to be true.
# So returning None from a function is error prone

# However

res = divide(0,2)
if res == None:
    print("2. invalid inputs")
    print("2. Even when numerator is 0, even then not res will evaluate to true")


# specific None check will work here, but we generally use not operator which can lead to issues
# Or we can return a tuple where first value is the status of operation and second one is the result of operation if any


def divide_returns_tuple(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

