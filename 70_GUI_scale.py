from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees celcius")


window = Tk()

hotimage = PhotoImage(file="pizza.png")
hotLabel = Label(image=hotimage)
hotLabel.pack()

scale = Scale(window,
              from_=200, to=0,          # range
              length=600,               # size
              orient=VERTICAL,          # orientation of scale
              font=("Consolas", 10),
              tickinterval=10,          # adds numeric indicators for value
              showvalue=True,           # hides current value
              resolution=5,             # increment of the slider
              troughcolor="#69EAFF",    # changes colour of trough/slider
              fg="#FF1C00",             # changes colour of the numbers and text
              bg="#111111",             # changes colour of the background
              )
scale.set((scale["from"] - scale["to"])/2 + scale["to"])

scale.pack()

coldimage = PhotoImage(file="pizza.png")
coldLabel = Label(image=coldimage)
coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()