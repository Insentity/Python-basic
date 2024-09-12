class Account(object):
    

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.count_transaction = 0

    def deposit(self, amount):
        self.balance += amount
        self.count_transaction += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.count_transaction += 1

    def get_balance(self):
        return self._balance

    def dump(self):
        s = "%s, %s, balance: %s, transactions: %s" % (self.name, self.no, self.balance,
                                                       self.count_transaction)
        print(s)

def test_Account():
    acc = Account("Luan", "1020", 10000)
    acc.withdraw(5000)
    expected_balance = 5000
    msg = "Account value %s is not as expected %s" %(acc.balance, expected_balance)
    assert acc.balance == expected_balance, msg

    acc.deposit(10000)
    expected_balance = 15000
    msg = "Account value %s is not as expected %s" %(acc.balance, expected_balance)
    assert acc.balance == expected_balance, msg

if __name__ == '__main__':
    test_Account()