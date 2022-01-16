# zip(*iterables) = aggregate elements from two or more iterable (list, tuple, sets, etc.)
# creates a zip object with paired elements stored in tuples for each element


usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

# we want to zip elements from each iterable together
# each pair will be stored as a tuple in a zip object

users = dict(zip(usernames, passwords))
# zip objects are iterable so we can use them in a for loop

print(type(users))
for key, value in users.items():
    print(key + ": " + value)


#-----------------------------------------------------------------------------------------------------------------------
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = list(zip(usernames, passwords, login_date))

print(type(users))
for i in users:
    print(i)
