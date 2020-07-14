# Program to convert strings which are numbers to numbers using functions

def toNumbers(strList):
    newList = []
    for i in strList:
        i = int(i)
        newList.append(i)
    return newList


def main():
    strList = ["1", "2", "3"]
    print(strList)
    print(toNumbers(strList))

main()
    
