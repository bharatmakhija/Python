# Functions

In python functions are first class objects

-  they can be passed to a variable
- can exist inside another function
- one function can be returned from another function
- can be passed as argument to another function

Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

One function can be passed to another function as a variable:

````python
def myfunc():
    print("inside myfunc, execting ...")


def wrapper_func(func):
    print("inside wrapper func, before given func is executed")
    func()
    print("inside wrapper func, after executing func")


wrapper_func(myfunc)
````
-  when passing a function as argument, we don't give paranthesis ()


```python
def outer_func(func):
    print("inside outer_func, before inner func is called")
    def inner_func():
        print("Inside inner function")
        print("trying to access variable passed to outer function")
        func()
        print("At the end of inner function")
    print("inside outer_func, after inner func is called")


def print_hi():
    print("Hiiiiiii")

outer_func(print_hi)
```
Output:

````
inside outer_func, before inner func is called
inside outer_func, after inner func is called

````
- If I define one function inside another function it doesn't execute automatically

- lets execute inner function after declaration in outer function like this 

```python
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
```

Output:

```
inside outer_func 1, before inner func 1 is declared
inside outer_func 1, after inner func 1 is declared
inner function 1 is called
Inside inner function 1
trying to access variable passed to outer function 1
Hiiiiiii
At the end of inner function 1
```

- Instead of calling inner function it can also be returned as a variable. 

```
def outer_func_1():
    .
    .
    def inner_func1():
        .
        .
    return inner_func1
    
k = outer_func1()
# now k will have reference to inner function
#by executing k we can execute inner_func1

k()
```