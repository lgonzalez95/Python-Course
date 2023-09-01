class Arith:
    def sum(self, x, y, z=None):
        if z is None:
            return x + y
        else:
            return x + y + z


a = Arith()
print(a.sum(10, 20, 30))
print(a.sum(10, 20))
