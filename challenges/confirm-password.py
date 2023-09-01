password = input("Enter your password: ")
confirm = input("Confirm your password: ")

if password == confirm:
    print("The password was confirmed")
elif(password.casefold() == confirm.casefold()):
    print("Please check the cases")
else:
    print("Confirmation failed")