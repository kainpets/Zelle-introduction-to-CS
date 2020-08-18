#futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculates the future value\
of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter years of investment: "))

    for i in range(years):
        principal = principal * ( 1 + apr)

    print("The value in", years, "years is:", round(principal, 2))

main()
