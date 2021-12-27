# function is a block of code which is executed only when it is called
# invoking a function. Helps to prevent repeating code

def hello(name):
    # name in the brackets above is the parameter
    print("Hello " + name)
    print("Have a nice day!")


# if we want to send information to a function, put it in the brackets
hello("Sniper Monkey")
# when you send information to a function, they are called arguments ("Sniper")


# another way to send an argument to the function is like this:
my_name = "Sniper Monkey"

hello(my_name)
# this will give the same output


def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")


# we are sending 3 arguments, so we need 3 parameters in the function
hello("Sniper", "Monkey", "21")
