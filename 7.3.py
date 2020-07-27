# Program to grade exam results

def main():
	score = int(input("Enter your exam score (0-5): "))

	if score == 5:
		print("You scored an A")
	elif score == 4:
		print("You scored a B")
	elif score == 3:
		print("You scored a C")
	elif score < 2:
		print("You scored an F")
	else:
		print("Wrong input.")

main()