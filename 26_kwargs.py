# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

# args = varying amount of positional arguments and pack them into a tuple
# kwargs = varying amount of keyword arguments and pack them into a dictionary


def hello(first, last):
    print("Hello " + first + " " + last)


# we get an unexpected keyword argument parameter. To solve this we use kwargs below
hello(first="Sniper", middle="The", last="Monkey")


def hello(**kwargs):
    # to access value in a dictionary use dictionary_name['key']
    print("Hello " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])


hello(first="Sniper", middle="The", last="Monkey")


# or we can do this using a for loop
def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Sniper", middle="The", last="Monkey")