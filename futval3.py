def main():
    principal = eval(input("Principal investment: "))
    rate = eval(input("Yearly interest rate: "))
    periods = eval(input("Number of times the interest is compounded each year: "))
    years = eval(input("Number of years for the investment: "))

    comPeriods = rate / periods 
    
    for i in range(periods * years):
        principal = (principal) * (1 + comPeriods) 
        
    print("The value in", years, "years is: ", principal)
    
main()
