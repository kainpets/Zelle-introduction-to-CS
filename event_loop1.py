# event_loop1.py --- keyboard-driven color changing window

from graphics import *

def main():
    print("Press r, w, g, b to change the color of window\n\
press q to quit.")
    win = GraphWin("Color Window", 500, 500)

    # Event Loop: handle key presses until user pressses the"q" key.
    while True:
        key = win.getKey()
        if key == "q": # loop exit
            break

        # process the key
        if key == "r":
            win.setBackground("pink")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("green")
        elif key == "b":
            win.setBackground("lightblue")

    # exit program
    win.close()

main()
