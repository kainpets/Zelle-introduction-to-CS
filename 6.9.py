# Program the tells the user which grade he recieved based on their
#   test result using functions


def grade(score, result):
    result = "FFFFFFDCBAA"[score//10]
    return result

def main():
    score = int(input("Your score: "))
    result = 0
    print("Your grade: ", grade(score))

main()


