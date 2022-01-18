from tkinter import *
from tkinter import filedialog


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


window = Tk()
window.geometry("690x420")
window.title("Sniper Monkey's first open file program")
icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

text = Text(window)
text.pack()

button = Button(text="save", command=saveFile)
button.pack()

window.mainloop()