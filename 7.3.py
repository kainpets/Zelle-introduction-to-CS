# Program to calculate results of 100 points quizes

def main():
	score = int(input("Enter your exam score: "))

	if score < 60:
		print("Your grade is an F")
	elif score < 70:
		print("Your grade is a D")
	elif score < 80:
		print("Your grade is a C")
	elif score < 90:
		print("Your grade is a B")
	else:
		print("Your grade is an A")

main()
