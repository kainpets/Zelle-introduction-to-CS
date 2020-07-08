
def main():
    principal  = eval(input("Enter the amount of money to invest: "))
    interest = eval(input("Interest rate: "))
    years = eval(input("Enter the number of years for your investment: "))
    fixed = eval(input("Enter the fixed amount to add to your investment each year: "))

    
    for i in range(years):
        principal = principal + fixed
        principal = principal * (1 + interest)
        
    print("The value in", years, "years is: ", principal)
    
main()
