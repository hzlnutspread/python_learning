from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex)

    #  or you can just write this

    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("690x420")
window.title("Sniper Monkey's first GUI program")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

button = Button(window, text="sniper monkey", command=click)
button.pack()

window.mainloop()
