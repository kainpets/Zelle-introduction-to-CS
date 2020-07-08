from graphics import *

def main():
    win = GraphWin()
    win.setCoords(-5,-5, 5,5)
    
    # draw the contour of the face
    face = Oval(Point(-5,-5), Point(5,5))
    face.setOutline("black")
    face.setFill("beige")
    face.draw(win)

    # draw the ears
    rightEar = Polygon(Point(4,3), Point(3.5,3.5), Point(4,4.25))
    rightEar.draw(win)
    leftEar = Polygon(Point(-4,3), Point(-3.5,3.5), Point(-4,4.25))
    leftEar.draw(win)
    leftEar.setFill("grey")
    rightEar.setFill("grey")

    # draw the eyes
    leftEye = Oval(Point(-3,3), Point(-1.5,2))
    leftEye.draw(win)
    rightEye = leftEye.clone()
    rightEye.move(4,0)
    rightEye.draw(win)
    rightEye.setFill("blue")
    leftEye.setFill("blue")

    # draw the nose
    nose = Polygon(Point(-0.75,2), Point(-0.3,1), Point(0.25,2))
    nose.draw(win)
    nose.setFill("grey")

    # draw the mouth
    mouth = Oval(Point(-3,-2), Point(3,-1))
    mouth.draw(win)
    mouth.setFill("red")

    # close after mouse click
    win.getMouse()
    win.close()
    
main()
