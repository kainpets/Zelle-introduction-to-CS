import math

time = float(input("Enter the between seeing the lightening and hearing it (in seconds): "))

speed = 1100 * time
miles = speed / 5280

print("The lightening is: ", miles, "miles away")
