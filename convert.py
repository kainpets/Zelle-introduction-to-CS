"""Modify the convert program with a loop so that it executes 5 times\
before quitting. Each time trough the loop, the program should get
another temperature from the user and print the converted value"""


def main():
    for i in range(0,5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
