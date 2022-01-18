# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *


def submit():
    user_input = text.get("1.0", END)
    print(user_input)


window = Tk()
window.geometry("690x420")
window.title("Sniper Monkey's first GUI program")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

text = Text(window,
            bg="beige",
            font=("Ink Free", 18),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()


submitButton = Button(window, text="Monkey", command=submit)
submitButton.pack()

window.mainloop()
