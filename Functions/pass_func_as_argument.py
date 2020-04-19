
def myfunc():
    print("inside myfunc, execting ...")


def wrapper_func(func):
    print("inside wrapper func, before given func is executed")
    func()
    print("inside wrapper func, after executing func")


wrapper_func(myfunc) # when passing a function as argument, we don't give paranthesis ()
