def donald(animal):
    print("""Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
And on that farm he had a """ + animal + """, Ee-igh, Ee-igh, Oh!""")



def sound(par):
      print("With a " + par + ", " + par + " here and a "
            + par + ", " + par + " there. Here a " + par
            + ", there a " + par + ", "  + "everywhere a " + par + ", " + par + ".")

def end():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def main():
    donald("cow")
    sound("moo")
    end()
    donald("duck")
    sound("quack")
    end()
    donald("goose")
    sound("dick")
    end()
    donald("pig")
    sound("oink")
    end()
    donald("fox")
    sound("kaw kaw")
    end()

main()
