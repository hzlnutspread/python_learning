#

from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="This is an info message box", message="You are a monkey")
    messagebox.showwarning(title="WARNING!", message="You are a monkey!")
    messagebox.showerror(title="ERROR!", message="You are a monkey!")


    if messagebox.askokcancel(title="Ask ok cancel", message="You are a monkey"):
        print("You really are a monkey")
    else:
        print("But you look like a monkey")


    if messagebox.askretrycancel(title="Ask retry cancel", message="You are a monkey"):
        print("You really are a monkey")
    else:
        print("But you look like a monkey")


    if messagebox.askyesno(title="Ask yes no", message="Are you a monkey?"):
        print("Yes, we are all a monkey")
    else:
        print("But you look like a monkey omegaLUL")


    answer = messagebox.askquestion(title="Ask question", message="Are you a monkey?")
    if answer == "yes":
        print("Yes, we are all a monkey")
    else:
        print("But you look like a monkey")


    answer = messagebox.askyesnocancel(title="ask yes no cancel", message="Are you a monkey?", icon='warning')
    if answer:
        print("Yes, we are all a monkey")
    elif answer == False:
        print("But you look like a monkey")
    else:
        print("That's kinda sus...I think you are monkey")


window = Tk()

button = Button(window, command=click, text="click me!")
button.pack()

window.mainloop()
