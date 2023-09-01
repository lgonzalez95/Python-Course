def factorial_of_number(num):
    if num == 0:
        return 1
    else:
        result = num * factorial_of_number(num - 1)
        return result


print(factorial_of_number(5))
