def main():
    print("This program calculates the future value of a x-year investment")


    # get the file names
    infileName = input("What file are the principal, apr, and years in? ")
    outfileName = input("What file should the results go in? ")
    
    # open the files
    bankData = open(infileName, "r")
    results = open(outfileName, "w")
    
    principal = float(input("Enter the intial principal: "))
    apr = float(input("Enter the annual interest rate (in decimal): "))
    years = int(input("Enter the number of years of investment: "))



    print("Year\tValue")
    print("--------------------")
    
    for i in range(years + 1):
        print("{0}\t${1:7.2f}".format(i,principal))
        principal = principal * (1 + apr)
    
    
main()
