# thread = a flow of execution. Like a separate order of instructions.
# each thread takes a turn running to achieve concurrency
# GIL = global interpreter lock, allows only one thread to hold control of interpreter at any one time

# CPU bound = program/task spends most of its time waiting for internal events (CPU intensive). Multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping). Multithreading


import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drink coffee")


def cram_study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=cram_study, args=())
z.start()
# these three threads will run at the same time (concurrently not parallel) and make it run faster

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# cram_study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())