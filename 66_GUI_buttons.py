from tkinter import *

# button = you click it, and then it does stuff

window = Tk()
window.geometry("690x420")
window.title("Sniper Monkey's first GUI program")

icon = PhotoImage(file="peepohappy.png")
window.iconphoto(True, icon)

window.config(background="#68228B")

count = 0
def click():
    global count
    count += 1
    print(count)
    print("You clicked the button. Leave it alone!")


photo = PhotoImage(file="C:\\Users\\ken\\Desktop\\Games\\steam\\profile pictures steam\\sloth stack - copy.png")
button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 15),
                padx=5,
                pady=5,
                relief=RAISED,
                bd=3,
                bg="green",
                activeforeground="black",
                activebackground="green",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
