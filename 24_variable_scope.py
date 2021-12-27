# scope = region that a variable is recognised
# a variable is only available from inside the region it is created
# A global and locally scoped version of a variable can be created


name = "Monkey"  # global variable has global scope inside and outside a function


def display_name():
    name = "Sniper"  # local variable has local scope because it is defined inside a function
    print(name)


display_name()
print(name)

# if you use a variable inside a function, we will first use local variable inside of function first

# LEGB = Local, enclosed, global, built-in
