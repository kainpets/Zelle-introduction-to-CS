# average5.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(FileName, "r")
    total = 0.0
    n = 0
    for line in infile:
        total = total + float(line)
        n = n + 1
    print("\nThe average is", total / n)

main()