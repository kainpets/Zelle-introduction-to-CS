# Program to calculate the Body Mass Index

def main():
	weight = float(input("Enter your weight in pounds: "))
	height = float(input("Enter your height in inches: "))
	bmi = round(weight * 720 / height**2, 1)

	print("Your BMI is: ", bmi)
	if bmi <= 25:
		print("That's healthy!")
	elif bmi < 19:
		print("Watch out! That's unhealthy")
	else:
		print("Watch out! That's unhealthy")

main()
