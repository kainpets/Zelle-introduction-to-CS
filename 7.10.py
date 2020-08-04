# Program to compute the date of Easter in years 1900-2099


def main():
    print("This program calculates the date of Easter within specified\
    range of years")

    easter = int(input("Enter a year between 1900-2099: "))
    a = easter % 19
    b = easter % 4
    c = easter % 7
    d = (19 * a +24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    
    if easter >= 1900 and easter <= 2099:
        if easter == 1954 or easter == 1981 or easter == 2049 or easter == 2076:
            if (22 - 7 + d + e) > 31:
                print("The date of Easter is April", 22 + d + e - 31 - 7)
            else:
                print("The date of Easter is March", 22 + d + e - 7)
        elif 22 + d + e > 31:
            print("The date of Easter is April", 22 + d + e - 31)
        else:
            print("The date of Easter is March", 22 + d + e)
    else:
        print("Wrong year")

    
main()
