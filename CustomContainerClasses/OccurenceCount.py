
# say i want make functionality that count's occurence of a key in a list.


def count_occurance(mylist):
    occ = {}
    for i in mylist:
        if i in occ.keys():
            occ[i] += 1
        else:
            occ[i] = 1
    return occ


mylist = [1,2,3,3,2,1,3,]
print(count_occurance(mylist))

# using method is one way, but say we want to add multiple functionalities like say
# get all odd occurances or even occurances, explicitly remove elements from end if
# count is greater than some threashold etc etc. So to achieve all such things creating a class
# is better.

class CountOccurances:

    def __init__(self, mylist):
        self.mylist = mylist

    def count_occurance(self):
        occ = {}
        for i in self.mylist:
            if i in occ.keys():
                occ[i] += 1
            else:
                occ[i] = 1
        return occ

    def remove_all_even(self):
        for i in self.mylist:
            if i % 2 == 0:
                self.mylist.remove(i)

k = CountOccurances(mylist)
print(k.count_occurance())
k.remove_all_even()
print(k.count_occurance())

# As long as the list is simple we don't have any benefit of maintaining a seperate class for this.
# Also in class If a list is sent, i can't modify it afterwards unless some functionality is added by me only.
# Also I have to write seperate functionality in class to get the length of list or add/remove item or print list items etc.


# So basically what we are doing here is creating another class that handles list and perform different functionality on it.
# Infact what better we can do is use the list container, make this class extend list container and all list functionality
# we will get + we can add our own functions.



class CountOccurancesExtended(list): # now here the class object itself is a list type so self will represent list only!!

    def __init__(self, mylist):
        super().__init__(mylist)

    def count_occurance(self):
        occ = {}
        for i in self:
            if i in occ.keys():
                occ[i] += 1
            else:
                occ[i] = 1
        return occ

    def remove_all_even(self):
        for i in self:
            if i % 2 == 0:
                self.remove(i)


print("................................ Using extended class..............................................................")
mynewlist = [1,2,3,4,5,1,2,3,4,5,1,2,]
k = CountOccurancesExtended(mynewlist)
print(k)
print(" so as we saw, if we print such object it will print list")
print("len == {}".format(k.__len__()))
k.append(40)
print("40 is appended")
print(k)
print("get index of 40")
print(k.index(40))
print(" so basically with this class we can do all that list container provides us")
print(k.count_occurance())
print(" we can even run our count occurance method on this..Its pretty cool, you can have your own custom list methods with what comes by deafault!!")

