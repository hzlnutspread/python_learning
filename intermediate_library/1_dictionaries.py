# key-value pairs, unordered, mutable
dictionary1 = {"name": "Max", "age": 28, "city": "New York"}

dictionary2 = dict(name="Mary", age=27, city="Boston")

# accessing values
value = dictionary1["name"]

# adding pairs. Get overridden if the key is identical
dictionary1["email"] = "max@xyz.com"

# deleting pairs
# dictionary1.pop("age") or
# dictionary1.popitem() which removes last pair or
del dictionary1["age"]

# check if key in dict
# try:
#     print(dictionary1["name"])
# except:
#     print("ERROR")
# or...
if "name" in dictionary1:
    print(dictionary1["name"])

# looping through dict
for key in dictionary1:
    print(key)

for value in dictionary1.values():
    print(value)

for key, value in dictionary1.items():
    print(key, value)

# copying dicts
# dictionary1_copy = dictionary1 is incorrect as both references will now point to the same object in the heap/memory



