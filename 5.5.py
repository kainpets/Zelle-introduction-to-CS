def main():
    name = input("Enter your name: ")
    nums = 0
    
    for char in name:
        nums = nums + ord(char.lower()) - ord('a') + 1
        
    print("The value of your name is: ", nums)

main()
