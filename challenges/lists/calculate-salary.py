work_hours = [int(x) for x in input("Enter the hours worked separated by space: ").split(" ")]
wage = int(input("Enter the hourly rate: "))

total = sum(work_hours) * wage

print("The salary is " + str(total))

