# tuple is like a list but the collection is ordered and unchangeable
# tuple is used to group together related data

student = ("Sniper Monkey", 21, "male")

print(student.count("Sniper Monkey"))  # how many times does this appear
print(student.index("male"))  # what number in the list is this

for x in student:
    print(x)

if "Sniper Monkey" in student:
    print("Sniper Monkey is here")
