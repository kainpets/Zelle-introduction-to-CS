# program to count the sum of n natural numbers

def sumN(n):
    n = n*(n+1)/2
    return n

def sumNCubes(n):
    n = (n*(n+1)/2)**2
    return n
    
def main():
    n = int(input("Enter a natural number: "))
    print("The sum of first %d numbers is %d."% (n, sumN(n)))
    print("The sum of the cubes of the first %d numbers is %d."% (n, sumNCubes(n)))

main()
