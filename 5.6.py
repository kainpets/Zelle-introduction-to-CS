def main():
    name = input("Enter your name: ")
    nums = 0
    letter = "".join(name.split())
    
    for char in letter:
        nums = nums + ord(char.lower()) - ord('a') + 1
        
    print("The value of your name is: ", nums)

main()
