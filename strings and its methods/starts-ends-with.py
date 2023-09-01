email = "test@gmail@.com"

print(email.endswith("gmail.com"))
print(email.startswith("test"))

print(email.removeprefix("test"))
print(email.removesuffix("com"))

print(email.partition("@"))
print(email.rpartition("@"))