# Program to compute the nth Fibonnaci number


def main():
    print("This program computes the nth Fibonacci number")
    n1 = 0
    n2 = 1
    count = 0
    n = int(input("Enter the nth number of the Fibonacci sequence: "))
    fibonacci = n - 1 + n - 2
    
    if n <= 0:
        print("Enter a positive integer")
    elif n == 1:
        print("1")
    else:
        while count < n:
            print(n1)
            num = n1 + n2
            n1 = n2
            n2 = num
            count = count + 1

main()
