import math

radius = int(input("Radius of the sphere: "))

volume = 4 / 3 * math.pi * radius**3
area = 4 * math.pi * radius**2

print("Volume: ", volume, "\nArea: ", area, sep="\t")
