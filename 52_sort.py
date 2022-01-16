# sort() method = used with lists
# sort() function = used with iterables


# using the sort() method
students = ["Squidware", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
students.sort(reverse=True)

for i in students:
    print(i)


# using the sort() function for example if its a tuple and not a list
students = ("Squidware", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

sorted_students = sorted(students, reverse=True)  # returns a list but accepts iterable as an argument

for i in sorted_students:
    print(i)


# a list of tuples
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

grade = lambda grades: grades[1]
students.sort(key=grade)

for i in students:
    print(i)


# sorting a tuple of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda age: age[2]
sorted_lists = sorted(students, key=age)

for i in sorted_lists:
    print(i)