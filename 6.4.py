from math import *

def sphereArea(radius):
    area = 4 * pi * radius **2
    return(area)

def sphereVolume(radius):
    volume = 4/3 * pi * radius **3
    return(volume)


def main():
    radius = int(input("Enter radius: "))
    print("Area: %0.2f" % (sphereArea(radius)), "volume: %0.2f" % (sphereVolume(radius)))

main()
