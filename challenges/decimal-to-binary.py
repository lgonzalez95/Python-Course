numToConvert = int(input("Enter the decimal number to be converted to binary: "))
bin = ""

while numToConvert > 0:
    remainder = numToConvert % 2
    numToConvert = numToConvert // 2
    bin = str(remainder) + bin
print("The binary num is", bin)