first_name = "bharat"
middle_name = "kumar"
last_name = "makhija"

message = " Hi this is {} {} {}".format(first_name,middle_name,last_name)
print(message)

message = "formatting can take number: {} decimal: {} string: {} ".format(89898989, 2.3, "testme")
print(message)

message = "My name is %s %s %s" % (first_name,middle_name,last_name)
print(message)


message = "formatting can take number: %d decimal: %f string: %s " % (89898989, 2.3, "testme")
print(message)