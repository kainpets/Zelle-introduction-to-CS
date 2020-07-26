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