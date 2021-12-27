# str.format = optional method that gives users more control when displaying output


# this is the normal inefficient way of printing a line
animal = "cow"
item = "moon"
utensil = "spoon"
weapon = "gun"

print("The " + animal + " jumped over the " + item)

# to print this using the format method we do the following:
print(f"The {animal} jumped over the {item}")

# we can also do this
print("The {2} jumped over the {3}".format(animal, item, utensil,weapon))  # positional arguments if more than 2 variables
print("The {utensil} jumped over the {item}".format(animal="cow", item="moon", utensil="spoon", weapon="gun")) # keyword arguments used here


# even more elegent
text = "The {} jumped over the {}"
print(text.format(animal, item))


# padding and alignments
name = "Sniper"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you.".format(name)) # allocating spaces to the right side of the variable (padding)
print("Hello, my name is {:<10}. Nice to meet you.".format(name)) # right align
print("Hello, my name is {:>10}. Nice to meet you.".format(name)) # left align
print("Hello, my name is {:^10}. Nice to meet you.".format(name)) # center


# formatting numbers
number = 15290

print("The number is {:.2f}".format(number)) # display only the first two digits after the decimal
print("The number is {:,}".format(number)) # puts commas every 1,000
print("The number is {:b}".format(number)) #displays number in binary
print("The number is {:o}".format(number)) # displays number in octal
print("The number is {:x}".format(number)) # displays in hexadecimal
print("The number is {:e}".format(number)) # scientific notation