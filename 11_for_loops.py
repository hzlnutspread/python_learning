import time

# for loop = will execute its block of code a limited amount of time

# for loop = limited
# while loop = unlimited

# if we want  to create a for loop to count up to 10
# use for index (i)
for i in range(10):
    i += 1
    print(i)

for i in range(10, 51, 2):
    print(i)


# for loops iterate through anything iterable, like strings, numbers and other collections
name = "Sniper Monkey"
for i in name:
    print(i)


# simulate countdown and print at 0
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year")
