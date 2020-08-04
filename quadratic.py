<<<<<<< HEAD
# quadratic5.py

import math

def main():
	print("This program finds the real solutions to a quadratic\n")

	try:
		a = float(input("Enter coefficient a: "))
		b = float(input("Enter coefficient b: "))
		c = float(input("Enter coefficient c: "))
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
	except ValueError:
		print("\nNo real roots")
		
main()
=======
# quadratic.py
#   A program that computes the real roots of a quadratic equation.
#   Note: this program crashes if the equation has no real roots.

import math

def main():
    print("This program finds the real solutions to a quadratic\n")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b + discRoot) / (2 * a)
>>>>>>> f1459b8c91c614d1bdbb85cd22970115c10aa457
