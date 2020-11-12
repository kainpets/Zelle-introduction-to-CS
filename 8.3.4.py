def fibo():
    n = int(input("Enter a whole number: "))
    count = 1
    while (n // 2) != 1:
        n //= 2
        count += 1

    print(count)
fibo()
