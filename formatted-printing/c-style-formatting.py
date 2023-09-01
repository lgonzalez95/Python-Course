"""
%s: Strings
%d: Decimal
%i: Integer
%o: Octal
%x: Hexadecimal
%f: Float
%F: Upper Float -> Exponents
%g: General form
"""


rollNumber = 10
name = "Juan"
avg = 78.9454

print("Student name is %s, his roll number is %d and average is %f" %(name, rollNumber, avg))
print("%2.3f" %avg)