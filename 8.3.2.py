def fibo():
    n = int(input("Enter a positive integer: "))
    total = 0
    i = 0
    while i <= n:
        if i % 2 != 0:
            total += i
        i += 1
    print(total + 2 * n - 1)

fibo()
