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

def main():
    file = open("listOfSquares", "r").readlines()
    
    print(sumList(squareEach(toNumbers(file))))
 
main()
