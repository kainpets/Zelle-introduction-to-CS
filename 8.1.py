# Program to compute the nth Fibonnaci number

def main():
    print("This program computes the nth Fibonacci number")
    n1 = 0
    n2 = 1
    count = 0
    n = int(input("Enter the nth number of the Fibonacci sequence: "))
    fibonacci = n - 1 + n - 2

    
    
    while True:
        if n <= 0:
            n = int(input("Enter a postivie number: "))
        elif n == 1:
            print("0")
            break
        else:
            while count < n:
                print(n1)
                num = n1 + n2
                n1 = n2
                n2 = num
                count = count + 1
            break

main()
