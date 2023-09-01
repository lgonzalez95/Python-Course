num_one = int(input("Enter the number one: "))
num_two = int(input("Enter the number two: "))

result = num_two - num_one
if result < 0:
    result = result*-1
print(result)
