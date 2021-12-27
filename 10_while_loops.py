# while loop is a statement that will execute its block of cute as long as its condition remains true


while 1 == 1:
    print("Help! I'm stuck in a loop!")
    break


# the length of the name is 0 until the user inputs a name
# when user inputs the name the while loop breaks and the block of code under the while loop is ignored
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)


# another way of writing this is:
# while not name: means if name has no value then run the block of code under the while loop
name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name)
