def main():

    investment = 10
    interest_rate = float(input("Enter annualized interest rate: "))
    result = 0
    condition = investment * 2
    while(investment < condition):
        
        result += 1
        investment = investment * (1 + interest_rate)
        
    print("You'll have to wait " + str(result) + " years.")
    
    return result
main()
