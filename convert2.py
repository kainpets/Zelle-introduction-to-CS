
def main():
    celsius = 0
    for celsius in range(0, 100, 10):
        fahrenheit = 9/5 * celsius + 32
        celsius = celsius + 10
        print("Celsius", celsius, "Fehrenheit", fahrenheit, sep="\t")

    
main()
