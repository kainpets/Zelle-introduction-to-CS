def fibo():
    n = int(input("Enter a positive integer: "))
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1
    print(total)

fibo()
