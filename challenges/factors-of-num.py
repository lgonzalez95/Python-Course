num = int(input("Enter a number to show its factors: "))

for x in range(1, num+1):
   if num%x == 0:
      print(x)
   else:
      pass