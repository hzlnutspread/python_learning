from tkinter import *

# label = an area widget that holds text/image within a window

window = Tk()  # this instantiates an instance of a window
window.geometry("690x690")
window.title("Sniper Monkey's GUI")

icon = PhotoImage(file="peepohappy.png")
icon_photo = window.iconphoto(True, icon)

window.config(background="#68228B")

label_photo = PhotoImage(file="C:\\Users\\ken\\Desktop\\Games\\steam\\profile pictures steam\\sloth stack - copy.png")
label = Label(window,
              text="Hello Sniper Monkey",
              font=("Arial", 25, "bold"),
              fg="white",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=label_photo,
              compound="bottom")
label.pack()  # defaults to top center
# label.place(x=0, y=0)  # use coordinates to place the label at specific places



window.mainloop()  # this will place a window on the computer screen and listen for events
