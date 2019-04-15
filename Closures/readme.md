# Closures in Python

A function which is defined inside another function is known as **nested function**. Nested functions are able to access variables of the enclosing scope.

```python
def outerFunction(text): 
    text = text 
  
    def innerFunction(): 
        print(text) 
  
    innerFunction() 
```

-  innerFunction() can easily be accessed inside the outerFunction body but not outside of it’s body. Hence, here innerFunction() is treated as nested Function which uses text as non-local variable.

<h4>A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.</h4>


```python
# Python program to illustrate 
# closures 
def outerFunction(text): 
    text = text 
  
    def innerFunction(): 
        print(text) 
  
    return innerFunction
  
if __name__ == '__main__': 
    myFunction = outerFunction('Hey!') 
    myFunction() 
```

Output:

```
Hey!
```

- with closures we can invoke function outside of their scope.
- The function innerFunction has its scope only inside the outerFunction. But with the use of closures we can easily extend its scope to invoke a function outside its scope.


<h4>Closures can be used for writting wrapper around a function</h4>

wrappers are basically to extend the functionality of a function without actually modifying it.