import math

hydrogen = float(input("Enter the number of hydrogen atoms: "))
carbon = float(input("Enter the number of carbon atoms: "))
oxygen = float(input("Enter the number of oxygen atoms: "))

hydrogen = 1.00794 * hydrogen
carbon = 12.0107 * carbon
oxygen = 15.9994 * oxygen

print("The molecular weight of this comopund is: ", hydrogen + carbon + oxygen, "grams per mole")
