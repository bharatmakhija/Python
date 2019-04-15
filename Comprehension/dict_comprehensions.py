d = { 'hello': 1, 'hi': 2, 'namaste': 3}

print("Current Dictionary")
print(d)

print("when we iterate over a dictionary, every item becomes a tuple")
for item in d.items():
    print(item)


a,b,c = ("abc", 12, 14) # and this is how a tuple can be extracted
print(a)
print(b)
print(c)

#so

for a, b in d.items():
    print("a = " + a)
    print("b = " + str(b))
print("So a becomes key and b becomes value")

print("So for a , b in items we want b : a in dictionary")

print(" d_inverse = { b: a for a, b in d.items()}")


# as you can see a automatically becomes key and b automatically becomes value

# I want that In one line value become key and key becomes value in another dictionary

d_inverse = {b:a for a, b in d.items()}
print(d_inverse)

#Similary if we want to find length of all values

k =  [ len(a) for a,b in d.items()] # it will be of same order as items are in dictionary
print(k)

# we can store above in dictionary as well

k = { len(a) for a,b in d.items()} # here no matter what it will always be sorted
print(k)