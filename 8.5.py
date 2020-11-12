def is_prime(a):
    
    return all(a % i for i in range(2, a))


def main():
    n = int(input("Enter a natural positive number to check\
f it's prime: "))
    if (is_prime(n)):
        print("The number " + str(n) + " is prime.")
    else:
        print("The number " + str(n) + " isn't prime.")
          
main()
