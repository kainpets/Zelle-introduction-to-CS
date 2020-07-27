# Program to calculate the total wages for the week

def main():
    hours_worked = float(input("Enter the number of hours worked this week: "))
    hourly_rate = float(input("Enter the hourly rate: "))
    hours_overtime = hours_worked - 40
    total = hours_worked * hourly_rate

    if hours_worked > 40:
        total_overtime = hours_overtime * hourly_rate * 1.5
        total = 40 * hourly_rate + total_overtime

    print("You've earned " + str(total) + " $ this week")

main()