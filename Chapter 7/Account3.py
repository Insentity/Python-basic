class Account(object):
    
    # Initialize account
    def __init__(self, name, account_number, initial_amount):
        from datetime import datetime
        self.name = name
        self.transaction_ID = 1
        self.no = account_number
        self.transactions = [ { "Transaction ID": self.transaction_ID,
                                "Date & time": "%s" %datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                "balance": initial_amount,
                                "transaction amount": initial_amount,
                              }
                            ]
                            
    # Deposit to account
    def deposit(self, amount):
        from datetime import datetime
        self.transaction_ID += 1
        balance = self.transactions[-1]["balance"] + amount
        self.transactions.append(  {"Transaction ID": self.transaction_ID,
                                    "Date & time": "%s" %datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                    "balance": balance,
                                    "transaction amount": amount
                                    }
                                )
        
    
    # Withdraw from account
    def withdraw(self, amount):
        from datetime import datetime
        self.transaction_ID += 1
        balance = self.transactions[-1]["balance"] - amount
        self.transactions.append(  {"Transaction ID": self.transaction_ID,
                                    "Date & time": "%s" %datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                    "balance": balance,
                                    "transaction amount": -amount
                                    }
                                )
        

    # Show balance of account
    def get_balance(self):
        return self.transactions[-1]["balance"]
    

    # Print out transactions history
    def print_transactions(self):
        dict_list = self.transactions
        print_dictionary(dict_list)

    # Display Object data
    def dump(self):
        s = "User: %s, ID: %s, " % (self.name, self.no)
        print(s)
        print(self.transactions)


def print_dictionary(dicts):
    headers = dicts[0].keys()
    print(headers)
    for header in headers: print("%-25s" %header, end = "")
    print()
    for dict in dicts:
        for keys, values in dict.items():
            print("%-25s" %values, end = "")
        print()


# Test function
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


# Test in another .py file

# from Account3 import Account

# acc = Account('Luan', '1020', 10000)
# acc.deposit(5000)
# acc.withdraw(7000)
# acc.deposit(20000)
# acc.deposit(100000)
# acc.withdraw(50000)
# # print(acc.get_balance())
# acc.print_transactions()