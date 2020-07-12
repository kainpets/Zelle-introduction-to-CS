# Program to compute the square roots of a number provided by a user using a function

import math

print("This program estimates the square root of a number")

def nextGuess(guess, x):
    guess = (guess + (x/guess))/2
    return guess

def improve(x, chances):
    guess = x / 2
    for i in range(chances):
        guess = nextGuess(guess, x)
    return guess

def main():
    x = float(input("Enter the number to take the root of: "))
    chances = int(input("Enter the number of times I can improve my guess: "))
    print("The square root is: ", improve(x, chances))
    
main()
