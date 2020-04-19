
def outer_func(func):
    print("inside outer_func, before inner func is declared")
    def inner_func():
        print("Inside inner function")
        print("trying to access variable passed to outer function")
        func()
        print("At the end of inner function")
    print("inside outer_func, after inner func is declared")


#outer_func(print_hi)



def outer_func1(func):
    print("inside outer_func 1, before inner func 1 is declared")
    def inner_func1():
        print("Inside inner function 1")
        print("trying to access variable passed to outer function 1")
        func()
        print("At the end of inner function 1")
    print("inside outer_func 1, after inner func 1 is declared")
    print("inner function 1 is called")
    inner_func1()


def print_hi():
    print("Hiiiiiii")



outer_func1(print_hi)