# Program to compute the square roots of a number provided by a user using a function

import math

print("This program estimates the square root of a number")

def nextGuess(guess, x):
    guess = (guess + (x/guess))/2

def main():
    x = float(input("Enter a number: "))
    guess = x/2
    answer = math.sqrt(x)
    print("My guess is: ", nextGuess(x))
    print("The answer is: % 0.4f" % (answer))
    #print("I was this close to guessing correctly: %0.4f" % (finalAnswer))


main()
