def calculate_sum(num1, num2, num3=0):
    return num1 + num2 + num3


def add_item(item, l=[]):
    l.append(item)
    return l


# def calculate_sum_test(num1=0, num2, num3): #This is not allowed, default arguments should start from the right
#     return num1 + num2 + num3

result = calculate_sum(10, 20, 5)
print(result)

print(calculate_sum(5, 5, 3))

print(calculate_sum(num1=5, num2=5, num3=3))

print(calculate_sum(5, 5))

# print(calculate_sum(num1=5, num2=5, 3)) positional argument follows keyword argument

# l = [1, 2, 3]
# print(add_item(5, l))

print(add_item(10))  # default arguments are created only once
print(add_item(20)) # That's why 20 is appended to the list
