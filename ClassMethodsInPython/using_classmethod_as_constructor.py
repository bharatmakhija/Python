class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def create_employee_from_str(cls, employee_str, split_param = '-'):
        name, age, salary = employee_str.split(split_param)
        return cls(name,age,salary)

    def __str__(self):
        return "name: {}, age: {} , salary: {}".format(self.name,self.age,self.salary)

new_employee = Employee.create_employee_from_str('BHARAT-23-1200012')
print(new_employee)