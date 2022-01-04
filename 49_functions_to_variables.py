# how to assign a function to a variable

def hello():
    print("Hello")


hello()  # the parentheses after a function's name is the portion that will call the function

print(hello)  # this prints the memory address of the function = where function is located within computer memory. Hexa.

hi = hello  # we assign the function a new variable name
hi()
# the hello() function now has two names. Hello() and hi().

say = print
say("whoa! I can't believe this works! :o")

# not sure when you'd need to do this but you can lol
