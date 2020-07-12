# Program to create acronyms from user provided strings

def main():
    words = input("Enter words to be acronymed: ")
    acronym = ""
    
    for word in words.split():
        acronym = acronym + word[0]
    acronym = acronym.upper()
        
    print(acronym)

main()
