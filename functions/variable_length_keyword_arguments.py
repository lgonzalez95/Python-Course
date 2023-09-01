def fun(**kwargs):
    print(kwargs)


def mixed_arguments(a, b, *args, **kwargs):
    print(a, b, args, kwargs)


fun(name="Juan", age=1)

mixed_arguments(1, True, p=4, name="Juan", age=1)
