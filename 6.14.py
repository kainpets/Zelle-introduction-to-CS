# Program to compute the sum of squares of numbers read from a file using functions
#   from 3 previous exercises

def toNumbers(strList):
    newList = []
    for i in strList:
        i = float(i)
        newList.append(i)
    return newList

def squareEach(nums):
    newList = []
    for i in nums:
        i = i**2
        newList.append(i)
    return newList

def sumList(nums):
    count = 0
    for i in nums:
        count += i
    return count
# The function doesn't work but neither does the code answer given by the author
#   The cause might be the fact the input file isn't specified

def main():
    file = open("listOfSquares", "r").readlines()
    print(sumList(squareEach(toNumbers(file))))
 
main()
