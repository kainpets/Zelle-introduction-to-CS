def verse1(num):
    verse = "The ants go maching " + num + " by " + num + ", hurrah, hurrah."
    print(verse)
    print(verse)

def verse2(num):
    verse = "The ants go maching " + num + " by " + num + ", "
    print(verse)

def verse3(activity):
    print("The little one stops to " + activity)

def verse4():
    print("""And they all go marching down,
To the ground, to get out, of the rain.
BOOM! BOOM! BOOM!""")

def main():
    verse1("one")
    verse2("one")
    verse3("suck his thumb.")
    verse4()
    verse1("two")
    verse2("two")
    verse3("climb a tree.")
    verse4()
    # etc...
    
main()
