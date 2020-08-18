# convert.py
#   A program to convert Celsius temps to Fahrenheit

def main():
    print("This program converts temperature in Celsius to Fahrenheit")
    
    for i in range(5):
        celsius = eval(input("What is the Celsisu temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
