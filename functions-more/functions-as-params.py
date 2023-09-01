def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def fun_receiving_fun(fun, x, y):
    return fun(x, y)


print(fun_receiving_fun(add, 10, 14))
print(fun_receiving_fun(sub, 10, 14))
