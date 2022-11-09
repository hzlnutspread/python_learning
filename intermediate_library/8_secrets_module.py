# secrets module
import secrets

a = secrets.randbelow(10)
print(a)

b = secrets.randbits(4)
# 4 bits = 4 different random binary values eg 1010. 1111 = 15
print(b)

mylist = list("ABCEDFG")
c = secrets.choice(mylist)
print(c)