"""
isupper
islower
istitle

isalnum: contains alpha characters or numbers
isalpha: contains alpha characters
isspace: if contains only space
isacii: if the string contains ascii codes

isidentifier: If the string is a valid variable name
isprintable: If the string can be printed

isdecimal: if the string contains decimal numbers 
isdigit: if the string contains powered numbers (except fractions)
isnumeric: if the string contains powered numbers (includes fractions)
"""

string = "Hello"

print(string.isupper())
print(string.islower())
print(string.istitle())

s1 = "abc123"
s2 = "abc"
s3 = " "
print()

print(s1.isalnum())
print(s1.isalpha())
print(s2.isalpha())
print(s3.isspace())
print(s3.isascii())
print(s1.isascii())

print()
s4 = '1Hello'
s5 = '\n Hello'
print(s5.isidentifier())
print(s2.isidentifier())
print(s5.isprintable())

print()
s6 = '123'
print(s6.isdecimal())
print(s6.isdigit())
print(s6.isnumeric())

print()
s7 = '8\u00b2'
print(s7)
print(s7.isdecimal())
print(s7.isdigit())
print(s7.isnumeric())

print()
s8 = '8\u00bd'
print(s8)
print(s8.isdecimal())
print(s8.isdigit())
print(s8.isnumeric())
