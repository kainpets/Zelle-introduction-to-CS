#futval.py
#   A program to compute the value of an investment
#   carried years into the future while reinvesting
#   a fixed amount each year

def main():
    print("This program calculates the future value\
of an investment.")

    principal = eval(input("Enter the amount to invest each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter years of investment: "))
    investment = 0.0

    for i in range(years):
        investment = investment * (1 + apr) + principal
        
    print("The value in", years, "years is:", round(investment, 2))

main()
