# Program to compute the windchill index
import math

def main():
    temperature = - 20
    velocity = 0
    formula = 35.74 + 0.6215 * temperature - 35.75 * \
              (math.pow(velocity, 0.16))\
              + 0.4275 * t *(math.pow(velocity, 0.16))

    print(formula)

main()
