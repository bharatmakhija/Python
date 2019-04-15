
class user:

    def __init__(self, name, age, disabled = False):
        self.name = name
        self.age = age
        self.disabled = disabled # we can keep default parameters in constructor like this!!

    def __str__(self):
        return "name: {} , age: {}, disabled: {} ".format(self.name, self.age, self.disabled)

basic_user = user('first', 12)
print(basic_user)

# say i want to extend the user class and create a prime user.

class prime_user(user): # this is how we extend

    def __init__(self, name, age):
        # here first we call the constructor of a super class
        super().__init__(name,age) # This is how super-object is called.
        self.prime = True
        self.plan = None

    def add_plan(self, plan):
        self.plan = plan

    def print_parent_str(self):
        return super().__str__() # we can access any one parent up method like this.

    def __str__(self):
        return "name: {} , age: {}, prime: {}, plan: {} ".format(self.name, self.age, self.prime, self.plan)



p_usr = prime_user('bharat',22)
p_usr.add_plan(200)
print(p_usr)
print(p_usr.print_parent_str())