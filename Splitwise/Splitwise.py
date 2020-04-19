from User import User
from Group import Group
from Transaction import Transaction

class Splitwise:

    def __init__(self):
        self.users = {}
        self.groups = {}
        self.transactions = {}

    def create_users(self, users):
        for user_str in users:
            user = User.get_user_from_str(user_str)
            print(user)
            self.users[user.id] = user

    def create_test_users(self):
        users = ['Bharat-bharatmasky@gmail.com-3213211231', 'Ankita-afafasdasf@gmail.com-1231233211',
                 'Piyush-afafasdasf@gmail.com-1231233211']
        self.create_users(users)


    def create_groups(self):
        group = Group.get_group_for_users([key for key, value in self.users.items()])
        print(group)
        self.groups[group.group_id] = group

    def create_transaction(self,from_user, to, amount):
        transaction = Transaction(from_user,to,amount)
        self.transactions[transaction.transaction_id] = transaction

    def perform_transactions(self):
        amount = float(input('enter amount \n'))
        paid_by = int(input('who paid user_id \n'))
        other_user = int(input('other userid \n'))
        payer_owns = float(input('how much payer owns \n'))
        if payer_owns > amount:
            raise ValueError('Value cannot exceed amount')
        description = input('description \n')
        self.create_transaction(other_user, paid_by, amount - payer_owns)
        return int(input('do you want to continue adding transactions \n'))


    def show_results(self):
        k = int(input('enter user id \n'))
        user_has_to_pay = {}
        user_will_get = {}
        for _, trans in self.transactions.items():
            if trans.from_user == k:
                if trans.to_user not in user_has_to_pay.keys():
                    user_has_to_pay[trans.to_user] = 0
                user_has_to_pay[trans.to_user] += trans.amount
            if trans.to_user == k:
                if trans.from_user not in user_will_get.keys():
                    user_will_get[trans.from_user] = 0
                user_will_get[trans.from_user] += trans.amount

        for user_id, amount in user_has_to_pay.items():
            user = self.users[user_id]
            print("You own user {} amount :{}".format(user.name, amount))

        for user_id, amount in user_will_get.items():
            user = self.users[user_id]
            print("user {} owns you amount :{}".format(user.name, amount))

    def run(self):
        self.create_test_users() # Instead we should call create users
        self.create_groups()
        k = input('perform transactions 1/0 \n')
        while(int(k) == 1):
          k = self.perform_transactions()
        t = 1
        while(t == 1):
            self.show_results()
            t = int(input('do you want to see other users result \n'))

k = Splitwise()
k.run()