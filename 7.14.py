# Program to 

from graphics import *
from math import *

def main():
    # gather input from user
    radius = float(input("Enter the radius: "))
    yIntercept = float(input("Enter the y intercept: "))

    # draw the graphics window
    win = GraphWin("window", 600,600)
    win.setCoords(-10,-10,10,10)
    center = Point(0,0)

    # draw the circle
    circle = Circle(center, radius)
    circle.draw(win)

    # draw the y-axis intercept
    y = Line(Point(-10, yIntercept), Point(10, yIntercept))
    y.draw(win)

    # find and color the interception points
    intPoint1 = abs(sqrt(radius**2 - yIntercept**2))
    interception1 = Point(intPoint1,yIntercept)
    interception1.setFill("red")
    interception1.setOutline("red")
    interception1.draw(win)
    
    intPoint2 = -(sqrt(radius**2 - yIntercept**2))
    interception2 = Point(intPoint2,yIntercept)
    interception2.setFill("red")
    interception2.setOutline("red")
    interception2.draw(win)
    
    # close the program after the last click
    win.getMouse()
    win.close()

    # print the x value of the points of intersection
    print("The values of the interception points: \n",intPoint1, intPoint2)

main()
