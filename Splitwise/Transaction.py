class Transaction:

    transaction_id_count = 0

    @classmethod
    def get_transaction_id(cls):
        cls.transaction_id_count += 1
        return cls.transaction_id_count

    def __init__(self, from_user, to_user, amount):
        self.transaction_id = self.get_transaction_id()
        self.from_user =  from_user
        self.to_user = to_user
        self.amount = amount

    def __str__(self):
        return "trans_id : {}, from: {} , to: {}, amount: {}".format(self.transaction_id, self.from_user, self.to_user, self.amount)