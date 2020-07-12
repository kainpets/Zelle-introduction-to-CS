# Program to modify the list by squaring each entry

def squareEach(nums):
    newList = []
    for i in nums:
        i = i**2
        newList.append(i)
    return newList

def main():
    nums = [1, 2, 3, 4, 5, 6]
    print("", squareEach(nums))
    
main()


