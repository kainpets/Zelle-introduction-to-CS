import math

point1 = float(input("Coordinates of the first point? "))
point2 = float(input("Coordinates of the second point? "))
point3 = float(input("Coordinates of the third point? "))
point4 = float(input("Coordinates of the fourth point? "))

slope = (point4 - point2) / (point3 - point1)

print("The slope is: ", slope)
