from tkinter import *
from Class_ball import *
import time



window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


volley_ball = Ball(canvas, 75, 75, 100, 13, 6, "purple")
tennis_ball = Ball(canvas, 12, 12, 50, 3, 9, "yellow")
basket_ball = Ball(canvas, 240, 240, 125, 8, 7, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()