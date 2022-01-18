from tkinter import *


def create_window():
    # new_window = Toplevel()       # Toplevel() = new window on top of the other windows. Linked to a bottom window
    new_window = Tk()               # Tk() = new independent window
    old_window.destroy()            # this will close out of old window


old_window = Tk()
old_window.geometry("690x420")

button = Button(old_window, text="create new window", command=create_window)
button.pack()

old_window.mainloop()
