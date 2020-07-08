from graphics import *

def main():
    win = GraphWin("Value growth calculator", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # draw the interface
    Text(Point(1,3.75), "Initial principal: ").draw(win)
    Text(Point(1,3), "Annual interest rate (in decimal): ").draw(win)
    Text(Point(1,2), "Years of investment: ").draw(win)
    Text(Point(1,1), "The answer is: ").draw(win)
    principal = Entry(Point(2.25, 3.75), 5)
    principal.setText("0.0")
    principal.draw(win)
    apr = Entry(Point(2.25, 3), 5)
    apr.setText("0.0")
    apr.draw(win)
    years = Entry(Point(2.25, 2), 5)
    years.setText("0.0")
    years.draw(win)

    # wait for a mouse click and get values
    win.getMouse()
    principal = float(principal.getText())
    apr = float(apr.getText())

    # calculate and print the answer to the user


    # quit after another click
    win.getMouse()
    win.close()
    
main()
