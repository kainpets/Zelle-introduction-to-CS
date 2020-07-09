# Program to compute the nth Fibonacci number

import math

print("This program computes the nth Fibonacci number")


def fibo(n):
    num =((((1 + math.sqrt(5))/2)**n) - (((1 - math.sqrt(5))/2)**n))/ math.sqrt(5)
    return num    

def main():
    n = int(input("Enter a number: "))    
    print("%d" % fibo(n))
    return fibo(n)

main()


