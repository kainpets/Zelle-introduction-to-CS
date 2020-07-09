import math

diameter = float(input("Enter the diameter of your pizza: "))
price = float(input("Enter the price of your pizza: "))

def areaOfPizza(diameter):
    return math.pi * (diameter/2)**2

def costSquareInch(diameter, price):
    return price / areaOfPizza(diameter)

def main():
    print("The area of the pizza is %0.4f" % (areaOfPizza(diameter)))
    print("The cost of square unit of pizza is %0.4f" % (costSquareInch(diameter, price)))
    input("Press enter to quit")
    
main()
