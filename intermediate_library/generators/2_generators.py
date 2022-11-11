# without the next() call, nothing will be printed.
# once the "value = next(cd) is added, then we get "Starting" printed
# the program stops once it reaches the first yield statement so printing value will give num
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))