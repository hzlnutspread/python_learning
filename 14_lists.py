# list is used to store multiple items in a single variable

# to turn this into a list we surround this by square brackets
# each item in a list is called an element
food = ["pizza", "hamburgers", "fries", "calamari", "pasta"]

print(food)


# if we want to print a particular element we need to show the index. For hamburgers:
print(food[1])


# we want to change an element and replace pizza with sushi
food[0] = "sushi"
print(food[0])


# to turn the list into a for loop
for x in food:
    print(x)

# useful functions of lists
food.append("ice cream")
food.remove(food[0])
food.pop()
food.insert(0, "banana")
food.sort()

print(food)



