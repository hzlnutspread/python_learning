# reduce() = applies a function of our choosing to an iterable and reduces it to a single cumulative value.
# performs function on first two elements of our iterable and repeats the process until 1 a single value remains
# reduce(function, iterable)


import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y,: x + y, letters)
print(word)


factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,: x * y, factorial)
print(result)