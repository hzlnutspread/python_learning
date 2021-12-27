# a dictionary is a changeable, unordered collection of unique key:value pairs
# they are fast because they use hashing, which allows us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})  # adds a new key:value pair
capitals.update({"USA": "Las Vegas"})  # changes an existing key:value pair

capitals.pop("China")

print(capitals["Russia"])
print(capitals.get("Poland"))  # use this to see if it exists
print(capitals.keys())  # print only keys
print(capitals.values())  # print only values

print(capitals.items())  # print key:value pairs
for key, value in capitals.items():  # print key:value pairs
    print(key + ": " + value)

capitals.clear()  # removes all key:value pairs
