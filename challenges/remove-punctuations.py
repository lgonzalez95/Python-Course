punctuations = "' ! () . , ; : \ /"
finalString=""

string = input("Enter a string: ")

for i in string:
    if i not in punctuations:
        finalString+= i


print("Your final string is", finalString)