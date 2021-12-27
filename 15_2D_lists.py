# a 2D list is a list of lists or multidimensional lists

# we want to add all of these lists into one list
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(food)
# this prints the lists within a list


# to access one of the lists we index the list and then index it again to get an element within that list
print(food[0][1])