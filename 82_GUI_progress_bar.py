from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.50)
        progress_bar["value"] += (speed/GB) * 100
        download += speed
        percent.set(str(int(download/GB*100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GBs completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10, padx=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()

task_label = Label(window, textvariable=text)
task_label.pack()

button = Button(window, text="download", command=start)
button.pack(pady=10)

window.mainloop()
