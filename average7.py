# average6.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(FileName, "r")
    total = 0.0
    n = 0 
    line = infile.readline().strip()
    while line != "":
    	# update sum and count for values in line
    	items = line.split(",")
    	for xStr in items:
    		total = total + float(xStr)
    		n = n + 1
    	line = infile.readline().strip()
    print("\nThe average is", total / n)

main()