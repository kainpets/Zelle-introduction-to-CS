# Program to calculate whether a given year is a leap year

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                return False
            else:
                return True
        else:
            return True
    else:
        return False


def main():
    print("This program calucaltes whether given year is a leap year")
    year = int(input("Enter year: "))
    
    if leapYear(year):
        print(year,"is a leap year")
    else:
        print(year, "is not a leap year")
        
if __name__ == '__main__':
    main()
