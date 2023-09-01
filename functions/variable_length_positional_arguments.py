def unlimited_params(*args):  # all arguments are parsed in the form of tuple
    print(args)


def f2(a, b, c):
    print(a, b, c)


def f3(a, b, c):
    return a ** a, b ** b, c ** c


unlimited_params()
unlimited_params(1, True, "Hi")

L = [1, 2, 3]

f2(*L)  # unpacking elements

t = f3(1, 2, 3)
print(t)
print(type(t))

x, y, z = f3(1, 2, 3)
print(x, y, z)
