string = "Hello, how are you?"
string2 = "     Test    "
string3 = ".... ... ++aaapython ..."

# These methods don't modify the original string

print(string.ljust(50))
print(string.rjust(50))
print(string.center(50))

print("-------")

print(string2.lstrip())
print(string2.rstrip())
print(string2.strip())

print("-------")
print(string3.lstrip('.'))
print(string3.rstrip('.'))
print(string3.strip('.'))

print("-------")
print(string3.lstrip('. +'))
print(string3.rstrip('. +'))
print(string3.strip('. +'))