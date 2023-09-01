from NegativeAgeException import NegativeAgeException


def stage(age):
    if age < 0:
        raise NegativeAgeException("The age should not be negative")
    elif age < 13:
        print('Kid')
    elif 13 <= age < 19:
        print('Teen')
    elif 10 <= age < 50:
        print('Young')
    else:
        print('Old')


try:
    stage(-3)
except NegativeAgeException as err:
    print(err)
