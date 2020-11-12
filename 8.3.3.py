def fibo():
    lst = []
    i = 0
    total = 0
    while 999 not in lst:
        n = int(input("The loop stops after you enter 999: "))
        lst.append(n)
        print(lst)
        
    while lst[i] != 999:
        total += lst[i]
        i += 1
    print(total)
    
fibo()
