# convert.py
#   A program to convert Celsius temps to Fahrenheit

def main():
    print("This program prints a table of Celsius and\
Fahrenheit degrees:")
    
    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "\t", fahrenheit)

main()
