# c03ex13.py
#    Sum of numbers entered by the user.

def main():
    print("This program allows you to total up some numbers")
    print()

    n = int(input("How many numbers do you have? "))
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total = total + num

    print()
    print("The sum of the numbers is:", total)

main()

