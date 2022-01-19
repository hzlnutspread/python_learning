from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 5)


def move_left(event):
    label.place(x=label.winfo_x() - 5, y=label.winfo_y())


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 5)


def move_right(event):
    label.place(x=label.winfo_x() + 5, y=label.winfo_y())


window = Tk()
window.geometry("690x690")

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

myimage = PhotoImage(file="pizza.png")
label = Label(window,
              image=myimage,
              bg="red")
label.place(x=0, y=0)

window.mainloop()
