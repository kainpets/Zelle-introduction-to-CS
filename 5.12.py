
def main():
    print("This program calculates the future value of a x-year investment")

    
    principal = float(input("Enter the intial principal: "))
    apr = float(input("Enter the annual interest rate (in decimal): "))
    years = int(input("Enter the number of years of investment: "))

    print("Year\tValue")
    print("--------------------")
    
    for i in range(years + 1):
        print("{0}\t${1:7.2f}".format(i,principal))
        principal = principal * (1 + apr)
    
    
main()
