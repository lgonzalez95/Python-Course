def outer(name):
    def inner():
        print('Hello', name)
    inner()


f = outer

f('Juan')
# inner() not found since inner function can be executed only within its parent function
