word = input("Enter a string: ")

if word.casefold() == word[::-1]:
    print("The word is palindrome")
else:
    print("The word is not palindrome, I will make it")
    print("Your palindrome is:", word + word[::-1])


