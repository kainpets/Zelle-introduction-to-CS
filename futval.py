
def main():
    print("This program calculates the future value of a x-year investment")

    
    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the annual interest rate (in decimal): "))
    years = eval(input("Enter the number of years of investment: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is: ", principal)
    
main()
