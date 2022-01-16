from tkinter import *
# imports everything related tkinter module

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a contained to hold or contain the widgets


window = Tk()  # this instantiates an instance of a window
window.geometry("690x420")
window.title("Sniper Monkey's first GUI program")

icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

window.config(background="#68228B")

window.mainloop()  # this will place a window on the computer screen and listen for events

