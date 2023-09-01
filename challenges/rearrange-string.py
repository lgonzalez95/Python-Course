string = input("Enter the string: ")

upper = ""
lower = ""

for i in string:
    if i.islower():
        lower += i
    else:
        upper += i

print(''.join(sorted(lower) + sorted(upper)))