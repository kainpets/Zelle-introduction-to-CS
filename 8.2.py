def main():

    for velocity in range(0, 50, 5):
        print("\t")
        for temperature in range(-20, 60, 10):
            index = 35.74 + 0.6215 * temperature - 35.75 * (velocity *0.16 * 0.16) + 0.4275 * (temperature* 0.16 * 0.16)
            print(str(round(velocity, 2)) + "\t", end='')
            print(str(round(index, 2)), end='')



    
main()
