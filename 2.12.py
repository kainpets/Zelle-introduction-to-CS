# A calculator

def main():
    print("This is a calculator.")
    print("Simply crash the program to exit.")

    for i in range(0, 100):
        num = eval(input("Enter your expression here: "))
        print(num)

main()
