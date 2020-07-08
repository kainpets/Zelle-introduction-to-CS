from graphics import *

def main():
    win = GraphWin()
    win.setCoords(-5,-5, 5,5)
    win.setBackground("gray")
    
    firstCircle = Circle(Point(0,0), 5)
    firstCircle.setOutline("white")
    firstCircle.setFill("white")
    firstCircle.draw(win)
    
    secondCircle = Circle(Point(0,0), 4)
    secondCircle.setOutline("black")
    secondCircle.setFill("black")
    secondCircle.draw(win)
    
    thirdCircle = Circle(Point(0,0), 3)
    thirdCircle.setOutline("blue")
    thirdCircle.setFill("blue")
    thirdCircle.draw(win)
    
    fourthCircle = Circle(Point(0,0), 2)
    fourthCircle.setOutline("red")
    fourthCircle.setFill("red")
    fourthCircle.draw(win)
    
    fifthCircle = Circle(Point(0,0), 1)
    fifthCircle.setOutline("yellow")
    fifthCircle.setFill("yellow")
    fifthCircle.draw(win)

    win.getMouse()
    win.close()
    
main()
