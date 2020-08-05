# Program to confirm whether gien data is valid

def main():
    print("Date Validator\n")
    print("Enter date using format MM/DD/YEAR")
    month, day, year = input("Date(MM/DD/YEAR): ").split("/")
    month = int(month)
    day = int(day)
    year = int(year)

    # special case for February in leap years
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 != 0:
                    if day > 29:
                        print("Invalid date")
        elif day > 28:
            print("Invalid date")
    # months that have 30 days
    elif month == 4:
        if day > 30:
            print("Invalid date")
    elif month == 6:
        if day > 30:
            print("Invalid date")
    elif month == 9:
        if day > 30:
            print("Invalid date")
    elif month == 11:
        if day > 30:
            print("Invalid date")
    # rest of months
    elif month > 12 or day > 31:
        print("Invalid date")
    else:
        print("This is a valid date")
        
main()

