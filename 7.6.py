# Program to calculate the babysitter's wage

def main():
	hour_start = float(input("Enter the hour babysitting begun: "))
	minute_start = float(input("Enter the minute babysitting begun: "))
	hour_end = float(input("Enter the hour babysitting ended: "))
	minute_end = float(input("Enter the minute babysitting ended: "))

	if hour_start or hour_end < 21:
		time  =  (hour_end * 60 + minute_end) - (hour_start * 60 + minute_start)
		payment = time * 2,5 / 60
	else:
		payment = (hour_end * 60 + minute_end) - (hour_start * 60 + minute_start) 
	print(payment)

main()

