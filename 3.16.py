# Program to compute the nth Fibonacci number

import math

print("This program computes the nth Fibonacci number")

num = int(input("Enter an integer: "))

fibo =((((1 + math.sqrt(5))/2)**num) - (((1 - math.sqrt(5))/2)**num))/ math.sqrt(5)
print("%d" % fibo)    

