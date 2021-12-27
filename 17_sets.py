# A set is a collection which is unordered and unindexed. Do not allow duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

# to add the dishes set to the utensils set
utensils.update(dishes)

# or to create a new set containing both sets:
dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)
# a set is faster than a list if you want to check to see if something is within a set


# this also gives the same output:
utensils = {"fork", "spoon", "knife", "knife", "knife"}

for x in utensils:
    print(x)


# to add item to set
utensils.add("napkin")

# to remove and item from the set
utensils.remove("fork")

# to remove all elements in the set
utensils.clear()

# to see what the sets do not have in common
print(utensils.difference(dishes))

# to see what they have in common
print(utensils.intersection(dishes))

