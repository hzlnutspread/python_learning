# Variable is a container for a value


# 1. a string is a series of characters e.g:
first_name = 'Sniper'
last_name = 'Monkey'
full_name = first_name + " " + last_name


# to find type of a variable:
print(type(full_name))


# 2. An integer is a whole number
age = 23
age = age + 1
# or age += 1
print(age)
print(type(age))


# can only concatenate string to string not int to int
print("your age is: " + age)  # this will not work


# need to do this instead:
print("your age is: " + str(age))


# 3. A float is a decimal number
height = 178.5
print("your height is: " + str(height) + "cm")


# 4. A boolean is a variable that can only store true or false
human = True
print("are you a human: " + str(human))