# Walrus operator looks like :=
# assignment expression
# assigns values to variables as part of a larger expression

happy = True
print(happy)

# to combine the two lines we use walrus operator
print(happy := True)

# --------------------------------------------------------------------------------------------------------------------#

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)


# we can rewrite this as the following using walrus operator
foods = list()
while food := input("What food do you like?: ") != "quit":  # the food := input is the assignment portion
    foods.append(food)

