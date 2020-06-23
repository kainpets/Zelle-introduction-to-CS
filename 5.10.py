def main():
    # program to count the average word length in a sentence entered by
    #   the user
    print("Program to count the number of words in a sentence")
    sentence = input("Your sentence: ")
    total = 0

    # count the occurence of spaces in sentence
    total = total + sentence.count(" ") + 1
    
    print("The number of words in your sentence is: ", total)  
    
main()
