# Program to create acronyms from user provided strings using functions

def acronym(phrase):
    acr = ""
    for word in phrase.split():
        acr = acr + word[0]
        acr = acr.upper()
    return acr

def main():
    phrase = input("Enter the phrase you want acronym of: ")
    print("", acronym(phrase))
    
main()


