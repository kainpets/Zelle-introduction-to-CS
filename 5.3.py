# Program the tells the user which grade he recieved based on their
#   test result

def main():
    score = int(input("Your score: "))
    grade = "FFFFFFDCBAA"[score//10]
    print("Your grade: ", grade)

main()
