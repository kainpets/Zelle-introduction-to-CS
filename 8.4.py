def main():
    x = int(input("Enter a natural positive number: "))

    while x > 1:
        if x % 2 == 0:
            x /= 2
            print(x)
        else:
            x = 3 * x + 1
            print(x)


main()
