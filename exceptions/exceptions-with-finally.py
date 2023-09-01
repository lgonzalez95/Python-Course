def div():
    try:  # in try section, add only code that can trigger an exception, nothing else
        a = int(input('Enter numerator: '))
        b = int(input('Enter denominator: '))
        c = a // b
    except ZeroDivisionError as err:
        raise ZeroDivisionError
    else:
        print('The result is ' + str(c))
    finally:
        print('Finally executed')


div()
