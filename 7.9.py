# Program to compute the date of Easter in years 1982-2048


def main():
    print("This program calculates the date of Easter within specified\
    range of years")

    easter = int(input("Enter a year between 1982-2048: "))
    a = easter % 19
    b = easter % 4
    c = easter % 7
    d = (19 * a +24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    
    if easter >= 1982 and easter <= 2048:
        if 22 + d + e > 31:
            print("The date of Easter is April", 22 + d + e - 31)
        else:
            print("The date of Easter is March", 22 + d + e)
    else:
        print("Wrong year")

    
main()
