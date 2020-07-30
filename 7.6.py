# Program to calculate the speeding ticket policy in Podunksville

def main():
	limit = int(input("What was the speed limit? "))
	speed = int(input("Enter the speed you were going at: "))
	fine = 50

	if speed >= limit:
		fine = fine + (speed-limit) * 5
		if speed >= 90:
			fine + 200
		print("You'll have to pay", fine)
	else:
		print("You don't have to pay.")

main()