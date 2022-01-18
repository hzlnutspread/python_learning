from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="./",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))


def saveFile():
    file = filedialog.asksaveasfile(initialdir="./",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All file", ".*")
                                    ])
    if file is None:
        return
    # filetext = str(text.get(1.0, END))
    filetext = input("Enter some text: ")  # you can enter in your input in the console. Don't need text area
    file.write(filetext)
    file.close()


def cut():
    print("You cut text")


def copy():
    print("You copy text")


def paste():
    print("You paste text")


window = Tk()

openImage = PhotoImage(file="pizza.png")
saveImage = PhotoImage(file="pizza.png")
exitImage = PhotoImage(file="pizza.png")

window.geometry("690x420")
window.title("Sniper Monkey's first menubar program")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 13))  # adding this to the menu_bar instead of the window
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="open", command=openFile, image=openImage, compound="left")
file_menu.add_command(label="save", command=saveFile, image=saveImage, compound="left")
file_menu.add_separator()
file_menu.add_command(label="exit", command=quit, image=exitImage, compound="left")

edit_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 13))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=cut)
edit_menu.add_command(label="copy", command=copy)
edit_menu.add_command(label="paste", command=paste)

text = Text(window)
text.pack()

window.mainloop()
