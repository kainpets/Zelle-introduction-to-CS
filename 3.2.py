import math

diameter = int(input("Enter the diameter of your pizza: "))
price = int(input("Enter the price of your pizza: "))

radius = diameter / 2
area = math.pi * radius**2

print("The cost of square inch of your pizza is: ", price / area)
