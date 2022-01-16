from tkinter import *


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()  # this instantiates an instance of a window
window.geometry("690x690")
window.title("Sniper Monkey's GUI")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)
window.config(background="#68228B")


entry = Entry(window,
              font=("Arial", 30),
              fg="green",
              bg="black",
              show="*")
entry.insert(0, "Sniper Monkey")  # default text inserted into entry box
entry.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()  # this will place a window on the computer screen and listen for events
