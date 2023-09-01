def decorator_fun(fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)

    return wrapper


@decorator_fun
def printing(msg):
    print(msg)


# wrapper = decorator(printing) when having the tag @decorator_fun then this line is not needed
# wrapper('Hello')

printing('Hello')
