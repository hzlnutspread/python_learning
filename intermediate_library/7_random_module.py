# random module
import random

mylist = list("ABCDEFGH")
print(mylist)

a = random.sample(mylist, 3)
print(a)

b = random.choices(mylist, k=3)  # elements can be chosen multiple times
print(b)

shufflelist = list("ABCDEFGH")
random.shuffle(shufflelist)
print(shufflelist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))