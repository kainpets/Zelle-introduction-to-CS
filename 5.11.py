def main():
    print("This program illustrates a chaotic function")

    num1 = float(input("Enter a number beween 0 and 1: "))
    num2 = float(input("Enter a number beween 0 and 1: "))
    iterations = int(input("Enter the number of iterations: "))
    
    print("index \t" + " "+ str(num1) + "\t\t"  + " " + str(num2))
    print("------------------------------")
    
    for i in range(iterations):
        num1 = 3.9 * num1 * (1 - num1)
        num2 = 3.9 * num2 * (1 - num2)
        print("{0} \t {1:5f} \t {2:5f}".format(i+1, num1, num2))

main()
