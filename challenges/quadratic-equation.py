import math
#eg: ax^2 + bx + c = 0

a = float(input("Enter the a value: "))
b = float(input("Enter the b value: "))
c = float(input("Enter the c value: "))

r1 = (-b + math.sqrt(b**2 - 4* a * c)) / 2 * a 
r2 = (-b - math.sqrt(b**2 - 4* a * c)) / 2 * a 

print("r1 is ", r1)
print("r2 is ", r2)