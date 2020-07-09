# Program to calculate the area of a triangle given the length of its
#   three sides as parameters

import math
from graphics import *


def square(x):
    return x ** 2

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p2.getY()))
    return dist

def triangleArea(a, b, c):
    s = (a+b+c) / 2.0
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 2), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter and area of the triangle
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p3,p1)
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText(""" Perimeter is: %0.2f\nThe area is: %0.2f"""
                    % (perim, triangleArea(d1, d2, d3)))

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
