roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
number = input('Enter roman number in upper cases: ')

convertedNum = 0
x = 0

while (x < len(number)):
    if x+1 < len(number) and roman[number[x]] < roman[number[x+1]]:
        convertedNum += roman[number[x+1]] - roman[number[x]]
        x += 2
    else:
        convertedNum += roman[number[x]]
        x += 1
    print(convertedNum)
   
print('The number is ' + str(convertedNum))
