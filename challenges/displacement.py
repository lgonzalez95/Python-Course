
initialVelocity = int(input("Enter the initial velocity: "))
finalVelocity = int(input("Enter the final velocity: "))
acceleration = int(input("Enter the acceleration: "))

area = ((finalVelocity**2)-(initialVelocity**2)) / (2 * acceleration)
print("The acceleration is ", area)