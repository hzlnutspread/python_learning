# radio buttons = similar to checkbox but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?)")


window = Tk()

pizzaimage = PhotoImage(file="pizza.png")
hamburgerimage = PhotoImage(file="pizza.png")
hotdogimage = PhotoImage(file="pizza.png")
food_images = [pizzaimage, hamburgerimage, hotdogimage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],             # adds text to radio buttons
                              variable=x,                   # group buttons together if they share same variable
                              value=index,                  # assigns each radiobutton a different value
                              padx=25,
                              font=("Impact", 50),
                              image=food_images[index],     # adds image to radio button
                              compound="left",              # adds image and text
                              indicatoron=False,            # eliminates circle indicators
                              width=500,                    # sets width of radio buttons
                              command=order,                # set command of radio button to function
                              anchor="w")                   # aligns the text to the left side
    radiobutton.pack()

window.mainloop()
