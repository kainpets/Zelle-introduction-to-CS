def main():
    n = int(input("Enter a number of Fibonnaci sequence\
you'd like to know: "))

    current = 1
    previous = 1

    for i in range(n - 2):
        current += previous
        previous = current
        
    print(current)

main()
