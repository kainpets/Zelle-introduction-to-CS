# Program to calculate class standing from the number of credits earned

def main():
	credits = int(input("Enter the number of your credits: "))

	if credits < 7:
		print("You're a Freshman")
	elif credits >= 7:
		print("You're a Sophomore")
	elif credits >= 16:
		print("You're a Junior")
	elif credits >= 26:
		print("You're a Senior")

main()
