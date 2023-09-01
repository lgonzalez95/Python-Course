"""
capitalize: Makes upper case only the first letter:
lower: Makes all the string in lower case
upper: Makes all the string in upper case
title: Makes every letter of every letter capital
swapcase: Swaps the letters, upper becomes lower and lower becomes upper
casefold: Similar than lower but useful for caseless strings
"""
string = "hello THERE baby!"

print(string.capitalize())
print(string.lower())
print(string.upper())
print(string.title())
print(string.swapcase())
print(string.casefold())

s1 = "Bu\u00DF"
print(s1)
print(s1.casefold() == "Buss".casefold())