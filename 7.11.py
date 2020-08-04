# Program to calculate whether a given year is a leap year

def main():
    print("This program calucaltes whether given year is a leap year")
    year = int(input("Enter year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                print("This is not a leap year")
            else:
                print("This is a lap year")
        else:
            print("This is a lap year")
    else:
        print("This is not a leap year")

main()
