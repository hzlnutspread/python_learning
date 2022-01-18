from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)             # managed a collection of windows/displays

tab1 = Frame(notebook)                      # new frame for tab 1
tab2 = Frame(notebook)                      # new frame for tab 2
tab3 = Frame(notebook)                      # new frame for tab 3

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")
notebook.pack(expand=True, fill=BOTH)       # expands to fill any space not otherwise used
                                            # fill = fill space on x and y axis

Label(tab1, text="Hello this is tab 1", width=50, height=25).pack()
Label(tab2, text="Hello this is tab 2", width=50, height=25).pack()
Label(tab3, text="Hello this is tab 3", width=50, height=25).pack()


window.mainloop()
