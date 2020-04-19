# Say we want to sort a list of numbers but want to prioritize one group of number to come first

# We will use a normal sort function only, to this function we will pass a helper function
# helpers return value will be used for sorting each item.

# helper function will check if given number belongs to that particular group or not and can
# vary the sort key accordingly.

group = {2,3,4,5}

numbers = [2,4,5,7,9,6,1]

expected_output = [2,4,5,1,6,7,9]

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

sort_priority(numbers,group)
print("Output: " +  numbers.__str__())
print("Expected Output: " +  expected_output.__str__())

# As you can see its working as expected, why are we sending 0 when number is in group and 1 when it is not.

# Python compares tuples in specific ways it first compares index 0 variable and then index 1 variables and so on.

# first keys(tuple) will be generated for every number in numbers list
# for 2 --> (0,2) as 2 is in group
# for 1 --> (1,1) as 1 is not in group
# for 4 --> (0,4) as 4 is in group

# now (0,2) and (1,1) will be compared first 0 and 1 will be compared , 0 < 1 s0 tuple (0,2) will be kept before (1,1)
# if (0,2) and (0,4) are compared , at 0th index both have 0 so first index variable is comared and (0,2) is kept before (0,4)
# (0,4) and (1,1) compared, (0,4) will come before (1,1)

# (0,2), (0,4) (1,1) # this is how keys will be placed finally after sort and what sort will return is values corresponding to these
# 2,4,1 will be returned.

