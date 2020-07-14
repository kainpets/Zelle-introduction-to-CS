# Program to return the sum of the numbers in the list

def sumList(nums):
    count = 0
    for i in nums:
        count += i
    return count      

def main():
    nums = [1, 2, 133]
    print(sumList(nums))

main()
