import datetime

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print("%s: %s" % (message, values_str))

log("helo")
log("my numbers are ",1,2,3)
log("current date is ", datetime.datetime.now())



l = [1, 12.3, 'hello']
log("we can pass list as optional params", *l)
