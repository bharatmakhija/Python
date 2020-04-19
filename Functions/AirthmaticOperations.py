# A simple example where nested functions implemmentation can come handy. Basically it can be used as Factory of java where
# different functions can be returned on runtime based on what input parameter is passed

def arithmatic(operation):

    if operation == "ADD":
        def addition(x, y):
            return x + y
        return addition

    if operation == "SUB":
        def substraction(x,y):
            return x - y
        return substraction

    if operation == "DIV":
        def division(x,y):
            return x / y
        return division

    if operation == "MUL":
        def multiplication(x,y):
            return x*y
        return multiplication

    return None

operation = arithmatic("ADD")
if operation != None:
    res = operation(2,3)
    print(res)

operation = arithmatic("MUL")
if operation != None:
    res = operation(2,3)
    print(res)