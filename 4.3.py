from graphics import *

def main():
    win = GraphWin()
    win.setCoords(-5,-5, 5,5)
    
    
    face = Oval(Point(-5,-5), Point(5,5))
    face.setOutline("black")
    face.setFill("white")
    face.draw(win)

    leftEye = Oval(Point(-3,3), Point(-1.5,2))
    leftEye.draw(win)
    rightEye = leftEye.get
    
    win.getMouse()
    win.close()
    
main()
