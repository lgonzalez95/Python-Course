s1= input("Enter the first string: ")
s2= input("Enter the second string: ")

if len(s1) != len(s2):
    print("The strings are not an anagram")
else:
    for x in s1:
        if x not in s2:
            print("The strings are not an anagram")
            break
    else:
        print("The strings are an anagram")
