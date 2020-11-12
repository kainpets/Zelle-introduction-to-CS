#   A program to compute the value of an investment
#   carried years into the future with accruing interest

def main():
    print("This program calculates the future value of a x-year investment")

    
    principal = eval(input("Enter the intial principal: "))
    years = eval(input("Enter the number of years of investment: "))
    rate = eval(input("Enter yearly rate of interest: "))
    periods = eval(input("Enter number of times that the interest \
is compounded each year: "))
    
    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The value in", years, "years is: ", round(principal, 2))

main()

