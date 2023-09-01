def outer(name):
    def inner():
        print('Hello', name)
    return inner()


f = outer

f('Juancho')
