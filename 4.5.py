from graphics import *

def main():
    # set the graphics window
    win = GraphWin("", 400, 400)
    win.setCoords(-6,-6, 6,6)

    # draw the tree stump
    stump = Rectangle(Point(-1,-6), Point(1,3))
    stump.setFill("brown")
    stump.draw(win)

    # draw the left side of the tree
    downLeftSide = Polygon(Point(-1,-5), Point(-4,-4), Point(-1,-2))
    downLeftSide.setFill("green")
    downLeftSide.draw(win)
    midLeftSide = Polygon(Point(-1,-2), Point(-3.5,0), Point(-1,1))
    midLeftSide.setFill("green")
    midLeftSide.draw(win)
    upLeftSide = Polygon(Point(-1,1), Point(-3,2), Point(-1,3))
    upLeftSide.setFill("green")
    upLeftSide.draw(win)

    # draw the right side of the tree
    downRightSide = downLeftSide.clone()
    downRightSide.move(2,0)
    downRightSide.draw(win)
    
    # close after mouse click
    win.getMouse()
    win.close()
    
main()
