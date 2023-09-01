class CurrencyConverter:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_rate(self, rate):
        self.rate = rate

    def get_rate(self):
        return self.rate

    def convert(self, amount):
        return self.currency + ' conversion is: ' + str(amount * self.rate)


c = CurrencyConverter('USD', 70)
print(c.convert(100))
