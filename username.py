# username.py
# Simple string processing program to generate usernames.

def main():
    print("This program generates computer usernames.")

    # get user's first and last names
    first = input("Please enter your first name (in lowercase): ")
    last = input("Please enter your last name (in lowercase): ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    # output the username
    print("Your username is:", uname)

main()
