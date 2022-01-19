from tkinter import *


def doSomething(event):
    print("Mouse coordinate: " + str(event.x) + "," + str(event.y))


window = Tk()

window.bind("<Button-1>", doSomething)          # left click
window.bind("<Button-2>", doSomething)          # middle click
window.bind("<Button-3>", doSomething)          # right click
window.bind("<ButtonRelease>", doSomething)     # when you let go of any mouse click
window.bind("<Enter>", doSomething)             # shows coordinates of where cursor entered the window
window.bind("<Leave>", doSomething)             # shows coordinates of where cursor left the window
window.bind("<Motion>", doSomething)            # Where the cursor moved only when it changes

window.mainloop()
