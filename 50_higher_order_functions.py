# higher Order functions = A function that either:
# accepts a function as an argument or
# returns a function
# in python, functions are also treated as objects


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):  # this is the higher order function. We pass either loud() or quiet() into the hello() function
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)


# ---------------------------------------------------------------------------------------------------------------------#

def divisor(x):  # this is the higher order function because it returns a function (dividend)
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)  # program begins here
print(divide(10))

# the above starts at divide = divisor(2). Here we are assigning x = 2
# We skip the def dividend(y): because we have not called it yet and immediately return dividend
# This means we have now the dividend function assigned to variable name divide.
# now we call print(divide(10)) which means dividend(10) and we run the function
# from the first line, x = 2 and from divide(10) y will equal 10.
# 10/2 = 0.5
