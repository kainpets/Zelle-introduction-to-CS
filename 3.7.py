import math

x1 = float(input("Enter the x for the first point: "))
y1 = float(input("Enter the y for the first point: "))
x2 = float(input("Enter the x for the second point: "))
y2 = float(input("Enter the y for the second point: "))
    
distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

print("The disatnce is: ", distance)
