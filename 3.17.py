# Program to compute the square roots of a number provided by a user

import math

print("This program estimates the square root of a number")

num = float(input("Enter a number: "))
timesToGuess = int(input("Enter the number of times I can improve my algorithm: ")) 
guess = num/2
answer = math.sqrt(num)


for i in range(1, timesToGuess):
    guess = (guess + (num/guess))/2

finalAnswer = answer - guess

print("My guess is: ", guess)
print("The answer is: % 0.4f" % (answer))
print("I was this close to guessing correctly: %0.4f" % (finalAnswer))
