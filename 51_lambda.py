# lambda functions = function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression (
# useful for one use or short period of time
# syntax = lambda parameters: expression

def double(x):
    return x * 2


print(double(5))

# we can write the same above as follow:

double = lambda x: x * 2
print(double(5))

# if we have two parameters

double = lambda x: x * 2
multiply = lambda x, y: x * y

print(multiply(5, 6))

# if we have three parameters

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

print(add(13, 42, 55))

# can also be done with things like strings

full_name = lambda first_name, last_name: first_name + " " + last_name

print(full_name("Sniper", "Monkey"))

# to check someone's age

age_check = lambda age: True if age >= 18 else False

print(age_check(2))