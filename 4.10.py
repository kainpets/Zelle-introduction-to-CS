from graphics import *
from math import *

def main():    
    # draw the graphics window
    win = GraphWin("window", 600,600)
    win.setCoords(-10,-10,10,10)

    # gather mouse clicks from the user
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    corner3 = win.getMouse()

    # draw the triangle
    triangle = Polygon(corner1, corner2, corner3)
    triangle.draw(win)

    # close the program after the last click
    win.getMouse()
    win.close()

    # calculate the perimeter and area of the rectangle
    length = abs(corner1.getX() - corner2.getX())
    width = abs(corner1.getY() - corner2.getY())
    area = length * width
    perimeter = 2 * (length + width)

    # print the x value of the points of intersection
    print("The area is: ",area,"The perimeter is: ", perimeter)

main()
