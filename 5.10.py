def main():
    # program to count the average word length in a sentence entered by
    #   the user
    print("Program to count the average length of words in a sentence")
    sentence = input("Your sentence: ")
    letters = 0
    words = 0

    for i in sentence.split():
        letters = letters + len(i)
        words = words + 1

    average = letters/words
    
    print("The average word length in your sentence is: ", average)  
    
main()
