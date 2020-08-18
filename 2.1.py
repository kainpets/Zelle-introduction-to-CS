# convert.py
#   A program to convert Celsius temps to Fahrenheit

def main():
    print("Hello, this program introduces itself and does nothing else.")
    celsius = eval(input("What is the Celsisu temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    exit = input("Press enter to exit")

main()
