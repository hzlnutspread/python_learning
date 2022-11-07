# lambda arguments: expression
from functools import reduce

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# def sort_by_y(x):
#     return x[1]
points2D_sorted_by_y = sorted(points2D, key=lambda x: x[1])  # sort by y
points2D_sorted_by_sum = sorted(points2D, key=lambda x: x[0] + x[1])  # sort by sum of the x and y values

print(points2D)
print(points2D_sorted_by_y)
print(points2D_sorted_by_sum)

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

# or this (which is probably easier)
c = [x * 2 for x in a]
print(c)

# filter(func, seq) the func must return boolean
d = [1, 2, 3, 4, 5, 6]
e = filter(lambda x: x % 2 == 0, d)
print(list(e))

# or
f = [x for x in d if x % 2 == 0]
print(f)

# reduce(func, seq)
g = [1, 2, 3, 4, 5, 6]
product_g = reduce(lambda x, y: x * y, g)
print(product_g)