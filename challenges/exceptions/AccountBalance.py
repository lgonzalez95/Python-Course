from AccountBalanceException import AccountBalanceException

balance = 10000
min_balance = 5000


def withdraw(amount):
    global balance
    if (balance - amount) < min_balance:
        raise AccountBalanceException('Insufficient founds')
    else:
        balance -= amount


try:
    withdraw(5001)
except AccountBalanceException as e:
    print(e)
