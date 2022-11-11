# generator
# functions that return an object that can be iterated over
# good for memory when dealing with large data sets
# yield keyword instead of return

def mygenerator():
    yield 1
    yield 2
    yield 3


g = mygenerator()

value = next(g)  # runs until it reaches the first yield statement and return only 1
print(value)
value = next(g)  # picks up where it left off, will return 2
print(value)
value = next(g)
print(value)

# for i in g:
#     print(i)

# print(list(g))