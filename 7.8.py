# Program to compute the eligibility to be a US senator or
#   a US congressman


def main():
    age = int(input("Enter your age: "))
    citizenship = int(input("Enter years of citizenship: "))
    
    if age >= 30 and citizenship >= 9:
        print("You're eligible to be a US senator and congressman.")
    elif age >= 25 and citizenship >= 7:
        print("You're eligible to be a US congressman.")
    else:
        print("You're unable to be a US senator or congressman")

    
main()
