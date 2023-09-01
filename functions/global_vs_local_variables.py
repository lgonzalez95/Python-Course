g = 10


def locals_sample():
    x, y, z, = 10, 15, 20
    print(locals())  # locals function returns all local variables


locals_sample()


def fun2():
    global g
    g = g + 5  # use global to modify global variables
    print(g)


fun2()

print(globals()) # returns global variables, functions, etc

def fun1():
    g = g + 5  # A function cannot modify global variables without global keyword
    print(g)


fun1()


