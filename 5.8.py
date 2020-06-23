def main():
    # get the name, message, key and set the alphabet
    message = input("Enter your message: ")
    key = int(input("Enter the value of your "
                    "encryption/decryption key: "))
    alphabet = "abcedghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newMessage = ""

    # get the letter of each word from message
    letter = "".join(message.split())

    for char in letter:
        # find the position of the letter in the alphabet
        position = alphabet.find(char)
        # add the key value to the position
        newPosition = position + key
        # assign the encrypted/decrypted message to a variable
        newMessage = newMessage + alphabet[newPosition]

        
    print("Your encrypted/ decrypted message is: ", newMessage)

main()
