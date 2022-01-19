# grid() = geometry manager that organises widgets in a table-like structure in a parent

from tkinter import *

window = Tk()

titelLabel = Label(window, text="Enter your information", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window, text="First name: ", width=15, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last name: ", bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emilLabel = Label(window, text="Email: ", bg="blue").grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()
