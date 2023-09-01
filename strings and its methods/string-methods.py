string = "Hello, how are you?"
print(type(string))




#str.find(sub, initialIndex, endIndex)
#str.rfind(sub, initialIndex, endIndex)
print(string.find("o"))
print(string.find("o", 5))

print(string.rfind("o"))
print(string.rfind("o", 17))


# count
print(string.count("o"))

#str.index(sub, initialIndex, endIndex)
print(string.find("k")) # throws -1 when not found
print(string.index("k")) # throws exception when not found



#print(dir(str))
#print(help(str.find))