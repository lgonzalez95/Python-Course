class Rational:
    def __init__(self, n=1, d=1):
        self.n = n
        self.d = d

    def __add__(self, other):
        s = Rational()
        s.n = self.n * other.d + self.d * other.n
        s.d = self.d * other.d
        return s

    def __str__(self):
        return str(self.n) + '/' + str(self.d)


r1 = Rational(2, 3)
r2 = Rational(2, 5)
sum = r1 + r2
print(sum)
