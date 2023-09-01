email = input ("Enter the email")

data = email.partition("@")
print("User id", data[0])
print("domain", data[2])


data = email.find("@")

print("User id", email[0:data])
print("domain", email[data+1:])