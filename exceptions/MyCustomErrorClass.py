class MyCustomErrorClass(Exception):
    def __init__(self):
        self.msg = msg

    def __str__(self):  # return exception message here
        return 'Creating my exception '


try:
    raise MyCustomErrorClass('My error')
except MyCustomErrorClass as e:
    print(e)
