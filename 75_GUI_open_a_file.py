from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="./",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    print(filepath)
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()
window.geometry("690x420")
window.title("Sniper Monkey's first open file program")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
