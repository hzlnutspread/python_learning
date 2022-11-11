import sys


# usually we would do this
# takes a lot of memory since all the numbers are stored in the list
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(sys.getsizeof(firstn(10000)))


# ----------------------------------

# dont have to save all the numbers inside an array so you save this memory
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(firstn_generator(10000)))