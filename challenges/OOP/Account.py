class MinimumBalanceError(Exception):
    pass


class Account:
    min_balance = 1000

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < Account.min_balance:
            raise MinimumBalanceError(
                'Unable to withdraw the money since the balance falls below ' + str(Account.min_balance))
        else:
            self.balance -= amount

    def show_details(self):
        print('Name: ' + self.name)
        print('Account Number: ' + self.account_number)
        print('Balance: ' + str(self.balance))


a = Account('Pepe', 'ACC-1203-3242', 2000)
a.deposit(500)
a.show_details()
a.withdraw(1500)
a.show_details()
a.withdraw(500)
