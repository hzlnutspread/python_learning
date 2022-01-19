# canvas = widget that i used to draw graphs, plots and images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# blue_line = canvas.create_line(0, 0, 500, 500,
#                                fill="blue",
#                                width=3)
# red_line = canvas.create_line(500, 0, 0, 500,
#                               fill="red",
#                               width=3)
# rectangle = canvas.create_rectangle(50, 50, 250, 250,
#                                     fill="purple")
# canvas.create_polygon(250, 0, 500, 500, 0, 500,
#                       fill="yellow",
#                       outline="black",
#                       width=3)
# canvas.create_arc(0, 0, 500, 500,
#                   fill="green",
#                   style=PIESLICE,
#                   start=270,
#                   extent=180)

# this is a pokeball:
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, width=10, start=180)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)

canvas.pack(padx=10, pady=10)

window.mainloop()
