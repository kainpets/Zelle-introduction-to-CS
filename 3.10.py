import math

height = float(input("The height of the ladder: "))
angle = float(input("The angle of the ladder: "))

radians = (math.pi / 180) * angle

length = height / math.sin(radians)

print(length)


