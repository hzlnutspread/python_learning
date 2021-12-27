# keyword arguments = arguments preceded by an identifier when we pass them to a function
# order of arguments don't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last + "!")


# We use keyword arguments to assign each argument to a parameter so that order does not matter
hello(last="Monkey", middle="The", first="Sniper")
