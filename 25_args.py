# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(num1, num2):
    sum = num1 + num2
    return sum


print(add(1, 2, 3))
# we are given error that add() takes 2 positional arguments when 3 were given


# to go around this we can do the follow:
def add(*args):
    sum = 0
    args = list(args)   # if we want to edit the tuple we must cast to a list
    args[0] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))
